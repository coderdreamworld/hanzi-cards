#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 衣物·穿戴（yifu）第 1 段插画（10 卡：T-shirt~sock）。

每卡造型要点：T-shirt 蓝短袖平铺领口袖口罗纹 / shirt 白衬衫尖领配红小领带钉扣 /
dress 红花裙挂木衣架钩露领口 / skirt 黄百褶裙腰头扇形褶线锯齿下摆 /
shorts 青绿运动短裤松紧腰抽绳侧白条 / pants 深蓝长裤立起腰头铜扣烫线 /
coat 橙大衣宽翻领一排扣袋盖 / jacket 棕黄夹克罗纹下摆拉链半开露内里 /
sweater 粉圆领麻花纹毛衣罗纹边 / sock 白底红黄青条花袜一双外八并排。
衣物平铺/挂起展示，主体占高 55%~65%，领口/袖口/下摆罗纹用深一号色，
褶皱同族深色弧线，高光同族浅色椭圆；主色相邻错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "T-shirt", "cn": "T恤"},
    {"w": "shirt", "cn": "衬衫"},
    {"w": "dress", "cn": "连衣裙"},
    {"w": "skirt", "cn": "短裙"},
    {"w": "shorts", "cn": "短裤"},
    {"w": "pants", "cn": "裤子"},
    {"w": "coat", "cn": "外套"},
    {"w": "jacket", "cn": "夹克"},
    {"w": "sweater", "cn": "毛衣"},
    {"w": "sock", "cn": "袜子"},
]


# ---------- 本组同族补充色 ----------
BLUE_L = "#a3d0ee"                       # 蓝族浅（高光）
BLUE_DD = "#3a7ba6"                      # 蓝族深（长裤阴影/烫线）
WHITE_D = "#e8e0cc"                      # 白族暖深（白衬衫/白袜阴影）
PLKT = "#f2ecd8"                         # 白族浅暖（门襟/口袋）
BTN = "#d9cfb8"                          # 白族深一档（衬衫扣）
RED_L = "#f59b78"                        # 红族浅（高光，同水果段）
FLW = "#fdf3d6"                          # 乳白（裙花花瓣/果络同族）
YEL_L2 = "#f8d582"                       # 黄族浅（高光）
ORANGE, ORANGE_D, ORANGE_L = "#e07f24", "#c96a18", "#f2a45c"   # 橙（SUN/YEL 族）
PINK_D, PINK_L = "#e08a6e", "#fcc7b2"    # 粉族深/浅
BROWN_BT = "#8a5a33"                     # 深棕（WOOD 族深：扣/夹克内里）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色斜高光椭圆。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


# ---------- 1 T-shirt 蓝短袖平铺，领口/袖口/下摆罗纹 ----------
TEE = ("M 350 170 Q 380 206 410 170 L 460 188 L 522 254 L 476 288 L 452 274 "
       "L 446 432 Q 380 444 314 432 L 308 274 L 284 288 L 238 254 L 300 188 Z")


def art_tshirt():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(TEE, BLUE_D) + "</g>"
    g += P(TEE, BLUE)
    g += P("M 344 168 Q 380 208 416 168 L 408 162 Q 380 196 352 162 Z", BLUE_D)  # 领口罗纹
    g += PG([(520, 252), (478, 286), (472, 278), (514, 248)], BLUE_D)             # 右袖口
    g += PG([(240, 252), (282, 286), (288, 278), (246, 248)], BLUE_D)             # 左袖口
    g += P("M 316 424 Q 380 436 444 424 L 442 432 Q 380 444 318 432 Z", BLUE_D)   # 下摆罗纹
    g += shine(336, 252, 22, 50, BLUE_L, 0.65, -12)
    g += P("M 338 302 Q 380 314 422 302", stroke=BLUE_D, w=4.5)                   # 褶皱
    g += P("M 346 354 Q 380 364 414 354", stroke=BLUE_D, w=4)
    return g


# ---------- 2 shirt 白衬衫尖领 + 红小领带 + 钉扣 ----------
SHIRT = ("M 346 166 Q 380 196 414 166 L 466 182 L 512 366 L 480 390 L 448 284 "
         "L 442 432 Q 380 444 318 432 L 312 284 L 280 390 L 248 366 L 294 182 Z")


