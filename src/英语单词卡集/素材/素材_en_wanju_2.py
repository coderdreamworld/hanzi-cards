#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 玩具（wanju）第 2 段插画（10 卡：swing~hula hoop）。

每卡造型要点：swing 灰架秋千 kid 坐坐板荡起（身前倾臂上举）/
seesaw 黄支点绿跷板两端各一娃（一低一高） / trampoline 蓝面蹦床 kid 腾空
分腿跳 / bubbles 吹泡棒+一群七彩泡泡（娃 face=o 举棒吹） /
paper plane 白纸飞机折痕+灰色虚线航迹云朵 / pinwheel 红黄青蓝
四叶风车木杆草丛风丝 / drum 红鼓金钉斜绑绳双槌敲击线 / piano 木琴身红毡
黑白琴键一排+音符 / scooter kid 站滑板车手扶 T 把蹬行 /
hula hoop kid 举臂腰间转红青双色圈（后弧在前弧夹身）。kid 全用组件；
主体居中放大，相邻主色错开，每卡第一笔 ground()；无描边无渐变，
图上无文字数字。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "swing", "cn": "秋千"},
    {"w": "seesaw", "cn": "跷跷板"},
    {"w": "trampoline", "cn": "蹦床"},
    {"w": "bubbles", "cn": "泡泡"},
    {"w": "paper plane", "cn": "纸飞机"},
    {"w": "pinwheel", "cn": "风车"},
    {"w": "drum", "cn": "鼓"},
    {"w": "piano", "cn": "钢琴"},
    {"w": "scooter", "cn": "滑板车"},
    {"w": "hula hoop", "cn": "呼啦圈"},
]


# ---------- 本组同族补充色 ----------
STEEL_L = "#c9cdd1"                                         # 运动轨迹浅灰（STEELC 族）
STEEL_D = "#a9b0b7"                                         # 金属深灰
GREY_D = "#46535f"                                          # 深灰（jiaju GREY 族）
STRING = "#8a5a33"                                          # 线绳深棕
ORANGE = "#f0923c"                                          # 暖橙（jiaju 沙发族）
GREEN_D = "#638a56"                                         # 深绿
PINK_L = "#fcc7b2"                                          # 泡泡粉（PINK 族）
PURP_L = "#c0aae0"                                          # 泡泡紫（yanse 紫族）
KEY_B = "#3c444d"                                           # 琴键黑（深灰黑）
SILVER = "#b7bcc2"                                          # 浅银（yanse 灰族）
WOOD_TAN = "#f4d3a4"                                        # 鼓皮浅木（WOOD_L 族）
SOFT = "#e8e4dc"                                            # 纸机下翼折影（STONE 族）
SUN_D = "#d99a2b"                                           # 黄深（SUN 族深，同 YEL_D）


# ---------- 12 swing 灰架秋千，kid 荡起 ----------
def art_swing():
    g = ground()
    # A 字支架×2 + 顶梁
    g += L(210, 172, 158, 440, GREY_D, 15)
    g += L(210, 172, 264, 440, GREY_D, 15)
    g += L(556, 172, 504, 440, GREY_D, 15)
    g += L(556, 172, 612, 440, GREY_D, 15)
    g += L(198, 268, 224, 268, GREY_D, 9)
    g += L(542, 268, 568, 268, GREY_D, 9)
    g += L(200, 168, 566, 168, GREY_D, 18)
    # 吊绳（横梁直落座板两端，全长在娃身侧可见）+ 坐板
    g += L(344, 176, 344, 332, STRING, 7)
    g += L(456, 176, 456, 332, STRING, 7)
    g += R(330, 330, 140, 17, 8, BLUE)
    # 坐上的小朋友（臀部落在坐板上，双手正好抓住两侧吊绳）
    g += kid(400, 383, 0.7, pose="sit", face="open", arms="up", shirt=GREEN)
    # 摆动轨迹弧
    g += P("M 282 246 Q 262 322 282 396", stroke=STEEL_L, w=7)
    g += P("M 518 246 Q 538 322 518 396", stroke=STEEL_L, w=7)
    return g


# ---------- 13 seesaw 黄支点绿板，两端各一娃 ----------
def art_seesaw():
    g = ground()
    # 跷板（左低右高）+ 两端扶手
    g += f'<g transform="rotate(-10 380 379)">{R(180, 366, 400, 26, 12, GREEN_L)}{R(196, 338, 16, 30, 7, BLUE)}{R(548, 338, 16, 30, 7, BLUE)}</g>'
    # 支点（黄色三角 + 顶轴）
    g += PG([(380, 338), (338, 440), (422, 440)], SUN_D)
    g += PG([(380, 344), (348, 438), (412, 438)], SUN)
    g += C(380, 340, 11, SUN_D)
    # 低端小朋友（坐在落地端）
    g += kid(212, 452, 0.75, pose="sit", face="smile", arms="down", shirt=BLUE)
    # 高端小朋友（坐在翘起端，随板微倾，脚悬空）
    g += f'<g transform="rotate(10 556 322)">{kid(556, 382, 0.75, pose="sit", face="open", arms="up", shirt=ORANGE)}</g>'
    return g


