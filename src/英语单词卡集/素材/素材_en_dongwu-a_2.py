#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 动物·陆地（dongwu-a）第 2 段插画（pig~kangaroo，共 10 卡）。

全部侧面全身像，底边落地 y≈430 一带，主体高约画布 60%~73%：
粉猪圆鼻卷尾(站) / 白底大黑斑奶牛(粉吻小角大奶) / 棕马立鬃扬尾(长脸) /
乳白云卷毛羊黑脸黑腿(朝右) / 红狐坐姿尖耳蓬尾白尖 / 灰狼立耳仰头嚎叫(垂尾朝右) /
棕鹿枝角白斑点细腿 / 黄长颈鹿头顶双角伸脖吃高处树叶 / 黑白条纹斑马立鬃(朝右) /
棕红袋鼠立姿粗尾拖地、育儿袋露小袋鼠头。
相邻卡主色与轮廓错开；cow 与 sheep 均偏白，以大块黑斑 vs 云纹卷毛区分质感。
"""
import sys

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

# ---------- 本段同族补充色 ----------
PINK_D, PINK_L = "#e08a6d", "#fbd0c0"                      # 粉猪深/浅
COW_W, COW_WD, COW_H, COW_E = "#f6f3e8", "#ded7c4", "#efe3c2", "#5c534a"  # 奶牛
HOR, HOR_D, HOR_L = "#c09062", "#a9743f", "#e3bd90"        # 棕马
WOOL, WOOL_D = "#f5efdf", "#ddd2ba"                        # 羊毛乳白
FACE, FACE_D = "#5a4a3c", "#483a2e"                        # 羊黑脸
FOX_W = "#f7ead8"                                          # 狐白胸尾尖
WOLF, WOLF_D, WOLF_L = "#a3adb8", "#84909c", "#d3dae1"     # 灰狼
DEER, DEER_D, DEER_L = "#cf9a63", "#b5804a", "#f0e0c2"     # 梅花鹿
ZEB, ZEB_D = "#f4f1e6", "#dcd6c6"                          # 斑马白底
KAN, KAN_D, KAN_L = "#cd7d45", "#b06432", "#ecc9a2"        # 袋鼠棕红
GIR_P = "#c08a4a"                                          # 长颈鹿网纹棕


# ---------- 小工具 ----------
def eye(cx, cy, rx=9, ry=11, dark=INK):
    """侧脸单眼：INK 色竖椭圆 + 左上小白高光。"""
    return E(cx, cy, rx, ry, dark) + C(cx - 3, cy - 4, 2.8, WHITE)


def smile(cx, cy, w=14, d=8, dark=INK, sw=4):
    return P(f"M {cx - w} {cy} Q {cx} {cy + d} {cx + w} {cy}", stroke=dark, w=sw)


def body_e(cx, cy, rx, ry, main, dark):
    """侧身椭圆：深一号底偏右下制造体积。"""
    return E(cx + rx * 0.05, cy + ry * 0.12, rx, ry, dark) + E(cx, cy, rx, ry, main)


def head_c(cx, cy, r, main, dark):
    return C(cx + r * 0.07, cy + r * 0.13, r, dark) + C(cx, cy, r, main)


def legq(x, y, w, h, main, hoof, hoof_h=14):
    return R(x, y, w, h, w * 0.45, main) + R(x, y + h - hoof_h, w, hoof_h, hoof_h * 0.45, hoof)


def tuft(x, y, s=1.0):
    """地面两笔小草。"""
    return (P(f"M {x} {y} Q {x - 9 * s} {y - 26 * s} {x - 3 * s} {y - 38 * s}", stroke=GREEN, w=7 * s)
            + P(f"M {x + 13 * s} {y} Q {x + 18 * s} {y - 20 * s} {x + 11 * s} {y - 30 * s}",
                stroke=GREEN_L, w=6 * s))


GROUP_CARDS = [
    {"w": "pig", "cn": "猪"},
    {"w": "cow", "cn": "奶牛"},
    {"w": "horse", "cn": "马"},
    {"w": "sheep", "cn": "绵羊"},
    {"w": "fox", "cn": "狐狸"},
    {"w": "wolf", "cn": "狼"},
    {"w": "deer", "cn": "鹿"},
    {"w": "giraffe", "cn": "长颈鹿"},
    {"w": "zebra", "cn": "斑马"},
    {"w": "kangaroo", "cn": "袋鼠"},
]


# ---------- 各卡插画 ----------
def art_pig():
    g = ground()
    # 卷小尾巴（本卡特征）
    g += P("M 524 330 Q 566 312 574 344 Q 580 372 552 374 Q 536 374 540 358 Q 543 348 552 352",
           stroke=PINK_D, w=9)
    # 短腿
    for x in (306, 348, 470, 512):
        g += legq(x, 384, 26, 58, PINK, PINK_D)
    # 圆胖身
    g += body_e(400, 326, 128, 86, PINK, PINK_D)
    # 前折耳（画在头后）
    g += (f'<g transform="rotate(-18 302 172)">'
          + P("M 282 196 Q 286 138 318 132 Q 340 150 322 200 Q 300 214 282 196 Z", PINK_D)
          + P("M 294 190 Q 298 152 316 148 Q 328 160 316 192 Q 304 202 294 190 Z", PINK_L)
          + "</g>")
    # 头
    g += head_c(262, 238, 72, PINK, PINK_D)
    # 圆猪鼻 + 双鼻孔（本卡特征）
    g += E(200, 262, 34, 27, "#ee9179") + E(189, 262, 6, 10, "#c56a50") + E(211, 262, 6, 10, "#c56a50")
    # 眼 / 嘴 / 腮
    g += eye(240, 220, 9, 12)
    g += smile(242, 296, 16, 8)
    g += C(294, 262, 11, PINK_L, 0.9)
    g += tuft(150, 448) + tuft(642, 448)
    return g


def art_cow():
    g = ground()
    # 尾 + 黑穗
    g += P("M 566 292 Q 598 330 586 388", stroke=COW_WD, w=12) + C(586, 396, 13, INK)
    # 四腿（深蹄）
    for x in (302, 346, 484, 526):
        g += legq(x, 376, 28, 66, COW_W, "#54493e")
    # 大方身
    g += body_e(428, 318, 150, 94, COW_W, COW_WD)
    # 大块黑斑（本卡主角：与羊的云纹卷毛区分）
    g += P("M 352 258 Q 414 234 458 266 Q 478 298 446 322 Q 402 344 362 320 Q 330 294 352 258 Z", INK)
    g += P("M 474 352 Q 512 336 536 360 Q 548 386 514 398 Q 480 404 466 384 Q 458 366 474 352 Z", INK)
    g += C(336, 368, 24, INK)
    # 粉乳房
    g += E(502, 412, 32, 20, PINK) + C(494, 428, 5, PINK) + C(512, 428, 5, PINK)
    # 颈 + 头
    g += P("M 330 262 Q 300 236 272 218", stroke=COW_WD, w=54)
    g += P("M 326 256 Q 298 232 272 214", stroke=COW_W, w=44)
    g += head_c(252, 210, 64, COW_W, COW_WD)
    # 小弯角
    g += P("M 222 152 Q 214 126 232 120 Q 238 138 234 154 Z", COW_H)
    g += P("M 272 148 Q 280 122 264 116 Q 256 134 262 150 Z", COW_H)
    # 深色耳
    g += f'<g transform="rotate(-22 196 196)">{E(196, 196, 24, 13, COW_E)}</g>'
    g += f'<g transform="rotate(22 310 190)">{E(310, 190, 24, 13, COW_E)}</g>'
    # 粉吻 + 鼻孔
    g += E(216, 252, 40, 29, PINK) + E(200, 252, 6, 9, "#c56a50") + E(228, 250, 6, 9, "#c56a50")
    # 双眼 / 嘴
    g += eye(230, 186, 8.5, 11) + eye(276, 182, 8.5, 11)
    g += smile(232, 290, 20, 8)
    g += tuft(150, 448) + tuft(648, 450)
    return g


def art_horse():
    g = ground()
    # 扬起的鬃尾（深棕粗线）
    g += P("M 556 292 Q 606 276 622 318 Q 630 350 610 374", stroke=HAIR, w=20)
    g += P("M 556 292 Q 600 280 614 316", stroke="#7a5230", w=10)
    # 四蹄踏地
    for x in (300, 342, 484, 524):
        g += legq(x, 374, 26, 68, HOR, "#4a3d33")
    # 身体
    g += body_e(418, 312, 140, 86, HOR, HOR_D)
    g += E(408, 356, 96, 36, HOR_L, 0.55)
    # 粗颈
    g += P("M 338 284 Q 302 238 276 190", stroke=HOR_D, w=58)
    g += P("M 332 278 Q 298 234 272 186", stroke=HOR, w=48)
    # 立鬃沿颈后飘（本卡特征，从鬐甲处起笔）
    g += P("M 348 262 Q 314 222 290 172 Q 282 158 288 148", stroke=HAIR, w=22)
    # 长脸头
    g += head_c(258, 168, 44, HOR, HOR_D)
    g += E(226, 192, 34, 26, HOR_L) + C(206, 194, 4.5, "#8a5c38")
    g += smile(230, 216, 16, 7)
    # 双耳 + 额鬃
    g += P("M 276 130 L 292 100 L 302 134 Z", HOR_D) + P("M 282 128 L 291 108 L 297 130 Z", HOR_L)
    g += P("M 246 128 L 244 100 L 266 126 Z", HOR_D)
    g += P("M 252 128 Q 264 112 282 122", stroke=HAIR, w=10)
    # 眼
    g += eye(242, 158, 9, 12)
    g += tuft(150, 448) + tuft(650, 448)
    return g


def art_sheep():
    g = ground()
    inner = ""
    # 黑腿黑蹄
    for x in (338, 380, 468, 506):
        inner += legq(x, 388, 24, 54, "#4a3d33", "#3a2f26")
    # 云状卷毛（暗团偏右下 → 亮团盖面，云纹边缘；本卡主角）
    puffs = [(352, 272, 46), (394, 244, 50), (450, 240, 48), (502, 268, 44),
             (522, 318, 44), (506, 366, 42), (450, 390, 44), (388, 380, 44), (344, 322, 46)]
    for (px, py, pr) in puffs:
        inner += C(px + 5, py + 7, pr, WOOL_D)
    inner += C(437, 321, 88, WOOL_D)
    for (px, py, pr) in puffs:
        inner += C(px, py, pr, WOOL)
    inner += C(432, 314, 88, WOOL)
    # 颈间毛 + 绒球尾
    inner += C(305, 255, 6, 34, WOOL_D) + C(300, 250, 32, WOOL)
    inner += C(553, 323, 20, WOOL_D) + C(548, 316, 18, WOOL)
    # 黑脸头
    inner += C(258, 214, 56, FACE_D) + C(252, 208, 54, FACE)
    # 头顶卷毛
    inner += C(226, 168, 26, WOOL_D) + C(258, 160, 30, WOOL_D) + C(288, 172, 24, WOOL_D)
    inner += C(222, 162, 24, WOOL) + C(256, 154, 28, WOOL) + C(286, 166, 22, WOOL)
    # 下垂耳
    inner += f'<g transform="rotate(24 306 224)">{E(306, 224, 26, 13, FACE_D)}</g>'
    # 眼（黑脸加白底托）+ 鼻嘴
    inner += E(234, 196, 13, 15, WHITE) + E(234, 197, 8.5, 11, INK) + C(231, 192, 3, WHITE)
    inner += C(218, 238, 5, "#2f261f") + smile(232, 252, 16, 7, "#2f261f")
    g += f'<g transform="translate(760,0) scale(-1,1)">{inner}</g>'
    g += tuft(150, 448) + tuft(636, 450)
    return g


def art_fox():
    g = ground()
    # 蓬蓬大尾巴（粗弧线 + 末段白尖，本卡主角）
    g += P("M 468 372 Q 584 392 606 306 Q 612 268 590 246", stroke=RED_D, w=62)
    g += P("M 468 372 Q 578 390 598 308", stroke=RED, w=48)
    g += P("M 600 300 Q 610 268 590 246", stroke=WHITE, w=44)
    g += P("M 566 272 Q 578 286 574 302", stroke=RED_D, w=5)
    # 坐姿后臀 + 后脚
    g += C(410, 354, 78, RED_D) + C(404, 348, 74, RED)
    g += E(444, 428, 40, 15, RED_D) + E(438, 424, 36, 13, RED)
    # 前胸身
    g += E(334, 308, 46, 72, RED_D) + E(328, 302, 42, 68, RED)
    g += E(318, 330, 22, 42, FOX_W)
    # 前腿（深爪）
    for x in (298, 338):
        g += R(x, 336, 22, 106, 10, RED) + R(x, 426, 22, 16, 8, "#a8431f")
    # 尖耳（内耳深）
    g += P("M 272 160 L 292 104 L 318 154 Z", RED) + P("M 281 154 L 293 118 L 306 150 Z", "#a8431f")
    g += P("M 230 152 L 220 96 L 254 142 Z", RED) + P("M 235 146 L 230 116 L 246 140 Z", "#a8431f")
    # 头 + 白吻
    g += head_c(252, 196, 54, RED, RED_D)
    g += E(212, 222, 30, 22, FOX_W) + C(192, 216, 7, INK)
    g += smile(212, 240, 16, 7)
    # 眼
    g += eye(240, 178, 9, 12)
    g += tuft(648, 450)
    return g


def art_wolf():
    g = ground()
    inner = ""
    # 垂尾（斜向下，与马扬尾、狐卷尾错开）
    inner += f'<g transform="rotate(42 546 350)">{E(546, 350, 26, 62, WOLF_D) + E(541, 344, 23, 56, WOLF)}</g>'
    # 四腿
    for x in (314, 352, 476, 512):
        inner += legq(x, 378, 22, 64, WOLF, WOLF_D)
    # 身体 + 浅腹
    inner += body_e(425, 318, 138, 78, WOLF, WOLF_D)
    inner += E(412, 352, 98, 34, WOLF_L, 0.9)
    # 仰起的粗颈
    inner += P("M 350 284 Q 312 248 285 205", stroke=WOLF_D, w=56)
    inner += P("M 344 278 Q 308 244 282 202", stroke=WOLF, w=46)
    # 仰头嚎叫：整头（耳+头+指天吻+眼）一组后仰，保证五官连贯（本卡）
    head_g = wrap(
        P("M 296 150 L 310 92 L 336 142 Z", WOLF_D) + P("M 306 140 L 312 110 L 322 136 Z", WOLF_L),
        P("M 254 146 L 248 92 L 282 138 Z", WOLF_D) + P("M 260 136 L 258 108 L 272 132 Z", WOLF_L),
        C(290, 184, 46, WOLF_D) + C(284, 178, 44, WOLF),
        P("M 252 160 Q 206 166 192 184 Q 206 204 250 202 Q 266 180 252 160 Z", WOLF_L),
        C(198, 182, 7, INK),
        PG([(206, 198), (232, 212), (204, 210)], "#6b4a3a"),
        E(272, 164, 9, 11, INK) + C(269, 160, 2.8, WHITE),
    )
    inner += f'<g transform="rotate(34 280 208)">{head_g}</g>'
    # 嚎叫声波
    inner += P("M 192 134 Q 180 122 184 106", stroke=INK, w=5)
    inner += P("M 174 144 Q 156 126 162 102", stroke=INK, w=5)
    inner += P("M 158 154 Q 136 130 144 98", stroke=INK, w=5)
    g += f'<g transform="translate(760,0) scale(-1,1)">{inner}</g>'
    g += tuft(150, 448)
    return g


def art_deer():
    g = ground()
    # 头顶枝角（先画，在头后；本卡特征）
    g += P("M 268 152 Q 264 116 246 94", stroke=WOOD, w=9)
    g += P("M 262 124 Q 248 118 238 104", stroke=WOOD, w=8)
    g += P("M 256 106 Q 264 94 278 90", stroke=WOOD, w=8)
    g += P("M 292 150 Q 297 114 315 92", stroke=WOOD, w=9)
    g += P("M 297 122 Q 311 116 321 102", stroke=WOOD, w=8)
    # 短尾
    g += C(556, 296, 17, DEER_D) + C(551, 291, 15, DEER)
    # 细腿
    for x in (318, 354, 482, 516):
        g += legq(x, 382, 20, 60, DEER, "#7a5230", 12)
    # 窄身
    g += body_e(419, 319, 122, 72, DEER, DEER_D)
    g += E(410, 358, 88, 28, DEER_L, 0.9)
    # 白斑点（本卡主角）
    for (sx, sy, sr) in [(348, 288, 9), (390, 272, 8), (436, 280, 9), (480, 294, 8),
                         (514, 314, 8), (366, 328, 8), (414, 322, 8), (458, 334, 8), (498, 348, 7)]:
        g += C(sx, sy, sr, DEER_L)
    # 颈
    g += P("M 338 290 Q 308 252 290 214", stroke=DEER_D, w=44)
    g += P("M 332 284 Q 304 248 286 210", stroke=DEER, w=36)
    # 双耳
    g += f'<g transform="rotate(-26 236 176)">{E(236, 176, 26, 13, DEER_D) + E(233, 174, 22, 10, DEER_L)}</g>'
    g += f'<g transform="rotate(24 316 172)">{E(316, 172, 26, 13, DEER_D) + E(313, 170, 22, 10, DEER_L)}</g>'
    # 头 + 浅吻
    g += head_c(273, 193, 38, DEER, DEER_D)
    g += E(238, 208, 28, 20, DEER_L) + C(220, 208, 5, "#6b4a2e")
    g += smile(238, 226, 14, 6)
    # 眼
    g += eye(256, 178, 8.5, 11)
    g += tuft(150, 448) + tuft(648, 450)
    return g


def art_giraffe():
    g = ground()
    # 左上树枝嫩叶（吃高处树叶）
    g += P("M 26 92 Q 88 84 150 100", stroke=WOOD, w=16)
    g += (C(74, 68, 30, GREEN) + C(126, 76, 34, GREEN) + C(52, 100, 24, GREEN)
          + C(112, 52, 22, GREEN_L, 0.9) + C(158, 96, 20, GREEN) + C(170, 120, 17, GREEN))
    # 尾 + 穗
    g += P("M 576 318 Q 608 338 602 386", stroke=YEL_D, w=9) + C(602, 392, 12, "#8a5a33")
    # 长腿（深棕蹄更清楚）
    for x in (408, 446, 520, 554):
        g += legq(x, 388, 22, 54, YEL, "#b5804a", 12)
    # 身体
    g += body_e(471, 335, 106, 62, YEL, YEL_D)
    # 超长颈（伸向左上，本卡主角）
    g += P("M 392 308 Q 332 252 268 178", stroke=YEL_D, w=46)
    g += P("M 386 302 Q 328 248 264 174", stroke=YEL, w=38)
    g += P("M 404 296 Q 344 244 282 172", stroke="#b57b44", w=8)
    # 头 + 上仰浅吻
    g += head_c(243, 159, 32, YEL, YEL_D)
    g += f'<g transform="rotate(30 214 140)">{E(214, 140, 28, 19, "#f7d98f")}</g>'
    g += C(196, 126, 4.5, "#8a5c38") + smile(206, 146, 12, 6)
    # 耳
    g += f'<g transform="rotate(28 276 138)">{E(276, 138, 16, 10, YEL_D)}</g>'
    # 头顶两只角（本卡特征）
    g += L(234, 130, 228, 110, YEL_D, 6) + C(228, 106, 9, "#8a5a33")
    g += L(254, 128, 252, 106, YEL_D, 6) + C(252, 102, 9, "#8a5a33")
    # 眼
    g += eye(228, 152, 8, 10)
    # 棕色网纹斑块
    for (px, py, pr) in [(444, 310, 13), (492, 322, 12), (452, 352, 11), (504, 352, 11),
                         (536, 330, 10), (414, 336, 10), (360, 276, 10), (326, 242, 9),
                         (296, 208, 9), (270, 184, 8)]:
        g += C(px, py, pr, GIR_P)
    g += tuft(636, 450)
    return g


def art_zebra():
    g = ground()
    inner = ""
    # 尾 + 黑穗
    inner += P("M 556 286 Q 592 310 588 362", stroke=ZEB_D, w=8) + C(588, 368, 12, INK)
    # 四腿（深蹄）
    for x in (306, 346, 482, 520):
        inner += legq(x, 372, 24, 70, ZEB, "#3f342b")
    # 身体
    inner += body_e(421, 309, 137, 82, ZEB, ZEB_D)
    # 全身均匀竖纹（本卡主角：条纹铺满全身）
    for d in ("M 312 258 Q 300 306 312 354", "M 338 244 Q 326 306 338 368",
              "M 368 234 Q 356 306 368 378", "M 402 229 Q 392 306 402 383",
              "M 440 229 Q 432 306 440 383", "M 476 236 Q 468 306 476 376",
              "M 510 250 Q 502 306 510 362", "M 540 274 Q 532 306 540 338"):
        inner += P(d, stroke=INK, w=11)
    # 颈 + 颈纹
    inner += P("M 340 278 Q 308 240 288 198", stroke=ZEB_D, w=50)
    inner += P("M 334 272 Q 304 236 284 194", stroke=ZEB, w=42)
    inner += P("M 314 250 L 336 264", stroke=INK, w=8) + P("M 300 224 L 320 238", stroke=INK, w=8)
    inner += P("M 330 274 L 352 286", stroke=INK, w=8)
    # 短立鬃（与马的长鬃错开）
    inner += P("M 322 240 Q 296 214 282 190", stroke="#3f342b", w=15)
    # 头 + 深吻
    inner += head_c(269, 167, 36, ZEB, ZEB_D)
    inner += E(232, 186, 27, 20, "#5a4f42") + C(216, 184, 4.5, "#2f261f")
    # 面纹
    inner += P("M 252 142 L 262 164", stroke=INK, w=5) + P("M 272 136 L 279 158", stroke=INK, w=5)
    # 竖耳
    inner += P("M 286 136 L 292 102 L 310 130 Z", ZEB_D) + P("M 293 130 L 296 112 L 303 128 Z", ZEB)
    inner += P("M 254 132 L 250 100 L 272 124 Z", ZEB_D)
    # 眼
    inner += eye(250, 156, 8.5, 11)
    g += f'<g transform="translate(760,0) scale(-1,1)">{inner}</g>'
    g += tuft(150, 448) + tuft(636, 450)
    return g


def art_kangaroo():
    g = ground()
    # 粗尾拖地（本卡支点）
    g += P("M 452 396 Q 540 404 600 434", stroke=KAN_D, w=36)
    g += P("M 452 396 Q 536 402 592 430", stroke=KAN, w=27)
    # 直立身体（上胸 + 后臀）
    g += E(398, 262, 58, 76, KAN_D) + E(392, 256, 54, 72, KAN)
    g += C(414, 352, 84, KAN_D) + C(408, 346, 80, KAN)
    # 育儿袋 + 露头的小袋鼠（本卡主角）
    g += E(352, 386, 46, 22, KAN_D)
    g += C(340, 366, 23, "#c98a55")
    g += f'<g transform="rotate(-24 324 348)">{E(324, 348, 9, 20, "#c98a55")}</g>'
    g += f'<g transform="rotate(18 356 344)">{E(356, 344, 9, 20, "#c98a55")}</g>'
    g += E(332, 362, 5.5, 7, INK) + C(330, 359, 2, WHITE)
    g += E(348, 392, 46, 17, KAN_L)
    # 小前臂
    g += P("M 360 292 Q 332 298 320 318", stroke=KAN_D, w=15) + C(318, 322, 10, KAN_D)
    g += P("M 378 306 Q 354 314 344 332", stroke=KAN_D, w=13) + C(342, 336, 9, KAN_D)
    # 大脚
    g += E(316, 432, 52, 16, KAN_D) + E(310, 428, 48, 14, KAN)
    # 头 + 浅吻
    g += head_c(348, 196, 40, KAN, KAN_D)
    g += E(304, 212, 27, 19, KAN_L) + C(286, 208, 6, "#6b3f24")
    g += smile(308, 228, 16, 7)
    # 长立耳
    g += f'<g transform="rotate(-16 356 140)">{E(356, 140, 13, 34, KAN_D) + E(355, 141, 9, 27, KAN_L)}</g>'
    g += f'<g transform="rotate(14 388 144)">{E(388, 144, 13, 36, KAN_D) + E(387, 145, 9, 29, KAN_L)}</g>'
    # 眼
    g += eye(326, 180, 8.5, 11)
    g += tuft(150, 448) + tuft(648, 452)
    return g


def arts():
    return {
        "pig": art_pig(),
        "cow": art_cow(),
        "horse": art_horse(),
        "sheep": art_sheep(),
        "fox": art_fox(),
        "wolf": art_wolf(),
        "deer": art_deer(),
        "giraffe": art_giraffe(),
        "zebra": art_zebra(),
        "kangaroo": art_kangaroo(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    ws = [c["w"] for c in GROUP_CARDS]
    a = arts()
    assert set(ws) == set(a) and len(ws) == len(set(ws)), "键集合与词条不一致"
    for k, v in a.items():
        assert not any(t in v for t in ("<svg", "<defs", "<use", "<text", "<image")), f"{k} 含禁止标签"
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">{v}</svg>')
    print("OK", len(ws), "卡")
