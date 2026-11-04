#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 数字（shuzi）插画（13 卡）。

造型要点：zero 空木盘（椭圆盘+浅内圈，无苹果）；one~twelve 全部共用同一只
红苹果（红圆果 r≈54×s + 深一号底偏移 + 褐色短柄 + 单片绿叶 + 左上浅高光），
按数量摆盘：one 居中 1 颗、two 并排 2 颗、three 品字、four 2×2、five 上2下3、
six 2×3、seven 上3下4、eight 2×4、nine 3×3、ten 2×5、eleven 下6上5 两排、
twelve 3×4。苹果只换坐标与 s（1~4 用 1.0~0.9、5~9 用 0.72、10~12 用 0.6），
逐颗 ±5° 微转增自然感；图上不画任何数字或点数记号。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "zero", "cn": "零"},
    {"w": "one", "cn": "一"},
    {"w": "two", "cn": "二"},
    {"w": "three", "cn": "三"},
    {"w": "four", "cn": "四"},
    {"w": "five", "cn": "五"},
    {"w": "six", "cn": "六"},
    {"w": "seven", "cn": "七"},
    {"w": "eight", "cn": "八"},
    {"w": "nine", "cn": "九"},
    {"w": "ten", "cn": "十"},
    {"w": "eleven", "cn": "十一"},
    {"w": "twelve", "cn": "十二"},
]


# ---------- 本组同族补充色 ----------
APPLE_L = "#f59b78"   # 红族浅（苹果高光，与水果组同源）
STEMG = "#5d8a52"     # 绿族深（叶脉）
WOOD_XL = "#f4d3a4"   # 木族特浅（盘心，同 lid 内衬色）


# ---------- 系列硬规则：单只红苹果（全组唯一造型，只换 x/y/s） ----------
def apple(x, y, s=1.0):
    """单只红苹果。(x,y)=果心，r≈54×s；红圆果+深一号底偏移+褐短柄+单片绿叶+左上浅高光。"""
    r = 54.0 * s
    return wrap(
        C(x + 0.05 * r, y + 0.08 * r, r, RED_D),                                   # 深一号底偏移
        C(x - 0.03 * r, y - 0.05 * r, 0.955 * r, RED),                             # 红圆果
        E(x, y - 0.84 * r, 0.30 * r, 0.10 * r, RED_D, 0.8),                        # 顶部果窝
        f'<g transform="rotate(-26 {x - 0.34 * r:.1f} {y - 0.32 * r:.1f})">'
        + E(x - 0.34 * r, y - 0.32 * r, 0.19 * r, 0.30 * r, APPLE_L, 0.8) + "</g>",  # 左上浅高光
        P(f"M {x:.1f} {y - 0.78 * r:.1f} Q {x + 0.06 * r:.1f} {y - 1.04 * r:.1f}"
          f" {x + 0.15 * r:.1f} {y - 1.26 * r:.1f}", stroke=WOOD_D, w=max(4.5, 9 * s)),  # 褐色短柄
        f'<g transform="rotate(28 {x + 0.46 * r:.1f} {y - 1.00 * r:.1f})">'
        + E(x + 0.46 * r, y - 1.00 * r, 0.40 * r, 0.16 * r, GREEN)
        + L(x + 0.16 * r, y - 1.00 * r, x + 0.76 * r, y - 1.00 * r, STEMG, max(2, 3 * s))
        + "</g>",                                                                   # 单片绿叶+叶脉
    )


TILTS = (4, -3, 2, -5, 5, -2, 3, -4, 1, -3, 4, -1)   # ±5° 确定性微转


def pile(rows, s, y_bot=440):
    """按数量摆苹果。rows 自下而上每排颗数（如 [3,2]=上2下3）；
    水平间距 112×s、排距 2r+12，紧凑不重叠；底排先画、上排后画（叶尖收进上层果后）。"""
    r = 54.0 * s
    dx = 112.0 * s
    dy = 2 * r + 12
    g = ""
    idx = 0
    for ri, cols in enumerate(rows):
        y = y_bot - r - ri * dy
        span = (cols - 1) * dx
        for ci in range(cols):
            x = 380 - span / 2 + ci * dx
            g += (f'<g transform="rotate({TILTS[idx % len(TILTS)]} {x:.1f} {y:.1f})">'
                  + apple(x, y, s) + "</g>")
            idx += 1
    return g


# ---------- 0 zero 空木盘 ----------
def art_zero():
    g = ground()
    g += E(380, 404, 210, 62, WOOD_D)                    # 盘底外缘（深）
    g += E(380, 398, 204, 58, WOOD)                      # 盘身
    g += E(380, 404, 154, 38, WOOD_L)                    # 浅内圈
    g += E(380, 406, 116, 26, WOOD_XL, 0.75)             # 盘心更浅
    g += f'<g transform="rotate(-16 280 372)">' + E(280, 372, 30, 9, WOOD_L, 0.8) + "</g>"  # 沿口高光
    return g


def art_one(): return ground() + pile([1], 1.0)
def art_two(): return ground() + pile([2], 0.98)
def art_three(): return ground() + pile([2, 1], 0.95)      # 品字
def art_four(): return ground() + pile([2, 2], 0.9)        # 2×2
def art_five(): return ground() + pile([3, 2], 0.72)       # 上2下3
def art_six(): return ground() + pile([3, 3], 0.72)        # 2×3
def art_seven(): return ground() + pile([4, 3], 0.72)      # 上3下4
def art_eight(): return ground() + pile([4, 4], 0.72)      # 2×4
def art_nine(): return ground() + pile([3, 3, 3], 0.72)    # 3×3
def art_ten(): return ground() + pile([5, 5], 0.6)         # 2×5
def art_eleven(): return ground() + pile([6, 5], 0.6)      # 下6上5 两排
def art_twelve(): return ground() + pile([4, 4, 4], 0.6)   # 3×4


def arts():
    return {
        "zero": art_zero(),
        "one": art_one(),
        "two": art_two(),
        "three": art_three(),
        "four": art_four(),
        "five": art_five(),
        "six": art_six(),
        "seven": art_seven(),
        "eight": art_eight(),
        "nine": art_nine(),
        "ten": art_ten(),
        "eleven": art_eleven(),
        "twelve": art_twelve(),
    }
