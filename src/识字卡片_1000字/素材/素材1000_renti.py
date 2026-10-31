#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""人体组补充 21 卡插画与文案（1000 字批次 B8）。

字表：骨汗血脑唇腿肩肘膝脖睫泪额胸掌腕腰甲拇腮颊
（legacy ../识字卡片_素材_renti.py 已有 16 卡 口手足耳目头发牙心脸嘴脚肚眉拳指舌，
本文件只做增量，不与 legacy 撞造型）。

一眼可辨约定（主控硬规则）：
骨=友好卡通骨头（带小笑脸）/ 汗=kid 跑步大汗珠飞出 / 血=手指贴创可贴（不画血腥）/
脑=kid 头顶思考泡泡里小灯泡 / 唇=嘟嘴大红唇特写 / 腿=kid 指自己的腿 /
肩=kid 手搭对侧肩 / 肘=弯臂特写肘尖鼓起 / 膝=坐地屈腿短裤露大膝盖+手按住 /
脖=大头+露一截脖子+围脖特写 /
睫=闭眼长睫毛特写 / 泪=哭脸大泪珠 / 额=梳发露大额头+手贴额头试温 / 胸=kid 指胸口红心 /
掌=hand() 摊开手掌 / 腕=前臂戴手表特写 / 腰=双手叉腰（kid 画不了叉腰，同风格手绘）/
甲=手指甲特写 / 拇=竖大拇指 / 腮=圆脸大红腮红 / 颊=小手捏脸颊。
身体部位卡一律放大突出（脸/唇/手/臂特写），人物卡用 kid()；相邻卡轮廓+主色错开。
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
NAIL = "#fbedd7"          # 指甲浅色（亮）
CREAM = "#fdfdfa"         # 骨头白
CREAM_D = "#e3ded2"       # 骨头阴影
PLASTER = "#e6bd8a"       # 创可贴
PLASTER_L = "#f7e7cd"     # 创可贴衬垫
SILVER = "#c9cdd1"        # 灯泡灯口灰
BLUSH_D = "#f0937c"       # 深腮红


def _rot(x, y, deg, svg):
    return f'<g transform="rotate({deg} {x} {y})">{svg}</g>'


def _tr(x, y, deg, svg):
    """平移到位再旋转（内容以原点为中心）。"""
    return f'<g transform="translate({x},{y}) rotate({deg})">{svg}</g>'


# ---------- 各卡插画 ----------
def a_gu():
    """骨：经典大骨头，两端双圆鼓头，带小笑脸。"""
    g = ground(380, 442, 250, 24)
    bone = wrap(
        C(262, 322, 50, CREAM_D), C(274, 238, 50, CREAM_D),
        C(494, 250, 50, CREAM_D), C(482, 334, 50, CREAM_D),
        C(260, 318, 47, CREAM), C(272, 236, 47, CREAM),
        C(492, 248, 47, CREAM), C(480, 330, 47, CREAM),
        R(266, 258, 220, 70, 35, CREAM_D),
        R(260, 252, 220, 70, 35, CREAM),
        C(346, 282, 6.5, INK), C(390, 276, 6.5, INK),
        C(348, 280, 2.2, WHITE), C(392, 274, 2.2, WHITE),
        P("M 350 298 Q 368 310 386 294", stroke=INK, w=5.5),
        C(330, 298, 8, PINK, 0.75), C(404, 292, 8, PINK, 0.75),
    )
    return g + _rot(380, 288, -12, bone)


def a_han():
    """汗：kid 奔跑（整体前倾），大颗汗珠从额头飞出。"""
    return wrap(
        ground(390, 446, 250, 24),
        _rot(390, 438, 6, kid(390, 436, s=1.05, pose="run", shirt=TEAL,
                              face="open", arms="pump", look=(0.7, 0))),
        drop(280, 148, 21), drop(240, 206, 15), drop(288, 104, 12),
        C(272, 141, 6.5, WHITE, 0.7), C(235, 200, 5, WHITE, 0.7),
    )


