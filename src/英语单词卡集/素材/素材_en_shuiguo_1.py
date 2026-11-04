#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 水果（shuiguo）第 1 段插画（11 卡：apple~lemon）。

每卡造型要点：apple 大红圆果带叶柄 / banana 黄串三根蕉头带青 /
orange 深橙整果+右下切角露瓣 / pear 黄绿葫芦形带柄叶 / peach 粉桃中缝衬双叶 /
grape 紫一大串压顶大叶 / watermelon 深绿条纹整瓜+右侧半圆切面红瓤黑籽 /
strawberry 鲜红心形籽点密布绿叶托 / mango 橙芒斜卧+右侧切半露大核 /
pineapple 橙金格纹皮戴绿冠 / lemon 亮黄双脐整果+右侧切半露瓣。
整果居中放大，切口/切面一律作右下辅角，主次分明；主色相邻错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "apple", "cn": "苹果"},
    {"w": "banana", "cn": "香蕉"},
    {"w": "orange", "cn": "橙子"},
    {"w": "pear", "cn": "梨"},
    {"w": "peach", "cn": "桃子"},
    {"w": "grape", "cn": "葡萄"},
    {"w": "watermelon", "cn": "西瓜"},
    {"w": "strawberry", "cn": "草莓"},
    {"w": "mango", "cn": "芒果"},
    {"w": "pineapple", "cn": "菠萝"},
    {"w": "lemon", "cn": "柠檬"},
]


# ---------- 本组同族补充色 ----------
APPLE_L = "#f59b78"                                            # 红族浅（苹果高光）
YEL_L2 = "#f8d582"                                             # 黄族浅（蕉棱/草莓籽）
STEMG = "#5d8a52"                                              # 绿族深（果柄/叶脉）
ORANGE, ORANGE_D, ORANGE_L = "#e07f24", "#c96a18", "#f2a45c"   # 深橙（YEL/SUN 族）
PEAR, PEAR_D, PEAR_L = "#c2cd57", "#a2ad3e", "#e0e493"         # 黄绿（GREEN×YEL 族）
PEACH = PINK                                                   # 粉桃（粉族主色）
PEACH_D, PEACH_L = "#e08a6e", "#fcc7b2"                        # 粉族深/浅
GRAPE, GRAPE_D, GRAPE_L = "#a477c9", "#8759ad", "#c9a8e4"      # 紫（本组新族，按分配）
WMEL, WMEL_D, WMEL_ST = "#5f8c50", "#4d7440", "#3f6234"        # 瓜绿（GREEN 族深）
MELONF = "#e2574a"                                             # 瓜瓤红（RED 族变体）
MANGO, MANGO_D, MANGO_L = "#f09a3e", "#d97e26", "#f8c07a"      # 芒果橙（SUN 族）
PIT, PIT_D = "#f5e9cf", "#e3d2ae"                              # 芒核米白（WOOD_L 族）
PINE, PINE_D, PINE_L = "#f2a83c", "#d98a26", "#f8c877"         # 菠萝橙金（SUN 族）
LEM, LEM_D, LEM_L = "#f7cd4f", "#dfa92e", "#fae08a"            # 柠檬亮黄（SUN 族）
HEADG = "#7ba86d"                                              # 蕉头青（GREEN 族）


def leaf(cx, cy, ln, wd, rot, col=GREEN, vcol=STEMG):
    """椭圆叶 + 中脉，绕 (cx,cy) 旋转。"""
    return (f'<g transform="rotate({rot} {cx} {cy})">'
            + E(cx, cy, ln, wd, col)
            + L(cx - ln * 0.78, cy, cx + ln * 0.78, cy, vcol, 3.5)
            + "</g>")


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色斜高光椭圆。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


# ---------- 1 apple 大红圆果，叶柄完整 ----------
def art_apple():
    g = ground()
    g += E(389, 309, 128, 120, RED_D)
    g += E(380, 300, 126, 118, RED)
    g += E(380, 187, 24, 10, RED_D)                       # 顶部凹陷
    g += shine(318, 244, 36, 54, APPLE_L, 0.8, -26)
    g += shine(448, 356, 20, 12, APPLE_L, 0.5, 30)        # 右下反光
    g += P("M 380 190 Q 386 160 398 140", stroke=WOOD_D, w=13)
    g += leaf(446, 146, 42, 16, 26)
    return g


