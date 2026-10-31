#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画素材：对比组（duibi）。

字库对比组共 18 对，其中种子卡（大，小）（上，下）的插画已在 识字卡片_图片/，
由构建脚本并入——本模块只负责其余 16 对：
左右 前后 里外 高低 长短 多少 远近 轻重 空满 出进 胖瘦 弯直 冷热 圆方 亮暗 开关。

对比卡画法约定（与种子卡 大小.svg / 上下.svg 一致）：
- 画布 760×480，左右分半：左半中心 x≈240 对第一个字，右半中心 x≈560 对第二个字；
- 每半各自一块 ground()（rx≈148），两半主体之间留 ≥60px 间隔；
- 两个半边同色同款，只变对比维度。

自检：python3 识字卡片_素材_duibi.py
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import 识字卡片_素材库 as lib  # noqa: E402

BLUE_HI = "#a8d4ee"          # 蓝球高光（BLUE 同族浅色）
CAT, CAT_D, CAT_L = "#e8935c", "#c97a44", "#f4b58a"   # 橘猫同族色
GRAY, GRAY_D = "#a8a094", "#8f887c"                   # 石头/灯柱暖灰
CONE, CONE_D = "#e0a35e", "#c78a44"                   # 蛋筒木色同族


def hg(cx, cy=446, rx=148, ry=20):
    """对比卡半边地面。"""
    return lib.E(cx, cy, rx, ry, lib.GROUND)


def _ball_blue(cx, cy, r):
    return lib.ball(cx, cy, r, lib.BLUE, lib.BLUE_D, BLUE_HI)


def _ball_sun(cx, cy, r):
    return lib.ball(cx, cy, r, lib.SUN, lib.YEL_D, lib.SUN_L)


# ---------- 1 左右：同一只手镜像，左手拇指在右、右手拇指在左 ----------
def art_左右():
    left = f'<g transform="translate(238,324) scale(-1,1)">{lib.hand(0, 0, rot=14)}</g>'
    right = lib.hand(562, 324, rot=-14)
    return lib.wrap(hg(240, 442), hg(560, 442), left, right)


# ---------- 2 前后：同一只小鸭，面朝观者 / 背影 ----------
def _duck(cx, base=436, s=1.0, front=True):
    p = [lib.E(cx, base - 52 * s, 66 * s, 46 * s, lib.YEL)]
    p.append(lib.E(cx - 74 * s, base - 58 * s, 20 * s, 34 * s, lib.YEL_D))
    p.append(lib.E(cx + 74 * s, base - 58 * s, 20 * s, 34 * s, lib.YEL_D))
    if not front:
        p.append(lib.PG([(cx - 18 * s, base - 14 * s), (cx + 18 * s, base - 14 * s),
                         (cx, base - 46 * s)], lib.YEL_D))
    p.append(lib.R(cx - 32 * s, base - 12 * s, 26 * s, 12 * s, 6, "#e8862c"))
    p.append(lib.R(cx + 6 * s, base - 12 * s, 26 * s, 12 * s, 6, "#e8862c"))
    p.append(lib.C(cx, base - 128 * s, 40 * s, lib.YEL))
    if front:
        p.append(lib.C(cx - 14 * s, base - 134 * s, 5.5 * s, lib.INK))
        p.append(lib.C(cx + 14 * s, base - 134 * s, 5.5 * s, lib.INK))
        p.append(lib.C(cx - 12 * s, base - 136 * s, 1.8 * s, lib.WHITE))
        p.append(lib.C(cx + 16 * s, base - 136 * s, 1.8 * s, lib.WHITE))
        p.append(lib.E(cx, base - 112 * s, 15 * s, 9 * s, "#e8862c"))
        p.append(lib.C(cx - 42 * s, base - 118 * s, 8 * s, lib.PINK, 0.7))
        p.append(lib.C(cx + 42 * s, base - 118 * s, 8 * s, lib.PINK, 0.7))
    else:
        p.append(lib.C(cx, base - 168 * s, 9 * s, lib.YEL_D))
    return lib.wrap(*p)


def art_前后():
    return lib.wrap(hg(240), hg(560), _duck(240, front=True), _duck(560, front=False))


# ---------- 3 里外：同一个盒子，球在盒里探出头 / 球在盒外 ----------
def art_里外():
    box_in = lib.box(240, 332, 200, 118, open_top=True)
    ball_in = _ball_blue(238, 334, 42)
    lip = lib.R(143, 348, 194, 34, 8, lib.WOOD)
    box_out = lib.box(525, 332, 200, 118, open_top=True)
    ball_out = _ball_blue(660, 406, 42)
    return lib.wrap(hg(240), hg(560), box_in, ball_in, lip, box_out, ball_out)


