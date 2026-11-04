#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 动物·天空水族（dongwu-b）第 2 段插画（第 11~20 张：octopus~owl，共 10 卡）。

每卡造型要点：octopus 紫红圆脑袋八条爪张开可数 / crab 橙红白肚双大钳举起横走 /
snail 棕纹螺旋壳趴大叶上 / bee 黄黑条纹大蜜翅膀绕花飞 / butterfly 蓝紫对称双翅停花上 /
ant 黑棕三节身六足举饼干 / ladybug 红鞘翅黑点圆身 / spider 黑灰吊丝+完整放射螺旋网 /
penguin 黑白分明冰面摇摇摆摆 / owl 棕羽面盘大圆眼站枝。
主体高约 55%~75%，底边落 y≈430 一带；相邻卡主色与轮廓错开，衔接第 10 张 dolphin 蓝灰。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "octopus", "cn": "章鱼"},
    {"w": "crab", "cn": "螃蟹"},
    {"w": "snail", "cn": "蜗牛"},
    {"w": "bee", "cn": "蜜蜂"},
    {"w": "butterfly", "cn": "蝴蝶"},
    {"w": "ant", "cn": "蚂蚁"},
    {"w": "ladybug", "cn": "瓢虫"},
    {"w": "spider", "cn": "蜘蛛"},
    {"w": "penguin", "cn": "企鹅"},
    {"w": "owl", "cn": "猫头鹰"},
]


# ---------- 本段同族补充色 ----------
OCT, OCT_D, OCT_L = "#c75d84", "#a8446f", "#efb6cf"        # 紫红（粉/红族）
CRB, CRB_D, CRB_L = "#f4773f", "#d85a26", "#f9a878"        # 橙红
CREAM = "#fdeedd"                                          # 白肚（PAGE 族）
SN_B, SN_BD = "#f3ddb0", "#ddc08a"                         # 蜗牛体奶黄
SHL = "#8a5a33"                                            # 壳纹深棕（WOOD 族）
BUB = "#bfe3f2"                                            # 水泡浅蓝（WBLUE 族）
WEB = "#b9c2cc"                                            # 蛛网浅灰
SILK = "#9aa3ad"                                           # 蛛丝灰
SPD, SPD_D, SPD_L = "#4e4a52", "#38343c", "#7d7886"        # 蜘蛛黑灰
PGB, PGB_D = "#45414a", "#333038"                          # 企鹅黑
PUR, PUR_D, PUR_L = "#8a72cc", "#6f57ad", "#b7a6e3"        # 蓝紫
ANT, ANT_D, ANT_L = "#55432f", "#3f3021", "#7a6248"        # 蚂蚁黑棕
OWL, OWL_D, OWL_B = "#a97c50", "#8a5f38", "#ecd9b4"        # 猫头鹰棕


# ---------- 小工具 ----------
def eye(cx, cy, rx=10, ry=12):
    """单只眼：INK 圆点 + 左上小白高光。"""
    return E(cx, cy, rx, ry, INK) + C(cx - 3, cy - 4, 3.0, WHITE)


def eye2(cx, cy, dx, rx=10, ry=12):
    return eye(cx - dx, cy, rx, ry) + eye(cx + dx, cy, rx, ry)


def blush2(cx, cy, dx, r=11):
    return C(cx - dx, cy, r, PINK, 0.65) + C(cx + dx, cy, r, PINK, 0.65)


def ebody(cx, cy, rx, ry, main, dark):
    """椭圆身体：深一号偏移衬体积。"""
    return E(cx + rx * 0.06, cy + ry * 0.08, rx, ry, dark) + E(cx, cy, rx, ry, main)


def chead(cx, cy, r, main, dark):
    return C(cx + r * 0.08, cy + r * 0.09, r, dark) + C(cx, cy, r, main)