# ---------- 2 banana 黄串三根，蕉头带青 ----------
BAN_D = "M 388 158 Q 580.6 294.6 413.8 421.3 L 406.7 414.3 Q 467 291.8 380.2 176.3 Z"
BAN_RIDGE = "M 394 194 Q 480 293 410 398"


def art_banana():
    g = ground()
    # 三根同向弯月香蕉，绕蕉头扇形展开：深一号衬底 + 本体 + 浅棱线 + 深褐尾尖
    for a in (30, -30):
        g += f'<g transform="translate(7,9) rotate({a} 388 158)">' + P(BAN_D, YEL_D) + "</g>"
        g += (f'<g transform="rotate({a} 388 158)">' + P(BAN_D, YEL)
              + P(BAN_RIDGE, stroke=YEL_L2, w=5.5) + C(410, 417, 7, "#8a5a33") + "</g>")
    g += f'<g transform="translate(7,9)">' + P(BAN_D, YEL_D) + "</g>"
    g += P(BAN_D, YEL) + P(BAN_RIDGE, stroke=YEL_L2, w=5.5) + C(410, 417, 7, "#8a5a33")
    # 蕉头（断面青绿，盖住蕉柄收口）
    g += ('<g transform="rotate(-6 388 148)">' + E(388, 148, 40, 28, "#6b9a5c")
          + E(386, 144, 31, 20, HEADG) + E(386, 142, 16, 10.5, "#f5e2b0") + "</g>")
    return g


# ---------- 3 orange 深橙整果 + 右下切角露瓣 ----------
def art_orange():
    g = ground()
    g += E(358, 308, 126, 126, ORANGE_D)
    g += E(350, 300, 126, 126, ORANGE)
    g += C(350, 174, 10, STEMG) + C(350, 172, 6, GREEN_L)   # 顶部果蒂
    g += leaf(430, 148, 44, 17, 28)
    g += shine(296, 242, 34, 52, ORANGE_L, 0.7, -26)
    for dx, dy in ((302, 258), (408, 244), (322, 352), (414, 338), (360, 300), (282, 318)):
        g += C(dx, dy, 5, ORANGE_D, 0.4)                    # 皮孔
    # 切角：橙皮瓣 → 白络 → 三枚果瓣
    g += P("M 560 356 L 668 428 Q 712 370 686 310 Z", ORANGE_D)
    g += P("M 566 356 L 656 416 Q 692 368 672 320 Z", "#fdf3d6")
    g += PG([(572, 356), (646, 404), (654, 370)], ORANGE_L)
    g += PG([(572, 356), (650, 362), (646, 326)], ORANGE_L)
    g += PG([(572, 356), (632, 320), (610, 314)], ORANGE_L)
    return g


# ---------- 4 pear 黄绿葫芦形带柄叶 ----------
def art_pear():
    g = ground()
    g += E(388, 224, 60, 64, PEAR_D) + E(396, 338, 102, 92, PEAR_D)
    g += R(360, 262, 56, 84, 26, PEAR_D)
    g += E(380, 218, 58, 62, PEAR) + E(380, 330, 100, 90, PEAR)
    g += R(352, 256, 56, 84, 26, PEAR)
    g += E(382, 160, 14, 8, PEAR_D, 0.9)                   # 柄窝
    g += P("M 380 162 Q 388 138 396 118", stroke=WOOD_D, w=12)
    g += leaf(448, 128, 38, 15, 28)
    g += shine(330, 282, 26, 46, PEAR_L, 0.7, -22)
    for dx, dy in ((330, 300), (430, 322), (362, 380), (412, 270), (324, 252), (440, 286)):
        g += C(dx, dy, 4, PEAR_D, 0.5)                      # 果点
    return g


# ---------- 5 peach 粉桃中缝，衬双叶 ----------
def art_peach():
    g = ground()
    g += E(389, 313, 124, 116, PEACH_D)
    g += E(380, 304, 122, 114, PEACH)
    g += E(382, 194, 16, 7, PEACH_D)                                     # 顶部凹陷
    g += P("M 380 202 Q 402 300 380 414", stroke=PEACH_D, w=7)           # 中缝
    g += shine(318, 254, 36, 56, PEACH_L, 0.8, -24)
    g += leaf(462, 166, 46, 18, 30)
    g += leaf(298, 164, 40, 16, -32, GREEN_L)
    return g


