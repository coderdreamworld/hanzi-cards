#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 自然·天气（ziran）第 2 段插画（11 卡：flower~stone）。

每卡造型要点：flower 向日葵大花盘十二瓣 / grass 草丛摇曳点小花 / leaf 大绿叶脉络清楚 /
seed 种子剖面破土双叶嫩芽 / forest 松林前后层叠 / mountain 青山连绵雪顶 / river 蜿蜒河岸石头 /
lake 平静湖面倒映青山 / sea 大海波浪海鸥飞 / beach 沙滩遮阳伞贝壳海星 / stone 灰石苔点。
主体居中放大，主色相邻错开；只画图形不画任何文字。
"""
import math
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "flower", "cn": "花"},
    {"w": "grass", "cn": "草"},
    {"w": "leaf", "cn": "叶子"},
    {"w": "seed", "cn": "种子"},
    {"w": "forest", "cn": "森林"},
    {"w": "mountain", "cn": "山"},
    {"w": "river", "cn": "河"},
    {"w": "lake", "cn": "湖"},
    {"w": "sea", "cn": "海"},
    {"w": "beach", "cn": "沙滩"},
    {"w": "stone", "cn": "石头"},
]


# ---------- 本组同族补充色 ----------
GRN_D = "#699756"                                              # 深草绿（GREEN 族深）
SAND = "#f2d9a4"                                               # 沙（YEL 族浅）
SAND_SH = "#e0bf8a"                                            # 沙影（YEL 族中）
GRAY_C, GRAY_D, GRAY_L = "#9aa4ad", "#868f99", "#b3bac1"       # 石灰三档（金属灰族）
SOIL, SOIL_D = "#b58756", "#8a5f3a"                            # 土剖面（WOOD 族变体）
SEED_C, SEED_L = "#9c6b3d", "#c99a6a"                          # 种子棕（WOOD 族变体）
DEEPSEA = "#61a9d4"                                            # 深层海（WBLUE 族中深）
SHELL = "#f7d0b8"                                              # 贝壳（PINK 族浅）
PINK_D = "#e08a6e"                                             # 贝纹深粉（PINK 族深）
CORE_C, CORE_D = "#8a5a33", "#6b4a28"                          # 葵花籽芯（WOOD 族深）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色高光椭圆（可旋转）。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


def pine(cx, base, s, leaf=GREEN, dark=None):
    """小松树：干+三层三角冠。"""
    dark = dark or GRN_D
    g = R(cx - 10 * s, base - 40 * s, 20 * s, 44 * s, 6 * s, WOOD_D)
    g += PG([(cx - 52 * s, base - 36 * s), (cx, base - 140 * s), (cx + 52 * s, base - 36 * s)], leaf)
    g += PG([(cx - 42 * s, base - 98 * s), (cx, base - 188 * s), (cx + 42 * s, base - 98 * s)], dark)
    g += PG([(cx - 30 * s, base - 150 * s), (cx, base - 226 * s), (cx + 30 * s, base - 150 * s)], leaf)
    return g


def tuft(x, y, s=1.0):
    """一小撮草叶。"""
    return (P(f"M {x} {y} Q {x - 7 * s} {y - 18 * s} {x} {y - 32 * s}", stroke=GREEN, w=6 * s)
            + P(f"M {x + 12 * s} {y} Q {x + 18 * s} {y - 16 * s} {x + 14 * s} {y - 28 * s}",
                stroke=GRN_D, w=5 * s))


# ---------- 12 flower 向日葵大花盘 ----------
def art_flower():
    g = ground()
    g += R(372, 300, 16, 132, 7, GREEN)                         # 茎
    g += '<g transform="rotate(-24 330 362)">' + E(330, 362, 44, 18, GREEN) + "</g>"   # 叶
    g += '<g transform="rotate(24 432 336)">' + E(432, 336, 44, 18, GREEN) + "</g>"
    for i in range(12):                                         # 十二瓣
        g += f'<g transform="rotate({i * 30} 380 250)">' + E(380, 152, 21, 44, SUN) + "</g>"
    g += C(380, 250, 78, CORE_C)                                # 籽芯
    for x, y, r in ((356, 232, 5), (398, 228, 5), (378, 262, 5), (404, 256, 5),
                    (352, 266, 5), (380, 226, 5), (416, 240, 4.5), (344, 248, 4.5)):
        g += C(x, y, r, CORE_D)                                 # 籽点
    g += E(350, 218, 18, 10, SEED_L, 0.6)
    return g


# ---------- 13 grass 草丛点小花 ----------
def art_grass():
    g = ground()
    for d, w, col in ((("M 380 444 Q 366 380 392 300"), 15, GREEN),
                      (("M 380 444 Q 344 392 326 348"), 13, GREEN),
                      (("M 380 444 Q 416 396 436 350"), 13, GREEN),
                      (("M 380 444 Q 330 424 302 402"), 11, GRN_D),
                      (("M 380 444 Q 432 428 462 406"), 11, GRN_D),
                      (("M 380 444 Q 354 404 344 368"), 11, GREEN),
                      (("M 380 444 Q 404 408 414 372"), 11, GREEN),
                      (("M 380 444 Q 316 446 288 440"), 10, GRN_D),
                      (("M 380 444 Q 446 448 476 442"), 10, GRN_D)):
        g += P(d, stroke=col, w=w)                              # 主草丛
    for x, y in ((250, 446), (516, 446)):
        g += tuft(x, y, 1.1) + tuft(x - 26, y + 2, 0.85) + tuft(x + 26, y + 2, 0.85)
    g += flower5(310, 348, 15)
    g += flower5(448, 330, 17)
    g += flower5(222, 414, 11)
    g += flower5(508, 396, 12, petal=WHITE, core=SUN)
    return g


# ---------- 14 leaf 大绿叶脉络清楚 ----------
def art_leaf():
    g = ground()
    g += P("M 380 430 Q 262 380 268 262 Q 274 152 380 120 Q 486 152 492 262 "
           "Q 498 380 380 430 Z", GREEN)                        # 叶身
    g += L(380, 430, 380, 460, GRN_D, 12)                       # 叶柄
    g += L(380, 424, 380, 136, GRN_D, 10)                       # 主脉
    for y in (196, 244, 292, 340, 388):                         # 侧脉五对
        g += L(380, y, 304, y - 32, GRN_D, 6)
        g += L(380, y, 456, y - 32, GRN_D, 6)
    g += shine(322, 232, 30, 58, GREEN_L, 0.55, 16)
    return g


# ---------- 15 seed 种子剖面破土嫩芽 ----------
def art_seed():
    g = ground()
    g += P("M 210 442 L 210 396 Q 210 380 230 380 L 530 380 Q 550 380 550 396 "
           "L 550 442 Q 380 466 210 442 Z", SOIL)               # 土剖面
    g += R(212, 372, 336, 12, 6, GREEN_L)                       # 土面草皮
    g += E(380, 414, 30, 21, SEED_C)                            # 种子
    g += E(372, 406, 12, 8, SEED_L, 0.85)
    g += L(380, 408, 380, 300, GREEN, 11)                       # 破土的芽茎
    g += '<g transform="rotate(-28 352 288)">' + E(352, 288, 34, 16, GREEN_L) + "</g>"   # 双叶
    g += '<g transform="rotate(28 408 288)">' + E(408, 288, 34, 16, GREEN_L) + "</g>"
    g += E(380, 288, 12, 18, GREEN)                             # 顶芽
    g += C(366, 378, 6, SOIL_D) + C(396, 376, 5, SOIL_D) + C(424, 382, 4, SOIL_D)   # 土粒
    return g


# ---------- 16 forest 松林前后层叠 ----------
def art_forest():
    g = ground()
    for cx in (170, 310, 450, 590):                             # 后排小深绿
        g += pine(cx, 438, 0.75, GRN_D, GREEN)
    g += pine(250, 450, 1.2, GREEN)                             # 前排大
    g += pine(470, 450, 1.2, GREEN)
    g += pine(640, 444, 0.95, GREEN)
    return g


# ---------- 17 mountain 青山连绵雪顶 ----------
def art_mountain():
    g = ground()
    g += PG([(120, 424), (320, 210), (520, 424)], GRN_D)        # 后山
    g += PG([(284, 258), (320, 210), (356, 258), (338, 250), (320, 264), (302, 250)], WHITE)
    g += PG([(276, 434), (500, 172), (724, 434)], GREEN)        # 主峰
    g += PG([(454, 230), (500, 172), (546, 230), (526, 220), (500, 238), (474, 220)], WHITE)
    g += E(625, 442, 125, 28, GREEN_L, 0.9)                     # 前丘
    g += PG([(180, 448), (208, 394), (236, 448)], GREEN) + R(200, 448, 12, 12, 4, WOOD_D)
    g += P("M 296 148 Q 306 140 316 148 Q 326 140 336 148", stroke=INK, w=5)   # 飞鸟
    g += P("M 356 176 Q 364 170 372 176 Q 380 170 388 176", stroke=INK, w=5)
    return g


# ---------- 18 river 蜿蜒河岸石头 ----------
def art_river():
    g = ground()
    g += P("M 50 480 L 50 330 Q 220 316 340 366 Q 430 402 520 372 Q 610 344 710 372 "
           "L 710 480 Z", GREEN_L)                              # 草岸
    g += P("M 96 480 Q 130 420 240 400 Q 350 384 380 440 Q 406 486 520 470 "
           "Q 640 452 700 480 Z", WBLUE)                        # 蜿蜒河带
    g += P("M 200 420 Q 250 410 300 420", stroke=WHITE, w=5, opacity=0.8)
    g += P("M 360 452 Q 410 444 460 452", stroke=WHITE, w=5, opacity=0.8)
    g += P("M 540 462 Q 580 456 620 462", stroke=WHITE, w=5, opacity=0.8)
    g += E(160, 452, 26, 15, GRAY_C)                            # 岸石
    g += E(214, 462, 17, 11, GRAY_L)
    g += E(575, 430, 22, 13, GRAY_C)
    g += C(252, 466, 8, GRAY_L)
    return g


# ---------- 19 lake 平静湖面倒映青山 ----------
def art_lake():
    g = ground()
    g += PG([(150, 336), (330, 196), (510, 336)], GREEN)        # 背山一
    g += PG([(390, 336), (540, 214), (690, 336)], GRN_D)        # 背山二
    g += E(380, 390, 282, 62, WBLUE)                            # 湖
    g += E(380, 388, 262, 52, "#a5d9f0")
    g += P("M 302 340 L 458 340 L 380 408 Z", BLUE, opacity=0.4)   # 山倒影
    g += P("M 300 382 Q 380 370 460 382", stroke=WHITE, w=6, opacity=0.8)
    g += P("M 340 406 Q 380 398 420 406", stroke=WHITE, w=5, opacity=0.7)
    g += tuft(150, 456, 1.0) + tuft(614, 456, 1.0)
    return g


# ---------- 20 sea 大海波浪海鸥 ----------
def art_sea():
    g = ground()
    g += P("M 40 302 Q 120 288 200 304 Q 280 320 360 304 Q 440 288 520 304 "
           "Q 600 320 680 304 L 720 302 L 720 480 L 40 480 Z", WBLUE)   # 海
    g += P("M 40 372 Q 200 358 380 372 Q 560 386 720 372 L 720 480 L 40 480 Z", DEEPSEA)
    g += P("M 140 322 Q 190 310 240 322", stroke=WHITE, w=6, opacity=0.85)
    g += P("M 330 330 Q 380 318 430 330", stroke=WHITE, w=6, opacity=0.85)
    g += P("M 520 324 Q 570 312 620 324", stroke=WHITE, w=6, opacity=0.85)
    g += C(200, 300, 8, WHITE) + C(400, 302, 8, WHITE) + C(600, 300, 8, WHITE)
    g += P("M 296 172 Q 311 158 326 172 Q 341 158 356 172", stroke=INK, w=6)   # 海鸥
    g += P("M 430 216 Q 441 206 452 216 Q 463 206 474 216", stroke=INK, w=5)
    g += P("M 548 148 Q 558 140 568 148 Q 578 140 588 148", stroke=INK, w=5)
    return g


# ---------- 21 beach 沙滩遮阳伞贝壳 ----------
def art_beach():
    g = ground()
    g += P("M 40 300 L 720 300 L 720 348 Q 560 360 380 346 Q 200 332 40 352 Z", WBLUE)   # 近海
    g += P("M 40 352 Q 200 332 380 346 Q 560 360 720 344 L 720 480 L 40 480 Z", SAND)   # 沙滩
    g += P("M 70 350 Q 200 338 360 348", stroke=WHITE, w=6, opacity=0.8)
    g += L(480, 354, 480, 210, WOOD_D, 10)                      # 伞杆
    g += P("M 356 244 Q 480 150 604 244 Q 576 232 548 244 Q 518 232 480 244 "
           "Q 442 232 412 244 Q 384 232 356 244 Z", RED)        # 伞盖
    g += P("M 480 152 Q 430 188 416 244", stroke=RED_D, w=5)
    g += P("M 480 152 Q 530 188 544 244", stroke=RED_D, w=5)
    g += E(480, 404, 92, 13, SAND_SH, 0.7)                      # 伞影
    g += P("M 252 434 Q 252 402 282 398 Q 312 402 312 434 Q 282 444 252 434 Z", SHELL)   # 贝壳
    g += L(282, 400, 282, 432, PINK_D, 4)
    g += L(264, 408, 274, 432, PINK_D, 3.5)
    g += L(300, 408, 290, 432, PINK_D, 3.5)
    g += star5(372, 448, 16, PINK)                              # 海星
    g += C(580, 442, 10, GRAY_L)
    return g


# ---------- 22 stone 灰石苔点 ----------
def art_stone():
    g = ground()
    g += P("M 220 434 Q 210 340 292 296 Q 360 266 444 296 Q 516 326 512 400 "
           "Q 514 438 468 444 Q 350 470 220 434 Z", GRAY_C)     # 大石
    g += shine(320, 342, 62, 30, GRAY_L, 0.9, -12)              # 亮面
    g += shine(436, 358, 30, 18, GRAY_L, 0.7, -8)
    g += P("M 352 320 Q 360 376 350 442", stroke=GRAY_D, w=5)   # 石缝
    for x, y, r in ((272, 420, 8), (306, 438, 6), (418, 434, 8), (466, 416, 6), (376, 448, 5)):
        g += C(x, y, r, GREEN_L)                                # 苔点
    g += E(570, 448, 38, 18, GRAY_L)                            # 小石
    g += E(630, 456, 22, 12, GRAY_C)
    g += tuft(252, 452, 0.9)
    return g


def arts():
    return {
        "flower": art_flower(),
        "grass": art_grass(),
        "leaf": art_leaf(),
        "seed": art_seed(),
        "forest": art_forest(),
        "mountain": art_mountain(),
        "river": art_river(),
        "lake": art_lake(),
        "sea": art_sea(),
        "beach": art_beach(),
        "stone": art_stone(),
    }
