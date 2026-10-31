#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1000字卡集 动作·身体 23 卡：躺趴蹲踩踏跨蹦攀登钻跃滑泳骑翻滚散奔冲梦澡望扭。

插画只用 素材库 组件（kid/ground/ball/drop/cloud_p/star5...），人物一律 kid()；
kid() 没有的姿态（俯卧/仰躺/蹲/团身/侧滚/游泳等）用同风格手绘件补足，
viewBox 0 0 760 480 内部标记；与 legacy 动作卡（跑/走/跳/爬/睡/游/立 等）姿态不撞。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa

D_CHARS = "躺趴蹲踩踏跨蹦攀登钻跃滑泳骑翻滚散奔冲梦澡望扭"


# ---------- 本文件小工具 ----------
def _dash(d, color, w, gap="4 9"):
    """虚线动效弧。"""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-dasharray="{gap}"/>')


def _rot(x, y, ang, inner):
    return f'<g transform="rotate({ang} {x} {y})">{inner}</g>'


def _head(cx, cy, s, look=(0, 0), face="smile", hair_color=HAIR, skin=SKIN):
    """kid() 同款头（侧用/低姿用），坐标=头心。"""
    hd = 62 * s
    top = cy - hd
    bang = cy - hd * 0.42
    f = [C(cx - 58 * s, cy + 10 * s, 11 * s, skin), C(cx + 58 * s, cy + 10 * s, 11 * s, skin),
         C(cx, cy, hd, skin)]
    f.append(P(f"M {cx-hd*0.98} {cy-hd*0.35} Q {cx-hd*0.9} {top-hd*0.18} {cx} {top-hd*0.12} "
               f"Q {cx+hd*0.9} {top-hd*0.18} {cx+hd*0.98} {cy-hd*0.35} "
               f"Q {cx+hd*0.55} {bang-hd*0.1} {cx} {bang} "
               f"Q {cx-hd*0.55} {bang-hd*0.1} {cx-hd*0.98} {cy-hd*0.35} Z", hair_color))
    lx, ly = look
    for ex in (-22, 22):
        f.append(E(cx + ex * s, cy - 8 * s, 10 * s, 13 * s, INK))
        f.append(C(cx + ex * s + lx * s, cy - 13 * s + ly * s, 3.4 * s, WHITE))
    f.append(P(f"M {cx-36*s} {cy-hd*0.52} Q {cx-22*s} {cy-hd*0.62} {cx-8*s} {cy-hd*0.54}",
               stroke=hair_color, w=6 * s))
    f.append(P(f"M {cx+8*s} {cy-hd*0.54} Q {cx+22*s} {cy-hd*0.62} {cx+36*s} {cy-hd*0.52}",
               stroke=hair_color, w=6 * s))
    my = cy + 26 * s
    if face == "open":
        f.append(P(f"M {cx-26*s} {my} Q {cx} {my-10*s} {cx+26*s} {my} Q {cx+24*s} {my+26*s} {cx} {my+30*s} "
                   f"Q {cx-24*s} {my+26*s} {cx-26*s} {my} Z", "#6b3325"))
        f.append(P(f"M {cx-14*s} {my+16*s} Q {cx} {my+8*s} {cx+14*s} {my+16*s} "
                   f"Q {cx+9*s} {my+27*s} {cx} {my+28*s} Q {cx-9*s} {my+27*s} {cx-14*s} {my+16*s} Z", "#f0876f"))
    elif face == "o":
        f.append(E(cx, my + 4 * s, 10 * s, 12 * s, "#6b3325"))
    else:
        f.append(P(f"M {cx-20*s} {my} Q {cx} {my+16*s} {cx+20*s} {my}", stroke=INK, w=7 * s))
    f.append(C(cx - 44 * s, cy + 14 * s, 11 * s, PINK, 0.8))
    f.append(C(cx + 44 * s, cy + 14 * s, 11 * s, PINK, 0.8))
    return wrap(*f)


