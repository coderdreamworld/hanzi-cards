#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比组 16 对插画与文案（1000 字批次 B10）。

字表（与字库1000 duibi 组尾部一致）：粗细 厚薄 深浅 干湿 软硬 饱饿 沉浮
浓淡 宽窄 阴晴 卷展 睁闭 吞吐 输赢 挖填 香臭。

对比卡画法约定（沿 legacy 识字卡片_素材_duibi.py，与种子卡 大小/上下 一致）：
- 画布 760×480 左右分半：左半中心 x≈240 = 第一个字，右半中心 x≈560 = 第二个字；
- 每半各自一块 hg() 半边地面（rx≈148），两半主体间隔 ≥60px；
- 同一物件只变对比维度；方向性对比（沉浮/吞吐/睁闭/挖填等）左=第一个字，绝不反。
字标（两字分压两半正上方）由卡片模板渲染，图内无文字。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
GRAY, GRAY_D = "#a8a094", "#8f887c"          # 石头/天平静灰
CAT_F, CAT_F_D, CAT_F_L = "#f4a7b9", "#e08ba0", "#fbd0da"   # 毛绒球粉
TOWEL, TOWEL_D = "#f5b8a0", "#f0987e"        # 毛巾蜜桃
CLOUD_D, CLOUD_M = "#aebbc6", "#c6d0d8"      # 阴天乌云
PAPER, PAPER_D, PAPER_L = "#f7ecd2", "#efe0bc", "#e7d5ae"   # 画卷纸
FISH, FISH_D, FISH_L = "#e8935c", "#c97a44", "#f4b58a"      # 橙鱼
DIRT, DIRT_D, DIRT_L = "#b57b44", "#8a5a33", "#c89058"      # 泥土
STINK = "#a8b06a"                             # 臭气橄榄绿
SCENT = "#d9b98a"                             # 香气暖沙
STEEL = "#c9cdd1"                             # 铁锹金属


def hg(cx, cy=446, rx=148, ry=20):
    """对比卡半边地面。"""
    return E(cx, cy, rx, ry, GROUND)


# ---------- 1 粗细：同色绳一粗一细 ----------
def art_粗细():
    thick_d = "M 104 372 Q 146 320 188 372 Q 230 424 272 372 Q 314 320 356 372"
    thin_d = "M 452 386 Q 494 334 536 386 Q 578 438 620 386 Q 662 334 704 386"
    thick = wrap(
        P(thick_d, stroke=TEAL_D, w=46),
        P(thick_d, stroke=TEAL, w=36),
        P("M 110 366 Q 148 322 190 370", stroke=TEAL_L, w=10, opacity=0.85),
        L(146, 326, 146, 368, TEAL_D, 5),
        L(230, 378, 230, 420, TEAL_D, 5),
        L(314, 326, 314, 368, TEAL_D, 5))
    thin = wrap(
        P(thin_d, stroke=TEAL, w=14),
        P("M 456 382 Q 496 336 538 384", stroke=TEAL_L, w=5, opacity=0.85),
        L(494, 352, 494, 366, TEAL_D, 4),
        L(578, 404, 578, 418, TEAL_D, 4),
        L(662, 352, 662, 366, TEAL_D, 4))
    return wrap(hg(240), hg(560), thick, thin)


# ---------- 2 厚薄：同样的书一厚一薄 ----------
def art_厚薄():
    thick = wrap(
        R(166, 246, 140, 190, 12, RED),            # 厚书封面
        R(168, 250, 16, 182, 8, RED_D),            # 书脊
        R(184, 262, 78, 30, 8, WHITE, 0.55),       # 封面亮带
        R(300, 254, 26, 174, 4, WHITE),            # 书页
        L(304, 296, 322, 296, "#e3ded2", 3),
        L(304, 330, 322, 330, "#e3ded2", 3),
        L(304, 364, 322, 364, "#e3ded2", 3),
        L(304, 398, 322, 398, "#e3ded2", 3))
    thin = wrap(
        R(486, 352, 140, 82, 10, RED),             # 薄书封面
        R(488, 355, 14, 76, 7, RED_D),
        R(620, 358, 20, 70, 4, WHITE),
        L(623, 380, 636, 380, "#e3ded2", 3),
        L(623, 402, 636, 402, "#e3ded2", 3))
    return wrap(hg(240), hg(560), thick, thin)


