#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""拼音卡数据与新增插画。

- SETS：两套卡（字母卡=声母/y-w/韵母/整体认读/完整表/声调/易混；拼读卡保留为离线产物）
- NEW_ARTS：拼音卡新画场景；识字卡现成插画用 "ref":字 引用（构建器从 422 素材解析）
- 画布同素材库：viewBox 0 0 760 480 的 <g> 内部内容；扁平绘本、暖色、ground() 开头
"""
import importlib.util
from pathlib import Path

PARENT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("pinyin_lib", PARENT / "识字卡片_素材库.py")
lib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lib)

C, E, R, L, P, PG, wrap = lib.C, lib.E, lib.R, lib.L, lib.P, lib.PG, lib.wrap
ground = lib.ground
INK = lib.INK
YEL, YEL_D = lib.YEL, lib.YEL_D
TEAL, TEAL_D, TEAL_L = lib.TEAL, lib.TEAL_D, lib.TEAL_L
BLUE, BLUE_D = lib.BLUE, lib.BLUE_D
WBLUE = lib.WBLUE
SKIN, SKIN_D, HAIR = lib.SKIN, lib.SKIN_D, lib.HAIR
WOOD, WOOD_D, WOOD_L = lib.WOOD, lib.WOOD_D, lib.WOOD_L
GREEN, GREEN_L = lib.GREEN, lib.GREEN_L
SUN, SUN_L = lib.SUN, lib.SUN_L
PINK, WHITE, RED, RED_D = lib.PINK, lib.WHITE, lib.RED, lib.RED_D
kid = lib.kid

# ---------------- 字母卡场景 ----------------
NEW_ARTS = {}

NEW_ARTS["s_b"] = wrap(  # b：旗杆（左）+ 大气球鼓在杆右侧下方
    ground(),
    R(246, 54, 32, 360, 16, WOOD_D),
    C(390, 304, 112, RED_D, 0.25), C(382, 294, 106, RED),
    P("M 278 218 Q 314 210 330 226", stroke="#d9d0c5", w=8),
    C(348, 254, 22, WHITE, 0.78),
)

NEW_ARTS["s_p"] = wrap(  # p：球拍（大拍面网格线，手持柄）
    ground(),
    R(252, 102, 34, 326, 17, WOOD_D),
    E(394, 204, 114, 126, BLUE_D, 0.22), E(386, 196, 108, 120, BLUE),
    L(286, 156, 488, 156, "#8bc2e7", 7), L(286, 216, 492, 216, "#8bc2e7", 7),
    L(348, 82, 348, 310, "#8bc2e7", 7), L(420, 82, 420, 310, "#8bc2e7", 7),
    E(352, 158, 25, 31, WHITE, 0.72),
)

NEW_ARTS["s_m"] = wrap(  # m：两个门洞的城墙
    ground(),
    R(110, 140, 540, 260, 24, "#e7d3ac"),
    R(110, 140, 540, 44, 22, "#d9bf92"),
    P("M 200 400 L 200 300 Q 200 236 268 236 Q 336 236 336 300 L 336 400 Z", "#8a5a33"),
    P("M 424 400 L 424 300 Q 424 236 492 236 Q 560 236 560 300 L 560 400 Z", "#8a5a33"),
    C(234, 186, 14, RED_D), C(522, 186, 14, RED_D),
    E(380, 428, 250, 22, lib.GROUND, 0.5),
)

NEW_ARTS["s_n"] = wrap(  # n：一个门洞
    ground(),
    R(180, 170, 400, 230, 22, "#e7d3ac"),
    R(180, 170, 400, 40, 20, "#d9bf92"),
    P("M 280 400 L 280 310 Q 280 250 380 250 Q 480 250 480 310 L 480 400 Z", "#8a5a33"),
    C(320, 214, 12, RED_D), C(440, 214, 12, RED_D),
)

NEW_ARTS["s_f"] = wrap(  # f：爷爷的拐棍
    ground(),
    P("M 470 60 Q 380 74 372 180 L 366 400", stroke=WOOD_D, w=34),
    P("M 470 60 Q 380 74 372 180 L 366 400", stroke=WOOD_L, w=16),
    R(286, 174, 190, 30, 15, TEAL),
    E(366, 408, 30, 14, WOOD_D),
)

NEW_ARTS["s_d"] = wrap(  # d：小鼓和鼓槌（左半圆鼓身+竖鼓槌）
    ground(),
    C(356, 302, 116, RED_D, 0.26), C(348, 294, 110, RED),
    C(326, 262, 22, WHITE, 0.65),
    R(458, 76, 34, 344, 17, WOOD_D), C(475, 78, 28, SUN),
    L(458, 294, 430, 294, WOOD_D, 20),
)

NEW_ARTS["s_l"] = wrap(  # l：金箍棒（直棍）
    ground(),
    R(356, 40, 48, 380, 24, SUN),
    R(356, 40, 48, 60, 24, RED), R(356, 360, 48, 60, 24, RED),
    R(368, 110, 24, 240, 12, SUN_L, 0.7),
    L(300, 420, 470, 420, lib.GROUND, 10),
)

NEW_ARTS["s_g"] = wrap(  # g：小蝌蚪（圆头+弯尾）
    ground(),
    C(400, 220, 86, "#3d3a38"), C(378, 200, 84, "#4a4744"),
    C(352, 190, 15, WHITE), C(357, 192, 7, INK),
    P("M 452 262 Q 560 320 520 396 Q 496 436 448 414", stroke="#4a4744", w=26),
    P("M 520 396 Q 500 380 478 388", stroke="#4a4744", w=14),
)

NEW_ARTS["s_k"] = wrap(  # k：水草张开（直茎+两片朝左斜叶，小鱼作参照）
    ground(),
    P("M 316 430 L 316 96", stroke=TEAL_D, w=24),
    P("M 326 264 Q 398 212 492 178 Q 516 170 502 194 Q 444 270 330 294", fill=TEAL),
    P("M 326 282 Q 410 324 496 376 Q 516 392 490 392 Q 402 380 324 318", fill=TEAL_L),
    E(380, 446, 240, 20, lib.GROUND, 0.7),
)

NEW_ARTS["s_h"] = wrap(  # h：小椅子
    ground(),
    R(280, 74, 36, 336, 18, WOOD),
    P("M 298 238 Q 370 186 456 224 Q 486 238 486 282 L 486 400", stroke=WOOD_L, w=34),
    R(288, 370, 30, 40, 12, WOOD_D), R(494, 370, 30, 40, 12, WOOD_D),
    E(380, 436, 220, 20, lib.GROUND, 0.5),
)

NEW_ARTS["s_j"] = wrap(  # j：鱼钩（弯钩+浮点）
    ground(),
    P("M 438 118 L 438 320 Q 438 402 354 398 Q 300 394 306 344", stroke="#8a949c", w=22),
    C(438, 66, 24, RED),
    P("M 306 344 L 286 366 L 318 362 Z", "#8a949c"),
)

NEW_ARTS["s_q"] = wrap(  # q：气球（圆+长线垂右下）
    ground(),
    C(344, 190, 112, TEAL_D, 0.3), C(336, 182, 106, TEAL),
    E(304, 148, 25, 30, WHITE, 0.72),
    R(440, 164, 26, 260, 13, WOOD_D),
)

NEW_ARTS["s_x"] = wrap(  # x：切开的西瓜（叉状瓜纹）
    ground(),
    P("M 232 112 L 528 402", stroke=RED, w=52),
    P("M 528 112 L 232 402", stroke=BLUE, w=52),
    C(232, 112, 26, SUN), C(528, 112, 26, SUN),
)

NEW_ARTS["s_z"] = wrap(  # z：小鸭子游成 2 字形（脖子弯 + 圆背 + 底横水纹）
    ground(),
    P("M 214 126 L 548 126 L 226 364 L 560 364", stroke=SUN, w=48),
    P("M 230 114 L 566 114", stroke=YEL_D, w=12),
    P("M 210 378 L 548 378", stroke=YEL_D, w=12),
)

NEW_ARTS["s_c"] = wrap(  # c：弯月牙
    R(0, 0, 760, 480, 0, "#3c4a6b"),
    C(560, 130, 5, WHITE, 0.9), C(640, 220, 4, WHITE, 0.7), C(120, 90, 5, WHITE, 0.8),
    C(200, 300, 4, WHITE, 0.6), C(680, 90, 4, WHITE, 0.7),
    C(400, 250, 150, SUN_L), C(452, 236, 132, "#3c4a6b"),
)

NEW_ARTS["s_s"] = wrap(  # s：小蛇蜿蜒
    ground(),
    P("M 240 130 Q 400 90 470 170 Q 540 250 420 280 Q 300 310 370 370 Q 420 408 540 386",
      stroke=GREEN, w=44),
    P("M 240 130 Q 400 90 470 170 Q 540 250 420 280 Q 300 310 370 370 Q 420 408 540 386",
      stroke=GREEN_L, w=18),
    C(560, 390, 40, GREEN), C(576, 378, 9, WHITE), C(579, 380, 4.5, INK),
    P("M 600 400 L 634 410 L 602 418 Q 606 408 600 400 Z", RED_D),
    P("M 548 366 Q 556 372 552 380", stroke=INK, w=5),
)

NEW_ARTS["s_r"] = wrap(  # r：小苗发芽
    ground(),
    P("M 332 420 L 332 176", stroke=GREEN, w=24),
    E(332, 424, 60, 14, WOOD_D),
    P("M 334 250 Q 388 174 486 206 Q 510 214 486 226 Q 410 264 338 278", fill=GREEN_L),
)

NEW_ARTS["s_y"] = wrap(  # y：树杈
    ground(),
    P("M 380 430 L 380 250", stroke=WOOD_D, w=30),
    P("M 380 260 Q 320 180 250 120", stroke=WOOD_D, w=24),
    P("M 380 260 Q 440 180 520 130", stroke=WOOD_D, w=24),
    E(380, 434, 60, 13, WOOD_D),
)

NEW_ARTS["s_w"] = wrap(  # w：一条 W 形缎带（斜下斜上两次＝∨∨），中间停一只乌鸦（乌＝鸟）
    ground(),
    P("M 185 168 L 287 412 L 380 168 L 482 412 L 575 168", stroke=RED, w=34),
    C(185, 168, 19, RED_D), C(575, 168, 19, RED_D),
    P("M 352 116 L 306 142 L 348 142 Z", fill="#3a3a3a"),
    R(340, 96, 62, 40, 20, "#3a3a3a"),
    C(392, 92, 19, "#3a3a3a"),
    P("M 406 88 L 436 96 L 406 104 Z", fill=YEL),
    C(397, 86, 5, "#ffffff"),
    R(346, 100, 40, 20, 10, "#4d4d4d"),
    E(380, 436, 190, 18, lib.GROUND, 0.6),
)

NEW_ARTS["s_ei"] = wrap(  # ei：一只一眼就能认出的黑猫，提示“黑”
    ground(),
    E(376, 314, 122, 82, "#3d3937"),
    C(372, 208, 78, "#3d3937"),
    PG([(314, 164), (332, 92), (368, 158)], "#3d3937"),
    PG([(376, 158), (420, 92), (432, 174)], "#3d3937"),
    C(344, 202, 12, WHITE), C(400, 202, 12, WHITE),
    C(346, 204, 5, INK), C(402, 204, 5, INK),
    PG([(370, 224), (386, 224), (378, 238)], PINK),
    P("M 486 324 Q 570 270 548 212", stroke="#3d3937", w=24),
    R(308, 372, 34, 52, 15, "#3d3937"), R(418, 372, 34, 52, 15, "#3d3937"),
)

NEW_ARTS["s_ang"] = wrap(  # ang：羊身、羊头、四条腿完整可辨
    ground(),
    E(344, 288, 170, 98, "#f1dfba"),
    C(220, 280, 54, WOOD_L),
    E(176, 250, 34, 18, WOOD_L), E(258, 250, 34, 18, WOOD_L),
    P("M 188 246 Q 166 206 202 196", stroke=SUN, w=12),
    P("M 252 246 Q 278 206 242 196", stroke=SUN, w=12),
    C(202, 270, 7, INK), C(238, 270, 7, INK),
    P("M 208 298 Q 220 308 232 298", stroke=INK, w=5),
    R(270, 360, 24, 64, 12, WOOD_L), R(350, 360, 24, 64, 12, WOOD_L),
    R(430, 360, 24, 64, 12, WOOD_L), R(500, 350, 24, 74, 12, WOOD_L),
)

NEW_ARTS["s_ying"] = wrap(  # ying：张开双翅的鹰，不再用普通小鸟代替
    ground(),
    P("M 352 246 Q 238 142 112 208 Q 202 298 330 318 Z", fill=WOOD_D),
    P("M 408 246 Q 522 142 648 208 Q 558 298 430 318 Z", fill=WOOD_D),
    E(380, 286, 64, 102, WOOD),
    C(380, 174, 58, WHITE),
    C(360, 170, 8, INK), C(400, 170, 8, INK),
    PG([(362, 194), (398, 194), (380, 224)], SUN),
    P("M 360 390 L 340 424 M 400 390 L 420 424", stroke=SUN, w=12),
)

# zh/ch/sh 用“前一个字母 + h”的结构图，不再用猪/茶/山这类只表达词义的图片。
NEW_ARTS["s_zh"] = wrap(  # zh：z + h
    ground(),
    R(92, 122, 250, 250, 26, "#fbeecb"), R(418, 122, 250, 250, 26, "#d9f0ea"),
    P("M 140 178 L 290 178 L 140 316 L 290 316", stroke=RED_D, w=26),
    P("M 474 156 L 474 320 M 474 248 Q 520 204 578 232 Q 606 244 606 278 L 606 320", stroke=TEAL_D, w=24),
    P("M 342 246 L 418 246", stroke=YEL_D, w=12),
)
NEW_ARTS["s_ch"] = wrap(  # ch：c + h
    ground(),
    R(92, 122, 250, 250, 26, "#fbeecb"), R(418, 122, 250, 250, 26, "#d9f0ea"),
    P("M 286 178 Q 156 178 156 246 Q 156 316 286 316", stroke=RED_D, w=26),
    P("M 474 156 L 474 320 M 474 248 Q 520 204 578 232 Q 606 244 606 278 L 606 320", stroke=TEAL_D, w=24),
    P("M 342 246 L 418 246", stroke=YEL_D, w=12),
)
NEW_ARTS["s_sh"] = wrap(  # sh：s + h
    ground(),
    R(92, 122, 250, 250, 26, "#fbeecb"), R(418, 122, 250, 250, 26, "#d9f0ea"),
    P("M 286 178 Q 156 178 156 236 Q 156 278 276 278 Q 286 316 156 316", stroke=RED_D, w=26),
    P("M 474 156 L 474 320 M 474 248 Q 520 204 578 232 Q 606 244 606 278 L 606 320", stroke=TEAL_D, w=24),
    P("M 342 246 L 418 246", stroke=YEL_D, w=12),
)

NEW_ARTS["s_a"] = wrap(  # a：阿姨挥手问好（张嘴发 a；kid 原生人物组件）
    ground(),
    lib.kid(380, 446, s=1.05, face="open", arms="up", shirt=lib.RED, bun=True, skirt=True),
)

NEW_ARTS["s_t"] = wrap(  # t：伞柄向下——平直的伞沿＝t 的横，直伞杆＝竖，伞柄弯钩＝竖右弯；伞面压低更显"撑开"
    ground(),
    P("M 316 210 Q 390 166 464 210", stroke=RED_D, w=13),
    L(310, 212, 470, 212, RED, 22),
    L(390, 146, 390, 384, "#3f89c9", 22),
    P("M 390 384 Q 390 436 444 426", stroke="#3f89c9", w=22),
    E(390, 436, 190, 18, lib.GROUND, 0.6),
)

NEW_ARTS["s_o"] = wrap(
    ground(), C(380, 236, 150, SKIN), C(380, 270, 62, RED_D), C(380, 270, 34, INK),
    C(330, 188, 10, INK), C(430, 188, 10, INK),
)
NEW_ARTS["s_e"] = wrap(
    ground(), C(380, 236, 150, SKIN),
    P("M 304 272 Q 380 244 456 272 Q 380 304 304 272 Z", RED_D),
    L(326, 272, 434, 272, WHITE, 10), C(330, 188, 10, INK), C(430, 188, 10, INK),
)
NEW_ARTS["s_i"] = wrap(
    ground(), C(380, 236, 150, SKIN),
    R(306, 250, 148, 54, 27, RED_D), R(324, 260, 112, 28, 10, WHITE),
    L(330, 274, 430, 274, INK, 5), C(330, 188, 10, INK), C(430, 188, 10, INK),
)
NEW_ARTS["s_ü"] = wrap(
    ground(), C(380, 236, 150, SKIN), C(380, 270, 42, RED_D), C(380, 270, 20, INK),
    C(330, 188, 10, INK), C(430, 188, 10, INK),
    C(486, 194, 16, WBLUE, 0.9), C(522, 154, 11, WBLUE, 0.7),
)

NEW_ARTS["s_yuan"] = wrap(
    ground(), C(380, 244, 154, TEAL_D, 0.22), C(372, 236, 146, TEAL),
    C(330, 194, 30, WHITE, 0.65), E(380, 430, 176, 22, lib.GROUND, 0.55),
)

NEW_ARTS["s_u"] = wrap(  # u：嘴唇明显向前突出
    ground(), C(380, 236, 150, SKIN),
    E(380, 270, 48, 62, RED_D), E(380, 270, 22, 34, INK),
    C(330, 188, 10, INK), C(430, 188, 10, INK),
)

# ---------------- 四声卡小图（8 张） ----------------
NEW_ARTS["t_b2"] = wrap(  # bá 拔萝卜
    ground(),
    C(380, 260, 96, RED_D, 0.3), C(376, 254, 92, RED),
    P("M 340 190 Q 376 150 412 190 L 400 130 L 352 130 Z", GREEN),
    P("M 356 150 L 376 96 M 396 150 L 380 100", stroke=GREEN, w=14),
    P("M 320 210 Q 260 240 280 300", stroke=SKIN, w=26),
    P("M 432 210 Q 492 240 472 300", stroke=SKIN, w=26),
    P("M 300 330 Q 376 366 452 330", stroke=WOOD_D, w=10),
)
NEW_ARTS["t_b3"] = wrap(  # bǎ 靶心
    ground(),
    C(380, 240, 130, "#8a5a33"), C(380, 240, 112, WHITE),
    C(380, 240, 86, RED), C(380, 240, 58, WHITE), C(380, 240, 30, RED),
    P("M 560 90 L 420 226", stroke=WOOD, w=12),
    P("M 420 226 L 448 210 L 434 240 Z", "#9aa3a8"),
    R(560, 80, 20, 60, 8, RED),
)
NEW_ARTS["t_m2"] = wrap(  # má 麻花
    ground(),
    P("M 240 240 Q 300 170 360 240 Q 420 310 480 240 Q 540 170 560 240",
      stroke="#d99a4e", w=52),
    P("M 240 240 Q 300 170 360 240 Q 420 310 480 240 Q 540 170 560 240",
      stroke="#e9b97e", w=22),
    C(230, 244, 26, "#c98a3e"), C(566, 244, 26, "#c98a3e"),
)
NEW_ARTS["t_m4"] = wrap(  # mà 蚂蚱
    ground(),
    E(380, 280, 130, 60, GREEN_D if hasattr(lib, "GREEN_D") else "#5d8a4e"),
    C(490, 240, 44, "#6f9e5e"),
    C(502, 228, 10, INK), C(522, 218, 10, INK),
    P("M 512 214 L 536 188 M 528 222 L 552 200", stroke="#5d8a4e", w=7),
    P("M 300 262 Q 380 200 470 236", stroke="#5d8a4e", w=18),
    P("M 330 300 Q 380 356 460 330", stroke="#5d8a4e", w=14),
    P("M 420 288 L 470 366", stroke="#5d8a4e", w=10),
)
NEW_ARTS["t_d1"] = wrap(  # dā 搭积木
    ground(),
    R(280, 320, 200, 70, 12, RED), R(300, 250, 160, 66, 12, BLUE),
    R(330, 184, 100, 62, 12, SUN),
    C(430, 150, 26, TEAL),
    kid(600, 434, s=0.6, face="open", arms="up", look=(-60, 0)),
)
NEW_ARTS["t_d2"] = wrap(  # dá 举手回答
    ground(),
    R(220, 260, 320, 140, 18, "#e7d3ac"),
    kid(580, 432, s=0.85, face="open", arms="up", shirt=TEAL, look=(-40, -4)),
    C(286, 220, 14, SUN), C(340, 180, 11, SUN_L, 0.9),
)
NEW_ARTS["t_w2"] = wrap(  # wú 空盘子
    ground(),
    E(380, 300, 190, 84, "#d9d0c5", 0.4), E(376, 292, 184, 80, WHITE),
    E(376, 292, 120, 48, "#f2efe4"),
    P("M 330 258 Q 376 276 422 258", stroke="#c9c4b4", w=6),
    kid(620, 434, s=0.55, face="o", arms="cross", look=(-50, 4)),
)
NEW_ARTS["t_w4"] = wrap(  # wù 雾
    ground(),
    R(140, 300, 480, 110, 40, "#cfd8de", 0.9),
    E(240, 320, 120, 48, "#dfe6ea", 0.9), E(430, 300, 140, 54, "#e8eef1", 0.9),
    P("M 250 300 L 250 220 M 250 240 Q 220 200 250 170 Q 284 200 258 236", stroke="#8fa3ad", w=12),
    E(380, 428, 240, 22, lib.GROUND, 0.6),
)

# ---------------- 卡片数据 ----------------
def L_(letter, tip, jue, scene=None, ref=None, combo=None, kind="initial"):
    audio_letter = letter.replace("ü", "v")
    return {"letter": letter, "type": "letter", "kind": kind, "tip": tip, "jue": jue,
            "scene": scene, "ref": ref, "combo": combo, "audio": f"L_{audio_letter}"}


def S_(sound, kind, tip, jue, ref=None, scene=None, parts=None):
    """复韵母、鼻韵母和整体认读音节卡。"""
    audio_sound = sound.replace("ü", "v")
    return {"key": f"S_{audio_sound}", "type": "sound", "sound": sound, "kind": kind,
            "tip": tip, "jue": jue, "ref": ref, "scene": scene,
            "parts": parts or list(sound), "audio": f"L_{audio_sound}"}

INITIAL_CARDS = [
    L_("b", "嘴唇抿紧再弹开，像蹦出一颗小豆子", "右下半圆 b b b", scene="s_b"),
    L_("p", "嘴唇弹开送气，放张纸巾会被吹动", "右上半圆 p p p", scene="s_p"),
    L_("m", "嘴巴闭紧，从鼻子里哼出来", "两个门洞 m m m", scene="s_m"),
    L_("f", "上牙轻轻咬住下唇，轻轻送气", "拐杖加横 f f f", scene="s_f"),
    L_("d", "舌尖顶住上牙再弹开", "左下半圆 d d d", scene="s_d"),
    L_("t", "舌尖弹开，送出一股强气流", "伞柄向下 t t t", scene="s_t"),
    L_("n", "气流从鼻子里出来", "一个门洞 n n n", scene="s_n"),
    L_("l", "舌尖顶住上膛，喉咙响", "一根小棍 l l l", scene="s_l"),
    L_("g", "舌根抬起来再放开，气流不强", "蝌蚪弯尾 ɡ ɡ ɡ", scene="s_g"),
    L_("k", "像 g，但气流冲得更强", "直茎分叉 k k k", scene="s_k"),
    L_("h", "像喝水一样从喉咙吹气", "一把椅子 h h h", scene="s_h"),
    L_("j", "嘴巴扁扁，舌面抬起来", "竖弯加点 j j j", scene="s_j"),
    L_("q", "像 j，但气流冲得更强", "左上半圆 q q q", scene="s_q"),
    L_("x", "嘴角拉开像笑，轻轻送气", "一个大叉 x x x", scene="s_x"),
    L_("zh", "z 后面接 h，舌尖卷起，读 zh", "z + h，合成 zh", scene="s_zh", combo=("z", "h")),
    L_("ch", "c 后面接 h，舌尖卷起，送气读 ch", "c + h，合成 ch", scene="s_ch", combo=("c", "h")),
    L_("sh", "s 后面接 h，舌尖卷起，读 sh", "s + h，合成 sh", scene="s_sh", combo=("s", "h")),
    L_("r", "像 sh，但喉咙要振动", "小树发芽 r r r", scene="s_r"),
    L_("z", "舌尖抵住上齿背，气流从窄缝出去", "折线闪电 z z z", scene="s_z"),
    L_("c", "像 z，但气流冲得更强", "半个圆圈 c c c", scene="s_c"),
    L_("s", "舌尖放平，像蛇一样嘶嘶", "半个 8 字 s s s", scene="s_s"),
]

# 2024 秋季启用的修订版统编一年级教材明确按 21 个声母教学；y、w 是
# i、u 开头的零声母音节在书写时使用的字母，单列学习，不能继续标成声母。
YW_CARDS = [
    L_("y", "i 开头的音节前面写 y；读音像“衣”", "树杈 y y y", scene="s_y", kind="spelling"),
    L_("w", "u 开头的音节前面写 w；读音像“乌”", "两弯相连 w w w", scene="s_w", kind="spelling"),
]

FINAL_CARDS = [
    L_("a", "张大嘴巴 ɑ ɑ ɑ", "阿姨问好 a a a", scene="s_a", kind="final"),
    L_("o", "嘴巴拢圆，舌头往后缩", "公鸡喔喔 o o o", ref="鸡", kind="final"),
    L_("e", "嘴巴自然张开，嘴角向两边", "白鹅唱歌 e e e", ref="鹅", kind="final"),
    L_("i", "上下牙齿对齐，嘴角向两边", "一件衣服 i i i", ref="衣", kind="final"),
    L_("u", "嘴巴突出 u u u，乌鸦飞呀飞", "乌鸦飞呀 u u u", ref="乌", kind="final"),
    L_("ü", "舌位像 i，嘴唇像吹口哨一样拢圆", "小鱼吐泡 ü ü ü", ref="鱼", kind="final"),
]

COMPOUND_FINAL_CARDS = [
    S_("ai", "compound_final", "先发 a，再快速滑向 i", "a + i → ai（海）", ref="海", parts=["a", "i"]),
    S_("ei", "compound_final", "先发 e，再快速滑向 i", "e + i → ei（黑）", scene="s_ei", parts=["e", "i"]),
    S_("ui", "compound_final", "由 u 很快滑向 i；实际是 uei 的简写", "u + i → ui（水）", ref="水", parts=["u", "i"]),
    S_("ao", "compound_final", "嘴巴由大到圆，从 a 滑向 o", "a + o → ao（猫）", ref="猫", parts=["a", "o"]),
    S_("ou", "compound_final", "先发 o，再收向 u", "o + u → ou（手）", ref="手", parts=["o", "u"]),
    S_("iu", "compound_final", "由 i 很快滑向 u；实际是 iou 的简写", "i + u → iu（球）", ref="球", parts=["i", "u"]),
    S_("ie", "compound_final", "先发 i，再滑向 e", "i + e → ie（叶）", ref="叶", parts=["i", "e"]),
    S_("üe", "compound_final", "先发 ü，再滑向 e", "ü + e → üe（月）", ref="月", parts=["ü", "e"]),
    S_("er", "special_final", "舌尖向后卷，er 可以单独成音节", "特殊韵母 er（耳）", ref="耳", parts=["e", "r"]),
]

NASAL_FINAL_CARDS = [
    S_("an", "front_nasal", "结尾舌尖抵住上齿龈", "前鼻韵母 an（山）", ref="山", parts=["a", "n"]),
    S_("en", "front_nasal", "结尾舌尖抵住上齿龈", "前鼻韵母 en（门）", ref="门", parts=["e", "n"]),
    S_("in", "front_nasal", "由 i 滑向前鼻音 n", "前鼻韵母 in（林）", ref="林", parts=["i", "n"]),
    S_("un", "front_nasal", "实际由 uen 简写而来", "前鼻韵母 un（春）", ref="春", parts=["u", "n"]),
    S_("ün", "front_nasal", "由 ü 滑向前鼻音 n", "前鼻韵母 ün（云）", ref="云", parts=["ü", "n"]),
    S_("ang", "back_nasal", "结尾舌根抬起，气流从鼻腔出来", "后鼻韵母 ang（羊）", scene="s_ang", parts=["a", "n", "g"]),
    S_("eng", "back_nasal", "结尾舌根抬起，不要读成 en", "后鼻韵母 eng（灯）", ref="灯", parts=["e", "n", "g"]),
    S_("ing", "back_nasal", "由 i 滑向后鼻音 ng", "后鼻韵母 ing（星）", ref="星", parts=["i", "n", "g"]),
    S_("ong", "back_nasal", "嘴唇拢圆，结尾发后鼻音 ng", "后鼻韵母 ong（钟）", ref="钟", parts=["o", "n", "g"]),
]

WHOLE_CARDS = [
    S_("zhi", "whole", "整体认读，不拆开拼", "整体认读 zhi（纸）", ref="纸", parts=["zh", "i"]),
    S_("chi", "whole", "整体认读，不拆开拼", "整体认读 chi（吃）", ref="吃", parts=["ch", "i"]),
    S_("shi", "whole", "整体认读，不拆开拼", "整体认读 shi（狮）", ref="狮", parts=["sh", "i"]),
    S_("ri", "whole", "整体认读，不拆开拼", "整体认读 ri（日）", ref="日", parts=["r", "i"]),
    S_("zi", "whole", "整体认读，不拆开拼", "整体认读 zi（字）", ref="字", parts=["z", "i"]),
    S_("ci", "whole", "整体认读，不拆开拼", "整体认读 ci（词）", ref="词", parts=["c", "i"]),
    S_("si", "whole", "整体认读，不拆开拼", "整体认读 si（四）", ref="四", parts=["s", "i"]),
    S_("yi", "whole", "整体认读，不拆开拼", "整体认读 yi（衣）", ref="衣", parts=["y", "i"]),
    S_("wu", "whole", "整体认读，不拆开拼", "整体认读 wu（五）", ref="五", parts=["w", "u"]),
    S_("yu", "whole", "整体认读；yu 里的 u 实际是 ü，省去两点", "整体认读 yu（鱼）", ref="鱼", parts=["y", "u"]),
    S_("ye", "whole", "整体认读，不拆开拼", "整体认读 ye（叶）", ref="叶", parts=["y", "e"]),
    S_("yue", "whole", "整体认读；y 后面的 ue 实际来自 üe", "整体认读 yue（月）", ref="月", parts=["y", "u", "e"]),
    S_("yuan", "whole", "整体认读；不要逐字母拼读", "整体认读 yuan（圆）", scene="s_yuan", parts=["y", "u", "a", "n"]),
    S_("yin", "whole", "整体认读，不拆开拼", "整体认读 yin（音）", ref="音", parts=["y", "i", "n"]),
    S_("yun", "whole", "整体认读；yun 中的 u 实际是 ü", "整体认读 yun（云）", ref="云", parts=["y", "u", "n"]),
    S_("ying", "whole", "整体认读，不拆开拼", "整体认读 ying（鹰）", scene="s_ying", parts=["y", "i", "n", "g"]),
]

ALL_FINAL_CARDS = FINAL_CARDS + COMPOUND_FINAL_CARDS + NASAL_FINAL_CARDS
FULL_CARDS = INITIAL_CARDS + YW_CARDS + ALL_FINAL_CARDS + WHOLE_CARDS

TONE_CARDS = [
    {"key": "tone_1", "type": "tone", "tone": 1, "label": "一声（阴平）", "mark": "ˉ",
     "vowels": "ā ō ē ī ū ǖ", "tip": "声音高而平，像小车走平路", "audio": "TONE_1",
     "words": [{"sy": "mā", "zi": "妈", "ref": "妈"}, {"sy": "yī", "zi": "衣", "ref": "衣"}, {"sy": "wū", "zi": "乌", "ref": "乌"}]},
    {"key": "tone_2", "type": "tone", "tone": 2, "label": "二声（阳平）", "mark": "ˊ",
     "vowels": "á ó é í ú ǘ", "tip": "声音由低往高扬，像小车上坡", "audio": "TONE_2",
     "words": [{"sy": "é", "zi": "鹅", "ref": "鹅"}, {"sy": "yú", "zi": "鱼", "ref": "鱼"}, {"sy": "yáng", "zi": "羊", "ref": "羊"}]},
    {"key": "tone_3", "type": "tone", "tone": 3, "label": "三声（上声）", "mark": "ˇ",
     "vowels": "ǎ ǒ ě ǐ ǔ ǚ", "tip": "声音先降再升，像小车下坡再上坡", "audio": "TONE_3",
     "words": [{"sy": "mǎ", "zi": "马", "ref": "马"}, {"sy": "wǔ", "zi": "五", "ref": "五"}, {"sy": "yǔ", "zi": "雨", "ref": "雨"}]},
    {"key": "tone_4", "type": "tone", "tone": 4, "label": "四声（去声）", "mark": "ˋ",
     "vowels": "à ò è ì ù ǜ", "tip": "声音从高处快速降下，像小车下坡", "audio": "TONE_4",
     "words": [{"sy": "bà", "zi": "爸", "ref": "爸"}, {"sy": "tù", "zi": "兔", "ref": "兔"}, {"sy": "shù", "zi": "树", "ref": "树"}]},
    {"key": "tone_0", "type": "tone", "tone": 0, "label": "轻声", "mark": "·",
     "vowels": "轻、短、不标调号", "tip": "轻声不是第五声；它读得轻而短，调值随前一个音节变化", "audio": "TONE_0",
     "words": [{"sy": "māma", "zi": "妈妈", "ref": "妈"}, {"sy": "bàba", "zi": "爸爸", "ref": "爸"}, {"sy": "háizi", "zi": "孩子", "ref": "子"}]},
]

CONTRAST_CARDS = [
    {"key": "C_bdpq", "type": "contrast", "label": "b d p q", "items": ["b", "d", "p", "q"], "audio": "C_bdpq",
     "tip": "先看竖在哪边，再看半圆在上还是在下。"},
    {"key": "C_ft", "type": "contrast", "label": "f 和 t", "items": ["f", "t"], "audio": "C_ft",
     "tip": "f 的长竖进上格；t 的短竖只略高出第二线。"},
    {"key": "C_mn", "type": "contrast", "label": "m 和 n", "items": ["m", "n"], "audio": "C_mn",
     "tip": "m 有两个门洞，n 只有一个门洞。"},
    {"key": "C_zzh", "type": "contrast", "label": "z 和 zh", "items": ["z", "zh"], "audio": "C_zzh",
     "tip": "多一个 h 就要卷舌；先看清字形，再听平舌和翘舌。"},
    {"key": "C_cch", "type": "contrast", "label": "c 和 ch", "items": ["c", "ch"], "audio": "C_cch",
     "tip": "c 是平舌音，ch 多一个 h，是送气的翘舌音。"},
    {"key": "C_ssh", "type": "contrast", "label": "s 和 sh", "items": ["s", "sh"], "audio": "C_ssh",
     "tip": "s 是平舌音，sh 多一个 h，要把舌尖卷起来。"},
    {"key": "C_uv", "type": "contrast", "label": "u 和 ü", "items": ["u", "ü"], "audio": "C_uv",
     "tip": "ü 比 u 多两点；发 ü 时舌位像 i，嘴唇仍拢圆。"},
]

# 首音配对（C）：ref=识字卡现成插画；art=新插画
MATCH_CARDS = [
    {"letter": "b", "zi": "爸", "py": "bà", "ref": "爸", "hint": "猜猜：它的名字开头是哪个字母？"},
    {"letter": "p", "zi": "爬", "py": "pá", "ref": "爬"},
    {"letter": "m", "zi": "马", "py": "mǎ", "ref": "马"},
    {"letter": "f", "zi": "饭", "py": "fàn", "ref": "饭"},
    {"letter": "d", "zi": "蛋", "py": "dàn", "ref": "蛋"},
    {"letter": "t", "zi": "兔", "py": "tù", "ref": "兔"},
    {"letter": "n", "zi": "牛", "py": "niú", "ref": "牛"},
    {"letter": "l", "zi": "鹿", "py": "lù", "ref": "鹿"},
    {"letter": "g", "zi": "狗", "py": "gǒu", "ref": "狗"},
    {"letter": "k", "zi": "哭", "py": "kū", "ref": "哭"},
    {"letter": "h", "zi": "虎", "py": "hǔ", "ref": "虎"},
    {"letter": "j", "zi": "鸡", "py": "jī", "ref": "鸡"},
    {"letter": "q", "zi": "七", "py": "qī", "ref": "七"},
    {"letter": "x", "zi": "象", "py": "xiàng", "ref": "象"},
    {"letter": "zh", "zi": "猪", "py": "zhū", "ref": "猪"},
    {"letter": "ch", "zi": "车", "py": "chē", "ref": "车"},
    {"letter": "sh", "zi": "山", "py": "shān", "ref": "山"},
    {"letter": "r", "zi": "日", "py": "rì", "ref": "日"},
    {"letter": "z", "zi": "坐", "py": "zuò", "ref": "坐"},
    {"letter": "c", "zi": "草", "py": "cǎo", "ref": "草"},
    {"letter": "s", "zi": "伞", "py": "sǎn", "ref": "伞"},
    {"letter": "y", "zi": "羊", "py": "yáng", "ref": "羊"},
    {"letter": "w", "zi": "蛙", "py": "wā", "ref": "蛙"},
    {"letter": "a", "zi": "阿姨", "py": "ā yí", "art": "s_a", "hint": "张大嘴巴 ɑ ɑ ɑ"},
    {"letter": "o", "zi": "公鸡", "py": "gōng jī", "ref": "鸡", "hint": "喔喔啼 o o o"},
    {"letter": "e", "zi": "白鹅", "py": "bái é", "ref": "鹅", "hint": "扁扁嘴巴 e e e"},
    {"letter": "i", "zi": "衣", "py": "yī", "ref": "衣", "hint": "牙齿对齐 i i i"},
    {"letter": "u", "zi": "乌鸦", "py": "wū yā", "art": "s_u", "hint": "嘴巴突出 u u u"},
    {"letter": "ü", "zi": "鱼", "py": "yú", "ref": "鱼", "hint": "嘴吹口哨 ü ü ü"},
]

# 拼读卡（D）：韵母 × 声母 → 库内字，由构建器从 422 字库自动匹配生成 chips
SPELL_RULES = {
    "ü": "j q x y 碰到 ü，两点要省去：ju qu xu yu",
}

SETS = [
    {
        "file": "拼音字母卡.html",
        "kind": "letter",
        "title": "拼音字母卡",
        "sub": "逐卡认读 · 自动发音 · 易混对照",
        "accent": "#3e9486",
        "groups": [
            {"id": "initial", "name": "声母 21", "cards": INITIAL_CARDS},
            {"id": "spelling", "name": "y / w 2", "cards": YW_CARDS},
            {"id": "final", "name": "韵母 24", "cards": ALL_FINAL_CARDS},
            {"id": "whole", "name": "整体认读 16", "cards": WHOLE_CARDS},
            {"id": "full", "name": "完整拼音表 63", "cards": FULL_CARDS},
            {"id": "tone", "name": "声调五类", "cards": TONE_CARDS},
            {"id": "contrast", "name": "易混对照", "cards": CONTRAST_CARDS},
        ],
    },
    {
        "file": "拼音拼读卡.html",
        "kind": "spell",
        "title": "拼音拼读卡",
        "sub": "音形配对 · 拼读游乐场",
        "accent": "#4a90c9",
        "groups": [
            {"id": "match", "name": "首音配对", "cards": MATCH_CARDS},
            {"id": "spell", "name": "拼读", "cards": "AUTO_SPELL"},
        ],
    },
]
