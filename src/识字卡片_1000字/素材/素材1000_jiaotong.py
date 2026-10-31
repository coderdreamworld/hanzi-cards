#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交通出行组 15 卡插画与文案（1000 字批次 B5）。

字表（与字库1000 jiaotong 组一致）：
轮 帆 道 停 票 轨 舵 锚 舱 翼 汽 划 港 机 桨。

画法约定（交通类，车辆侧视图完整可辨；不画车祸危险场景）：
轮=大车轮特写（胎面+辐条+转动弧线）；帆=蓝船身+橙条纹大帆（区别 legacy 白帆木船）；
道=柏油路+斑马线+中线虚线；停=圆形红边斜杠禁停牌；票=两张彩色车票（色块图案无字）；
轨=铁轨+枕木透视图；舵=木质船舵轮盘；锚=铁链+船锚+海床；
舱=太空舱+舱窗+火焰+星星；翼=机翼+翼尖小翼+发动机+云；
汽=蒸汽机车烟囱冒白汽；划=划艇上小孩双手双桨；港=码头+吊机吊货柜+货船；
机=飞机整体侧视；桨=木桨桨叶入水+涟漪。图上无文字数字。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
STEEL, STEEL_L, STEEL_D = "#8f959c", "#b9bec4", "#7c8288"   # 钢轨/路面
DARK, DARK_L = "#4a4f55", "#c9cdd1"                          # 车轮/烟囱
SILVER = "#dfe3e6"
GRAVEL, GRAVEL_D = "#dccca9", "#c4b18a"                      # 道砟
LOCO, LOCO_D = "#6b9459", "#5e854f"                          # 蒸汽机车
ANCH, ANCH_D = "#7a8a96", "#5f6d78"                          # 船锚
CLOUD = "#e8edf0"                                            # 云/白汽
ORG, ORG_D = "#f2a44c", "#d98a2b"                            # 车票/吊机
CAPS = "#e9eef1"                                             # 太空舱
STR_WHITE = "#fdfdfa"                                        # 纯白（斑马线/舷窗等）


# ---------- 轮 ----------
def a_lun():
    """轮：大车轮特写（胎面+辐条+转动弧线）。"""
    g = ground()
    g += C(380, 270, 170, DARK)                               # 轮胎
    g += C(380, 270, 120, SILVER)                             # 轮辋
    for i in range(12):                                       # 胎面花纹
        a = i * math.pi / 6
        g += C(380 + 145 * math.cos(a), 270 + 145 * math.sin(a), 9, "#454a4f")
    for i in range(6):                                        # 辐条
        a = i * math.pi / 3
        g += L(380 + 46 * math.cos(a), 270 + 46 * math.sin(a),
               380 + 110 * math.cos(a), 270 + 110 * math.sin(a), STEEL_L, 13)
    g += C(380, 270, 44, YEL)                                 # 轮毂
    g += C(380, 270, 15, YEL_D)
    g += C(376, 266, 4, STR_WHITE)
    g += P("M 588 320 Q 606 270 588 220", stroke=TEAL_L, w=7)  # 转动弧线
    g += P("M 624 340 Q 648 270 624 200", stroke=TEAL_L, w=7, opacity=0.7)
    return g


# ---------- 帆 ----------
def a_fan():
    """帆：蓝船身帆船，橙条纹大帆。"""
    g = ground()
    g += E(380, 416, 256, 28, WBLUE)
    g += R(372, 116, 14, 224, 7, WOOD_D)                      # 桅杆
    g += P("M 396 136 Q 522 238 530 330 L 396 330 Z", ORG)    # 主帆
    g += P("M 400 158 Q 496 226 514 330", stroke=STR_WHITE, w=8, opacity=0.7)
    g += P("M 404 196 Q 470 248 492 330", stroke=STR_WHITE, w=10, opacity=0.85)
    g += P("M 366 162 L 366 330 L 284 330 Z", STR_WHITE)      # 前帆
    g += R(390, 330, 148, 12, 6, WOOD_D)                      # 帆桁
    g += PG([(379, 108), (421, 118), (379, 130)], RED)        # 小旗
    g += R(208, 336, 344, 16, 8, BLUE_D)                      # 船舷
    g += P("M 212 350 L 548 350 L 506 404 Q 380 420 254 404 Z", BLUE)
    g += C(310, 376, 9, STR_WHITE) + C(380, 378, 9, STR_WHITE) + C(450, 376, 9, STR_WHITE)
    g += P("M 200 430 Q 240 438 280 430", stroke="#a5d9f0", w=5)
    g += P("M 470 432 Q 510 440 550 432", stroke="#a5d9f0", w=5)
    return g


