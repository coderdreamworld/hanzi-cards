#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""时间组补充 6 卡插画与文案（1000 字批次 B8）。

字表：秒季岁晨寒暑（legacy ../识字卡片_素材_shijian.py 已有 12+候 13 卡
年分时早午晚春夏秋冬今昨，本文件只做增量，不与 legacy 撞造型）。

一眼可辨约定（主控硬规则）：
秒=银灰秒表指针特写（区别 legacy 分=绿挂钟、时=红闹钟）/
季=四格小窗里同一棵树的四季（窗内无文字）/ 岁=生日蛋糕插 4 根小蜡烛 /
晨=朝阳+草叶露珠+小鸟（区别 legacy 早=地平线太阳+小花）/
寒=棉衣帽巾小孩+小雪人（区别 legacy 冬=雪人主角）/ 暑=大太阳+大折扇+一牙西瓜
（折扇放射褶一眼可辨，区别 legacy 夏=太阳+大牙西瓜，无扇）。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
STEEL, STEEL_D, STEEL_L = "#c3cad1", "#9aa3ac", "#eef1f4"   # 秒表金属
PINK_ICING = "#f5a58c"
SKY_SP, SKY_SU, SKY_AU, SKY_WI = "#e2f2e0", "#d5edf9", "#fdeecd", "#e8f1f8"
ORANGE = "#e8742a"


def _rot(x, y, deg, svg):
    return f'<g transform="rotate({deg} {x} {y})">{svg}</g>'


def _tr(x, y, deg, svg):
    """平移到位再旋转（内容以原点为中心）。"""
    return f'<g transform="translate({x},{y}) rotate({deg})">{svg}</g>'


def _sun_plain(cx, cy, r):
    """大太阳：八向光芒，无笑脸（区别 legacy 阳=笑脸三角光芒）。"""
    g = ""
    for i in range(8):
        a = math.radians(i * 45 + 10)
        x1, y1 = cx + (r + 14) * math.cos(a), cy + (r + 14) * math.sin(a)
        x2, y2 = cx + (r + 44) * math.cos(a), cy + (r + 44) * math.sin(a)
        g += L(x1, y1, x2, y2, YEL_D, 9)
    g += C(cx + r * 0.05, cy + r * 0.06, r, "#e2952a")
    g += C(cx - r * 0.04, cy - r * 0.04, r * 0.94, SUN)
    g += C(cx - r * 0.32, cy - r * 0.32, r * 0.2, SUN_L, 0.9)
    return g


# ---------- 各卡插画 ----------
def a_miao():
    """秒：银灰秒表指针特写，红秒针在跑。"""
    ticks = ""
    for i in range(12):
        a = math.radians(i * 30)
        r1, r2 = 96, 110
        x1, y1 = 380 + r1 * math.sin(a), 292 - r1 * math.cos(a)
        x2, y2 = 380 + r2 * math.sin(a), 292 - r2 * math.cos(a)
        ticks += L(x1, y1, x2, y2, INK, 6 if i % 3 == 0 else 3.5)
    hx, hy = 380 + 104 * math.sin(math.radians(40)), 292 - 104 * math.cos(math.radians(40))
    return wrap(
        ground(380, 446, 235, 24),
        R(358, 116, 44, 40, 10, STEEL_D),              # 表冠
        R(350, 102, 60, 20, 9, STEEL),
        f'<g transform="translate(264,194) rotate(-50)">'
        + R(-15, -28, 30, 56, 13, STEEL_D) + "</g>",   # 左按钮
        f'<g transform="translate(496,194) rotate(50)">'
        + R(-15, -28, 30, 56, 13, STEEL_D) + "</g>",   # 右按钮
        C(388, 298, 154, STEEL_D),
        C(380, 292, 152, STEEL),
        C(380, 292, 124, STEEL_L),
        C(380, 292, 118, WHITE),
        ticks,
        L(380, 292, hx, hy, RED, 11),                  # 红秒针
        L(380, 292, 372, 312, RED, 7),
        C(380, 292, 11, "#e8a13c"),
    )


def _tree(cx, base, season):
    """同一棵小树，四季四样（窗内无文字）。"""
    g = R(cx - 13, base - 76, 26, 80, 9, WOOD_D)
    if season == "spring":
        g += C(cx, base - 104, 40, "#a8d8a0")
        g += C(cx - 34, base - 84, 28, "#bfe3b4") + C(cx + 34, base - 84, 28, "#bfe3b4")
        for dx, dy in ((-16, -122), (10, -134), (26, -108)):
            g += C(cx + dx, base + dy, 8, "#f5b8c4")
    elif season == "summer":
        g += C(cx, base - 110, 46, GREEN)
        g += C(cx - 38, base - 88, 32, GREEN) + C(cx + 38, base - 88, 32, GREEN)
        g += C(cx, base - 132, 28, GREEN_L)
    elif season == "autumn":
        g += C(cx, base - 104, 40, "#e8963c")
        g += C(cx - 34, base - 84, 28, "#f2b53c") + C(cx + 34, base - 84, 28, "#d4552f")
    else:  # winter
        g += L(cx, base - 60, cx - 34, base - 98, WOOD_D, 9)
        g += L(cx, base - 52, cx + 36, base - 92, WOOD_D, 9)
        g += L(cx, base - 76, cx, base - 112, WOOD_D, 9)
        g += E(cx, base - 116, 26, 9, WHITE)
    return g


