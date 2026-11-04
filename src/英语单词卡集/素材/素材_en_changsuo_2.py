#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 场所（changsuo）第 2 段插画（10 卡：library~pool）。

每卡造型要点：library 满墙书架彩色书脊+阅读小桌 / museum 深蓝展厅白恐龙骨架展台 /
farm 红顶谷仓+白帆风车 / city 高楼天际线主楼窗格天线 / village 田野三小屋红蓝绿顶 /
building 玻璃幕墙高楼横带竖柱 / post office 白楼大信封招牌+圆顶绿邮筒 /
airport 塔台+客机舷梯 / bus stop 蓝公交靠站+站牌长椅 / pool 蓝池红白泳圈扶梯水花。
各建筑用可辨标志，主体居中放大；只画图形不画任何文字。
"""
import math
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "library", "cn": "图书馆"},
    {"w": "museum", "cn": "博物馆"},
    {"w": "farm", "cn": "农场"},
    {"w": "city", "cn": "城市"},
    {"w": "village", "cn": "乡村"},
    {"w": "building", "cn": "楼房"},
    {"w": "post office", "cn": "邮局"},
    {"w": "airport", "cn": "机场"},
    {"w": "bus stop", "cn": "公交站"},
    {"w": "pool", "cn": "游泳池"},
]


# ---------- 本组同族补充色 ----------
GLASS = "#bfe0f2"                                              # 玻璃窗（WBLUE 族浅）
GLASS_L = "#a5d9f0"                                            # 玻璃淡（WBLUE 族）
SKYBLU = "#9cc9e2"                                             # 淡蓝楼体（WBLUE 族）
MET, MET_M, MET_L = "#dfe3e6", "#c9cdd1", "#eef1f3"            # 金属浅灰族
MET_D = "#adb2b7"                                              # 金属灰中
TIRE = "#565b62"                                               # 深灰（金属族深）
GRN_D = "#699756"                                              # 深绿（GREEN 族深）
WALL = "#f9f5ea"                                               # 墙奶白（WHITE 族）
WALL_SH = "#f0eadb"                                            # 墙影（WHITE 族深）
PLINTH = "#d9cdb2"                                             # 展台基（WHITE 族深）


def road_wheel(cx, cy, r):
    """实心宽车轮。"""
    return C(cx, cy, r, INK) + C(cx, cy, r * 0.56, TIRE) + C(cx, cy, r * 0.24, MET_L)


# ---------- 12 library 书墙+阅读小桌 ----------
def art_library():
    g = ground()
    g += R(120, 170, 520, 240, 12, WOOD_D)                      # 书架体
    for y in (170, 238, 306, 374):                              # 搁板
        g += R(120, y, 520, 14 if y else 16, 4, WOOD)
    cols = (RED, SUN, TEAL, GREEN, BLUE, PINK)
    for row_y in (190, 258, 326):                               # 三层书脊
        for i in range(9):
            g += R(140 + i * 54, row_y, 40, 44, 4, cols[i % 6])
    g += R(300, 424, 160, 16, 6, WOOD)                          # 阅读桌
    g += R(312, 440, 14, 24, 4, WOOD_D) + R(434, 440, 14, 24, 4, WOOD_D)
    g += R(340, 408, 40, 16, 4, RED) + R(384, 412, 34, 12, 4, TEAL)   # 桌上书
    return g


# ---------- 13 museum 白恐龙骨架展台 ----------
def art_museum():
    g = ground()
    g += R(140, 170, 480, 240, 14, BLUE_D)                      # 展厅深蓝墙
    g += R(290, 402, 180, 22, 8, PLINTH)                        # 展台
    g += P("M 252 352 Q 380 238 508 352", stroke=WHITE, w=13)   # 脊椎弧
    ribs = ((290, 330, 268, 376), (320, 310, 296, 362), (350, 299, 326, 352),
            (380, 295, 356, 350), (410, 299, 434, 352), (440, 310, 464, 362),
            (470, 330, 492, 376))
    for x, y, ex, ey in ribs:                                   # 肋骨
        g += P(f"M {x} {y} Q {x} {y + 36} {ex} {ey}", stroke=WHITE, w=8)
    g += E(510, 348, 34, 24, WHITE)                             # 头骨
    g += P("M 524 356 Q 548 358 552 344", stroke=WHITE, w=9)    # 颌
    g += C(516, 342, 7, BLUE_D)                                 # 眼窝
    g += L(300, 376, 300, 402, WHITE, 10) + L(460, 376, 460, 402, WHITE, 10)   # 腿骨
    return g


# ---------- 14 farm 红顶谷仓+风车 ----------
def art_farm():
    g = ground()
    g += P("M 158 436 L 186 300 L 214 300 L 242 436 Z", MET_M)  # 风车塔
    for i in range(4):                                          # 风车叶
        g += (f'<g transform="rotate({i * 90} 200 292)">'
              + L(200, 292, 200, 200, MET_L, 14) + R(188, 196, 24, 18, 4, WHITE) + "</g>")
    g += C(200, 292, 13, TIRE)                                  # 毂
    g += PG([(380, 276), (530, 196), (680, 276)], RED)          # 谷仓顶
    g += C(530, 250, 16, WHITE)                                 # 顶圆窗
    g += R(400, 270, 260, 160, 12, RED_D)                       # 谷仓体
    g += R(488, 336, 84, 94, 8, "#8a5a33")                      # 大谷仓门
    g += L(530, 336, 530, 430, WOOD_D, 6)
    g += R(60, 400, 130, 12, 5, WOOD_L) + R(60, 424, 130, 12, 5, WOOD_L)   # 栅栏
    g += R(70, 396, 12, 40, 4, WOOD_L) + R(168, 396, 12, 40, 4, WOOD_L)
    g += E(330, 440, 34, 22, WOOD_L) + E(366, 448, 26, 17, WOOD_L)   # 草垛
    return g


# ---------- 15 city 高楼天际线 ----------
def art_city():
    g = ground()
    g += cloud_p(180, 120, 0.55, WHITE) + cloud_p(640, 110, 0.5, WHITE)
    g += R(90, 220, 120, 216, 10, SKYBLU)                       # 后排楼群
    g += R(240, 180, 130, 256, 10, WBLUE)
    g += R(390, 236, 110, 200, 10, SKYBLU)
    g += R(510, 200, 150, 236, 10, WBLUE)
    g += R(300, 140, 160, 296, 12, BLUE)                        # 主楼
    for r in range(7):
        for c in range(3):
            g += R(316 + c * 48, 158 + r * 40, 36, 26, 4, GLASS)
    g += L(380, 140, 380, 102, MET_D, 6)                        # 天线
    g += C(380, 98, 7, RED)
    g += R(80, 330, 150, 106, 10, TEAL)                         # 前景矮楼
    g += R(96, 348, 34, 26, 4, GLASS) + R(140, 348, 34, 26, 4, GLASS)
    g += R(560, 348, 140, 88, 10, GREEN)
    g += R(576, 366, 34, 26, 4, GLASS) + R(620, 366, 34, 26, 4, GLASS)
    return g


# ---------- 16 village 田野三小屋 ----------
def art_village():
    g = ground()
    g += cloud_p(150, 250, 0.5, WHITE)
    g += P("M 40 360 L 720 344 L 720 480 L 40 480 Z", GREEN_L)  # 田野
    g += P("M 40 404 Q 380 390 720 400", stroke=GRN_D, w=6)     # 田埂
    g += P("M 40 444 Q 380 430 720 442", stroke=GRN_D, w=6)
    g += R(90, 370, 130, 70, 8, WHITE)                          # 屋一（红顶）
    g += PG([(78, 374), (155, 316), (232, 374)], RED)
    g += R(138, 398, 34, 42, 4, WOOD_D) + R(104, 386, 28, 22, 4, GLASS)
    g += R(300, 360, 150, 80, 8, WALL)                          # 屋二（蓝顶）
    g += PG([(286, 364), (375, 300), (464, 364)], BLUE)
    g += R(358, 392, 36, 48, 4, WOOD_D)
    g += R(316, 376, 30, 24, 4, GLASS) + R(404, 376, 30, 24, 4, GLASS)
    g += R(540, 378, 120, 62, 8, WALL_SH)                       # 屋三（绿顶）
    g += PG([(528, 382), (600, 330), (672, 382)], GREEN)
    g += R(586, 400, 30, 40, 4, WOOD_D) + R(552, 392, 24, 20, 4, GLASS)
    return g


# ---------- 17 building 玻璃幕墙高楼 ----------
def art_building():
    g = ground()
    g += R(120, 240, 130, 196, 12, SKYBLU)                      # 左侧楼
    for r in range(4):
        for c in range(2):
            g += R(136 + c * 56, 258 + r * 44, 40, 30, 4, GLASS)
    g += R(520, 260, 130, 176, 12, SKYBLU)                      # 右侧楼
    for r in range(4):
        for c in range(2):
            g += R(536 + c * 56, 278 + r * 44, 40, 30, 4, GLASS)
    g += R(280, 140, 200, 296, 14, WBLUE)                       # 主玻璃楼
    for r in range(7):
        g += R(280, 160 + r * 40, 200, 22, 4, GLASS_L)          # 玻璃横带
    for c in range(3):
        g += R(330 + c * 50, 140, 10, 296, 3, WBLUE)            # 竖柱
    g += R(272, 130, 216, 16, 8, BLUE_D)                        # 顶檐
    g += R(264, 436, 232, 18, 6, MET_M)                         # 底座
    g += R(330, 400, 100, 36, 8, BLUE_D)                        # 门厅
    return g


# ---------- 18 post office 大信封+绿邮筒 ----------
def art_postoffice():
    g = ground()
    g += R(160, 210, 440, 226, 16, WALL)                        # 店身
    g += R(230, 330, 80, 106, 8, GREEN)                         # 门
    g += C(296, 386, 6, SUN)
    g += R(320, 260, 190, 120, 10, WHITE)                       # 大信封招牌
    g += PG([(322, 262), (415, 318), (508, 262)], WALL_SH)      # 封口盖
    g += R(520, 320, 72, 116, 16, GREEN)                        # 绿邮筒
    g += E(556, 320, 36, 18, GREEN)                             # 圆顶
    g += E(556, 312, 40, 12, GRN_D)                             # 顶盖
    g += R(536, 356, 40, 12, 4, WOOD_D)                         # 投信口
    g += R(512, 434, 88, 14, 4, GRN_D)                          # 底座
    return g


# ---------- 19 airport 塔台+客机舷梯 ----------
def art_airport():
    g = ground()
    g += PG([(560, 430), (580, 260), (640, 260), (660, 430)], MET_M)   # 塔台杆
    g += R(546, 218, 128, 46, 10, BLUE)                         # 台
    g += R(554, 208, 112, 20, 8, GLASS)
    g += R(552, 196, 116, 14, 6, MET_D)
    g += L(610, 196, 610, 168, MET_D, 5)                        # 天线
    g += PG([(120, 322), (146, 274), (162, 322)], RED)          # 尾翼
    g += P("M 100 350 Q 100 322 150 320 L 330 320 Q 400 320 432 348 Q 436 352 432 356 "
           "Q 400 384 330 384 L 150 384 Q 100 382 100 350 Z", WHITE)   # 机身
    for i in range(7):                                          # 舷窗
        g += C(160 + i * 28, 336, 7, SKYBLU)
    g += P("M 396 330 Q 418 334 428 346 L 404 352 Q 394 342 396 330 Z", SKYBLU)   # 驾驶舱
    g += PG([(210, 366), (262, 412), (300, 404), (250, 362)], "#e9e2d4")   # 机翼
    g += R(352, 334, 20, 36, 4, MET_M)                          # 舱门
    g += P("M 368 386 L 428 386 L 460 438 L 396 438 Z", MET_M)  # 舷梯
    g += L(428, 386, 460, 438, MET_D, 6)
    g += L(380, 400, 428, 400, MET_D, 5) + L(392, 416, 440, 416, MET_D, 5)
    g += L(404, 432, 452, 432, MET_D, 5)
    g += L(80, 458, 460, 458, YEL, 8)                           # 停机坪引导线
    return g


# ---------- 20 bus stop 蓝公交靠站 ----------
def art_busstop():
    g = ground()
    g += R(60, 250, 240, 154, 18, BLUE)                         # 公交车身
    g += R(84, 282, 56, 50, 8, GLASS) + R(156, 282, 56, 50, 8, GLASS) + R(232, 282, 48, 50, 8, GLASS)
    g += R(62, 350, 10, 14, 4, SUN)                             # 尾灯
    g += road_wheel(140, 406, 38) + road_wheel(240, 406, 38)
    g += L(560, 250, 560, 440, MET_D, 10)                       # 站牌杆
    g += R(520, 210, 80, 90, 10, BLUE)                          # 站牌
    g += C(560, 240, 16, WHITE)                                 # 圆标
    g += R(544, 254, 32, 20, 5, WHITE)                          # 牌上小车
    g += C(552, 276, 5, WHITE) + C(568, 276, 5, WHITE)
    g += R(584, 336, 162, 16, 8, RED)                           # 棚
    g += L(738, 352, 738, 436, MET_D, 8)                        # 棚柱
    g += R(600, 366, 130, 14, 6, WOOD)                          # 长椅背
    g += R(600, 396, 130, 16, 6, WOOD)                          # 椅面
    g += R(608, 412, 12, 24, 4, WOOD_D) + R(706, 412, 12, 24, 4, WOOD_D)
    return g


# ---------- 21 pool 蓝池泳圈水花 ----------
def art_pool():
    g = ground()
    g += E(380, 362, 296, 100, "#e6dfcf")                       # 池沿
    g += E(380, 360, 280, 90, BLUE)                             # 池体
    g += E(380, 358, 262, 78, WBLUE)                            # 池水
    g += P("M 210 372 Q 300 360 380 372 Q 460 384 550 372", stroke=WHITE, w=6, opacity=0.8)
    g += C(380, 356, 56, RED)                                   # 泳圈
    g += C(380, 356, 30, WBLUE)                                 # 圈洞
    g += C(356, 336, 8, WHITE) + C(404, 336, 8, WHITE) + C(356, 376, 8, WHITE) + C(404, 376, 8, WHITE)
    g += drop(600, 300, 14, WBLUE) + drop(628, 330, 10, WBLUE)  # 水花
    g += P("M 578 374 Q 610 356 642 374", stroke=WHITE, w=6, opacity=0.8)
    g += L(650, 300, 650, 372, MET_M, 9) + L(672, 300, 672, 372, MET_M, 9)   # 池梯
    g += L(650, 316, 672, 316, MET_M, 7) + L(650, 336, 672, 336, MET_M, 7)
    g += L(650, 356, 672, 356, MET_M, 7)
    g += C(180, 330, 24, SUN) + C(172, 322, 8, WHITE)           # 池边球
    return g


def arts():
    return {
        "library": art_library(),
        "museum": art_museum(),
        "farm": art_farm(),
        "city": art_city(),
        "village": art_village(),
        "building": art_building(),
        "post office": art_postoffice(),
        "airport": art_airport(),
        "bus stop": art_busstop(),
        "pool": art_pool(),
    }
