#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站卡片内容不变量的严格回归测试（2026-11-01 新增）。

与 tests/test_navigation_progress.py（导航与进度）、tests/test_analytics_*.py（统计接入）
互补，本文件盯的是**内容**：卡片数据本身自洽、字形齐全、插画齐全、韵语押韵、
会意拆解与部首归属属实、页面在手机/宽屏下不溢出、运行期零 JS 错误。

用法：
    python3 tests/test_deck_content.py            # 静态内容检查
    python3 tests/test_deck_content.py --browser  # 加上浏览器运行期回归
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
PINYIN_JSON = SRC / "识字卡片_1000字" / "拼音表1000.json"
IDS_TSV = SRC / "汉语启蒙卡集" / "扩充" / "部首构形表.tsv"

# (发布页, 期望卡数, kind)   kind: index / pinyin / zishi / pic / magic / family / verse / other
DECKS = [
    ("index.html", None, "index"),
    ("pinyin-zimu.html", 138, "pinyin"),
    ("shizi-422.html", 402, "zishi"),
    ("shizi-1000.html", 964, "zishi"),
    ("xiangxing.html", 20, "pic"),
    ("huiyi.html", 24, "magic"),
    ("bushou.html", 19, "family"),
    ("yunyu.html", 24, "verse"),
    ("emotion.html", None, "other"),
]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TM = {"ā": "a", "á": "a", "ǎ": "a", "à": "a", "ē": "e", "é": "e", "ě": "e", "è": "e",
      "ī": "i", "í": "i", "ǐ": "i", "ì": "i", "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
      "ū": "u", "ú": "u", "ǔ": "u", "ù": "u", "ǖ": "ü", "ǘ": "ü", "ǚ": "ü", "ǜ": "ü", "ü": "ü"}
INIT = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h",
        "j", "q", "x", "r", "z", "c", "s"]

problems = []


def check(cond, msg):
    if not cond:
        problems.append(msg)
    return cond


def extract(html, var):
    m = re.search(rf"(?:const|var|let) {var} = (\[.*?\]|\{{.*?\}});\n", html, re.S)
    return json.loads(m.group(1)) if m else None


def final_of(p):
    """拼音 → 韵母（严格口径：同一个韵母才算押韵，不做十三辙并韵）。"""
    s = "".join(TM.get(c, c) for c in p.lower() if c.isalpha())
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
    return f.replace("ü", "v")


def line_tail(line):
    m = re.match(r"^(.*)([一-鿿])([，。；！？]?)$", line)
    return m.group(2) if m else None


def load_ids():
    ids = {}
    if not IDS_TSV.exists():
        return ids
    for line in IDS_TSV.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            p = line.split("\t")
            if len(p) >= 2:
                ids[p[0]] = p[1]
    return ids


def norm(s):
    return (s.replace("吅", "⿰口口").replace("昍", "⿰日日")
             .replace("龵", "手").replace("灬", "火"))


def comps(ids):
    return "".join(sorted(re.sub(r"[⿰-⿿]", "", norm(ids))))


# ---------------------------------------------------------------- 静态内容