# ---------- 11 octopus 紫红八爪张开 ----------
def art_octopus():
    g = ground()
    # 八条爪（深一号衬边 + 主色内芯），根藏在头后，端部散开可数
    ts = [
        "M 302 246 Q 230 284 204 348 Q 192 386 206 410 Q 212 420 224 414",
        "M 326 266 Q 276 316 262 378 Q 256 414 272 428",
        "M 350 280 Q 328 336 332 396 Q 334 424 350 430",
        "M 372 286 Q 364 340 368 398 Q 371 424 358 432",
        "M 394 286 Q 406 344 400 402 Q 397 428 412 434",
        "M 416 280 Q 448 338 444 398 Q 442 424 426 428",
        "M 440 266 Q 494 318 506 380 Q 510 412 496 426",
        "M 462 246 Q 536 288 558 350 Q 568 388 554 410 Q 548 420 536 414",
    ]
    for d in ts:
        g += P(d, stroke=OCT_D, w=30) + P(d, stroke=OCT, w=21)
    # 吸盘小点（第 2、7 条爪上）
    g += C(282, 322, 5, OCT_L) + C(268, 378, 5, OCT_L) + C(264, 412, 4.5, OCT_L)
    g += C(478, 320, 5, OCT_L) + C(500, 374, 5, OCT_L) + C(503, 406, 4.5, OCT_L)
    # 圆脑袋
    g += chead(380, 200, 96, OCT, OCT_D)
    g += E(348, 148, 30, 20, OCT_L, 0.75)
    # 脸
    g += eye2(380, 184, 34, 13, 16)
    g += P("M 362 238 Q 380 252 398 238", stroke=INK, w=6)
    g += blush2(380, 228, 62, 12)
    # 水泡
    g += C(596, 132, 13, BUB, 0.75) + C(626, 96, 8, BUB, 0.6) + C(570, 76, 5.5, BUB, 0.5)
    return g


# ---------- 12 crab 橙红白肚，双大钳举起横走 ----------
def pincer(x, y, rot):
    """蟹钳：带缺口的风扇形钳身 + 圆唇钳尖 + 关节圆，缺口朝外即钳口。"""
    g = (P("M 0 0 L 46 -27 A 53 53 0 1 0 44 25 Z", CRB)
         + C(46, -27, 10, CRB) + C(44, 25, 10, CRB)
         + C(0, 0, 15, CRB_D) + C(0, 0, 10, CRB))
    return f'<g transform="translate({x},{y}) rotate({rot})">{g}</g>'


def art_crab():
    g = ground()
    # 远侧步足（深）
    g += P("M 340 386 Q 322 414 306 432", stroke=CRB_D, w=13)
    g += P("M 388 396 Q 380 420 368 436", stroke=CRB_D, w=13)
    g += P("M 444 392 Q 452 418 444 436", stroke=CRB_D, w=13)
    # 身体 + 白肚
    g += ebody(400, 320, 134, 84, CRB, CRB_D)
    g += E(400, 358, 98, 38, CREAM)
    # 近侧步足
    g += P("M 356 392 Q 344 418 330 434", stroke=CRB, w=15)
    g += P("M 410 398 Q 406 422 398 436", stroke=CRB, w=15)
    g += P("M 466 388 Q 478 414 470 434", stroke=CRB, w=15)
    # 双臂 + 双大钳举起
    g += P("M 336 292 Q 300 250 298 204", stroke=CRB_D, w=30)
    g += P("M 464 292 Q 500 246 502 200", stroke=CRB_D, w=30)
    g += pincer(296, 192, -135)
    g += pincer(504, 188, -45)
    # 眼柄 + 眼
    g += L(368, 244, 358, 192, CRB_D, 10) + L(432, 244, 442, 192, CRB_D, 10)
    g += C(356, 184, 17, CREAM) + C(356, 186, 8, INK) + C(353, 182, 2.6, WHITE)
    g += C(444, 184, 17, CREAM) + C(444, 186, 8, INK) + C(441, 182, 2.6, WHITE)
    # 嘴 + 腮
    g += P("M 384 284 Q 400 296 416 284", stroke=INK, w=4.5)
    g += C(338, 294, 11, PINK, 0.6) + C(462, 294, 11, PINK, 0.6)
    # 横行动感弧线
    g += P("M 566 300 Q 578 314 566 328", stroke=CRB_D, w=5)
    g += P("M 590 288 Q 604 306 588 324", stroke=CRB_D, w=4)
    return g


