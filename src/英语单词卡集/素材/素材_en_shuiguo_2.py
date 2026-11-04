#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 水果（shuiguo）第 2 段插画（10 卡：cherry~plum）。

每卡造型要点：cherry 深红双果并蒂长梗分叉 / coconut 棕壳大圆果三孔，
开口处露白肉与椰汁并挂一滴 / kiwi 大切面居中，毛皮棕圈+绿心白核黑籽环，
右下辅一整只毛果 / lychee 红壳鳞凸粗纹一颗，右下一颗剥壳露白肉 /
persimmon 橙红扁圆四瓣中缝，顶戴四出绿萼短柄 / pomegranate 黄褐壳顶戴皇冠，
右上裂口露红籽堆并散两粒 / durian 黄绿刺壳刺密圆钝，中右开缝露黄肉棕核 /
starfruit 浅黄绿大横切居中，五角星轮廓清楚，右下辅一条棱整果 /
avocado 深绿皮切半居中露黄绿果肉与棕大核，右下辅一整只 / plum 紫李带果粉中缝单叶。
整果居中放大，切口/剥口按前段惯例作辅角；主色相邻错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "cherry", "cn": "樱桃"},
    {"w": "coconut", "cn": "椰子"},
    {"w": "kiwi", "cn": "猕猴桃"},
    {"w": "lychee", "cn": "荔枝"},
    {"w": "persimmon", "cn": "柿子"},
    {"w": "pomegranate", "cn": "石榴"},
    {"w": "durian", "cn": "榴莲"},
    {"w": "starfruit", "cn": "杨桃"},
    {"w": "avocado", "cn": "牛油果"},
    {"w": "plum", "cn": "李子"},
]


# ---------- 本组同族补充色 ----------
STEMG = "#5d8a52"                                               # 绿族深（果柄/叶脉/萼）
CHERRY, CHERRY_D, CHERRY_L = "#cf4444", "#ad2e2e", "#ef9a9a"    # 樱桃深红（RED 族）
COCO, COCO_D, COCO_L = "#8f5f38", "#77492a", "#b98a5e"          # 椰壳棕（WOOD 族深）
KIWIB, KIWIB_D = "#a8825a", "#8a6842"                           # 猕猴桃毛皮棕（WOOD 族浅/深）
KIWIFUZZ = "#c9a878"                                            # 茸毛浅棕
LYC, LYC_D, LYC_L = "#d94f43", "#b83a30", "#f2968a"             # 荔枝红壳（RED 族）
PER, PER_D, PER_L = "#e8862e", "#cc6f1d", "#f6ab63"             # 柿橙（SUN/YEL 族）
POME, POME_D, POME_L = "#c68f4c", "#a87438", "#e0b078"          # 石榴壳黄褐（WOOD 族）
POMOPI = "#6e4322"                                              # 壳内深腔
SEEDR = "#e2574a"                                               # 籽红（RED 族变体）
DUR, DUR_D = "#c2b34e", "#a3943a"                               # 榴莲黄绿（YEL×GREEN 族）
DURF = "#f8d582"                                                # 榴莲肉（YEL 族浅）
STARKIN, STAREDGE = "#5d8a52", "#7ba86d"                        # 杨桃皮绿（GREEN 族）
STARF, STARTINT, STARCORE = "#eef2ae", "#f6f8cc", "#fbf9de"     # 杨桃果肉浅黄绿
AVD, AVD_D = "#4a6b3a", "#3a5530"                               # 牛油果皮深绿（GREEN 族深）
AVF = "#cdd68b"                                                 # 果肉黄绿
PIT, PIT_L = "#8a5a33", "#b98a5e"                               # 果核棕（WOOD 族深）
PLUM, PLUM_D = "#7e55a0", "#654387"                             # 李紫（GRAPE 族深）
PLUM_BLOOM = "#e6dbf2"                                          # 果粉白（紫族浅）


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