def static_checks():
    pinyin = json.loads(PINYIN_JSON.read_text(encoding="utf-8")) if PINYIN_JSON.exists() else {}
    ids = load_ids()

    for name, n_expect, kind in DECKS:
        html = (ROOT / name).read_text(encoding="utf-8")
        if kind == "index":
            # 首页：7 套展示 + 象形字保留直达但不入首页
            for deck in ("pinyin-zimu.html", "shizi-422.html", "shizi-1000.html",
                         "huiyi.html", "bushou.html", "yunyu.html", "emotion.html"):
                check(deck in html, f"index.html: 首页缺 {deck} 的入口")
            check("xiangxing.html" not in html, "index.html: 象形字卡不应出现在首页")
            continue

        cards = extract(html, "CARDS")
        if cards is None:
            if kind != "other":
                problems.append(f"{name}: 找不到 CARDS")
            continue
        art = extract(html, "ART") or {}
        glyphs = extract(html, "GLYPHS") or {}
        payload = json.dumps([cards, art, glyphs], ensure_ascii=False)
        check("undefined" not in payload, f"{name}: 数据载荷里出现 undefined")
        check("NaN" not in payload, f"{name}: 数据载荷里出现 NaN")
        check(len(cards) == n_expect, f"{name}: 卡数 {len(cards)} ≠ {n_expect}")
        keys = [c.get("key") or c.get("letter") or c.get("char") or str(i)
                for i, c in enumerate(cards)]
        if kind != "pinyin":   # 拼音卡里同一个音会出现在多个组，key 天然重复
            check(len(keys) == len(set(keys)), f"{name}: 卡 key 重复")

        for c, k in zip(cards, keys):
            if kind == "pinyin":
                check("art" not in c or bool(c["art"]), f"{name}:{k} 插画为空")
            elif art:
                check(k in art and art[k].strip(), f"{name}:{k} 缺插画")
            for tag, txt in (c.get("tips") or []):
                check(txt and txt.strip(), f"{name}:{k} 「{tag}」提示为空")
                check("undefined" not in txt, f"{name}:{k} 「{tag}」提示含 undefined")
            # 字形齐全：会意卡的部件与结果字、部首家族成员与部首，都要有矢量字形
            need = []
            if c.get("type") == "magic":
                need = [p[0] for p in c["parts"]] + [c["result"]]
            elif c.get("type") == "family":
                need = [c["radical"]] + [m[0] for m in c["members"]]
            elif c.get("type") == "pic" and "char" in c:
                need = [c["char"]]
            elif kind == "zishi":
                need = [c["char"]] if "char" in c else list(c.get("pair", []))
            for ch in need:
                if glyphs:
                    check(ch in glyphs, f"{name}:{k} 字形缺 {ch}")

        if kind == "verse" and pinyin:
            for idx, c in enumerate(cards):
                if c.get("type") != "verse" or idx < 8:
                    continue          # 旧 8 首韵语按十三辙并韵，不做严格韵母要求
                tails = [line_tail(ln) for ln in c["lines"]]
                check(all(tails), f"{name}:{c['title']} 有行尾不是「句子+汉字+标点」")
                fins = [final_of(pinyin[t]["pinyin"]) for t in tails if t in pinyin]
                if len(set(fins)) != 1:
                    problems.append(f"{name}:{c['title']} 韵脚不齐 {list(zip(tails, fins))}")
                tip = next((t for tag, t in c.get("tips", []) if tag == "找韵脚"), "")
                head = tip.split("——")[0]
                listed = re.findall(r"[一-鿿]", head)
                # 旧韵语有 3 行、提示写「五、虎、鼠」这类也按行末字；只查形如「A、B、C」的清单
                if re.fullmatch(r"[一-鿿](、[一-鿿])+", head.strip("，")):
                    check(listed == tails,
                          f"{name}:{c['title']} 「找韵脚」提示列的字 {''.join(listed)} ≠ 行末字 {''.join(tails)}")

        if kind == "magic" and ids:
            for c in cards:
                if c.get("type") != "magic" or c["result"] not in ids:
                    continue          # 构形表只收录了 2026-11-01 新增的 10 张
                r = c["result"]
                parts = "".join(p[0] for p in c["parts"])
                got = comps(ids.get(r, ""))
                want = "".join(sorted(parts))
                folk = r == "出"          # 民间字理：两座山叠起来
                check(got == want or folk,
                      f"{name}:{r} 部件「{parts}」与真实构形「{got}」不一致")

        if kind == "family" and ids:
            need = {"虫": "虫", "讠": "讠", "忄": "忄", "犭": "犭", "月": "月",
                    "火": "火", "辶": "辶", "米": "米", "钅": "钅"}
            for c in cards:
                rad = c["radical"]
                if rad not in need:
                    continue
                for m in c["members"]:
                    ch = m[0]
                    d = ids.get(ch, "")
                    ok = ch == rad or (need[rad] in norm(d))
                    check(ok, f"{name}:{rad} 家族成员「{ch}」不带该部首（IDS={d or '无'}）")
    print(f"静态内容检查：{'发现问题 ' + str(len(problems)) if problems else '全部通过 ✓'}")