def a_xue():
    """血：手指破皮贴创可贴（不画血）。"""
    g = ground(380, 438, 240, 22)
    g += hand(380, 316, s=1.25)
    g += _tr(385, 230, 22, wrap(
        R(-78, -28, 156, 56, 24, PLASTER),
        R(-38, -28, 76, 56, 16, PLASTER_L),
        C(-19, 0, 4.5, "#dcc09a"), C(0, 0, 4.5, "#dcc09a"),
        C(19, 0, 4.5, "#dcc09a")))
    return g


def a_nao():
    """脑：kid 抬头想问题，头顶思考泡泡里小灯泡亮。"""
    bubble = wrap(
        cloud_p(560, 128, 1.5, "#dceef9"),
        C(560, 134, 32, SUN),
        C(548, 122, 9, WHITE, 0.85),
        R(547, 160, 26, 13, 5, SILVER),
        L(560, 82, 560, 70, "#e8a13c", 5),
        L(526, 94, 516, 84, "#e8a13c", 5),
        L(594, 94, 604, 84, "#e8a13c", 5),
    )
    return wrap(
        ground(360, 444, 250, 24),
        kid(330, 436, s=1.0, pose="stand", shirt=RED, face="o",
            look=(1.0, -0.7)),
        C(432, 216, 10, "#dceef9"), C(464, 186, 14, "#dceef9"),
        bubble,
    )


def a_chun():
    """唇：嘟起的大红唇特写。"""
    return wrap(
        ground(380, 438, 240, 22),
        P("M 220 262 Q 296 196 360 232 Q 372 220 380 220 Q 388 220 400 232 "
          "Q 464 196 540 262 Q 460 286 380 284 Q 300 286 220 262 Z", RED),
        P("M 236 276 Q 310 292 380 292 Q 450 292 524 276 "
          "Q 506 356 380 364 Q 254 356 236 276 Z", "#f0876f"),
        P("M 236 276 Q 380 302 524 276", stroke=RED_D, w=6),
        E(322, 330, 28, 13, WHITE, 0.55),
        C(438, 322, 10, WHITE, 0.4),
    )


def a_tui():
    """腿：kid 站立低头看腿，箭头指出大腿（手臂够不到大腿，沿用箭头指认）。"""
    return wrap(
        ground(320, 446, 250, 24),
        kid(280, 442, s=1.2, pose="stand", shirt=GREEN, face="smile",
            look=(0.4, 0.55)),
        L(580, 400, 368, 400, INK, 10),
        PG([(352, 400), (384, 384), (384, 416)], INK),
    )


def a_jian():
    """肩：kid 手搭在对侧肩膀上。"""
    return wrap(
        ground(360, 446, 250, 24),
        kid(360, 440, s=1.05, pose="stand", shirt=YEL, face="smile",
            arms="point", point_at=(315, 262), look=(0.5, -0.2)),
    )


def a_zhou():
    """肘：弯臂特写，肘尖在弯角鼓起。"""
    return wrap(
        ground(380, 442, 240, 22),
        R(150, 296, 120, 78, 30, YEL),              # 袖子
        R(150, 296, 120, 24, 12, YEL_D),
        L(252, 336, 380, 330, SKIN, 62),            # 上臂
        C(380, 330, 35, SKIN),                      # 肘尖
        L(380, 330, 380, 214, SKIN, 56),            # 前臂立起
        C(380, 200, 34, SKIN),                      # 小拳头
        P("M 362 192 Q 380 182 398 192", stroke=SKIN_D, w=5),
        P("M 258 350 Q 316 356 372 350", stroke=SKIN_D, w=6),
        P("M 358 300 Q 352 260 358 240", stroke=SKIN_D, w=5),
    )


