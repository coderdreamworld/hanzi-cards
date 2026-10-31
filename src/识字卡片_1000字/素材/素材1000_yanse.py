#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""颜色组补充 3 卡插画与文案（1000 字批次 B8）。

字表：银紫棕（legacy ../识字卡片_素材_yanse.py 已有 8 基色花+碟 与 彩色青 3 卡，
本文件只做增量，不与 legacy 撞造型）。

沿用 legacy「同一物件换颜色」思路，但每字一件专属物件：
银=银色大勺子（加高光小闪星表现金属反光）/ 紫=紫色葡萄串 /
棕=棕色大皮球。图上无文字。
"""
import importlib.util
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
SILVER, SILVER_D, SILVER_L = "#ccd3d9", "#aab3bc", "#eef2f5"
GRAPE, GRAPE_D = "#8e6bc0", "#7453a8"
BROWN_B, BROWN_BD, BROWN_BL = "#a5713f", "#8a5a30", "#c49a6c"


def _rot(x, y, deg, svg):
    return f'<g transform="rotate({deg} {x} {y})">{svg}</g>'


def _sparkle(cx, cy, r, fill=WHITE):
    """四角小闪星（表现金属反光，语义需要）。"""
    return wrap(
        PG([(cx, cy - r), (cx + r * 0.3, cy - r * 0.3), (cx + r, cy),
            (cx + r * 0.3, cy + r * 0.3), (cx, cy + r),
            (cx - r * 0.3, cy + r * 0.3), (cx - r, cy),
            (cx - r * 0.3, cy - r * 0.3)], fill))


def a_yin():
    """银：银色小勺长柄竖放，勺头小、柄长长，亮闪闪。"""
    return wrap(
        ground(380, 448, 220, 22),
        R(366, 236, 28, 208, 13, SILVER_D),
        R(361, 230, 28, 208, 13, SILVER),
        L(367, 242, 367, 428, SILVER_L, 5),
        C(380, 238, 13, SILVER),                       # 勺颈
        E(386, 158, 62, 80, SILVER_D),                 # 勺头（深一号底）
        E(380, 152, 62, 80, SILVER),
        E(380, 157, 44, 58, SILVER_D),                 # 勺凹面
        E(375, 151, 34, 46, SILVER_L),
        E(362, 122, 13, 22, WHITE, 0.75),              # 高光
        _sparkle(500, 88, 18), _sparkle(250, 140, 13), _sparkle(530, 300, 12),
    )


def a_zi():
    """紫：紫色葡萄一串串。"""
    grapes = ""
    for cx, cy in ((318, 262), (382, 244), (446, 262),
                   (350, 326), (414, 326), (382, 382)):
        grapes += C(cx + 5, cy + 6, 40, GRAPE_D) + C(cx, cy, 40, GRAPE)
        grapes += C(cx - 13, cy - 14, 9, WHITE, 0.55)
    return wrap(
        ground(380, 444, 230, 22),
        L(382, 160, 380, 226, "#8a5a33", 12),          # 果梗
        _rot(382, 200, -24, E(452, 200, 58, 22, GREEN)),  # 叶子
        L(440, 176, 462, 158, "#5f8f52", 5),
        grapes,
    )


def a_zong():
    """棕：棕色大皮球。"""
    return wrap(
        ground(380, 446, 240, 24),
        ball(380, 336, 108, BROWN_B, BROWN_BD, BROWN_BL),
        P("M 292 372 Q 380 402 468 372", stroke=BROWN_BD, w=5),
    )


def arts():
    return {"银": a_yin(), "紫": a_zi(), "棕": a_zong()}


GROUP_CARDS = [
    {"char": "银", "pinyin": "yín", "tone": "第二声",
     "sentence": "银色小勺亮闪闪。",
     "say": "银色亮亮的，像小镜子。",
     "chat": "勺子在光下会闪吗？",
     "life": "拿小勺照照光，看它发亮。"},
    {"char": "紫", "pinyin": "zǐ", "tone": "第三声",
     "sentence": "紫色葡萄一串串。",
     "say": "葡萄紫紫的，一颗颗抱在一起。",
     "chat": "葡萄是什么颜色的呀？",
     "life": "数一数这串有几颗葡萄。"},
    {"char": "棕", "pinyin": "zōng", "tone": "第一声",
     "sentence": "棕色的皮球拍一拍。",
     "say": "像巧克力一样的颜色是棕色。",
     "chat": "棕色和黄色哪里不一样？",
     "life": "找找家里棕色的家具。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "yanse" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B8"] if e["file"] == "素材1000_yanse.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"颜色组补充：卡数 {len(GROUP_CARDS)}")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    idx = [ziku_chars.index(ch) for ch in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = set(a) == set(mine)
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad = []
    for c in GROUP_CARDS:
        w = py[c["char"]]
        if c["pinyin"] != w["pinyin"]:
            bad.append((c["char"], "pinyin", c["pinyin"], w["pinyin"]))
        if not (c["tone"] == w["tone"] or c["tone"].startswith(w["tone"] + "（")):
            bad.append((c["char"], "tone", c["tone"], w["tone"]))
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((c["char"], "句长", hanzi))
        if c["char"] not in c["sentence"]:
            bad.append((c["char"], "句缺字"))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((c["char"], f, len(c[f])))
    print(f"拼音/声调/文案：{'全部通过 ✓' if not bad else str(bad)}")

    svgbad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            svgbad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                svgbad.append((k, t))
        if not v.startswith("<ellipse"):
            svgbad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not svgbad else f"SVG 问题：{svgbad}")

    assert mine == expect and keys_ok and idx == sorted(idx) and not bad and not svgbad, "自检未通过"
    print("自检通过 ✓")
