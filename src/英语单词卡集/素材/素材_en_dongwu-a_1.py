#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 动物·陆地（dongwu-a）第 1 段插画（10 卡：cat~elephant）。

每卡造型要点：cat 橘猫竖尾坐地长须 / dog 米黄棕斑吐舌摇尾红项圈 /
rabbit 白兔长耳直立抱胡萝卜 / mouse 浅灰鼠大圆耳长尾立起 /
bear 深棕壮熊直立圆耳 / panda 黑白熊猫抱竹 / tiger 橙黄黑纹虎张嘴露牙 /
lion 金黄大圆鬃张嘴吼 / monkey 棕猴卷尾挂枝手持香蕉 / elephant 灰象长鼻上卷大扇耳。
全部侧面全身像，主体高约 280~360px，脚底落在地面 y≈430~440。
与 1000 字动物卡错造型错构图，主色按分配且相邻卡错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "cat", "cn": "猫"},
    {"w": "dog", "cn": "狗"},
    {"w": "rabbit", "cn": "兔子"},
    {"w": "mouse", "cn": "老鼠"},
    {"w": "bear", "cn": "熊"},
    {"w": "panda", "cn": "熊猫"},
    {"w": "tiger", "cn": "老虎"},
    {"w": "lion", "cn": "狮子"},
    {"w": "monkey", "cn": "猴子"},
    {"w": "elephant", "cn": "大象"},
]


# ---------- 本组同族补充色 ----------
CAT, CAT_D, CAT_L = "#f0913c", "#d97926", "#f8b26a"       # 橘黄（YEL/SUN 族）
DOG, DOG_D = "#f2e0bd", "#dcc094"                          # 米黄
PATCH = "#b57b44"                                          # 棕斑（WOOD 族）
RAB_D = "#ded7c6"                                          # 白兔暗衬
MOUSE, MOUSE_D, MOUSE_L = "#b9c2cc", "#9fabb6", "#dde3e9"  # 浅灰
BEAR, BEAR_D, BEAR_L = "#8a5a33", "#6e4426", "#a5764a"     # 深棕
MUZZ = "#e9c9a2"                                           # 吻部浅米
PBLK, PBLK_L = "#47423c", "#5f584f"                        # 熊猫黑
TIGER, TIGER_D, TIGER_L = "#e8862c", "#cf7018", "#f8e3bb"  # 橙黄
LION, LION_D, LION_L = "#f2c14e", "#d99a2b", "#f6d488"     # 金黄
LFACE = "#f8e2ac"                                          # 狮脸
MONK, MONK_D, MFACE = "#b5824a", "#9a6b38", "#eec396"      # 猴棕
ELE, ELE_D, ELE_L = "#9aa6b2", "#82909c", "#c6d0d8"        # 象灰
MOUTH = "#8f4030"                                          # 口腔暗红


def eye(cx, cy, rx=10, ry=12):
    """单只眼睛：INK 圆点 + 白高光。"""
    return E(cx, cy, rx, ry, INK) + C(cx - 3, cy - 4, 3.0, WHITE)


def eye2(cx, cy, dx, rx=10, ry=12):
    """双眼。"""
    return eye(cx - dx, cy, rx, ry) + eye(cx + dx, cy, rx, ry)


def nose_mouth(cx, ty, by, w=5):
    """小兽鼻嘴：鼻下人中 + 左右弧线（cx 居中，ty 鼻底，by 嘴角分叉点）。"""
    return wrap(
        L(cx, ty, cx, by, INK, 4),
        P(f"M {cx} {by} Q {cx - 12} {by + 9} {cx - 23} {by + 2}", stroke=INK, w=w),
        P(f"M {cx} {by} Q {cx + 12} {by + 9} {cx + 23} {by + 2}", stroke=INK, w=w))


def blush2(cx, cy, dx, r=11):
    return C(cx - dx, cy, r, PINK, 0.65) + C(cx + dx, cy, r, PINK, 0.65)