def a_xi():
    """膝：坐地小孩屈腿穿短裤，又大又圆的光膝盖+小手按在膝盖上（自绘坐姿）。"""
    return wrap(
        ground(370, 448, 265, 24),
        E(300, 404, 62, 26, BLUE_D),                              # 坐地的小屁股
        L(236, 402, 300, 404, BLUE_D, 42),                        # 收在身后的左腿
        E(226, 404, 20, 11, INK),                                 # 左脚
        P("M 262 296 Q 258 394 298 402 L 354 402 Q 380 378 372 300 "
          "Q 320 278 262 296 Z", "#e8742a"),                      # 上衣（短裤露膝）
        L(350, 388, 442, 320, BLUE_D, 50),                        # 大腿（裤）
        C(462, 306, 34, SKIN),                                    # 大膝盖（主角）
        C(450, 293, 12, "#fad4b0", 0.9),                          # 膝盖高光
        L(484, 326, 502, 424, BLUE_D, 42),                        # 小腿（裤）
        E(512, 436, 26, 12, INK),                                 # 脚
        L(346, 302, 440, 276, SKIN, 23),                          # 手臂伸向膝盖
        C(456, 272, 14, SKIN),                                    # 小手按在膝盖上
        C(326, 232, 58, SKIN),                                    # 头
        P("M 268 212 Q 276 142 326 138 Q 376 142 384 212 "
          "Q 352 200 326 202 Q 300 200 268 212 Z", HAIR),
        E(300, 244, 10, 13, INK), C(303, 248, 3.2, WHITE),        # 看向膝盖
        E(348, 244, 10, 13, INK), C(351, 248, 3.2, WHITE),
        P("M 304 276 Q 326 292 348 276", stroke=INK, w=6),
        C(282, 268, 11, PINK, 0.8), C(372, 268, 11, PINK, 0.8),
    )


def a_bo():
    """脖：大头 + 红围脖特写。"""
    return wrap(
        ground(380, 440, 240, 22),
        R(352, 322, 56, 50, 16, SKIN),                       # 脖子
        C(266, 246, 20, SKIN), C(494, 246, 20, SKIN),        # 耳朵
        C(392, 246, 116, SKIN_D), C(380, 236, 112, SKIN),
        P("M 272 210 Q 280 96 380 92 Q 480 96 488 210 "
          "Q 416 164 380 166 Q 344 164 272 210 Z", HAIR),
        E(340, 242, 11, 14, INK), E(420, 242, 11, 14, INK),
        C(343, 236, 3.6, WHITE), C(423, 236, 3.6, WHITE),
        P("M 350 300 Q 380 318 410 300", stroke=INK, w=7),
        C(316, 272, 13, PINK, 0.8), C(444, 272, 13, PINK, 0.8),
        E(380, 408, 114, 40, TEAL),                          # 围脖一圈（下移露脖子）
        E(380, 390, 114, 16, TEAL_D),
        R(432, 412, 54, 62, 18, TEAL),                       # 围脖垂尾
        L(444, 458, 444, 470, TEAL_D, 7), L(458, 460, 458, 472, TEAL_D, 7),
        P("M 300 394 Q 380 410 456 394", stroke=TEAL_D, w=5),
    )


def a_jie():
    """睫：闭眼长睫毛特写（睫毛根贴眼线、向外下弯）。"""
    lashes = ""
    for (x1, y1, qx, qy, x2, y2) in ((250, 262, 236, 282, 218, 300),
                                     (315, 240, 302, 262, 294, 284),
                                     (380, 234, 379, 258, 380, 282),
                                     (445, 240, 458, 262, 466, 284),
                                     (510, 262, 524, 282, 542, 300)):
        lashes += P(f"M {x1} {y1} Q {qx} {qy} {x2} {y2}", stroke=INK, w=11)
    return wrap(
        ground(380, 438, 250, 22),
        E(380, 296, 258, 132, "#fbeadb"),                    # 肤色衬底
        P("M 222 190 Q 380 106 538 190", stroke=HAIR, w=13),  # 眉毛
        P("M 190 280 Q 380 160 570 280", stroke=INK, w=17),   # 闭眼线
        lashes,
    )


def a_lei():
    """泪：哭脸特写，大颗泪珠往下掉。"""
    return wrap(
        ground(380, 442, 250, 22),
        C(392, 272, 158, SKIN_D), C(380, 262, 154, SKIN),
        P("M 232 240 Q 240 112 380 106 Q 520 112 528 240 "
          "Q 460 200 380 204 Q 300 200 232 240 Z", HAIR),
        P("M 292 226 Q 314 214 334 228", stroke=INK, w=7),
        P("M 426 228 Q 446 214 468 226", stroke=INK, w=7),
        P("M 296 268 Q 318 254 338 268", stroke=INK, w=9),
        P("M 422 268 Q 442 254 464 268", stroke=INK, w=9),
        P("M 348 334 Q 362 324 376 334 Q 390 344 412 334", stroke=INK, w=7),
        drop(316, 308, 17), drop(312, 352, 13), drop(318, 392, 9),
        drop(444, 308, 17), drop(448, 352, 13), drop(442, 392, 9),
        C(310, 302, 5, WHITE, 0.8), C(438, 302, 5, WHITE, 0.8),
    )