def art_shirt():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(SHIRT, WHITE_D) + "</g>"
    g += P(SHIRT, WHITE)
    g += R(366, 166, 28, 272, 12, PLKT)                          # 门襟
    g += R(322, 238, 42, 36, 7, PLKT)                            # 左胸口袋
    g += PG([(510, 364), (482, 388), (474, 380), (502, 356)], WHITE_D)  # 袖口
    g += PG([(250, 364), (278, 388), (286, 380), (258, 356)], WHITE_D)
    # 尖领（深衬 + 白面）
    g += PG([(380, 174), (332, 160), (352, 206)], WHITE_D)
    g += PG([(380, 174), (428, 160), (408, 206)], WHITE_D)
    g += PG([(380, 172), (336, 158), (354, 200)], WHITE)
    g += PG([(380, 172), (424, 158), (406, 200)], WHITE)
    # 小领带：菱形结 + 长带尖角
    g += PG([(380, 172), (398, 186), (380, 206), (362, 186)], RED)
    g += PG([(368, 204), (392, 204), (400, 336), (380, 360), (360, 336)], RED)
    g += P("M 374 210 Q 371 228 377 244", stroke=RED_D, w=4)     # 领带酒窝
    g += shine(372, 226, 5, 26, RED_L, 0.7)
    g += C(380, 388, 7, BTN)                                     # 领带下两粒扣
    g += C(380, 416, 7, BTN)
    g += P("M 324 320 Q 344 328 360 322", stroke=WHITE_D, w=4)   # 褶皱
    g += P("M 400 320 Q 416 328 436 320", stroke=WHITE_D, w=4)
    return g


# ---------- 3 dress 红花裙挂木衣架，钩与架端外露 ----------
DRESS = ("M 322 126 Q 380 156 438 126 L 434 252 Q 492 348 486 430 "
         "Q 449 450 415 432 Q 380 452 345 432 Q 311 450 274 430 "
         "Q 268 348 326 252 Z")


def art_dress():
    g = ground()
    # 木衣架：弯钩 + 双臂 + 横杆
    g += P("M 380 112 L 380 86 Q 380 64 403 64 Q 421 64 421 82", stroke=WOOD_D, w=10)
    g += L(380, 112, 294, 164, WOOD, 12)
    g += L(380, 112, 466, 164, WOOD, 12)
    g += R(286, 156, 188, 14, 7, WOOD)
    # 裙身：吊带领口 → 收腰 → 大摆波浪
    g += f'<g transform="translate(7,9)">' + P(DRESS, RED_D) + "</g>"
    g += P(DRESS, RED)
    g += P("M 322 126 Q 380 158 438 126", stroke=RED_D, w=6)          # 领口滚边
    g += P("M 328 252 Q 380 262 434 252", stroke=RED_D, w=5)          # 腰缝
    g += shine(344, 176, 14, 34, RED_L, 0.7, -12)
    g += flower5(340, 318, 13, FLW, SUN)
    g += flower5(424, 306, 11, FLW, SUN)
    g += flower5(378, 392, 12, FLW, SUN)
    g += flower5(452, 370, 9, FLW, SUN)
    return g


# ---------- 4 skirt 黄百褶裙平铺：腰头 + 扇形褶线 + 锯齿摆 ----------
SKIRT = ("M 312 168 L 448 168 L 514 420 L 482 444 L 450 422 L 418 444 L 386 422 "
         "L 354 444 L 322 422 L 290 444 L 256 420 Z")


def art_skirt():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(SKIRT, YEL_D) + "</g>"
    g += P(SKIRT, YEL)
    g += R(306, 156, 148, 26, 10, YEL_D)                     # 腰头
    g += L(341, 184, 290, 442, YEL_D, 5)                     # 扇形褶线
    g += L(359, 184, 354, 442, YEL_D, 5)
    g += L(380, 184, 386, 420, YEL_D, 5)
    g += L(401, 184, 418, 442, YEL_D, 5)
    g += L(419, 184, 482, 442, YEL_D, 5)
    g += shine(316, 252, 13, 60, YEL_L2, 0.7, 14)
    g += shine(430, 260, 12, 56, YEL_L2, 0.55, -14)
    return g


# ---------- 5 shorts 青绿运动短裤：松紧腰抽绳 + 侧白条 ----------
SHORTS = ("M 296 174 L 464 174 L 484 268 L 512 414 L 412 428 L 380 300 "
          "L 348 428 L 248 414 L 276 268 Z")


