#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 场所（changsuo）第 1 段插画（11 卡：park~cinema）。

每卡造型要点：park 亭子大树长椅 / zoo 大门拱+栅栏后长颈鹿探头 / garden 篱笆花圃喷壶 /
playground 滑梯秋千沙坑 / street 两排小店斑马线路灯 / shop 条纹遮阳棚橱窗货架 /
supermarket 货架彩盒一排+推车 / market 红白棚摊位果蔬堆 / hospital 白楼圆底红十字 /
restaurant 圆招牌刀叉图案+绿伞 / cinema 深蓝影院胶片盘+门上灯泡排。
各建筑用可辨标志，主体居中放大；只画图形不画任何文字。
"""
import math
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "park", "cn": "公园"},
    {"w": "zoo", "cn": "动物园"},
    {"w": "garden", "cn": "花园"},
    {"w": "playground", "cn": "游乐场"},
    {"w": "street", "cn": "街道"},
    {"w": "shop", "cn": "商店"},
    {"w": "supermarket", "cn": "超市"},
    {"w": "market", "cn": "市场"},
    {"w": "hospital", "cn": "医院"},
    {"w": "restaurant", "cn": "餐厅"},
    {"w": "cinema", "cn": "电影院"},
]


# ---------- 本组同族补充色 ----------
GLASS = "#bfe0f2"                                              # 玻璃窗（WBLUE 族浅）
MET, MET_M, MET_L = "#dfe3e6", "#c9cdd1", "#eef1f3"            # 金属浅灰族
MET_D = "#adb2b7"                                              # 金属灰中
TIRE = "#565b62"                                               # 深灰（金属族深）
TREAD = "#8a9096"                                              # 路面灰（金属族中）
GRN_D = "#699756"                                              # 深绿（GREEN 族深）
SOIL = "#b58756"                                               # 花圃土（WOOD 族变体）
SAND = "#f2d9a4"                                               # 沙坑（YEL 族浅）
SAND_SH = "#e0bf8a"                                            # 沙影（YEL 族中）
WALL = "#f9f5ea"                                               # 店墙奶白（WHITE 族）
WALL_SH = "#f0eadb"                                            # 墙影（WHITE 族深）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色高光椭圆（可旋转）。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


def road_wheel(cx, cy, r):
    """实心宽车轮。"""
    return C(cx, cy, r, INK) + C(cx, cy, r * 0.56, TIRE) + C(cx, cy, r * 0.24, MET_L)


# ---------- 1 park 亭子大树长椅 ----------
def art_park():
    g = ground()
    g += tree_round(170, 436, 0.95)                             # 大树
    g += shine(136, 218, 26, 40, GREEN_L, 0.7, 12)
    g += R(330, 386, 130, 18, 6, WOOD)                          # 长椅面
    g += R(330, 354, 130, 14, 6, WOOD)                          # 椅背
    g += R(338, 354, 12, 34, 4, WOOD_D) + R(440, 354, 12, 34, 4, WOOD_D)
    g += R(340, 404, 12, 30, 4, WOOD_D) + R(438, 404, 12, 30, 4, WOOD_D)
    g += PG([(468, 322), (578, 252), (688, 322)], RED)          # 亭顶
    g += C(578, 246, 9, RED_D)                                  # 顶钮
    g += R(496, 322, 164, 14, 6, WOOD_D)                        # 檐枋
    g += R(520, 336, 16, 94, 6, WOOD_D) + R(620, 336, 16, 94, 6, WOOD_D)   # 柱
    g += R(500, 428, 156, 14, 6, WOOD_D)                        # 台基
    g += flower5(300, 442, 12) + flower5(560, 452, 11)
    return g


# ---------- 2 zoo 大门拱+长颈鹿探头 ----------
def art_zoo():
    g = ground()
    g += R(160, 240, 60, 190, 14, RED_D) + R(540, 240, 60, 190, 14, RED_D)   # 门柱
    g += C(190, 232, 16, SUN) + C(570, 232, 16, SUN)            # 柱顶球
    for i in range(3):                                          # 门内栅栏
        g += L(226, 316 + i * 36, 534, 316 + i * 36, MET_M, 9)
    g += R(368, 254, 26, 130, 12, SUN)                          # 长颈鹿颈
    g += E(381, 248, 30, 24, SUN)                               # 头
    g += L(370, 230, 362, 216, WOOD_D, 6) + C(360, 212, 7, WOOD_D)   # 角
    g += L(392, 230, 400, 216, WOOD_D, 6) + C(402, 212, 7, WOOD_D)
    g += C(392, 242, 5, INK)
    g += E(396, 256, 12, 8, "#c99a6a")                          # 吻
    g += R(372, 284, 12, 10, 3, WOOD_D) + R(378, 314, 12, 10, 3, WOOD_D)   # 斑
    g += R(372, 344, 12, 10, 3, WOOD_D)
    g += P("M 214 258 Q 380 194 546 258 L 546 288 Q 380 230 214 288 Z", RED)   # 拱牌
    return g


# ---------- 3 garden 篱笆花圃喷壶 ----------
def art_garden():
    g = ground()
    for x in range(140, 640, 60):                               # 篱笆竖条
        g += R(x, 300, 18, 130, 8, WOOD_L)
    g += R(130, 330, 520, 16, 6, WOOD)                          # 横杆
    g += R(130, 378, 520, 16, 6, WOOD)
    g += P("M 130 456 Q 200 424 380 430 Q 560 436 640 458 Q 380 486 130 456 Z", SOIL)   # 花圃
    g += flower5(220, 400, 18) + flower5(320, 382, 20)
    g += flower5(430, 386, 19) + flower5(540, 402, 17)
    g += E(600, 408, 44, 36, TEAL)                              # 喷壶体
    g += PG([(630, 390), (668, 356), (678, 364), (644, 400)], TEAL)   # 壶嘴
    g += P("M 570 384 Q 600 356 630 384", stroke=TEAL_D, w=9)   # 提梁
    g += E(600, 376, 16, 8, TEAL_D)                             # 壶口
    g += drop(692, 396, 10, WBLUE) + drop(708, 420, 8, WBLUE)
    return g


# ---------- 4 playground 滑梯秋千沙坑 ----------
def art_playground():
    g = ground()
    g += E(300, 448, 200, 22, SAND, 0.9)                        # 沙坑
    g += R(150, 260, 110, 24, 8, RED)                           # 滑梯平台
    g += PG([(238, 260), (268, 270), (238, 280)], SUN)          # 小旗
    g += R(160, 284, 18, 150, 6, RED_D) + R(232, 284, 18, 150, 6, RED_D)   # 平台柱
    g += P("M 256 282 Q 340 340 362 424 L 322 430 Q 300 356 246 302 Z", YEL)   # 滑道
    g += L(486, 434, 560, 260, MET_D, 14)                       # 秋千架
    g += L(634, 434, 560, 260, MET_D, 14)
    g += L(596, 434, 666, 260, MET_D, 14)
    g += L(744, 434, 666, 260, MET_D, 14)
    g += L(560, 260, 666, 260, MET_D, 12)                       # 顶梁
    g += L(590, 266, 590, 360, INK, 4) + L(618, 266, 618, 360, INK, 4)   # 秋千绳
    g += R(582, 358, 44, 12, 5, RED)                            # 座板
    return g


# ---------- 5 street 两排小店斑马线 ----------
def art_street():
    g = ground()
    g += P("M 130 300 L 630 300 L 720 480 L 40 480 Z", TREAD)   # 路面
    for i in range(5):                                          # 斑马线（透视）
        x0 = 180 + i * 84
        g += PG([(x0, 424), (x0 + 52, 424), (x0 + 66, 464), (x0 + 30, 464)], WHITE)
    g += R(30, 208, 182, 20, 8, RED_D) + R(36, 218, 170, 90, 10, PINK)   # 左排店
    g += R(60, 238, 40, 34, 6, GLASS) + R(120, 238, 40, 34, 6, GLASS)
    g += R(552, 208, 182, 20, 8, BLUE_D) + R(560, 218, 166, 90, 10, BLUE)   # 右排店
    g += R(582, 238, 40, 34, 6, GLASS) + R(640, 238, 40, 34, 6, GLASS)
    g += L(240, 226, 240, 300, MET_D, 7) + C(240, 220, 9, SUN)  # 路灯
    g += L(520, 226, 520, 300, MET_D, 7) + C(520, 220, 9, SUN)
    return g


# ---------- 6 shop 遮阳棚橱窗货架 ----------
def art_shop():
    g = ground()
    g += R(170, 200, 420, 236, 16, WALL)                        # 店身
    g += R(140, 264, 480, 30, 6, RED)                           # 遮阳棚
    for i, x in enumerate(range(140, 620, 60)):                 # 棚下扇贝垂边
        g += E(x + 30, 294, 30, 13, WHITE if i % 2 else RED)
    g += R(202, 322, 298, 106, 12, RED_D)                       # 橱窗框
    g += R(210, 330, 282, 90, 8, GLASS)
    for c, col in enumerate((SUN, TEAL, GREEN, PINK)):          # 上层货架
        g += R(230 + c * 60, 344, 34, 24, 4, col)
    g += R(226, 370, 250, 8, 4, WHITE)
    for c, col in enumerate((BLUE, RED, SUN, TEAL)):            # 下层货架
        g += R(230 + c * 60, 382, 34, 22, 4, col)
    g += R(516, 330, 70, 106, 10, BLUE_D)                       # 门
    g += C(576, 386, 6, SUN)
    return g


# ---------- 7 supermarket 货架+推车 ----------
def art_supermarket():
    g = ground()
    g += R(120, 180, 520, 250, 14, WALL)                        # 店内墙
    g += R(120, 148, 520, 32, 12, BLUE)                         # 招牌带
    g += C(280, 164, 10, WHITE) + C(380, 164, 10, WHITE) + C(480, 164, 10, WHITE)
    g += R(150, 240, 340, 160, 10, MET_M)                       # 货架
    for y in (240, 296, 352):
        g += R(150, y, 340, 14, 4, MET_D)
    cols1 = (SUN, TEAL, GREEN, PINK, BLUE, RED)
    cols2 = (GREEN, BLUE, RED, SUN, TEAL, PINK)
    cols3 = (PINK, SUN, TEAL, GREEN, RED, BLUE)
    for i in range(6):
        g += R(168 + i * 52, 256, 40, 26, 4, cols1[i])          # 上层商品
        g += R(168 + i * 52, 312, 40, 26, 4, cols2[i])          # 中层
        g += R(168 + i * 52, 368, 40, 26, 4, cols3[i])          # 下层
    g += P("M 520 330 L 620 330 L 606 380 L 534 380 Z", MET_M)  # 推车篮
    g += L(528, 348, 614, 348, MET_L, 4) + L(534, 364, 608, 364, MET_L, 4)
    g += L(568, 330, 568, 380, MET_L, 4)
    g += L(620, 330, 648, 314, MET_D, 8)                        # 推杆
    g += C(544, 396, 12, INK) + C(596, 396, 12, INK)            # 轮
    return g


# ---------- 8 market 红白棚果蔬摊 ----------
def art_market():
    g = ground()
    g += R(140, 298, 16, 130, 6, WOOD_D) + R(604, 298, 16, 130, 6, WOOD_D)   # 棚柱
    g += R(130, 246, 500, 52, 10, RED)                          # 棚顶
    g += R(190, 246, 60, 52, 0, WHITE) + R(310, 246, 60, 52, 0, WHITE) + R(430, 246, 60, 52, 0, WHITE)
    g += R(150, 380, 460, 56, 10, WOOD)                         # 摊台
    g += R(150, 414, 460, 22, 8, WOOD_D)
    for x, y in ((190, 368), (218, 364), (246, 368), (204, 352), (232, 352)):   # 苹果堆
        g += C(x, y, 14, RED)
    for x, y in ((300, 368), (326, 364), (352, 368), (314, 352), (338, 352)):   # 橙子堆
        g += C(x, y, 13, SUN)
    g += C(420, 370, 16, GREEN) + C(444, 374, 14, GREEN_L) + C(464, 370, 15, GREEN)   # 青菜
    g += PG([(500, 382), (516, 336), (532, 382)], RED_D)        # 萝卜
    g += L(516, 336, 508, 322, GREEN, 5) + L(516, 336, 524, 322, GREEN, 5)
    return g


# ---------- 9 hospital 白楼红十字 ----------
def art_hospital():
    g = ground()
    g += R(110, 280, 60, 156, 12, WALL_SH) + R(590, 280, 60, 156, 12, WALL_SH)   # 侧翼
    g += R(150, 190, 460, 246, 16, WHITE)                       # 主楼
    g += C(380, 234, 42, WHITE)                                 # 圆底
    g += R(360, 226, 40, 16, 4, RED)                            # 红十字横
    g += R(372, 214, 16, 40, 4, RED)                            # 红十字竖
    for r in range(3):
        for c in range(4):
            g += R(180 + c * 105, 296 + r * 58, 70, 40, 8, GLASS)   # 窗
    g += R(330, 388, 100, 14, 6, BLUE_D)                        # 雨棚
    g += R(340, 402, 80, 34, 8, BLUE)                           # 门
    return g


# ---------- 10 restaurant 圆牌刀叉图案+绿伞 ----------
def art_restaurant():
    g = ground()
    g += R(160, 210, 440, 226, 16, WALL)                        # 店身
    g += C(240, 340, 68, WHITE)                                 # 圆招牌
    g += L(214, 296, 214, 370, MET_D, 8)                        # 叉
    g += L(202, 296, 202, 314, MET_D, 5)
    g += L(226, 296, 226, 314, MET_D, 5)
    g += P("M 202 314 Q 214 324 226 314", stroke=MET_D, w=5)
    g += P("M 262 296 Q 276 320 262 344 L 254 344 L 254 296 Z", MET_D)   # 刀刃
    g += R(252, 344, 12, 28, 5, MET_D)                          # 刀柄
    g += R(300, 330, 180, 80, 10, GLASS)                        # 橱窗
    g += R(310, 376, 74, 10, 4, WOOD)
    g += R(496, 330, 76, 106, 10, GRN_D)                        # 门
    g += C(548, 386, 6, SUN)
    g += L(560, 350, 560, 244, WOOD_D, 9)                       # 门口绿伞
    g += P("M 470 268 Q 560 196 650 268 Q 626 258 600 268 Q 576 258 560 268 "
           "Q 534 258 520 268 Q 494 258 470 268 Z", GREEN)
    g += E(560, 372, 60, 10, SAND_SH, 0.6)
    return g


# ---------- 11 cinema 深蓝影院胶片盘 ----------
def art_cinema():
    g = ground()
    g += R(150, 210, 460, 226, 16, BLUE_D)                      # 店身
    g += C(380, 300, 92, TIRE)                                  # 胶片盘
    g += C(380, 300, 26, MET_L)                                 # 中毂
    for i in range(6):                                          # 链孔
        a = i * math.pi / 3
        g += C(380 + 58 * math.cos(a), 300 + 58 * math.sin(a), 15, BLUE_D)
    g += P("M 318 250 Q 380 230 442 250", stroke=MET_M, w=6, opacity=0.8)
    for i in range(11):                                         # 门顶灯泡排
        g += C(200 + i * 36, 232, 9, SUN)
    g += R(300, 372, 60, 64, 8, SUN) + R(400, 372, 60, 64, 8, SUN)   # 双门
    return g


def arts():
    return {
        "park": art_park(),
        "zoo": art_zoo(),
        "garden": art_garden(),
        "playground": art_playground(),
        "street": art_street(),
        "shop": art_shop(),
        "supermarket": art_supermarket(),
        "market": art_market(),
        "hospital": art_hospital(),
        "restaurant": art_restaurant(),
        "cinema": art_cinema(),
    }