def a_e():
    """额：头发梳上去露出大额头，小手平平贴在额头上试温度。"""
    return wrap(
        ground(380, 442, 250, 22),
        C(389, 279, 146, SKIN_D), C(380, 270, 143, SKIN),
        C(380, 96, 30, HAIR),                               # 冲天小揪揪
        P("M 256 208 Q 262 92 380 86 Q 498 92 504 208 "
          "Q 466 162 380 158 Q 294 162 256 208 Z", HAIR),   # 梳上去的头发，露大额头
        P("M 316 254 Q 336 242 356 252", stroke=INK, w=5),  # 眉毛
        P("M 404 252 Q 424 242 444 254", stroke=INK, w=5),
        E(336, 282, 11, 14, INK), E(424, 282, 11, 14, INK),
        C(339, 276, 3.6, WHITE), C(427, 276, 3.6, WHITE),
        P("M 348 338 Q 380 358 412 338", stroke=INK, w=7),
        C(300, 310, 13, PINK, 0.8), C(460, 310, 13, PINK, 0.8),
        hand(322, 216, s=0.62, rot=90),                     # 手背贴在额头正中
    )


def a_xiong():
    """胸：kid 指着胸口的小红心（红心画在胸口正中）。"""
    return wrap(
        ground(380, 446, 250, 24),
        kid(380, 440, s=1.05, pose="stand", shirt="#e8742a", face="smile",
            arms="point", point_at=(376, 306), look=(0.2, 0.6)),
        heart(408, 302, 27, RED),
        C(399, 292, 5, WHITE, 0.8),
    )


def a_zhang():
    """掌：摊开的手掌特写（hand 组件）。"""
    return wrap(
        ground(380, 440, 250, 22),
        hand(380, 296, s=1.45, rot=-6),
    )


def a_wan():
    """腕：前臂 + 手腕上戴小手表特写。"""
    return wrap(
        ground(380, 442, 250, 22),
        R(140, 294, 120, 84, 30, YEL),                      # 袖口
        R(140, 294, 120, 26, 12, YEL_D),
        L(252, 336, 428, 330, SKIN, 64),                    # 前臂
        P("M 262 358 Q 340 366 424 358", stroke=SKIN_D, w=5),
        C(476, 330, 52, SKIN),                              # 手背
        _rot(520, 300, -12, R(480, 286, 84, 27, 13, SKIN)),
        _rot(530, 330, -4, R(490, 316, 88, 27, 13, SKIN)),
        _rot(524, 358, 6, R(486, 344, 82, 27, 13, SKIN)),
        _rot(500, 382, 16, R(466, 370, 70, 26, 13, SKIN)),
        _rot(446, 282, -38, R(432, 240, 27, 66, 13, SKIN)),  # 拇指
        R(286, 282, 60, 110, 16, BLUE),                     # 表带
        L(298, 286, 298, 388, "#4a97c9", 5), L(334, 286, 334, 388, "#4a97c9", 5),
        C(316, 336, 44, BLUE_D), C(316, 336, 37, WHITE),    # 表盘
        L(316, 336, 316, 314, BLUE_D, 6), L(316, 336, 332, 336, RED_D, 5),
        C(316, 336, 6, INK),
    )


