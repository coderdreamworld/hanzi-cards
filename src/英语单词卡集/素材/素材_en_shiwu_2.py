#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 食物·饮品（shiwu）第 2 段插画（第 12~21 卡：cookie~yogurt）。

每卡造型要点：cookie 棕曲奇缺一角+深色巧克力豆 / chocolate 深棕排块掰开一格露浅色内层 /
lollipop 红白螺旋大圆糖+白棒+蓝蝴蝶结 / hamburger 芝麻顶包+生菜+肉饼+番茄分层 /
pizza 黄芝士红肠片整圆+右上角掀起拉丝 / French fries 红盒金黄薯条斜插 /
popcorn 红白条纹桶爆满白花+两粒飞出 / dumpling 白胖饺子堆成小山木笼屉褶子清楚 /
mooncake 棕黄花纹圆饼切一角露蛋黄馅 / yogurt 白粉酸奶杯插勺杯口滴挂。
主体居中放大（55%~75%），主色相邻错开，高光一律同族浅色椭圆。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "cookie", "cn": "曲奇"},
    {"w": "chocolate", "cn": "巧克力"},
    {"w": "lollipop", "cn": "棒棒糖"},
    {"w": "hamburger", "cn": "汉堡"},
    {"w": "pizza", "cn": "披萨"},
    {"w": "French fries", "cn": "薯条"},
    {"w": "popcorn", "cn": "爆米花"},
    {"w": "dumpling", "cn": "饺子"},
    {"w": "mooncake", "cn": "月饼"},
    {"w": "yogurt", "cn": "酸奶"},
]


# ---------- 本组同族补充色 ----------
COO, COO_L = "#dfa96b", "#f0d2a0"                              # 曲奇棕（WOOD 族）
CHO, CHO_D, CHO_IN, CHO_S = "#7c4a2a", "#63381e", "#a4764e", "#8f5a36"  # 深巧克力（棕族深）
STICK, STICK_D = "#f2e9d4", "#d9c9a8"                          # 糖棒暖白（PAGE 族）
BUN_S = "#f7e3b8"                                              # 芝麻/包面高光（WOOD_L 族浅）
PATTY, PATTY_D = "#9c6238", "#7c4a2a"                          # 肉饼棕（棕族）
CHEESE, CHEESE_L = "#f6c95e", "#f8dd9a"                        # 芝士黄（SUN 族）
CRUST, CRUST_D, CAKE_F, CAKE_L, PATT_IN = "#dda45f", "#c08348", "#e7b678", "#ecd3a0", "#c98d4e"  # 烘焙棕（WOOD 族）
FILL = "#8a5a33"                                               # 月饼馅（库内深棕）
FRY_D = "#a03320"                                              # 盒红加深（RED 族深）
PUFF_S = "#efe3c6"                                             # 爆米花阴影（暖白）
DUM, DUM_S, DUM_P = "#f7f0dd", "#d6c8a6", "#c4b28c"            # 饺皮暖白/阴影/褶线
PINKY, PINKY_D, PINKY_S = "#f9c2ab", "#e89c7f", "#eda284"      # 酸奶杯粉（PINK 族）
YOG = "#f7efe0"                                                # 酸奶暖白
YEL_L2 = "#f8d582"                                             # 黄族浅（草莓籽）
STEMG = "#5d8a52"                                              # 绿族深（果蒂）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色斜高光椭圆。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


# ---------- 12 cookie 棕曲奇缺一角 + 巧克力豆 ----------
def art_cookie():
    g = ground()
    g += C(376, 320, 132, WOOD_D)                                      # 投影
    g += C(368, 310, 132, COO)
    g += C(470, 225, 58, PAGE)                                         # 右上咬掉一角
    g += P("M 428 196 A 58 58 0 0 0 490 271", stroke=WOOD_L, w=8)      # 缺口断面
    for dx, dy in ((536, 196), (548, 238), (522, 168)):
        g += C(dx, dy, 5.5, COO)                                       # 掉渣
    for cx, cy in ((300, 250), (400, 262), (318, 352), (432, 338),
                   (372, 298), (272, 312), (392, 392), (302, 398)):
        g += C(cx, cy, 15, HAIR) + C(cx - 4, cy - 4, 4.5, "#8a6a4f", 0.9)  # 巧克力豆
    g += shine(306, 242, 36, 50, COO_L, 0.55, -24)
    return g