# ---------- 道 ----------
def a_dao():
    """道：柏油大马路+中线虚线+斑马线。"""
    g = ground()
    g += R(40, 282, 680, 16, 8, "#9cc98a")                    # 路缘草带
    g += R(40, 296, 680, 132, 20, STEEL)                      # 柏油路面
    g += R(40, 296, 680, 18, 9, STEEL_D)
    for x in (80, 180, 280, 380):                             # 中线虚线
        g += R(x, 354, 70, 13, 6, STR_WHITE)
    for x in (500, 558, 616, 674):                            # 斑马线
        g += R(x, 304, 42, 116, 8, STR_WHITE)
    return g


# ---------- 停 ----------
def a_ting():
    """停：圆形红边斜杠禁停牌。"""
    g = ground()
    g += R(368, 214, 24, 216, 10, STEEL)                      # 牌杆
    g += E(380, 434, 42, 11, STEEL_D)
    g += C(380, 152, 106, RED)                                # 红边
    g += C(380, 152, 88, STR_WHITE)
    g += L(330, 206, 430, 98, RED, 26)                        # 斜杠
    return g


# ---------- 票 ----------
def a_piao():
    """票：两张彩色车票（色块+星星/爱心图案，无字）。"""
    g = ground()
    g += E(380, 442, 230, 13, INK, 0.07)
    t1 = wrap(
        R(-130, -84, 260, 168, 18, TEAL),
        C(-130, 0, 16, PAGE) + C(130, 0, 16, PAGE),           # 撕票孔
        f'<line x1="0" y1="-84" x2="0" y2="84" stroke="#7cc8bb" stroke-width="5" '
        f'stroke-dasharray="12 14"/>',
        star5(-62, 0, 24, "#f9c95e"),
        C(62, -22, 15, STR_WHITE) + C(62, 24, 15, "#a5d9f0"))
    t2 = wrap(
        R(-130, -84, 260, 168, 18, ORG),
        C(-130, 0, 16, PAGE) + C(130, 0, 16, PAGE),
        f'<line x1="0" y1="-84" x2="0" y2="84" stroke="#d98a2b" stroke-width="5" '
        f'stroke-dasharray="12 14"/>',
        heart(-62, 0, 22, STR_WHITE),
        C(62, -22, 15, STR_WHITE) + C(62, 24, 15, "#f7c95e"))
    g += f'<g transform="translate(258,300) rotate(-8)">{t1}</g>'
    g += f'<g transform="translate(508,316) rotate(6)">{t2}</g>'
    return g


# ---------- 轨 ----------
def a_gui():
    """轨：铁轨+枕木（透视伸向远方）。"""
    g = ground()
    g += P("M 196 454 L 564 454 L 474 122 L 286 122 Z", GRAVEL)   # 道砟
    g += C(240, 420, 6, GRAVEL_D) + C(320, 300, 5, GRAVEL_D)
    g += C(470, 380, 6, GRAVEL_D) + C(430, 200, 5, GRAVEL_D)
    ties = [(406, 26, 236, 262), (352, 21, 180, 290), (306, 17, 140, 310),
            (266, 14, 110, 325), (232, 11, 86, 337), (202, 9, 68, 346),
            (176, 7, 54, 353)]
    for i, (y, h, w, x) in enumerate(ties):                   # 枕木
        g += R(x, y - h, w, h, h / 2, WOOD_D if i % 2 else WOOD)
    g += PG([(292, 430), (334, 430), (372, 128), (360, 128)], "#cfd5da")  # 左轨
    g += PG([(426, 430), (468, 430), (400, 128), (388, 128)], "#cfd5da")  # 右轨
    g += L(334, 424, 371, 134, STEEL, 5)
    g += L(426, 424, 389, 134, STEEL, 5)
    return g


