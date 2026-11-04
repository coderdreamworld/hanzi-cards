#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 颜色·形状（yanse）第 1 段插画（12 卡：red~silver）。

颜色系列：12 张同一只大蝴蝶——butterfly() 造型参数全组固定，只换 main/dark/light 三色；
右下角配词库指定同色小物：红苹果 / 黄香蕉 / 绿叶 / 蓝水杯 / 黑猫剪影 / 白牛奶杯 /
桃花 / 紫葡萄 / 木凳 / 灰石头 / 金奖牌 / 银钥匙。
每卡第一笔 ground()；无描边无渐变；图上无文字数字。
white 卡在上翅底下垫浅灰托底（不改动蝴蝶造型）保证白翅可读；black 卡靠深浅翅色自明。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "red", "cn": "红色"},
    {"w": "yellow", "cn": "黄色"},
    {"w": "green", "cn": "绿色"},
    {"w": "blue", "cn": "蓝色"},
    {"w": "black", "cn": "黑色"},
    {"w": "white", "cn": "白色"},
    {"w": "pink", "cn": "粉色"},
    {"w": "purple", "cn": "紫色"},
    {"w": "brown", "cn": "棕色"},
    {"w": "grey", "cn": "灰色"},
    {"w": "gold", "cn": "金色"},
    {"w": "silver", "cn": "银色"},
]


# ---------- 本组同族补充色 ----------
INK_D = "#33241a"                        # 黑族深（黑蝴蝶下翅）
INK_L = "#6b5443"                        # 黑族浅（黑蝴蝶翅斑）
WHITE_DK = "#e3ded2"                     # 白族深（白蝴蝶下翅 / 牛奶杯暗面）
WHITE_L = "#fffef9"                      # 白族浅（白蝴蝶翅斑）
WHITE_SD = "#d9d1bf"                     # 白族更深暖灰（白卡翅底托底）
MILK = "#fdf3d6"                         # 奶白（牛奶杯奶面）
BLUE_L = "#a5d3ee"                       # 蓝族浅（蓝蝴蝶翅斑）
GREEN_D = "#5e8f52"                      # 绿族深（绿叶叶脉 / 果柄叶）
PINK_D, PINK_L = "#e8876f", "#f9c3b0"    # 粉族深 / 浅
PURP, PURP_D, PURP_L = "#9b7fc4", "#7d63a6", "#c0aae0"   # 紫族
BROWN_M, BROWN_L = "#a5744a", "#c49670"  # 棕族主 / 浅（凳面 / 凳面高光）
STEM = "#8a5c38"                         # 果柄 / 凳腿深棕（WOOD 族深）
GREY, GREY_D, GREY_L = "#b7bcc2", "#9aa0a7", "#d4d8dc"   # 灰族
GOLD, GOLD_D, GOLD_L = "#e8b83c", "#c9992b", "#f5d878"   # 金族
SILV, SILV_D, SILV_L = "#c9ced4", "#a8afb8", "#e8ebee"   # 银族

SET_RED = (RED, RED_D, PINK)
SET_YELLOW = (YEL, YEL_D, SUN_L)
SET_GREEN = (GREEN, GREEN_D, GREEN_L)
SET_BLUE = (BLUE, BLUE_D, BLUE_L)
SET_BLACK = (INK, INK_D, INK_L)
SET_WHITE = (WHITE, WHITE_DK, WHITE_L)
SET_PINK = (PINK, PINK_D, PINK_L)
SET_PURPLE = (PURP, PURP_D, PURP_L)
SET_BROWN = (BROWN_M, STEM, BROWN_L)
SET_GREY = (GREY, GREY_D, GREY_L)
SET_GOLD = (GOLD, GOLD_D, GOLD_L)
SET_SILVER = (SILV, SILV_D, SILV_L)