def ebody(cx, cy, rx, ry, main, dark):
    """椭圆身体：深一号偏移衬体积。"""
    return E(cx + rx * 0.06, cy + ry * 0.08, rx, ry, dark) + E(cx, cy, rx, ry, main)


def chead(cx, cy, r, main, dark):
    return C(cx + r * 0.08, cy + r * 0.09, r, dark) + C(cx, cy, r, main)


# ---------- 1 cat 橘猫坐地，竖尾，长胡须 ----------
def art_cat():
    g = ground()
    # 竖尾（先画，在身后）
    g += P("M 450 404 Q 534 390 544 310 Q 548 262 514 248", stroke=CAT_D, w=24)
    g += P("M 450 404 Q 530 390 539 312 Q 543 266 512 250", stroke=CAT, w=15)
    g += C(512, 250, 10, CAT_D)
    # 身体（坐姿）
    g += ebody(385, 362, 90, 76, CAT, CAT_D)
    g += E(378, 384, 46, 42, CAT_L, 0.8)
    g += P("M 330 310 Q 342 328 334 348", stroke=CAT_D, w=7)
    g += P("M 440 312 Q 452 330 444 350", stroke=CAT_D, w=7)
    # 前腿与爪
    g += R(348, 326, 26, 104, 13, CAT) + E(361, 430, 21, 10, CAT_L)
    g += R(406, 326, 26, 104, 13, CAT) + E(419, 430, 21, 10, CAT_L)
    # 耳（先画，头盖住基部）
    g += PG([(334, 152), (354, 90), (386, 140)], CAT) + PG([(342, 144), (355, 104), (374, 136)], PINK)
    g += PG([(446, 152), (426, 90), (394, 140)], CAT) + PG([(438, 144), (425, 104), (406, 136)], PINK)
    # 头 + 额纹
    g += chead(390, 205, 72, CAT, CAT_D)
    g += L(372, 130, 372, 148, CAT_D, 6) + L(390, 126, 390, 146, CAT_D, 6) + L(408, 130, 408, 148, CAT_D, 6)
    # 脸
    g += eye2(390, 192, 30, 11, 13)
    g += PG([(381, 218), (399, 218), (390, 229)], PINK)
    g += nose_mouth(390, 229, 237)
    # 长胡须（本卡主角）
    g += L(326, 198, 254, 190, INK, 4) + L(326, 212, 252, 212, INK, 4) + L(326, 226, 256, 232, INK, 4)
    g += L(454, 198, 526, 190, INK, 4) + L(454, 212, 528, 212, INK, 4) + L(454, 226, 524, 232, INK, 4)
    g += blush2(390, 240, 60, 11)
    return g


# ---------- 2 dog 米黄+棕斑，吐舌摇尾，红项圈 ----------
def art_dog():
    g = ground()
    # 摇起的尾 + 动感弧线
    g += P("M 545 320 Q 585 300 588 258", stroke=DOG_D, w=18)
    g += P("M 545 320 Q 583 300 585 260", stroke=DOG, w=11) + C(587, 254, 10, DOG_D)
    g += P("M 606 262 Q 614 254 612 242", stroke=DOG_D, w=5)
    g += P("M 618 278 Q 628 268 626 254", stroke=DOG_D, w=4)
    # 远侧腿
    g += R(352, 360, 26, 74, 12, DOG_D) + E(365, 431, 19, 8, DOG_D)
    g += R(508, 360, 26, 74, 12, DOG_D) + E(521, 431, 19, 8, DOG_D)
    # 身体 + 背部棕斑 + 颈部（补齐头身连接）
    g += ebody(430, 318, 140, 74, DOG, DOG_D)
    g += f'<g transform="rotate(-8 490 292)">{E(490, 292, 54, 32, PATCH)}</g>'
    g += R(294, 238, 54, 74, 25, DOG)
    # 红项圈 + 铃牌（头盖上一半）
    g += f'<g transform="rotate(8 322 278)">{R(292, 268, 60, 20, 10, RED)}</g>'
    g += C(320, 298, 9, SUN)
    # 近侧腿
    g += R(316, 356, 27, 78, 12, DOG) + E(329, 433, 21, 9, DOG)
    g += R(470, 356, 27, 78, 12, DOG) + E(483, 433, 21, 9, DOG)
    # 头 + 垂耳（棕斑）
    g += chead(266, 220, 62, DOG, DOG_D)
    g += f'<g transform="rotate(-18 222 172)">{E(222, 172, 18, 38, PATCH)}</g>'
    g += f'<g transform="rotate(28 312 180)">{E(312, 180, 25, 52, PATCH)}</g>'
    # 吻部 + 鼻 + 吐舌
    g += E(220, 250, 44, 33, "#f7ecd4")
    g += C(192, 240, 13, INK)
    g += P("M 214 268 Q 232 282 252 272", stroke=INK, w=5)
    g += P("M 228 274 Q 224 300 238 304 Q 252 302 248 276 Z", PINK)
    # 眼（右眼带棕斑）
    g += C(302, 206, 24, PATCH)
    g += eye(240, 202, 10, 12) + eye(302, 202, 10, 12)
    g += C(236, 246, 11, PINK, 0.65)
    return g