# ---------- 舵 ----------
def a_duo():
    """舵：木质船舵轮盘（一圈握把）。"""
    g = ground()
    g += E(380, 452, 200, 14, INK, 0.08)
    for i in range(8):                                        # 握把辐条
        a = i * math.pi / 4
        x2, y2 = 380 + 186 * math.cos(a), 260 + 186 * math.sin(a)
        g += L(380 + 30 * math.cos(a), 260 + 30 * math.sin(a), x2, y2, WOOD_D, 15)
        g += C(x2, y2, 13, "#8a5a33")
    g += C(380, 260, 152, WOOD_D)                             # 轮盘
    g += C(380, 260, 108, PAGE)                               # 盘心镂空
    g += C(380, 260, 42, WOOD_L)                              # 轮毂
    g += C(380, 260, 15, "#8a5a33")
    g += P("M 288 172 A 128 128 0 0 1 400 122", stroke=WOOD, w=9)
    return g


# ---------- 锚 ----------
def a_mao2():
    """锚：铁链+船锚落在海床上。"""
    g = ground()
    g += E(380, 418, 190, 17, "#dcd0b4")                      # 海床沙
    g += E(380, 84, 15, 11, ANCH)                             # 铁链
    g += E(380, 62, 12, 9, "#8d9aa5")
    g += C(380, 146, 34, ANCH)                                # 锚环
    g += C(380, 146, 16, PAGE)
    g += R(363, 172, 34, 218, 15, ANCH)                       # 锚杆
    g += R(294, 200, 172, 26, 12, ANCH_D)                     # 锚横杆
    g += P("M 246 292 Q 258 372 380 380 Q 502 372 514 292", stroke=ANCH, w=30)
    g += PG([(268, 292), (222, 262), (234, 322)], ANCH_D)     # 左锚爪
    g += PG([(492, 292), (538, 262), (526, 322)], ANCH_D)     # 右锚爪
    g += L(374, 182, 374, 350, "#9aa8b2", 6)                  # 高光
    return g


# ---------- 舱 ----------
def a_cang():
    """舱：矮胖太空返回舱（双舱窗+隔热底+落地腿+火焰+星星）。"""
    g = ground()
    for cx, cy, r, f, o in [(180, 150, 20, SUN, None), (580, 190, 14, "#f9c95e", None),
                            (620, 300, 10, "#f9c95e", 0.9), (240, 240, 5, SUN_L, 0.8),
                            (540, 120, 6, SUN_L, 0.8), (160, 300, 5, SUN_L, 0.7)]:
        if r >= 10:
            g += star5(cx, cy, r, f)
        else:
            g += C(cx, cy, r, f, o)
    g += L(380, 118, 380, 88, STEEL, 6)                       # 天线
    g += C(380, 84, 10, RED)
    g += PG([(340, 414), (420, 414), (380, 458)], SUN)        # 火焰
    g += PG([(358, 414), (402, 414), (380, 442)], RED)
    g += P("M 380 118 Q 262 150 254 268 Q 250 340 284 396 L 476 396 "
           "Q 510 340 506 268 Q 498 150 380 118 Z", CAPS)     # 矮胖舱体
    g += P("M 380 118 Q 330 130 316 176 Q 380 196 444 176 Q 430 130 380 118 Z", RED)  # 舱顶
    g += P("M 286 260 Q 284 320 300 368", stroke=STR_WHITE, w=10, opacity=0.7)        # 高光
    g += C(338, 300, 34, BLUE_D)                              # 左舱窗
    g += C(338, 300, 26, "#a5d9f0")
    g += C(328, 290, 7, STR_WHITE, 0.9)
    g += C(422, 300, 34, BLUE_D)                              # 右舱窗
    g += C(422, 300, 26, "#a5d9f0")
    g += C(412, 290, 7, STR_WHITE, 0.9)
    g += R(266, 392, 16, 34, 7, STEEL)                        # 落地腿
    g += R(478, 392, 16, 34, 7, STEEL)
    g += P("M 280 396 L 480 396 Q 474 424 380 426 Q 286 424 280 396 Z", DARK_L)  # 隔热底
    return g