def art_shorts():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(SHORTS, TEAL_D) + "</g>"
    g += P(SHORTS, TEAL)
    g += R(292, 164, 176, 26, 11, TEAL_D)                       # 松紧腰头
    g += L(372, 190, 368, 216, WHITE, 6)                        # 抽绳两根
    g += L(390, 190, 394, 216, WHITE, 6)
    g += P("M 458 272 Q 484 336 498 400", stroke=WHITE, w=9)    # 侧白条
    g += P("M 302 272 Q 276 336 262 400", stroke=WHITE, w=9)
    g += P("M 252 404 L 346 420", stroke=TEAL_D, w=8)           # 裤脚口
    g += P("M 414 420 L 508 404", stroke=TEAL_D, w=8)
    g += P("M 380 302 Q 358 320 342 342", stroke=TEAL_D, w=4)   # 裆部褶皱
    g += P("M 380 302 Q 402 320 418 342", stroke=TEAL_D, w=4)
    g += shine(320, 220, 15, 42, TEAL_L, 0.7, -10)
    return g


# ---------- 6 pants 深蓝长裤立起：腰头铜扣 + 前袋 + 烫线 ----------
PANTS = ("M 314 146 L 446 146 L 454 268 L 470 434 L 398 440 L 392 302 "
         "Q 380 282 368 302 L 362 440 L 290 434 L 306 268 Z")


def art_pants():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(PANTS, BLUE_DD) + "</g>"
    g += P(PANTS, BLUE_D)
    g += R(310, 136, 140, 26, 10, BLUE_DD)                      # 腰头
    g += C(380, 150, 8, SUN)                                    # 铜扣
    g += P("M 380 162 Q 382 220 368 252", stroke=BLUE_DD, w=5)  # 门襟缝线
    g += P("M 320 168 Q 346 192 322 218", stroke=BLUE_DD, w=4)  # 前袋弧线
    g += P("M 440 168 Q 414 192 438 218", stroke=BLUE_DD, w=4)
    g += P("M 344 300 L 336 424", stroke=BLUE, w=5)             # 烫线
    g += P("M 416 300 L 424 424", stroke=BLUE, w=5)
    g += P("M 292 424 L 360 430", stroke=BLUE_DD, w=8)          # 裤脚翻边
    g += P("M 400 430 L 468 424", stroke=BLUE_DD, w=8)
    g += shine(330, 192, 13, 34, BLUE_L, 0.6, 8)
    return g


# ---------- 7 coat 橙大衣：宽翻领 + 一排扣 + 袋盖 ----------
COAT = ("M 322 152 Q 380 168 438 152 L 476 170 L 514 368 L 484 388 L 452 286 "
        "L 466 440 L 294 440 L 308 286 L 276 388 L 246 368 L 284 170 Z")


def art_coat():
    g = ground()
    g += f'<g transform="translate(8,10)">' + P(COAT, ORANGE_D) + "</g>"
    g += P(COAT, ORANGE)
    g += PG([(380, 164), (322, 148), (346, 206)], ORANGE_D)       # 左翻领
    g += PG([(380, 164), (438, 148), (414, 206)], ORANGE_D)       # 右翻领
    g += PG([(512, 366), (486, 386), (476, 376), (502, 356)], ORANGE_D)  # 袖口
    g += PG([(248, 366), (274, 386), (284, 376), (258, 356)], ORANGE_D)
    g += R(318, 336, 46, 14, 6, ORANGE_D)                         # 袋盖
    g += R(396, 336, 46, 14, 6, ORANGE_D)
    g += C(380, 232, 11, BROWN_BT)                                # 一排扣
    g += C(380, 302, 11, BROWN_BT)
    g += C(380, 372, 11, BROWN_BT)
    g += shine(338, 228, 16, 46, ORANGE_L, 0.6, 8)
    g += P("M 486 300 Q 496 330 492 356", stroke=ORANGE_D, w=4)   # 袖褶
    g += P("M 274 300 Q 264 330 268 356", stroke=ORANGE_D, w=4)
    return g


# ---------- 8 jacket 棕黄夹克：罗纹领/下摆 + 拉链半开露内里 ----------
JACKET = ("M 308 168 Q 380 184 452 168 L 494 186 L 532 352 L 502 372 L 466 284 "
          "L 474 400 L 286 400 L 294 284 L 258 372 L 228 352 L 266 186 Z")