def a_ji():
    """季：四格小窗，同一棵树的四季（无文字）。"""
    wins = ((84, 56, SKY_SP, "spring"), (404, 56, SKY_SU, "summer"),
            (84, 246, SKY_AU, "autumn"), (404, 246, SKY_WI, "winter"))
    g = ground(380, 448, 250, 22)
    for x, y, sky, season in wins:
        g += R(x - 10, y - 10, 300, 194, 24, WOOD_L)   # 窗框
        g += R(x, y, 280, 174, 16, sky)
        if season == "winter":
            g += E(x + 140, y + 158, 130, 22, WHITE)   # 积雪
        else:
            g += E(x + 140, y + 158, 130, 22, "#9cc98a")
        g += _tree(x + 140, y + 158, season)
    return g


def a_sui():
    """岁：生日蛋糕插 4 根小蜡烛。"""
    candles = ""
    for i, (cx, col) in enumerate(((317, RED), (359, TEAL), (401, YEL), (443, BLUE))):
        candles += R(cx - 7, 242, 14, 84, 7, col)
        candles += C(cx, 226, 15, SUN_L, 0.4)          # 火苗光晕
        candles += E(cx, 226, 9, 14, SUN) + C(cx, 231, 4.5, ORANGE)
    return wrap(
        ground(380, 446, 250, 22),
        E(380, 436, 186, 20, "#e3ded2"),
        E(380, 430, 176, 18, WHITE),
        R(252, 330, 256, 100, 22, "#f6dfae"),          # 蛋糕身
        R(252, 322, 256, 34, 16, PINK_ICING),          # 顶上糖霜
        E(300, 358, 14, 10, PINK_ICING), E(352, 362, 12, 9, PINK_ICING),
        E(412, 358, 14, 10, PINK_ICING), E(462, 352, 11, 8, PINK_ICING),
        candles,
        C(300, 396, 7, "#f2c14e"), C(380, 404, 7, "#7cc8bb"), C(456, 394, 7, "#f2c14e"),
    )


def a_chen():
    """晨：朝阳爬上山坡 + 草叶露珠 + 小鸟。"""
    g = ground(380, 446, 260, 24)
    g += _sun_plain(290, 396, 84)
    g += P("M 270 380 Q 290 400 310 380", stroke=INK, w=6)      # 太阳笑脸
    g += C(268, 372, 6, INK) + C(312, 372, 6, INK)
    g += E(300, 466, 262, 40, "#9cc98a")                        # 山坡挡住日头
    g += L(560, 438, 560, 424, INK, 4) + L(578, 438, 578, 424, INK, 4)
    g += E(574, 400, 36, 26, "#e8663c")                         # 小鸟
    g += C(602, 380, 20, "#e8663c")
    g += C(607, 376, 3.5, INK)
    g += PG([(621, 378), (638, 383), (621, 388)], YEL_D)        # 喙
    g += _rot(568, 396, -22, E(568, 396, 20, 12, RED_D))        # 翅膀
    g += PG([(542, 396), (518, 386), (540, 406)], RED_D)        # 尾巴
    g += L(468, 440, 460, 400, GREEN, 7) + L(486, 440, 496, 404, GREEN, 7)
    g += _rot(508, 414, 28, E(508, 414, 22, 10, GREEN_L))       # 草叶
    g += drop(460, 386, 12) + C(456, 381, 4, WHITE, 0.8)        # 露珠
    g += drop(494, 382, 10) + C(491, 378, 3.4, WHITE, 0.8)
    return g


