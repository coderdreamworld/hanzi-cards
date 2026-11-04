#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 蔬菜（shucai）第 1 段插画（10 卡：tomato~garlic）。

每卡造型要点：tomato 亮红圆果绿蒂 / potato 土黄椭圆半埋土丘露芽眼 /
carrot 橙锥形露半截戴绿缨 / corn 黄棒籽粒排齐须缨披着苞叶裹底 /
cabbage 浅绿圆球层层包叶 / broccoli 深绿伞花簇粗茎 / mushroom 红伞白点伞下褶 /
pumpkin 橙扁圆棱沟带藤 / onion 紫洋葱层皮根须 / garlic 白蒜头旁掰一瓣。
整物居中放大，主色相邻错开；高光一律同族浅色椭圆。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "tomato", "cn": "西红柿"},
    {"w": "potato", "cn": "土豆"},
    {"w": "carrot", "cn": "胡萝卜"},
    {"w": "corn", "cn": "玉米"},
    {"w": "cabbage", "cn": "卷心菜"},
    {"w": "broccoli", "cn": "西兰花"},
    {"w": "mushroom", "cn": "蘑菇"},
    {"w": "pumpkin", "cn": "南瓜"},
    {"w": "onion", "cn": "洋葱"},
    {"w": "garlic", "cn": "大蒜"},
]


# ---------- 本组同族补充色 ----------
STEMG = "#5d8a52"                                              # 绿族深（果柄/叶脉）
APPLE_L = "#f59b78"                                            # 红族浅（番茄/蘑菇高光）
ORANGE, ORANGE_D, ORANGE_L = "#e07f24", "#c96a18", "#f2a45c"   # 橙族（胡萝卜/南瓜）
POTATO, POTATO_D, POTATO_L = "#cfa05e", "#b9884a", "#e6c084"   # 土黄（WOOD 族）
MOUND, MOUND_D = "#9c6b3c", "#855a30"                          # 土丘（WOOD 族深）
YEL_L2 = "#f8d582"                                             # 黄族浅
CORN_D = "#bd8a1e"                                             # 黄族深（玉米棒阴影）
SILK = "#f0d9a6"                                               # 玉米须（黄族浅）
LEAFD = "#6f9c60"                                              # 绿族深（包叶外缘）
CABB_HL = "#c8e4b6"                                            # 绿族浅（包叶内层/高光）
BROC, BROC_D, BROC_L = "#57874b", "#47703d", "#79a86a"         # 深绿（GREEN 族深）
STALK, STALK_D = "#c9e0a6", "#aec98c"                          # 茎浅绿（GREEN 族浅）
CREAM, CREAM_D, CREAM_L = "#f4ead2", "#e0d0ae", "#fbf6ea"      # 米白（蘑菇柄/蒜皮）
GILL = "#cdb78e"                                               # 菌褶（米白族深）
ROOTS = "#d9c49a"                                              # 根须/干茎（同族米黄）
GRAPE, GRAPE_D, GRAPE_L = "#a477c9", "#8759ad", "#c9a8e4"      # 紫族（洋葱）


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


# ---------- 1 tomato 亮红圆果，绿蒂短梗 ----------
def art_tomato():
    g = ground()
    g += E(389, 313, 130, 122, RED_D)
    g += E(380, 305, 129, 121, RED)
    g += E(380, 190, 30, 12, RED_D)                      # 顶部凹陷
    # 绿蒂：四片萼片披在果肩 + 蒂心 + 短梗
    for a, col in ((-64, GREEN_L), (-32, GREEN), (32, GREEN_L), (64, GREEN)):
        g += f'<g transform="rotate({a} 380 204)">{E(380, 240, 9.5, 38, col)}</g>'
    g += C(380, 202, 11, STEMG)
    g += L(380, 200, 380, 158, STEMG, 11)
    g += shine(310, 254, 36, 54, APPLE_L, 0.8, -26)
    g += shine(452, 360, 20, 12, APPLE_L, 0.5, 30)       # 右下反光
    return g


# ---------- 2 potato 土黄椭圆半埋土丘，芽眼点 ----------
def art_potato():
    g = ground()
    g += E(392, 312, 180, 130, POTATO_D)
    g += E(380, 304, 179, 129, POTATO)
    for x, y, r in ((452, 244, 10), (424, 332, 9), (490, 300, 8), (322, 332, 9), (276, 300, 8)):
        g += E(x, y, r, r * 0.72, "#8a5a33", 0.8)        # 芽眼
    g += shine(298, 240, 42, 26, POTATO_L, 0.8, -16)
    # 土色小丘（半埋效果，压住下半截）
    g += P("M 150 448 Q 255 376 380 372 Q 505 376 610 448 Z", MOUND)
    g += P("M 215 448 Q 310 408 380 406 Q 450 408 545 448 Z", MOUND_D)
    g += C(268, 424, 7, MOUND_D) + C(452, 428, 6, MOUND_D) + C(360, 434, 5, MOUND_D)
    return g


