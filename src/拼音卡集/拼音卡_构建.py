#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""拼音卡构建器。

- 拼音卡_素材.py → SETS（卡片数据）与 NEW_ARTS（新插画）
- "ref":字  → 复用识字卡 402 素材解析出的插画（只取需要的 key）
- 拼读卡 chips：从 422 字库自动匹配「真声母×单韵母」音节（排除 y/w 整体类）
- 唯一构建入口：python3 拼音卡_构建.py
"""
import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
sys.path.insert(0, str(PARENT))
import 识字卡片_构建 as base  # noqa: E402  借用 resolve_deck 解析识字卡素材


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TRUE_INITIALS = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x",
                 "zh", "ch", "sh", "r", "z", "c", "s"]
CHIP_ORDER = TRUE_INITIALS + ["y", "w"]
FINALS = ["a", "o", "e", "i", "u", "ü"]


def split_py(py):
    """带调拼音 → (真声母或None, 单韵母 a/o/e/i/u/ü 或 None)。
    韵母整段必须恰为单韵母（ang/ong/ai 等复鼻韵母不算），否则返回 None。"""
    py = py.strip().lower()
    ini = None
    for cand in sorted(TRUE_INITIALS + ["y", "w"], key=len, reverse=True):
        if py.startswith(cand):
            ini = cand
            break
    rest = py[len(ini):] if ini else py
    nfd = unicodedata.normalize("NFD", rest)
    has_diaer = "\u0308" in nfd
    plain = "".join(ch for ch in nfd if not unicodedata.combining(ch))
    if plain == "v" or (plain == "u" and has_diaer):
        plain = "ü"
    if plain not in FINALS:
        return ini, None
    return ini, plain


def build_spell_cards(deck_cards, art_of_map, new_arts, art_map):
    """按单韵母生成拼读卡；每卡 chips 取不同声母的库内字。"""
    groups = {f: [] for f in FINALS}
    for c in deck_cards:
        if c.get("pair"):
            continue
        ini, fin = split_py(c["pinyin"])
        if not ini or fin is None:
            continue
        if fin == "u" and ini in ("j", "q", "x", "y"):
            fin = "ü"         # ju qu xu yu 书写不写点，教学归入 ü 组（省点规则示例）
        if ini == "y" and fin != "ü":
            continue          # y 只进 ü 组
        if c["key"] not in art_of_map:
            continue
        groups[fin].append({"ini": ini, "sy": c["pinyin"], "zi": c["char"],
                            "say": c.get("sentence", ""), "art": art_of_map.get(c["key"], "")})
    cards = []
    for fin in FINALS:
        pool, seen = [], set()
        for item in sorted(groups[fin], key=lambda x: (0 if x["ini"] in ("zh", "ch", "sh") else 1, CHIP_ORDER.index(x["ini"]))):
            if item["ini"] in seen:
                continue
            seen.add(item["ini"])
            pool.append(item)
        card = {"key": f"D_{fin}", "type": "spell", "final": fin,
                "rule": "j q x y 碰到 ü，两点要省去" if fin == "ü" else None,
                "chips": pool[:8]}
        scene = {"a": "s_a", "o": "鸡", "e": "鹅", "i": "衣", "u": None, "ü": "鱼"}.get(fin)
        if scene == "s_a":
            card["art"] = new_arts["s_a"]
        elif scene:
            card["art"] = art_map.get(scene, "")
        cards.append(card)
    return cards


def build_set(sucai, strokes_mod, set_def, art_map, deck_cards):
    problems = []
    art_cache = {}

    def resolve(card):
        if card.get("ref"):
            if card["ref"] not in art_map:
                problems.append(f"{card.get('key', card.get('letter'))}: ref {card['ref']} 不在识字卡素材")
                return ""
            return art_map[card["ref"]]
        if card.get("art") and not card["art"].startswith("<"):
            key = card["art"]
            if key not in sucai.NEW_ARTS:
                problems.append(f"{key}: 不在 NEW_ARTS")
                return ""
            return sucai.NEW_ARTS[key]
        if card.get("scene"):
            if card["scene"] not in sucai.NEW_ARTS:
                problems.append(f"{card['scene']}: 不在 NEW_ARTS")
                return ""
            return sucai.NEW_ARTS[card["scene"]]
        return ""

    groups_out = []
    for gi, g in enumerate(set_def["groups"]):
        cards = []
        if g["cards"] == "AUTO_SPELL":
            for c in build_spell_cards(deck_cards, art_map, sucai.NEW_ARTS, art_map):
                c = dict(c)
                c["g"] = gi
                cards.append(c)
        else:
            for c in g["cards"]:
                c = dict(c)
                c["g"] = gi
                c.setdefault("type", "match")
                if c["type"] == "tone":
                    for w in c["words"]:
                        w["art"] = resolve(w)
                elif c["type"] in ("letter", "match", "sound"):
                    c["art"] = resolve(c)
                cards.append(c)
        groups_out.append({"id": g["id"], "name": g["name"], "cards": cards})

    flat = []
    for gi, g in enumerate(groups_out):
        for c in g["cards"]:
            flat.append({**c, "g": gi})

    html = (strokes_mod.TEMPLATE
            .replace("__KIND__", set_def["kind"])
            .replace("__TITLE__", set_def["title"])
            .replace("__SUB__", set_def["sub"])
            .replace("__ACCENT__", set_def["accent"])
            .replace("__CARDS__", rj(flat))
            .replace("__GROUPS__", rj([{"id": g["id"], "name": g["name"]} for g in groups_out]))
            .replace("__STROKES__", rj(strokes_mod.STROKES))
            .replace("__TONE_MARKS__", rj({k: v for k, v in strokes_mod.TONE_MARKS.items() if v})))
    leftover = re.sub(r"__(?:KIND|TITLE|SUB|ACCENT|CARDS|GROUPS|STROKES|TONE_MARKS)__", "", html)
    if "__" in leftover:
        left = [ln.strip()[:80] for ln in leftover.splitlines() if "__" in ln][:3]
        problems.append(f"模板占位符可能有遗漏: {left}")
    if problems:
        raise ValueError("\n".join(problems))
    out = ROOT / set_def["file"]
    out.write_text(html, encoding="utf-8")
    print(f"OK {out.name}  {out.stat().st_size / 1024:.1f} KB  |  {len(flat)} 卡")
    return out


def rj(obj):
    import json
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def main():
    sucai = load_module(ROOT / "拼音卡_素材.py", "pysucai")
    strokes_mod = load_module(ROOT / "拼音卡_笔画.py", "pystrokes")
    strokes_mod.TEMPLATE = (ROOT / "拼音卡_模板.html").read_text(encoding="utf-8")

    groups, art_map = base.resolve_deck()
    deck_cards = [c for g in groups for c in g["cards"]]

    outs = []
    try:
        for set_def in sucai.SETS:
            outs.append(build_set(sucai, strokes_mod, set_def, art_map, deck_cards))
    except ValueError as exc:
        print("构建失败：")
        for line in str(exc).splitlines():
            print("  " + line)
        sys.exit(1)
    print(f"完成：{len(outs)} 个文件")


if __name__ == "__main__":
    main()