# ---------- 13 snail 棕纹螺旋壳，爬在大叶上 ----------
def art_snail():
    g = ground()
    # 大叶子（先铺）
    g += P("M 188 452 Q 290 398 452 402 Q 588 408 640 446 Q 544 468 420 466 "
           "Q 288 466 188 452 Z", GREEN)
    g += P("M 200 450 Q 400 424 630 444", stroke="#5d8a52", w=7)
    g += L(320, 436, 352, 412, "#5d8a52", 5) + L(420, 434, 452, 410, "#5d8a52", 5)
    g += L(520, 438, 548, 414, "#5d8a52", 5)
    # 腹足
    g += R(246, 402, 280, 36, 18, SN_BD) + R(240, 396, 280, 34, 17, SN_B)
    g += E(252, 412, 26, 18, SN_B)
    # 螺旋壳
    g += C(358, 292, 124, WOOD_D) + C(352, 286, 121, WOOD)
    g += E(310, 232, 34, 22, WOOD_L, 0.8)
    g += P("M 352 168 A 118 118 0 0 1 352 404 "
           "A 90 90 0 0 1 352 224 A 69 69 0 0 1 352 362 "
           "A 52 52 0 0 1 352 258 A 39 39 0 0 1 352 336 "
           "A 28 28 0 0 1 352 280 A 20 20 0 0 1 352 320 "
           "A 13 13 0 0 1 352 294", stroke=SHL, w=8)
    # 颈 + 头
    g += P("M 448 402 Q 498 392 508 316", stroke=SN_BD, w=58)
    g += P("M 448 398 Q 494 388 504 314", stroke=SN_B, w=48)
    g += chead(510, 280, 46, SN_B, SN_BD)
    # 触角（端部小球）
    g += L(526, 244, 550, 190, SN_BD, 9) + C(553, 183, 11, SN_BD)
    g += L(492, 242, 476, 188, SN_BD, 9) + C(473, 181, 11, SN_BD)
    # 脸
    g += eye2(510, 268, 20, 9, 12)
    g += P("M 498 302 Q 510 312 524 304", stroke=INK, w=5)
    g += blush2(510, 296, 34, 10)
    return g


# ---------- 14 bee 黄黑条纹，绕花飞舞 ----------
def art_bee():
    g = ground()
    # 虚线飞行轨迹
    g += ('<path d="M 148 344 Q 236 148 448 216 Q 636 276 606 388" fill="none" '
          'stroke="#c9cdd1" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 22"/>')
    # 两朵花
    g += L(172, 430, 166, 456, "#5d8a52", 10) + flower5(172, 398, 46, "#f0876f", SUN)
    g += L(618, 444, 616, 458, "#5d8a52", 8) + flower5(618, 424, 28, PINK, YEL)
    # 蜜蜂整体（倾斜飞行）
    b = ""
    # 后翅 + 前翅
    b += f'<g transform="rotate(-36 60 -80)">{E(76, -110, 64, 28, "#cfe7f6", 0.95)}</g>'
    b += f'<g transform="rotate(-18 20 -136)">{E(20, -136, 88, 36, "#e0f0fa", 1)}</g>'
    # 腹部（黄）+ 黑条纹
    b += E(8, 8, 158, 112, YEL_D) + E(0, 0, 158, 108, YEL)
    b += R(-58, -100, 28, 200, 14, INK)
    b += R(2, -106, 28, 212, 14, INK)
    b += R(66, -88, 28, 176, 13, INK)
    # 尾针
    b += PG([(152, -6), (196, 10), (152, 28), (142, 10)], INK)
    # 腿
    b += L(-70, 100, -90, 140, INK, 8) + L(-10, 106, -14, 142, INK, 8) + L(56, 98, 74, 130, INK, 8)
    # 头（黑脸，白底托眼）
    b += C(-186, -2, 66, INK)
    b += C(-216, -28, 14, WHITE) + C(-214, -27, 7, INK) + C(-217, -31, 2.5, WHITE)
    b += C(-170, -42, 14, WHITE) + C(-168, -41, 7, INK) + C(-171, -45, 2.5, WHITE)
    b += P("M -212 24 Q -198 34 -184 26", stroke=WHITE, w=4.5)
    # 触角
    b += L(-222, -62, -242, -106, INK, 7) + C(-245, -113, 9, INK)
    b += L(-172, -68, -164, -112, INK, 7) + C(-163, -119, 9, INK)
    g += f'<g transform="translate(452,272) rotate(-14)">{b}</g>'
    return g