# ---------- 6 grape 紫一大串，压顶大叶 ----------
def art_grape():
    g = ground()
    g += P("M 380 186 Q 386 156 394 126", stroke=WOOD_D, w=11)           # 果梗
    g += P("M 394 126 Q 424 108 440 120", stroke=STEMG, w=5)             # 卷须
    g += leaf(318, 148, 54, 23, -28)
    g += leaf(452, 162, 36, 15, 34, GREEN_L)
    rows = [[(380, 396)], [(348, 338), (412, 338)],
            [(314, 282), (380, 278), (446, 282)],
            [(282, 220), (348, 218), (414, 218), (480, 220)]]
    for row in rows:
        for x, y in row:
            g += C(x + 3, y + 4, 33, GRAPE_D)
            g += C(x, y, 32, GRAPE)
            g += C(x - 10, y - 10, 8, GRAPE_L, 0.8)
    return g


# ---------- 7 watermelon 深绿条纹整瓜 + 半圆切面红瓤黑籽 ----------
def art_watermelon():
    g = ground()
    # 整瓜（主）
    g += E(368, 314, 158, 120, WMEL_D)
    g += E(360, 306, 156, 118, WMEL)
    g += shine(298, 252, 44, 28, "#93c284", 0.55, -16)
    g += P("M 362 192 Q 346 306 362 420", stroke=WMEL_ST, w=16)
    g += P("M 292 210 Q 268 306 292 400", stroke=WMEL_ST, w=14)
    g += P("M 428 210 Q 452 306 428 400", stroke=WMEL_ST, w=14)
    g += P("M 247 266 Q 235 306 247 346", stroke=WMEL_ST, w=11)
    g += P("M 473 266 Q 485 306 473 346", stroke=WMEL_ST, w=11)
    g += P("M 366 192 Q 362 162 340 154 Q 322 150 320 164", stroke=STEMG, w=9)  # 卷须
    # 切面（辅）：瓜皮 → 白瓤层 → 红瓤 → 黑籽
    g += P("M 528 424 A 100 100 0 0 1 728 424 Z", WMEL)
    g += P("M 544 424 A 84 84 0 0 1 712 424 Z", WHITE)
    g += P("M 556 424 A 72 72 0 0 1 700 424 Z", MELONF)
    for sx, sy in ((600, 374), (656, 374), (628, 356), (614, 400), (644, 400)):
        g += E(sx, sy, 5, 7, INK)
    return g


# ---------- 8 strawberry 鲜红心形，籽点密布，绿叶托 ----------
def art_strawberry():
    g = ground()
    g += P("M 276 216 Q 276 156 380 156 Q 484 156 484 216 Q 484 324 380 430 Q 276 324 276 216 Z", RED_D)
    g += P("M 280 210 Q 280 150 380 150 Q 480 150 480 210 Q 480 316 380 422 Q 280 316 280 210 Z", RED)
    g += shine(322, 246, 30, 46, APPLE_L, 0.75, -22)
    for sx, sy in ((334, 232), (400, 228), (448, 264), (300, 278), (366, 272),
                   (432, 312), (338, 330), (396, 354), (304, 322), (362, 392), (412, 300)):
        g += E(sx, sy, 4.5, 7, YEL_L2)                       # 籽点
    # 绿叶托（萼片五出）+ 短柄
    for a, col in ((-75, GREEN_L), (-40, GREEN), (0, GREEN), (40, GREEN), (75, GREEN_L)):
        g += f'<g transform="rotate({a} 380 158)">{E(380, 128, 13, 36, col)}</g>'
    g += R(374, 100, 12, 46, 6, STEMG)
    return g