# ---------- 3 深浅：同样的杯子，水一深一浅 ----------
def _glass(cx, level, color, op=None, drip=False):
    """透明玻璃杯（杯身加实，避免网格缩略时消失）。"""
    top, w, h = 268, 150, 176
    x0 = cx - w / 2
    body = P(f"M {x0} {top} L {x0+13} {top+h-16} Q {x0+15} {top+h} {x0+32} {top+h} "
             f"L {x0+w-32} {top+h} Q {x0+w-15} {top+h} {x0+w-13} {top+h-16} L {x0+w} {top} Z",
             "#dceef5", 0.9)
    wy0 = top + h * (1 - level)
    liquid = P(f"M {x0+7} {wy0} Q {cx-35} {wy0-10} {cx} {wy0-2} Q {cx+35} {wy0+6} {x0+w-7} {wy0} "
               f"L {x0+w-16} {top+h-16} Q {x0+w-18} {top+h-8} {x0+w-32} {top+h-8} "
               f"L {x0+32} {top+h-8} Q {x0+18} {top+h-8} {x0+16} {top+h-16} Z", color, op)
    g = wrap(
        E(cx, top, w / 2, 14, "#cfe6f0"), body, liquid,
        E(cx, wy0, w * 0.43, 8, "#a5d9f0" if color == WBLUE else "#fefbf2", 0.9),
        R(x0 + 22, top + 18, 14, h * level - 8, 7, WHITE, 0.6))
    if drip:
        g += drop(cx + w / 2 - 6, top + 66, 9, color)
    return g


def art_深浅():
    return wrap(hg(240, 442), hg(560, 442),
                _glass(240, 0.82, WBLUE), _glass(560, 0.28, WBLUE))


# ---------- 4 干湿：同样的毛巾，干的清爽 / 湿的滴水 ----------
def _towel(cx, wet):
    x0, y0, w, h = cx - 85, 316, 170, 88
    g = R(x0, y0, w, h, 14, TOWEL)
    g += R(x0, y0 + 16, w, 13, 6, TOWEL_D)
    g += R(x0, y0 + 50, w, 13, 6, TOWEL_D)
    g += L(x0 + 16, y0 + 34, x0 + w - 16, y0 + 34, "#e88a70", 4)
    if wet:
        g += R(x0 + 6, y0 + 6, w - 12, h - 12, 10, WBLUE, 0.22)   # 湿漉漉的水色
        g += drop(x0 + 32, y0 + h + 24, 11)
        g += drop(cx, y0 + h + 36, 9)
        g += drop(x0 + w - 32, y0 + h + 24, 10)
        g += E(cx, 448, 70, 10, WBLUE, 0.85)
        g += E(cx - 18, y0 + h - 2, 28, 6, WHITE, 0.5)
    return g


def art_干湿():
    return wrap(hg(240), hg(560), _towel(240, False), _towel(560, True))


# ---------- 5 软硬：毛绒球软 / 石头硬 ----------
def art_软硬():
    fuzz = ""
    for i in range(14):
        a = i * 2 * math.pi / 14 + 0.2
        fuzz += L(240 + 62 * math.cos(a), 356 + 62 * math.sin(a),
                  240 + 79 * math.cos(a), 356 + 79 * math.sin(a), CAT_F, 6)
    plush = wrap(
        C(243, 359, 64, CAT_F_D),
        C(239, 355, 60, CAT_F),
        C(220, 336, 15, CAT_F_L, 0.9),
        fuzz)
    stone = wrap(
        E(560, 386, 62, 40, GRAY),
        E(570, 394, 46, 27, GRAY_D),
        L(536, 372, 560, 366, GRAY_D, 4))
    return wrap(hg(240), hg(560), plush, stone)


