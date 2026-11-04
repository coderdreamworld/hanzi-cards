#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 动物·天空水族（dongwu-b）第 1 段插画（10 卡：bird~dolphin）。

每卡造型要点：bird 蓝鸟站枝头张嘴唱歌带声波线 / duck 金黄鸭浮水面划波纹 /
chick 奶黄圆滚滚尖嘴小翅 / frog 亮绿蛙蹲荷叶鼓眼吐舌 / turtle 橄榄壳纹龟伸颈慢爬 /
snake 黄蛇盘绕吐红信 / fish 橙鱼摆尾吐气泡串 / shark 灰鲨背鳍高耸露尖牙 /
whale 深蓝鲸头顶喷水柱 / dolphin 蓝灰豚跃出水面弯成弧线。
全部侧面全身像，主体高约 250~340px，底边落在地面/水面 y≈430。
水生卡把 ground 换成同族浅蓝水色扁椭圆。主色按分配且相邻卡错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "bird", "cn": "鸟"},
    {"w": "duck", "cn": "鸭子"},
    {"w": "chick", "cn": "小鸡"},
    {"w": "frog", "cn": "青蛙"},
    {"w": "turtle", "cn": "乌龟"},
    {"w": "snake", "cn": "蛇"},
    {"w": "fish", "cn": "鱼"},
    {"w": "shark", "cn": "鲨鱼"},
    {"w": "whale", "cn": "鲸鱼"},
    {"w": "dolphin", "cn": "海豚"},
]


# ---------- 本组同族补充色 ----------
WATER, WATER_D = "#c6e5f2", "#a5d7ec"                    # 水色地面/波纹（WBLUE 族浅）
SPOUT = "#9fd2ea"                                        # 水柱/水花（WBLUE 族）
BLU_L = "#a8d6ee"                                        # 鸟浅腹（WBLUE 族）
DUCK, DUCK_D, DUCK_L = "#f2b53c", "#d99a2b", "#f8d37e"   # 鸭金黄（YEL 族）
BILL, BILL_D = "#e8912f", "#d9822b"                      # 喙/脚橙
CHK, CHK_D, CHK_L = "#f7e3ae", "#e4cd90", "#fdf3d4"      # 小鸡奶黄（比鸭浅很多）
FRG, FRG_D, FRG_L = "#6fb45f", "#5a9c4c", "#a8d98f"      # 蛙亮绿（GREEN 族）
SHL, SHL_D, SHL_L = "#8f9e52", "#77873f", "#b7c37e"      # 龟壳橄榄绿
TSK, TSK_D = "#9dbcae", "#86a598"                        # 龟皮肤青灰（TEAL 族灰）
SNK, SNK_D = "#eac95a", "#d0ab3c"                        # 蛇黄身
BRN = "#a5764a"                                          # 蛇棕斑（WOOD 族）
ORG, ORG_D, ORG_L = "#ef8f3a", "#d97a26", "#f8bb78"      # 鱼橙
GRY, GRY_D = "#a3b3c2", "#8a9bab"                        # 鲨灰
WHL, WHL_D = "#3f7cb5", "#326699"                        # 鲸深蓝（BLUE 族深）
DLN, DLN_D = "#8aa7ba", "#7391a5"                        # 海豚蓝灰
MOUTH = "#8f4030"                                        # 口腔暗红
REED = "#6f9e63"                                         # 芦苇绿（GREEN 族深）


def eye(cx, cy, rx=10, ry=12):
    """单只眼睛：INK 圆点 + 白高光。"""
    return E(cx, cy, rx, ry, INK) + C(cx - 3, cy - 4, 3.0, WHITE)


def eye2(cx, cy, dx, rx=10, ry=12):
    """双眼。"""
    return eye(cx - dx, cy, rx, ry) + eye(cx + dx, cy, rx, ry)


def blush2(cx, cy, dx, r=11):
    return C(cx - dx, cy, r, PINK, 0.65) + C(cx + dx, cy, r, PINK, 0.65)


def ebody(cx, cy, rx, ry, main, dark):
    """椭圆身体：深一号偏移衬体积。"""
    return E(cx + rx * 0.06, cy + ry * 0.08, rx, ry, dark) + E(cx, cy, rx, ry, main)


