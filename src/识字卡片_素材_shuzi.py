#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画——数字组（13 字）：一二三四五六七八九十两半百。

数数规律：每个数字卡画恰好 N 个同一物件，排列整齐一眼可数（十=2×5 两排）；
相邻数字换物件（球→星→花轮换），两=两条小鱼，半=切成两半的苹果，
百=10×10 小圆点点阵。图上不出现任何数字或文字。
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_shuzi", os.path.join(_HERE, "识字卡片_素材库.py"))


# ---------- 排列小工具 ----------
def row(n, cx, gap):
    """一行 n 个物件的水平中心 x 列表。"""
    return [cx + (i - (n - 1) / 2) * gap for i in range(n)]


BALL_COLORS = {
    "teal": (lib.TEAL, lib.TEAL_D, lib.TEAL_L),
    "blue": (lib.BLUE, lib.BLUE_D, "#a8d4ef"),
    "red": (lib.RED, lib.RED_D, lib.PINK),
    "yel": (lib.YEL, lib.YEL_D, "#f9dc8f"),
}


def balls_at(pts, r, color):
    m, d, h = BALL_COLORS[color]
    return "".join(lib.ball(x, y, r, m, d, h) for x, y in pts)


def stars_at(pts, r, fill):
    return "".join(lib.star5(x, y, r, fill) for x, y in pts)


def flowers_at(pts, r, petal, core=lib.SUN):
    return "".join(lib.flower5(x, y, r, petal, core) for x, y in pts)


# ---------- 小鱼（「两」卡专用） ----------
def fish(cx, cy, s=1.0, body=lib.RED, dark=lib.RED_D, fin=lib.YEL):
    """小鱼：头朝右，圆眼圆腮，圆润友好。"""
    g = lib.PG([(cx - 58 * s, cy), (cx - 102 * s, cy - 36 * s), (cx - 102 * s, cy + 36 * s)], fin)
    g += lib.E(cx + 3 * s, cy + 5 * s, 72 * s, 44 * s, dark)
    g += lib.E(cx - 2 * s, cy - 3 * s, 71 * s, 43 * s, body)
    tail_y = cy - 38 * s
    g += lib.P(f"M {cx - 26 * s} {cy - 40 * s} Q {cx + 4 * s} {cy - 72 * s} {cx + 36 * s} {tail_y} "
               f"L {cx - 26 * s} {cy - 40 * s} Z", fin)  # 背鳍
    g += lib.E(cx + 4 * s, cy + 14 * s, 16 * s, 10 * s, fin)  # 侧鳍
    g += lib.P(f"M {cx + 30 * s} {cy - 22 * s} Q {cx + 22 * s} {cy} {cx + 30 * s} {cy + 20 * s}",
               stroke=dark, w=5 * s, opacity=0.55)  # 鱼鳃线
    g += lib.C(cx + 40 * s, cy - 10 * s, 8.5 * s, lib.WHITE)
    g += lib.C(cx + 42 * s, cy - 10 * s, 4.5 * s, lib.INK)
    g += lib.P(f"M {cx + 62 * s} {cy + 6 * s} Q {cx + 55 * s} {cy + 13 * s} {cx + 47 * s} {cy + 11 * s}",
               stroke=lib.INK, w=4 * s)  # 小嘴
    return g


# ---------- 苹果（「半」卡专用） ----------
def _apple_dome(cx, cy, s, mirror, fill):
    """半个苹果的外皮轮廓：平边贴在 x=cx，鼓包朝 mirror 方向。"""

    def x(v):
        return cx + v * s * mirror

    def y(v):
        return cy + v * s

    d = (f"M {cx} {y(-78)} "
         f"C {x(30)} {y(-92)} {x(96)} {y(-72)} {x(112)} {y(-28)} "
         f"C {x(126)} {y(10)} {x(112)} {y(56)} {x(78)} {y(76)} "
         f"C {x(56)} {y(89)} {x(24)} {y(84)} {cx} {y(78)} Z")
    return lib.P(d, fill)


def _apple_flesh(cx, cy, s, mirror):
    """切面：奶黄果肉，比外皮窄一圈，露出红皮边。"""

    def x(v):
        return cx + v * s * mirror

    def y(v):
        return cy + v * s

    d = (f"M {cx} {y(-74)} "
         f"C {x(26)} {y(-84)} {x(84)} {y(-66)} {x(98)} {y(-26)} "
         f"C {x(110)} {y(8)} {x(98)} {y(50)} {x(68)} {y(68)} "
         f"C {x(49)} {y(80)} {x(21)} {y(76)} {cx} {y(71)} Z")
    return lib.P(d, "#fbeec9")