# ---------- 6 饱饿：同一小朋友，圆鼓肚 / 瘪肚子 ----------
def art_饱饿():
    g = wrap(hg(240, 442), hg(560, 442))
    g += kid(240, 440, s=0.88, face="open", shirt=RED)
    g += E(240, 376, 50, 44, "#f0876f")                 # 圆鼓肚（浅一号更醒目）
    g += E(240, 374, 46, 41, RED)
    g += P("M 194 394 Q 240 430 286 394", stroke=RED_D, w=5)
    g += C(240, 404, 4, RED_D)                          # 肚脐
    g += kid(560, 440, s=0.88, face="sad", shirt=RED, look=(0, 1))
    g += P("M 520 356 Q 560 382 600 356", stroke=RED_D, w=6)   # 瘪肚子褶
    g += P("M 486 372 q 9 -10 18 0 q 9 10 18 0", stroke=INK, w=4)   # 肚子咕咕叫
    g += P("M 480 398 q 9 -10 18 0 q 9 10 18 0", stroke=INK, w=4)
    g += bowl(642, 428, 26, rice=False)                 # 吃空的小碗
    return g


# ---------- 7 沉浮：同色球一沉水底一浮水面 ----------
def _tank(cx):
    x0, w = cx - 84, 168
    return wrap(
        R(x0, 248, 10, 180, 5, "#b7d8ec"),
        R(x0 + w - 10, 248, 10, 180, 5, "#b7d8ec"),
        R(x0, 420, w, 12, 6, "#b7d8ec"),
        R(x0 + 10, 318, w - 20, 102, 4, WBLUE),
        E(cx, 318, w / 2 - 10, 8, "#a5d9f0", 0.9))


def art_沉浮():
    g = wrap(hg(240), hg(560))
    g += _tank(240)
    g += ball(240, 388, 30, BLUE, BLUE_D, "#a8d4ef")     # 沉在水底
    g += _tank(560)
    g += ball(560, 322, 30, BLUE, BLUE_D, "#a8d4ef")     # 浮在水面
    g += P("M 494 334 q 14 10 28 0", stroke="#a5d9f0", w=5)
    g += P("M 598 334 q 14 10 28 0", stroke="#a5d9f0", w=5)
    return g


# ---------- 8 浓淡：同样的牛奶，一杯浓一杯淡 ----------
def art_浓淡():
    return wrap(hg(240, 442), hg(560, 442),
                _glass(240, 0.70, "#eed9a4", drip=True),     # 浓：色深挂壁
                _glass(560, 0.70, "#f9f1dd", op=0.88))       # 淡：色浅


# ---------- 9 宽窄：同样的路一宽一窄 ----------
def art_宽窄():
    wide = wrap(
        E(240, 316, 172, 12, GREEN_L, 0.9), E(240, 428, 172, 12, GREEN_L, 0.9),
        R(74, 326, 332, 92, 30, "#ead9b6"),
        L(96, 338, 384, 338, "#d9c49a", 6),
        L(96, 406, 384, 406, "#d9c49a", 6),
        L(122, 372, 158, 372, WHITE, 8), L(182, 372, 218, 372, WHITE, 8),
        L(242, 372, 278, 372, WHITE, 8), L(302, 372, 338, 372, WHITE, 8),
        L(362, 372, 386, 372, WHITE, 8))
    narrow = wrap(
        E(560, 366, 122, 9, GREEN_L, 0.9), E(560, 424, 122, 9, GREEN_L, 0.9),
        R(446, 372, 228, 46, 18, "#ead9b6"),
        L(458, 379, 662, 379, "#d9c49a", 5),
        L(458, 411, 662, 411, "#d9c49a", 5),
        L(480, 395, 502, 395, WHITE, 5), L(526, 395, 548, 395, WHITE, 5),
        L(572, 395, 594, 395, WHITE, 5), L(618, 395, 640, 395, WHITE, 5))
    return wrap(hg(240), hg(560), wide, narrow)


