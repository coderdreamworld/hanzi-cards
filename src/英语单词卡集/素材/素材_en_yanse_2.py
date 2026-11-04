#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 颜色·形状（yanse）第 2 段插画（8 卡：rainbow~crescent）。

形状系列：主形居中放大（占画布高度 50%~70%），积木类用深一号底偏移 + 浅色顶面做体积。
rainbow=赤橙黄绿青蓝紫七条同心拱带两端小云朵；circle=蓝色大圆积木+小皮球；
square=红色方形积木+缎带十字礼盒；triangle=黄色三角积木+红顶小屋；
rectangle=绿色长方积木+圆把手木门；heart=大红心形靠垫加粉色高光；
diamond=橙色菱形积木+十字骨架风筝带尾穗；crescent=浅蓝夜空横幅（画在 ground 之上）铺星星托黄月牙。
相邻主色错开：七彩→蓝→红→黄→绿→红→橙→黄。伴物缩右下 25%。每卡第一笔 ground()；
无描边无渐变；图上无文字数字。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "rainbow", "cn": "彩虹"},
    {"w": "circle", "cn": "圆形"},
    {"w": "square", "cn": "正方形"},
    {"w": "triangle", "cn": "三角形"},
    {"w": "rectangle", "cn": "长方形"},
    {"w": "heart", "cn": "心形"},
    {"w": "diamond", "cn": "菱形"},
    {"w": "crescent", "cn": "月牙形"},
]

# ---------- 本组同族补充色 ----------
ORANGE, ORANGE_D, ORANGE_L = "#f08a3e", "#d1702a", "#f8bd74"  # 橙族（菱形积木）
PURP, PURP_L = "#9b7fc4", "#c0aae0"                            # 紫族（彩虹最内带 / 星）
GREEN_D = "#5e8f52"                                            # 绿族深（长方积木厚度）
BLUE_L = "#a5d3ee"                                             # 蓝族浅（圆积木高光）


# ---------- 通用形状 ----------
def arc_band(cx, cy, r_o, r_i, fill):
    """半圆拱带：外弧 r_o、内弧 r_i，两端落在 (cx±r, cy) 地面线上。"""
    return P(f"M {cx-r_o} {cy} A {r_o} {r_o} 0 0 1 {cx+r_o} {cy} "
             f"L {cx+r_i} {cy} A {r_i} {r_i} 0 0 0 {cx-r_i} {cy} Z", fill)


# ---------- 各卡主形与伴物 ----------
def rainbow_arch():
    """赤橙黄绿青蓝紫七条同心拱带（带宽 17），雨点两点，两端云朵压拱脚。"""
    g = ""
    for r_o, color in ((252, RED), (235, ORANGE), (218, YEL), (201, GREEN),
                       (184, TEAL), (167, BLUE), (150, PURP)):
        g += arc_band(380, 430, r_o, r_o - 17, color)
    g += drop(84, 132, 14)            # 雨后残雨两点
    g += drop(676, 118, 12)
    g += cloud_p(150, 426, 1.15)      # 左右小云朵压住拱脚
    g += cloud_p(610, 426, 1.15)
    return g


def circle_block():
    """蓝色大圆积木：深底偏移出厚度 + 正面 + 左上高光；右下小皮球。"""
    return wrap(
        C(380, 322, 122, BLUE_D),
        C(380, 304, 122, BLUE),
        E(336, 250, 36, 22, BLUE_L, 0.85),
        ball(608, 398, 44),
    )


def square_block():
    """红色方形积木：深底偏移 + 正面 + 浅色顶带；右下缎带十字礼盒。"""
    return wrap(
        R(266, 210, 248, 248, 18, RED_D),
        R(252, 196, 248, 248, 18, RED),
        R(252, 196, 248, 42, 16, PINK),
        R(540, 362, 136, 22, 10, TEAL_D),   # 礼盒盖
        R(548, 376, 120, 64, 10, TEAL),     # 盒身
        R(598, 376, 20, 64, 4, SUN),        # 竖缎带
        R(548, 398, 120, 18, 6, SUN),       # 横缎带（十字）
        C(600, 354, 11, SUN),               # 蝴蝶结双环
        C(616, 354, 11, SUN),
        C(608, 358, 7, SUN_L),              # 结心
    )