def card_ban():
    g = lib.ground()
    cy = 350
    flesh = "#fbeec9"
    # 左半：外皮面（平边朝右）
    g += _apple_dome(330, cy, 1.0, -1, lib.RED_D)
    g += _apple_dome(324, cy, 1.0, -1, lib.RED)
    g += lib.PG([(324, cy - 70), (338, cy - 64), (338, cy + 64), (324, cy + 70)], flesh)
    # 右半：切面（平边朝左，果肉 + 籽）
    g += _apple_dome(414, cy, 1.0, 1, lib.RED)
    g += _apple_flesh(414, cy, 1.0, 1)
    g += lib.drop(414 + 38, cy - 2, 9, lib.INK)
    g += lib.drop(414 + 62, cy + 22, 9, lib.INK)
    # 左半顶上的果柄和小叶
    g += lib.L(320, cy - 84, 310, cy - 112, "#8a5a33", 9)
    g += (f'<g transform="rotate(-30 294 {cy - 108})">'
          + lib.E(294, cy - 108, 19, 9, lib.GREEN) + "</g>")
    return g


def card_bai():
    g = lib.ground()
    # 白色点阵板（浅青衬边），点小而密但清楚
    g += lib.R(202, 140, 356, 344, 32, lib.PANEL_T)
    g += lib.R(214, 152, 332, 320, 26, lib.WHITE)
    dots = ""
    for i in range(10):
        for j in range(10):
            dots += lib.C(380 + (j - 4.5) * 30, 314 + (i - 4.5) * 28, 8, lib.RED)
    return g + dots


def card_liang():
    g = lib.ground()
    g += lib.E(380, 384, 316, 76, "#cfe9f6")  # 小池塘
    g += lib.P("M 200 408 Q 226 398 252 408", stroke=lib.WBLUE, w=6)
    g += lib.P("M 508 408 Q 534 398 560 408", stroke=lib.WBLUE, w=6)
    g += fish(296, 350, 0.92)
    g += fish(464, 350, 0.92)
    return g


# ---------- 数字卡场景 ----------
def card_one():
    return lib.ground() + lib.ball(380, 346, 72)


def card_two():
    return lib.ground() + stars_at([(288, 340), (472, 340)], 58, lib.SUN)


def card_three():
    return lib.ground() + flowers_at([(232, 342), (380, 342), (528, 342)], 34, "#f0876f")


def card_four():
    pts = [(305, 290), (455, 290), (305, 396), (455, 396)]
    return lib.ground() + balls_at(pts, 50, "blue")


def card_five():
    g = lib.ground()
    g += flowers_at([(232, 292), (380, 292), (528, 292)], 32, "#9cc9e2")
    g += flowers_at([(306, 396), (454, 396)], 32, "#9cc9e2")
    return g


def card_six():
    g = lib.ground()
    g += stars_at([(240, 288), (380, 288), (520, 288)], 42, lib.TEAL)
    g += stars_at([(240, 394), (380, 394), (520, 394)], 42, lib.TEAL)
    return g


def card_seven():
    g = lib.ground()
    g += balls_at([(x, 288) for x in row(4, 380, 128)], 48, "red")
    g += balls_at([(x, 394) for x in row(3, 380, 128)], 48, "red")
    return g


def card_eight():
    g = lib.ground()
    g += flowers_at([(x, 292) for x in row(4, 380, 128)], 32, "#9cc98a", lib.RED)
    g += flowers_at([(x, 396) for x in row(4, 380, 128)], 32, "#9cc98a", lib.RED)
    return g


def card_nine():
    g = lib.ground()
    g += stars_at([(x, 288) for x in row(5, 380, 116)], 40, lib.PINK)
    g += stars_at([(x, 394) for x in row(4, 380, 116)], 40, lib.PINK)
    return g


def card_ten():
    g = lib.ground()
    g += balls_at([(x, 290) for x in row(5, 380, 116)], 42, "yel")
    g += balls_at([(x, 392) for x in row(5, 380, 116)], 42, "yel")
    return g