# ---------- 4 高低：同样的红积木柱一高一矮，顶上各放一个同样的球 ----------
def art_高低():
    tall = lib.wrap(
        lib.R(194, 268, 92, 172, 14, lib.RED),
        lib.R(194, 330, 92, 10, 5, lib.RED_D),
        lib.R(194, 392, 92, 10, 5, lib.RED_D))
    short = lib.wrap(
        lib.R(514, 358, 92, 82, 14, lib.RED),
        lib.R(514, 390, 92, 10, 5, lib.RED_D))
    return lib.wrap(hg(240), hg(560), tall, _ball_sun(240, 238, 32),
                    short, _ball_sun(560, 328, 32))


# ---------- 5 长短：同样的青绿围巾，一条长一条短 ----------
def _scarf(x0, x1, cy, th=34):
    mid = (x0 + x1) / 2
    band = lib.P(f"M {x0} {cy} Q {mid} {cy+26} {x1} {cy} "
                 f"L {x1} {cy+th} Q {mid} {cy+th+26} {x0} {cy+th} Z", lib.TEAL)
    stripe = lib.P(f"M {x0+16} {cy+11} Q {mid} {cy+33} {x1-16} {cy+11} "
                   f"L {x1-16} {cy+21} Q {mid} {cy+43} {x0+16} {cy+21} Z", lib.TEAL_L, 0.85)
    fringe = lib.wrap(
        lib.L(x0 + 4, cy + th - 2, x0 - 4, cy + th + 20, lib.TEAL_D, 6),
        lib.L(x0 + 16, cy + th, x0 + 12, cy + th + 22, lib.TEAL_D, 6),
        lib.L(x1 - 4, cy + th - 2, x1 + 4, cy + th + 20, lib.TEAL_D, 6),
        lib.L(x1 - 16, cy + th, x1 - 12, cy + th + 22, lib.TEAL_D, 6))
    return lib.wrap(band, stripe, fringe)


def art_长短():
    return lib.wrap(hg(240, 442), hg(560, 442),
                    _scarf(96, 392, 330), _scarf(474, 646, 330))


# ---------- 6 多少：同样的蓝球，三个对一个 ----------
def art_多少():
    return lib.wrap(
        hg(240), hg(560),
        _ball_blue(198, 398, 40), _ball_blue(282, 398, 40), _ball_blue(240, 330, 40),
        _ball_blue(560, 398, 40))


# ---------- 7 远近：一条小路伸向远方，路尽头的小树小房子很远，眼前的大树很近 ----------
def art_远近():
    meadow = lib.P("M 20 252 Q 380 228 740 252 L 740 470 L 20 470 Z", "#e2f0e2")
    road = lib.P("M 402 470 C 330 396 292 322 228 260 L 246 250 C 336 316 442 388 588 470 Z", "#ead9b6")
    road_edge = lib.P("M 402 470 C 330 396 292 322 228 260 L 246 250", stroke="#dcc79a", w=5)
    far = ('<g opacity="0.88">'
           + lib.R(252, 226, 24, 18, 3, "#f2d3a0")
           + lib.PG([(247, 228), (281, 228), (264, 212)], "#e0a06a")
           + lib.R(261, 234, 7, 10, 2, "#a9743f")
           + lib.C(214, 224, 14, "#b7d3a8")
           + lib.R(211, 234, 6, 14, 2, "#c8a06a")
           + "</g>")
    near = lib.wrap(
        lib.E(614, 420, 88, 16, "#c9e2d4"),
        lib.R(601, 330, 26, 86, 9, "#a9743f"),
        lib.C(566, 306, 46, lib.GREEN),
        lib.C(664, 306, 46, lib.GREEN),
        lib.C(615, 272, 62, lib.GREEN),
        lib.C(588, 258, 26, lib.GREEN_L),
        lib.C(648, 292, 20, lib.GREEN_L, 0.8))
    return lib.wrap(meadow, road, road_edge, far, near)


# ---------- 8 轻重：同一块跷跷板，羽毛那头翘起、石头那头压下 ----------
def art_轻重():
    plank = f'<g transform="rotate(10 380 372)">{lib.R(150, 358, 460, 26, 13, lib.WOOD_L)}</g>'
    fulcrum = lib.PG([(346, 428), (414, 428), (380, 366)], lib.WOOD_D)
    feather = ('<g transform="rotate(-14 176 304)">'
               + lib.E(178, 308, 44, 14, "#cfe4f0")
               + lib.E(174, 302, 42, 13, "#eef6fa")
               + lib.L(134, 308, 218, 298, "#7fb6d9", 4)
               + "</g>")
    stone = lib.wrap(
        lib.E(594, 371, 46, 27, GRAY),
        lib.E(598, 377, 37, 19, GRAY_D))
    return lib.wrap(hg(240), hg(560), fulcrum, plank, feather, stone)


# ---------- 9 空满：同样的玻璃杯，空杯无水 / 满杯快溢 ----------
def _glass_body(cx, top, w, h):
    x0 = cx - w / 2
    body = lib.P(f"M {x0} {top} L {x0+13} {top+h-16} Q {x0+15} {top+h} {x0+32} {top+h} "
                 f"L {x0+w-32} {top+h} Q {x0+w-15} {top+h} {x0+w-13} {top+h-16} "
                 f"L {x0+w} {top} Z", "#e8f4f9", 0.75)
    return lib.wrap(lib.E(cx, top, w / 2, 14, "#cfe6f0"), body)