def art_jacket():
    g = ground()
    g += f'<g transform="translate(8,10)">' + P(JACKET, WOOD_D) + "</g>"
    g += P(JACKET, WOOD)
    g += P("M 308 168 Q 380 186 452 168 L 446 152 Q 380 170 314 152 Z", WOOD_D)  # 罗纹领
    g += R(284, 392, 192, 30, 12, WOOD_D)                         # 罗纹下摆
    for x in range(298, 464, 15):
        g += L(x, 398, x, 414, WOOD_L, 3.5)                       # 下摆罗纹齿
    g += PG([(530, 350), (504, 370), (494, 360), (520, 340)], WOOD_D)  # 袖口
    g += PG([(230, 350), (256, 370), (266, 360), (240, 340)], WOOD_D)
    g += L(318, 300, 348, 324, WOOD_D, 6)                         # 斜插袋
    g += L(412, 300, 442, 324, WOOD_D, 6)
    # 拉链半开：内里 → 两侧链齿 → 拉头 → 闭合段
    g += R(370, 184, 20, 110, 6, BROWN_BT)
    for y in (190, 204, 218, 232, 246, 260, 274):
        g += R(363, y, 6, 9, 2, SUN)
        g += R(391, y, 6, 9, 2, SUN)
    g += R(373, 286, 14, 16, 4, YEL_D)                            # 拉头
    g += L(380, 302, 380, 392, SUN, 5)                            # 闭合链
    g += shine(330, 230, 15, 44, WOOD_L, 0.7, 8)
    return g


# ---------- 9 sweater 粉圆领麻花纹毛衣，罗纹边 ----------
SWEATER = ("M 336 164 Q 380 188 424 164 L 472 182 L 588 330 L 544 360 L 448 268 "
           "L 454 432 Q 380 446 306 432 L 312 268 L 216 360 L 172 330 L 288 182 Z")


def art_sweater():
    g = ground()
    g += f'<g transform="translate(7,9)">' + P(SWEATER, PINK_D) + "</g>"
    g += P(SWEATER, PINK)
    g += E(380, 170, 48, 15, PINK_D)                              # 圆领罗纹
    g += E(380, 168, 37, 10, PINK)
    g += shine(338, 244, 17, 50, PINK_L, 0.6, 10)
    # 麻花：两条反向波浪绞在一起
    g += P("M 358 214 Q 382 244 358 274 Q 334 304 358 334 Q 382 364 358 394",
           stroke=PINK_D, w=8)
    g += P("M 402 214 Q 378 244 402 274 Q 426 304 402 334 Q 378 364 402 394",
           stroke=PINK_D, w=8)
    g += P("M 308 424 Q 380 438 452 424", stroke=PINK_D, w=7)     # 下摆罗纹
    for x in (322, 338, 354, 370, 386, 402, 418, 434):
        g += L(x, 428, x, 441, PINK_D, 3)
    g += PG([(584, 328), (546, 358), (536, 348), (574, 318)], PINK_D)  # 袖口罗纹
    g += PG([(176, 328), (214, 358), (224, 348), (186, 318)], PINK_D)
    return g


# ---------- 10 sock 白底彩条花袜一双并排（外八） ----------
SOCK = ("M 416 154 Q 458 146 500 154 L 504 330 Q 510 348 534 350 Q 576 354 578 388 "
        "Q 580 420 542 422 L 452 422 Q 414 420 413 372 Z")


def art_sock():
    g = ground()
    body = wrap(
        f'<g transform="translate(7,9)">' + P(SOCK, WHITE_D) + "</g>",
        P(SOCK, WHITE),
        P("M 416 186 L 501 186 L 502 212 L 416 212 Z", RED),      # 三道彩条
        P("M 416 228 L 502 228 L 502 254 L 416 254 Z", YEL),
        P("M 416 270 L 503 270 L 503 294 L 416 294 Z", TEAL),
        P("M 413 372 Q 414 420 452 422 L 452 404 Q 428 402 426 372 Z", TEAL),  # 袜跟
        P("M 534 350 Q 576 354 578 388 Q 580 420 542 422 L 522 422 L 522 352 Z", TEAL),  # 袜尖
        R(410, 146, 96, 30, 12, WHITE_D),                         # 袜口翻边
        E(560, 392, 8, 6, WHITE, 0.6),
        E(432, 394, 6, 5, WHITE, 0.5),
    )
    g += body                                                     # 右袜（尖朝右）
    g += f'<g transform="translate(760,0) scale(-1,1)">{body}</g>'  # 左袜镜像（尖朝左）
    return g


def arts():
    return {
        "T-shirt": art_tshirt(),
        "shirt": art_shirt(),
        "dress": art_dress(),
        "skirt": art_skirt(),
        "shorts": art_shorts(),
        "pants": art_pants(),
        "coat": art_coat(),
        "jacket": art_jacket(),
        "sweater": art_sweater(),
        "sock": art_sock(),
    }