# ---------- 15 butterfly 蓝紫对称彩翅，停花上 ----------
def art_butterfly():
    g = ground()
    # 花茎与花（先铺，蝴蝶停在上面）
    g += L(390, 430, 390, 458, "#5d8a52", 12)
    g += f'<g transform="rotate(-20 348 432)">{E(348, 432, 30, 13, GREEN)}</g>'
    g += f'<g transform="rotate(15 434 446)">{E(434, 446, 26, 12, GREEN_L)}</g>'
    g += flower5(390, 400, 52, "#f0876f", SUN)
    # 左侧双翅（右侧镜像）
    wing = (
        # 下翅（浅紫）
        P("M 380 286 Q 324 308 278 346 Q 238 380 264 398 Q 298 410 332 374 Q 368 338 382 302 Z", PUR_D)
        + P("M 378 284 Q 322 306 276 342 Q 238 374 264 392 Q 296 402 328 368 Q 362 334 380 300 Z", PUR_L)
        + C(300, 352, 12, PINK) + C(300, 352, 5.5, WHITE)
        # 上翅（蓝紫大翅）
        + P("M 382 258 Q 334 174 258 142 Q 192 118 178 182 Q 168 246 240 282 Q 318 312 382 276 Z", PUR_D)
        + P("M 380 256 Q 332 172 256 140 Q 192 118 180 180 Q 170 242 242 278 Q 316 306 380 272 Z", PUR)
        + C(262, 196, 19, YEL) + C(262, 196, 9, WHITE)
        + C(318, 240, 11, WBLUE) + C(230, 232, 8, PUR_L)
    )
    g += wing
    g += f'<g transform="translate(780 0) scale(-1 1)">{wing}</g>'
    # 身体 + 头 + 触角
    g += E(390, 268, 17, 54, "#54432f")
    g += C(390, 196, 21, "#54432f")
    g += L(381, 180, 358, 136, INK, 5) + C(355, 130, 7.5, INK)
    g += L(399, 180, 422, 136, INK, 5) + C(425, 130, 7.5, INK)
    # 停在花上的小足
    g += L(384, 318, 376, 346, INK, 5) + L(396, 318, 404, 346, INK, 5)
    return g


# ---------- 16 ant 黑棕三节身，六足举饼干 ----------
def art_ant():
    g = ground()
    # 出发动感弧线
    g += P("M 176 322 Q 164 338 176 354", stroke=ANT_D, w=5)
    g += P("M 152 310 Q 138 330 152 350", stroke=ANT_D, w=4)
    # 远侧腿（前对上举扶饼干，中后对行走）
    g += P("M 440 322 Q 448 288 460 260", stroke=ANT_D, w=9)
    g += P("M 420 376 Q 404 408 390 428", stroke=ANT_D, w=9)
    g += P("M 268 358 Q 254 394 264 424", stroke=ANT_D, w=9)
    # 饼干（先画，被前腿扶住）
    g += C(492, 206, 64, "#c8924e") + C(484, 198, 62, "#e0b06a")
    g += C(462, 180, 8, SHL) + C(502, 172, 7, SHL) + C(516, 214, 8, SHL)
    g += C(474, 232, 7, SHL) + C(498, 204, 5, SHL)
    # 三节身
    g += ebody(296, 336, 88, 70, ANT, ANT_D)
    g += E(272, 314, 34, 22, ANT_L, 0.7)
    g += ebody(430, 344, 50, 40, ANT, ANT_D)
    g += P("M 468 340 Q 496 330 508 316", stroke=ANT_D, w=30)
    g += chead(532, 306, 52, ANT, ANT_D)
    # 近侧腿
    g += P("M 456 316 Q 458 278 466 252", stroke=ANT, w=10)
    g += P("M 432 380 Q 442 410 432 432", stroke=ANT, w=10)
    g += P("M 284 366 Q 272 400 282 430", stroke=ANT, w=10)
    # 脸（黑脸白底托眼）
    g += C(556, 296, 12, WHITE) + C(554, 295, 6, INK) + C(558, 299, 2, WHITE)
    g += C(522, 288, 10, WHITE) + C(520, 287, 5, INK) + C(524, 291, 1.8, WHITE)
    g += P("M 546 330 Q 556 338 566 330", stroke="#f0e3c8", w=4.5)
    # 触角
    g += L(556, 264, 584, 228, ANT_D, 6) + C(587, 222, 8, ANT_D)
    g += L(528, 260, 524, 218, ANT_D, 6) + C(523, 211, 8, ANT_D)
    return g