# ---------- 3 rabbit 白兔长耳站立，抱胡萝卜 ----------
def art_rabbit():
    g = ground()
    # 长耳（先画）
    g += f'<g transform="rotate(-10 348 130)">{E(348, 130, 20, 44, RAB_D) + E(348, 130, 15, 38, WHITE) + E(348, 134, 7, 28, PINK)}</g>'
    g += f'<g transform="rotate(10 424 130)">{E(424, 130, 20, 44, RAB_D) + E(424, 130, 15, 38, WHITE) + E(424, 134, 7, 28, PINK)}</g>'
    # 立起的身体
    g += ebody(391, 345, 82, 88, WHITE, RAB_D)
    g += E(391, 374, 46, 48, "#faf6ea")
    # 头
    g += chead(385, 208, 66, WHITE, RAB_D)
    # 脸
    g += eye2(385, 196, 26, 10, 12)
    g += PG([(377, 216), (393, 216), (385, 226)], PINK)
    g += nose_mouth(385, 226, 232, 4.5)
    g += L(334, 212, 276, 204, INK, 3.5) + L(334, 224, 278, 230, INK, 3.5)
    g += L(436, 212, 494, 204, INK, 3.5) + L(436, 224, 492, 230, INK, 3.5)
    g += blush2(385, 234, 47, 10)
    # 胡萝卜（斜抱）
    g += P("M 358 294 Q 380 288 396 306 L 434 350 Q 442 362 428 370 Q 416 376 406 364 L 366 318 Q 352 302 358 294 Z", "#f0913c")
    g += L(378, 318, 392, 326, "#d97926", 4) + L(392, 332, 406, 340, "#d97926", 4)
    g += f'<g transform="rotate(-24 346 272)">{E(346, 272, 10, 26, GREEN)}</g>'
    g += f'<g transform="rotate(6 366 268)">{E(366, 268, 10, 28, GREEN)}</g>'
    g += f'<g transform="rotate(30 384 278)">{E(384, 278, 9, 22, GREEN_L)}</g>'
    # 抱着的小爪
    g += E(372, 314, 20, 14, RAB_D) + E(370, 312, 18, 12, WHITE)
    g += E(406, 346, 20, 14, RAB_D) + E(404, 344, 18, 12, WHITE)
    # 后脚
    g += E(346, 428, 34, 14, RAB_D) + E(346, 424, 30, 12, WHITE)
    g += E(436, 428, 34, 14, RAB_D) + E(436, 424, 30, 12, WHITE)
    return g