# ---------- 12 cherry 深红双果并蒂长梗 ----------
def art_cherry():
    g = ground()
    # 长梗从同一蒂点分叉
    g += P("M 392 124 Q 352 182 316 250", stroke=WOOD_D, w=11)
    g += P("M 392 124 Q 438 196 466 256", stroke=WOOD_D, w=11)
    g += C(392, 120, 10, WOOD_D)
    g += leaf(448, 138, 44, 17, 30)
    # 左果（大）
    g += C(316, 352, 100, CHERRY_D)
    g += C(310, 344, 98, CHERRY)
    g += E(314, 250, 13, 6.5, CHERRY_D)                    # 梗窝
    g += shine(262, 296, 30, 46, CHERRY_L, 0.75, -24)
    # 右果（略小低）
    g += C(472, 356, 96, CHERRY_D)
    g += C(466, 350, 94, CHERRY)
    g += E(470, 260, 12, 6, CHERRY_D)
    g += shine(424, 308, 26, 42, CHERRY_L, 0.7, -24)
    return g


# ---------- 13 coconut 棕壳三孔开口露汁 ----------
def art_coconut():
    g = ground()
    g += C(358, 304, 142, COCO_D)
    g += C(350, 296, 140, COCO)
    g += shine(284, 232, 38, 56, COCO_L, 0.55, -22)
    # 壳面纤维弧纹
    g += P("M 240 352 Q 348 416 458 348", stroke=COCO_D, w=7, opacity=0.45)
    g += P("M 262 384 Q 352 438 448 380", stroke=COCO_D, w=6, opacity=0.35)
    # 三孔区（开口最大，微倾）
    g += '<g transform="rotate(-16 430 214)">'
    g += E(430, 214, 36, 27, COCO_D)                       # 开口外圈
    g += E(430, 214, 29, 21, "#5d3a1e")                    # 洞
    g += E(430, 214, 22, 15, "#f7ecd8")                    # 白肉环
    g += E(430, 214, 14, 9, WBLUE)                         # 椰汁
    g += E(427, 211, 7, 4.5, "#a5dcf0", 0.9)               # 汁面高光
    g += E(394, 190, 7, 10, "#4e2f18")                     # 孔一
    g += E(472, 240, 7, 10, "#4e2f18")                     # 孔二
    g += "</g>"
    # 开口下挂一滴汁
    g += P("M 474 262 Q 485 279 474 290 Q 463 279 474 262 Z", WBLUE)
    g += C(472, 270, 3, "#a5dcf0", 0.9)
    return g


# ---------- 14 kiwi 毛皮棕外圈 + 切面绿心黑籽 ----------
def _kiwi_seeds(cx, cy, rr):
    import math
    g = ""
    for i in range(14):
        a = i * 360 / 14
        g += (f'<g transform="rotate({a:.0f} {cx} {cy})">'
              + E(cx, cy - rr, 4.5, 8, INK) + "</g>")
    return g


def _kiwi_rays(cx, cy, r0, r1):
    import math
    g = '<g opacity="0.55">'
    for i in range(11):
        a = math.radians(i * 360 / 11)
        g += L(round(cx + r0 * math.cos(a), 1), round(cy + r0 * math.sin(a), 1),
               round(cx + r1 * math.cos(a), 1), round(cy + r1 * math.sin(a), 1),
               "#f5f0d5", 5)
    return g + "</g>"


def art_kiwi():
    g = ground()
    # 大切面（主）：毛皮 → 浅皮里 → 绿肉 → 浅心 → 白核 → 放射纹 → 黑籽环
    g += C(352, 296, 150, KIWIB)
    g += C(352, 296, 142, KIWIFUZZ)
    g += C(352, 296, 135, GREEN)
    g += C(352, 296, 112, GREEN_L)
    g += _kiwi_rays(352, 296, 42, 104)
    g += E(352, 296, 46, 42, "#f5f0d5")
    g += _kiwi_seeds(352, 296, 78)
    # 皮圈高光 + 茸毛点
    g += shine(252, 196, 26, 13, KIWIFUZZ, 0.75, -32)
    import math
    for i in range(12):
        a = math.radians(-160 + i * 13)
        g += C(round(352 + 145 * math.cos(a), 1), round(296 + 145 * math.sin(a), 1), 2.4, KIWIFUZZ)
    # 辅：右下一整只毛果
    g += E(612, 392, 78, 55, KIWIB_D)
    g += E(604, 384, 76, 53, KIWIB)
    for dx, dy in ((560, 358), (586, 344), (628, 342), (660, 366), (664, 398), (566, 404), (596, 428), (636, 426)):
        g += C(dx, dy, 2.4, KIWIFUZZ)
    return g