# ---------- 13 chocolate 深棕排块掰开一格 ----------
def art_chocolate():
    g = ground()
    # 主排块（4x2，右上格掰走），整体左倾
    bar = (R(-162, -85, 340, 190, 12, CHO_D)
           + R(-170, -95, 340, 190, 12, CHO)
           + R(-160, -88, 150, 78, 10, CHO_S, 0.55)                    # 左上光泽
           + L(-85, -95, -85, 95, CHO_D, 5) + L(0, -95, 0, 95, CHO_D, 5)
           + L(85, 6, 85, 95, CHO_D, 5) + L(-170, 0, 96, 0, CHO_D, 5))
    notch = P("M 88 -108 L 185 -108 L 185 14 L 110 10 L 104 -12 L 91 -10 L 87 -36 "
              "L 94 -42 L 88 -66 L 95 -72 L 85 -94 Z", PAGE)           # 掰掉一格的锯齿缺口
    g += f'<g transform="translate(352,312) rotate(-12)">{bar + notch}</g>'
    # 掰下的一格（右上方，断面浅色）
    piece = (R(-36, -37, 86, 92, 10, CHO_D)
             + R(-43, -46, 86, 92, 10, CHO)
             + R(-43, -40, 13, 80, 6, CHO_IN) + R(-36, 33, 72, 13, 6, CHO_IN)
             + C(-10, -16, 11, CHO_S, 0.7))
    g += f'<g transform="translate(555,184) rotate(14)">{piece}</g>'
    for dx, dy, r in ((508, 268, 6), (526, 246, 5), (498, 292, 4)):
        g += C(dx, dy, r, CHO)                                         # 碎屑
    return g


# ---------- 14 lollipop 红白螺旋大圆糖 + 白棒 + 蝴蝶结 ----------
def art_lollipop():
    g = ground()
    g += R(357, 374, 22, 74, 10, STICK_D, 0.8)                         # 棒影
    g += R(351, 370, 22, 76, 10, STICK)
    g += C(370, 257, 142, RED_D)
    g += C(362, 248, 142, RED) + C(362, 248, 118, WHITE)
    g += P("M 349 248 A 13 13 0 0 0 375 248 A 34 34 0 0 0 307 248 "
           "A 52 52 0 0 0 411 248 A 74 74 0 0 0 263 248 A 102 102 0 0 0 467 248 "
           "Q 470 168 394 136", stroke=RED, w=14)                      # 红螺旋
    g += shine(302, 184, 26, 16, WHITE, 0.5, -28)
    # 蝴蝶结
    g += P("M 354 404 L 308 386 Q 292 404 308 422 Z", BLUE)
    g += P("M 370 404 L 416 386 Q 432 404 416 422 Z", BLUE)
    g += P("M 356 416 L 342 446 L 358 440 Z", BLUE)
    g += P("M 368 416 L 382 446 L 366 440 Z", BLUE)
    g += R(352, 392, 20, 24, 8, BLUE_D)
    g += star5(516, 130, 18) + star5(214, 202, 12)
    return g


# ---------- 15 hamburger 芝麻顶包 / 生菜 / 肉饼 / 番茄分层 ----------
def art_hamburger():
    g = ground()
    g += R(246, 386, 268, 56, 26, WOOD_L)                              # 下包
    g += R(246, 424, 268, 18, 9, WOOD_D)
    g += R(238, 352, 284, 38, 18, RED)                                 # 番茄
    g += R(238, 378, 284, 12, 6, RED_D)
    g += R(234, 344, 292, 20, 9, YEL)                                  # 芝士+垂滴
    g += R(262, 358, 16, 30, 8, YEL) + R(348, 360, 16, 38, 8, YEL) + R(436, 358, 16, 26, 8, YEL)
    g += R(228, 306, 304, 50, 24, PATTY)                               # 肉饼
    g += R(228, 340, 304, 14, 7, PATTY_D)
    for dx in (300, 372, 444):
        g += C(dx, 326, 4.5, PATTY_D, 0.8)
    g += P("M 214 282 L 546 282 L 546 296 Q 522 316 498 296 Q 474 318 450 296 "
           "Q 426 318 402 296 Q 378 316 354 296 Q 330 318 306 296 Q 282 316 258 296 "
           "Q 234 314 214 296 Z", GREEN)                               # 生菜垂边
    g += P("M 210 278 Q 206 168 380 164 Q 554 168 550 278 Q 468 292 380 290 "
           "Q 292 292 210 278 Z", WOOD_L)                              # 顶包
    for sx, sy, rot in ((280, 208, -20), (340, 186, 10), (410, 196, 24), (470, 216, 30),
                        (320, 238, -12), (390, 244, 8), (452, 248, 18), (262, 244, -24),
                        (498, 248, 20)):
        g += shine(sx, sy, 7, 4.5, BUN_S, 0.95, rot)                   # 芝麻
    g += shine(300, 206, 38, 22, BUN_S, 0.5, -18)
    return g


