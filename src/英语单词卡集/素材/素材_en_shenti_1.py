#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 身体（shenti）第 1 段插画（11 卡：head~neck）。

每卡造型要点：head kid 放大裁切大头特写、双手举到头旁 /
hair 乌黑发娃丸子头+木梳+发丝 / face 无发圆脸五官特写 /
eye 单只大眼长睫毛+浓眉 / ear 大耳特写+右侧声波线 /
nose kid 侧脸闻花（鼻前大花香气线）/ mouth 张嘴大笑露齿舌 /
tooth 深色口腔底一颗大白牙+牙刷 / tongue kid 吐舌做鬼脸 /
cheek 红脸蛋特写+hand 指尖轻捏 / neck kid 围红围巾露脖子。
特写卡器官占画布 60% 以上、SKIN 肤色系同族深浅；
相邻卡主色错开：RED/黑+YEL/PINK/BLUE/TEAL/GREEN/PINK/薄荷TEAL/YEL/PINK/RED。
完整人形一律 kid() 组件，特写局部与纯器官造型按规范绘制。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "head", "cn": "头"},
    {"w": "hair", "cn": "头发"},
    {"w": "face", "cn": "脸"},
    {"w": "eye", "cn": "眼睛"},
    {"w": "ear", "cn": "耳朵"},
    {"w": "nose", "cn": "鼻子"},
    {"w": "mouth", "cn": "嘴"},
    {"w": "tooth", "cn": "牙齿"},
    {"w": "tongue", "cn": "舌头"},
    {"w": "cheek", "cn": "脸蛋"},
    {"w": "neck", "cn": "脖子"},
]


# ---------- 本组同族补充色 ----------
SKIN_L = "#fbdcbf"                  # 肤族浅（耳内/高光）
WHITE_D = "#e9e5d8"                 # 白族深（牙齿投影）
MOUTH_IN = "#6b3325"                # 口腔深棕（素材库 kid 张嘴同色）
TONGUE = "#f0876f"                  # 舌/腮红（kid 内置舌色）
TONGUE_D = "#d96a52"                # 舌中线（同族深）


def eyeball(cx, cy, rx, ry, lx=0, ly=0):
    """眼睛：INK 圆点 + 白高光（全组统一画法）。"""
    return E(cx, cy, rx, ry, INK) + C(cx + lx, cy + ly, max(3.0, rx * 0.34), WHITE)


# ---------- 1 head kid 放大裁切，大头特写双手举 ----------
def art_head():
    # 大头特写（与 face/cheek 同族手绘）：圆脸+刘海+举双手+红肩；SVG 不裁切，所有元素必须在画布内
    g = ground()
    g += E(380, 424, 200, 46, RED)
    g += E(380, 424, 200, 46, RED_D, 0.25)
    g += C(212, 380, 27, SKIN)
    g += C(548, 380, 27, SKIN)
    g += E(380, 296, 152, 146, SKIN_D)
    g += C(380, 288, 148, SKIN)
    g += P("M 240 258 Q 248 148 380 140 Q 512 148 520 258 Q 470 202 380 198 Q 290 202 240 258 Z", HAIR)
    g += P("M 300 262 Q 314 272 328 262", stroke=HAIR, w=6)
    g += P("M 432 262 Q 446 272 460 262", stroke=HAIR, w=6)
    g += E(328, 284, 12, 16, INK) + C(328, 278, 4.5, WHITE)
    g += E(432, 284, 12, 16, INK) + C(432, 278, 4.5, WHITE)
    g += P("M 340 330 Q 380 356 420 330", stroke=INK, w=7)
    g += C(298, 318, 17, PINK, 0.8)
    g += C(462, 318, 17, PINK, 0.8)
    return g


# ---------- 2 hair 乌黑头发丸子头 + 木梳 ----------
def art_hair():
    g = ground()
    g += kid(x=330, y=436, s=1.0, face="smile", shirt=YEL, hair_color=INK, bun=True)
    comb = R(-80, -18, 160, 32, 14, WOOD) + R(-80, -18, 160, 11, 6, WOOD_L)
    for i in range(6):
        tx = -72 + i * 24
        comb += R(tx, 10, 13, 34, 6, WOOD) + R(tx, 38, 13, 8, 4, WOOD_D)
    g += f'<g transform="translate(596,396) rotate(-12)">{comb}</g>'
    g += P("M 545 348 Q 556 368 550 388", stroke=INK, w=5)
    g += P("M 562 342 Q 576 362 572 384", stroke=INK, w=5)
    g += star5(384, 108, 12, SUN) + star5(272, 156, 9, SUN)
    return g