# ---------- 10 阴晴：乌云遮天是阴 / 太阳露脸是晴 ----------
def art_阴晴():
    clouds = wrap(
        cloud_p(236, 192, 1.5, CLOUD_D),
        cloud_p(318, 244, 1.0, CLOUD_M),
        cloud_p(158, 250, 0.85, CLOUD_M))
    rays = ""
    for i in range(8):
        a = i * math.pi / 4
        rays += L(560 + 78 * math.cos(a), 196 + 78 * math.sin(a),
                  560 + 100 * math.cos(a), 196 + 100 * math.sin(a), "#f2a72e", 7)
    sun = wrap(C(560, 196, 64, SUN), C(542, 178, 14, SUN_L, 0.9), rays,
               cloud_p(658, 262, 0.65, WHITE))
    return wrap(hg(240), hg(560), clouds, sun)


# ---------- 11 卷展：同一幅画卷，一卷一展 ----------
def art_卷展():
    rolled = wrap(
        C(118, 378, 16, WOOD_D), C(342, 378, 16, WOOD_D),      # 两端卷轴头
        R(148, 334, 150, 88, 44, PAPER),
        R(148, 392, 150, 30, 15, PAPER_D),
        C(296, 378, 44, PAPER_L), C(296, 378, 31, PAPER),
        C(296, 378, 19, PAPER_L), C(296, 378, 8, WOOD_D))      # 卷起的纸层
    unrolled = wrap(
        R(432, 268, 24, 178, 12, WOOD), R(664, 268, 24, 178, 12, WOOD),
        C(444, 258, 14, WOOD_D), C(676, 258, 14, WOOD_D),
        R(456, 276, 208, 164, 4, PAPER),
        C(626, 316, 15, SUN),
        PG([(470, 430), (524, 358), (578, 430)], GREEN),
        PG([(542, 430), (600, 370), (654, 430)], "#6a955c"),
        L(468, 430, 652, 430, "#b57b44", 4))
    return wrap(hg(240), hg(560), rolled, unrolled)


# ---------- 12 睁闭：同样的脸，两眼睁开 / 两眼闭上 ----------
def _face(cx, open_eye):
    g = C(cx, 306, 110, SKIN)
    g += C(cx - 106, 318, 13, SKIN) + C(cx + 106, 318, 13, SKIN)   # 耳朵
    g += P(f"M {cx-98} 300 Q {cx-98} 202 {cx} 198 Q {cx+98} 202 {cx+98} 300 "
           f"Q {cx+48} 252 {cx} 254 Q {cx-48} 252 {cx-98} 300 Z", HAIR)
    for ex in (-44, 44):
        if open_eye:
            g += E(cx + ex, 314, 27, 32, WHITE)
            g += C(cx + ex, 317, 14, "#7a4e2c")
            g += C(cx + ex, 317, 7, INK)
            g += C(cx + ex + 5, 311, 3.6, WHITE)
            g += P(f"M {cx+ex-28} 292 Q {cx+ex} 274 {cx+ex+28} 292", stroke=INK, w=5)
        else:
            g += P(f"M {cx+ex-28} 318 Q {cx+ex} 344 {cx+ex+28} 318", stroke=INK, w=7)
            g += L(cx + ex - 18, 332, cx + ex - 26, 346, INK, 4)
            g += L(cx + ex, 336, cx + ex, 350, INK, 4)
            g += L(cx + ex + 18, 332, cx + ex + 26, 346, INK, 4)
    g += P(f"M {cx-24} 380 Q {cx} 400 {cx+24} 380", stroke=INK, w=6)
    g += C(cx - 72, 350, 12, PINK, 0.8) + C(cx + 72, 350, 12, PINK, 0.8)
    return g