def art_空满():
    empty = _glass_body(240, 282, 136, 158)
    full = _glass_body(560, 282, 136, 158) + lib.cup(560, 282, 136, 158, water=0.85)
    return lib.wrap(hg(240, 442), hg(560, 442), empty, full)


# ---------- 10 出进：同一座小房子，小鸭在门外 / 小鸭进门里 ----------
def _house(cx, wall_top=268, w=190, h=162):
    x0 = cx - w / 2
    roof = lib.PG([(x0 - 16, wall_top), (x0 + w + 16, wall_top), (cx, wall_top - 78)], lib.RED)
    wall = lib.R(x0, wall_top, w, h, 12, lib.WOOD_L)
    door = lib.R(cx - 52, wall_top + 44, 104, 118, 28, "#8a5a33")
    return lib.wrap(roof, wall, door)


def art_出进():
    return lib.wrap(hg(240), hg(560),
                    _house(228), _duck(330, base=444, s=0.5, front=True),
                    _house(560), _duck(560, base=428, s=0.5, front=True))


# ---------- 11 胖瘦：同样的橘猫，一只肚圆一只身窄 ----------
def _cat(cx, bw):
    ear_l = lib.PG([(cx - 40, 262), (cx - 30, 222), (cx - 6, 246)], CAT)
    ear_r = lib.PG([(cx + 40, 262), (cx + 30, 222), (cx + 6, 246)], CAT)
    head = lib.C(cx, 292, 46, CAT)
    body = lib.E(cx, 378, bw, 60, CAT)
    tail = lib.P(f"M {cx + bw - 8} 396 Q {cx + bw + 36} 388 {cx + bw + 26} 350",
                 stroke=CAT_D, w=15)
    paws = lib.wrap(lib.E(cx - 20, 434, 16, 9, CAT_L), lib.E(cx + 20, 434, 16, 9, CAT_L))
    face = lib.wrap(
        lib.C(cx - 16, 288, 5, lib.INK), lib.C(cx + 16, 288, 5, lib.INK),
        lib.C(cx - 14, 286, 1.6, lib.WHITE), lib.C(cx + 18, 286, 1.6, lib.WHITE),
        lib.PG([(cx - 5, 302), (cx + 5, 302), (cx, 309)], CAT_D),
        lib.P(f"M {cx-10} 312 Q {cx-4} 318 {cx} 312", stroke=lib.INK, w=3),
        lib.P(f"M {cx} 312 Q {cx+4} 318 {cx+10} 312", stroke=lib.INK, w=3),
        lib.L(cx - 58, 298, cx - 30, 294, lib.INK, 3),
        lib.L(cx - 58, 308, cx - 30, 304, lib.INK, 3),
        lib.L(cx + 58, 298, cx + 30, 294, lib.INK, 3),
        lib.L(cx + 58, 308, cx + 30, 304, lib.INK, 3),
        lib.C(cx - 38, 308, 8, lib.PINK, 0.7), lib.C(cx + 38, 308, 8, lib.PINK, 0.7))
    return lib.wrap(ear_l, ear_r, head, body, tail, paws, face)


def art_胖瘦():
    return lib.wrap(hg(240), hg(560), _cat(240, 84), _cat(560, 50))


# ---------- 12 弯直：弯弯的香蕉 / 笔直的尺子 ----------
def art_弯直():
    # 同一根条纹吸管：左边掰成大弯，右边笔直
    bend = lib.wrap(
        lib.P("M 240 438 L 240 300 A 45 45 0 0 1 330 300", stroke="#f2913f", w=30),
        lib.R(225, 402, 30, 14, 6, "#ffffff", 0.85),
        lib.R(225, 362, 30, 14, 6, "#ffffff", 0.85),
        lib.R(225, 322, 30, 14, 6, "#ffffff", 0.85),
        f'<circle cx="330" cy="300" r="8" fill="#c96a2e"/>',
        lib.E(240, 436, 15, 5, "#c96a2e"))
    straight = lib.wrap(
        lib.P("M 560 438 L 560 258", stroke="#f2913f", w=30),
        lib.R(545, 402, 30, 14, 6, "#ffffff", 0.85),
        lib.R(545, 362, 30, 14, 6, "#ffffff", 0.85),
        lib.R(545, 322, 30, 14, 6, "#ffffff", 0.85),
        lib.R(545, 282, 30, 14, 6, "#ffffff", 0.85),
        lib.E(560, 436, 15, 5, "#c96a2e"))
    return lib.wrap(hg(240, 442), hg(560, 442), bend, straight)


