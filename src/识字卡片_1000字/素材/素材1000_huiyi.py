#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""会意字组 7 卡插画与文案（1000 字批次 B9，全组新增）。

字表（字库 huiyi 尾段，legacy 已覆盖前 17 字）：品晶灶灭掰岩歪。
（批次分配.json 的 B9 huiyi 节还列了"看"，但 legacy 动作·拓展组已有"看"卡，
重复生产会成重复卡，故不产——与任务要求的 7 卡一致。）

一眼可辨约定（字理构图，主控硬规则）：
品=三个方口物摆成品字 / 晶=三颗亮晶体 / 灶=灶台+火眼火苗+坐锅 /
灭=火苗上压盖子冒烟 / 掰=双手把大饼掰两半（hand()）/ 岩=山顶上叠着石头 /
歪=画框挂歪了。部件即字理，同组相邻卡轮廓+主色错开。
"""
import importlib.util
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
BRICK, BRICK_D = "#c0705c", "#a05f4c"
IRON, IRON_L, IRON_D = "#5b6470", "#7a828c", "#495058"
GRAY, GRAY_D, LGRAY = "#c9cdd1", "#9aa2ab", "#d8d2c2"
ROCK, ROCK_D = "#6b7280", "#565d66"
BISCUIT, BISCUIT_D = "#eec27e", "#d9a05b"

GROUP_CARDS = [
    {"char": "品", "pinyin": "pǐn", "tone": "第三声",
     "sentence": "三个方盒摆成品。",
     "say": "三个口字叠起来，就是品字。",
     "chat": "上面一个口，下面几个口呀？",
     "life": "拿三块积木摆一个品字。"},
    {"char": "晶", "pinyin": "jīng", "tone": "第一声",
     "sentence": "宝石亮晶晶。",
     "say": "三个日字拼成晶，闪闪亮。",
     "chat": "还有什么东西亮晶晶的呀？",
     "life": "看夜晚的星星说：亮晶晶。"},
    {"char": "灶", "pinyin": "zào", "tone": "第四声",
     "sentence": "灶台上煮着饭。",
     "say": "烧火做饭的台子叫灶台。",
     "chat": "火眼里的火苗在干什么呀？",
     "life": "路过厨房看看灶台和锅。"},
    {"char": "灭", "pinyin": "miè", "tone": "第四声",
     "sentence": "盖上盖子，火灭了。",
     "say": "盖子把火苗一压，火就灭了。",
     "chat": "小火苗去哪儿了呀？",
     "life": "生日吹蜡烛，一口气把火灭掉。"},
    {"char": "掰", "pinyin": "bāi", "tone": "第一声",
     "sentence": "把大饼掰成两半。",
     "say": "两只手用力一掰，分两半。",
     "chat": "你掰开过饼干或面包吗？",
     "life": "把饼干掰一半分给妈妈。"},
    {"char": "岩", "pinyin": "yán", "tone": "第二声",
     "sentence": "山顶上叠着岩石。",
     "say": "山上叠石头，就是岩石。",
     "chat": "岩石摸起来是什么感觉呀？",
     "life": "去公园找一块大石头摸摸。"},
    {"char": "歪", "pinyin": "wāi", "tone": "第一声",
     "sentence": "画框挂歪了。",
     "say": "歪歪扭扭不正，就是歪。",
     "chat": "画歪了该怎么扶正呀？",
     "life": "把歪掉的小椅子摆摆正。"},
]


# ---------- 卡片插画 ----------
def a_pin():
    """品：三个方口木盒，摆成品字。"""
    g = ground()
    boxes = ""
    for cx, cy in ((312, 356), (448, 356), (380, 216)):
        boxes += wrap(
            E(cx, cy + 66, 72, 10, GRAY, 0.5) if cy > 300 else "",
            R(cx - 62, cy - 62, 124, 124, 16, WOOD),
            R(cx - 62, cy - 62, 124, 18, 9, WOOD_L),
            R(cx - 34, cy - 30, 68, 68, 10, WOOD_D))
    return g + boxes


def _gem(cx, cy, s=1.0):
    """一颗亮晶体：六边形宝石+高光+小闪星。"""
    return wrap(
        PG([(cx, cy - 46 * s), (cx + 40 * s, cy - 22 * s), (cx + 40 * s, cy + 22 * s),
            (cx, cy + 46 * s), (cx - 40 * s, cy + 22 * s), (cx - 40 * s, cy - 22 * s)],
           "#79c2e6"),
        PG([(cx, cy - 46 * s), (cx + 40 * s, cy - 22 * s), (cx, cy), (cx - 40 * s, cy - 22 * s)],
           "#a8d8ef"),
        PG([(cx, cy), (cx + 40 * s, cy + 22 * s), (cx, cy + 46 * s), (cx - 40 * s, cy + 22 * s)],
           "#5fa8d8"),
        C(cx - 14 * s, cy - 20 * s, 7 * s, WHITE, 0.85),
        L(cx + 48 * s, cy - 58 * s, cx + 48 * s, cy - 34 * s, SUN, 6 * s),
        L(cx + 36 * s, cy - 46 * s, cx + 60 * s, cy - 46 * s, SUN, 6 * s))


def a_jing():
    """晶：三颗亮晶晶的宝石，摆成品字闪着光。"""
    g = ground()
    g += E(300, 428, 66, 10, GRAY, 0.5) + E(460, 428, 66, 10, GRAY, 0.5)
    g += _gem(300, 366, 1.0) + _gem(460, 366, 1.0) + _gem(380, 214, 1.0)
    return g


def a_zao():
    """灶：砖砌灶台，火眼里有火苗，灶上坐着锅冒热气。"""
    g = ground()
    body = wrap(
        R(250, 270, 260, 170, 20, BRICK),
        L(250, 330, 510, 330, BRICK_D, 5),
        L(250, 385, 510, 385, BRICK_D, 5),
        L(330, 330, 330, 385, BRICK_D, 5),
        L(430, 330, 430, 385, BRICK_D, 5),
        R(242, 254, 276, 26, 12, IRON))
    eye = wrap(
        P("M 330 440 L 330 384 Q 380 348 430 384 L 430 440 Z", "#3a2a20"),
        P("M 380 432 Q 348 402 364 372 Q 370 388 380 378 Q 390 390 398 370 "
          "Q 412 400 380 432 Z", "#e8663c"),
        P("M 380 428 Q 364 408 374 390 Q 380 400 386 390 Q 394 406 380 428 Z", SUN))
    pot = wrap(
        R(300, 192, 160, 62, 16, IRON),
        E(380, 192, 84, 15, "#6b7480"),
        C(380, 176, 10, IRON_D),
        P("M 350 168 q -8 -20 6 -34", stroke=LGRAY, w=7),
        P("M 408 168 q 8 -20 -6 -34", stroke=LGRAY, w=7))
    return g + body + eye + pot


def a_mie():
    """灭：盖子压住火苗，火灭了只冒烟。"""
    g = ground()
    logs = wrap(
        f'<g transform="rotate(14 380 428)">{R(300, 416, 160, 26, 12, WOOD_D)}</g>',
        f'<g transform="rotate(-14 380 428)">{R(300, 416, 160, 26, 12, WOOD_D)}</g>')
    flame = wrap(
        P("M 380 418 Q 328 386 352 326 Q 360 348 374 334 Q 382 314 394 332 "
          "Q 406 320 410 342 Q 432 384 380 418 Z", "#e8663c"),
        P("M 380 412 Q 358 392 370 356 Q 378 372 386 360 Q 396 384 380 412 Z", SUN))
    lid_p = lid(380, 300, 216, 52, rot=-6)
    smoke = wrap(
        P("M 292 262 q -16 -20 2 -38", stroke=LGRAY, w=8),
        P("M 268 240 q -12 -18 4 -32", stroke=LGRAY, w=6),
        P("M 470 262 q 16 -20 -2 -38", stroke=LGRAY, w=8))
    return g + logs + flame + lid_p + smoke


def a_bai():
    """掰：两只手把大饼掰成两半。"""
    g = ground()
    left = P("M 300 268 Q 234 276 234 340 Q 234 398 300 404 L 356 396 "
             "L 342 372 L 358 352 L 344 330 L 356 308 L 344 286 L 358 272 Z", BISCUIT)
    right = P("M 460 268 Q 526 276 526 340 Q 526 398 460 404 L 404 396 "
              "L 418 372 L 402 352 L 416 330 L 404 308 L 416 286 L 402 272 Z", BISCUIT)
    spots = wrap(
        C(278, 318, 8, BISCUIT_D, 0.8), C(262, 362, 6, BISCUIT_D, 0.8),
        C(296, 380, 5, BISCUIT_D, 0.8), C(488, 320, 8, BISCUIT_D, 0.8),
        C(502, 364, 6, BISCUIT_D, 0.8), C(470, 384, 5, BISCUIT_D, 0.8))
    crumbs = wrap(
        C(378, 336, 6, BISCUIT_D), C(386, 368, 5, BISCUIT_D), C(372, 356, 4, BISCUIT_D))
    return g + left + right + spots + crumbs + hand(186, 320, rot=90, s=0.9) \
        + hand(574, 320, rot=-90, s=0.9)


def a_yan():
    """岩：山顶上叠着大石头。"""
    g = ground()
    mount = wrap(
        P("M 176 440 Q 240 300 330 232 Q 380 196 430 232 Q 520 300 584 440 Z", GRAY),
        P("M 330 232 Q 380 196 430 232 Q 420 262 380 252 Q 340 264 330 232 Z", LGRAY))
    rocks = wrap(
        C(380, 182, 42, ROCK),
        C(366, 168, 11, LGRAY, 0.75),
        C(334, 226, 27, ROCK_D),
        C(428, 228, 27, ROCK_D),
        C(326, 216, 8, LGRAY, 0.7),
        C(422, 218, 8, LGRAY, 0.7))
    return g + mount + rocks


def a_wai():
    """歪：画框挂歪了。"""
    g = ground()
    nail = C(380, 130, 9, GRAY_D)
    frame = (
        '<g transform="rotate(11 380 300)">'
        + R(282, 190, 196, 220, 12, WOOD_D)
        + R(298, 206, 164, 188, 8, WHITE)
        + P("M 298 352 Q 360 300 420 352 L 462 352 L 462 394 L 298 394 Z", GREEN_L)
        + C(430, 250, 22, SUN)
        + "</g>")
    strings = wrap(
        L(380, 132, 296, 194, GRAY_D, 4),
        L(380, 132, 456, 172, GRAY_D, 4))
    swing = wrap(
        P("M 500 330 q 18 14 4 32", stroke=GRAY, w=6),
        P("M 524 310 q 26 20 6 46", stroke=GRAY, w=6))
    return g + nail + strings + frame + swing


def arts():
    return {
        "品": a_pin(), "晶": a_jing(), "灶": a_zao(), "灭": a_mie(),
        "掰": a_bai(), "岩": a_yan(), "歪": a_wai(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    lg_spec = importlib.util.spec_from_file_location(
        "lg_huiyi", str(ROOT.parent / "识字卡片_素材_huiyi.py"))
    lg = importlib.util.module_from_spec(lg_spec)
    lg_spec.loader.exec_module(lg)
    legacy_chars = {c["char"] for c in lg.GROUP_CARDS}
    all_chars = []
    for grp in ziku.GROUPS:
        if grp["id"] == "huiyi":
            all_chars = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in all_chars if c not in legacy_chars]
    assert set(all_chars) == legacy_chars | set(expect), "legacy 覆盖与字库对不上"
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"会意字组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}），legacy 已含 {len(legacy_chars)} 字")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对（去掉 legacy 17 字）：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != c["tone"]]
    print(f"拼音/声调：{'与拼音表逐一一致 ✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len(c["sentence"]) - 1 <= 10)]
    miss = [c["char"] for c in GROUP_CARDS if c["char"] not in c["sentence"]]
    print(f"三段长度：{'全部 ≤30 ✓' if not lens else str(lens)}")
    print(f"句长 4–10：{'全部达标 ✓' if not sl else str(sl)}")
    print(f"句含目标字：{'全部 ✓' if not miss else str(miss)}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
        if not v.startswith("<ellipse"):
            bad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