# ---------- 14 trampoline 蓝面蹦床，kid 腾空跳 ----------
def art_trampoline():
    g = ground()
    # 支腿（斜撑）+ 护网示意短柱
    g += L(238, 388, 214, 442, GREY_D, 15)
    g += L(522, 388, 546, 442, GREY_D, 15)
    g += L(300, 396, 288, 440, GREY_D, 11)
    g += L(460, 396, 472, 440, GREY_D, 11)
    # 底框护边 + 弹簧
    g += E(380, 368, 202, 46, GREY_D)
    for dx in (-150, -100, -50, 50, 100, 150):
        g += L(380 + dx, 396, 380 + dx * 1.08, 410, STEEL_D, 6)
    # 跳面（绷紧微凹）
    g += E(380, 356, 184, 34, BLUE_D)
    g += P("M 200 352 Q 380 384 560 352 Q 380 368 200 352 Z", BLUE)
    # 腾空的小朋友（分腿跳，臂上举）
    g += kid(380, 212, 0.62, pose="sprint", face="open", arms="up", shirt=RED)
    # 起跳弹力线
    g += P("M 336 268 Q 380 246 424 268", stroke=STEEL_L, w=7)
    g += P("M 348 292 Q 380 276 412 292", stroke=STEEL_L, w=5)
    return g


# ---------- 15 bubbles 吹泡棒 + 一群七彩泡泡 ----------
def art_bubbles():
    g = ground()
    # 吹泡泡的小朋友（o 嘴吹气，一手指向泡泡棒）
    g += kid(300, 432, 0.8, pose="stand", face="o", arms="point",
             point_at=(398, 300), shirt=TEAL)
    # 泡泡棒（杆 + 圈 + 膜）
    g += L(398, 300, 424, 272, "#f0876f", 9)
    g += '<circle cx="442" cy="254" r="23" fill="none" stroke="#f0876f" stroke-width="9"/>'
    g += C(442, 254, 14, WBLUE, 0.5)
    # 七彩泡泡群（各色 + 高光）
    g += C(506, 218, 30, WBLUE, 0.55)
    g += C(496, 206, 9, WHITE, 0.9)
    g += C(566, 172, 22, PINK_L, 0.6)
    g += C(558, 164, 6, WHITE, 0.9)
    g += C(538, 262, 16, SUN_L, 0.6)
    g += C(606, 240, 26, TEAL_L, 0.55)
    g += C(596, 228, 8, WHITE, 0.9)
    g += C(584, 128, 15, PURP_L, 0.55)
    g += C(470, 166, 18, GREEN_L, 0.55)
    g += C(464, 158, 5, WHITE, 0.9)
    g += C(650, 186, 12, BLUE, 0.4)
    return g


# ---------- 16 paper plane 白纸飞机 + 虚线航迹 ----------
def art_paper_plane():
    g = ground()
    # 云两朵
    g += cloud_p(190, 160, 0.75, WHITE)
    g += cloud_p(560, 356, 0.55, WHITE)
    # 虚线航迹（灰，飞向机尾）
    g += ('<path d="M 168 400 Q 240 292 330 330 Q 424 368 446 268 Q 456 232 480 224" '
          'fill="none" stroke="#b7bcc2" stroke-width="7" stroke-linecap="round" '
          'stroke-dasharray="18 16"/>')
    # 纸飞机（上翼 + 折痕 + 下翼）
    g += PG([(566, 152), (392, 232), (444, 264)], WHITE)
    g += PG([(566, 152), (424, 296), (448, 268)], SOFT)
    g += L(566, 152, 448, 268, "#d9d0c5", 5)
    g += PG([(566, 152), (448, 268), (470, 296)], "#d9d0c5")
    # 速度线
    g += L(360, 190, 420, 184, STEEL_L, 6)
    g += L(340, 240, 404, 236, STEEL_L, 5)
    return g


# ---------- 17 pinwheel 红黄青蓝四叶风车 ----------
def art_pinwheel():
    g = ground()
    # 风丝
    g += P("M 236 148 Q 280 158 316 148", stroke="#cfe6f0", w=9)
    g += P("M 220 196 Q 268 206 308 196", stroke="#cfe6f0", w=7)
    # 四叶（风车叶片）
    g += PG([(380, 220), (348, 118), (404, 138)], RED)
    g += PG([(380, 220), (482, 188), (462, 244)], SUN)
    g += PG([(380, 220), (412, 322), (356, 302)], TEAL)
    g += PG([(380, 220), (278, 252), (298, 196)], BLUE)
    # 中心钉
    g += C(380, 220, 17, SUN_D)
    g += C(374, 214, 6, SUN_L)
    # 木杆 + 草丛
    g += R(371, 236, 18, 202, 8, WOOD_D)
    g += L(377, 250, 377, 430, WOOD_L, 4)
    g += E(380, 442, 66, 12, GREEN, 0.5)
    g += L(332, 444, 324, 414, GREEN, 7)
    g += L(348, 446, 344, 418, GREEN_L, 7)
    g += L(420, 444, 428, 414, GREEN, 7)
    g += L(404, 446, 408, 418, GREEN_L, 7)
    return g