# ---------- 4 mouse 浅灰鼠大圆耳，长尾立起 ----------
def art_mouse():
    g = ground()
    # 长尾立起（本卡主角）
    g += P("M 452 402 Q 540 396 556 318 Q 566 258 528 236", stroke=MOUSE_D, w=9)
    g += C(528, 236, 5.5, MOUSE_D)
    # 大圆耳（先画）
    g += C(266, 220, 48, MOUSE_D) + C(262, 216, 44, MOUSE) + C(262, 218, 27, PINK)
    g += C(378, 216, 48, MOUSE_D) + C(374, 212, 44, MOUSE) + C(374, 214, 27, PINK)
    # 头 + 身体
    g += C(326, 300, 56, MOUSE_D) + C(322, 294, 54, MOUSE)
    g += ebody(390, 366, 86, 62, MOUSE, MOUSE_D)
    g += E(382, 388, 46, 34, MOUSE_L)
    # 脸
    g += eye2(322, 284, 26, 9, 11)
    g += E(322, 316, 9, 7, PINK)
    g += P("M 322 324 Q 316 330 308 326", stroke=INK, w=4)
    g += P("M 322 324 Q 328 330 336 326", stroke=INK, w=4)
    g += blush2(322, 314, 36, 9)
    # 前爪小圆
    g += E(356, 420, 16, 9, MOUSE_L) + E(356, 418, 13, 7, MOUSE)
    # 后脚
    g += E(348, 430, 30, 12, MOUSE_D) + E(346, 426, 26, 10, MOUSE)
    g += E(430, 430, 30, 12, MOUSE_D) + E(428, 426, 26, 10, MOUSE)
    # 胡须（最后画，压在身上也清晰）
    g += L(274, 308, 222, 300, INK, 3.5) + L(274, 320, 224, 326, INK, 3.5)
    g += L(370, 308, 422, 300, INK, 3.5) + L(370, 320, 420, 326, INK, 3.5)
    return g


# ---------- 5 bear 深棕壮硕圆耳直立 ----------
def art_bear():
    g = ground()
    # 圆耳（先画）
    g += C(330, 122, 32, BEAR_D) + C(326, 118, 28, BEAR) + C(326, 120, 14, MUZZ)
    g += C(456, 122, 32, BEAR_D) + C(452, 118, 28, BEAR) + C(452, 120, 14, MUZZ)
    # 壮硕身体
    g += ebody(392, 346, 112, 92, BEAR, BEAR_D)
    g += E(392, 378, 60, 54, BEAR_L)
    # 后脚
    g += E(344, 428, 38, 15, BEAR_D) + E(340, 424, 34, 13, BEAR)
    g += E(452, 428, 38, 15, BEAR_D) + E(448, 424, 34, 13, BEAR)
    # 垂在体侧的粗臂
    g += P("M 306 298 Q 276 328 280 374", stroke=BEAR_D, w=48)
    g += P("M 303 296 Q 274 326 278 372", stroke=BEAR, w=36) + C(280, 380, 21, BEAR)
    g += P("M 478 298 Q 508 328 504 374", stroke=BEAR_D, w=48)
    g += P("M 481 296 Q 510 326 506 372", stroke=BEAR, w=36) + C(504, 380, 21, BEAR)
    # 头
    g += chead(390, 190, 80, BEAR, BEAR_D)
    # 吻部 + 鼻嘴
    g += E(390, 222, 40, 30, MUZZ)
    g += E(390, 208, 15, 11, INK)
    g += nose_mouth(390, 218, 228)
    g += eye2(390, 172, 38, 11, 13)
    g += blush2(390, 210, 60, 12)
    return g