def a_yao():
    """腰：双手叉腰（kid 画不了叉腰，同风格手绘）。"""
    head = wrap(
        C(266, 172, 20, SKIN), C(494, 172, 20, SKIN),
        C(386, 166, 114, SKIN_D), C(380, 158, 110, SKIN),
        P("M 276 132 Q 284 22 380 18 Q 476 22 484 132 "
          "Q 416 88 380 90 Q 344 88 276 132 Z", HAIR),
        E(342, 162, 11, 14, INK), E(418, 162, 11, 14, INK),
        C(345, 156, 3.6, WHITE), C(421, 156, 3.6, WHITE),
        P("M 352 216 Q 380 232 408 216", stroke=INK, w=7),
        C(320, 190, 13, PINK, 0.8), C(440, 190, 13, PINK, 0.8),
    )
    body = wrap(
        P("M 318 262 Q 316 372 352 378 L 408 378 Q 444 372 442 262 "
          "Q 380 246 318 262 Z", TEAL),                     # 上衣
        R(346, 372, 68, 22, 8, WOOD_D),                    # 腰带
        R(338, 392, 30, 62, 12, BLUE_D),                   # 裤腿
        R(392, 392, 30, 62, 12, BLUE_D),
        L(320, 276, 274, 330, SKIN, 30),                   # 左臂：肩→肘
        C(274, 330, 15, SKIN),
        L(274, 330, 352, 366, SKIN, 30),                   # 肘→手卡腰
        C(352, 366, 15, SKIN),
        L(440, 276, 486, 330, SKIN, 30),                   # 右臂
        C(486, 330, 15, SKIN),
        L(486, 330, 408, 366, SKIN, 30),
        C(408, 366, 15, SKIN),
    )
    return wrap(
        ground(380, 446, 250, 24),
        body, head,
    )


def a_jia():
    """甲：手指甲特写（一根大手指，指甲亮亮）。"""
    return wrap(
        ground(380, 440, 230, 22),
        R(334, 158, 108, 288, 54, SKIN_D),
        R(326, 150, 108, 288, 54, SKIN),
        E(380, 218, 45, 52, SKIN_D),                        # 指甲衬边
        E(380, 216, 41, 48, NAIL),                          # 指甲
        P("M 344 190 Q 380 176 416 190", stroke=SKIN_D, w=5),
        E(380, 244, 30, 14, WHITE, 0.8),
        P("M 342 330 Q 380 344 418 330", stroke=SKIN_D, w=5),
        P("M 342 372 Q 380 386 418 372", stroke=SKIN_D, w=5),
    )


def a_mu():
    """拇：竖起大拇指。"""
    thumb = wrap(
        R(310, 110, 58, 160, 29, SKIN),
        E(339, 139, 20, 24, SKIN_D),
        E(339, 138, 17, 21, NAIL),
    )
    return wrap(
        ground(380, 442, 240, 22),
        _rot(340, 246, -14, thumb),
        R(320, 248, 158, 168, 46, SKIN_D),
        R(312, 240, 158, 168, 46, SKIN),                    # 拳头
        C(344, 240, 26, SKIN), C(386, 236, 28, SKIN), C(428, 240, 26, SKIN),
        R(312, 396, 158, 52, 18, YEL),                      # 袖口
        R(312, 396, 158, 20, 10, YEL_D),
    )


def a_sai():
    """腮：圆脸两团大红腮红。"""
    return wrap(
        ground(380, 442, 250, 22),
        C(392, 277, 152, SKIN_D), C(380, 266, 148, SKIN),
        P("M 240 240 Q 248 118 380 112 Q 512 118 520 240 "
          "Q 452 196 380 200 Q 308 196 240 240 Z", HAIR),
        P("M 292 250 Q 312 232 332 250", stroke=INK, w=8),
        P("M 428 250 Q 448 232 468 250", stroke=INK, w=8),
        P("M 344 320 Q 380 346 416 320", stroke=INK, w=7),
        C(296, 316, 46, PINK), C(296, 316, 30, "#f9c1b0", 0.75),
        C(464, 316, 46, PINK), C(464, 316, 30, "#f9c1b0", 0.75),
    )