# ---------- 17 ladybug 红鞘翅黑点圆身 ----------
def art_ladybug():
    g = ground()
    # 六条小足（先画，藏身下）
    g += L(278, 262, 238, 234, "#4a382c", 8) + L(268, 320, 226, 322, "#4a382c", 8)
    g += L(280, 380, 242, 408, "#4a382c", 8)
    g += L(502, 262, 542, 234, "#4a382c", 8) + L(512, 320, 554, 322, "#4a382c", 8)
    g += L(500, 380, 538, 408, "#4a382c", 8)
    # 触角（先画，头盖基部）
    g += L(376, 148, 358, 116, "#4a382c", 5) + C(355, 110, 7, "#4a382c")
    g += L(404, 148, 422, 116, "#4a382c", 5) + C(425, 110, 7, "#4a382c")
    # 头（黑脸）
    g += C(390, 180, 40, "#42342a")
    # 红鞘翅大圆身
    g += C(396, 312, 122, RED_D) + C(390, 306, 120, RED)
    g += E(338, 244, 36, 24, "#f2906b", 0.75)
    # 中缝线
    g += P("M 390 206 Q 388 310 390 424", stroke=INK, w=6)
    # 黑点
    g += C(330, 262, 22, INK) + C(452, 258, 20, INK)
    g += C(322, 338, 18, INK) + C(466, 336, 18, INK)
    g += C(360, 384, 15, INK) + C(428, 388, 14, INK)
    # 头上白底托眼
    g += C(374, 162, 11, WHITE) + C(372, 161, 5.5, INK) + C(376, 165, 1.8, WHITE)
    g += C(406, 162, 11, WHITE) + C(404, 161, 5.5, INK) + C(408, 165, 1.8, WHITE)
    g += P("M 378 190 Q 390 198 402 190", stroke=WHITE, w=4)
    return g


# ---------- 18 spider 黑灰吊丝，完整蛛网 ----------
def art_spider():
    g = ground()
    # 蛛网（放射 8 根 + 四圈螺旋多边形）
    cxw, cyw = 158, 132
    ring_pts = []
    for r in (128, 108, 76, 42):
        pts = []
        for i in range(8):
            a = i * 3.14159265 / 4
            pts.append((cxw + r * _cos(a), cyw + r * _sin(a)))
        ring_pts.append(pts)
        g += P("M " + " L ".join(f"{x:.0f} {y:.0f}" for x, y in pts) + " Z",
               stroke=WEB, w=4)
    for i in range(8):
        a = i * 3.14159265 / 4
        g += L(cxw, cyw, cxw + 128 * _cos(a), cyw + 128 * _sin(a), WEB, 4)
    g += C(cxw, cyw, 5, WEB)
    # 吊丝
    g += L(490, 0, 490, 172, SILK, 5)
    # 八条节肢（先画，藏身下）
    legs = [
        "M 446 216 Q 392 196 364 226", "M 442 240 Q 380 240 348 286",
        "M 444 268 Q 388 300 372 352", "M 452 292 Q 416 340 412 398",
        "M 534 216 Q 588 196 616 226", "M 538 240 Q 600 240 632 286",
        "M 536 268 Q 592 300 608 352", "M 528 292 Q 564 340 568 398",
    ]
    for d in legs:
        g += P(d, stroke=SPD_D, w=9)
    # 腹 + 头
    g += ebody(492, 336, 82, 104, SPD, SPD_D)
    g += C(492, 322, 17, SPD_L) + C(466, 366, 11, SPD_L) + C(518, 370, 9, SPD_L)
    g += C(494, 230, 57, SPD_D) + C(490, 226, 55, SPD)
    # 脸（黑脸白底托眼）
    g += C(468, 214, 13, WHITE) + C(466, 213, 6.5, INK) + C(470, 217, 2.2, WHITE)
    g += C(512, 214, 13, WHITE) + C(510, 213, 6.5, INK) + C(514, 217, 2.2, WHITE)
    g += P("M 478 250 Q 490 258 502 250", stroke=WHITE, w=4)
    g += C(450, 244, 9, "#e8a0b4", 0.6) + C(530, 244, 9, "#e8a0b4", 0.6)
    return g


def _cos(a):
    import math
    return math.cos(a)


