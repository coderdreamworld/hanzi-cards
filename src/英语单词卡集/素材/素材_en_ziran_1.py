#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 自然·天气（ziran）第 1 段插画（11 卡：sun~tree）。

每卡造型要点：sun 金太阳十二芒+笑脸 / moon 弯月睡脸伴星 / star 金星五角+闪烁线 /
sky 蓝天白云风筝高飞 / cloud 大白云双层 / rain 乌云雨滴撑伞娃 / snow 六瓣雪花雪地 /
wind 风线吹树弯腰叶飘 / lightning 紫电劈乌云 / island 海中小岛棕榈椰子 / tree 圆冠大树。
主体居中放大，主色相邻错开；只画图形不画任何文字。
"""
import math
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "sun", "cn": "太阳"},
    {"w": "moon", "cn": "月亮"},
    {"w": "star", "cn": "星星"},
    {"w": "sky", "cn": "天空"},
    {"w": "cloud", "cn": "云"},
    {"w": "rain", "cn": "雨"},
    {"w": "snow", "cn": "雪"},
    {"w": "wind", "cn": "风"},
    {"w": "lightning", "cn": "闪电"},
    {"w": "island", "cn": "岛屿"},
    {"w": "tree", "cn": "树"},
]


# ---------- 本组同族补充色 ----------
SKY_B = "#cfe9f7"                                              # 天空浅蓝（WBLUE 族更浅）
SUN_D = "#d98d1c"                                              # 太阳深一号（SUN 族深）
SNOW_B, SNOW_L = "#bfe0f2", "#dff0f8"                          # 雪花蓝白（WBLUE 族）
GRAY_C, GRAY_D = "#9aa4ad", "#868f99"                          # 乌云/石灰（金属灰族）
PURPLE, PURPLE_D = "#9b7fd4", "#7c5fb8"                        # 紫电（按词库 note 新族）
SAND = "#f2d9a4"                                               # 沙滩浅黄（YEL 族浅）
GRN_D = "#699756"                                              # 深草绿（GREEN 族深）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色高光椭圆（可旋转）。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


def snowflake(cx, cy, r, main=SNOW_B, sub=SNOW_L):
    """六瓣雪花：主枝+双侧小枝。"""
    g = ""
    for i in range(6):
        a = math.radians(i * 60)
        g += L(cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), main, max(4, r * 0.11))
        for t in (0.55, 0.85):
            bx, by = cx + t * r * math.cos(a), cy + t * r * math.sin(a)
            for da in (-40, 40):
                b = a + math.radians(da)
                g += L(bx, by, bx + r * 0.3 * math.cos(b), by + r * 0.3 * math.sin(b),
                       sub, max(3, r * 0.07))
    return g + C(cx, cy, r * 0.14, main)


# ---------- 1 sun 金太阳光芒四射 ----------
def art_sun():
    g = ground()
    for i in range(12):                                         # 十二道光芒
        a = math.radians(i * 30)
        g += L(380 + 128 * math.cos(a), 250 + 128 * math.sin(a),
               380 + 182 * math.cos(a), 250 + 182 * math.sin(a), SUN, 13)
    g += C(384, 254, 110, SUN_D)
    g += C(380, 250, 106, SUN)
    g += C(340, 214, 20, SUN_L, 0.85)
    g += E(344, 244, 9, 12, INK) + E(416, 244, 9, 12, INK)      # 眼
    g += P("M 350 280 Q 380 302 410 280", stroke=INK, w=7)      # 笑
    g += C(318, 270, 11, PINK, 0.8) + C(442, 270, 11, PINK, 0.8)
    for x in (200, 560):                                        # 地面小草
        g += P(f"M {x} 452 Q {x - 6} 436 {x} 424", stroke=GREEN, w=6)
        g += P(f"M {x + 14} 452 Q {x + 20} 438 {x + 16} 428", stroke=GRN_D, w=5)
    return g


# ---------- 2 moon 弯月睡脸伴星 ----------
def art_moon():
    g = ground()
    g += P("M 468 128 Q 322 190 322 276 Q 322 362 478 424 Q 396 384 356 312 "
           "Q 332 258 360 196 Q 396 148 468 128 Z", SUN)         # 弯月
    g += P("M 356 312 Q 332 258 360 196", stroke=SUN_L, w=7, opacity=0.8)   # 内缘高光
    g += P("M 384 262 Q 396 272 408 262", stroke=INK, w=6)      # 闭眼
    g += P("M 388 300 Q 397 308 406 300", stroke=INK, w=5)      # 嘴
    g += C(374, 286, 9, PINK, 0.7)
    for x, y, r in ((546, 168, 16), (588, 292, 13), (236, 196, 12), (206, 336, 14), (508, 396, 11)):
        g += star5(x, y, r, SUN)
    return g


# ---------- 3 star 金星五角闪烁 ----------
def art_star():
    g = ground()
    g += L(380, 100, 380, 62, SUN, 9)                           # 闪烁线
    g += L(212, 268, 172, 268, SUN, 9)
    g += L(548, 268, 588, 268, SUN, 9)
    g += L(262, 156, 236, 132, SUN, 8)
    g += L(498, 156, 524, 132, SUN, 8)
    g += L(262, 380, 236, 404, SUN, 8)
    g += L(498, 380, 524, 404, SUN, 8)
    g += star5(384, 274, 132, SUN_D)
    g += star5(380, 268, 126, SUN)
    g += C(336, 216, 16, SUN_L, 0.9)
    g += star5(600, 158, 22)
    g += star5(172, 386, 20)
    return g


# ---------- 4 sky 蓝天白云风筝高飞 ----------
def art_sky():
    g = ground()
    g += R(0, 0, 760, 424, 0, SKY_B)                            # 蓝天
    g += cloud_p(176, 104, 0.8, WHITE)
    g += cloud_p(592, 88, 0.65, WHITE)
    g += cloud_p(452, 168, 0.5, WHITE)
    g += PG([(380, 186), (326, 250), (380, 322), (434, 250)], RED)   # 风筝面
    g += L(380, 186, 380, 322, RED_D, 5)                        # 骨架
    g += L(326, 250, 434, 250, RED_D, 5)
    g += P("M 380 322 Q 400 352 386 378 Q 374 400 392 424", stroke=SUN, w=8)   # 尾带
    g += P("M 380 322 Q 336 384 298 434", stroke=INK, w=4)      # 风筝线
    for x in (150, 620):                                        # 地面小草
        g += P(f"M {x} 456 Q {x - 6} 440 {x} 428", stroke=GREEN, w=6)
    return g


# ---------- 5 cloud 大白云双层 ----------
def art_cloud():
    g = ground()
    g += C(300, 316, 66, "#e9e2d2")                             # 云影层
    g += C(396, 274, 84, "#e9e2d2")
    g += C(492, 314, 68, "#e9e2d2")
    g += R(244, 306, 296, 66, 32, "#e9e2d2")
    g += C(292, 300, 66, WHITE)                                 # 云本体
    g += C(388, 258, 84, WHITE)
    g += C(484, 298, 68, WHITE)
    g += R(236, 292, 296, 66, 32, WHITE)
    g += E(342, 232, 26, 14, WHITE, 0.9)
    g += star5(610, 196, 16, SUN)
    g += star5(158, 186, 14, SUN)
    return g


# ---------- 6 rain 乌云雨滴撑伞娃 ----------
def art_rain():
    g = ground()
    g += C(268, 152, 62, GRAY_C)                                # 乌云
    g += C(380, 130, 80, GRAY_C)
    g += C(492, 152, 64, GRAY_C)
    g += R(218, 150, 340, 62, 30, GRAY_C)
    g += R(218, 178, 340, 32, 16, GRAY_D)
    # 撑伞（伞先画，娃双手举到伞杆）
    g += P("M 460 250 Q 560 158 660 250 Q 636 238 610 250 Q 586 238 560 250 "
           "Q 536 238 510 250 Q 486 238 460 250 Z", RED)
    g += L(560, 250, 560, 330, INK, 8)
    g += P("M 560 330 Q 560 344 546 344", stroke=INK, w=8)
    g += kid(560, 444, 0.72, arms="up", shirt=TEAL)
    for x, y, r in ((298, 252, 14), (350, 306, 12), (430, 254, 14), (482, 308, 12),
                    (266, 330, 11), (390, 350, 11), (316, 396, 10)):
        g += drop(x, y, r, WBLUE)
    return g


# ---------- 7 snow 六瓣雪花雪地 ----------
def art_snow():
    g = ground()
    g += E(380, 434, 244, 30, WHITE)                            # 雪地
    g += E(380, 436, 200, 22, SNOW_L, 0.7)
    g += snowflake(380, 260, 96)                                # 主雪花
    g += C(380, 260, 14, WHITE)
    g += snowflake(190, 388, 40)                                # 小雪花
    g += snowflake(566, 372, 34)
    for x, y in ((300, 448), (470, 442), (240, 430), (520, 452)):
        g += C(x, y, 5, SNOW_L, 0.9)
    return g


# ---------- 8 wind 风线吹树弯腰叶飘 ----------
def art_wind():
    g = ground()
    # 风线（最先画置底层，只露在空白处，不遮人物五官与树冠）
    g += P("M 118 182 Q 208 160 294 188", stroke=WHITE, w=10, opacity=0.9)
    g += P("M 104 262 Q 170 246 240 268", stroke=WHITE, w=8, opacity=0.85)
    g += P("M 132 336 Q 210 322 286 344", stroke=WHITE, w=7, opacity=0.8)
    # 弯干 + 树冠
    g += P("M 566 436 Q 548 356 480 318 Q 440 296 428 262", stroke=WOOD_D, w=24)   # 弯干
    g += C(424, 244, 64, GREEN)                                 # 树冠
    g += C(356, 278, 52, GREEN)
    g += C(478, 282, 54, GREEN)
    g += C(412, 196, 50, GREEN_L, 0.9)
    # 娃（衣摆连着向后飘的小飘带）
    g += kid(230, 442, 0.78, pose="walk", face="smile", shirt=YEL)
    g += P("M 197 334 Q 160 330 136 312", stroke=YEL, w=10)
    # 飘落的叶子
    g += shine(520, 250, 16, 8, GREEN_L, 0.9, -20)              # 飘落的叶子
    g += shine(570, 300, 14, 7, GREEN_L, 0.9, -30)
    g += shine(620, 350, 12, 6, GREEN_L, 0.85, -35)
    return g


# ---------- 9 lightning 紫电劈乌云 ----------
def art_lightning():
    g = ground()
    g += C(268, 152, 62, GRAY_C)
    g += C(380, 130, 80, GRAY_C)
    g += C(492, 152, 64, GRAY_C)
    g += R(218, 150, 340, 62, 30, GRAY_C)
    g += R(218, 178, 340, 32, 16, GRAY_D)
    g += PG([(388, 204), (330, 306), (374, 306), (330, 410), (420, 296), (376, 296),
             (414, 212)], PURPLE)                               # 紫电
    g += L(366, 250, 348, 292, PURPLE_D, 6)
    g += drop(296, 262, 12, WBLUE)
    g += drop(474, 300, 12, WBLUE)
    g += drop(258, 336, 10, WBLUE)
    return g


# ---------- 10 island 海中小岛棕榈树 ----------
def art_island():
    g = ground()
    g += P("M 80 412 Q 380 382 680 412 L 680 470 Q 380 492 80 470 Z", WBLUE)   # 海
    g += P("M 120 428 Q 200 416 280 428", stroke=WHITE, w=6, opacity=0.85)     # 浪沫
    g += P("M 470 432 Q 550 420 630 432", stroke=WHITE, w=6, opacity=0.85)
    g += P("M 296 432 Q 330 396 380 392 Q 430 396 464 432 Q 380 454 296 432 Z", SAND)   # 沙岛
    g += P("M 380 396 Q 372 330 392 288", stroke=WOOD_D, w=16)  # 棕榈弯干
    g += P("M 392 288 Q 350 262 310 274", stroke=GREEN, w=13)   # 椰叶五片
    g += P("M 392 288 Q 356 242 336 238", stroke=GREEN, w=12)
    g += P("M 392 288 Q 396 234 380 226", stroke=GREEN, w=12)
    g += P("M 392 288 Q 428 240 448 242", stroke=GREEN, w=12)
    g += P("M 392 288 Q 436 264 474 278", stroke=GREEN, w=13)
    g += C(384, 298, 9, WOOD_D) + C(400, 300, 9, WOOD_D)        # 椰子
    return g


# ---------- 11 tree 圆冠大树 ----------
def art_tree():
    g = ground()
    g += tree_round(380, 432, 1.2)
    g += shine(336, 210, 34, 52, GREEN_L, 0.7, 14)              # 冠高光
    for x in (216, 556):                                        # 地面草撮
        g += P(f"M {x} 452 Q {x - 7} 434 {x} 420", stroke=GREEN, w=7)
        g += P(f"M {x + 16} 452 Q {x + 23} 438 {x + 18} 426", stroke=GRN_D, w=6)
    return g


def arts():
    return {
        "sun": art_sun(),
        "moon": art_moon(),
        "star": art_star(),
        "sky": art_sky(),
        "cloud": art_cloud(),
        "rain": art_rain(),
        "snow": art_snow(),
        "wind": art_wind(),
        "lightning": art_lightning(),
        "island": art_island(),
        "tree": art_tree(),
    }