# ---------- 15 lychee 红壳粗纹一颗 + 剥开露白 ----------
def _scale(x, y, s, op):
    """壳面鳞凸（小梭形）。"""
    return P(f"M {x - 10 * s} {y} Q {x} {y - 13 * s} {x + 10 * s} {y} Q {x} {y + 5 * s} {x - 10 * s} {y} Z",
             LYC_D, opacity=op)


def art_lychee():
    g = ground()
    # 整果（主）
    g += C(332, 312, 138, LYC_D)
    g += C(324, 304, 136, LYC)
    g += shine(268, 248, 34, 50, LYC_L, 0.7, -24)
    # 粗鳞纹
    for sx, sy, s in ((262, 260, 1.0), (328, 236, 1.15), (392, 262, 1.0),
                      (240, 316, 1.1), (300, 298, 0.9), (366, 304, 1.2),
                      (422, 318, 0.95), (266, 362, 1.05), (330, 350, 0.95),
                      (394, 366, 1.1), (302, 402, 1.0), (364, 412, 0.9), (426, 360, 0.85)):
        g += _scale(sx, sy, s, 0.5)
    g += C(284, 330, 3.5, LYC_D) + C(354, 384, 3.5, LYC_D) + C(410, 292, 3.5, LYC_D)
    # 短柄 + 小叶
    g += R(318, 152, 14, 34, 7, "#8a5a33")
    g += leaf(378, 146, 40, 16, 28)
    # 剥开的一颗（辅）：红壳裙 + 白肉珠
    g += PG([(534, 392), (556, 368), (572, 390), (592, 362), (612, 388),
             (634, 366), (652, 390), (662, 414), (640, 430), (560, 432), (536, 414)], LYC_D)
    g += C(596, 378, 52, "#fdf3ea")
    g += E(600, 388, 40, 34, "#f0dcc8", 0.5)
    g += C(578, 360, 12, WHITE, 0.85)
    return g


# ---------- 16 persimmon 橙红四瓣 + 绿萼 ----------
def art_persimmon():
    g = ground()
    g += E(376, 320, 158, 122, PER_D)
    g += E(368, 310, 156, 122, PER)
    # 四瓣中缝
    g += P("M 322 200 Q 312 312 322 426", stroke=PER_D, w=6, opacity=0.6)
    g += P("M 414 198 Q 424 312 414 424", stroke=PER_D, w=6, opacity=0.6)
    g += shine(296, 258, 38, 54, PER_L, 0.75, -22)
    # 顶萼四出 + 短柄
    for a, col in ((-135, GREEN), (-45, STEMG), (45, GREEN), (135, STEMG)):
        g += f'<g transform="rotate({a} 372 206)">' + E(372, 172, 17, 42, col) + "</g>"
    g += C(372, 208, 14, STEMG)
    g += R(366, 152, 13, 36, 6, WOOD_D)
    return g


# ---------- 17 pomegranate 壳黄褐裂口露红籽堆 ----------
def art_pomegranate():
    g = ground()
    g += E(366, 316, 146, 132, POME_D)
    g += E(358, 308, 144, 130, POME)
    g += shine(282, 250, 34, 52, POME_L, 0.6, -22)
    # 顶冠
    g += PG([(322, 196), (312, 148), (342, 190)], POME_D)
    g += PG([(344, 190), (348, 138), (368, 188)], POME)
    g += PG([(370, 188), (388, 142), (390, 192)], POME_D)
    g += PG([(392, 196), (424, 158), (408, 204)], POME)
    # 右上裂口：翻起的壳瓣 → 深腔 → 红籽堆
    g += PG([(494, 242), (536, 262), (548, 306), (516, 330), (500, 300), (504, 258)], POME)
    g += PG([(416, 242), (456, 218), (494, 242), (502, 292), (474, 326), (434, 318), (418, 276)], POMOPI)
    for sx, sy, sr in ((444, 256, 12), (474, 262, 13), (458, 286, 14), (430, 280, 11),
                       (486, 298, 11), (442, 306, 12), (470, 306, 11), (458, 258, 9)):
        g += C(sx, sy, sr, SEEDR)
    for gx, gy in ((440, 252), (454, 282), (470, 258), (482, 294), (438, 302)):
        g += C(gx, gy, 3, WHITE, 0.75)
    # 地面散落两粒
    g += C(566, 420, 13, SEEDR) + C(598, 408, 11, SEEDR)
    g += C(562, 416, 3, WHITE, 0.75) + C(594, 404, 2.5, WHITE, 0.75)
    return g