# ---------- 13 冷热：同一支冰淇淋，旁边飘雪花是冷 / 太阳晒化是热 ----------
def _icecream(cx, base=436):
    cone = lib.PG([(cx - 40, base - 96), (cx + 40, base - 96), (cx, base)], CONE)
    lines = lib.wrap(lib.L(cx - 26, base - 62, cx + 26, base - 62, CONE_D, 5),
                     lib.L(cx - 15, base - 32, cx + 15, base - 32, CONE_D, 5))
    cream = lib.wrap(
        lib.C(cx, base - 104, 34, lib.PINK),
        lib.C(cx - 24, base - 128, 26, lib.PINK), lib.C(cx + 24, base - 128, 26, lib.PINK),
        lib.C(cx, base - 152, 22, lib.PINK))
    return lib.wrap(cone, lines, cream)


def art_冷热():
    # 左：冬天——雪地、雪花、穿棉袄戴帽子围巾的小朋友
    cold = lib.wrap(
        hg(240),
        lib.E(240, 444, 152, 21, "#ffffff", 0.9),
        # 裹成圆滚滚厚棉袄的小朋友（自绘：蓬蓬棉袄+棉线缝纹+厚手套+毛线帽+厚围巾）
        lib.P("M 172 306 Q 162 298 174 292 L 306 292 Q 318 298 308 306 L 318 400 Q 240 420 162 400 Z", "#9cc9e2"),
        lib.L(174, 344, 306, 344, "#7ba9c9", 5),
        lib.L(174, 374, 306, 374, "#7ba9c9", 5),
        lib.L(206, 344, 206, 374, "#7ba9c9", 5), lib.L(274, 344, 274, 374, "#7ba9c9", 5), lib.L(240, 344, 240, 374, "#7ba9c9", 5),
        lib.P("M 176 310 Q 140 328 132 370", stroke="#9cc9e2", w=28),
        lib.C(130, 378, 16, "#c96a4a"),
        lib.P("M 304 310 Q 340 328 348 370", stroke="#9cc9e2", w=28),
        lib.C(350, 378, 16, "#c96a4a"),
        lib.R(198, 402, 34, 28, 10, "#c96a4a"), lib.R(248, 402, 34, 28, 10, "#c96a4a"),
        lib.E(215, 430, 22, 7, "#3a2418", 0.8), lib.E(265, 430, 22, 7, "#3a2418", 0.8),
        lib.C(240, 232, 58, "#f7c49c"),
        lib.C(220, 228, 6, "#3a2418"), lib.C(260, 228, 6, "#3a2418"),
        lib.C(204, 248, 10, "#f5a58c"), lib.C(276, 248, 10, "#f5a58c"),
        lib.E(240, 262, 10, 13, "#6b3325"),
        lib.P("M 182 202 A 58 58 0 0 1 298 202 Z", "#d9734f"),
        lib.R(176, 194, 128, 20, 10, "#e08a6a"),
        lib.C(240, 134, 11, "#fdfdfa"),
        lib.R(200, 282, 80, 26, 12, "#c96a4a"),
        lib.R(258, 294, 22, 44, 9, "#c96a4a"),
        lib.P("M 158 212 q 8 -12 0 -24 q -8 -12 0 -24", stroke="#a8d4f0", w=5),
        lib.P("M 322 212 q -8 -12 0 -24 q 8 -12 0 -24", stroke="#a8d4f0", w=5),
        lib.L(140, 140, 160, 140, "#a8d4f0", 4), lib.L(143, 133, 157, 147, "#a8d4f0", 4), lib.L(143, 147, 157, 133, "#a8d4f0", 4),
        lib.L(296, 96, 316, 96, "#a8d4f0", 4), lib.L(299, 89, 313, 103, "#a8d4f0", 4), lib.L(299, 103, 313, 89, "#a8d4f0", 4),
        lib.L(330, 200, 350, 200, "#a8d4f0", 4), lib.L(333, 193, 347, 207, "#a8d4f0", 4), lib.L(333, 207, 347, 193, "#a8d4f0", 4))
    # 右：夏天——大太阳、短袖小朋友摇扇子擦汗
    hot = lib.wrap(
        hg(560),
        lib.C(668, 110, 36, lib.SUN),
        lib.L(714, 110, 730, 110, "#f2a72e", 6), lib.L(700, 143, 712, 154, "#f2a72e", 6),
        lib.L(668, 156, 668, 172, "#f2a72e", 6), lib.L(636, 143, 624, 154, "#f2a72e", 6),
        lib.L(622, 110, 606, 110, "#f2a72e", 6), lib.L(636, 77, 624, 66, "#f2a72e", 6),
        lib.L(668, 64, 668, 48, "#f2a72e", 6), lib.L(700, 77, 712, 66, "#f2a72e", 6),
        lib.kid(560, 436, 0.92, face="smile", shirt=lib.RED),
        lib.drop(522, 196, 9, lib.WBLUE), lib.drop(598, 192, 8, lib.WBLUE),
        lib.P("M 536 172 q 9 -16 0 -32 q -9 -16 0 -32", stroke="#f2a72e", w=5),
        lib.P("M 578 156 q 9 -15 0 -30", stroke="#f2a72e", w=5),
        lib.L(619, 352, 616, 314, "#a9743f", 7),
        lib.C(614, 284, 34, "#f7e7c9"),
        '<circle cx="614" cy="284" r="34" fill="none" stroke="#d9b98a" stroke-width="5"/>',
        lib.L(614, 284, 586, 272, "#d9b98a", 4), lib.L(614, 284, 642, 272, "#d9b98a", 4),
        lib.L(614, 284, 614, 252, "#d9b98a", 4))
    return lib.wrap(cold, hot)