# ---------- 3 face 无发圆脸五官特写 ----------
def art_face():
    g = ground()
    g += C(228, 268, 32, SKIN) + C(532, 268, 32, SKIN)
    g += C(213, 268, 12, SKIN_D) + C(547, 268, 12, SKIN_D)
    g += E(389, 260, 150, 150, SKIN_D)
    g += C(380, 252, 150, SKIN)
    g += P("M 293 174 Q 327 156 361 172", stroke=HAIR, w=14)
    g += P("M 399 172 Q 433 156 467 174", stroke=HAIR, w=14)
    g += eyeball(327, 233, 24, 31, 0, -11) + eyeball(433, 233, 24, 31, 0, -11)
    g += E(380, 276, 14, 10, SKIN_D)
    g += P("M 320 306 Q 380 346 440 306", stroke=INK, w=14)
    g += C(274, 288, 27, PINK, 0.8) + C(486, 288, 27, PINK, 0.8)
    return g


# ---------- 4 eye 单只大眼长睫毛 ----------
def art_eye():
    g = ground()
    g += E(390, 258, 262, 208, SKIN_D) + E(380, 250, 258, 204, SKIN)
    g += P("M 118 246 Q 380 70 642 246 Q 380 150 118 246 Z", SKIN_D)
    g += P("M 140 246 Q 380 104 620 246 Q 380 388 140 246 Z", WHITE)
    g += C(380, 246, 62, BLUE) + C(380, 246, 28, INK)
    g += C(356, 220, 13, WHITE) + C(404, 272, 7, WHITE, 0.7)
    for d in ("M 260 193 Q 244 170 224 162", "M 332 178 Q 324 150 306 140",
              "M 380 175 Q 380 146 368 132", "M 428 178 Q 436 150 454 140",
              "M 500 193 Q 516 170 536 162"):
        g += P(d, stroke=INK, w=7)
    g += P("M 262 118 Q 380 78 498 118", stroke=HAIR, w=20)
    return g


# ---------- 5 ear 大耳特写 + 声波线 ----------
def art_ear():
    g = ground()
    g += P("M 444 190 A 75 75 0 0 1 444 310", stroke=TEAL, w=9)
    g += P("M 480 158 A 112 112 0 0 1 480 342", stroke=TEAL, w=9)
    g += P("M 516 126 A 148 148 0 0 1 516 374", stroke=TEAL, w=9)
    g += E(310, 262, 138, 166, SKIN_D)
    g += E(300, 252, 136, 164, SKIN)
    g += P("M 298 119 C 221 104 205 196 229 265 Q 241 290 240 329 C 242 381 290 402 318 365 Q 329 348 316 324 Q 300 297 329 280 C 390 240 366 141 298 119 Z", SKIN_D)
    g += P("M 283 144 C 237 146 232 205 251 239 Q 268 266 253 315 Q 248 352 274 361 Q 298 363 294 334 Q 277 289 304 272 C 354 249 345 177 307 165", stroke=SKIN_L, w=17)
    g += C(287, 279, 22, SKIN) + E(308, 270, 15, 23, SKIN_D)
    g += '<g transform="rotate(-30 252 148)">' + E(252, 148, 46, 18, SKIN_L, 0.8) + "</g>"
    return g


# ---------- 6 nose kid 侧脸闻花 ----------
def art_nose():
    g = ground()
    g += R(348, 336, 46, 64, 14, SKIN)
    g += P("M 272 480 Q 286 408 344 392 L 430 392 Q 490 410 498 480 Z", TEAL)
    prof = ("M 322 96 Q 402 114 416 172 Q 420 188 412 198 "
            "Q 452 206 476 232 Q 480 244 446 250 Q 438 254 452 266 "
            "Q 458 274 442 280 Q 456 290 452 302 Q 450 324 424 330 "
            "Q 384 350 344 356 Q 274 348 250 306 Q 228 246 236 186 "
            "Q 246 122 322 96 Z")
    g += f'<g transform="translate(9,9)">{P(prof, SKIN_D)}</g>'
    g += P(prof, SKIN)
    g += P("M 418 168 Q 404 110 322 96 Q 246 122 236 186 Q 228 246 250 306 "
           "Q 254 318 266 328 Q 258 244 288 196 Q 322 146 376 144 "
           "Q 404 146 418 168 Z", HAIR)
    g += C(262, 132, 27, HAIR) + C(256, 126, 12, "#7a5a42", 0.7)
    g += C(332, 258, 30, SKIN) + C(336, 258, 13, SKIN_D)
    g += P("M 376 180 Q 396 172 414 178", stroke=HAIR, w=8)
    g += eyeball(398, 208, 11, 14, 3, -4)
    g += C(402, 270, 15, PINK, 0.8)
    g += P("M 546 262 Q 558 330 546 424", stroke=GREEN, w=8)
    g += '<g transform="rotate(30 576 330)">' + E(576, 330, 26, 11, GREEN) + "</g>"
    g += flower5(544, 228, 36, petal=TONGUE, core=SUN)
    g += P("M 490 218 Q 502 210 514 218", stroke=GREEN_L, w=5)
    g += P("M 494 240 Q 506 234 518 240", stroke=GREEN_L, w=5)
    return g