def a_han():
    """寒：棉衣帽巾小孩 + 旁边小雪人。"""
    kid_extra = wrap(
        P("M 292 158 Q 294 96 350 92 Q 406 96 408 158 "
          "Q 350 178 292 158 Z", TEAL),                  # 毛线帽
        R(288, 150, 124, 26, 12, TEAL_D),
        C(350, 86, 15, WHITE),                           # 帽球
        R(312, 252, 76, 24, 11, YEL),                    # 围巾
        R(384, 262, 22, 48, 9, YEL),
        C(283, 344, 17, TEAL), C(417, 344, 17, TEAL),    # 手套
    )
    snowman = wrap(
        C(578, 424, 35, "#d7e5ee"), C(575, 420, 34, WHITE),
        C(578, 378, 24, "#d7e5ee"), C(575, 375, 23, WHITE),
        C(567, 371, 3, INK), C(583, 371, 3, INK),
        PG([(575, 377), (601, 381), (575, 385)], ORANGE),
        C(575, 408, 3, INK), C(575, 420, 3, INK),
        L(552, 398, 528, 384, "#8a5a33", 5),
    )
    flakes = ""
    for fx, fy, fr in ((150, 130, 7), (238, 84, 5), (600, 120, 6), (660, 240, 5), (120, 280, 5)):
        flakes += C(fx, fy, fr, "#cfe0ec")
    return wrap(
        ground(380, 446, 270, 24, "#e3eef5"),
        flakes,
        C(578, 426, 38, "#cfe0ec"),                      # 雪人影子底
        snowman,
        kid(350, 438, s=1.05, pose="stand", shirt=RED, face="smile",
            arms="down", extra=kid_extra),
    )


def a_shu():
    """暑：大太阳 + 大折扇（放射褶最好认，不会读成叶子）+ 一牙西瓜。"""
    px, py = 505, 396
    R1, R2 = 26, 148
    fan = P("M "
            + " L ".join(
                f"{px + R1 * math.sin(math.radians(b)):.1f} {py - R1 * math.cos(math.radians(b)):.1f}"
                for b in range(-152, -27, 31))
            + " L " + " L ".join(
                f"{px + R2 * math.sin(math.radians(b)):.1f} {py - R2 * math.cos(math.radians(b)):.1f}"
                for b in range(-28, -153, -31))
            + " Z", RED)
    ribs = ""
    for i in range(9):
        b = -152 + i * 15.5
        ribs += L(px + R1 * math.sin(math.radians(b)), py - R1 * math.cos(math.radians(b)),
                  px + R2 * math.sin(math.radians(b)), py - R2 * math.cos(math.radians(b)),
                  "#c9611f", 3.5)
    return wrap(
        ground(380, 446, 250, 24),
        _sun_plain(170, 124, 62),
        fan,
        ribs,
        C(px, py, 11, WOOD_D),                          # 扇钉
        R(px - 9, py + 4, 18, 40, 8, WOOD),             # 扇柄
        _tr(195, 392, -8, wrap(
            P("M -80 0 C -71 56 -37 78 0 78 C 37 78 71 56 80 0 Z", GREEN),
            P("M -68 0 C -60 46 -32 64 0 64 C 32 64 60 46 68 0 Z", RED),
            drop(-34, 30, 8, INK), drop(0, 44, 8, INK), drop(34, 30, 8, INK))),
        P("M 408 208 Q 396 238 410 268", stroke="#9cc98a", w=6),   # 摇扇弧
        P("M 432 194 Q 418 228 434 260", stroke="#9cc98a", w=6),
    )


def arts():
    return {
        "秒": a_miao(), "季": a_ji(), "岁": a_sui(),
        "晨": a_chen(), "寒": a_han(), "暑": a_shu(),
    }


GROUP_CARDS = [
    {"char": "秒", "pinyin": "miǎo", "tone": "第三声",
     "sentence": "秒针跑一圈六十秒。",
     "say": "跑步计时用的就是秒表。",
     "chat": "秒针跑一圈是多长时间呀？",
     "life": "按按秒表，数数十秒。"},
    {"char": "季", "pinyin": "jì", "tone": "第四声",
     "sentence": "一年有四个季节。",
     "say": "同一棵树，春夏秋冬变了样。",
     "chat": "你最喜欢哪个季节呀？",
     "life": "出门看看现在是什么季节。"},
    {"char": "岁", "pinyin": "suì", "tone": "第四声",
     "sentence": "过生日，长一岁。",
     "say": "过一次生日就长大一岁。",
     "chat": "你今年几岁啦？",
     "life": "生日蛋糕前许个愿。"},
    {"char": "晨", "pinyin": "chén", "tone": "第二声",
     "sentence": "清晨小鸟吱吱叫。",
     "say": "太阳刚爬上来就是清晨。",
     "chat": "清晨的草叶上有什么呀？",
     "life": "早晨起来向太阳问个好。"},
    {"char": "寒", "pinyin": "hán", "tone": "第二声",
     "sentence": "天寒地冻穿棉衣。",
     "say": "冷得缩手缩脚就是寒。",
     "chat": "寒天出门要穿什么呀？",
     "life": "戴上帽子围巾再出门。"},
    {"char": "暑", "pinyin": "shǔ", "tone": "第三声",
     "sentence": "暑天热得摇扇子。",
     "say": "太阳最毒最热就是暑天。",
     "chat": "暑天吃什么最凉快呀？",
     "life": "热了就摇摇小扇子。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "shijian" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B8"] if e["file"] == "素材1000_shijian.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"时间组补充：卡数 {len(GROUP_CARDS)}")
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