# ---------- 14 圆方：同样绿色的圆球 / 方积木 ----------
def art_圆方():
    ball = lib.ball(240, 378, 62, lib.GREEN, "#6a955c", lib.GREEN_L)
    cube = lib.wrap(
        lib.PG([(496, 338), (522, 314), (626, 314), (600, 338)], lib.GREEN_L),
        lib.PG([(600, 338), (626, 314), (626, 414), (600, 438)], "#6a955c"),
        lib.R(496, 338, 104, 100, 12, lib.GREEN))
    return lib.wrap(hg(240), hg(560), ball, cube)


# ---------- 15 亮暗：同一盏台灯，亮的有光晕 / 熄的灯泡发灰 ----------
def _lamp(cx, on=True):
    p = []
    if on:
        p.append(lib.C(cx, 330, 96, lib.SUN, 0.30))
        p.append(lib.C(cx, 330, 62, lib.SUN, 0.35))
    p.append(lib.C(cx, 326, 17, lib.SUN_L if on else "#c9c2b4"))
    p.append(lib.R(cx - 6, 316, 12, 88, 6, GRAY))
    p.append(lib.E(cx, 412, 54, 14, GRAY))
    p.append(lib.PG([(cx - 46, 246), (cx + 46, 246), (cx + 76, 316), (cx - 76, 316)], lib.BLUE))
    if on:
        p.append(lib.E(cx, 438, 84, 11, lib.SUN_L, 0.55))
    return lib.wrap(*p)


def art_亮暗():
    return lib.wrap(hg(240), hg(560), _lamp(240, on=True), _lamp(560, on=False))


# ---------- 16 开关：同一个青色玩具箱，掀盖是开 / 合盖是关 ----------
def _chest_lid(cx, cy, rot=0):
    lid = (f'<g transform="rotate({rot} {cx} {cy})">'
           + lib.R(cx - 90, cy - 20, 180, 40, 14, lib.TEAL_L)
           + lib.C(cx, cy - 28, 13, lib.SUN) + "</g>")
    return lid


def art_开关():
    # 开：盖子向后翻开立起，下缘没入盒口（与盒身相连），微倾；关：盖子合在盒上
    lid_open = ('<g transform="rotate(-8 240 362)">'
                + lib.R(170, 262, 140, 110, 14, lib.TEAL_L)
                + lib.C(240, 256, 13, lib.SUN) + "</g>")
    body_open = lib.wrap(
        lib.R(150, 356, 180, 92, 16, lib.TEAL),
        lib.R(162, 356, 156, 24, 10, lib.TEAL_D))
    body_closed = lib.R(470, 356, 180, 92, 16, lib.TEAL)
    return lib.wrap(hg(240), hg(560),
                    lid_open, body_open,
                    _chest_lid(560, 342, rot=0), body_closed)


# ---------- 组装 ----------
def arts():
    keys = ["左右", "前后", "里外", "高低", "长短", "多少", "远近", "轻重",
            "空满", "出进", "胖瘦", "弯直", "冷热", "圆方", "亮暗", "开关"]
    return {k: globals()[f"art_{k}"]() for k in keys}