# 组卡片文案数据（不含种子字）
GROUP_CARDS = [
    {"char": "一", "pinyin": "yī", "tone": "第一声",
     "sentence": "一个皮球拍一拍。",
     "say": "指着一个球告诉宝宝：一个，就是一。",
     "chat": "家里还有什么只有一个的？",
     "life": "拿一个橘子放桌上，指着说一。"},
    {"char": "二", "pinyin": "èr", "tone": "第四声",
     "sentence": "一加一等于二。",
     "say": "两颗星星排一排，数一数，一、二。",
     "chat": "你有两只小手，数给妈妈听听。",
     "life": "伸出两根手指，比一个二。"},
    {"char": "三", "pinyin": "sān", "tone": "第一声",
     "sentence": "花园里开着三朵花。",
     "say": "三朵花，一起数：一、二、三。",
     "chat": "我们家一共有几口人呀？",
     "life": "搭三块积木，边搭边数到三。"},
    {"char": "四", "pinyin": "sì", "tone": "第四声",
     "sentence": "地上滚着四个皮球。",
     "say": "四个球摆成方方正正的两排，是四。",
     "chat": "小汽车有几个轮子，你数过吗？",
     "life": "挑四颗豆子，摆成一个方块。"},
    {"char": "五", "pinyin": "wǔ", "tone": "第三声",
     "sentence": "花园里开着五朵花。",
     "say": "五朵花，上面三朵，下面两朵。",
     "chat": "一只手有几根手指头？",
     "life": "张开小手，一根一根数到五。"},
    {"char": "六", "pinyin": "liù", "tone": "第四声",
     "sentence": "六颗星星排成两排。",
     "say": "六颗星星，一排三颗，共两排。",
     "chat": "六和五比，谁多一点呀？",
     "life": "搭六块积木，两排每排三块。"},
    {"char": "七", "pinyin": "qī", "tone": "第一声",
     "sentence": "七个皮球滚过来。",
     "say": "七个球，上面四个，下面三个。",
     "chat": "一个星期有几天，猜猜看？",
     "life": "上楼梯时数台阶，数到七歇一歇。"},
    {"char": "八", "pinyin": "bā", "tone": "第一声",
     "sentence": "八朵花儿开满园。",
     "say": "八朵花，两排一样多，都是四朵。",
     "chat": "螃蟹有好几条腿，像不像八？",
     "life": "摆八颗豆子，两颗两颗数。"},
    {"char": "九", "pinyin": "jiǔ", "tone": "第三声",
     "sentence": "九颗星星亮晶晶。",
     "say": "九颗星，上面五颗，下面四颗。",
     "chat": "九个球拿走一个，还剩几个？",
     "life": "拍九下皮球，边拍边大声数。"},
    {"char": "十", "pinyin": "shí", "tone": "第二声",
     "sentence": "十个皮球排两排。",
     "say": "十个球，两排各五个，数到十。",
     "chat": "你有十根手指，对不对？",
     "life": "数数自己的十根手指和脚趾。"},
    {"char": "两", "pinyin": "liǎng", "tone": "第三声",
     "sentence": "两条小鱼游啊游。",
     "say": "两条小鱼在游泳，两个也叫两。",
     "chat": "两只眼睛和两只耳朵，一样多吗？",
     "life": "拿两个苹果，一手一个掂一掂。"},
    {"char": "半", "pinyin": "bàn", "tone": "第四声",
     "sentence": "半个苹果分你吃。",
     "say": "苹果切成一样大的两份，每份是半。",
     "chat": "半个苹果再加半个，是几个？",
     "life": "掰开饼干，你一半我一半。"},
    {"char": "百", "pinyin": "bǎi", "tone": "第三声",
     "sentence": "一百个点点排整齐。",
     "say": "十个一排，十排就是一百个点。",
     "chat": "一百比十多好多，是吗？",
     "life": "数豆子，数十颗放一堆，数数几堆。"},
]


def arts():
    return {
        "一": card_one(),
        "二": card_two(),
        "三": card_three(),
        "四": card_four(),
        "五": card_five(),
        "六": card_six(),
        "七": card_seven(),
        "八": card_eight(),
        "九": card_nine(),
        "十": card_ten(),
        "两": card_liang(),
        "半": card_ban(),
        "百": card_bai(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    ziku = _load("scys_ziku_shuzi", os.path.join(_HERE, "识字卡片_字库.py"))
    grp = next(g for g in ziku.GROUPS if g["id"] == "shuzi")
    expect = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    mine = [c["char"] for c in GROUP_CARDS]
    assert mine == expect, f"卡序与字库不一致：{mine} vs {expect}"

    cards = arts()
    assert set(cards) == set(mine), "arts 键与 GROUP_CARDS 不一致"
    punct = "，。！？、；：·—…"
    for c in GROUP_CARDS:
        ch = c["char"]
        core = [t for t in c["sentence"] if t not in punct]
        assert 4 <= len(core) <= 10, f"{ch} sentence 长度 {len(core)}"
        assert ch in c["sentence"], f"{ch} sentence 未含目标字"
        for k in ("say", "chat", "life"):
            assert len(c[k]) <= 30, f"{ch} {k} 超长：{len(c[k])}"
        v = cards[ch]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            assert bad not in v, f"{ch} 含禁止标记 {bad}"
    print(f"数字组：卡数 {len(GROUP_CARDS)}，arts {len(cards)}，与字库比对一致 ✓")