def a_jia2():
    """颊：两只小手捏软软的脸颊。"""
    return wrap(
        ground(380, 442, 260, 22),
        C(380, 282, 140, SKIN),
        C(296, 162, 38, HAIR), C(380, 146, 44, HAIR), C(464, 162, 38, HAIR),
        P("M 266 226 Q 272 138 380 134 Q 488 138 494 226 "
          "Q 440 182 380 184 Q 320 182 266 226 Z", HAIR),
        P("M 316 288 Q 330 274 344 288", stroke=INK, w=8),
        P("M 416 288 Q 430 274 444 288", stroke=INK, w=8),
        P("M 356 348 Q 368 342 380 348 Q 392 354 404 348", stroke=INK, w=6),
        C(300, 330, 34, PINK, 0.9), C(460, 330, 34, PINK, 0.9),
        hand(200, 330, s=0.75, rot=90),                     # 左手捏左脸颊
        hand(560, 330, s=0.75, rot=-90),                    # 右手捏右脸颊
    )


def arts():
    return {
        "骨": a_gu(), "汗": a_han(), "血": a_xue(), "脑": a_nao(),
        "唇": a_chun(), "腿": a_tui(), "肩": a_jian(), "肘": a_zhou(),
        "膝": a_xi(), "脖": a_bo(), "睫": a_jie(), "泪": a_lei(),
        "额": a_e(), "胸": a_xiong(), "掌": a_zhang(), "腕": a_wan(),
        "腰": a_yao(), "甲": a_jia(), "拇": a_mu(), "腮": a_sai(),
        "颊": a_jia2(),
    }