# ---------- 系列统一蝴蝶（造型参数全组共用，一个字都不能改） ----------
def butterfly(cx, cy, main, dark, light):
    """同一只蝴蝶：下翅两片 rx60 ry45 @(±76,+46) rotate∓12 → 上翅两片 rx88 ry62
    @(±105,-55) rotate∓25 → 上翅浅斑 r20 → 身体竖椭圆 rx15 ry50 → 头 r19 +
    头侧白高光点 → 两根触角线段端头小球。"""
    g = ""
    for sx, rot in ((-1, -12), (1, 12)):    # 下翅左右两片
        x, y = cx + 76 * sx, cy + 46
        g += f'<g transform="rotate({rot} {x} {y})">' + E(x, y, 60, 45, dark) + "</g>"
    for sx, rot in ((-1, -25), (1, 25)):    # 上翅左右两片
        x, y = cx + 105 * sx, cy - 55
        g += f'<g transform="rotate({rot} {x} {y})">' + E(x, y, 88, 62, main) + "</g>"
    for sx in (-1, 1):                      # 上翅中央浅色圆斑
        g += C(cx + 105 * sx, cy - 55, 20, light)
    g += E(cx, cy, 15, 50, INK)             # 身体
    g += C(cx, cy - 62, 19, INK)            # 头
    g += C(cx - 8, cy - 67, 4.5, WHITE)     # 头两侧白高光点
    g += C(cx + 8, cy - 67, 4.5, WHITE)
    g += L(cx - 6, cy - 76, cx - 32, cy - 106, INK, 4)   # 触角 ×2，端头小球
    g += L(cx + 6, cy - 76, cx + 32, cy - 106, INK, 4)
    g += C(cx - 32, cy - 106, 5.5, INK)
    g += C(cx + 32, cy - 106, 5.5, INK)
    return g


def _wing_backing():
    """仅 white 卡用：上翅底下浅灰托底（位置在蝴蝶之外，不改动蝴蝶造型）。"""
    g = ""
    for sx, rot in ((-1, -25), (1, 25)):
        x, y = 380 + 105 * sx + 4, 205 - 55 + 6
        g += f'<g transform="rotate({rot} {x} {y})">' + E(x, y, 96, 70, WHITE_SD) + "</g>"
    return g


# ---------- 右下角伴物（各卡同色小物，约 20% 画布） ----------
def apple():
    """红苹果：深底红果 + 高光 + 果柄绿叶。"""
    return wrap(
        C(570, 402, 45, RED_D),
        C(565, 397, 43, RED),
        E(546, 378, 11, 8, PINK, 0.85),
        L(565, 356, 571, 338, STEM, 7),
        f'<g transform="rotate(28 588 344)">' + E(588, 344, 17, 9, GREEN) + "</g>",
    )


def banana():
    """黄香蕉：卧放弯月身 + 深色脊线 + 蒂头。"""
    return wrap(
        P("M 486 378 Q 486 436 548 448 Q 610 458 644 404 Q 648 396 638 396 "
          "Q 616 434 566 428 Q 516 422 500 376 Q 496 366 486 378 Z", YEL),
        P("M 496 384 Q 520 428 566 434 Q 614 438 640 400", stroke=YEL_D, w=5),
        C(487, 377, 7, STEM),
        E(536, 434, 15, 6, SUN_L, 0.8),
    )


def leaf():
    """绿叶：尖头叶身 + 主脉三侧脉 + 短柄。"""
    return wrap(
        P("M 506 436 Q 536 348 646 362 Q 630 452 506 436 Z", GREEN),
        P("M 514 430 Q 580 402 638 366", stroke=GREEN_D, w=5),
        L(556, 414, 548, 394, GREEN_D, 4),
        L(590, 400, 590, 380, GREEN_D, 4),
        L(618, 384, 620, 370, GREEN_D, 4),
        L(506, 436, 490, 448, GREEN_D, 6),
    )


def cat():
    """黑猫剪影（坐姿侧影朝左）：后臀 + 前胸 + 头 + 双耳 + 卷尾，全 INK。"""
    return wrap(
        P("M 606 436 Q 638 446 644 416 Q 648 398 634 392", stroke=INK, w=9),
        C(580, 412, 33, INK),
        f'<g transform="rotate(12 548 404)">' + E(548, 404, 26, 40, INK) + "</g>",
        C(536, 354, 23, INK),
        PG([(518, 344), (512, 322), (532, 334)], INK),
        PG([(544, 334), (552, 316), (562, 336)], INK),
    )


def milk_cup():
    """白牛奶杯：浅灰阴影托底 + 白杯身 + 右侧暗面 + 奶白杯口奶面。"""
    return wrap(
        E(566, 442, 58, 12, WHITE_SD),
        P("M 534 336 L 598 336 L 590 436 Q 578 446 566 446 Q 554 446 542 436 Z", WHITE),
        P("M 566 336 L 598 336 L 590 436 Q 578 445 566 446 Z", WHITE_DK, 0.75),
        E(566, 336, 32, 10, WHITE_DK),
        E(566, 336, 26, 8, MILK),
    )