def chead(cx, cy, r, main, dark):
    return C(cx + r * 0.08, cy + r * 0.09, r, dark) + C(cx, cy, r, main)


# ---------- 1 bird 蓝鸟站枝头，张嘴唱歌带声波线 ----------
def art_bird():
    g = ground()
    # 树枝 + 叶
    g += R(128, 398, 496, 24, 12, WOOD_D) + R(128, 398, 496, 9, 4, WOOD)
    g += f'<g transform="rotate(32 616 390)">{E(616, 390, 12, 27, GREEN)}</g>'
    g += f'<g transform="rotate(58 640 378)">{E(640, 378, 11, 24, GREEN_L)}</g>'
    g += f'<g transform="rotate(-30 152 392)">{E(152, 392, 11, 25, GREEN_L)}</g>'
    # 翘尾（先画）
    g += P("M 500 288 Q 562 256 590 206", stroke=BLUE_D, w=34)
    g += P("M 496 286 Q 556 254 585 206", stroke=BLUE, w=24)
    g += C(587, 202, 9, BLUE_D)
    # 身体 + 浅腹
    g += ebody(416, 284, 112, 98, BLUE, BLUE_D)
    g += E(402, 318, 64, 56, BLU_L, 0.9)
    # 翅膀
    g += f'<g transform="rotate(-16 452 288)">{E(452, 288, 50, 70, BLUE_D)}</g>'
    # 头 + 冠羽（先画羽，被头盖基部）
    g += f'<g transform="rotate(-18 336 122)">{E(336, 122, 10, 24, BLUE_D)}</g>'
    g += f'<g transform="rotate(10 362 118)">{E(362, 118, 9, 22, BLUE_D)}</g>'
    g += chead(322, 200, 72, BLUE, BLUE_D)
    # 张嘴（上下喙）
    g += PG([(260, 186), (194, 170), (256, 212)], BILL)
    g += PG([(258, 216), (202, 234), (258, 240)], BILL_D)
    # 眼 + 腮红
    g += eye(300, 186, 11, 13)
    g += C(342, 226, 12, PINK, 0.7)
    # 腿脚（站在枝上）
    g += L(398, 368, 392, 402, BILL, 9)
    g += L(434, 370, 430, 402, BILL, 9)
    g += L(380, 401, 404, 401, BILL, 6)
    g += L(420, 401, 444, 401, BILL, 6)
    # 声波线（本卡主角）
    g += P("M 172 168 Q 144 202 172 236", stroke=BLUE_D, w=6)
    g += P("M 138 146 Q 100 202 138 258", stroke=BLUE_D, w=6)
    g += P("M 104 124 Q 56 202 104 280", stroke=BLUE_D, w=6)
    return g


# ---------- 2 duck 金黄鸭浮水面，划出波纹 ----------
def art_duck():
    g = ground(fill=WATER)
    # 翘尾（先画）
    g += P("M 498 316 Q 560 284 586 230", stroke=DUCK_D, w=32)
    g += P("M 494 314 Q 554 282 581 230", stroke=DUCK, w=22)
    g += C(583, 226, 9, DUCK_D)
    # 颈（先铺深色再上主色）
    g += P("M 316 306 Q 292 268 290 226", stroke=DUCK_D, w=58)
    g += P("M 312 304 Q 290 266 288 224", stroke=DUCK, w=46)
    # 身体 + 浅腹
    g += ebody(402, 336, 136, 92, DUCK, DUCK_D)
    g += E(388, 366, 84, 48, DUCK_L, 0.85)
    # 头
    g += chead(283, 206, 56, DUCK, DUCK_D)
    # 翅膀
    g += f'<g transform="rotate(-14 428 322)">{E(428, 322, 62, 44, DUCK_D)}</g>'
    # 扁嘴（上下喙）
    g += f'<g transform="rotate(-6 216 224)">{E(216, 224, 36, 14, BILL)}</g>'
    g += f'<g transform="rotate(-6 222 244)">{E(222, 244, 31, 11, BILL_D)}</g>'
    # 眼 + 腮红
    g += eye(276, 192, 10, 12)
    g += C(318, 234, 11, PINK, 0.7)
    # 水线盖过腹底（浮水感）+ 波纹
    g += E(380, 444, 178, 17, WATER)
    g += P("M 158 430 Q 196 442 236 432", stroke=WATER_D, w=5)
    g += P("M 552 428 Q 590 440 630 430", stroke=WATER_D, w=5)
    # 芦苇
    g += R(668, 306, 11, 118, 5, REED) + E(673, 296, 13, 27, "#8a5a33")
    g += P("M 654 424 Q 640 380 650 340", stroke=REED, w=6)
    return g