def triangle_block():
    """黄色三角积木：主面 + 右侧深色棱面；右下红三角顶小屋（方墙身+圆窗）。"""
    return wrap(
        PG([(380, 176), (560, 442), (200, 442)], YEL),
        PG([(380, 176), (560, 442), (452, 442)], YEL_D),
        R(574, 398, 92, 44, 5, WOOD_L),                 # 方墙身
        PG([(562, 402), (678, 402), (620, 352)], RED),  # 三角屋顶
        C(620, 422, 9, SUN),                            # 圆窗
    )


def rectangle_block():
    """绿色长方积木（竖放）：深底偏移 + 正面 + 浅色顶带；右下圆把手木门。"""
    return wrap(
        R(292, 192, 200, 260, 18, GREEN_D),
        R(280, 180, 200, 260, 18, GREEN),
        R(280, 180, 200, 44, 16, GREEN_L),
        R(576, 336, 88, 106, 10, WOOD),     # 长方门板
        R(590, 352, 60, 42, 8, WOOD_L),     # 上门芯
        R(590, 402, 60, 26, 8, WOOD_L),     # 下门芯
        C(650, 390, 8, SUN),                # 圆把手
    )


def heart_cushion():
    """大红心形靠垫：深底偏移 + 主心 + 左右两瓣粉色高光。"""
    return wrap(
        heart(388, 306, 150, RED_D),
        heart(380, 298, 150, RED),
        f'<g transform="rotate(-22 300 246)">' + E(300, 246, 30, 16, PINK, 0.9) + "</g>",
        f'<g transform="rotate(22 460 246)">' + E(460, 246, 30, 16, PINK, 0.9) + "</g>",
    )


def diamond_block():
    """橙色菱形积木：左亮右暗两棱面 + 高光；右下十字骨架风筝带尾穗。"""
    return wrap(
        PG([(380, 160), (540, 300), (380, 440), (220, 300)], ORANGE),
        PG([(380, 160), (540, 300), (380, 440)], ORANGE_D),
        f'<g transform="rotate(-45 315 245)">' + E(315, 245, 40, 13, ORANGE_L, 0.85) + "</g>",
        PG([(604, 330), (652, 388), (604, 446), (556, 388)], BLUE),  # 风筝面
        L(604, 330, 604, 446, WHITE, 3),    # 竖骨架
        L(556, 388, 652, 388, WHITE, 3),    # 横骨架
        L(604, 446, 578, 468, INK, 3),      # 尾线
        PG([(596, 444), (602, 451), (596, 458), (590, 451)], SUN),   # 尾穗结×2
        PG([(586, 454), (592, 461), (586, 468), (580, 461)], SUN),
    )


def night_moon():
    """浅蓝夜空横幅（盖在 ground 上）铺星星；黄色大月牙开口朝右 + 高光。"""
    g = R(0, 0, 760, 452, 24, BLUE_D)
    g += star5(150, 110, 16, SUN) + star5(600, 84, 13, SUN)
    g += star5(520, 190, 10, SUN_L) + star5(236, 244, 9, SUN_L) + star5(84, 300, 12, SUN_L)
    g += C(320, 76, 5, WHITE) + C(676, 244, 6, WHITE) + C(108, 192, 5, WHITE)
    g += C(452, 120, 4, WHITE, 0.9)
    g += P("M 380 140 A 150 150 0 0 0 380 440 A 190 190 0 0 1 380 140 Z", YEL)
    g += f'<g transform="rotate(-35 300 220)">' + E(300, 220, 26, 13, SUN_L, 0.9) + "</g>"
    return g


def arts():
    return {
        "rainbow": ground() + rainbow_arch(),
        "circle": ground() + circle_block(),
        "square": ground() + square_block(),
        "triangle": ground() + triangle_block(),
        "rectangle": ground() + rectangle_block(),
        "heart": ground() + heart_cushion(),
        "diamond": ground() + diamond_block(),
        "crescent": ground() + night_moon(),
    }