# ---------- 18 durian 黄绿刺壳开缝露黄肉 ----------
def _durian_spikes(cx, cy, a, b):
    """周缘一圈圆钝刺：底在椭圆上，尖朝外，尖部加圆点。"""
    import math
    g = ""
    for i in range(24):
        if i in (23, 0, 1):        # 让位给开缝
            continue
        t = math.radians(i * 15)
        bx, by = cx + a * math.cos(t), cy + b * math.sin(t)
        nx, ny = b * math.cos(t), a * math.sin(t)
        nl = math.hypot(nx, ny)
        nx, ny = nx / nl, ny / nl
        tx, ty = -a * math.sin(t), b * math.cos(t)
        tl = math.hypot(tx, ty)
        tx, ty = tx / tl, ty / tl
        ln = 24 + 6 * math.sin(3 * t)
        tipx, tipy = bx + nx * ln, by + ny * ln
        g += PG([(round(bx + tx * 9, 1), round(by + ty * 9, 1)),
                 (round(tipx, 1), round(tipy, 1)),
                 (round(bx - tx * 9, 1), round(by - ty * 9, 1))], DUR)
        g += C(round(tipx, 1), round(tipy, 1), 6, DUR)
    return g


def art_durian():
    g = ground()
    g += E(352, 314, 152, 130, DUR_D)
    g += E(344, 306, 150, 128, DUR)
    g += shine(262, 248, 34, 48, "#ddd07a", 0.55, -22)
    # 壳面刺纹（小 Λ）
    for mx, my in ((272, 262), (316, 318), (262, 352), (378, 238),
                   (232, 300), (348, 272), (310, 388), (392, 322)):
        g += P(f"M {mx - 9} {my + 6} L {mx} {my - 8} L {mx + 9} {my + 6}", stroke=DUR_D, w=5)
    # 开缝：深腔 → 两瓣黄肉 → 棕核 → 锯齿唇
    g += PG([(426, 238), (488, 262), (502, 340), (458, 396), (420, 352), (414, 276)], "#77622a")
    g += E(458, 286, 34, 26, DURF)
    g += E(472, 346, 32, 26, DURF)
    g += E(450, 278, 12, 8, "#fdf0c0", 0.9) + E(464, 340, 11, 7, "#fdf0c0", 0.9)
    g += C(438, 318, 13, "#8a5a33")
    g += PG([(426, 238), (446, 272), (424, 306), (448, 344), (420, 352), (414, 276)], DUR)
    # 周缘圆钝刺
    g += _durian_spikes(344, 306, 150, 128)
    # 短柄
    g += R(334, 150, 16, 36, 8, "#8a5a33")
    g += E(342, 150, 18, 9, DUR_D)
    return g


# ---------- 19 starfruit 浅黄绿横切五角星 ----------
def _star_poly(cx, cy, ro, ri, fill):
    import math
    pts = []
    for i in range(10):
        rr = ro if i % 2 == 0 else ri
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((round(cx + rr * math.cos(a), 1), round(cy + rr * math.sin(a), 1)))
    return PG(pts, fill)