# ---------- 3 chick 奶黄圆滚滚小鸡，尖嘴小翅 ----------
def art_chick():
    g = ground()
    # 脚（先画）
    g += L(356, 420, 350, 452, BILL, 11)
    g += L(424, 420, 430, 452, BILL, 11)
    g += E(346, 454, 18, 7, BILL) + E(434, 454, 18, 7, BILL)
    # 圆滚滚身体
    g += ebody(390, 300, 130, 128, CHK, CHK_D)
    g += E(376, 332, 74, 62, CHK_L, 0.9)
    # 小翅膀
    g += f'<g transform="rotate(-18 284 310)">{E(284, 310, 30, 54, CHK_D)}</g>'
    g += f'<g transform="rotate(18 496 310)">{E(496, 310, 30, 54, CHK_D)}</g>'
    # 头顶绒毛
    g += f'<g transform="rotate(-24 362 172)">{E(362, 172, 8, 20, CHK_D)}</g>'
    g += f'<g transform="rotate(-4 390 164)">{E(390, 164, 9, 24, CHK_D)}</g>'
    g += f'<g transform="rotate(20 418 172)">{E(418, 172, 8, 20, CHK_D)}</g>'
    # 眼 + 尖嘴 + 腮红
    g += eye2(390, 262, 36, 11, 13)
    g += PG([(364, 290), (416, 290), (390, 318)], BILL)
    g += PG([(374, 306), (406, 306), (390, 322)], BILL_D)
    g += blush2(390, 300, 58, 11)
    return g


# ---------- 4 frog 亮绿蛙蹲荷叶上，鼓眼吐舌 ----------
def art_frog():
    g = ground(fill=WATER)
    # 荷叶（带缺口 + 叶脉）
    g += E(382, 420, 218, 34, GREEN) + E(376, 414, 208, 30, GREEN_L)
    g += PG([(378, 414), (560, 398), (574, 430)], WATER)
    g += L(376, 414, 236, 402, "#67965a", 4)
    g += L(376, 414, 258, 434, "#67965a", 4)
    g += L(376, 414, 544, 402, "#67965a", 4)
    # 后腿（鼓起的腿部，先画）
    g += C(482, 366, 58, FRG_D) + C(477, 362, 54, FRG)
    # 身体 + 浅腹
    g += ebody(386, 330, 138, 98, FRG, FRG_D)
    g += E(368, 366, 90, 50, FRG_L, 0.85)
    # 前脚
    g += E(318, 420, 32, 12, FRG_D) + E(316, 417, 28, 9, FRG)
    g += E(452, 422, 32, 12, FRG_D) + E(450, 419, 28, 9, FRG)
    # 鼓眼（本卡主角）
    g += C(340, 220, 38, FRG_D) + C(336, 216, 35, FRG) + C(336, 218, 21, WHITE)
    g += E(336, 218, 8.5, 10, INK) + C(333, 214, 3, WHITE)
    g += C(424, 224, 38, FRG_D) + C(420, 220, 35, FRG) + C(420, 222, 21, WHITE)
    g += E(420, 222, 8.5, 10, INK) + C(417, 218, 3, WHITE)
    # 鼻孔 + 宽嘴
    g += C(318, 288, 4, INK) + C(342, 286, 4, INK)
    g += P("M 288 316 Q 380 356 470 312", stroke=INK, w=6)
    # 吐舌（本卡主角）
    g += P("M 296 322 Q 248 348 210 334", stroke="#f0876f", w=15)
    g += C(208, 334, 11, "#f0876f")
    # 腮红
    g += C(456, 340, 12, PINK, 0.6)
    return g