def _ant(ax, ay):
    """一只小蚂蚁（趴卡配角）。"""
    return wrap(
        E(ax, ay, 12, 7, INK), C(ax + 10, ay - 3, 5.5, INK),
        L(ax - 6, ay + 6, ax - 10, ay + 12, INK, 2),
        L(ax + 2, ay + 7, ax + 2, ay + 13, INK, 2),
        L(ax + 9, ay + 5, ax + 13, ay + 11, INK, 2),
        L(ax + 13, ay - 7, ax + 17, ay - 12, INK, 2),
        L(ax + 16, ay - 5, ax + 21, ay - 9, INK, 2))


def _ant_line(x0, y0, x1, y1, n=3):
    import math
    out = ""
    for i in range(n):
        t = i / max(1, n - 1)
        out += _ant(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)
    return out


GROUP_CARDS = [
    {"char": "躺", "pinyin": "tǎng", "tone": "第三声",
     "sentence": "躺在床上歇一歇。", "say": "身体放平、后背贴床就是躺。",
     "chat": "躺着的时候你最想做什么呀？", "life": "午休陪他在垫子上躺一躺。"},
    {"char": "趴", "pinyin": "pā", "tone": "第一声",
     "sentence": "趴在地上看蚂蚁。", "say": "肚子贴地、头抬起来就是趴。",
     "chat": "趴着的时候你看到了什么？", "life": "趴在垫子上看蚂蚁排队。"},
    {"char": "蹲", "pinyin": "dūn", "tone": "第一声",
     "sentence": "蹲下来系鞋带。", "say": "膝盖弯弯、蹲低身子就是蹲。",
     "chat": "蹲下来能看到什么小东西？", "life": "蹲下来系一次鞋带给他看。"},
    {"char": "踩", "pinyin": "cǎi", "tone": "第三声",
     "sentence": "小心别踩水坑。", "say": "脚踩进水坑，水花溅起来。",
     "chat": "踩水坑要穿什么鞋呀？", "life": "雨天穿雨靴轻轻踩踩水坑。"},
    {"char": "踏", "pinyin": "tà", "tone": "第四声",
     "sentence": "一步一步踏台阶。", "say": "脚稳稳踏上台阶就是踏。",
     "chat": "上台阶要先踏哪只脚？", "life": "上楼时数一数踏了几级。"},
    {"char": "跨", "pinyin": "kuà", "tone": "第四声",
     "sentence": "大步跨过小水沟。", "say": "两腿张开跨过去，不碰到水。",
     "chat": "水沟宽不宽，你敢跨吗？", "life": "地上贴条线，练跨过去。"},
    {"char": "蹦", "pinyin": "bèng", "tone": "第四声",
     "sentence": "蹦蹦跳跳真开心。", "say": "双脚一起蹬地蹦起来。",
     "chat": "你能连着蹦几下？", "life": "拉着他的手原地蹦五下。"},
    {"char": "攀", "pinyin": "pān", "tone": "第一声",
     "sentence": "小手攀上攀爬架。", "say": "双手抓稳、一节一节向上攀。",
     "chat": "攀爬架上你爬到过几层？", "life": "去操场陪他攀一次爬架。"},
    {"char": "登", "pinyin": "dēng", "tone": "第一声",
     "sentence": "登上山顶插红旗。", "say": "一步一步向上登，登到顶插旗。",
     "chat": "登上山顶你看到了什么？", "life": "爬楼梯当登山，顶楼插面小旗。"},
    {"char": "钻", "pinyin": "zuàn", "tone": "第四声（动词读 zuān，如“钻进去”）",
     "sentence": "钻到桌子底下玩。", "say": "低下身子从桌子底下钻过去。",
     "chat": "钻桌子怎样才不会碰到头？", "life": "纸箱开个洞，玩钻山洞。"},
    {"char": "跃", "pinyin": "yuè", "tone": "第四声",
     "sentence": "用力跃过小河。", "say": "猛地向前一跃，跳过小河。",
     "chat": "小青蛙是怎么跃的？", "life": "划两条线当小河跃过去。"},
    {"char": "滑", "pinyin": "huá", "tone": "第二声",
     "sentence": "从滑梯上滑下来。", "say": "坐好扶稳，嗖地滑下来。",
     "chat": "滑滑梯要不要排队呀？", "life": "陪他滑三次滑梯再回家。"},
    {"char": "泳", "pinyin": "yǒng", "tone": "第三声",
     "sentence": "学游泳不怕水。", "say": "手臂划水、腿打水就是游泳。",
     "chat": "游泳的时候要带泳镜吗？", "life": "洗澡时趴在水里练打腿。"},
    {"char": "骑", "pinyin": "qí", "tone": "第二声",
     "sentence": "骑上木马摇一摇。", "say": "跨坐上去、抓住把手骑木马。",
     "chat": "木马摇起来像坐什么呀？", "life": "扶他骑摇马，数摇几下。"},
    {"char": "翻", "pinyin": "fān", "tone": "第一声",
     "sentence": "翻个跟头站起来。", "say": "低头团身，骨碌翻个跟头。",
     "chat": "翻跟头前要先做什么准备？", "life": "在软垫上帮他翻一次。"},
    {"char": "滚", "pinyin": "gǔn", "tone": "第三声",
     "sentence": "抱着膝盖滚一滚。", "say": "抱住膝盖缩成球，滚来滚去。",
     "chat": "像球一样滚是什么感觉？", "life": "垫子上侧身滚一小圈。"},
    {"char": "散", "pinyin": "sàn", "tone": "第四声",
     "sentence": "和妈妈散步去。", "say": "慢慢地走、看看风景是散步。",
     "chat": "晚饭后你想和谁去散步？", "life": "饭后牵手下楼走一圈。"},
    {"char": "奔", "pinyin": "bēn", "tone": "第一声",
     "sentence": "撒开腿向前奔。", "say": "使大劲、飞快地跑就是奔。",
     "chat": "你奔起来像一阵风吗？", "life": "喊一二三，奔到那棵树下。"},
    {"char": "冲", "pinyin": "chōng", "tone": "第一声",
     "sentence": "冲过终点线啦。", "say": "鼓足劲一直向前就是冲。",
     "chat": "冲线以后要做什么动作？", "life": "玩赛跑，冲线时击个掌。"},
    {"char": "梦", "pinyin": "mèng", "tone": "第四声",
     "sentence": "做个甜甜的梦。", "say": "睡着后脑子里放小电影就是梦。",
     "chat": "你昨天晚上梦到什么啦？", "life": "睡前聊一聊想梦到什么。"},
    {"char": "澡", "pinyin": "zǎo", "tone": "第三声",
     "sentence": "洗个泡泡澡。", "say": "泡进澡盆、搓出泡泡就是洗澡。",
     "chat": "泡泡澡你最想带哪个玩具？", "life": "今晚洗澡多玩五分钟泡泡。"},
    {"char": "望", "pinyin": "wàng", "tone": "第四声",
     "sentence": "望一望远处的云。", "say": "抬手朝远处看就是望。",
     "chat": "往远处望，你看到了什么？", "life": "到阳台望一望远处的楼。"},
    {"char": "扭", "pinyin": "niǔ", "tone": "第三声",
     "sentence": "跟着音乐扭一扭。", "say": "腰扭一扭、胳膊摆一摆。",
     "chat": "扭一扭时身体哪里在动呀？", "life": "放首歌，跟他一起扭一扭。"},
]