def art_睁闭():
    return wrap(hg(240, 446), hg(560, 446), _face(240, True), _face(560, False))


# ---------- 13 吞吐：同一条鱼，张嘴吞 / 吐泡泡 ----------
def _fish_base(cx, cy):
    return wrap(
        PG([(cx - 74, cy), (cx - 126, cy - 46), (cx - 126, cy + 46)], FISH_D),
        E(cx, cy, 86, 54, FISH),
        E(cx - 8, cy + 18, 62, 26, FISH_L, 0.75),
        P(f"M {cx-36} {cy-50} Q {cx} {cy-88} {cx+42} {cy-48} Z", FISH_D),
        P(f"M {cx-2} {cy-26} Q {cx-14} {cy} {cx-2} {cy+26}", stroke=FISH_D, w=5),
        E(cx - 14, cy + 26, 20, 12, FISH_D))


def art_吞吐():
    cx, cy = 232, 352
    swallow = wrap(
        _fish_base(cx, cy),
        C(cx + 30, cy - 34, 9, WHITE), C(cx + 32, cy - 34, 5, INK),
        PG([(cx + 30, cy - 16), (cx + 104, cy - 54), (cx + 104, cy + 46), (cx + 30, cy + 26)], "#8a3a26"),
        P(f"M {cx+22} {cy-40} Q {cx+70} {cy-62} {cx+104} {cy-54}", stroke=FISH, w=20),
        P(f"M {cx+22} {cy+30} Q {cx+72} {cy+52} {cx+104} {cy+46}", stroke=FISH, w=20),
        # 正被吞进去的小鱼
        PG([(cx + 116, cy - 4), (cx + 138, cy - 20), (cx + 138, cy + 12)], YEL),
        E(cx + 128, cy - 4, 16, 10, YEL),
        C(cx + 134, cy - 7, 2.5, INK))
    cx2 = 568
    blow = wrap(
        _fish_base(cx2, cy),
        C(cx2 + 34, cy - 22, 9, WHITE), C(cx2 + 36, cy - 22, 5, INK),
        C(cx2 + 84, cy + 6, 10, "#8a3a26"),
        C(cx2 + 108, cy - 6, 13, WBLUE), C(cx2 + 104, cy - 9, 4, WHITE, 0.8),
        C(cx2 + 128, cy - 40, 10, WBLUE), C(cx2 + 125, cy - 43, 3, WHITE, 0.8),
        C(cx2 + 142, cy - 74, 7, WBLUE),
        C(cx2 + 150, cy - 100, 5, WBLUE))
    return wrap(hg(240), hg(560), swallow, blow)


# ---------- 14 输赢：下棋，愁脸输了 / 笑脸赢了 ----------
def _chess_board(cx):
    return wrap(
        R(cx - 84, 396, 168, 46, 8, WOOD_D),
        R(cx - 84, 396, 168, 12, 6, WOOD),
        L(cx - 84, 418, cx + 84, 418, "#8a5a33", 3),
        L(cx - 28, 396, cx - 28, 442, "#8a5a33", 3),
        L(cx + 28, 396, cx + 28, 442, "#8a5a33", 3),
        C(cx - 56, 410, 8, INK), C(cx + 2, 408, 8, WHITE), C(cx + 56, 412, 8, INK))


def art_输赢():
    g = wrap(hg(240), hg(560))
    g += kid(240, 438, s=0.7, pose="sit", face="sad", shirt=TEAL, look=(0, 1.2))
    g += kid(560, 438, s=0.7, pose="sit", face="open", arms="up", shirt=TEAL)
    g += _chess_board(240) + _chess_board(560)
    g += star5(560, 150, 30)
    return g