# ---------- 5 turtle 橄榄壳纹乌龟，伸颈慢慢爬 ----------
def art_turtle():
    g = ground()
    # 尾（右后）
    g += PG([(548, 376), (606, 392), (546, 402)], TSK_D)
    # 远侧腿（先画，探出壳外）
    g += R(244, 384, 46, 58, 20, TSK_D) + E(266, 440, 30, 10, TSK_D)
    g += R(500, 382, 46, 60, 20, TSK_D) + E(522, 440, 30, 10, TSK_D)
    # 伸长的颈 + 头（向前看）
    g += P("M 296 330 Q 262 300 234 258", stroke=TSK_D, w=52)
    g += P("M 292 326 Q 258 296 230 254", stroke=TSK, w=42)
    g += chead(210, 236, 50, TSK, TSK_D)
    # 壳 + 浅色壳缘
    g += ebody(394, 344, 152, 108, SHL, SHL_D)
    g += E(390, 426, 160, 26, SHL_L)
    # 壳纹（清晰：中缝 + 盾片弧线）
    g += L(394, 244, 394, 318, SHL_D, 6)
    g += P("M 318 262 Q 352 288 346 330", stroke=SHL_D, w=6)
    g += P("M 470 262 Q 436 288 442 330", stroke=SHL_D, w=6)
    g += P("M 268 320 Q 330 336 394 332 Q 458 336 520 320", stroke=SHL_D, w=6)
    g += P("M 394 332 Q 380 372 392 402", stroke=SHL_D, w=5)
    g += P("M 320 340 Q 316 372 330 396", stroke=SHL_D, w=5)
    g += P("M 468 340 Q 472 372 458 396", stroke=SHL_D, w=5)
    # 近侧腿
    g += R(292, 398, 50, 46, 20, TSK) + E(318, 442, 32, 11, TSK)
    g += R(448, 396, 50, 48, 20, TSK) + E(474, 442, 32, 11, TSK)
    # 脸
    g += eye(196, 222, 9, 11)
    g += C(176, 250, 3.5, INK)
    g += P("M 172 264 Q 188 274 204 270", stroke=INK, w=5)
    g += C(236, 274, 10, PINK, 0.6)
    return g


# ---------- 6 snake 黄蛇盘绕，吐红色信子 ----------
def art_snake():
    g = ground()
    # 盘绕三圈（自下而上）
    g += ebody(392, 398, 152, 42, SNK, SNK_D)
    g += ebody(392, 340, 126, 38, SNK, SNK_D)
    g += ebody(392, 288, 100, 33, SNK, SNK_D)
    # 尾尖（右端探出）
    g += PG([(536, 386), (592, 374), (542, 404)], SNK_D)
    g += PG([(538, 390), (580, 382), (540, 398)], SNK)
    # 圈间影线
    g += P("M 276 356 Q 392 382 508 354", stroke=SNK_D, w=5)
    g += P("M 302 302 Q 392 324 482 300", stroke=SNK_D, w=5)
    # 棕斑纹（本卡特征）
    g += E(300, 396, 14, 9, BRN, 0.9) + E(396, 404, 15, 9, BRN, 0.9) + E(482, 394, 13, 8, BRN, 0.9)
    g += E(318, 340, 13, 8, BRN, 0.9) + E(432, 342, 12, 8, BRN, 0.9)
    g += E(352, 288, 12, 8, BRN, 0.9) + E(444, 286, 11, 7, BRN, 0.9)
    # 颈身升起
    g += P("M 336 296 Q 300 262 292 214", stroke=SNK_D, w=40)
    g += P("M 332 292 Q 297 258 289 210", stroke=SNK, w=30)
    # 头（微低）
    g += f'<g transform="rotate(-10 276 196)">{E(276, 196, 48, 34, SNK_D) + E(272, 192, 45, 31, SNK)}</g>'
    g += eye2(272, 184, 17, 7.5, 9)
    # 吐红信（本卡主角）
    g += P("M 230 202 Q 208 206 190 202", stroke=RED, w=7)
    g += L(190, 202, 172, 192, RED, 6)
    g += L(190, 202, 172, 212, RED, 6)
    # 腮红
    g += C(296, 214, 9, PINK, 0.6)
    return g