# ---------- 3 carrot 橙锥形露半截，戴绿缨 ----------
CARROT = ("M 324 192 Q 324 166 380 164 Q 436 166 436 192 Q 436 260 402 348 "
          "Q 386 390 380 452 Q 374 390 358 348 Q 324 260 324 192 Z")


def art_carrot():
    g = ground()
    inner = ""
    inner += f'<g transform="translate(7,9)">{P(CARROT, ORANGE_D)}</g>'
    inner += P(CARROT, ORANGE)
    inner += E(350, 250, 18, 66, ORANGE_L, 0.75)
    # 横向环纹
    inner += P("M 338 236 Q 380 248 422 236", stroke=ORANGE_D, w=5)
    inner += P("M 332 292 Q 380 304 428 292", stroke=ORANGE_D, w=5)
    inner += P("M 344 340 Q 380 350 416 340", stroke=ORANGE_D, w=5)
    # 绿缨：短梗 + 五叶扇
    inner += L(380, 168, 380, 142, STEMG, 9)
    inner += leaf(380, 130, 42, 13, 0, GREEN)
    inner += leaf(346, 140, 38, 12, -32, GREEN_L)
    inner += leaf(414, 140, 38, 12, 32, GREEN)
    inner += leaf(322, 156, 30, 10, -55, GREEN_L)
    inner += leaf(438, 156, 30, 10, 55, GREEN)
    g += f'<g transform="rotate(-10 380 300)">{inner}</g>'
    # 土丘盖住下截
    g += P("M 185 448 Q 280 380 380 376 Q 480 380 575 448 Z", MOUND)
    g += P("M 240 448 Q 325 412 380 410 Q 435 412 520 448 Z", MOUND_D)
    g += C(300, 426, 6, MOUND_D) + C(452, 430, 6, MOUND_D)
    return g


# ---------- 4 corn 黄棒籽粒排齐，须缨披着，苞叶裹底 ----------
def art_corn():
    g = ground()
    inner = ""
    # 苞叶（后层）
    inner += P("M 366 430 Q 282 442 220 402 Q 298 412 350 392 Z", GREEN_L)
    inner += P("M 394 430 Q 478 442 540 402 Q 462 412 410 392 Z", GREEN)
    # 棒体：阴影 + 底色（籽粒间隙色）
    inner += R(326, 168, 132, 264, 62, CORN_D)
    inner += R(314, 156, 132, 264, 62, YEL_D)
    # 籽粒网格（粒粒排齐）
    for r in range(8):
        for c in range(4):
            inner += R(323 + c * 29, 170 + r * 29, 25, 25, 9, YEL)
    inner += E(340, 190, 15, 22, YEL_L2, 0.65)
    # 须缨：顶部一撮 + 披在棒身两缕
    inner += P("M 380 168 Q 368 128 334 106", stroke=SILK, w=6)
    inner += P("M 380 168 Q 382 122 378 100", stroke=SILK, w=6)
    inner += P("M 380 168 Q 394 126 428 110", stroke=SILK, w=6)
    inner += P("M 400 178 Q 452 238 446 318", stroke=SILK, w=5.5)
    inner += P("M 362 176 Q 320 232 328 302", stroke=SILK, w=5)
    # 苞叶（前层裹底）
    inner += P("M 372 426 Q 330 452 266 450 Q 312 424 326 380 Q 352 400 372 426 Z", GREEN)
    inner += P("M 388 426 Q 430 452 494 450 Q 448 424 434 380 Q 408 400 388 426 Z", GREEN_L)
    inner += P("M 350 440 Q 380 456 410 440 Q 396 420 380 418 Q 364 420 350 440 Z", STEMG)
    return g + f'<g transform="rotate(8 380 300)">{inner}</g>'