# ---------- 15 挖填：铲子挖坑 / 土把坑填上 ----------
def art_挖填():
    dig = wrap(
        E(250, 424, 66, 20, DIRT_D),
        E(250, 422, 50, 13, "#6e4526"),                    # 深坑
        E(146, 424, 34, 16, DIRT), E(140, 414, 20, 10, DIRT_L),   # 挖出的土堆
        L(322, 300, 270, 408, "#d9a05b", 10),
        C(322, 296, 11, "#d9a05b"),
        PG([(270, 408), (246, 430), (282, 440), (294, 416)], STEEL))
    fill = wrap(
        E(560, 434, 84, 12, DIRT_D, 0.55),                 # 坑口边缘
        E(560, 418, 76, 26, DIRT), E(560, 404, 48, 18, DIRT_L),   # 填起来的土堆
        L(648, 300, 598, 400, "#d9a05b", 10),
        C(648, 296, 11, "#d9a05b"),
        PG([(598, 400), (576, 422), (612, 430), (624, 406)], STEEL))
    return wrap(hg(240), hg(560), dig, fill)


# ---------- 16 香臭：花儿香 / 臭袜捂鼻 ----------
def art_香臭():
    flower = wrap(
        L(240, 424, 240, 302, GREEN, 11),
        f'<g transform="rotate(-26 208 372)">{E(208, 372, 26, 12, GREEN)}</g>',
        f'<g transform="rotate(26 272 340)">{E(272, 340, 26, 12, GREEN)}</g>',
        flower5(240, 262, 46, "#f0876f", SUN),
        P("M 198 178 q 12 -16 0 -32 q -12 -16 0 -32", stroke=SCENT, w=5),
        P("M 282 184 q 12 -16 0 -32 q -12 -16 0 -32", stroke=SCENT, w=5))
    sock = wrap(
        E(576, 430, 74, 11, "#c9cdd1", 0.5),
        P("M 516 286 L 516 366 Q 516 402 552 402 L 606 402 Q 632 402 632 378 "
          "Q 632 354 606 354 L 568 354 L 568 286 Z", WHITE),
        E(606, 380, 18, 11, "#e8e4d8", 0.85),
        R(508, 272, 68, 26, 10, "#f0876f"),
        P("M 496 252 l 16 -20 l -14 -20 l 16 -20", stroke=STINK, w=6),
        P("M 566 232 l 16 -20 l -14 -20 l 16 -20", stroke=STINK, w=6),
        P("M 638 256 l 16 -20 l -14 -20 l 16 -20", stroke=STINK, w=6))
    return wrap(hg(240), hg(560), flower, sock)


# ---------- 组装 ----------
def arts():
    keys = ["粗细", "厚薄", "深浅", "干湿", "软硬", "饱饿", "沉浮", "浓淡",
            "宽窄", "阴晴", "卷展", "睁闭", "吞吐", "输赢", "挖填", "香臭"]
    return {k: globals()[f"art_{k}"]() for k in keys}