def arts():
    a = {}

    # 躺：平躺床上，面朝上睁眼，无毯盖身（区别 legacy 睡=侧卧盖被+月亮）
    a["躺"] = wrap(
        ground(390, 446, 260, 24),
        R(112, 200, 26, 202, 12, WOOD),          # 床头板
        R(636, 296, 24, 106, 10, WOOD),          # 床尾板
        R(120, 344, 540, 58, 14, WOOD),          # 床架
        R(128, 322, 524, 34, 12, WHITE),         # 床垫
        E(202, 330, 68, 22, "#f4d3a4"),          # 枕头
        R(412, 296, 152, 34, 16, BLUE_D),        # 腿
        E(576, 312, 20, 11, INK),                # 鞋
        R(240, 288, 182, 42, 20, BLUE),          # 身体
        R(266, 280, 110, 16, 8, SKIN),           # 手臂搭腹
        _head(200, 298, 0.88, look=(0, -0.55), face="smile"),
        R(436, 282, 116, 56, 14, TEAL_L),        # 折在脚边的小毯子
        L(452, 282, 452, 338, TEAL, 4))

    # 趴：趴地撑肘看蚂蚁（区别 legacy 爬=手脚着地爬行）
    a["趴"] = wrap(
        ground(400, 446, 270, 24),
        _rot(500, 396, -7, wrap(R(440, 382, 152, 30, 15, BLUE_D))),
        E(594, 386, 17, 11, INK), E(578, 396, 15, 9, INK, 0.85),
        E(370, 398, 88, 32, GREEN),
        L(312, 392, 280, 424, SKIN, 24), C(276, 428, 12, SKIN),
        L(340, 398, 322, 428, SKIN, 21), C(318, 432, 11, SKIN),
        _head(268, 348, 0.9, look=(0.75, 0.3), face="open"),
        _ant_line(498, 434, 618, 428, 3))

    # 蹲：蹲下系鞋带，屈膝低头看鞋（区别 趴=全身贴地）
    a["蹲"] = wrap(
        ground(380, 446, 240, 22),
        L(310, 372, 410, 376, BLUE_D, 36),       # 大腿（水平）
        L(410, 376, 416, 432, BLUE_D, 30),       # 小腿（竖直）
        E(330, 440, 16, 7, INK, 0.5),            # 后脚跟抬起
        E(438, 436, 26, 11, INK), E(414, 434, 12, 8, INK),   # 鞋
        P("M 286 382 Q 280 316 336 282 L 376 298 Q 336 326 342 384 Z", RED),
        L(372, 302, 430, 412, SKIN, 25), C(434, 418, 12, SKIN),
        L(356, 312, 410, 418, SKIN, 21), C(414, 424, 11, SKIN),
        _head(392, 256, 0.88, look=(0.7, 0.5), face="o"),
        E(418, 424, 12, 7, WHITE), E(442, 421, 12, 7, WHITE), C(430, 423, 5, WHITE))

    # 踩：一脚踩进水坑，水花四溅
    a["踩"] = wrap(
        ground(390, 446, 260, 24),
        E(456, 434, 112, 20, WBLUE, 0.9),
        E(450, 432, 88, 13, "#a5d9f0", 0.9),
        kid(x=414, y=420, s=1.0, pose="walk", shirt=BLUE, arms="swing",
            face="o", look=(0.45, 0.35)),
        drop(500, 380, 10), drop(400, 372, 8), drop(542, 404, 9),
        drop(372, 400, 7), drop(462, 348, 8), drop(524, 350, 6),
        P("M 470 416 Q 486 396 504 412", stroke=WBLUE, w=8),
        P("M 424 416 Q 408 398 392 412", stroke=WBLUE, w=7))

    # 踏：前脚踏上一级级台阶
    a["踏"] = wrap(
        ground(420, 446, 270, 24),
        R(330, 414, 280, 32, 8, WOOD_L),
        R(452, 366, 158, 48, 8, WOOD),
        R(544, 318, 66, 48, 8, WOOD_D),
        kid(x=306, y=421, s=1.0, pose="stride", shirt=YEL, arms="swing",
            face="smile", look=(0.6, -0.2)),
        E(272, 442, 30, 7, "#a5d0bd", 0.8),
        _dash("M 196 340 Q 214 306 244 292", TEAL, 5))

    # 跨：双腿张开跨过小水沟（深沟+ Grass 边）
    a["跨"] = wrap(
        ground(290, 446, 170, 22), E(560, 448, 160, 20, GROUND),
        P("M 330 434 L 330 462 L 502 462 L 502 434 Z", "#8a5a33"),
        P("M 344 440 L 344 458 L 488 458 L 488 440 Z", "#6b4226"),
        E(330, 434, 26, 9, GREEN_L), E(502, 434, 26, 9, GREEN_L),
        kid(x=416, y=400, s=1.1, pose="stride", shirt=WBLUE, arms="swing",
            face="open", look=(0.5, 0.1)),
        _dash("M 300 424 Q 416 386 532 424", TEAL, 5, "5 12"))

    # 蹦：屈膝团身蹦起，双脚离地（区别 legacy 跳=直腿举臂+落地圈）
    a["蹦"] = wrap(
        ground(380, 446, 230, 22),
        _head(380, 188, 0.95, look=(0, -0.35), face="open"),
        R(352, 240, 56, 76, 24, TEAL),
        L(358, 258, 296, 296, SKIN, 26), C(292, 300, 13, SKIN),
        L(402, 258, 464, 296, SKIN, 26), C(468, 300, 13, SKIN),
        L(366, 316, 332, 356, BLUE_D, 30), L(332, 356, 354, 394, BLUE_D, 26),
        E(360, 400, 16, 9, INK),
        L(394, 316, 428, 356, BLUE_D, 30), L(428, 356, 406, 394, BLUE_D, 26),
        E(400, 400, 16, 9, INK),
        _dash("M 292 428 Q 380 402 468 428", TEAL, 6, "5 12"),
        _dash("M 250 454 Q 380 420 510 454", "#7cc8bb", 5, "5 12"),
        _dash("M 268 366 Q 258 338 272 314", "#7cc8bb", 5),
        _dash("M 492 366 Q 502 338 488 314", "#7cc8bb", 5))

    # 攀：双手上抓攀爬架横杠，身体悬空
    a["攀"] = wrap(
        ground(380, 446, 260, 24),
        R(232, 150, 22, 262, 9, WOOD_D), R(506, 150, 22, 262, 9, WOOD_D),
        R(220, 148, 320, 20, 9, WOOD),
        R(268, 168, 13, 32, 5, WOOD_L), R(340, 168, 13, 32, 5, WOOD_L),
        R(412, 168, 13, 32, 5, WOOD_L), R(484, 168, 13, 32, 5, WOOD_L),
        kid(x=370, y=386, s=0.95, pose="stand", shirt="#f0876f",
            arms="up", face="open", look=(0, -0.5)),
        C(292, 166, 14, SKIN_D), C(450, 166, 14, SKIN_D))

    # 登：登上平顶山顶插红旗
    a["登"] = wrap(
        ground(380, 452, 280, 22),
        P("M 110 442 L 330 150 L 430 150 L 660 442 Z", GREEN),
        P("M 430 150 L 660 442 L 500 442 Z", "#6f9e60"),
        _dash("M 180 416 Q 262 300 348 196", "#f6ecd6", 5),
        R(444, 62, 8, 88, 4, WOOD_D),
        PG([(452, 66), (510, 84), (452, 102)], RED),
        kid(x=366, y=150, s=0.55, pose="stand", shirt=BLUE, arms="up",
            face="open", look=(0.4, -0.4)))

    # 钻：弓身钻到桌子底下（低头迈步）
    a["钻"] = wrap(
        ground(380, 446, 270, 24),
        L(316, 388, 502, 380, GREEN, 58),
        _head(546, 364, 0.84, look=(0.85, 0.05), face="o"),
        L(510, 396, 532, 430, SKIN, 22), C(536, 434, 11, SKIN),
        L(478, 398, 488, 432, SKIN, 20), C(490, 436, 10, SKIN),
        L(346, 394, 312, 416, BLUE_D, 30), L(312, 416, 330, 438, BLUE_D, 25),
        E(340, 442, 15, 8, INK),
        L(386, 392, 356, 418, BLUE_D, 28), L(356, 418, 372, 440, BLUE_D, 23),
        E(382, 444, 14, 7, INK),
        table(380, 236, 300, 150, 28))

    # 跃：腾身跃过小河（前腿屈后腿蹬）
    a["跃"] = wrap(
        ground(190, 448, 180, 20), E(616, 448, 150, 20, GROUND),
        R(226, 410, 316, 42, 18, WBLUE),
        P("M 262 426 Q 282 420 302 426 T 342 426", stroke="#a5d9f0", w=5),
        P("M 402 434 Q 422 428 442 434 T 482 434", stroke="#a5d9f0", w=5),
        E(226, 428, 26, 20, GREEN_L), E(542, 428, 26, 20, GREEN_L),
        _dash("M 196 366 Q 386 236 574 352", TEAL, 6, "6 14"),
        kid(x=386, y=326, s=1.0, pose="sprint", shirt=RED, arms="pump",
            face="open", look=(0.75, -0.1)),
        drop(330, 402, 7), drop(452, 396, 7))

    # 滑：坐姿从滑梯滑下，双手举高
    a["滑"] = wrap(
        ground(430, 446, 280, 24),
        R(244, 196, 16, 218, 7, WOOD_D), R(304, 196, 16, 218, 7, WOOD_D),
        L(252, 244, 312, 244, WOOD_L, 10), L(252, 294, 312, 294, WOOD_L, 10),
        L(252, 344, 312, 344, WOOD_L, 10), L(252, 390, 312, 390, WOOD_L, 10),
        R(236, 182, 104, 22, 9, RED),
        P("M 318 194 L 372 168 L 622 380 L 566 414 Z", YEL),
        P("M 372 168 L 384 176 L 634 388 L 622 380 Z", YEL_D),
        _dash("M 372 226 Q 402 248 424 266", TEAL, 5),
        f'<g transform="rotate(41 470 290)">'
        + kid(x=470, y=318, s=0.78, pose="sit", shirt=GREEN, arms="up",
              face="open", look=(0.4, 0.3)) + "</g>",
        _dash("M 600 430 Q 622 442 646 444", TEAL, 5))

    # 泳：趴水面前游，一臂前伸出水，打腿溅花（区别 legacy 游=鱼）
    a["泳"] = wrap(
        ground(380, 448, 290, 22),
        E(380, 372, 330, 26, WBLUE, 0.35),
        L(330, 352, 480, 344, "#e8663c", 60),
        L(300, 338, 216, 314, SKIN, 24), C(208, 310, 12, SKIN),
        _head(272, 306, 0.85, look=(0.75, 0.05), face="o"),
        drop(196, 288, 8), drop(228, 274, 6), drop(244, 300, 5),
        P("M 486 330 Q 508 312 530 330", stroke=WBLUE, w=7),
        drop(512, 296, 9), drop(544, 314, 7), drop(478, 306, 6),
        P("M 40 372 Q 100 358 160 372 T 280 372 T 400 372 T 520 372 T 640 372 T 720 372 "
          "L 720 452 L 40 452 Z", WBLUE),
        P("M 120 408 Q 160 400 200 408 T 280 408", stroke="#a5d9f0", w=5),
        P("M 420 424 Q 460 416 500 424 T 580 424", stroke="#a5d9f0", w=5))

    # 骑：骑木马前后摇，双手抓把手
    a["骑"] = wrap(
        ground(380, 446, 250, 24),
        P("M 276 392 Q 380 448 484 392", stroke=WOOD_D, w=16),
        _dash("M 236 396 Q 258 424 288 434", TEAL, 5),
        _dash("M 524 396 Q 502 424 472 434", TEAL, 5),
        E(420, 306, 92, 40, WOOD),
        P("M 452 262 Q 470 216 504 224 Q 528 232 518 264 L 500 296 L 452 296 Z", WOOD),
        PG([(498, 214), (514, 196), (522, 220)], WOOD_D),
        P("M 470 226 Q 490 244 486 292", stroke=RED, w=10),
        E(430, 292, 60, 16, WOOD_L),
        L(340, 330, 316, 388, WOOD_D, 14), L(490, 330, 514, 388, WOOD_D, 14),
        kid(x=396, y=322, s=0.76, pose="sit", shirt=BLUE, arms="reach",
            face="open", look=(-0.6, 0.15), flip=-1),
        L(454, 238, 454, 262, "#8a5a33", 7), L(488, 238, 488, 262, "#8a5a33", 7),
        C(464, 250, 11, SKIN), C(480, 242, 11, SKIN))

    # 翻：侧翻跟头，头下脚上划弧线（区别 滚=团成球）
    a["翻"] = wrap(
        ground(380, 446, 250, 22),
        _dash("M 176 404 Q 380 178 586 404", TEAL, 7, "6 14"),
        f'<g transform="rotate(-120 380 300)">'
        + kid(x=380, y=352, s=0.95, pose="stand", shirt="#f0876f",
              arms="up", face="o") + "</g>",
        _dash("M 238 434 Q 258 448 284 452", TEAL, 4))

    # 滚：抱膝团成球侧滚（膝脚包在球缘+旋弧箭头；头贴球缘露大半，抱臂沿球面）
    a["滚"] = wrap(
        ground(380, 446, 240, 22),
        ball(380, 348, 96, TEAL, TEAL_D, TEAL_L),
        _rot(330, 404, 26, wrap(R(286, 386, 100, 34, 17, BLUE_D))),
        _rot(310, 396, 26, E(296, 392, 15, 9, INK)),
        L(356, 316, 436, 352, SKIN, 26), C(448, 358, 12, SKIN),
        _head(414, 288, 0.7, look=(0.5, 0.2), face="smile"),
        _dash("M 258 416 Q 222 348 258 280", TEAL, 6, "6 13"),
        PG([(246, 268), (284, 280), (246, 292)], TEAL),
        _dash("M 502 280 Q 538 348 502 416", "#7cc8bb", 5, "6 13"),
        PG([(514, 420), (478, 432), (514, 444)], "#7cc8bb"))

    # 散：一大一小牵手散步（区别 legacy 走/跑=单人）
    a["散"] = wrap(
        ground(390, 446, 300, 24),
        kid(x=268, y=430, s=1.05, pose="walk", shirt=PINK, bun=True, skirt=True,
            arms="hold_right", face="smile", look=(0.5, 0)),
        kid(x=398, y=430, s=0.8, pose="walk", shirt=BLUE,
            arms="hold_left", face="smile", look=(0.5, 0)),
        C(338, 328, 15, SKIN),
        _dash("M 148 330 Q 166 300 196 288", TEAL, 5),
        _dash("M 470 330 Q 488 300 518 288", TEAL, 5))

    # 奔：奋力前奔，汗滴飞出（区别 legacy 跑=普通跑步）
    a["奔"] = wrap(
        ground(420, 446, 260, 24),
        kid(x=350, y=430, s=1.05, pose="sprint", shirt=GREEN, arms="pump",
            face="open", look=(0.85, 0)),
        drop(246, 244, 11), drop(216, 292, 9), drop(254, 204, 8),
        _dash("M 138 312 L 236 308", TEAL, 6),
        _dash("M 128 352 L 230 350", TEAL, 6),
        _dash("M 146 392 L 240 390", TEAL, 6))

    # 冲：冲刺冲过终点线（彩带在后，身体前压）
    a["冲"] = wrap(
        ground(390, 446, 270, 24),
        R(176, 254, 14, 192, 6, WOOD_D), R(610, 248, 14, 198, 6, WOOD_D),
        PG([(190, 254), (232, 268), (190, 282)], RED),
        PG([(624, 248), (668, 262), (624, 276)], RED),
        P("M 190 262 Q 400 300 616 256", stroke=RED, w=10),
        kid(x=406, y=430, s=1.05, pose="sprint", shirt=BLUE, arms="pump",
            face="open", look=(0.85, 0)),
        _dash("M 236 330 L 316 326", TEAL, 5),
        _dash("M 226 372 L 310 370", TEAL, 5))

    # 梦：睡着+头顶大梦中泡泡（泡泡里有月亮星星；区别 legacy 睡=床上盖被+天上月亮）
    a["梦"] = wrap(
        ground(320, 442, 270, 22),
        E(234, 400, 52, 14, "#f4d3a4"),
        kid(x=290, y=420, s=1.15, pose="sleep", shirt=BLUE,
            extra=wrap(
                C(392, 302, 9, WHITE, 0.95), C(422, 270, 12, WHITE, 0.95),
                C(454, 240, 15, WHITE, 0.95),
                cloud_p(540, 178, 1.9, WHITE),
                C(540, 170, 40, SUN), C(558, 160, 34, WHITE),
                star5(486, 208, 14), star5(602, 146, 12))))

    # 澡：泡泡浴，泡泡盖满，头顶泡泡帽，小黄鸭作伴
    a["澡"] = wrap(
        ground(380, 446, 250, 22),
        R(238, 444, 26, 14, 6, "#c9cdd1"), R(496, 444, 26, 14, 6, "#c9cdd1"),
        R(200, 330, 360, 118, 26, WHITE),
        R(212, 320, 336, 20, 10, "#e8e4da"),
        E(380, 330, 150, 12, WBLUE, 0.8),
        C(244, 312, 28, WHITE), C(292, 300, 36, WHITE), C(352, 292, 42, WHITE),
        C(414, 298, 38, WHITE), C(470, 310, 30, WHITE),
        R(234, 306, 280, 26, 13, WHITE),
        _head(378, 246, 0.92, look=(0, 0.15), face="smile"),
        C(346, 194, 27, WHITE), C(384, 186, 32, WHITE), C(416, 200, 24, WHITE),
        C(302, 318, 13, SKIN), C(454, 318, 13, SKIN),
        E(534, 304, 24, 17, YEL), C(554, 286, 15, YEL),
        PG([(566, 284), (582, 289), (566, 296)], "#e8663c"),
        C(549, 282, 3.5, INK),
        C(566, 232, 13, WBLUE, 0.55), C(604, 192, 10, WBLUE, 0.55),
        C(200, 236, 11, WBLUE, 0.5), C(172, 284, 8, WBLUE, 0.5),
        C(598, 258, 7, WBLUE, 0.5), C(158, 226, 6, WBLUE, 0.5))

    # 望：站上小坡手搭额头远眺，远处小鸟、白云、小树都很小（区别 legacy 看=抬头看鸟）
    a["望"] = wrap(
        ground(360, 446, 260, 24),
        E(330, 442, 140, 26, "#9cc98a"),
        cloud_p(566, 92, 0.6, WHITE),
        P("M 610 168 Q 626 152 642 168 Q 658 152 674 168", stroke=INK, w=5),
        tree_round(708, 446, 0.42),
        kid(x=320, y=420, s=1.05, pose="stand", shirt=TEAL, arms="down",
            look=(0.9, -0.2), face="o"),
        L(366, 250, 406, 200, SKIN, 31),
        L(406, 200, 356, 140, SKIN, 31),
        C(356, 140, 14, SKIN))

    # 扭：扭腰摆臂，腰边两条扭动弧+脚下摆动
    a["扭"] = wrap(
        ground(380, 446, 240, 22),
        f'<g transform="rotate(-9 380 430)">'
        + kid(x=380, y=430, s=1.0, pose="stand", shirt=RED, arms="swing",
              face="open", look=(0.35, 0)) + "</g>",
        _dash("M 286 366 Q 266 396 288 428", RED, 6),
        _dash("M 474 366 Q 494 396 472 428", RED, 6),
        _dash("M 300 444 Q 380 456 460 444", "#7cc8bb", 5))

    return a


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    cards = GROUP_CARDS
    assert [c["char"] for c in cards] == list(D_CHARS), "字序与 B11 分配清单不一致"
    amap = arts()
    assert list(amap.keys()) == list(D_CHARS), "arts key 与清单不一致"
    tone_marks = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    for c in cards:
        k = c["char"]
        assert k in c["sentence"], f"{k}: sentence 未含目标字"
        body = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        assert 4 <= body <= 10, f"{k}: sentence 长度 {body}"
        for fld in ("say", "chat", "life"):
            assert len(c[fld]) <= 30, f"{k}: {fld} 超长({len(c[fld])})"
            assert c[fld], f"{k}: 缺 {fld}"
        assert any(m in c["pinyin"] for m in tone_marks), f"{k}: 拼音缺调号"
        v = amap[k]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">{v}</svg>')
        low = v.lower()
        assert not any(t in low for t in ("<text", "<use", "<defs", "<image", "href")), k
    print(f"dongzuo3 自检通过：{len(cards)} 卡，SVG 全部合法")