# ---------- 翼 ----------
def a_yi():
    """翼：机身中段+宽大后掠机翼特写（翼尖小翼+发动机+云）。"""
    g = ground()
    g += cloud_p(620, 120, 0.8, CLOUD)
    g += cloud_p(150, 150, 0.6, CLOUD)
    g += R(64, 196, 232, 150, 40, "#e8eef3")                  # 机身中段
    g += P("M 64 300 Q 180 322 296 306 L 296 330 Q 180 348 64 336 Z",
           "#c9d8e2", 0.8)                                    # 机腹影
    g += C(150, 246, 13, BLUE) + C(210, 250, 13, BLUE)        # 舷窗
    g += P("M 280 268 Q 500 320 636 372 L 662 424 L 280 344 Z", "#a8d4f0")  # 宽机翼
    g += L(282, 268, 640, 374, BLUE, 12)                      # 前缘
    g += P("M 420 320 Q 520 348 610 384 L 600 404 Q 508 370 412 342 Z",
           "#c2e2f4")                                         # 后缘襟翼
    g += PG([(612, 372), (662, 422), (700, 352), (652, 336)], RED)      # 翼尖小翼
    g += P("M 640 378 L 690 348", stroke=RED_D, w=7)
    eng = wrap(
        R(-58, -30, 132, 62, 31, DARK_L),                     # 发动机吊舱
        E(-54, 0, 17, 31, STEEL_D),
        E(-48, 0, 9, 21, DARK))
    g += f'<g transform="translate(452,392) rotate(13)">{eng}</g>'
    return g


# ---------- 汽 ----------
def a_qi():
    """汽：蒸汽机车，烟囱冒白汽。"""
    g = ground()
    g += C(250, 120, 24, CLOUD) + C(296, 88, 32, CLOUD)       # 白汽
    g += C(356, 66, 40, CLOUD) + C(424, 52, 30, CLOUD, 0.85)
    g += C(288, 108, 14, STR_WHITE, 0.9) + C(360, 82, 18, STR_WHITE, 0.9)
    g += C(238, 384, 42, DARK) + C(356, 384, 42, DARK) + C(470, 384, 34, DARK)
    g += C(238, 384, 18, DARK_L) + C(356, 384, 18, DARK_L) + C(470, 384, 14, DARK_L)
    g += L(238, 396, 356, 396, "#aab0b6", 9)                  # 连杆
    g += PG([(128, 414), (172, 338), (194, 348), (160, 420)], YEL_D)  # 排障器
    g += R(170, 238, 240, 104, 34, LOCO)                      # 锅炉
    g += R(210, 238, 14, 104, 4, LOCO_D) + R(300, 238, 14, 104, 4, LOCO_D) \
         + R(380, 238, 14, 104, 4, LOCO_D)
    g += E(320, 240, 26, 17, "#8fae7f")                       # 汽包
    g += C(178, 262, 12, YEL)                                 # 车灯
    g += R(400, 168, 140, 178, 16, LOCO)                      # 司机室
    g += R(390, 156, 160, 26, 12, LOCO_D)                     # 顶棚
    g += R(428, 196, 84, 58, 12, "#a5d9f0")                   # 车窗
    g += R(212, 158, 50, 84, 14, DARK)                        # 烟囱
    g += E(237, 156, 36, 13, DARK)
    return g