# ---------- 9 mango 橙芒斜卧 + 右侧切半露大核 ----------
def art_mango():
    g = ground()
    # 整芒（主，斜卧）
    g += ('<g transform="rotate(-16 330 316)">'
          + E(339, 324, 150, 104, MANGO_D) + E(330, 316, 148, 102, MANGO)
          + E(188, 306, 11, 9, "#8a5a33")
          + shine(276, 272, 36, 24, MANGO_L, 0.8, -14)
          + E(400, 310, 42, 26, PINK, 0.45)
          + "</g>")
    g += L(378, 206, 400, 180, STEMG, 8)
    g += leaf(426, 170, 42, 17, 32)
    # 切半（辅）：果皮边 → 浅色果肉 → 大果核带纤维
    g += P("M 556 216 Q 668 232 668 326 Q 668 420 556 432 L 556 412 Q 648 402 648 326 Q 648 244 556 236 Z", MANGO_D)
    g += P("M 556 236 Q 648 244 648 326 Q 648 402 556 412 Z", MANGO_L)
    g += E(604, 330, 30, 76, PIT) + E(604, 330, 21, 62, PIT_D)
    g += L(604, 282, 604, 304, "#d9c49a", 3) + L(604, 320, 604, 350, "#d9c49a", 3) + L(604, 366, 604, 384, "#d9c49a", 3)
    return g


# ---------- 10 pineapple 橙金格纹皮，戴绿冠 ----------
def art_pineapple():
    g = ground()
    # 绿冠（先画，果身压住基部）
    g += PG([(348, 202), (384, 196), (300, 96)], GREEN_L)
    g += PG([(346, 202), (378, 206), (286, 140)], STEMG)
    g += PG([(376, 198), (410, 202), (442, 88)], GREEN_L)
    g += PG([(380, 200), (412, 206), (474, 130)], STEMG)
    g += PG([(352, 200), (390, 198), (368, 78)], GREEN)
    # 果身
    g += R(284, 200, 208, 240, 74, PINE_D)
    g += R(276, 192, 208, 240, 74, PINE)
    g += shine(318, 306, 26, 94, PINE_L, 0.6)
    for x1, y1, x2, y2 in ((296, 296, 386, 206), (300, 388, 466, 222), (340, 420, 462, 298),
                           (392, 416, 456, 352), (374, 206, 464, 296), (294, 222, 460, 388),
                           (298, 298, 420, 420), (304, 352, 368, 416)):
        g += L(x1, y1, x2, y2, PINE_D, 5)
    return g


# ---------- 11 lemon 亮黄双脐整果 + 右侧切半露瓣 ----------
def art_lemon():
    g = ground()
    # 整果（主，微斜，两端果脐）
    g += ('<g transform="rotate(-14 320 306)">'
          + E(330, 314, 158, 130, LEM_D)
          + C(190, 314, 27, LEM_D) + C(458, 314, 27, LEM_D)
          + C(186, 306, 25, LEM) + C(454, 306, 25, LEM)
          + E(320, 306, 158, 130, LEM)
          + shine(258, 262, 36, 24, LEM_L, 0.8, -18)
          + "</g>")
    for dx, dy in ((356, 296), (398, 340), (300, 346)):
        g += C(dx, dy, 5, LEM_D, 0.35)
    g += L(408, 196, 428, 168, STEMG, 8)
    g += leaf(456, 152, 42, 17, 28)
    # 切半（辅）：皮 → 白络 → 果肉底 → 五枚放射果瓣
    g += P("M 578 210 A 112 112 0 0 1 578 434 Z", LEM_D)
    g += P("M 578 226 A 96 96 0 0 1 578 418 Z", "#fdf3d0")
    g += P("M 578 240 A 82 82 0 0 1 578 404 Z", LEM_L)
    seg = "#f6c94a"
    g += P("M 578 322 L 602.1 252.0 A 74 74 0 0 1 622.5 262.9 Z", seg)
    g += P("M 578 322 L 638.6 279.6 A 74 74 0 0 1 648.8 300.4 Z", seg)
    g += P("M 578 322 L 651.3 311.7 A 74 74 0 0 1 651.3 332.3 Z", seg)
    g += P("M 578 322 L 648.8 343.6 A 74 74 0 0 1 638.6 364.4 Z", seg)
    g += P("M 578 322 L 622.5 381.1 A 74 74 0 0 1 602.1 392.0 Z", seg)
    return g


def arts():
    return {
        "apple": art_apple(),
        "banana": art_banana(),
        "orange": art_orange(),
        "pear": art_pear(),
        "peach": art_peach(),
        "grape": art_grape(),
        "watermelon": art_watermelon(),
        "strawberry": art_strawberry(),
        "mango": art_mango(),
        "pineapple": art_pineapple(),
        "lemon": art_lemon(),
    }