# 组卡片文案数据（种子对 大小/上下 由构建脚本提供，不在这里）
GROUP_CARDS = [
    {"pair": ["左", "右"], "key": "左右", "pinyin": "zuǒ · yòu", "tone": "第三声 · 第四声",
     "sentence": "左手右手，拍拍手。",
     "say": "把手举起来跟图对照：大拇指朝这边的是左手，另一只是右手。",
     "chat": "“你用哪只手拿勺子？举给我看看。”",
     "life": "走路时喊“左脚、右脚”，踩着节奏迈步。"},
    {"pair": ["前", "后"], "key": "前后", "pinyin": "qián · hòu", "tone": "第二声 · 第四声",
     "sentence": "一只朝前，一只朝后。",
     "say": "脸朝我们的是前，看到背影的是后。",
     "chat": "“排队的时候，谁在你前面？谁在你后面？”",
     "life": "让他站到你前面，再绕到你后面，来回说。"},
    {"pair": ["里", "外"], "key": "里外", "pinyin": "lǐ · wài", "tone": "第三声 · 第四声",
     "sentence": "球在盒里，球在盒外。",
     "say": "球待在盒子里面是里，跑到盒子旁边是外。",
     "chat": "“玩具玩完了，要放进箱子里面还是外面？”",
     "life": "把球扔进箱子再拿出来，边做边说里、外。"},
    {"pair": ["高", "低"], "key": "高低", "pinyin": "gāo · dī", "tone": "第一声 · 第一声",
     "sentence": "积木高，积木低。",
     "say": "柱子搭得高就离天空近，搭得低就挨着地面。",
     "chat": "“哪根柱子高？我们再搭一根更高的好不好？”",
     "life": "两人举手比一比，谁举得高、谁放得低。"},
    {"pair": ["长", "短"], "key": "长短", "pinyin": "cháng · duǎn", "tone": "第二声 · 第三声（长另读 zhǎng，长大的长）",
     "sentence": "长围巾，短围巾。",
     "say": "两条围巾比一比，拖得长的是长，短的是短。",
     "chat": "“你的围巾和我的比一比，哪条长？”",
     "life": "拿两根绳子并排摆好，让他指出长的和短的。"},
    {"pair": ["多", "少"], "key": "多少", "pinyin": "duō · shǎo", "tone": "第一声 · 第三声",
     "sentence": "这边球多，那边球少。",
     "say": "三个球是多，一个球是少，摆在一起看就知道。",
     "chat": "“你碗里饭多还是少？吃完了会变成什么样？”",
     "life": "分饼干时问他：要多的一点还是少的一点？"},
    {"pair": ["远", "近"], "key": "远近", "pinyin": "yuǎn · jìn", "tone": "第三声 · 第四声",
     "sentence": "那棵远，这棵近。",
     "say": "顺着小路望：尽头的小房子很远，眼前的大树很近。",
     "chat": "“哪棵树远，哪棵树近？”",
     "life": "散步时找一找：远处的东西看起来小小的。"},
    {"pair": ["轻", "重"], "key": "轻重", "pinyin": "qīng · zhòng", "tone": "第一声 · 第四声",
     "sentence": "羽毛轻，石头重。",
     "say": "羽毛这头翘起来了，石头那头把板压了下去。",
     "chat": "“抱一抱枕子和书，哪个重哪个轻？”",
     "life": "用尺子当跷跷板，两头放橡皮和豆袋比轻重。"},
    {"pair": ["空", "满"], "key": "空满", "pinyin": "kōng · mǎn", "tone": "第一声 · 第三声",
     "sentence": "空杯倒水，倒到满。",
     "say": "一点水都没有是空，水装到快满出来就是满。",
     "chat": "“洗澡的时候，浴缸里是空的还是满的？”",
     "life": "用水杯接水，看着水从空到满，满了喊停。"},
    {"pair": ["出", "进"], "key": "出进", "pinyin": "chū · jìn", "tone": "第一声 · 第四声",
     "sentence": "小鸭出门，小鸭进门。",
     "say": "从家里走出去是出，走回屋里来是进。",
     "chat": "“我们出门的时候，是谁先跨出门的呀？”",
     "life": "进出房门时说一说：出门啦、进门啦。"},
    {"pair": ["胖", "瘦"], "key": "胖瘦", "pinyin": "pàng · shòu", "tone": "第四声 · 第四声",
     "sentence": "胖猫胖，瘦猫瘦。",
     "say": "肚子圆鼓鼓的是胖猫，身子窄窄的是瘦猫。",
     "chat": "“咱们家里谁胖一点？谁瘦一点？”",
     "life": "捏捏自己的胳膊，再比比爸爸是胖还是瘦。"},
    {"pair": ["弯", "直"], "key": "弯直", "pinyin": "wān · zhí", "tone": "第一声 · 第二声",
     "sentence": "吸管弯弯，吸管直直。",
     "say": "同一根吸管：左边掰弯了，右边是直的。",
     "chat": "“哪根吸管弯，哪根吸管直？”",
     "life": "拿一根吸管轻轻掰弯再松开，说说弯和直。"},
    {"pair": ["冷", "热"], "key": "冷热", "pinyin": "lěng · rè", "tone": "第三声 · 第四声",
     "sentence": "冬天冷，夏天热。",
     "say": "冬天穿棉袄戴帽子还是冷；夏天摇着扇子还出汗，热。",
     "chat": "“冬天和夏天，哪个冷哪个热？你现在觉得冷还是热？”",
     "life": "翻一翻冬装和夏装：厚的冷天穿，薄的热天穿。"},
    {"pair": ["圆", "方"], "key": "圆方", "pinyin": "yuán · fāng", "tone": "第二声 · 第一声",
     "sentence": "球是圆的，积木是方的。",
     "say": "球可以滚来滚去是圆的，积木稳稳站住是方的。",
     "chat": "“家里哪些东西圆圆的？哪些东西方方的？”",
     "life": "找一块圆饼干和一块方饼干，摆在一起认。"},
    {"pair": ["亮", "暗"], "key": "亮暗", "pinyin": "liàng · àn", "tone": "第四声 · 第四声",
     "sentence": "开灯真亮，关灯好暗。",
     "say": "灯亮着有光，什么都能看清；灯灭了屋里就是暗的。",
     "chat": "“晚上睡觉的时候，房间亮一点还是暗一点好？”",
     "life": "玩开关灯的游戏：说亮了、暗了，再钻进被窝。"},
    {"pair": ["开", "关"], "key": "开关", "pinyin": "kāi · guān", "tone": "第一声 · 第一声",
     "sentence": "打开盒盖，关上盒盖。",
     "say": "盖子掀起来是开，盖回去合上就是关。",
     "chat": "“冰箱门是开着的还是关着的？为什么要关上？”",
     "life": "让他自己开盒拿零食，吃完记得提醒关好。"},
]


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import 识字卡片_字库 as ZIKU

    grp = next(g for g in ZIKU.GROUPS if g["id"] == "duibi")
    ziku_pairs = [tuple(k) for k in grp["chars"] if isinstance(k, (tuple, list))]
    seeds = {("小", "大"), ("上", "下")}
    expect = [p for p in ziku_pairs if p not in seeds]
    mine = [tuple(c["pair"]) for c in GROUP_CARDS]
    print(f"卡数：{len(GROUP_CARDS)}（字库对比组 {len(ziku_pairs)} 对，扣除种子 大小/上下）")
    assert mine == expect, f"与字库顺序/内容不一致：\n字库={expect}\n本模块={mine}"
    a = arts()
    print(f"arts 数：{len(a)}")
    assert list(a.keys()) == ["".join(p) for p in mine], f"arts key 不匹配：{list(a.keys())}"
    for c in GROUP_CARDS:
        assert c["key"] == "".join(c["pair"]) and " · " in c["pinyin"], c["key"]
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        assert 4 <= hanzi <= 10, (c["key"], c["sentence"])
        for f in ("say", "chat", "life"):
            assert len(c[f]) <= 30, (c["key"], f, len(c[f]))
    for k, v in a.items():
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            assert bad not in v, (k, bad)
    print("与字库比对一致 ✓  文案字段检查通过 ✓  SVG 全部合法 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'pair': ['正', '反'], 'key': '正反', 'pinyin': 'zhèng · fǎn', 'tone': '第四声 · 第三声', 'sentence': '正面笑，反面看不见。', 'say': '看到笑脸是正面，转到背后是反面。', 'chat': '“手心手背，哪面算正面？”', 'life': '翻翻卡片，认一认正反两面。'},
    {'pair': ['男', '女'], 'key': '男女', 'pinyin': 'nán · nǚ', 'tone': '第二声 · 第三声', 'sentence': '男孩女孩排排站。', 'say': '短发蓝衣是男孩，裙装长发是女孩。', 'chat': '“咱们家谁是男孩，谁是女孩？”', 'life': '说说幼儿园里男孩女孩的名字。'},
]
_arts_mig = {
    '正反': '<ellipse cx="240" cy="446" rx="148" ry="20" fill="#c8e6d8"/><ellipse cx="560" cy="446" rx="148" ry="20" fill="#c8e6d8"/><rect x="212.4" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="243.68" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="224.36" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="255.64" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 188.48 289.44 Q 186.64 361.2 203.2 363.04 L 276.8 363.04 Q 293.36 361.2 291.52 289.44 Q 240 274.71999999999997 188.48 289.44 Z" fill="#5fa8d8"/><line x1="199.51999999999998" y1="294.96" x2="181.12" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="181.12" cy="361.2" r="11.96" fill="#f8cba4"/><line x1="280.48" y1="294.96" x2="298.88" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="298.88" cy="361.2" r="11.96" fill="#f8cba4"/><circle cx="186.64" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="293.36" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="240" cy="225.04" r="57.04" fill="#f8cba4"/><path d="M 184.1008 205.076 Q 188.664 157.7328 240 161.1552 Q 291.336 157.7328 295.8992 205.076 Q 271.372 195.3792 240 201.0832 Q 208.628 195.3792 184.1008 205.076 Z" fill="#5a3d2b"/><ellipse cx="219.76" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="219.76" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="260.24" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="260.24" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 206.88 195.3792 Q 219.76 189.6752 232.64 194.23839999999998" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 247.36 194.23839999999998 Q 260.24 189.6752 273.12 195.3792" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 221.6 248.95999999999998 Q 240 263.68 258.4 248.95999999999998" fill="none" stroke="#4a3226" stroke-width="6.44" stroke-linecap="round" stroke-linejoin="round"/><circle cx="199.51999999999998" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="280.48" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><rect x="532.4" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="563.68" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="544.36" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="575.64" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 508.48 289.44 Q 506.64 361.2 523.2 363.04 L 596.8 363.04 Q 613.36 361.2 611.52 289.44 Q 560 274.71999999999997 508.48 289.44 Z" fill="#5fa8d8"/><line x1="519.52" y1="294.96" x2="501.12" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="501.12" cy="361.2" r="11.96" fill="#f8cba4"/><line x1="600.48" y1="294.96" x2="618.88" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="618.88" cy="361.2" r="11.96" fill="#f8cba4"/><circle cx="506.64" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="613.36" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="560" cy="225.04" r="57.04" fill="#f8cba4"/><path d="M 504.1008 205.076 Q 508.664 157.7328 560 161.1552 Q 611.336 157.7328 615.8992 205.076 Q 591.372 195.3792 560 201.0832 Q 528.628 195.3792 504.1008 205.076 Z" fill="#5a3d2b"/><ellipse cx="539.76" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="539.76" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="580.24" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="580.24" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 526.88 195.3792 Q 539.76 189.6752 552.64 194.23839999999998" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 567.36 194.23839999999998 Q 580.24 189.6752 593.12 195.3792" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 541.6 248.95999999999998 Q 560 263.68 578.4 248.95999999999998" fill="none" stroke="#4a3226" stroke-width="6.44" stroke-linecap="round" stroke-linejoin="round"/><circle cx="519.52" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="600.48" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="560" cy="223.3288" r="60.4624" fill="#5a3d2b"/><path d="M 534 199 Q 560 190 586 199" fill="none" stroke="#7a5840" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><circle cx="507.5232" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="612.4768" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/>',
    '男女': '<ellipse cx="240" cy="446" rx="148" ry="20" fill="#c8e6d8"/><ellipse cx="560" cy="446" rx="148" ry="20" fill="#c8e6d8"/><rect x="212.4" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="243.68" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="224.36" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="255.64" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 188.48 289.44 Q 186.64 361.2 203.2 363.04 L 276.8 363.04 Q 293.36 361.2 291.52 289.44 Q 240 274.71999999999997 188.48 289.44 Z" fill="#5fa8d8"/><line x1="199.51999999999998" y1="294.96" x2="181.12" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="181.12" cy="361.2" r="11.96" fill="#f8cba4"/><line x1="280.48" y1="294.96" x2="298.88" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="298.88" cy="361.2" r="11.96" fill="#f8cba4"/><circle cx="186.64" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="293.36" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="240" cy="225.04" r="57.04" fill="#f8cba4"/><path d="M 184.1008 205.076 Q 188.664 157.7328 240 161.1552 Q 291.336 157.7328 295.8992 205.076 Q 271.372 195.3792 240 201.0832 Q 208.628 195.3792 184.1008 205.076 Z" fill="#5a3d2b"/><ellipse cx="219.76" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="219.76" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="260.24" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="260.24" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 206.88 195.3792 Q 219.76 189.6752 232.64 194.23839999999998" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 247.36 194.23839999999998 Q 260.24 189.6752 273.12 195.3792" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 216.07999999999998 248.95999999999998 Q 240 239.76 263.92 248.95999999999998 Q 262.08 272.88 240 276.56 Q 217.92 272.88 216.07999999999998 248.95999999999998 Z" fill="#6b3325"/><path d="M 227.12 263.68 Q 240 256.32 252.88 263.68 Q 248.28 273.79999999999995 240 274.71999999999997 Q 231.72 273.79999999999995 227.12 263.68 Z" fill="#f0876f"/><circle cx="199.51999999999998" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="280.48" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><path d="M 489 227 Q 486 161 560 159 Q 634 161 631 227 L 624 350 Q 618 363 604 356 L 516 356 Q 502 363 496 350 Z" fill="#5a3d2b"/><rect x="532.4" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="563.68" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="544.36" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="575.64" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 508.48 289.44 Q 506.64 361.2 523.2 363.04 L 596.8 363.04 Q 613.36 361.2 611.52 289.44 Q 560 274.71999999999997 508.48 289.44 Z" fill="#f2b53c"/><line x1="519.52" y1="294.96" x2="501.12" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="501.12" cy="361.2" r="11.96" fill="#f8cba4"/><line x1="600.48" y1="294.96" x2="618.88" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="618.88" cy="361.2" r="11.96" fill="#f8cba4"/><circle cx="506.64" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="613.36" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="560" cy="225.04" r="57.04" fill="#f8cba4"/><path d="M 504.1008 205.076 Q 508.664 157.7328 560 161.1552 Q 611.336 157.7328 615.8992 205.076 Q 591.372 195.3792 560 201.0832 Q 528.628 195.3792 504.1008 205.076 Z" fill="#5a3d2b"/><ellipse cx="539.76" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="539.76" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="580.24" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="580.24" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 526.88 195.3792 Q 539.76 189.6752 552.64 194.23839999999998" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 567.36 194.23839999999998 Q 580.24 189.6752 593.12 195.3792" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 541.6 248.95999999999998 Q 560 263.68 578.4 248.95999999999998" fill="none" stroke="#4a3226" stroke-width="6.44" stroke-linecap="round" stroke-linejoin="round"/><circle cx="519.52" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="600.48" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><polygon points="536.08,148.64 556.32,143.12 556.32,157.84" fill="#e8663c"/><polygon points="583.92,148.64 563.68,143.12 563.68,157.84" fill="#e8663c"/><circle cx="560" cy="156" r="5.5200000000000005" fill="#d4552f"/><path d="M 512 334 L 608 334 L 621 396 L 499 396 Z" fill="#f5a58c"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