# ---------- 5 cabbage 浅绿圆球，层层包叶 ----------
def art_cabbage():
    g = ground()
    g += E(392, 322, 137, 129, LEAFD)
    g += E(380, 314, 136, 128, GREEN)
    g += E(378, 312, 121, 114, GREEN_L)
    # 两侧外层包叶（深绿月牙）
    g += P("M 376 428 Q 262 424 222 330 Q 204 266 238 212 Q 240 300 286 356 Q 326 402 376 414 Z", GREEN)
    g += P("M 384 428 Q 498 424 538 330 Q 556 266 522 212 Q 520 300 474 356 Q 434 402 384 414 Z", GREEN)
    # 内层浅色月牙
    g += P("M 376 400 Q 300 394 268 338 Q 250 300 258 254 Q 270 322 308 360 Q 338 388 376 394 Z", CABB_HL)
    g += P("M 384 400 Q 460 394 492 338 Q 510 300 502 254 Q 490 322 452 360 Q 422 388 384 394 Z", CABB_HL)
    # 叶脉
    g += P("M 248 244 Q 284 318 350 376", stroke=STEMG, w=4)
    g += P("M 512 244 Q 476 318 410 376", stroke=STEMG, w=4)
    # 顶部叶尖
    g += leaf(336, 214, 36, 15, -42, GREEN)
    g += leaf(380, 198, 38, 16, 0, GREEN_L)
    g += leaf(424, 214, 36, 15, 42, GREEN)
    g += shine(320, 252, 40, 58, CABB_HL, 0.65, -28)
    return g


# ---------- 6 broccoli 深绿伞花簇，粗茎 ----------
def art_broccoli():
    g = ground()
    # 粗茎（深侧 + 亮面）
    g += P("M 356 290 L 344 424 Q 342 442 366 444 L 394 444 Q 418 442 416 424 L 404 290 Z", STALK_D)
    g += P("M 348 290 L 338 422 Q 336 438 358 440 L 386 440 Q 408 438 406 422 L 396 290 Z", STALK)
    # 分枝
    g += f'<g transform="rotate(-32 332 288)">{R(319, 260, 26, 54, 12, STALK)}</g>'
    g += f'<g transform="rotate(32 428 288)">{R(415, 260, 26, 54, 12, STALK)}</g>'
    # 伞花球（深一号衬底 + 本体）
    for dx, dy, r in ((388, 226, 86), (306, 258, 62), (452, 258, 62),
                      (344, 168, 46), (428, 172, 45), (256, 298, 40), (504, 298, 40)):
        g += C(dx + 6, dy + 8, r, BROC_D)
    for dx, dy, r in ((380, 218, 85), (300, 252, 61), (444, 252, 61),
                      (338, 164, 45), (422, 168, 43), (250, 292, 39), (498, 292, 39)):
        g += C(dx, dy, r, BROC)
    # 小伞簇颗粒
    for x, y, r in ((300, 236, 7), (268, 274, 6), (332, 204, 8), (378, 180, 8), (422, 190, 7),
                    (456, 234, 7), (486, 278, 6), (350, 248, 6), (402, 252, 7), (318, 288, 6),
                    (442, 288, 6), (382, 232, 6), (310, 306, 5), (452, 306, 5)):
        g += C(x, y, r, BROC_L)
    g += shine(330, 186, 24, 38, BROC_L, 0.5, -20)
    return g


# ---------- 7 mushroom 红伞白点，伞下褶 ----------
def art_mushroom():
    g = ground()
    # 菌柄 + 柄底
    g += R(346, 280, 68, 152, 28, CREAM)
    g += R(382, 280, 32, 152, 28, CREAM_D)
    g += E(380, 428, 44, 13, CREAM_D)
    # 伞下菌褶带 + 放射褶线
    g += E(380, 316, 140, 22, CREAM_D)
    for ex, ey in ((262, 322), (306, 330), (344, 336), (380, 338), (416, 336), (454, 330), (498, 322)):
        g += L(380, 316, ex, ey, GILL, 4)
    # 菌盖（深一号衬底 + 本体）
    g += P("M 234 302 Q 234 158 388 152 Q 542 158 542 302 Q 542 316 524 316 L 252 316 Q 234 316 234 302 Z", RED_D)
    g += P("M 226 296 Q 226 150 380 144 Q 534 150 534 296 Q 534 310 516 310 L 244 310 Q 226 310 226 296 Z", RED)
    # 白点
    for x, y, r in ((320, 208, 16), (420, 188, 13), (370, 250, 12), (470, 248, 14), (284, 262, 11),
                    (300, 176, 9), (452, 200, 9), (398, 232, 8), (508, 282, 8)):
        g += C(x, y, r, WHITE)
    g += shine(302, 198, 32, 44, APPLE_L, 0.5, -24)
    return g