# ---------- 16 pizza 黄芝士红肠片一角掀起拉丝 ----------
def art_pizza():
    g = ground()
    g += C(365, 303, 150, WOOD_D)
    g += C(356, 292, 150, CRUST) + C(356, 292, 133, RED, 0.9) + C(356, 292, 124, CHEESE)
    for tx, ty in ((226, 245), (231, 350), (481, 350), (403, 422), (476, 223)):
        g += C(tx, ty, 8, CRUST_D, 0.75)                               # 饼边焦斑
    for px, py in ((300, 232), (420, 244), (356, 318), (272, 320), (446, 326), (368, 192)):
        g += C(px, py, 25, RED_D) + C(px, py, 21, RED) + C(px - 7, py - 7, 4.5, "#f0876f", 0.85)
    for hx, hy, rot in ((330, 270, -20), (400, 292, 14), (320, 352, 30), (372, 240, -8), (304, 300, 12)):
        g += shine(hx, hy, 6, 3, GREEN, 0.9, rot)                      # 香草碎
    # 右上角掀起的一角 + 拉丝
    g += P("M 440 206 Q 472 196 488 212 Q 494 228 474 238 Q 448 242 440 226 Z", CHEESE_L)
    g += P("M 452 214 Q 486 176 520 168", stroke=CHEESE_L, w=6)
    g += P("M 476 226 Q 508 196 540 186", stroke=CHEESE_L, w=6)
    g += P("M 498 238 Q 530 214 556 204", stroke=CHEESE_L, w=6)
    slice_p = (R(-58, -14, 116, 30, 14, CRUST)
               + PG([(-58, 16), (58, 16), (0, 86)], CHEESE) + C(0, 42, 12, RED))
    g += f'<g transform="translate(600,132) rotate(35)">{slice_p}</g>'
    return g


# ---------- 17 French fries 红盒金黄薯条斜插 ----------
def art_fries():
    g = ground()
    g += PG([(280, 272), (444, 272), (452, 298), (272, 298)], FRY_D)   # 盒口内暗
    sticks = ((-42, 312, 326, 297, 186, 30, 155, YEL_D, None),
              (-30, 330, 330, 315, 160, 30, 190, YEL, None),
              (-16, 362, 336, 347, 138, 30, 210, SUN_L, 352),
              (-4, 394, 338, 379, 150, 30, 200, YEL, 384),
              (10, 424, 334, 409, 156, 30, 190, SUN_L, 414),
              (26, 446, 330, 431, 168, 30, 175, YEL_D, None),
              (40, 452, 326, 437, 190, 30, 150, YEL, None))
    for a, bx, by, x, y, w, h, col, lx in sticks:
        s = R(x, y, w, h, 14, col)
        if lx:
            s += L(lx, y + 14, lx, y + h - 24, "#fbd98c", 6)
        g += f'<g transform="rotate({a} {bx} {by})">{s}</g>'
    g += PG([(272, 298), (452, 298), (428, 442), (296, 442)], RED)     # 盒正面
    g += PG([(452, 298), (486, 320), (462, 442), (428, 442)], RED_D)   # 盒侧面
    g += PG([(272, 298), (452, 298), (449, 326), (275, 326)], WHITE)
    g += '<g transform="rotate(-12 566 424)">' + R(518, 410, 100, 27, 13, SUN_L) \
        + L(526, 417, 604, 417, "#fbd98c", 5) + "</g>"                 # 掉落一根
    return g


