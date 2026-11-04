#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 交通工具（jiaotong）第 2 段插画（10 卡：tricycle~wheel）。

每卡造型要点：tricycle 前一大后二小三轮 / motorcycle 摩托车把挂头盔 / truck 白货箱蓝车头 /
fire truck 红消防车云梯斜架+水带卷 / ambulance 白救护车红十字双警灯 / tractor 大后轮小前轮绿机车 /
excavator 黄挖掘机履带+大铲斗三齿 / hot air balloon 红黄条纹气球吊篮 / traffic light 红灯亮黄绿暗 /
wheel 大车轮八辐条+胎纹块。
主体居中放大，主色相邻错开；只画图形不画任何文字。
"""
import math
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "tricycle", "cn": "三轮车"},
    {"w": "motorcycle", "cn": "摩托车"},
    {"w": "truck", "cn": "卡车"},
    {"w": "fire truck", "cn": "消防车"},
    {"w": "ambulance", "cn": "救护车"},
    {"w": "tractor", "cn": "拖拉机"},
    {"w": "excavator", "cn": "挖掘机"},
    {"w": "hot air balloon", "cn": "热气球"},
    {"w": "traffic light", "cn": "红绿灯"},
    {"w": "wheel", "cn": "轮子"},
]


# ---------- 本组同族补充色 ----------
GLASS = "#bfe0f2"                                              # 车窗玻璃（WBLUE 族浅）
MET, MET_M, MET_L = "#dfe3e6", "#c9cdd1", "#eef1f3"            # 金属浅灰族
MET_D = "#adb2b7"                                              # 金属灰中
TIRE = "#565b62"                                               # 深灰（金属族深）
CAR_L = "#f2917a"                                              # 红高光（RED 族浅）
GRN_D = "#699756"                                              # 机车深绿（GREEN 族深）
YEL_DIM = "#b58a24"                                            # 暗黄（YEL 族深）
GRN_DIM = "#4d7d49"                                            # 暗绿（GREEN 族深）
TREAD = "#8a9096"                                              # 胎纹灰（金属族中）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色高光椭圆（可旋转）。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


def wheel(cx, cy, r):
    """车轮：黑胎+灰毂+六辐条。"""
    g = C(cx, cy, r, INK) + C(cx, cy, r * 0.8, PAGE) + C(cx, cy, 13, MET_D)
    for i in range(6):
        a = i * math.pi / 3
        g += L(cx + 13 * math.cos(a), cy + 13 * math.sin(a),
               cx + r * 0.77 * math.cos(a), cy + r * 0.77 * math.sin(a), MET_M, 3.5)
    return g


def road_wheel(cx, cy, r):
    """实心宽车轮（货车）：黑胎+深灰圈+亮毂。"""
    return C(cx, cy, r, INK) + C(cx, cy, r * 0.56, TIRE) + C(cx, cy, r * 0.24, MET_L)


# ---------- 1 tricycle 前一大后二小 ----------
def art_tricycle():
    g = ground()
    g += wheel(230, 400, 44) + wheel(330, 400, 44)              # 后双轮（小）
    g += wheel(500, 388, 62)                                    # 前轮（大）
    g += L(500, 388, 486, 292, MET_D, 11)                       # 前叉
    g += L(466, 282, 512, 276, INK, 10)                         # 把横
    g += C(462, 282, 9, RED) + C(516, 276, 9, RED)              # 把手球
    g += L(486, 296, 318, 366, RED, 11)                         # 大梁
    g += R(280, 322, 76, 20, 9, RED)                            # 座椅
    g += R(272, 294, 18, 32, 8, RED_D)                          # 椅背
    g += L(500, 388, 524, 412, MET_D, 8)                        # 前轮脚踏曲柄
    g += R(514, 408, 26, 11, 4, INK)                            # 踏板
    g += C(478, 286, 8, SUN)                                    # 车铃
    return g


# ---------- 2 motorcycle 把上挂头盔 ----------
def art_motorcycle():
    g = ground()
    g += wheel(236, 392, 54) + wheel(536, 392, 54)              # 双轮
    g += L(236, 392, 344, 350, RED, 11)                         # 后车架
    g += L(344, 350, 500, 296, RED, 11)                         # 前车架
    g += L(536, 392, 500, 296, MET_D, 13)                       # 前叉
    g += L(482, 290, 516, 280, INK, 10)                         # 把手
    g += L(516, 280, 534, 258, MET_D, 6)                        # 后视镜杆
    g += C(538, 252, 9, MET_M)                                  # 镜面
    g += '<g transform="rotate(-8 330 330)">' + E(330, 330, 74, 40, RED) + "</g>"   # 油箱
    g += P("M 248 318 Q 300 300 358 306 L 398 318 Q 398 334 380 336 L 262 336 "
           "Q 244 330 248 318 Z", INK)                          # 座椅
    g += PG([(250, 334), (222, 360), (260, 356)], RED)          # 尾裙
    g += R(320, 338, 110, 42, 10, MET_D)                        # 发动机箱
    g += R(296, 362, 160, 20, 10, MET_M)                        # 排气管
    g += E(458, 372, 9, 10, MET_D)
    g += L(524, 288, 534, 296, INK, 4)                          # 头盔挂带
    g += C(548, 306, 23, SUN)                                   # 挂着的安全帽
    g += E(545, 300, 14, 9, GLASS)
    g += C(540, 296, 5, WHITE)
    return g


# ---------- 3 truck 白货箱蓝车头 ----------
def art_truck():
    g = ground()
    g += R(140, 252, 320, 150, 14, WHITE)                       # 货箱
    g += L(300, 252, 300, 400, "#e6dfcf", 6)                    # 箱门缝
    g += R(140, 342, 320, 22, 0, TEAL)                          # 箱身色带
    g += R(140, 400, 480, 18, 8, MET_D)                         # 底盘
    g += R(470, 268, 150, 134, 16, BLUE)                        # 驾驶室
    g += R(494, 288, 62, 46, 8, GLASS)                          # 驾驶窗
    g += C(606, 380, 9, SUN)                                    # 前灯
    g += road_wheel(240, 420, 34) + road_wheel(320, 420, 34) + road_wheel(548, 420, 34)
    return g


# ---------- 4 fire truck 云梯斜架 ----------
def art_firetruck():
    g = ground()
    g += L(206, 252, 566, 162, MET_M, 10)                       # 云梯纵梁一
    g += L(206, 270, 566, 180, MET_M, 10)                       # 云梯纵梁二
    for i in range(7):                                          # 梯级
        x = 234 + i * 48
        y = 252 - 0.25 * (x - 206)
        g += L(x, y, x, y + 18, MET_D, 7)
    g += L(566, 162, 584, 296, MET_D, 8)                        # 梯支撑
    g += R(150, 296, 400, 118, 16, RED)                         # 车身
    g += R(150, 322, 400, 16, 8, WHITE, 0.6)                    # 白条
    g += C(430, 372, 20, WHITE) + C(430, 372, 10, "#e6dfcf")    # 水带卷
    g += R(320, 280, 60, 18, 8, RED_D)                          # 警灯座
    g += C(350, 274, 10, SUN)                                   # 顶警灯
    g += R(550, 272, 110, 142, 16, RED)                         # 驾驶室
    g += R(572, 292, 56, 44, 8, GLASS)
    g += C(644, 388, 9, SUN)
    g += road_wheel(240, 420, 34) + road_wheel(330, 420, 34) + road_wheel(580, 420, 34)
    return g


# ---------- 5 ambulance 白车身红十字 ----------
def art_ambulance():
    g = ground()
    g += R(140, 270, 350, 146, 18, WHITE)                       # 车厢
    g += R(282, 312, 66, 22, 6, RED)                            # 红十字横
    g += R(304, 290, 22, 66, 6, RED)                            # 红十字竖
    g += R(140, 386, 480, 14, 7, BLUE)                          # 腰条
    g += R(490, 300, 130, 116, 16, WHITE)                       # 驾驶室
    g += R(512, 320, 58, 44, 8, GLASS)
    g += R(298, 250, 42, 20, 8, RED)                            # 警灯红
    g += R(348, 250, 42, 20, 8, BLUE)                           # 警灯蓝
    g += R(140, 402, 480, 16, 8, MET_D)                         # 底盘
    g += road_wheel(230, 420, 34) + road_wheel(560, 420, 34)
    return g


# ---------- 6 tractor 大后轮小前轮 ----------
def art_tractor():
    g = ground()
    g += C(268, 390, 78, INK) + C(268, 390, 60, TIRE) + C(268, 390, 22, YEL_D)   # 大后轮
    for i in range(6):
        a = i * math.pi / 3
        g += L(268 + 10 * math.cos(a), 390 + 10 * math.sin(a),
               268 + 56 * math.cos(a), 390 + 56 * math.sin(a), INK, 5)
    g += C(540, 414, 40, INK) + C(540, 414, 27, TIRE) + C(540, 414, 10, MET_D)   # 小前轮
    g += P("M 192 378 Q 268 302 344 378 L 344 398 Q 268 326 192 398 Z", GRN_D)   # 后挡泥板
    g += R(452, 344, 152, 58, 14, GREEN)                        # 机盖
    g += R(330, 258, 110, 122, 14, GREEN)                       # 驾驶室
    g += R(346, 274, 78, 44, 8, GLASS)
    g += R(320, 246, 130, 20, 9, GRN_D)                         # 棚顶
    g += R(348, 226, 18, 34, 7, INK)                            # 烟囱
    g += cloud_p(360, 216, 0.4, "#e6dfcf")                      # 烟
    g += E(304, 302, 20, 10, INK)                               # 座椅
    g += C(592, 366, 9, SUN)                                    # 前灯
    return g


# ---------- 7 excavator 履带+大铲斗 ----------
def art_excavator():
    g = ground()
    g += R(180, 396, 300, 56, 26, TIRE)                         # 履带底座
    for i in range(4):
        g += C(220 + i * 72, 424, 17, INK)                      # 履带轮
    g += R(210, 330, 240, 72, 16, SUN)                          # 车体
    g += R(230, 268, 90, 66, 12, SUN)                           # 驾驶室
    g += R(244, 282, 62, 40, 8, GLASS)
    g += P("M 428 352 L 562 296", stroke=YEL_D, w=22)           # 大臂
    g += L(452, 398, 524, 330, MET_D, 9)                        # 液压杆
    g += P("M 562 296 L 632 372", stroke=YEL_D, w=20)           # 小臂
    g += P("M 610 360 L 678 352 Q 692 354 690 368 L 678 408 Q 674 424 656 420 "
           "L 620 406 Q 608 400 610 388 Z", YEL_D)              # 铲斗
    g += PG([(622, 412), (630, 432), (640, 410)], YEL_D)        # 斗齿
    g += PG([(646, 408), (654, 428), (664, 406)], YEL_D)
    g += PG([(668, 402), (676, 420), (686, 400)], YEL_D)
    return g


# ---------- 8 hot air balloon 条纹气球吊篮 ----------
def art_balloon():
    g = ground()
    g += cloud_p(566, 200, 0.6, WHITE)                          # 云
    g += cloud_p(180, 244, 0.5, WHITE)
    g += P("M 230 262 Q 230 146 380 102 Q 530 146 530 262 Q 530 334 452 354 "
           "L 308 354 Q 230 334 230 262 Z", RED)                # 球体
    g += P("M 232 238 Q 300 276 380 276 Q 460 276 528 238 Q 530 252 529 264 "
           "Q 460 322 380 322 Q 300 322 231 264 Q 230 252 232 238 Z", SUN)   # 黄横带
    g += shine(300, 180, 34, 60, CAR_L, 0.5, 12)
    g += PG([(330, 354), (430, 354), (414, 378), (346, 378)], RED_D)   # 球颈
    g += L(346, 378, 356, 410, INK, 5)                          # 吊绳
    g += L(414, 378, 404, 410, INK, 5)
    g += R(338, 410, 84, 52, 10, WOOD)                          # 吊篮
    g += L(338, 426, 422, 426, WOOD_D, 5)
    g += L(338, 442, 422, 442, WOOD_D, 5)
    return g


# ---------- 9 traffic light 红亮黄绿暗 ----------
def art_trafficlight():
    g = ground()
    g += R(320, 96, 120, 210, 22, TIRE)                         # 灯箱
    g += C(380, 138, 46, RED, 0.25)                             # 红灯光晕（当前亮）
    g += C(380, 138, 34, RED)
    g += C(366, 124, 9, WHITE, 0.7)
    g += C(380, 202, 34, YEL_DIM)                               # 黄灯（暗）
    g += E(380, 206, 14, 10, "#93701c", 0.6)
    g += C(380, 266, 34, GRN_DIM)                               # 绿灯（暗）
    g += E(380, 270, 14, 10, "#3a6340", 0.6)
    g += R(366, 306, 28, 122, 10, MET_D)                        # 灯杆
    g += R(346, 426, 68, 18, 8, MET_D)                          # 底座
    return g


# ---------- 10 wheel 大车轮辐条清楚 ----------
def art_wheel():
    g = ground()
    g += C(380, 320, 150, INK)                                  # 轮胎
    g += C(380, 320, 132, TIRE)
    g += C(380, 320, 104, MET_M)                                # 轮辋
    g += C(380, 320, 96, MET_L)
    for i in range(8):                                          # 八辐条
        a = i * math.pi / 4
        g += L(380 + 16 * math.cos(a), 320 + 16 * math.sin(a),
               380 + 94 * math.cos(a), 320 + 94 * math.sin(a), MET_D, 10)
    g += C(380, 320, 20, MET_D)                                 # 毂
    g += C(380, 320, 9, MET_L)
    for i in range(12):                                         # 胎纹块
        g += f'<g transform="rotate({i * 30} 380 320)">' + R(372, 174, 16, 18, 4, TREAD) + "</g>"
    return g


def arts():
    return {
        "tricycle": art_tricycle(),
        "motorcycle": art_motorcycle(),
        "truck": art_truck(),
        "fire truck": art_firetruck(),
        "ambulance": art_ambulance(),
        "tractor": art_tractor(),
        "excavator": art_excavator(),
        "hot air balloon": art_balloon(),
        "traffic light": art_trafficlight(),
        "wheel": art_wheel(),
    }