# ---------- 7 mouth 张嘴开心笑特写 ----------
def art_mouth():
    g = ground()
    g += E(392, 268, 240, 200, SKIN_D) + E(382, 258, 236, 196, SKIN)
    g += P("M 172 258 Q 380 196 588 258 Q 566 380 380 400 Q 194 380 172 258 Z", PINK)
    g += P("M 192 262 Q 380 214 568 262 Q 550 376 380 392 Q 210 376 192 262 Z", MOUTH_IN)
    g += P("M 206 264 Q 380 222 554 264 Q 546 300 380 310 Q 214 300 206 264 Z", WHITE)
    g += P("M 296 366 Q 380 322 464 366 Q 450 384 380 386 Q 310 384 296 366 Z", TONGUE)
    g += C(196, 330, 24, PINK, 0.7) + C(564, 330, 24, PINK, 0.7)
    return g


# ---------- 8 tooth 一颗大白牙 + 牙刷 ----------
TOOTH = ("M 282 210 Q 282 148 380 148 Q 478 148 478 210 L 478 330 "
         "Q 478 368 456 392 Q 440 408 428 378 Q 414 342 380 342 "
         "Q 346 342 332 378 Q 320 408 304 392 Q 282 368 282 330 Z")


def art_tooth():
    g = ground()
    g += C(386, 282, 190, TEAL_D) + C(376, 272, 188, TEAL_L)
    g += E(380, 400, 156, 42, PINK)
    g += f'<g transform="translate(10,10)">{P(TOOTH, WHITE_D)}</g>'
    g += P(TOOTH, WHITE)
    g += '<g transform="rotate(-20 322 210)">' + E(322, 210, 26, 44, "#ffffff", 0.85) + "</g>"
    g += C(436, 190, 12, "#ffffff", 0.7)
    g += star5(258, 168, 15, SUN) + star5(500, 232, 11, SUN) + star5(486, 150, 8, SUN)
    brush = (R(-30, -13, 170, 26, 13, TEAL) + R(106, -13, 34, 26, 13, TEAL_D)
             + R(-58, -9, 34, 18, 9, TEAL) + R(-108, -12, 54, 24, 12, TEAL))
    for i in range(4):
        brush += R(-104 + i * 13, -34, 10, 24, 4, WHITE)
    g += f'<g transform="translate(614,378) rotate(-32)">{brush}</g>'
    return g


# ---------- 9 tongue kid 吐舌做鬼脸 ----------
def art_tongue():
    g = ground()
    g += kid(x=380, y=436, s=1.05, face="open", arms="up", shirt=YEL)
    g += P("M 352 232 Q 380 222 408 232 Q 418 276 380 302 Q 342 276 352 232 Z", TONGUE)
    g += L(380, 242, 380, 284, TONGUE_D, 5)
    g += star5(262, 120, 11, SUN) + star5(500, 132, 9, SUN)
    return g


# ---------- 10 cheek 红脸蛋特写 + 指尖轻捏 ----------
def art_cheek():
    g = ground()
    g += E(390, 286, 195, 184, SKIN_D)
    g += C(380, 280, 190, SKIN)
    g += P("M 260 232 Q 292 210 324 232", stroke=INK, w=9)
    g += P("M 436 228 Q 468 206 500 228", stroke=INK, w=9)
    g += C(286, 310, 64, PINK) + C(286, 310, 40, TONGUE, 0.85)
    g += C(486, 322, 60, PINK) + C(486, 322, 37, TONGUE, 0.85)
    g += heart(192, 130, 22, RED)
    g += hand(580, 316, -90, 0.62)
    return g


# ---------- 11 neck kid 围围巾露脖子 ----------
def art_neck():
    g = ground()
    g += P("M 209 444 Q 223 348 308 330 L 452 330 Q 537 348 551 444 Z", GREEN)
    g += R(339, 242, 82, 105, 23, SKIN_D) + R(337, 238, 78, 105, 22, SKIN)
    g += C(380, 177, 96, SKIN) + C(281, 183, 16, SKIN) + C(479, 183, 16, SKIN)
    g += P("M 286 155 Q 294 70 380 65 Q 466 70 474 155 Q 432 114 380 112 Q 328 114 286 155 Z", HAIR)
    g += eyeball(346, 173, 10, 13, 0, -5) + eyeball(414, 173, 10, 13, 0, -5)
    g += P("M 350 212 Q 380 232 410 212", stroke=INK, w=6)
    g += R(290, 345, 177, 35, 15, RED) + R(414, 364, 35, 72, 10, RED)
    g += P("M 524 296 L 435 296 M 455 282 L 435 296 L 455 310", stroke=TEAL_D, w=8)
    return g


def arts():
    return {
        "head": art_head(),
        "hair": art_hair(),
        "face": art_face(),
        "eye": art_eye(),
        "ear": art_ear(),
        "nose": art_nose(),
        "mouth": art_mouth(),
        "tooth": art_tooth(),
        "tongue": art_tongue(),
        "cheek": art_cheek(),
        "neck": art_neck(),
    }