def blossom():
    """桃花：大五瓣花（粉瓣黄芯）+ 小花苞 + 小叶。"""
    return wrap(
        L(614, 434, 606, 450, GREEN_D, 5),
        flower5(560, 392, 30, PINK, SUN),
        flower5(614, 424, 16, PINK_L, SUN),
        f'<g transform="rotate(-24 524 424)">' + E(524, 424, 14, 7, GREEN) + "</g>",
    )


def grapes():
    """紫葡萄小串：6 粒紫果（深底 + 高光）+ 果柄小叶。"""
    g = L(566, 372, 558, 350, STEM, 6)
    g += f'<g transform="rotate(24 580 352)">' + E(580, 352, 15, 8, GREEN) + "</g>"
    for x, y, r in ((540, 386, 16), (592, 386, 16), (566, 380, 16),
                    (552, 412, 16), (578, 412, 16), (565, 436, 15)):
        g += C(x + 3, y + 3, r, PURP_D)
        g += C(x, y, r, PURP)
    for x, y in ((540, 386), (566, 380), (592, 386), (552, 412), (578, 412)):
        g += C(x - 5, y - 6, 4, PURP_L, 0.9)
    return g


def stool():
    """小木方凳：两条前腿 + 横撑 + 棕凳面 + 浅色面沿。"""
    return wrap(
        R(518, 386, 18, 60, 6, STEM),
        R(596, 386, 18, 60, 6, STEM),
        R(522, 416, 88, 8, 4, STEM),
        R(508, 368, 116, 24, 9, BROWN_M),
        R(508, 368, 116, 9, 4, BROWN_L),
    )


def stone():
    """灰石头：大小两块（深底 + 灰面 + 浅色高光）。"""
    return wrap(
        C(608, 426, 20, GREY_D),
        C(604, 423, 18, GREY),
        C(566, 412, 34, GREY_D),
        C(560, 408, 32, GREY),
        E(548, 394, 11, 7, GREY_L, 0.9),
        E(598, 416, 6, 4, GREY_L, 0.9),
    )


def medal():
    """金奖牌：红缎带交叉 + 金圆牌（深边 + 浅芯 + 深金星）。"""
    return wrap(
        PG([(546, 330), (570, 330), (586, 390), (560, 396)], RED),
        PG([(594, 330), (618, 330), (590, 396), (578, 390)], RED_D),
        C(570, 411, 34, GOLD_D),
        C(566, 408, 32, GOLD),
        C(566, 408, 20, GOLD_L),
        star5(566, 408, 13, GOLD_D),
    )


def key():
    """银钥匙：圆环头（环孔透底）+ 银柄 + 两个齿。"""
    return wrap(
        R(550, 394, 24, 56, 10, SILV),
        R(564, 396, 10, 52, 5, SILV_D, 0.7),
        R(574, 414, 20, 11, 4, SILV),
        R(574, 432, 24, 11, 4, SILV),
        C(566, 367, 34, SILV_D),
        C(562, 364, 31, SILV),
        C(562, 364, 13, PAGE),
        E(548, 350, 8, 5, SILV_L, 0.9),
    )


def arts():
    return {
        "red": ground() + butterfly(380, 205, *SET_RED) + apple(),
        "yellow": ground() + butterfly(380, 205, *SET_YELLOW) + banana(),
        "green": ground() + butterfly(380, 205, *SET_GREEN) + leaf(),
        "blue": ground() + butterfly(380, 205, *SET_BLUE) + cup(566, 316, 96, 116, 0.62),
        "black": ground() + butterfly(380, 205, *SET_BLACK) + cat(),
        "white": ground() + _wing_backing() + butterfly(380, 205, *SET_WHITE) + milk_cup(),
        "pink": ground() + butterfly(380, 205, *SET_PINK) + blossom(),
        "purple": ground() + butterfly(380, 205, *SET_PURPLE) + grapes(),
        "brown": ground() + butterfly(380, 205, *SET_BROWN) + stool(),
        "grey": ground() + butterfly(380, 205, *SET_GREY) + stone(),
        "gold": ground() + butterfly(380, 205, *SET_GOLD) + medal(),
        "silver": ground() + butterfly(380, 205, *SET_SILVER) + key(),
    }