# ---------- 18 drum 红鼓金钉斜绳，双槌敲 ----------
def art_drum():
    g = ground()
    # 鼓口沿（深红环）+ 鼓身 + 上面皮
    g += E(380, 272, 118, 40, RED_D)
    g += P("M 268 274 L 268 386 Q 380 428 492 386 L 492 274 Q 380 312 268 274 Z", RED)
    g += E(380, 272, 110, 34, WOOD_TAN)
    g += E(380, 274, 94, 27, "#eac9a0")
    # 鼓身斜绑绳 + 金钉
    g += L(296, 300, 356, 372, SUN_D, 6)
    g += L(340, 296, 402, 380, SUN_D, 6)
    g += L(396, 302, 322, 376, SUN_D, 6)
    g += L(452, 300, 384, 374, SUN_D, 6)
    for cx, cy in ((300, 330), (336, 354), (380, 366), (424, 354), (460, 330)):
        g += C(cx, cy, 8, SUN)
    # 双槌（交叉举在鼓上方）+ 敲击线
    g += L(300, 178, 428, 238, WOOD_L, 14)
    g += C(436, 242, 12, WOOD_D)
    g += L(460, 178, 332, 238, WOOD_L, 14)
    g += C(324, 242, 12, WOOD_D)
    g += P("M 352 258 Q 380 246 408 258", stroke=STEEL_L, w=6)
    g += P("M 366 276 Q 380 268 394 276", stroke=STEEL_L, w=5)
    return g


# ---------- 19 piano 木琴身红毡黑白琴键 + 音符 ----------
def art_piano():
    g = ground()
    # 琴身（木框）+ 内凹键床
    g += R(140, 150, 480, 280, 16, WOOD_D)
    g += R(150, 196, 460, 226, 10, "#5a3d2b")
    # 红毡条
    g += R(158, 200, 444, 20, 8, RED)
    # 白键 12 枚
    for i in range(12):
        g += R(158 + i * 38, 226, 36, 160, 4, WHITE)
    # 黑键（2-3-2-3 分布）
    for bx in (183, 221, 297, 335, 373, 449, 487, 563):
        g += R(bx, 226, 22, 96, 3, KEY_B)
    # 键盘前沿
    g += R(150, 392, 460, 30, 10, WOOD)
    g += L(162, 404, 598, 404, WOOD_L, 5)
    # 飘出的音符（圆头 + 符杆 + 符尾）
    g += C(648, 150, 13, KEY_B)
    g += L(659, 150, 659, 106, KEY_B, 7)
    g += P("M 659 106 Q 676 112 674 128", stroke=KEY_B, w=6)
    g += C(700, 196, 10, KEY_B)
    g += L(709, 196, 709, 162, KEY_B, 6)
    return g


# ---------- 20 scooter kid 站滑板车蹬行 ----------
def art_scooter():
    g = ground()
    # T 把 + 立杆
    g += L(432, 194, 508, 194, GREY_D, 15)
    g += C(428, 194, 13, KEY_B)
    g += C(512, 194, 13, KEY_B)
    g += L(448, 404, 470, 202, GREY_D, 15)
    # 车架踏板 + 挡泥板
    g += R(318, 404, 138, 18, 9, RED)
    g += R(306, 398, 24, 26, 10, RED_D)
    # 前后轮 + 轮心
    g += C(336, 430, 23, GREY_D)
    g += C(336, 430, 10, SILVER)
    g += C(458, 430, 23, GREY_D)
    g += C(458, 430, 10, SILVER)
    # 蹬车的小朋友（站姿，手扶把杆）
    g += kid(368, 416, 1.0, pose="stand", face="smile", arms="point",
             point_at=(468, 212), shirt=TEAL)
    # 行进速度线
    g += L(250, 380, 296, 380, STEEL_L, 7)
    g += L(236, 404, 288, 404, STEEL_L, 6)
    return g


# ---------- 21 hula hoop kid 举臂，腰间转双色圈 ----------
def art_hula_hoop():
    g = ground()
    # 圈的后半弧（画在娃身后，青）
    g += P("M 258 344 A 122 35 0 0 1 502 344", stroke=TEAL, w=15)
    # 转圈的小朋友（举臂）
    g += kid(380, 436, 1.0, pose="stand", face="smile", arms="up", shirt=SUN)
    # 圈的前半弧（画在娃身前，红）
    g += P("M 258 344 A 122 35 0 0 0 502 344", stroke=RED, w=15)
    # 旋转风线
    g += P("M 540 318 Q 562 344 540 372", stroke=STEEL_L, w=7)
    g += P("M 222 320 Q 200 344 222 370", stroke=STEEL_L, w=7)
    return g


def arts():
    return {
        "swing": art_swing(), "seesaw": art_seesaw(), "trampoline": art_trampoline(),
        "bubbles": art_bubbles(), "paper plane": art_paper_plane(),
        "pinwheel": art_pinwheel(), "drum": art_drum(), "piano": art_piano(),
        "scooter": art_scooter(), "hula hoop": art_hula_hoop(),
    }