# ---------- 18 popcorn 红白条纹桶爆满白花 + 两粒飞出 ----------
def art_popcorn():
    g = ground()
    g += E(380, 288, 100, 16, "#8f2b1c")                               # 桶口暗
    for px, py, r in ((302, 258, 30), (348, 236, 32), (398, 232, 34),
                      (448, 250, 30), (482, 274, 24), (272, 284, 22)):
        g += C(px, py, r, PUFF_S)                                      # 后层米花
    for px, py, r in ((286, 272, 26), (332, 252, 30), (380, 224, 34), (430, 260, 28),
                      (464, 282, 22), (306, 290, 28), (354, 286, 30), (404, 292, 30),
                      (446, 298, 22), (352, 198, 24), (408, 204, 20)):
        g += C(px, py, r, WHITE)                                       # 前层米花
    for bx, by, r in ((368, 232, 5), (330, 262, 4), (412, 244, 4), (388, 282, 4),
                      (342, 216, 3.5), (430, 286, 3.5)):
        g += C(bx, by, r, "#f2c14e")                                   # 黄油点
    g += PG([(280, 296), (480, 296), (458, 442), (302, 442)], RED)     # 桶身
    g += PG([(314, 296), (342, 296), (350, 442), (328, 442)], WHITE)
    g += PG([(358, 296), (390, 296), (388, 442), (363, 442)], WHITE)
    g += PG([(412, 296), (444, 296), (430, 442), (405, 442)], WHITE)
    g += R(272, 276, 212, 28, 14, RED_D)                               # 桶沿
    # 飞出两粒
    g += C(196, 168, 20, WHITE) + C(181, 181, 11, WHITE) + C(208, 153, 9, PUFF_S)
    g += P("M 230 176 Q 246 168 256 156", stroke="#d9cfae", w=5)
    g += P("M 236 190 Q 250 186 258 178", stroke="#d9cfae", w=4)
    g += C(572, 206, 17, WHITE) + C(584, 218, 10, PUFF_S)
    g += P("M 540 210 Q 552 208 560 206", stroke="#d9cfae", w=4)
    return g


# ---------- 19 dumpling 白胖饺子木笼屉褶子清楚 ----------
def jiaozi(cx, cy, s):
    d = (f"M {cx-78*s:.0f} {cy+2*s:.0f} Q {cx-72*s:.0f} {cy+30*s:.0f} {cx-30*s:.0f} {cy+34*s:.0f} "
         f"L {cx+30*s:.0f} {cy+34*s:.0f} Q {cx+72*s:.0f} {cy+30*s:.0f} {cx+78*s:.0f} {cy+2*s:.0f} "
         f"Q {cx+66*s:.0f} {cy-40*s:.0f} {cx+18*s:.0f} {cy-46*s:.0f} "
         f"Q {cx-34*s:.0f} {cy-50*s:.0f} {cx-64*s:.0f} {cy-16*s:.0f} "
         f"Q {cx-78*s:.0f} {cy-4*s:.0f} {cx-78*s:.0f} {cy+2*s:.0f} Z")
    pleats = ""
    for px, py in ((-34, -40), (-10, -46), (14, -44), (38, -36)):
        pleats += P(f"M {cx+px*s:.0f} {cy+py*s:.0f} Q {cx+(px-9)*s:.0f} {cy+(py+13)*s:.0f} "
                    f"{cx+(px-7)*s:.0f} {cy+(py+27)*s:.0f}", stroke=DUM_P, w=4*s)
    return (f'<g transform="translate({6*s:.0f},{7*s:.0f})">' + P(d, DUM_S) + "</g>"
            + P(d, DUM) + pleats)


def art_dumpling():
    g = ground()
    g += P("M 112 360 A 268 50 0 0 0 648 360 L 648 402 A 268 50 0 0 1 112 402 Z", WOOD)
    g += P("M 112 380 A 268 50 0 0 0 648 380", stroke=WOOD_D, w=5)     # 笼壁篾纹
    g += P("M 112 394 A 268 50 0 0 0 648 394", stroke=WOOD_D, w=4)
    g += E(380, 360, 268, 50, WOOD_L)                                  # 笼沿
    g += P("M 126 360 A 254 44 0 0 0 634 360", stroke=WOOD, w=5)       # 沿面篾纹
    g += P("M 150 360 A 230 34 0 0 0 610 360", stroke=WOOD_D, w=4)
    g += E(380, 360, 242, 42, "#9a6a3d")                               # 笼内
    g += jiaozi(310, 282, 1.25) + jiaozi(452, 276, 1.25)               # 后排两只
    g += jiaozi(381, 222, 1.3)                                         # 顶上一只
    g += jiaozi(278, 348, 1.55) + jiaozi(484, 342, 1.55)               # 前排两只大的
    g += P("M 352 158 Q 338 130 354 104 Q 368 82 356 52", stroke="#dcd3bd", w=7)
    g += P("M 414 152 Q 428 126 412 100 Q 400 80 410 50", stroke="#dcd3bd", w=7)
    return g