# ---------- 7 fish 橙鱼摆尾，吐气泡串 ----------
def art_fish():
    g = ground(fill=WATER)
    # 水草
    g += P("M 148 444 Q 136 402 156 364", stroke=GREEN, w=9)
    g += P("M 176 446 Q 188 410 172 378", stroke=GREEN_L, w=8)
    g += P("M 612 446 Q 624 412 608 380", stroke=GREEN, w=8)
    # 尾鳍（分叉，先画）
    g += PG([(502, 316), (646, 234), (608, 336)], ORG_D)
    g += PG([(502, 326), (638, 422), (598, 338)], ORG)
    # 背鳍 + 腹鳍（先画）
    g += PG([(326, 234), (390, 156), (468, 238)], ORG_D)
    g += PG([(356, 424), (398, 466), (438, 424)], ORG_D)
    # 身体 + 浅腹
    g += ebody(384, 322, 148, 108, ORG, ORG_D)
    g += E(376, 368, 98, 52, ORG_L, 0.8)
    # 鳃线 + 侧鳍 + 鳞片弧
    g += P("M 306 258 Q 286 320 308 382", stroke=ORG_D, w=6)
    g += f'<g transform="rotate(28 322 348)">{E(322, 348, 44, 22, ORG_D)}</g>'
    g += P("M 392 252 Q 408 274 392 296", stroke=ORG_D, w=5)
    g += P("M 444 258 Q 460 280 444 302", stroke=ORG_D, w=5)
    g += P("M 496 270 Q 512 290 496 312", stroke=ORG_D, w=5)
    # 眼 + 嘴
    g += eye(288, 286, 12, 14)
    g += P("M 240 322 Q 252 332 266 328", stroke=INK, w=5)
    # 气泡串（本卡主角）
    g += C(224, 248, 12, WATER_D) + C(220, 244, 4, WHITE)
    g += C(206, 198, 9, WATER_D) + C(203, 195, 3, WHITE)
    g += C(218, 152, 13, WATER_D) + C(213, 147, 4.5, WHITE)
    g += C(200, 104, 8, WATER_D) + C(197, 101, 3, WHITE)
    return g


# ---------- 8 shark 灰鲨背鳍高耸，露尖牙 ----------
def art_shark():
    g = ground(fill=WATER)
    # 尾鳍（先画）
    g += PG([(552, 330), (672, 208), (646, 344)], GRY_D)
    g += PG([(552, 338), (660, 426), (630, 350)], GRY)
    # 背鳍（高耸，先画）
    g += PG([(384, 280), (462, 146), (516, 282)], GRY_D)
    # 身体 + 白肚
    g += ebody(408, 348, 170, 88, GRY, GRY_D)
    g += E(398, 388, 120, 42, WHITE, 0.95)
    # 尖吻
    g += PG([(258, 316), (190, 344), (260, 376)], GRY)
    # 张嘴露尖牙（本卡主角）
    g += PG([(226, 350), (322, 368), (244, 398)], MOUTH)
    g += PG([(234, 352), (250, 370), (262, 355)], WHITE)
    g += PG([(266, 358), (280, 376), (292, 360)], WHITE)
    g += PG([(296, 363), (310, 380), (322, 365)], WHITE)
    # 鳃线
    g += P("M 344 292 Q 330 322 344 352", stroke=GRY_D, w=5)
    g += P("M 372 290 Q 358 320 372 350", stroke=GRY_D, w=5)
    g += P("M 400 288 Q 386 318 400 348", stroke=GRY_D, w=5)
    # 胸鳍
    g += f'<g transform="rotate(26 372 410)">{E(372, 410, 54, 22, GRY_D)}</g>'
    # 眼
    g += C(282, 312, 11, INK) + C(279, 308, 3.5, WHITE)
    # 尾后气泡
    g += C(596, 262, 9, WATER_D) + C(624, 232, 6, WATER_D)
    return g