GROUP_CARDS = [
    {"char": "骨", "pinyin": "gǔ", "tone": "第三声",
     "sentence": "大骨头，硬邦邦。",
     "say": "狗狗啃的硬硬的就是骨头。",
     "chat": "摸摸手指头，里面有骨头哦。",
     "life": "吃完的鸡腿骨头轻轻放好。"},
    {"char": "汗", "pinyin": "hàn", "tone": "第四声",
     "sentence": "跑一跑，出汗啦。",
     "say": "跑得快，额头冒出小汗珠。",
     "chat": "出汗的时候是什么感觉呀？",
     "life": "跑完擦擦汗，喝口温水。"},
    {"char": "血", "pinyin": "xuè", "tone": "第四声（口语另读 xiě，如“流血了”）",
     "sentence": "贴上创可贴，血止住啦。",
     "say": "破皮流一点点血，贴上创可贴。",
     "chat": "受伤了要请谁来帮忙呀？",
     "life": "小伤口贴创可贴，不哭哦。"},
    {"char": "脑", "pinyin": "nǎo", "tone": "第三声",
     "sentence": "动动小脑瓜想办法。",
     "say": "想事情用的是小脑袋。",
     "chat": "你动脑筋的时候在想什么呀？",
     "life": "出个小谜语一起动动脑。"},
    {"char": "唇", "pinyin": "chún", "tone": "第二声",
     "sentence": "嘟起小嘴唇亲亲。",
     "say": "嘟起来的红红的是嘴唇。",
     "chat": "嘴唇是什么颜色的呀？",
     "life": "对着镜子嘟个小嘴亲一个。"},
    {"char": "腿", "pinyin": "tuǐ", "tone": "第三声",
     "sentence": "两条小腿跑得快。",
     "say": "大腿小腿一起用力跑。",
     "chat": "你的小腿能跳多高呀？",
     "life": "踢踢腿，伸伸小腿。"},
    {"char": "肩", "pinyin": "jiān", "tone": "第一声",
     "sentence": "小手拍拍肩。",
     "say": "脖子下面宽宽的是肩膀。",
     "chat": "书包背在什么地方呀？",
     "life": "给妈妈捶捶肩。"},
    {"char": "肘", "pinyin": "zhǒu", "tone": "第三声",
     "sentence": "弯弯胳膊肘碰一碰。",
     "say": "胳膊弯弯的关节是胳膊肘。",
     "chat": "弯一弯胳膊，哪里鼓起来啦？",
     "life": "吃饭时胳膊肘放放好。"},
    {"char": "膝", "pinyin": "xī", "tone": "第一声",
     "sentence": "坐下指指小膝盖。",
     "say": "大腿小腿中间的是膝盖。",
     "chat": "跳一跳，膝盖会弯吗？",
     "life": "坐下来摸摸自己的膝盖。"},
    {"char": "脖", "pinyin": "bó", "tone": "第二声",
     "sentence": "围上围巾暖脖子。",
     "say": "头和身体中间的是脖子。",
     "chat": "你的脖子会转动吗？转转看。",
     "life": "转转头，脖子动一动。"},
    {"char": "睫", "pinyin": "jié", "tone": "第二声",
     "sentence": "眨眨眼，睫毛扇一扇。",
     "say": "眼边上细细长长的是睫毛。",
     "chat": "睫毛像不像小扇子呀？",
     "life": "眨眨眼，让睫毛碰碰手指。"},
    {"char": "泪", "pinyin": "lèi", "tone": "第四声",
     "sentence": "眼泪汪汪像下雨。",
     "say": "难过时眼里流出来的是泪。",
     "chat": "开心的时候也会流泪吗？",
     "life": "擦擦眼泪，抱一抱。"},
    {"char": "额", "pinyin": "é", "tone": "第二声",
     "sentence": "摸摸额头烫不烫。",
     "say": "眉毛上面鼓鼓的是额头。",
     "chat": "发烧时妈妈摸哪里呀？",
     "life": "摸摸额头，再摸摸小手。"},
    {"char": "胸", "pinyin": "xiōng", "tone": "第一声",
     "sentence": "小手拍拍胸口。",
     "say": "红心跳跳的地方是胸口。",
     "chat": "跑完步摸摸胸口跳得快吗？",
     "life": "把手放在胸口听心跳。"},
    {"char": "掌", "pinyin": "zhǎng", "tone": "第三声",
     "sentence": "摊开手掌拍拍手。",
     "say": "手心朝上张开就是手掌。",
     "chat": "手掌上有没有细细的线呀？",
     "life": "摊开手掌和妈妈击个掌。"},
    {"char": "腕", "pinyin": "wàn", "tone": "第四声",
     "sentence": "手腕上戴小手表。",
     "say": "手和胳膊连着的是手腕。",
     "chat": "手表戴在什么地方呀？",
     "life": "转转手腕，画个圆圈。"},
    {"char": "腰", "pinyin": "yāo", "tone": "第一声",
     "sentence": "双手叉腰站站好。",
     "say": "两只手卡住的地方就是腰。",
     "chat": "你弯腰时哪里弯下去了？",
     "life": "叉起小腰站得直直的。"},
    {"char": "甲", "pinyin": "jiǎ", "tone": "第三声",
     "sentence": "勤剪指甲讲卫生。",
     "say": "指头顶上硬硬的是指甲。",
     "chat": "指甲长了要怎么样呀？",
     "life": "伸出小手检查小指甲。"},
    {"char": "拇", "pinyin": "mǔ", "tone": "第三声",
     "sentence": "竖起大拇指，顶呱呱！",
     "say": "最粗最短的这根是大拇指。",
     "chat": "夸夸身边的人，竖起大拇指。",
     "life": "真棒的时候就竖大拇指。"},
    {"char": "腮", "pinyin": "sāi", "tone": "第一声",
     "sentence": "腮帮红红像苹果。",
     "say": "脸两边鼓鼓红红的是腮帮。",
     "chat": "害羞的时候腮会变红吗？",
     "life": "照照镜子看看小腮红。"},
    {"char": "颊", "pinyin": "jiá", "tone": "第二声",
     "sentence": "小脸颊，捏一捏。",
     "say": "脸的两边软软的是脸颊。",
     "chat": "脸颊摸起来像棉花糖吗？",
     "life": "轻轻捏捏自己的脸颊。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "renti" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B8"] if e["file"] == "素材1000_renti.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"人体组补充：卡数 {len(GROUP_CARDS)}")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    idx = [ziku_chars.index(ch) for ch in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = set(a) == set(mine)
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad = []
    for c in GROUP_CARDS:
        w = py[c["char"]]
        if c["pinyin"] != w["pinyin"]:
            bad.append((c["char"], "pinyin", c["pinyin"], w["pinyin"]))
        if not (c["tone"] == w["tone"] or c["tone"].startswith(w["tone"] + "（")):
            bad.append((c["char"], "tone", c["tone"], w["tone"]))
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((c["char"], "句长", hanzi))
        if c["char"] not in c["sentence"]:
            bad.append((c["char"], "句缺字"))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((c["char"], f, len(c[f])))
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