# ---------------------------------------------------------------- 浏览器回归

def browser_checks():
    import http.server
    import functools
    import pathlib
    import tempfile
    import threading
    import time
    import base64
    import websocket

    server = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(http.server.SimpleHTTPRequestHandler,
                                            directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
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
                    raise RuntimeError(json.dumps(res["exceptionDetails"])[:300])
                return res.get("result", {}).get("value")

            cmd("Page.enable")
            cmd("Runtime.enable")
            base = f"http://127.0.0.1:{server.server_port}/"

            def visit(path, width, height, mobile):
                cmd("Emulation.setDeviceMetricsOverride",
                    {"width": width, "height": height, "deviceScaleFactor": 2, "mobile": mobile})
                cmd("Page.navigate", {"url": base + path})
                for _ in range(200):
                    try:
                        if evaluate("document.readyState === 'complete'"):
                            evaluate("window.__errs=[];window.onerror=function(m,s,l){(window.__errs=window.__errs||[]).push(m+' @'+l)}")
                            time.sleep(.12)
                            return
                    except RuntimeError:
                        pass
                    time.sleep(.05)
                raise RuntimeError(f"页面未加载: {path}")

            for name, n_expect, kind in DECKS:
                if kind == "index":
                    visit(name, 390, 844, True)
                    check(not evaluate("document.documentElement.scrollWidth>innerWidth+1"),
                          "index.html: 手机端横向溢出")
                    check(evaluate("document.querySelectorAll('a[href*=\".html\"]').length") >= 7,
                          "index.html: 卡片入口少于 7 个")
                    continue
                for width, height, mobile in ((390, 844, True), (1440, 900, False)):
                    visit(name, width, height, mobile)
                    errs = evaluate("window.__errs || []")
                    check(not errs, f"{name} @{width}px: JS 错误 {errs[:2]}")
                    check(not evaluate("document.documentElement.scrollWidth>innerWidth+1"),
                          f"{name} @{width}px: 横向溢出")
                    if kind != "other":
                        home = evaluate(
                            "Array.from(document.querySelectorAll('a.home-btn')).some(a=>{"
                            "const r=a.getBoundingClientRect();"
                            "return r.width>0 && r.height>0 && (a.getAttribute('href')||'').includes('index');})")
                        check(home, f"{name} @{width}px: 返回首页按钮缺失或不可达")
                    if n_expect:
                        got = evaluate("(typeof CARDS!=='undefined') ? CARDS.length : null")
                        check(got == n_expect, f"{name} @{width}px: 运行时 CARDS={got} ≠ {n_expect}")
                # 翻页与进度：每套卡都能翻到下一张并记住位置
                visit(name, 390, 844, True)
                if evaluate("(typeof go==='function')"):
                    before = evaluate("state.i")
                    evaluate("go(1)")
                    check(evaluate("state.i") != before, f"{name}: 翻页无效")
                    check(evaluate("(typeof localStorage.getItem('hz.last')==='string')"),
                          f"{name}: 未写入 hz.last")
            ws.close()
        finally:
            browser.terminate()
            browser.wait(timeout=5)
            server.shutdown()
    print(f"浏览器回归：{'发现问题 ' + str(len(problems)) if problems else '全部通过 ✓'}")


def main():
    static_checks()
    if "--browser" in sys.argv:
        browser_checks()
    if problems:
        print("\n".join("  ✗ " + p for p in problems))
        sys.exit(1)
    print("内容回归测试全部通过 ✓")


if __name__ == "__main__":
    main()