# ---------- 6 panda 黑白坐地，抱竹子 ----------
def art_panda():
    g = ground()
    # 圆耳（先画）
    g += C(320, 138, 32, PBLK) + C(318, 134, 28, PBLK_L)
    g += C(456, 138, 32, PBLK) + C(454, 134, 28, PBLK_L)
    # 白身体 + 黑腿脚
    g += ebody(386, 346, 104, 88, WHITE, RAB_D)
    g += E(322, 396, 44, 38, PBLK) + E(452, 396, 44, 38, PBLK)
    g += E(318, 428, 34, 15, PBLK_L) + E(452, 428, 34, 15, PBLK_L)
    # 头
    g += C(392, 208, 84, RAB_D) + C(388, 202, 82, WHITE)
    # 黑眼斑 + 眼
    g += f'<g transform="rotate(-18 352 192)">{E(352, 192, 19, 26, PBLK)}</g>'
    g += f'<g transform="rotate(18 424 192)">{E(424, 192, 19, 26, PBLK)}</g>'
    g += C(352, 190, 8, WHITE) + C(352, 190, 4.5, INK) + C(350, 188, 1.8, WHITE)
    g += C(424, 190, 8, WHITE) + C(424, 190, 4.5, INK) + C(422, 188, 1.8, WHITE)
    g += E(388, 226, 13, 9, INK)
    g += nose_mouth(388, 234, 240, 4.5)
    g += blush2(388, 238, 56, 10)
    # 竹子（抱在右侧）
    g += f'<g transform="rotate(-3 494 285)">{R(484, 132, 20, 306, 10, GREEN)}</g>'
    g += L(485, 230, 504, 226, "#5d8a52", 5) + L(486, 330, 505, 327, "#5d8a52", 5)
    g += f'<g transform="rotate(-30 466 124)">{E(466, 124, 12, 34, GREEN)}</g>'
    g += f'<g transform="rotate(25 522 120)">{E(522, 120, 12, 36, GREEN)}</g>'
    g += f'<g transform="rotate(-4 494 110)">{E(494, 110, 11, 30, GREEN_L)}</g>'
    # 黑手臂环抱
    g += P("M 452 296 Q 476 316 486 342", stroke=PBLK, w=42) + C(488, 346, 19, PBLK)
    g += P("M 322 322 Q 366 380 462 386", stroke=PBLK, w=40) + C(474, 388, 18, PBLK)
    return g


# ---------- 7 tiger 橙黄黑纹虎，张嘴露牙 ----------
def art_tiger():
    g = ground()
    # 上翘长尾 + 环纹
    g += P("M 556 300 Q 620 288 636 232 Q 644 198 620 182", stroke=TIGER_D, w=22)
    g += P("M 556 300 Q 616 288 631 234 Q 638 202 617 186", stroke=TIGER, w=13)
    g += C(618, 184, 10, TIGER_D)
    g += L(626, 234, 642, 242, INK, 5.5) + L(614, 202, 630, 210, INK, 5.5)
    # 远侧腿
    g += R(366, 352, 26, 76, 12, TIGER_D) + E(379, 431, 19, 8, TIGER_D)
    g += R(512, 352, 26, 76, 12, TIGER_D) + E(525, 431, 19, 8, TIGER_D)
    # 身体 + 白腹
    g += ebody(430, 310, 136, 72, TIGER, TIGER_D)
    g += E(430, 342, 96, 34, TIGER_L, 0.85)
    # 黑纹（纹路线）
    g += P("M 380 244 Q 392 268 384 292", stroke=INK, w=8)
    g += P("M 430 240 Q 442 266 434 292", stroke=INK, w=8)
    g += P("M 480 246 Q 492 270 484 294", stroke=INK, w=8)
    g += P("M 526 258 Q 538 278 532 300", stroke=INK, w=7)
    g += P("M 356 268 Q 370 282 364 304", stroke=INK, w=7)
    # 近侧腿
    g += R(330, 356, 27, 78, 12, TIGER) + E(343, 433, 21, 9, TIGER)
    g += R(474, 356, 27, 78, 12, TIGER) + E(487, 433, 21, 9, TIGER)
    # 耳（先画）
    g += C(238, 162, 26, TIGER_D) + C(234, 158, 22, TIGER) + C(234, 160, 11, TIGER_L)
    g += C(330, 158, 26, TIGER_D) + C(326, 154, 22, TIGER) + C(326, 156, 11, TIGER_L)
    # 头 + 额纹
    g += chead(282, 220, 68, TIGER, TIGER_D)
    g += L(268, 162, 268, 178, INK, 4.5) + L(282, 158, 282, 178, INK, 5) + L(296, 162, 296, 178, INK, 4.5)
    g += L(330, 236, 344, 248, INK, 5)
    # 张嘴露牙（本卡主角）
    g += E(254, 244, 44, 30, TIGER_L)
    g += PG([(216, 232), (244, 232), (230, 248)], INK)
    g += E(256, 270, 32, 17, MOUTH)
    g += PG([(238, 262), (250, 262), (244, 276)], WHITE)
    g += PG([(258, 262), (270, 262), (264, 276)], WHITE)
    g += PG([(246, 284), (258, 284), (252, 272)], WHITE)
    g += eye2(282, 196, 30, 10, 12)
    g += C(322, 240, 10, PINK, 0.65)
    return g