def art_starfruit():
    g = ground()
    # 大切面（主）：皮绿星 → 果肉星 → 内色星 → 白心 → 放射浅纹 → 籽
    g += _star_poly(350, 286, 172, 96, STARKIN)
    g += _star_poly(350, 286, 156, 82, STARF)
    g += _star_poly(350, 286, 118, 60, STARTINT)
    g += E(350, 286, 36, 32, STARCORE)
    rays = '<g opacity="0.8">'
    import math
    for ang in (-90, -18, 54, 126, 198):
        a = math.radians(ang)
        rays += L(round(350 + 44 * math.cos(a), 1), round(286 + 44 * math.sin(a), 1),
                  round(350 + 100 * math.cos(a), 1), round(286 + 100 * math.sin(a), 1),
                  "#dfe68e", 5)
    g += rays + "</g>"
    for deg in (18, 90, 162):
        g += f'<g transform="rotate({deg} 350 286)">' + E(350, 228, 5, 9, "#8a5a33") + "</g>"
    g += f'<g transform="rotate(-18 322 208)">' + E(322, 208, 14, 24, WHITE, 0.4) + "</g>"
    # 辅：右下一整条棱果（横向五棱）
    g += '<g transform="rotate(-26 606 388)">'
    g += E(612, 394, 64, 28, STAREDGE)
    g += E(604, 386, 62, 26, "#93bd82")
    g += L(548, 378, 656, 376, "#c9dfa8", 4.5)
    g += L(544, 388, 660, 388, "#c9dfa8", 4.5)
    g += L(548, 398, 656, 398, "#c9dfa8", 4.5)
    g += C(546, 386, 6, STARKIN) + C(664, 386, 6, STARKIN)
    g += "</g>"
    return g


# ---------- 20 avocado 深绿皮切半 + 棕大核 ----------
AVO_MAIN = ("M 330 152 C 396 152 446 242 446 326 C 446 404 394 444 330 444 "
            "C 266 444 214 404 214 326 C 214 242 264 152 330 152 Z")
AVO_FLESH = ("M 330 172 C 386 172 430 252 430 324 C 430 394 384 428 330 428 "
             "C 276 428 230 394 230 324 C 230 252 274 172 330 172 Z")


def art_avocado():
    g = ground()
    g += P("M 338 160 C 404 160 454 250 454 334 C 454 412 402 452 338 452 "
           "C 274 452 222 412 222 334 C 222 250 272 160 338 160 Z", AVD_D)
    g += P(AVO_MAIN, AVD)
    g += P(AVO_FLESH, AVF)
    g += C(330, 334, 86, "#e0e5a2", 0.55)
    # 大核
    g += C(330, 344, 68, PIT)
    g += C(306, 320, 11, PIT_L, 0.85)
    g += shine(262, 232, 22, 40, "#71935f", 0.55, -20)
    # 辅：右下一整只
    g += '<g transform="rotate(12 598 360)">'
    g += E(606, 368, 54, 76, AVD_D)
    g += E(598, 360, 52, 74, AVD)
    g += C(594, 286, 7, "#6b4423")
    g += f'<g transform="rotate(-16 578 330)">' + E(578, 330, 12, 26, "#71935f", 0.5) + "</g>"
    g += "</g>"
    return g


# ---------- 21 plum 紫李带果粉 ----------
def art_plum():
    g = ground()
    g += C(362, 306, 142, PLUM_D)
    g += C(354, 298, 140, PLUM)
    # 中缝
    g += P("M 356 164 Q 382 300 356 434", stroke=PLUM_D, w=7, opacity=0.5)
    # 高光 + 果粉
    g += shine(284, 238, 30, 46, "#cfaee2", 0.55, -24)
    for bx, by, br, bo in ((300, 226, 6, 0.65), (332, 206, 5, 0.6), (268, 262, 7, 0.55),
                           (316, 262, 4.5, 0.6), (356, 232, 4, 0.5), (288, 300, 5, 0.45),
                           (246, 330, 4, 0.4), (390, 250, 4, 0.4), (420, 380, 4, 0.35)):
        g += C(bx, by, br, PLUM_BLOOM, bo)
    # 柄 + 双小叶
    g += P("M 354 162 Q 358 138 368 118", stroke="#8a5a33", w=10)
    g += leaf(422, 132, 44, 17, 30)
    g += leaf(320, 118, 30, 12, -26, GREEN_L)
    return g


def arts():
    return {
        "cherry": art_cherry(),
        "coconut": art_coconut(),
        "kiwi": art_kiwi(),
        "lychee": art_lychee(),
        "persimmon": art_persimmon(),
        "pomegranate": art_pomegranate(),
        "durian": art_durian(),
        "starfruit": art_starfruit(),
        "avocado": art_avocado(),
        "plum": art_plum(),
    }