# ---------- 9 whale 深蓝大鲸，头顶喷水柱 ----------
def art_whale():
    g = ground(fill=WATER)
    # 尾鳍（先画）
    g += PG([(524, 328), (652, 246), (626, 352)], WHL_D)
    g += PG([(526, 336), (644, 426), (612, 354)], WHL)
    # 背脊小鳍（先画）
    g += PG([(468, 266), (502, 234), (534, 272)], WHL_D)
    # 身体 + 浅腹
    g += ebody(388, 344, 182, 96, WHL, WHL_D)
    g += E(378, 392, 132, 44, "#b9d8ec", 0.9)
    # 胸鳍
    g += f'<g transform="rotate(24 326 404)">{E(326, 404, 56, 24, WHL_D)}</g>'
    # 喷水柱（本卡主角）：气孔 + 水柱 + 分叉 + 水珠
    g += E(306, 257, 11, 6, WHL_D)
    g += P("M 306 253 Q 300 216 304 184", stroke=SPOUT, w=18)
    g += P("M 304 194 Q 276 172 258 148", stroke=SPOUT, w=11)
    g += P("M 304 194 Q 334 170 352 146", stroke=SPOUT, w=11)
    g += C(254, 140, 11, SPOUT) + C(250, 136, 4, WHITE)
    g += C(356, 138, 11, SPOUT) + C(352, 134, 4, WHITE)
    g += C(305, 114, 13, SPOUT) + C(300, 109, 4.5, WHITE)
    # 眼 + 微笑 + 腮红
    g += C(290, 308, 10, INK) + C(287, 304, 3.2, WHITE)
    g += P("M 224 346 Q 262 366 302 360", stroke=INK, w=6)
    g += C(324, 336, 10, PINK, 0.5)
    return g


# ---------- 10 dolphin 蓝灰海豚跃出水面，弯成弧线 ----------
def art_dolphin():
    g = ground(fill=WATER)
    # 尾鳍（先画，被身体盖住基部）
    g += PG([(566, 280), (676, 206), (646, 300)], DLN_D)
    g += PG([(568, 302), (664, 348), (636, 278)], DLN)
    # 身体弯成弧线（本卡主角）：先深色偏移再主色
    g += P("M 215 339 Q 257 169 399 157 Q 547 159 597 289 L 573 319 Q 507 221 399 219 Q 295 223 247 371 Z", DLN_D)
    g += P("M 208 332 Q 250 162 392 150 Q 540 152 590 282 L 566 312 Q 500 214 392 212 Q 288 216 240 364 Z", DLN)
    # 白肚（沿下缘的窄条）
    g += P("M 560 306 Q 498 216 392 214 Q 290 218 244 360 Q 300 198 392 196 Q 490 198 545 292 Z", WHITE, 0.92)
    # 背鳍
    g += P("M 366 172 Q 398 100 452 122 Q 420 138 410 176 Z", DLN_D)
    # 尖喙
    g += PG([(214, 320), (152, 342), (216, 354)], DLN_D)
    # 胸鳍
    g += f'<g transform="rotate(40 340 232)">{E(340, 232, 44, 17, DLN_D)}</g>'
    # 眼 + 嘴 + 腮红
    g += C(282, 200, 9, INK) + C(279, 197, 3, WHITE)
    g += P("M 198 348 Q 224 364 250 358", stroke=INK, w=5)
    g += C(308, 208, 9, PINK, 0.6)
    # 入水浪花 + 波纹
    g += E(300, 434, 96, 13, WHITE, 0.75)
    g += drop(212, 406, 10, SPOUT)
    g += drop(258, 380, 8, SPOUT)
    g += drop(352, 394, 9, SPOUT)
    g += P("M 158 436 Q 200 448 246 438", stroke=WATER_D, w=5)
    g += P("M 416 434 Q 458 446 504 436", stroke=WATER_D, w=5)
    return g


def arts():
    return {
        "bird": art_bird(),
        "duck": art_duck(),
        "chick": art_chick(),
        "frog": art_frog(),
        "turtle": art_turtle(),
        "snake": art_snake(),
        "fish": art_fish(),
        "shark": art_shark(),
        "whale": art_whale(),
        "dolphin": art_dolphin(),
    }