# ---------- 8 lion 金色大鬃毛狮子，张嘴吼 ----------
def art_lion():
    g = ground()
    # 尾 + 绒球
    g += P("M 470 400 Q 520 396 528 352", stroke=LION_D, w=12)
    g += C(530, 342, 15, LION_D) + C(530, 342, 9, LION_L)
    # 坐姿身体 + 前爪
    g += E(386, 400, 106, 52, LION_D) + E(380, 394, 106, 52, LION_L)
    g += E(332, 438, 34, 13, "#f8e2ac") + E(328, 434, 30, 11, LION_L)
    g += E(436, 438, 34, 13, "#f8e2ac") + E(440, 434, 30, 11, LION_L)
    # 大圆鬃毛（本卡主角）
    g += C(386, 240, 132, LION_D) + C(380, 234, 126, LION)
    # 耳
    g += C(316, 126, 26, LION_D) + C(314, 124, 21, LFACE)
    g += C(446, 126, 26, LION_D) + C(448, 124, 21, LFACE)
    # 脸
    g += C(384, 244, 82, LFACE)
    g += eye2(384, 224, 34, 11, 13)
    # 吻部 + 鼻
    g += E(384, 272, 44, 30, "#fbf0d6")
    g += PG([(370, 256), (398, 256), (384, 270)], "#8a5a33")
    # 张嘴吼
    g += P("M 348 280 Q 384 270 420 280 Q 424 314 384 322 Q 344 314 348 280 Z", MOUTH)
    g += E(384, 312, 22, 10, "#f0876f")
    g += PG([(356, 280), (368, 280), (362, 294)], WHITE)
    g += PG([(400, 280), (412, 280), (406, 294)], WHITE)
    g += PG([(344, 284), (352, 284), (348, 292)], WHITE)
    g += PG([(416, 284), (424, 284), (420, 292)], WHITE)
    g += C(356, 276, 3, INK) + C(350, 286, 3, INK) + C(412, 276, 3, INK) + C(418, 286, 3, INK)
    g += blush2(384, 252, 62, 12)
    return g


