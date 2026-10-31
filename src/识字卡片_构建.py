#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片构建脚本（300 字完整版）。

数据来源：
- 识字卡片_字库.py      → GROUPS：300 字的分组与顺序（校验基准）
- 识字卡片_素材_*.py    → 各组模块，暴露 GROUP_CARDS（卡片文案数据）与 arts()（插画 SVG 串）
- 识字卡片_图片/*.svg   → 首批试制 8 张（山日水手吃/大小/上下）的插画成品，构图组不重复生产
- 识字卡片_模板.html    → 页面框架（含分组导航、藏图、家长提示）

构建：python3 识字卡片_构建.py
"""
import importlib.util
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART_DIR = ROOT / "识字卡片_图片"
OUT = ROOT / "识字卡片_422字.html"
FONT_TTC = Path("/System/Library/Fonts/Supplemental/Songti.ttc")
SCALE = 0.215
PAIR_SCALE = 0.185

sys.path.insert(0, str(ROOT))
import 识字卡片_字库 as ZIKU  # noqa: E402

# 首批试制卡：插画已在 识字卡片_图片/，这里只带文案数据（插入对应组，按字库顺序排位）
SEED_CARDS = {
    "tianwen": [{"pair": None, "key": "日", "pinyin": "rì", "tone": "第四声", "sentence": "日出，天亮啦。",
                 "say": "太阳也叫日。太阳升起来，叫日出。", "chat": "“早上太阳从哪里升起来？”", "life": "早晨看看太阳升起，白天找一找太阳。"}],
    "ziran": [{"pair": None, "key": "山", "pinyin": "shān", "tone": "第一声", "sentence": "山高高。",
               "say": "这是山，山高高。", "chat": "“我们在哪里见过山？”看过图画或去过郊野再聊。", "life": "散步时指一指远处的山，找找图画书里的山。"},
              {"pair": None, "key": "水", "pinyin": "shuǐ", "tone": "第三声", "sentence": "杯子里有水。",
               "say": "我们喝的、洗手用的，都是水。", "chat": "“杯子里的水是什么样子的？”", "life": "倒一杯水给他看一看、摸一摸，洗手时再指认。"}],
    "renti": [{"pair": None, "key": "手", "pinyin": "shǒu", "tone": "第三声", "sentence": "我有两只手。",
               "say": "这是手，我们有两只手。", "chat": "“手能做什么？”拍手、拿东西都说得算。", "life": "一起举手、拍手、数一数手指。"}],
    "duibi": [{"pair": ["小", "大"], "key": "大小", "pinyin": "xiǎo · dà", "tone": "第三声 · 第四声", "sentence": "小球小，大球大。",
               "say": "两个球放在一起比：小的、大的。指哪个就说哪个字。", "chat": "“哪个球大，哪个球小？”换两个杯子再问一次。", "life": "拿同类的两个东西比大小：球、杯子、鞋子。"},
              {"pair": ["上", "下"], "key": "上下", "pinyin": "shàng · xià", "tone": "都是第四声", "sentence": "球在上，球在下。",
               "say": "球在桌子上面，是“上”；桌子下面，是“下”。", "chat": "“球在哪里？”先指上半问一次，再指下半问一次。", "life": "把玩具放上桌、放桌下，来回说“上”和“下”。"}],
    "dongzuo": [{"pair": None, "key": "吃", "pinyin": "chī", "tone": "第一声", "sentence": "我吃一口饭。",
                 "say": "吃，是把食物送进嘴里。", "chat": "“他在吃什么？”孩子答饭就说对。", "life": "吃饭的时候指一指“吃”，吃别的东西也用。"}],
}
SEED_ART_FILES = {"山": "山.svg", "日": "日.svg", "水": "水.svg", "手": "手.svg", "吃": "吃.svg",
                  "大小": "大小.svg", "上下": "上下.svg"}


def load_group_modules():
    """发现并导入 识字卡片_素材_*.py。同一组可拆多个模块：素材_<组id>.py 或 素材_<组id>_<后缀>.py。"""
    mods = {}
    for f in sorted(ROOT.glob("识字卡片_素材_*.py")):
        if f.name == "识字卡片_素材库.py":
            continue
        base = f.stem.replace("识字卡片_素材_", "")
        gid = re.sub(r"_[^_]*$", "", base) if "_" in base else base
        try:
            spec = importlib.util.spec_from_file_location(f"sucai_{base}", f)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            mods.setdefault(gid, []).append(mod)
        except Exception as e:  # noqa: BLE001
            print(f"[错误] 组模块 {f.name} 导入失败：{type(e).__name__}: {e}")
            raise
    return mods


def ziku_index():
    """{group_id: {key: 顺序号}}，key 为 char 或 tuple(pair)。"""
    idx = {}
    for g in ZIKU.GROUPS:
        m = {}
        for i, item in enumerate(g["chars"]):
            key = item["char"] if isinstance(item, dict) else item
            key = tuple(key) if isinstance(key, list) or isinstance(key, tuple) else key
            m[key] = i
        idx[g["id"]] = m
    return idx


def norm_key(card):
    if card.get("pair"):
        return tuple(card["pair"])
    return card["char"] if "char" in card else card["key"]


def extract_glyphs(chars):
    from fontTools.ttLib import TTCollection
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.boundsPen import BoundsPen

    collection = TTCollection(str(FONT_TTC), lazy=True)
    sc_fonts = [f for f in collection.fonts
                if "SC" in ((f["name"].getDebugName(1) or "") + (f["name"].getDebugName(4) or ""))]
    font = None
    for weight in ("Bold", "Black", "Medium", "Regular"):
        for f in sc_fonts:
            if weight in (f["name"].getDebugName(2) or ""):
                font = f
                break
        if font:
            break
    font = font or (sc_fonts[0] if sc_fonts else collection.fonts[0])
    cmap = font.getBestCmap()
    glyphset = font.getGlyphSet()
    out = {}
    for ch in chars:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(glyphset)
        glyphset[gname].draw(pen)
        bp = BoundsPen(glyphset)
        glyphset[gname].draw(bp)
        x0, y0, x1, y1 = bp.bounds
        out[ch] = {"d": re.sub(r"\s+", " ", pen.getCommands()).strip(),
                   "bx": (x0 + x1) / 2, "by": (y0 + y1) / 2}
    return out


def load_art(filename):
    text = (ART_DIR / filename).read_text(encoding="utf-8")
    inner = re.search(r"<svg[^>]*>(.*)</svg>", text, re.S).group(1)
    inner = inner.replace('id="art"', "").replace('id="monster"', 'id="m-seed"')
    inner = inner.replace('id="hand"', 'id="hand-seed"').replace('href="#hand"', 'href="#hand-seed"')
    return inner.strip()


def resolve_deck():
    """解析最终卡片与插画；供构建、预览和修改范围校验共同使用。"""
    mods = load_group_modules()
    zidx = ziku_index()

    # 1) 组装各组卡片（组模块文案 + 种子卡），按字库顺序排序
    groups_out, art_map, problems = [], {}, []
    for g in ZIKU.GROUPS:
        gid = g["id"]
        cards = []
        for mod in mods.get(gid, []):
            cards += [dict(c) for c in mod.GROUP_CARDS]
        cards += [dict(c) for c in SEED_CARDS.get(gid, [])]
        seen_keys = set()
        for c in cards:
            k = norm_key(c)
            if "key" not in c:
                c["key"] = "".join(k) if isinstance(k, tuple) else k
            if not c.get("pair") and "char" not in c:
                c["char"] = c["key"]
            c["pair"] = list(k) if isinstance(k, tuple) else None
            if k in seen_keys:
                problems.append(f"[{gid}] 重复卡片：{k}")
            seen_keys.add(k)
        idx_map = zidx[gid]
        missing = [k for k in idx_map if k not in seen_keys]
        extra = [k for k in seen_keys if k not in idx_map]
        if missing:
            problems.append(f"[{gid}] 缺卡片：{missing}")
        if extra:
            problems.append(f"[{gid}] 多余卡片：{extra}")
        cards.sort(key=lambda c: idx_map[norm_key(c)])
        # 插画解析
        mod_arts = {}
        for mod in mods.get(gid, []):
            for k, v in mod.arts().items():
                if k in mod_arts:
                    problems.append(f"[{gid}] 插画 key 重复：{k}")
                mod_arts[k] = v
        for c in cards:
            if c["key"] in SEED_ART_FILES:
                art_map[c["key"]] = load_art(SEED_ART_FILES[c["key"]])
            elif c["key"] in mod_arts:
                art_map[c["key"]] = mod_arts[c["key"]]
            else:
                problems.append(f"[{gid}] 卡「{c['key']}」没有插画")
        groups_out.append({"id": gid, "name": g["name"], "desc": g["desc"], "cards": cards})

    # 2) 全局查重
    all_keys = [c["key"] for g in groups_out for c in g["cards"]]
    dup = sorted({k for k in all_keys if all_keys.count(k) > 1})
    if dup:
        problems.append(f"重复卡：{dup}")

    total_chars = sum(len(c["pair"]) if c["pair"] else 1 for g in groups_out for c in g["cards"])
    n_cards = len(all_keys)
    if problems:
        raise ValueError("\n".join(problems))

    return groups_out, art_map


def deck_digest(groups_out, art_map):
    """标识一次最终解析结果，确保范围检查与实际构建使用同一副牌。"""
    raw = json.dumps(
        {"groups": groups_out, "art": art_map},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def render_document(groups_out, art_map):
    """把已解析的最终卡片编译成 HTML 字符串，不写磁盘。"""
    all_keys = [c["key"] for g in groups_out for c in g["cards"]]
    glyphs = extract_glyphs(sorted({ch for c in all_keys for ch in c}))
    template = (ROOT / "识字卡片_模板.html").read_text(encoding="utf-8")
    flat_cards = []
    for gi, g in enumerate(groups_out):
        for c in g["cards"]:
            flat_cards.append({**c, "g": gi})
    return (template
            .replace("__CARDS__", json.dumps(flat_cards, ensure_ascii=False))
            .replace("__GROUPS__", json.dumps([{"id": g["id"], "name": g["name"]} for g in groups_out], ensure_ascii=False))
            .replace("__GLYPHS__", json.dumps(glyphs, ensure_ascii=False))
            .replace("__SCALE__", str(SCALE))
            .replace("__PAIR_SCALE__", str(PAIR_SCALE))
            .replace("__ART__", json.dumps(art_map, ensure_ascii=False))
            .replace("__STROKES__", _strokes_json()))


def _strokes_json():
    """标准笔顺数据（每字每笔的中线点列），供"显示笔画"逐笔动画使用。"""
    import importlib.util
    data_file = ROOT / "识字卡片_笔画数据.py"
    if not data_file.exists():
        return "{}"
    spec = importlib.util.spec_from_file_location("strokes_data", data_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.STROKES_JSON


def build():
    try:
        groups_out, art_map = resolve_deck()
    except ValueError as exc:
        problems = str(exc).splitlines()
        print(f"共 {len(problems)} 个问题：")
        for problem in problems:
            print("  " + problem)
        sys.exit(1)

    # 有范围锁时必须精确通过；没有范围锁时，只允许幂等重建，拒绝写入任何新变化。
    scope_state = ROOT / ".识字卡片_修改范围.json"
    if scope_state.exists():
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "识字卡片_修改范围.py"),
                "check",
                "--expected-deck",
                deck_digest(groups_out, art_map),
            ],
            cwd=ROOT,
            check=True,
        )

    html = render_document(groups_out, art_map)
    if not scope_state.exists() and (not OUT.exists() or OUT.read_text(encoding="utf-8") != html):
        print("[拒绝] 当前源码会改变正式 HTML，但没有活动修改范围。")
        print("请先运行：python3 识字卡片_修改范围.py begin <卡片...>")
        sys.exit(1)

    total_chars = sum(len(c["pair"]) if c["pair"] else 1 for g in groups_out for c in g["cards"])
    n_cards = sum(len(g["cards"]) for g in groups_out)
    temp_out = OUT.with_suffix(OUT.suffix + ".tmp")
    try:
        temp_out.write_text(html, encoding="utf-8")
        temp_out.replace(OUT)
    finally:
        temp_out.unlink(missing_ok=True)
    print(f"OK {OUT.name}  {OUT.stat().st_size/1024:.1f} KB  |  {len(groups_out)} 组  {n_cards} 卡  {total_chars} 字")


if __name__ == "__main__":
    build()
