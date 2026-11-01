#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汉语启蒙三套扩充卡 · 发布前质量校验。

用法：
    python3 扩充/质量校验.py            # 静态审计（数据+构建产物）
    python3 扩充/质量校验.py --browser [发布目录]   # 浏览器交互回归 + 逐卡截图
    python3 扩充/质量校验.py --all  [发布目录]      # 两者都跑

静态审计覆盖：卡数/重复 key/1000字归属/拼音声调对拍/拼音与声调一致性/
story·部件词行长/家族成员全库零重叠/韵语行末韵脚一致且互不重复/ART·GLYPHS 覆盖。
浏览器回归覆盖：页面零 JS 错误、卡数、翻页环绕、「变！」揭晓、组切换、
家族成员网格、韵语行末高亮、手机/窄屏/宽屏布局、进度保存与恢复、逐卡截图。
"""
import hashlib
import http.server
import functools
import json
import re
import subprocess
import sys
import tempfile
import threading
import time
import pathlib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent       # 汉语启蒙卡集/
PARENT = ROOT.parent                                 # 孩子/
sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(ROOT))

DECKS = [
    # (文件, 发布名, 期望卡数, kind)
    ("汉语启蒙_会意字卡.html", "huiyi", 24, "magic"),
    ("汉语启蒙_部首家族卡.html", "bushou", 19, "family"),
    ("汉语启蒙_韵语与声音卡.html", "yunyu", 24, "shengyin"),
]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

problems = []
notes = []


def check(cond, msg):
    if not cond:
        problems.append(msg)
    return cond


# ---------------------------------------------------------------- 静态审计

def load_html(path):
    return Path(path).read_text(encoding="utf-8")


def extract(html, var):
    m = re.search(rf"const {var} = (\[.*?\]|\{{.*?\}});\n", html, re.S)
    if not check(m is not None, f"{Path(html).name if isinstance(html,Path) else 'html'}: 找不到 const {var}"):
        return None
    return json.loads(m.group(1))


def static_audit():
    ziku = load_module(PARENT / "识字卡片_1000字" / "字库1000.py", "qa_ziku")
    S = set()
    for g in ziku.GROUPS:
        for it in g["chars"]:
            for c in (list(it) if isinstance(it, tuple) else
                      [it.get("char", it) if isinstance(it, dict) else it]):
                S.add(c)
    py = json.loads((PARENT / "识字卡片_1000字" / "拼音表1000.json").read_text(encoding="utf-8"))

    # 象形字卡必须与扩充前逐字节一致
    before = {}
    try:
        for line in Path("/tmp/before_hash.txt").read_text().splitlines():
            parts = line.split()
            if len(parts) >= 2:
                before[Path(parts[1]).name] = parts[0]
    except Exception:
        pass
    if before:
        cur = hashlib.sha256((ROOT / "汉语启蒙_象形字卡.html").read_bytes()).hexdigest()
        check(cur == before.get((ROOT / "汉语启蒙_象形字卡.html").name), "象形字卡哈希与扩充前不一致")

    deck_data = {}
    for fname, pub, n_expect, kind in DECKS:
        html = load_html(ROOT / fname)
        cards = extract(html, "CARDS")
        groups = extract(html, "GROUPS")
        glyphs = extract(html, "GLYPHS")
        art = extract(html, "ART")
        if cards is None:
            continue
        deck_data[pub] = dict(cards=cards, groups=groups, glyphs=glyphs, art=art)
        check(len(cards) == n_expect, f"{pub}: 卡数 {len(cards)} ≠ {n_expect}")
        keys = [c["key"] for c in cards]
        check(len(keys) == len(set(keys)), f"{pub}: 卡 key 重复 {[k for k in keys if keys.count(k)>1]}")
        check(len(art) > 0 and all(k in art for k in keys), f"{pub}: 有卡缺插画 {[k for k in keys if k not in art]}")

        if kind == "magic":
            HUIYI_EXIST = {"明", "林", "森", "从", "众", "休", "尖", "尘", "看", "坐", "灭", "歪", "鸣", "泪"}
            for c in cards:
                r = c["result"]
                check(len(c["story"]) <= 24, f"{pub}:{r} story 超长")
                check(len(c["parts"]) <= 3, f"{pub}:{r} 部件超过 3")
                for p in c["parts"] + [[r]]:
                    check(p[0] in glyphs, f"{pub}:{r} 字形缺 {p[0]}")
                for p in c["parts"]:
                    check(len(p[1]) <= 4, f"{pub}:{r} 部件词过长 {p[1]}")
                if r in HUIYI_EXIST:
                    continue  # 旧卡（已上线、用户已核）：只做结构与字形回归
                check(r in S, f"{pub}:{r} 不在 1000 字全集")
                check(c["pinyin"] == py.get(r, {}).get("pinyin") and c["tone"] == py.get(r, {}).get("tone"),
                      f"{pub}:{r} 拼音/声调不符 {c['pinyin']}/{c['tone']} vs {py.get(r)}")
                for p in c["parts"]:
                    check(p[0] in S, f"{pub}:{r} 部件 {p[0]} 不在 1000 字全集")
            huiyi_new = {"好", "双", "品", "掰", "灶", "岩", "晶", "朋", "出", "男"}
            got = {c["result"] for c in cards} - HUIYI_EXIST
            check(got == huiyi_new, f"huiyi: 新卡集合不符 {sorted(got)}")

        if kind == "family":
            FAMILY_EXIST = {"氵", "木", "口", "亻", "艹", "扌", "日", "女", "鸟", "足"}
            members_all = []
            for c in cards:
                rad = c["radical"]
                members_all += [m[0] for m in c["members"]]
                check(rad in glyphs, f"{pub}: 字形缺部首 {rad}")
                check(c["key"] in art, f"{pub}:{rad} 缺徽章插画")
                check(3 <= len(c["members"]) <= 7, f"{pub}:{rad} 成员数异常 {len(c['members'])}")
                for m in c["members"]:
                    check(m[0] in glyphs, f"{pub}:{rad} 字形缺 {m[0]}")
                    check(len(m[1]) <= 4, f"{pub}:{rad} 成员词过长 {m[1]}")
                    if rad not in FAMILY_EXIST:  # 旧家族成员含 1000 字集外的已上线字（唱/她/鸣/踢）
                        check(m[0] in S, f"{pub}:{rad} 成员 {m[0]} 不在 1000 字全集")
            dups = sorted({m for m in members_all if members_all.count(m) > 1})
            check(not dups, f"{pub}: 家族成员重复 {dups}")
            rads = [c["radical"] for c in cards]
            check(len(rads) == len(set(rads)), f"{pub}: 部首重复 {rads}")
            # 现有 10 家族成员固定在位（回归保护）
            must = {"氵": ["江","河","海","洗","游","沙","汗"], "木": ["树","林","森","桌","桥","椅"],
                    "口": ["吃","喝","叫","唱","吹","听"], "亻": ["你","他","们","休"],
                    "艹": ["花","草","苗","菜","蓝"], "扌": ["打","拉","推","拍","抱","找"],
                    "日": ["早","晚","明","晴","时"], "女": ["妈","奶","妹","她","娃","好"],
                    "鸟": ["鸡","鸭","鹅","鸦","鸣"], "足": ["跑","跳","踢","路"]}
            byrad = {c["radical"]: [m[0] for m in c["members"]] for c in cards}
            for rad, mem in must.items():
                check(rad in byrad, f"{pub}: 原家族 {rad} 丢失")
                if rad in byrad:
                    check(byrad[rad] == mem, f"{pub}:{rad} 原成员被改动 {byrad[rad]} vs {mem}")

        if kind == "shengyin":
            TM = {"ā":"a","á":"a","ǎ":"a","à":"a","ē":"e","é":"e","ě":"e","è":"e","ī":"i","í":"i","ǐ":"i",
                  "ì":"i","ō":"o","ó":"o","ǒ":"o","ò":"o","ū":"u","ú":"u","ǔ":"u","ù":"u",
                  "ǖ":"ü","ǘ":"ü","ǚ":"ü","ǜ":"ü","ü":"ü"}

            def base(p):
                return "".join(TM.get(c, c) for c in p.lower() if c.isalpha())
            INIT = ["zh","ch","sh","b","p","m","f","d","t","n","l","g","k","h","j","q","x","r","z","c","s"]

            def final_of(p):
                s = base(p)
                if not s:
                    return "?"
                if s[0] in "yw":
                    f = s[1:] if len(s) > 1 else ""
                    if s[0] == "y" and f.startswith("u"):
                        f = "ü" + f[1:]
                else:
                    f = s
                    for i in INIT:
                        if s.startswith(i) and len(s) > len(i):
                            f = s[len(i):]
                            break
                f = f.replace("ü", "v")
                for a, b in (("iu","iou"),("ui","uei"),("un","uen")):
                    f = f.replace(a, b)
                f = {"iou":"iu","uei":"ui","uen":"un"}.get(f, f)
                return f.replace("v", "ü")

            def rhyme_family(p):
                """十三辙式并韵：去介音 i/u/ü，ao/iao 一辙、a/ua 一辙、ang/iang/uang 一辙。"""
                f = final_of(p)
                while f and f[0] in "iuü" and len(f) > 1:
                    f = f[1:]
                return f

            verses = [c for c in cards if c["type"] == "verse"]
            games = [c for c in cards if c["type"] == "game"]
            check(len(verses) == 14 and len(games) == 10, f"{pub}: 韵语 {len(verses)} / 游戏 {len(games)} ≠ 14/10")
            new_families = []
            for vi, v in enumerate(verses):
                last = [re.search(r"([\u4e00-\u9fff])[，。；！？]?$", ln).group(1) for ln in v["lines"]]
                fams = [rhyme_family(py[ch]["pinyin"]) for ch in last]
                check(len(v["lines"]) <= 4, f"{pub}:{v['title']} 超过 4 行")
                for ln in v["lines"]:
                    check(len(ln) <= 12, f"{pub}:{v['title']} 行超长 {ln}")
                check(v["key"] in art, f"{pub}:{v['title']} 缺插画")
                if vi < 8:
                    # 旧韵语（已上线）：AABA 等格局——主韵辙须覆盖过半行末字
                    main = max(set(fams), key=fams.count)
                    check(fams.count(main) * 2 >= len(fams), f"{pub}:{v['title']} 旧韵语主韵辙不足 {list(zip(last, fams))}")
                    continue
                # 新韵语：每行末字同辙、6 首互不同辙、用字全在 1000 字集
                check(len(set(fams)) == 1, f"{pub}:{v['title']} 韵脚不齐 {list(zip(last, fams))}")
                new_families.append(fams[0])
                for ch in "".join(v["lines"]):
                    if "\u4e00" <= ch <= "\u9fff":
                        check(ch in S, f"{pub}:{v['title']} 用字 {ch} 不在 1000 字全集")
            check(len(set(new_families)) == 6, f"{pub}: 6 首新韵语韵辙重复 {new_families}")
            covered_old = {"ao", "iao", "a", "ua", "ou", "u", "i", "ian", "ang", "uang"}
            check(not (set(new_families) & covered_old), f"{pub}: 新韵语与旧韵辙撞车 {set(new_families)}")
            for gi, g in enumerate(games):
                check(len(g["steps"]) == 4, f"{pub}:{g['title']} 步数 {len(g['steps'])} ≠ 4")
                check(g["key"] in art, f"{pub}:{g['title']} 缺插画")
                if gi >= 6:  # 只对新增 4 个游戏做用字约束（现有 6 个游戏提示语本就含集合外用字）
                    for ch in "".join(g["steps"]):
                        if "\u4e00" <= ch <= "\u9fff":
                            check(ch in S, f"{pub}:{g['title']} 用字 {ch} 不在 1000 字全集")
    # 家族成员与韵语用字跨套互不影响（无全局唯一约束），但家族表打印出来供人工复核
    if "bushou" in deck_data:
        fam = {c["radical"]: [m[0] for m in c["members"]] for c in deck_data["bushou"]["cards"]}
        notes.append("家族总表: " + json.dumps(fam, ensure_ascii=False))
    print("静态审计：" + ("发现问题 " + str(len(problems)) if problems else "全部通过 ✓"))
    return deck_data


def load_module(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- 浏览器回归

def browser_audit(publish_dir, deck_data):
    import websocket
    publish_dir = Path(publish_dir).resolve()
    shot_dir = Path("/tmp/qa_shots")
    shot_dir.mkdir(exist_ok=True)

    server = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(http.server.SimpleHTTPRequestHandler,
                                            directory=str(publish_dir)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    bp = []
    with tempfile.TemporaryDirectory() as profile:
        browser = subprocess.Popen(
            [CHROME, "--headless=new", "--no-first-run", "--disable-gpu",
             "--remote-debugging-port=0", "--remote-allow-origins=*",
             f"--user-data-dir={profile}", "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            portfile = pathlib.Path(profile) / "DevToolsActivePort"
            for _ in range(100):
                if portfile.exists():
                    break
                time.sleep(.05)
            port = int(portfile.read_text().splitlines()[0])
            pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
            page = next(p for p in pages if p["type"] == "page")
            ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=15)
            serial = [0]

            def cmd(method, params=None):
                serial[0] += 1
                ws.send(json.dumps({"id": serial[0], "method": method, "params": params or {}}))
                while True:
                    r = json.loads(ws.recv())
                    if r.get("id") == serial[0]:
                        if "error" in r:
                            raise RuntimeError(r["error"])
                        return r.get("result", {})

            def evaluate(expr):
                res = cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                               "awaitPromise": True})
                if "exceptionDetails" in res:
                    raise RuntimeError(json.dumps(res["exceptionDetails"])[:400])
                return res.get("result", {}).get("value")

            # JS 错误收集走页面内 window.onerror（避免与 cmd 抢同一 CDP 套接字）
            cmd("Page.enable"); cmd("Runtime.enable")

            base = f"http://127.0.0.1:{server.server_port}/"

            def visit(path, width=390, height=844, mobile=True, dsf=3):
                cmd("Emulation.setDeviceMetricsOverride",
                    {"width": width, "height": height, "deviceScaleFactor": dsf, "mobile": mobile})
                cmd("Page.navigate", {"url": base + path})
                for _ in range(160):
                    ready = evaluate("document.readyState === 'complete'")
                    if ready and evaluate(f"location.pathname.endsWith({json.dumps('/'+path.split('?')[0])})"):
                        evaluate("window.__qaerrs=[];window.onerror=function(m,s,l,c){(window.__qaerrs=window.__qaerrs||[]).push(m+' @'+l)}")
                        time.sleep(.15)
                        return
                    time.sleep(.05)
                raise RuntimeError(f"页面未加载: {path}")

            def shot(name):
                r = cmd("Page.captureScreenshot", {"format": "png"})
                (shot_dir / f"{name}.png").write_bytes(__import__("base64").b64decode(r["data"]))

            def errs():
                try:
                    return evaluate("window.__qaerrs || []")
                except RuntimeError:
                    return ["<evaluate 失败>"]

            def layout_expr():
                return ("(() => { const card=document.querySelector('.gallery .stage .card-svg, .gallery .stage .card');"
                        "const nav=document.querySelector('.gallery .bar, .gallery .controls');"
                        "return {overflow:document.documentElement.scrollWidth>innerWidth+1,"
                        "overlap:!!card&&!!nav&&card.getBoundingClientRect().bottom>nav.getBoundingClientRect().top+1};})()")

            new_idx = {"huiyi": list(range(14, 24)), "bushou": list(range(10, 19)),
                       "yunyu": list(range(8, 14)) + list(range(20, 24))}

            def jump(i):  # 绝对跳转到第 i 张卡（go 是相对步进，别用）
                evaluate(f"state.i={i}; state.revealed=false; render()")

            for fname, pub, n_expect, kind in DECKS:
                visit(pub + ".html?from=hub")
                evaluate("localStorage.clear()")
                visit(pub + ".html?from=hub")
                check(evaluate("CARDS.length") == n_expect, f"{pub}: 页面 CARDS {evaluate('CARDS.length')}≠{n_expect}")
                home = evaluate("!!document.querySelector('a.home-btn') && document.querySelector('a.home-btn').getBoundingClientRect().width>0")
                check(home, f"{pub}: 手机端首页按钮不可达")
                check(not evaluate(layout_expr())["overflow"], f"{pub}: 手机横向溢出")

                # 翻页环绕 + 进度
                evaluate("go(-1)")
                check(evaluate("state.i") == n_expect - 1, f"{pub}: go(-1) 未环绕")
                evaluate("go(1)"); evaluate("go(1)")
                check(evaluate("state.i") == 1, f"{pub}: go(1) 步进错误")
                last = evaluate("JSON.parse(localStorage.getItem('hz.last')||'null')")
                check(last and last.get("id") == pub, f"{pub}: 进度未写入 hz.last")
                saved = evaluate(f"JSON.parse(localStorage.getItem('hz.deck.{pub}')||'null')")
                check(saved and saved.get("i") == 1, f"{pub}: 卡2 未存 hz.deck")

                if kind == "magic":
                    jump(14)             # 第一张新卡：好
                    check(evaluate("CARDS[state.i].result") == "好", f"{pub}: 索引14 不是「好」")
                    check("变！" in evaluate("document.getElementById('primaryBtn').textContent"),
                          f"{pub}: 主按钮不是「变！」")
                    wrap_html = evaluate("document.getElementById('cardWrap').innerHTML")
                    hidden_paths = len(re.findall(r"<path", wrap_html))
                    check("先猜一猜" in wrap_html, f"{pub}: 未揭晓态没有「先猜一猜」提示")
                    evaluate("document.getElementById('primaryBtn').click()")
                    time.sleep(.1)
                    now = evaluate("document.getElementById('cardWrap').innerHTML")
                    story = evaluate("CARDS[state.i].story")
                    check("先猜一猜" not in now, f"{pub}: 点击后未揭晓")
                    check(story in now, f"{pub}: 揭晓后没有字的故事")
                    check("收起来" in evaluate("document.getElementById('primaryBtn').textContent"),
                          f"{pub}: 揭晓后按钮未变「收起来」")
                    n_path = len(re.findall(r"<path", now))
                    check(n_path > hidden_paths, f"{pub}: 揭晓画面插画未增加 path {hidden_paths}->{n_path}")
                    evaluate("document.getElementById('primaryBtn').click()")  # 收起，恢复原状
                    time.sleep(.05)
                    check("先猜一猜" in evaluate("document.getElementById('cardWrap').innerHTML"),
                          f"{pub}: 二次点击未收起")

                if kind == "family":
                    jump(10)             # 第一张新家族：虫
                    check(evaluate("CARDS[state.i].radical") == "虫", f"{pub}: 索引10 不是虫家族")
                    inner = evaluate("document.getElementById('cardWrap').innerHTML")
                    mems = evaluate("CARDS[state.i].members.map(m => m[0])")
                    miss = [m for m in mems
                            if evaluate(f"GLYPHS[{json.dumps(m)}].d.slice(0,30)") not in inner]
                    check(not miss, f"{pub}: 成员字形未渲染 {miss}")
                    check(inner.count("<circle") >= 2, f"{pub}: 徽章未渲染")

                if kind == "shengyin":
                    jump(8)              # 新韵语第一首：小白兔
                    check(evaluate("CARDS[state.i].title") == "小白兔白又白", f"{pub}: 索引8 不是小白兔")
                    inner = evaluate("document.getElementById('cardWrap').innerHTML")
                    check("<tspan" in inner, f"{pub}: 韵脚高亮缺失")
                    tspans = re.findall(r"<tspan[^>]*>([^<]+)</tspan>", inner)
                    want_ends = [re.search(r"([一-鿿])[，。；！？]?$", ln).group(1)
                                 for ln in evaluate("CARDS[state.i].lines")]
                    check(tspans == want_ends, f"{pub}: 高亮字 {tspans} ≠ 行末字 {want_ends}")
                    jump(20)
                    check(evaluate("CARDS[state.i].type") == "game", f"{pub}: 索引20 不是游戏")
                    steps = evaluate("CARDS[state.i].steps.length")
                    check(steps == 4, f"{pub}: 游戏步数 {steps} ≠ 4")
                    n_groups = evaluate("GROUPS.length")
                    check(n_groups == 2, f"{pub}: 组数 {n_groups} ≠ 2")
                    evaluate("jumpTo(1)")
                    check(evaluate("CARDS[state.i].type") == "game", f"{pub}: 切组未跳到游戏")

                # 宽屏桌面模式
                visit(pub + ".html", width=1440, height=900, mobile=False, dsf=1)
                desk = evaluate("!!document.querySelector('.desk-top')")
                check(desk, f"{pub}: 宽屏桌面版未出现")
                if kind == "magic":
                    check("变！" in evaluate("document.getElementById('deskState').textContent"),
                          f"{pub}: 桌面模式未显示「变！」")
                    evaluate("document.getElementById('deskCenter').click()")
                    time.sleep(.1)
                    check("收起来" in evaluate("document.getElementById('deskState').textContent"),
                          f"{pub}: 桌面模式点击未揭晓")

                # 逐张新卡截图（手机视口）
                visit(pub + ".html")
                for i in new_idx[pub]:
                    if i >= n_expect:
                        continue
                    jump(i)
                    time.sleep(.08)
                    if kind == "magic":
                        evaluate("if(!state.revealed){document.getElementById('primaryBtn').click()}")
                        time.sleep(.05)
                    shot(f"{pub}_{i:02d}_" + evaluate(
                        "CARDS[state.i].result || CARDS[state.i].radical || CARDS[state.i].title"))
                # 整套网格视图
                visit(pub + ".html?mode=grid", width=1440, height=2400, mobile=False, dsf=1)
                time.sleep(.4)
                shot(f"{pub}_grid")
                got_errs = errs()
                check(not got_errs, f"{pub}: 浏览器错误 {got_errs[:3]}")
            ws.close()
        finally:
            browser.terminate()
            browser.wait(timeout=5)
            server.shutdown()
    print("浏览器回归：" + (f"发现问题 {len(problems)}" if problems else "全部通过 ✓"))
    print(f"截图目录: {shot_dir}")


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "--static"
    deck_data = static_audit()
    if problems:
        print("\n".join("  ✗ " + p for p in problems))
        sys.exit(1)
    for n in notes:
        print(n)
    if arg in ("--browser", "--all"):
        pub = sys.argv[2] if len(sys.argv) > 2 else str(PARENT / "微信传播方案" / "发布" / "github-pages")
        browser_audit(pub, deck_data)
        if problems:
            print("\n".join("  ✗ " + p for p in problems))
            sys.exit(1)
        print("质量校验全部通过 ✓")


if __name__ == "__main__":
    main()
