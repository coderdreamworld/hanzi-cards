#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""学习文教组 18 卡插画与文案（1000 字批次 B9，全组新增）。

字表（字库 xuexi 尾段，legacy 已覆盖前 20 字）：题奖室板考试名班教答页铅橡胶墨记认识。
（批次分配.json 的 B9 xuexi 节还列了"音"，但 legacy 学习文教组已有"音"卡，
重复生产会成重复卡，故不产——与任务要求的 18 卡一致。）

一眼可辨约定（主控硬规则）：
题=卷子+大问号+铅笔 / 奖=金杯金星+奖牌 / 室=教室门+门牌（图形色块）/
板=黑板+板擦粉笔 / 考=娃娃坐桌前答卷 / 试=卷子打大勾 /
名=挂绳名牌（星标无字）/ 班=娃娃戴星星袖标 / 教=老师拿教鞭 /
答=问号变打勾 / 页=翻开的书页在翻动 / 铅=大铅笔 / 橡=橡皮擦纸屑 /
胶=胶水粘纸 / 墨=墨水瓶+毛笔 / 记=记事本+笔 / 认=两娃握手问好 /
识=举识字卡认一认。同组相邻卡轮廓+主色错开。
"""
import importlib.util
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
ORANGE, ORANGE_D = "#e8742a", "#c95f1e"
PURPLE = "#9a6bb0"
BOARD = "#3f5f52"
BOARD_D = "#334f44"
GRAY, GRAY_D, LGRAY = "#c9cdd1", "#9aa2ab", "#d8d2c2"
SHADOWG = "#a5d0bd"
ROSE = "#e87d9d"

GROUP_CARDS = [
    {"char": "题", "pinyin": "tí", "tone": "第二声",
     "sentence": "这道题我会做。",
     "say": "要动脑筋回答的，叫题目。",
     "chat": "你遇到过最有趣的题是什么？",
     "life": "不会的题圈出来问老师。"},
    {"char": "奖", "pinyin": "jiǎng", "tone": "第三声",
     "sentence": "比赛得了大奖杯。",
     "say": "得了第一名，奖杯亮闪闪。",
     "chat": "你想得一个什么奖呀？",
     "life": "把奖状贴在墙上夸夸他。"},
    {"char": "室", "pinyin": "shì", "tone": "第四声",
     "sentence": "教室门口有门牌。",
     "say": "有门牌的房间，就是教室。",
     "chat": "你们教室的门牌什么颜色？",
     "life": "认一认教室门上的牌子。"},
    {"char": "板", "pinyin": "bǎn", "tone": "第三声",
     "sentence": "老师在黑板上写字。",
     "say": "黑黑的板叫黑板，能写能擦。",
     "chat": "黑板上画了什么呀？",
     "life": "在小黑板上画画给他看。"},
    {"char": "考", "pinyin": "kǎo", "tone": "第三声",
     "sentence": "考试时专心写。",
     "say": "坐桌前认真答卷，是考试。",
     "chat": "考试的时候你会紧张吗？",
     "life": "像考试一样安静做完一件事。"},
    {"char": "试", "pinyin": "shì", "tone": "第四声",
     "sentence": "试一试，打个大勾。",
     "say": "做完卷子打上勾，通过了。",
     "chat": "新的游戏你想试一试吗？",
     "life": "学新本领先试一试。"},
    {"char": "名", "pinyin": "míng", "tone": "第二声",
     "sentence": "名牌上写着我的名字。",
     "say": "写着名字的牌子，叫名牌。",
     "chat": "你的名字是谁给取的呀？",
     "life": "在水杯上贴一张名牌。"},
    {"char": "班", "pinyin": "bān", "tone": "第一声",
     "sentence": "我是班里的小班长。",
     "say": "戴星星袖标的，是班长。",
     "chat": "班长要做哪些事情呀？",
     "life": "今天当一次小班长试试。"},
    {"char": "教", "pinyin": "jiāo", "tone": "第四声（'教育'义；表'传授'读 jiāo，如本句'教唱歌'）",
     "sentence": "老师教我们唱歌。",
     "say": "拿着教鞭的老师在教本领。",
     "chat": "老师教过你们什么呀？",
     "life": "当小老师，教家人念儿歌。"},
    {"char": "答", "pinyin": "dá", "tone": "第二声（另读 dā，如'答应'）",
     "sentence": "我会大声回答。",
     "say": "问号提问题，打勾是答案。",
     "chat": "老师提问你举手回答吗？",
     "life": "妈妈问话时大声回答。"},
    {"char": "页", "pinyin": "yè", "tone": "第四声",
     "sentence": "翻到下一页。",
     "say": "书翻过去一张，就是一页。",
     "chat": "这本书你翻到第几页啦？",
     "life": "睡前一起翻一页绘本。"},
    {"char": "铅", "pinyin": "qiān", "tone": "第一声",
     "sentence": "我用铅笔画画画。",
     "say": "木头的铅笔，能写能画。",
     "chat": "你的铅笔是什么颜色呀？",
     "life": "削好铅笔准备画画。"},
    {"char": "橡", "pinyin": "xiàng", "tone": "第四声",
     "sentence": "写错了，橡皮擦一擦。",
     "say": "橡皮能把写错的擦干净。",
     "chat": "橡皮擦能擦掉什么呀？",
     "life": "写错不用怕，擦掉再写。"},
    {"char": "胶", "pinyin": "jiāo", "tone": "第一声",
     "sentence": "胶水把纸粘住了。",
     "say": "白白的胶水，粘东西很牢。",
     "chat": "胶水能粘住哪些东西呀？",
     "life": "做手工用胶水贴纸。"},
    {"char": "墨", "pinyin": "mò", "tone": "第四声",
     "sentence": "毛笔蘸墨写字。",
     "say": "黑黑的墨水，毛笔蘸一蘸。",
     "chat": "墨水是什么颜色的呀？",
     "life": "看家人写毛笔字蘸墨。"},
    {"char": "记", "pinyin": "jì", "tone": "第四声",
     "sentence": "我用本子记事情。",
     "say": "好事情都写进记事本。",
     "chat": "今天最想记下哪件事呀？",
     "life": "画一笔，记下开心的事。"},
    {"char": "认", "pinyin": "rèn", "tone": "第四声",
     "sentence": "认识你，真开心。",
     "say": "见面握手问好，是认识。",
     "chat": "你和好朋友是怎么认识的？",
     "life": "见到新朋友主动打招呼。"},
    {"char": "识", "pinyin": "shí", "tone": "第二声",
     "sentence": "看卡片识字真快。",
     "say": "看着卡片认出字，就是识。",
     "chat": "这张卡片上是什么字呀？",
     "life": "抽一张识字卡玩猜字游戏。"},
]


# ---------- 本组小工具 ----------
def _km(x, y, s, pose="stand"):
    """kid 关键坐标：头半径/肩线/头心/髋部。"""
    hd = 62 * s
    if pose == "sit":
        hip = y - 78 * s
        sho = hip - 74 * s
    else:
        hip = y - 96 * s
        sho = y - 168 * s
    hcy = sho - 8 * s - hd
    return hd, sho, hcy, hip


def _qmark(cx, cy, s, color=INK, w=None):
    """问号（允许符号）。"""
    return P(f"M {cx-52*s} {cy-60*s} q {-10*s} {-56*s} {36*s} {-62*s} "
             f"q {44*s} {-6*s} {46*s} {32*s} q {2*s} {32*s} {-30*s} {42*s} l 0 {22*s}",
             stroke=color, w=w or 10 * s) + C(cx, cy + 18 * s, 8 * s, color)


def _pencil(tip_x, tip_y, ang=0, ln=150, body=YEL):
    """铅笔：笔尖在 (tip_x,tip_y)，笔身朝上，ang 顺时针旋转。"""
    g = wrap(
        PG([(tip_x, tip_y), (tip_x - 16, tip_y - 34), (tip_x + 16, tip_y - 34)], WOOD_L),
        PG([(tip_x, tip_y), (tip_x - 6, tip_y - 13), (tip_x + 6, tip_y - 13)], INK),
        R(tip_x - 16, tip_y - 34 - ln, 32, ln, 4, body),
        L(tip_x - 9, tip_y - 36, tip_x - 9, tip_y - 34 - ln, "#d99a2b", 4),
        R(tip_x - 16, tip_y - 52 - ln, 32, 20, 4, GRAY),
        R(tip_x - 14, tip_y - 82 - ln, 28, 30, 10, PINK))
    return f'<g transform="rotate({ang} {tip_x} {tip_y})">{g}</g>'


def _wline(x, y, ln, color=LGRAY, w=7):
    """卷子上的写字波浪线。"""
    return P(f"M {x} {y} q {ln*0.3:.0f} 8 {ln*0.55:.0f} 0 q {ln*0.22:.0f} -6 {ln*0.45:.0f} 2",
             stroke=color, w=w)


# ---------- 卡片插画 ----------
def a_ti():
    """题：卷子上有大问号，铅笔准备好。"""
    g = ground()
    sheet = (f'<g transform="rotate(-3 385 290)">'
             + R(250, 150, 270, 280, 16, WHITE)
             + _wline(285, 205, 190)
             + _wline(285, 245, 190)
             + "</g>")
    g += sheet
    g += _qmark(372, 348, 1.05, INK)
    g += _pencil(560, 428, 35, 130)
    return g


def a_jiang():
    """奖：金灿灿的大奖杯，旁边挂一块奖牌。"""
    g = ground()
    cup = wrap(
        P("M 306 216 Q 246 218 258 272 Q 266 304 310 298", stroke="#d99a2b", w=16),
        P("M 454 216 Q 514 218 502 272 Q 494 304 450 298", stroke="#d99a2b", w=16),
        P("M 302 196 L 458 196 L 446 296 Q 442 330 380 338 Q 318 330 314 296 Z", YEL),
        R(360, 338, 40, 36, 6, YEL_D),
        R(320, 372, 120, 34, 10, YEL_D),
        R(304, 404, 152, 30, 10, WOOD_D),
        star5(380, 252, 34, WHITE))
    medal = wrap(
        PG([(536, 296), (584, 296), (574, 350), (546, 350)], RED),
        C(560, 386, 34, YEL),
        C(560, 386, 24, YEL_D),
        star5(560, 386, 13, WHITE))
    spark = wrap(
        L(268, 160, 268, 184, SUN, 7) + L(256, 172, 280, 172, SUN, 7),
        L(500, 150, 500, 170, SUN, 6) + L(490, 160, 510, 160, SUN, 6))
    return g + cup + medal + spark


def a_shi():
    """室：教室的门，门上挂着门牌。"""
    g = ground()
    door = wrap(
        R(280, 150, 212, 290, 10, WOOD_L),
        R(294, 164, 184, 276, 8, BLUE),
        R(316, 192, 140, 92, 10, BLUE_D),
        R(316, 306, 140, 110, 10, BLUE_D),
        C(458, 316, 11, YEL))
    plate = wrap(
        R(300, 92, 172, 54, 10, "#fbf0c2"),
        P(f"M 312 100 L 460 100 L 460 138 L 312 138 Z", fill="none", stroke=WOOD_D, w=4),
        C(352, 119, 15, RED),
        L(352, 104, 356, 96, "#5e8f52", 5),
        E(364, 104, 9, 5, GREEN),
        star5(420, 119, 14, "#e8a13c"))
    return g + door + plate


def a_ban():
    """板：黑板写画好，板擦和粉笔搁在槽上。"""
    g = ground()
    board = wrap(
        R(180, 158, 400, 242, 14, WOOD),
        R(196, 174, 368, 210, 10, BOARD))
    chalk = wrap(
        P("M 236 240 q 30 -18 60 0 q 30 18 60 0 q 26 -14 50 0", stroke=WHITE, w=7),
        f'<circle cx="516" cy="238" r="24" fill="none" stroke="{WHITE}" stroke-width="6"/>',
        PG([(238, 330), (296, 330), (267, 286)], WHITE),
        P("M 330 322 q 28 -12 56 0", stroke=WHITE, w=6))
    tray = wrap(
        R(216, 394, 344, 20, 8, WOOD_L),
        R(470, 384, 46, 10, 5, WHITE),
        R(346, 378, 86, 28, 8, ORANGE),
        R(346, 372, 86, 14, 7, LGRAY))
    return g + board + chalk + tray


def a_kao():
    """考：坐在桌前认真答卷。"""
    g = ground()
    g += kid(455, 436, s=0.85, pose="sit", face="o", shirt=BLUE, look=(0.7, 0.9))
    desk = wrap(
        R(390, 350, 24, 88, 8, WOOD_D),
        R(576, 350, 24, 88, 8, WOOD_D),
        R(370, 326, 250, 26, 10, WOOD),
        R(370, 340, 250, 12, 6, WOOD_D))
    paper = (f'<g transform="rotate(-4 495 320)">'
             + R(432, 288, 126, 64, 8, WHITE)
             + L(452, 308, 536, 308, LGRAY, 6)
             + L(452, 326, 520, 326, LGRAY, 6)
             + "</g>")
    pencil = _pencil(556, 338, -16, 82)
    grip = wrap(L(472, 292, 566, 297, SKIN, 24), C(574, 296, 11, SKIN))
    return g + desk + paper + pencil + grip


def a_shi2():
    """试：卷子做完，打上一个大勾。"""
    g = ground()
    sheet = (f'<g transform="rotate(2 380 295)">'
             + R(230, 170, 300, 250, 16, WHITE)
             + L(268, 214, 372, 214, LGRAY, 8)
             + L(268, 248, 350, 248, LGRAY, 8)
             + "</g>")
    g += sheet
    g += check(368, 322, 62, TEAL)
    g += star5(478, 216, 26, SUN)
    return g


def a_ming():
    """名：挂着带子的名牌，牌上一颗星。"""
    g = ground()
    straps = wrap(
        P("M 292 44 Q 348 124 372 198", stroke=TEAL, w=22),
        P("M 468 44 Q 412 124 388 198", stroke=TEAL, w=22),
        R(364, 196, 32, 28, 6, GRAY_D))
    badge = wrap(
        R(292, 224, 176, 128, 18, YEL),
        R(306, 238, 148, 100, 12, WHITE),
        star5(380, 288, 30, SUN))
    return g + straps + badge


def a_ban2():
    """班：戴上星星袖标的小班长。"""
    g = ground()
    g += kid(380, 446, s=1.0, face="open", shirt=TEAL, arms="down")
    band = (f'<g transform="rotate(-16 322 314)">'
            + R(292, 294, 60, 40, 10, RED)
            + star5(322, 314, 12, YEL)
            + "</g>")
    g += band
    return g


def a_jiao():
    """教：老师拿教鞭指一指，教你本领。"""
    g = ground()
    g += kid(340, 436, s=1.05, face="smile", shirt=PURPLE, arms="down",
             glasses=True, bun=True, skirt=True, look=(1.8, 0))
    pointer = wrap(
        L(390, 330, 560, 448, WOOD_D, 9),
        C(407, 341, 14, SKIN),
        P("M 566 428 q 18 -8 30 2", stroke=GRAY_D, w=6),
        P("M 574 448 q 16 -6 26 4", stroke=GRAY_D, w=5))
    return g + pointer


def a_da():
    """答：问号提出问题，大勾是答案。"""
    g = ground()
    g += _qmark(258, 288, 1.35, "#8a6a4a")
    arrow = wrap(
        P("M 352 306 Q 402 278 446 298", stroke=GRAY_D, w=9),
        PG([(462, 306), (432, 276), (428, 310)], GRAY_D))
    g += arrow
    g += check(566, 292, 66, TEAL)
    return g


def a_ye():
    """页：翻开的书，一页正在翻过去。"""
    g = ground()
    book = wrap(
        P("M 380 264 L 236 240 L 236 410 Q 310 430 380 416 Q 450 430 524 410 "
          "L 524 240 L 380 264 Z", TEAL_D),
        P("M 372 276 L 252 254 L 252 398 Q 316 416 372 404 Z", WHITE),
        P("M 388 276 L 508 254 L 508 398 Q 444 416 388 404 Z", WHITE),
        L(380, 268, 380, 414, TEAL_D, 5),
        L(272, 292, 352, 306, LGRAY, 6),
        L(272, 330, 352, 344, LGRAY, 6),
        L(408, 306, 488, 292, LGRAY, 6))
    flip = wrap(
        P("M 498 262 Q 498 176 396 194 Q 448 210 460 258 Q 476 274 498 262 Z", WHITE),
        P("M 498 262 Q 498 176 396 194", stroke=LGRAY, w=4),
        P("M 420 148 q 20 -14 42 -4", stroke=GRAY, w=5),
        P("M 448 128 q 20 -14 42 -4", stroke=GRAY, w=5))
    return g + book + flip


def a_qian():
    """铅：一支大铅笔，正在画线。"""
    g = ground()
    g += _pencil(370, 430, 0, 230)
    g += P("M 372 438 q 46 14 92 2", stroke=INK, w=6)
    return g


def a_xiang():
    """橡：橡皮擦过去，纸屑飞起来。"""
    g = ground()
    paper = wrap(
        R(200, 352, 360, 86, 10, WHITE),
        _wline(236, 384, 150),
        P("M 380 388 q 26 10 52 0 q 20 -8 44 2", stroke=LGRAY, w=6, opacity=0.6))
    eraser = (f'<g transform="rotate(-14 470 252)">'
              + R(388, 210, 172, 56, 16, WHITE)
              + R(388, 254, 172, 44, 16, BLUE)
              + "</g>")
    crumbs = wrap(
        C(430, 322, 7, LGRAY), C(468, 302, 6, LGRAY), C(502, 330, 5, LGRAY),
        C(396, 336, 5, LGRAY), C(448, 344, 4, LGRAY))
    arcs = wrap(
        P("M 470 300 q 16 -12 32 -2", stroke=GRAY, w=5),
        P("M 498 282 q 16 -12 32 -2", stroke=GRAY, w=5))
    return g + paper + crumbs + eraser + arcs


def a_jiao2():
    """胶：胶水把两张纸粘在一起。"""
    g = ground()
    bottle = (f'<g transform="rotate(-32 330 250)">'
              + R(352, 118, 56, 44, 10, ORANGE)
              + R(368, 100, 24, 22, 8, ORANGE_D)
              + P("M 320 208 Q 320 178 348 172 L 412 172 Q 440 178 440 208 "
                  "L 440 330 Q 440 358 412 362 L 348 362 Q 320 358 320 330 Z", WHITE)
              + R(340, 236, 80, 60, 10, "#eaf3f8")
              + "</g>")
    glue = wrap(
        P("M 300 130 Q 290 260 330 384", stroke=WHITE, w=18),
        C(332, 388, 13, WHITE))
    papers = wrap(
        f'<g transform="rotate(-6 340 424)">{R(276, 390, 122, 72, 8, "#7cc8bb")}</g>',
        f'<g transform="rotate(5 430 420)">{R(368, 384, 122, 72, 8, YEL)}</g>')
    return g + bottle + glue + papers


def a_mo():
    """墨：墨水瓶配毛笔，蘸墨写字。"""
    g = ground()
    bottle = wrap(
        P("M 300 250 L 300 380 Q 300 408 328 410 L 412 410 Q 440 408 440 380 "
          "L 440 250 Q 440 236 424 230 L 424 210 L 316 210 L 316 230 "
          "Q 300 236 300 250 Z", "#4a4a4a"),
        E(370, 210, 54, 10, "#2b2b2b"),
        R(330, 290, 80, 72, 8, WHITE))
    brush = (f'<g transform="rotate(16 560 430)">'
             + R(546, 130, 30, 234, 14, WOOD_L)
             + R(546, 362, 30, 26, 5, GRAY_D)
             + P("M 546 388 L 576 388 Q 570 446 561 458 Q 552 446 546 388 Z", INK)
             + "</g>")
    swash = wrap(
        R(440, 434, 200, 36, 8, WHITE),
        P("M 466 452 q 44 -16 88 -2", stroke=INK, w=9),
        drop(600, 420, 9, INK))
    return g + bottle + brush + swash


def a_ji():
    """记：记事本记一记，末尾打个勾。"""
    g = ground()
    book = wrap(
        R(270, 200, 220, 240, 14, "#7cc8bb"),
        R(286, 214, 188, 212, 10, WHITE))
    rings = ""
    for ry in (244, 292, 340, 388):
        rings += f'<circle cx="288" cy="{ry}" r="8" fill="none" stroke="{GRAY_D}" stroke-width="5"/>'
    lines = wrap(
        L(320, 262, 446, 262, LGRAY, 7),
        L(320, 310, 446, 310, LGRAY, 7),
        L(320, 358, 420, 358, LGRAY, 7))
    band = R(446, 200, 24, 240, 10, RED, 0.92)
    return g + book + rings + lines + check(430, 396, 20, TEAL) + band \
        + _pencil(566, 424, 24, 118)


def a_ren():
    """认：两个娃娃握手问好，认识啦。"""
    g = ground()
    g += kid(250, 444, s=0.92, face="open", shirt=ORANGE, arms="point",
             point_at=(411, 356), look=(1.8, 0))
    g += kid(510, 444, s=0.92, face="smile", shirt=BLUE, arms="reach",
             look=(-1.8, 0.2))
    g += C(408, 354, 15, SKIN) + C(422, 348, 13, SKIN)
    g += heart(380, 196, 18, RED) + heart(424, 162, 10, RED)
    return g


def a_shi3():
    """识：举起识字卡，认一认上面是什么。"""
    g = ground()
    card = (f'<g transform="rotate(5 500 290)">'
            + R(410, 200, 180, 180, 16, WHITE)
            + star5(500, 290, 52, SUN)
            + C(432, 222, 6, LGRAY) + C(500, 222, 6, LGRAY)
            + "</g>")
    g += card
    g += kid(300, 444, s=0.95, face="open", shirt=GREEN, arms="point",
             point_at=(452, 300), look=(2, 0))
    return g


def arts():
    return {
        "题": a_ti(), "奖": a_jiang(), "室": a_shi(), "板": a_ban(),
        "考": a_kao(), "试": a_shi2(), "名": a_ming(), "班": a_ban2(),
        "教": a_jiao(), "答": a_da(), "页": a_ye(), "铅": a_qian(),
        "橡": a_xiang(), "胶": a_jiao2(), "墨": a_mo(), "记": a_ji(),
        "认": a_ren(), "识": a_shi3(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    lg_spec = importlib.util.spec_from_file_location(
        "lg_xuexi", str(ROOT.parent / "识字卡片_素材_xuexi.py"))
    lg = importlib.util.module_from_spec(lg_spec)
    lg_spec.loader.exec_module(lg)
    legacy_chars = {c["char"] for c in lg.GROUP_CARDS}
    all_chars = []
    for grp in ziku.GROUPS:
        if grp["id"] == "xuexi":
            all_chars = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in all_chars if c not in legacy_chars]
    assert set(all_chars) == legacy_chars | set(expect), "legacy 覆盖与字库对不上"
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"学习文教组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}），legacy 已含 {len(legacy_chars)} 字")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对（去掉 legacy 20 字）：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != re.sub(r"（.*?）", "", c["tone"])]
    print(f"拼音/声调：{'与拼音表一致（括注为另读注）✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len(c["sentence"]) - 1 <= 10)]
    miss = [c["char"] for c in GROUP_CARDS if c["char"] not in c["sentence"]]
    print(f"三段长度：{'全部 ≤30 ✓' if not lens else str(lens)}")
    print(f"句长 4–10：{'全部达标 ✓' if not sl else str(sl)}")
    print(f"句含目标字：{'全部 ✓' if not miss else str(miss)}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
        if not v.startswith("<ellipse"):
            bad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