# ---------- 划 ----------
def a_hua():
    """划：小孩坐划艇，双手双桨划水。"""
    g = ground()
    g += E(380, 424, 264, 32, WBLUE)
    g += kid(380, 428, s=0.62, pose="sit", shirt=RED)         # 坐进艇里
    g += P("M 150 372 Q 380 336 610 372 Q 560 424 380 430 "
           "Q 200 424 150 372 Z", WOOD)                       # 划艇
    g += P("M 150 372 Q 380 336 610 372 L 596 388 Q 380 356 164 388 Z", WOOD_D)
    g += L(240, 402, 268, 408, "#a9743f", 4) + L(470, 404, 498, 398, "#a9743f", 4)
    g += L(352, 344, 340, 338, SKIN, 11)                      # 小臂
    g += L(408, 344, 420, 338, SKIN, 11)
    g += L(338, 336, 240, 414, WOOD_D, 11)                    # 左桨
    g += L(422, 336, 520, 414, WOOD_D, 11)                    # 右桨
    g += f'<g transform="rotate(-38 232 424)">{E(232, 424, 19, 33, WOOD_L)}</g>'
    g += f'<g transform="rotate(38 528 424)">{E(528, 424, 19, 33, WOOD_L)}</g>'
    g += C(338, 336, 13, SKIN) + C(422, 336, 13, SKIN)        # 握桨的手
    g += P("M 196 434 Q 232 444 268 434", stroke="#a5d9f0", w=5)
    g += P("M 492 436 Q 528 446 564 436", stroke="#a5d9f0", w=5)
    return g


# ---------- 港 ----------
def a_gang():
    """港：码头+吊机吊货柜，货船停泊。"""
    g = ground()
    g += E(380, 416, 300, 32, WBLUE)
    g += R(440, 330, 250, 38, 10, WOOD)                       # 码头
    g += R(476, 368, 24, 50, 8, WOOD_D) + R(640, 368, 24, 50, 8, WOOD_D)
    g += L(480, 334, 480, 364, "#a9743f", 4) + L(540, 334, 540, 364, "#a9743f", 4) \
         + L(600, 334, 600, 364, "#a9743f", 4) + L(660, 334, 660, 364, "#a9743f", 4)
    g += R(70, 350, 230, 14, 7, BLUE_D)                       # 货船
    g += P("M 70 356 L 300 356 L 268 404 Q 180 418 96 400 Z", BLUE)
    g += R(120, 314, 60, 34, 6, ORG) + R(184, 314, 60, 34, 6, TEAL)  # 甲板货柜
    g += C(150, 380, 9, STR_WHITE) + C(200, 380, 9, STR_WHITE) + C(250, 380, 9, STR_WHITE)
    g += R(540, 190, 48, 140, 8, ORG_D)                       # 吊机塔身
    g += R(528, 152, 72, 42, 10, YEL)                         # 吊机驾驶室
    g += R(420, 152, 220, 24, 10, YEL)                        # 吊臂
    g += R(588, 152, 80, 20, 8, ORG_D)                        # 配重
    g += L(564, 112, 534, 154, ORG_D, 9) + L(564, 112, 594, 154, ORG_D, 9)
    g += L(564, 112, 436, 154, "#b57b44", 5) + L(564, 112, 654, 154, "#b57b44", 5)
    g += L(456, 176, 456, 258, STEEL, 5)                      # 吊缆
    g += R(432, 258, 48, 10, 4, STEEL)
    g += R(424, 268, 64, 44, 6, TEAL)                         # 吊起的货柜
    g += L(440, 272, 440, 308, "#3e9486", 4) + L(456, 272, 456, 308, "#3e9486", 4) \
         + L(472, 272, 472, 308, "#3e9486", 4)
    g += P("M 320 428 Q 360 436 400 428", stroke="#a5d9f0", w=5)
    return g