# ---------- 20 mooncake 棕黄花纹圆饼切一角露馅 ----------
def art_mooncake():
    import math
    g = ground()
    g += C(356, 300, 140, WOOD_D)
    for i in range(16):
        a = i * 22.5 - 180
        if -28 < a < 22:
            continue                                                   # 缺口处无花边
        g += C(348 + 132 * math.cos(math.radians(a)),
               292 + 132 * math.sin(math.radians(a)), 19, CRUST_D)
    g += C(348, 292, 140, CRUST) + C(348, 292, 116, CAKE_F)
    g += flower5(348, 292, 40, PATT_IN, "#b0763e")
    for dx, dy in ((410, 354), (348, 380), (286, 354), (260, 292),
                   (286, 230), (348, 204), (410, 230)):
        g += C(dx, dy, 6.5, PATT_IN)                                   # 周圈花纹点
    g += P("M 348 292 L 472 226 A 140 140 0 0 1 478 344 Z", PAGE)      # 切去一角
    g += PG([(348, 292), (468, 219), (472, 226)], CAKE_L)              # 切断面
    g += PG([(348, 292), (475, 352), (478, 344)], CAKE_L)
    wedge = (PG([(0, 0), (129.8, 52.4), (123.6, -65.7)], CRUST_D)
             + C(129.1, -27.4, 19, CRUST_D) + C(131.3, 13.8, 19, CRUST_D)
             + P("M 0 0 L 123.6 -65.7 A 140 140 0 0 1 129.8 52.4 Z", CRUST)
             + P("M 0 0 L 98.9 -52.6 A 112 112 0 0 1 103.9 42.0 Z", CAKE_F)
             + C(84.1, -17.9, 6.5, PATT_IN) + C(85.6, 9.0, 6.5, PATT_IN)
             + PG([(0, 0), (123.6, -65.7), (130.2, -53.3), (6.6, 12.4)], FILL)
             + C(64, -16, 22, SUN) + C(64, -16, 14, SUN_L))            # 切块露蛋黄馅
    g += f'<g transform="translate(596,352) rotate(30)">{wedge}</g>'
    for dx, dy, r in ((505, 300, 6), (520, 330, 5), (512, 268, 5)):
        g += C(dx, dy, r, CRUST)
    return g


# ---------- 21 yogurt 白粉酸奶杯插勺滴挂 ----------
def art_yogurt():
    g = ground()
    g += PG([(292, 258), (468, 258), (448, 442), (312, 442)], PINKY)   # 杯身
    g += PG([(428, 258), (468, 258), (448, 442), (408, 442)], PINKY_S)  # 右侧暗面
    g += PG([(300, 318), (460, 318), (455, 388), (305, 388)], "#fdf7ee")  # 白标
    g += C(380, 352, 22, RED) + E(380, 331, 13, 7, GREEN_L) + R(377, 320, 6, 10, 3, STEMG)
    for sx, sy in ((372, 350), (388, 354), (380, 362)):
        g += C(sx, sy, 2.5, YEL_L2)
    g += E(380, 258, 88, 20, PINKY_D) + E(380, 258, 76, 15, YOG)       # 杯口酸奶面
    g += L(420, 250, 468, 136, "#e8a13c", 23)                          # 勺柄
    g += E(472, 130, 13, 18, "#e8a13c")
    g += E(415, 257, 15, 6, "#d9c49a", 0.9)                            # 勺入酸奶处
    g += P("M 298 262 Q 292 298 302 322 Q 310 336 316 318 Q 322 290 314 264 Z", YOG)
    g += P("M 452 262 Q 458 286 452 304 Q 446 318 440 302 Q 436 280 444 262 Z", YOG)
    g += C(326, 352, 7, YOG)                                           # 滴落一滴
    g += star5(298, 176, 14) + C(474, 206, 6, SUN_L)
    return g


def arts():
    return {
        "cookie": art_cookie(),
        "chocolate": art_chocolate(),
        "lollipop": art_lollipop(),
        "hamburger": art_hamburger(),
        "pizza": art_pizza(),
        "French fries": art_fries(),
        "popcorn": art_popcorn(),
        "dumpling": art_dumpling(),
        "mooncake": art_mooncake(),
        "yogurt": art_yogurt(),
    }