# ---------- 8 pumpkin 橙扁圆棱沟，带藤 ----------
def art_pumpkin():
    g = ground()
    g += E(390, 320, 190, 134, ORANGE_D)
    g += E(380, 312, 189, 133, ORANGE)
    # 棱沟
    g += P("M 316 202 Q 290 312 316 422", stroke=ORANGE_D, w=11)
    g += P("M 380 182 Q 380 312 380 442", stroke=ORANGE_D, w=11)
    g += P("M 444 202 Q 470 312 444 422", stroke=ORANGE_D, w=11)
    g += P("M 252 242 Q 240 312 252 382", stroke=ORANGE_D, w=9)
    g += P("M 508 242 Q 520 312 508 382", stroke=ORANGE_D, w=9)
    g += shine(348, 298, 20, 92, ORANGE_L, 0.5, 4)
    # 顶部凹窝 + 短梗
    g += E(380, 188, 46, 15, ORANGE_D)
    g += f'<g transform="rotate(-8 380 160)">{R(365, 128, 30, 62, 13, STEMG)}{E(380, 130, 16, 7, "#466d3c")}</g>'
    # 卷须 + 小叶
    g += P("M 402 178 Q 458 158 474 124 Q 484 100 466 96 Q 452 94 454 112", stroke=STEMG, w=7)
    g += L(362, 150, 322, 156, STEMG, 6)
    g += leaf(296, 154, 30, 13, -24)
    return g


# ---------- 9 onion 紫洋葱，层皮根须 ----------
def art_onion():
    g = ground()
    g += E(392, 320, 132, 120, GRAPE_D)
    g += E(380, 312, 131, 119, GRAPE)
    # 层皮经线
    g += P("M 332 224 Q 300 314 332 402", stroke=GRAPE_D, w=8)
    g += P("M 380 196 Q 380 314 380 428", stroke=GRAPE_D, w=8)
    g += P("M 428 224 Q 460 314 428 402", stroke=GRAPE_D, w=8)
    g += P("M 272 270 Q 262 314 272 358", stroke=GRAPE_D, w=7)
    g += P("M 488 270 Q 498 314 488 358", stroke=GRAPE_D, w=7)
    g += shine(314, 262, 34, 54, GRAPE_L, 0.75, -26)
    # 顶部干茎
    g += P("M 362 210 Q 374 184 380 182 Q 386 184 398 210 Q 388 200 380 200 Q 372 200 362 210 Z", ROOTS)
    g += L(380, 184, 380, 158, ROOTS, 8)
    # 根须
    g += L(352, 414, 338, 448, ROOTS, 6)
    g += L(368, 422, 362, 454, ROOTS, 6)
    g += L(380, 426, 380, 458, ROOTS, 6)
    g += L(392, 422, 398, 454, ROOTS, 6)
    g += L(408, 414, 422, 448, ROOTS, 6)
    return g


# ---------- 10 garlic 白蒜头，旁边掰开一瓣 ----------
def art_garlic():
    g = ground()
    g += R(342, 150, 28, 54, 12, ROOTS)                  # 短柱顶
    # 蒜头（深一号衬底 + 本体）
    g += E(366, 316, 137, 121, CREAM_D)
    g += E(356, 308, 136, 120, CREAM)
    # 分瓣经线
    g += P("M 304 236 Q 290 314 306 398", stroke=CREAM_D, w=7)
    g += P("M 356 192 Q 356 314 356 426", stroke=CREAM_D, w=7)
    g += P("M 408 236 Q 422 314 406 398", stroke=CREAM_D, w=7)
    g += P("M 262 282 Q 256 314 264 354", stroke=CREAM_D, w=6)
    g += P("M 450 282 Q 456 314 448 354", stroke=CREAM_D, w=6)
    g += shine(288, 260, 32, 52, CREAM_L, 0.85, -24)
    # 根须
    g += L(330, 416, 322, 444, ROOTS, 5)
    g += L(352, 422, 350, 448, ROOTS, 5)
    g += L(374, 422, 378, 448, ROOTS, 5)
    g += L(396, 416, 404, 444, ROOTS, 5)
    # 旁边掰开的一瓣
    clove = ("M 484 322 Q 466 358 476 402 Q 486 436 524 438 Q 562 438 570 400 "
             "Q 576 358 554 318 Q 534 288 512 296 Q 494 302 484 322 Z")
    g += f'<g transform="translate(6,7)">{P(clove, CREAM_D)}</g>'
    g += P(clove, CREAM)
    g += P("M 504 314 Q 490 354 498 400", stroke=CREAM_D, w=6)
    g += P("M 510 300 Q 504 282 514 270 Q 522 284 520 300 Z", ROOTS)
    g += shine(538, 338, 15, 32, CREAM_L, 0.8, 14)
    return g


def arts():
    return {
        "tomato": art_tomato(),
        "potato": art_potato(),
        "carrot": art_carrot(),
        "corn": art_corn(),
        "cabbage": art_cabbage(),
        "broccoli": art_broccoli(),
        "mushroom": art_mushroom(),
        "pumpkin": art_pumpkin(),
        "onion": art_onion(),
        "garlic": art_garlic(),
    }