# ---------- 机 ----------
def a_ji():
    """机：飞机整体侧视（尾翼+双翼+舷窗）。"""
    g = ground()
    g += cloud_p(640, 140, 0.9, CLOUD)
    g += PG([(300, 240), (214, 178), (272, 174), (360, 236)], BLUE_D)  # 远翼
    g += E(350, 286, 226, 66, "#e8eef3")                      # 机身
    g += E(350, 304, 220, 42, "#c9d8e2", 0.7)                 # 机腹
    g += P("M 158 250 L 96 142 L 172 142 Q 200 190 220 252 Z", RED)    # 尾翼
    g += P("M 176 268 L 92 246 L 176 232 Z", RED_D)           # 尾平翼
    g += P("M 540 252 Q 578 254 596 272 Q 566 282 536 272 Z", "#a5d9f0")  # 驾驶舱
    for i in range(6):                                        # 舷窗
        g += C(250 + i * 54, 278, 11, BLUE)
    g += R(486, 262, 20, 34, 8, "#c9d8e2")                    # 舱门
    g += PG([(350, 318), (238, 414), (326, 414), (442, 320)], BLUE)    # 近翼
    g += E(300, 398, 30, 17, DARK_L)                          # 发动机
    g += C(594, 286, 8, RED)                                  # 机头灯
    return g


# ---------- 桨 ----------
def a_jiang():
    """桨：木桨桨叶划入水中，泛起涟漪。"""
    g = ground()
    g += E(380, 412, 250, 32, WBLUE)
    g += L(552, 156, 316, 380, WOOD, 20)                      # 桨杆
    g += R(296, 366, 44, 26, 12, WOOD_D)                      # 桨领
    g += P("M 318 378 Q 282 424 312 450 Q 348 468 372 430 L 350 370 Z", WOOD_L)  # 桨叶
    g += P("M 336 386 Q 318 416 336 442", stroke=WOOD_D, w=6)
    g += hand(556, 162, rot=-52, s=0.52)                      # 握桨的手
    g += E(330, 436, 130, 24, WBLUE, 0.55)                    # 水面盖住桨叶下段
    g += P("M 240 416 Q 300 400 372 414", stroke=STR_WHITE, w=6)
    g += P("M 300 446 Q 352 460 410 448", stroke="#a5d9f0", w=5)
    return g


def arts():
    return {
        "轮": a_lun(), "帆": a_fan(), "道": a_dao(), "停": a_ting(),
        "票": a_piao(), "轨": a_gui(), "舵": a_duo(), "锚": a_mao2(),
        "舱": a_cang(), "翼": a_yi(), "汽": a_qi(), "划": a_hua(),
        "港": a_gang(), "机": a_ji(), "桨": a_jiang(),
    }