# ---------- 9 monkey 棕猴卷尾挂枝，手持香蕉 ----------
def art_monkey():
    g = ground()
    # 横枝 + 叶
    g += R(150, 100, 470, 24, 12, WOOD_D) + R(150, 100, 470, 9, 4, WOOD)
    g += f'<g transform="rotate(30 604 108)">{E(604, 108, 13, 30, GREEN)}</g>'
    g += f'<g transform="rotate(55 626 122)">{E(626, 122, 12, 26, GREEN_L)}</g>'
    g += f'<g transform="rotate(-24 200 104)">{E(200, 104, 12, 26, GREEN_L)}</g>'
    # 卷尾挂枝（本卡主角：尾巴绕过树枝）
    g += P("M 438 232 Q 444 160 424 122 Q 410 100 390 106 Q 376 112 380 128", stroke=MONK_D, w=15)
    g += C(381, 129, 8, MONK_D)
    # 身体 + 浅肚
    g += ebody(406, 294, 62, 78, MONK, MONK_D)
    g += E(402, 314, 38, 48, MFACE)
    # 垂下的腿
    g += R(380, 358, 25, 68, 12, MONK) + E(392, 428, 21, 10, MFACE)
    g += R(422, 362, 25, 64, 12, MONK_D) + E(434, 428, 21, 10, "#e0b183")
    # 头 + 侧耳
    g += chead(402, 190, 56, MONK, MONK_D)
    g += C(346, 192, 16, MONK_D) + C(344, 190, 10, MFACE)
    g += C(460, 192, 16, MONK_D) + C(462, 190, 10, MFACE)
    # 脸盘
    g += C(376, 184, 30, MFACE) + C(424, 184, 30, MFACE) + E(400, 216, 40, 28, MFACE)
    g += eye2(400, 178, 20, 8, 10)
    g += E(392, 212, 4, 5, "#c99a63") + E(410, 212, 4, 5, "#c99a63")
    g += P("M 386 226 Q 402 236 418 226", stroke=INK, w=5)
    g += blush2(400, 214, 42, 9)
    # 手持香蕉（本卡主角）
    g += P("M 268 234 Q 284 196 320 202 Q 298 212 290 240 Q 278 246 268 234 Z", YEL)
    g += C(269, 233, 4, "#8a5a33") + C(318, 203, 4, "#8a5a33")
    # 两臂：左举蕉、右垂
    g += P("M 358 270 Q 324 272 310 244", stroke=MONK, w=30) + C(306, 240, 14, MONK)
    g += P("M 452 268 Q 478 296 480 330", stroke=MONK_D, w=30) + C(481, 336, 14, MONK_D)
    return g


# ---------- 10 elephant 灰象长鼻上卷，大扇耳 ----------
def art_elephant():
    g = ground()
    # 尾
    g += P("M 580 330 Q 606 350 600 386", stroke=ELE_D, w=10) + C(600, 392, 8, ELE_D)
    # 远侧腿
    g += R(452, 366, 34, 72, 15, ELE_D) + E(469, 434, 10, 6, "#aeb9c4")
    g += R(540, 366, 34, 72, 15, ELE_D) + E(557, 434, 10, 6, "#aeb9c4")
    # 身体
    g += ebody(470, 312, 142, 82, ELE, ELE_D)
    # 近侧腿 + 趾甲
    g += R(408, 362, 36, 76, 16, ELE) + E(426, 436, 12, 7, ELE_L)
    g += R(498, 362, 36, 76, 16, ELE) + E(516, 436, 12, 7, ELE_L)
    # 头 + 大扇耳（本卡主角）
    g += chead(290, 240, 76, ELE, ELE_D)
    g += E(334, 248, 56, 74, ELE_D) + E(330, 244, 47, 64, ELE_L)
    # 小象牙
    g += f'<g transform="rotate(18 272 302)">{E(272, 302, 10, 17, "#fbfaf4")}</g>'
    # 眼
    g += eye(252, 226, 9, 11)
    g += C(238, 254, 10, PINK, 0.5)
    # 长鼻上卷（本卡主角：粗段下行 + 末端上卷）
    g += P("M 262 284 Q 214 312 206 360 Q 200 402 234 416", stroke=ELE_D, w=42)
    g += P("M 262 284 Q 218 310 210 358 Q 204 396 232 410", stroke=ELE, w=32)
    g += P("M 232 412 Q 270 426 288 396 Q 300 366 286 340", stroke=ELE_D, w=30)
    g += P("M 232 410 Q 262 420 278 396 Q 288 378 280 360", stroke=ELE, w=21)
    g += C(283, 352, 10, ELE_D) + C(283, 352, 6, ELE)
    return g


def arts():
    return {
        "cat": art_cat(),
        "dog": art_dog(),
        "rabbit": art_rabbit(),
        "mouse": art_mouse(),
        "bear": art_bear(),
        "panda": art_panda(),
        "tiger": art_tiger(),
        "lion": art_lion(),
        "monkey": art_monkey(),
        "elephant": art_elephant(),
    }