def _sin(a):
    import math
    return math.sin(a)


# ---------- 19 penguin 黑白分明，冰面摇摇摆摆 ----------
def art_penguin():
    g = ground(fill="#e2f1f7")
    # 小冰块
    g += E(168, 446, 52, 13, WHITE, 0.9) + E(600, 448, 56, 13, WHITE, 0.9)
    body = ""
    # 身体（黑白分明）
    body += E(388, 306, 110, 134, PGB_D) + E(380, 300, 108, 132, PGB)
    # 摇摆的双鳍：左垂右扬
    body += P("M 284 296 Q 244 336 260 386", stroke=PGB, w=26)
    body += P("M 476 292 Q 518 316 532 362", stroke=PGB, w=26)
    # 白肚
    body += E(380, 336, 80, 92, WHITE)
    # 头 + 白脸
    body += C(384, 190, 72, PGB_D) + C(376, 186, 70, PGB)
    body += E(378, 200, 50, 38, WHITE)
    body += eye2(378, 190, 24, 10, 12)
    body += PG([(362, 212), (394, 212), (378, 236)], "#ef8f3a")
    body += C(346, 218, 9, PINK, 0.7) + C(410, 218, 9, PINK, 0.7)
    # 橙脚一前一后
    body += E(336, 434, 36, 13, "#ef8f3a") + E(438, 430, 36, 13, "#ef8f3a")
    g += f'<g transform="rotate(-6 380 428)">{body}</g>'
    return g


# ---------- 20 owl 棕羽大圆眼，站枝头 ----------
def art_owl():
    g = ground()
    # 横枝
    g += R(140, 408, 480, 28, 14, WOOD_D) + R(140, 408, 480, 11, 5, WOOD)
    g += f'<g transform="rotate(30 636 396)">{E(636, 396, 12, 26, GREEN)}</g>'
    # 耳羽簇
    g += PG([(300, 160), (318, 94), (352, 146)], OWL_D) + PG([(312, 150), (321, 110), (338, 144)], OWL)
    g += PG([(480, 160), (462, 94), (428, 146)], OWL_D) + PG([(468, 150), (459, 110), (442, 144)], OWL)
    # 圆润身体
    g += E(398, 280, 110, 144, OWL_D) + E(390, 274, 108, 142, OWL)
    # 收拢的双翅
    g += E(292, 306, 36, 88, OWL_D) + E(488, 306, 36, 88, OWL_D)
    # 浅肚 + 鳞纹
    g += E(390, 350, 66, 66, OWL_B, 0.95)
    chev = (P("M 356 318 L 368 330 L 380 318", stroke=OWL_D, w=5)
            + P("M 400 318 L 412 330 L 424 318", stroke=OWL_D, w=5)
            + P("M 340 352 L 352 364 L 364 352", stroke=OWL_D, w=5)
            + P("M 384 352 L 396 364 L 408 352", stroke=OWL_D, w=5)
            + P("M 428 352 L 440 364 L 452 352", stroke=OWL_D, w=5)
            + P("M 362 386 L 374 398 L 386 386", stroke=OWL_D, w=5)
            + P("M 406 386 L 418 398 L 430 386", stroke=OWL_D, w=5))
    g += chev
    # 面盘（双圆交叠）
    g += C(350, 240, 58, OWL_B) + C(430, 240, 58, OWL_B)
    # 大圆眼
    g += C(350, 240, 36, WHITE) + C(430, 240, 36, WHITE)
    g += C(350, 243, 18, INK) + C(430, 243, 18, INK)
    g += C(344, 236, 6, WHITE) + C(424, 236, 6, WHITE)
    # 喙
    g += PG([(374, 268), (406, 268), (390, 300)], YEL_D)
    g += C(310, 282, 11, PINK, 0.6) + C(470, 282, 11, PINK, 0.6)
    # 站枝的脚
    g += E(352, 414, 28, 12, "#ef8f3a") + E(428, 414, 28, 12, "#ef8f3a")
    return g


def arts():
    return {
        "octopus": art_octopus(),
        "crab": art_crab(),
        "snail": art_snail(),
        "bee": art_bee(),
        "butterfly": art_butterfly(),
        "ant": art_ant(),
        "ladybug": art_ladybug(),
        "spider": art_spider(),
        "penguin": art_penguin(),
        "owl": art_owl(),
    }