GROUP_CARDS = [
    {"char": "轮", "pinyin": "lún", "tone": "第二声",
     "sentence": "车轮滚滚转得快。",
     "say": "圆圆会转的是轮子。",
     "chat": "“家里哪些东西有轮子？”",
     "life": "推推玩具车看轮子转。"},
    {"char": "帆", "pinyin": "fān", "tone": "第一声",
     "sentence": "帆船张起大帆跑。",
     "say": "风推着大帆，船就前进。",
     "chat": "“没有风的时候帆怎么走？”",
     "life": "叠一只纸帆船玩玩。"},
    {"char": "道", "pinyin": "dào", "tone": "第四声",
     "sentence": "笔直大道通远方。",
     "say": "又长又直的大路叫大道。",
     "chat": "“马路中间的白线干什么用？”",
     "life": "散步时走一走斑马线。"},
    {"char": "停", "pinyin": "tíng", "tone": "第二声",
     "sentence": "看见停牌停一停。",
     "say": "红圈红杠是停牌，要停下。",
     "chat": "“什么时候汽车要停下？”",
     "life": "玩红绿灯游戏，喊停就停。"},
    {"char": "票", "pinyin": "piào", "tone": "第四声",
     "sentence": "两张车票拿在手。",
     "say": "上车前要先买的车票。",
     "chat": "“车票上画着什么图案？”",
     "life": "把车票交给他保管。"},
    {"char": "轨", "pinyin": "guǐ", "tone": "第三声",
     "sentence": "长长铁轨伸远方。",
     "say": "火车走的专用道是铁轨。",
     "chat": "“铁轨下面一根根是什么？”",
     "life": "用积木拼一段小铁轨。"},
    {"char": "舵", "pinyin": "duò", "tone": "第四声",
     "sentence": "船舵一转，方向就变。",
     "say": "转船舵就能让船拐弯。",
     "chat": "“舵轮像不像大方向盘？”",
     "life": "抱着他假装掌舵开船。"},
    {"char": "锚", "pinyin": "máo", "tone": "第二声",
     "sentence": "大锚抛下稳稳停。",
     "say": "锚钩住海底，船不漂走。",
     "chat": "“锚为什么要做得重重的？”",
     "life": "绘本里找一找船锚。"},
    {"char": "舱", "pinyin": "cāng", "tone": "第一声",
     "sentence": "太空舱里看星星。",
     "say": "宇航员坐的飞船小屋叫舱。",
     "chat": "“太空舱窗外能看到什么？”",
     "life": "大纸箱当太空舱一起玩。"},
    {"char": "翼", "pinyin": "yì", "tone": "第四声",
     "sentence": "机翼宽宽像大鸟。",
     "say": "飞机两边宽宽的是机翼。",
     "chat": "“机翼像大鸟的什么呀？”",
     "life": "张开手臂学飞机的机翼。"},
    {"char": "汽", "pinyin": "qì", "tone": "第四声",
     "sentence": "蒸汽火车呜呜开。",
     "say": "烧水冒蒸汽，推动火车跑。",
     "chat": "“白汽是从哪里冒出来的？”",
     "life": "看壶嘴冒白汽，说说汽。"},
    {"char": "划", "pinyin": "huá", "tone": "第二声（划另读 huà，如“计划”）",
     "sentence": "小船划呀划。",
     "say": "用桨拨水让船走就是划。",
     "chat": "“两只桨一起划会怎样？”",
     "life": "公园里看人划小船。"},
    {"char": "港", "pinyin": "gǎng", "tone": "第三声",
     "sentence": "大轮船开进港口。",
     "say": "港口是大船装卸货的地方。",
     "chat": "“吊机在把什么吊上船？”",
     "life": "水盆里停泊小船当港口。"},
    {"char": "机", "pinyin": "jī", "tone": "第一声",
     "sentence": "飞机飞上蓝天。",
     "say": "翅膀宽宽能载客的是飞机。",
     "chat": "“飞机的翅膀叫什么呀？”",
     "life": "举起他当小飞机飞一圈。"},
    {"char": "桨", "pinyin": "jiǎng", "tone": "第三声",
     "sentence": "木桨划水哗啦啦。",
     "say": "划水用的长木头是桨。",
     "chat": "“桨叶拍水会怎么样？”",
     "life": "洗澡用小勺当桨划划水。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "jiaotong" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B5"] if e["file"] == "素材1000_jiaotong.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"交通出行组：卡数 {len(GROUP_CARDS)}")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    idx = [ziku_chars.index(ch) for ch in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = set(a) == set(mine)
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    # 划：图与句均为「划船」义，读 huá；机器拼音表默认 huà，按审卡标准以图为准并标注另读。
    POLY = {"划": {"pinyin": "huá", "tone_prefix": "第二声"}}
    bad = []
    for c in GROUP_CARDS:
        ch = c["char"]
        w = py[ch]
        if ch in POLY:
            if c["pinyin"] != POLY[ch]["pinyin"]:
                bad.append((ch, "pinyin", c["pinyin"], POLY[ch]["pinyin"]))
            if not c["tone"].startswith(POLY[ch]["tone_prefix"]):
                bad.append((ch, "tone", c["tone"]))
        else:
            if c["pinyin"] != w["pinyin"]:
                bad.append((ch, "pinyin", c["pinyin"], w["pinyin"]))
            if not (c["tone"] == w["tone"] or c["tone"].startswith(w["tone"] + "（")):
                bad.append((ch, "tone", c["tone"], w["tone"]))
        hanzi = sum(1 for h in c["sentence"] if "\u4e00" <= h <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((ch, "句长", hanzi))
        if ch not in c["sentence"]:
            bad.append((ch, "句缺字"))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((ch, f, len(c[f])))
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