GROUP_CARDS = [
    {"pair": ["粗", "细"], "key": "粗细", "pinyin": "cū · xì", "tone": "第一声 · 第四声",
     "sentence": "粗绳粗，细绳细。",
     "say": "两根绳子比一比，圆滚滚的是粗，瘦瘦的是细。",
     "chat": "“哪根绳子粗？哪根细？”",
     "life": "拿毛线和鞋带比一比粗细。"},
    {"pair": ["厚", "薄"], "key": "厚薄", "pinyin": "hòu · báo", "tone": "第四声 · 第二声（薄另读 bó，如“单薄”）",
     "sentence": "这本书厚，那本书薄。",
     "say": "比一比：这本厚厚的，那本薄薄的。",
     "chat": "“你更喜欢厚厚的书还是薄薄的书？”",
     "life": "把两本书叠一叠，摸摸哪本厚。"},
    {"pair": ["深", "浅"], "key": "深浅", "pinyin": "shēn · qiǎn", "tone": "第一声 · 第三声",
     "sentence": "这杯水深，那杯水浅。",
     "say": "水多的杯子深，水少的杯子浅。",
     "chat": "“洗澡水放深一点还是浅一点？”",
     "life": "倒两杯水摆一起，比比深浅。"},
    {"pair": ["干", "湿"], "key": "干湿", "pinyin": "gān · shī", "tone": "第一声 · 第一声（干另读 gàn，如“干活”）",
     "sentence": "毛巾干，毛巾湿。",
     "say": "干毛巾不掉水，湿毛巾会滴水。",
     "chat": "“晒晒太阳，毛巾会变干还是变湿？”",
     "life": "摸摸晾干的毛巾，再摸摸刚洗的。"},
    {"pair": ["软", "硬"], "key": "软硬", "pinyin": "ruǎn · yìng", "tone": "第三声 · 第四声",
     "sentence": "毛球软，石头硬。",
     "say": "按下去会瘪的是软，硬邦邦的是硬。",
     "chat": "“你的枕头是软的还是硬的？”",
     "life": "捏捏毛绒玩具，再摸摸桌子腿。"},
    {"pair": ["饱", "饿"], "key": "饱饿", "pinyin": "bǎo · è", "tone": "第三声 · 第四声",
     "sentence": "肚子饱，肚子饿。",
     "say": "肚子圆圆撑起来是饱，瘪瘪的咕咕叫是饿。",
     "chat": "“吃饱了和肚子饿，感觉有什么不一样？”",
     "life": "饭前摸摸瘪肚子，饭后摸摸圆肚子。"},
    {"pair": ["沉", "浮"], "key": "沉浮", "pinyin": "chén · fú", "tone": "第二声 · 第二声",
     "sentence": "小球沉底，小球上浮。",
     "say": "一样的球：这个沉到水底，那个浮在水面。",
     "chat": "“洗澡时小鸭子是沉还是浮？”",
     "life": "把球按进水里，松手看它浮起来。"},
    {"pair": ["浓", "淡"], "key": "浓淡", "pinyin": "nóng · dàn", "tone": "第二声 · 第四声",
     "sentence": "这杯奶浓，那杯奶淡。",
     "say": "颜色深味道重是浓，颜色浅味道轻是淡。",
     "chat": "“你喜欢浓浓的牛奶还是淡淡的？”",
     "life": "冲奶粉时闻一闻，多放一勺就浓。"},
    {"pair": ["宽", "窄"], "key": "宽窄", "pinyin": "kuān · zhǎi", "tone": "第一声 · 第三声",
     "sentence": "大路宽，小路窄。",
     "say": "宽宽的路好多人一起走，窄窄的只能一个走。",
     "chat": "“咱们家哪扇门宽，哪扇门窄？”",
     "life": "张开手臂量一量，走廊宽还是门窄。"},
    {"pair": ["阴", "晴"], "key": "阴晴", "pinyin": "yīn · qíng", "tone": "第一声 · 第二声",
     "sentence": "阴天乌云，晴天太阳。",
     "say": "天被乌云盖住是阴，太阳露脸是晴。",
     "chat": "“今天是阴天还是晴天？你怎么看出来的？”",
     "life": "早上看看天，说说今天是阴是晴。"},
    {"pair": ["卷", "展"], "key": "卷展", "pinyin": "juàn · zhǎn", "tone": "第四声 · 第三声（卷另读 juǎn，如“卷起来”）",
     "sentence": "画卷卷起来，画卷展开来。",
     "say": "卷起来是一根小筒，展开是一幅长长的画。",
     "chat": "“展开的画里有什么？指给妈妈看。”",
     "life": "把画纸卷一卷，再展开铺平看看。"},
    {"pair": ["睁", "闭"], "key": "睁闭", "pinyin": "zhēng · bì", "tone": "第一声 · 第四声",
     "sentence": "眼睛睁开，眼睛闭上。",
     "say": "眼睛张开是睁，眼皮合上就是闭。",
     "chat": "“眨眼睛的时候，是睁还是闭？”",
     "life": "玩睁一只眼闭一只眼的游戏。"},
    {"pair": ["吞", "吐"], "key": "吞吐", "pinyin": "tūn · tǔ", "tone": "第一声 · 第三声（吐另读 tù，如“呕吐”）",
     "sentence": "吞小鱼，吐泡泡。",
     "say": "张大嘴咽下去是吞，把泡泡送出来是吐。",
     "chat": "“小鱼一会儿吞一会儿吐，它在玩什么呀？”",
     "life": "吃东西要慢慢嚼，别急着吞。"},
    {"pair": ["输", "赢"], "key": "输赢", "pinyin": "shū · yíng", "tone": "第一声 · 第二声",
     "sentence": "下棋有输，也有赢。",
     "say": "愁眉苦脸是输了，笑得开心是赢了。",
     "chat": "“输了怎么办？赢了又怎么说？”",
     "life": "下盘棋，输了就说再来一盘。"},
    {"pair": ["挖", "填"], "key": "挖填", "pinyin": "wā · tián", "tone": "第一声 · 第二声",
     "sentence": "挖个坑，填上土。",
     "say": "用铲子把土挖走是挖，把土放回去是填。",
     "chat": "“挖好的坑，用什么填起来呀？”",
     "life": "沙坑里挖个坑，再用沙填满它。"},
    {"pair": ["香", "臭"], "key": "香臭", "pinyin": "xiāng · chòu", "tone": "第一声 · 第四声",
     "sentence": "花儿香，袜子臭。",
     "say": "香香的气味好闻，臭臭的气味要捂鼻。",
     "chat": "“你闻过什么香香的东西？臭的呢？”",
     "life": "闻闻香皂真香，快把臭袜子拿去洗。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_pairs = []
    for g in ziku.GROUPS:
        if g["id"] != "duibi":
            continue
        for it in g["chars"]:
            ziku_pairs.append(list(it) if isinstance(it, (list, tuple)) else [it])

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B10"] if e["file"] == "素材1000_duibi.py")
    expect = [list(p) for p in entry["对比卡"]]

    mine = [c["pair"] for c in GROUP_CARDS]
    a = arts()
    print(f"对比组：卡数 {len(GROUP_CARDS)}（对）")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    # 与字库顺序一致（字库其余对由 legacy/种子提供）
    idx = [ziku_pairs.index(p) for p in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = list(a.keys()) == ["".join(p) for p in mine]
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad = []
    for c in GROUP_CARDS:
        x, y = c["pair"]
        want_py = f"{py[x]['pinyin']} · {py[y]['pinyin']}"
        want_tone = f"{py[x]['tone']} · {py[y]['tone']}"
        if c["pinyin"] != want_py:
            bad.append((c["key"], "pinyin", c["pinyin"], want_py))
        if not (c["tone"] == want_tone or
                (c["tone"].startswith(want_tone) and c["tone"][len(want_tone):].startswith("（"))):
            bad.append((c["key"], "tone", c["tone"], want_tone))
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((c["key"], "句长", hanzi))
        for ch in c["pair"]:
            if ch not in c["sentence"]:
                bad.append((c["key"], "句缺字", ch))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((c["key"], f, len(c[f])))
    print(f"拼音/声调/文案：{'全部通过 ✓' if not bad else str(bad)}")

    svgbad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            svgbad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                svgbad.append((k, t))
        if not v.startswith("<ellipse"):
            svgbad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not svgbad else f"SVG 问题：{svgbad}")

    assert mine == expect and keys_ok and idx == sorted(idx) and not bad and not svgbad, "自检未通过"
    print("自检通过 ✓")
