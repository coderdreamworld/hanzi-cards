#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""常用字组 19 卡插画与文案（1000 字批次 B9，全组新增）。

字表（字库 changyong 尾段，legacy 已覆盖前 37 字）：呢哦啦往跟越让些或刚各爱应该行能已懂嗯。

一眼可辨约定（主控硬规则）：
呢=手放耳边听+小问号 / 哦=头顶亮灯泡恍然大悟 / 啦=跳起欢呼+彩带 /
往=大箭头指前方娃娃走 / 跟=大小娃娃一前一后走 / 越=三级台阶越跳越高 /
让=把大苹果递给伙伴 / 些=三个球对一小堆球 / 或=两条岔路二选一 /
刚=挂钟+刚进家门 / 各=三只彩杯各归各位 / 爱=抱住大爱心 /
应=举手答应+嘴边声波 / 该=清单逐条打勾 / 行=大步走+竖大拇指 /
能=头顶举起大皮球 / 已=山顶插旗+大勾 / 懂=点头+小灯泡 / 嗯=点头嘟嘴答应。
虚词用小场景+手势表达，不硬造物体；同组相邻卡轮廓+主色错开。
"""
import importlib.util
import json
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
OLIVE = "#8a9e5c"
ROSE = "#e87d9d"
GRAY, GRAY_D, LGRAY = "#c9cdd1", "#9aa2ab", "#d8d2c2"
SHADOWG = "#a5d0bd"
TAN, TAN_L = "#c9b79a", "#e0d2b4"

GROUP_CARDS = [
    {"char": "呢", "pinyin": "ne", "tone": "轻声",
     "sentence": "妈妈在哪儿呢？",
     "say": "歪着头想一想，句尾加个呢。",
     "chat": "'小猫躲哪儿呢？'是在问什么？",
     "life": "玩捉迷藏时问：躲哪儿呢？"},
    {"char": "哦", "pinyin": "ò", "tone": "第四声",
     "sentence": "哦，原来是这样！",
     "say": "一下子明白，头顶灯泡亮。",
     "chat": "什么时候你会说'哦，懂了'？",
     "life": "拼图拼对了说：哦，是这样！"},
    {"char": "啦", "pinyin": "lā", "tone": "第一声（句尾常读轻声）",
     "sentence": "放学啦，真开心。",
     "say": "高兴欢呼时，句尾加上啦。",
     "chat": "什么时候你会喊'来啦'？",
     "life": "进门大声喊：我回来啦！"},
    {"char": "往", "pinyin": "wǎng", "tone": "第三声",
     "sentence": "一直往前走。",
     "say": "大箭头指的方向，就是往前。",
     "chat": "去公园要往哪边走呀？",
     "life": "散步时说：往前走，别停。"},
    {"char": "跟", "pinyin": "gēn", "tone": "第一声",
     "sentence": "我跟在妈妈后面走。",
     "say": "大的走前面，小的跟后面。",
     "chat": "你最喜欢跟着谁呀？",
     "life": "排队时跟紧前面的小朋友。"},
    {"char": "越", "pinyin": "yuè", "tone": "第四声",
     "sentence": "越跳越高真开心。",
     "say": "一次比一次跳得高，就是越。",
     "chat": "怎样能越跳越高呀？",
     "life": "跳三下，争取越跳越高。"},
    {"char": "让", "pinyin": "ràng", "tone": "第四声",
     "sentence": "我把苹果让给你。",
     "say": "把东西递给别人，就是让。",
     "chat": "坐车的时候你会让座吗？",
     "life": "吃水果先让给长辈一块。"},
    {"char": "些", "pinyin": "xiē", "tone": "第一声",
     "sentence": "拿一些球来玩吧。",
     "say": "三个是一小些，一堆是好多。",
     "chat": "一小堆和一大堆哪个多呀？",
     "life": "分饼干时说：给你一些。"},
    {"char": "或", "pinyin": "huò", "tone": "第四声",
     "sentence": "走这条路或那条路。",
     "say": "两条岔路选一条，就是或。",
     "chat": "苹果或香蕉，你想吃哪个？",
     "life": "选玩具时说：红的或蓝的。"},
    {"char": "刚", "pinyin": "gāng", "tone": "第一声",
     "sentence": "我刚进家门。",
     "say": "钟刚走到，人刚进门，就是刚。",
     "chat": "你刚才是从哪儿回来的呀？",
     "life": "到家就说一句：我刚回来！"},
    {"char": "各", "pinyin": "gè", "tone": "第四声",
     "sentence": "杯子各回各的位置。",
     "say": "红黄蓝三只杯，各放各的。",
     "chat": "你的杯子放在哪里呀？",
     "life": "玩具玩完，各归各位。"},
    {"char": "爱", "pinyin": "ài", "tone": "第四声",
     "sentence": "我爱爸爸妈妈。",
     "say": "张开手臂抱住爱心，就是爱。",
     "chat": "你最爱和家人做什么呀？",
     "life": "睡前抱抱家人说：我爱你。"},
    {"char": "应", "pinyin": "yìng", "tone": "第四声（另读 yīng，如'应该'）",
     "sentence": "老师点名我答应。",
     "say": "叫到名字举手答'到'，是答应。",
     "chat": "妈妈叫你时你会答应吗？",
     "life": "听到名字大声答一声：哎！"},
    {"char": "该", "pinyin": "gāi", "tone": "第一声",
     "sentence": "该睡觉啦。",
     "say": "清单都打了勾，该做的做完啦。",
     "chat": "现在该做什么了呀？",
     "life": "睡前一起核对：刷牙该做啦。"},
    {"char": "行", "pinyin": "xíng", "tone": "第二声（另读 háng，如'一行'）",
     "sentence": "竖起拇指说声行。",
     "say": "大步走加竖拇指，说声行！",
     "chat": "爸爸说'行'，就可以去做啦？",
     "life": "商量事情时问：这样行不行？"},
    {"char": "能", "pinyin": "néng", "tone": "第二声",
     "sentence": "我能举起大皮球。",
     "say": "大球也举得起来，真能干。",
     "chat": "什么事你现在能自己做了？",
     "life": "试一件新小事，说：我能行！"},
    {"char": "已", "pinyin": "yǐ", "tone": "第三声",
     "sentence": "作业已经写完了。",
     "say": "旗子插上山顶，已经到终点。",
     "chat": "已经做完的事有哪些呀？",
     "life": "收好玩具说：已经收好啦！"},
    {"char": "懂", "pinyin": "dǒng", "tone": "第三声",
     "sentence": "听一遍就懂了。",
     "say": "点着头灯泡一亮，听懂了。",
     "chat": "妈妈讲的故事你听懂了吗？",
     "life": "听完指令说一遍，看懂没懂。"},
    {"char": "嗯", "pinyin": "ǹg", "tone": "第四声",
     "sentence": "嗯，好的，就这样。",
     "say": "轻轻哼一声嗯，是答应了。",
     "chat": "妈妈问'好吗'，你会嗯一声吗？",
     "life": "答应时点点头说：嗯！"},
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


def _dash(x1, y1, x2, y2, color, w, dash="14 16"):
    return (f'<path d="M {x1} {y1} L {x2} {y2}" stroke="{color}" stroke-width="{w}" '
            f'stroke-dasharray="{dash}" stroke-linecap="round"/>')


def _qmark(cx, cy, s, color=INK, w=None):
    """问号（允许符号）。"""
    return P(f"M {cx-52*s} {cy-60*s} q {-10*s} {-56*s} {36*s} {-62*s} "
             f"q {44*s} {-6*s} {46*s} {32*s} q {2*s} {32*s} {-30*s} {42*s} l 0 {22*s}",
             stroke=color, w=w or 10 * s) + C(cx, cy + 18 * s, 8 * s, color)


def _bulb(cx, cy, s=1.0, ray="#e8a13c"):
    """亮着的灯泡（恍然大悟）。"""
    import math
    rays = ""
    for a in (-150, -115, -80, -65, -25, 0):
        rad = math.radians(a)
        x1 = cx + 48 * s * math.cos(rad)
        y1 = cy + 48 * s * math.sin(rad)
        x2 = cx + 66 * s * math.cos(rad)
        y2 = cy + 66 * s * math.sin(rad)
        rays += L(x1, y1, x2, y2, ray, 7 * s)
    return wrap(rays, C(cx, cy, 40 * s, SUN),
                C(cx - 12 * s, cy - 14 * s, 9 * s, WHITE, 0.75),
                R(cx - 17 * s, cy + 34 * s, 34 * s, 15 * s, 6 * s, GRAY_D))


def _ear_arcs(x, y, s=1.0, color=GRAY_D):
    """飘向耳朵的声波弧。"""
    return wrap(
        P(f"M {x} {y} q {-14*s} {12*s} {-4*s} {28*s}", stroke=color, w=6 * s),
        P(f"M {x-18*s} {y-14*s} q {-24*s} {20*s} {-8*s} {46*s}", stroke=color, w=6 * s),
        P(f"M {x-36*s} {y-26*s} q {-32*s} {26*s} {-12*s} {60*s}", stroke=color, w=6 * s))


def _voice(x, y, s=1.0, color=GRAY_D):
    """嘴边答应的声波弧。"""
    return wrap(
        P(f"M {x} {y} q {16*s} {8*s} {10*s} {28*s}", stroke=color, w=6 * s),
        P(f"M {x+22*s} {y-12*s} q {26*s} {16*s} {14*s} {44*s}", stroke=color, w=6 * s))


def _nod(x, y, s=1.0, color=INK, w=7):
    """头顶两侧的点头弧。"""
    return wrap(
        P(f"M {x-64*s} {y} q {8*s} {-22*s} {34*s} {-16*s}", stroke=color, w=w * s),
        P(f"M {x+64*s} {y} q {-8*s} {-22*s} {-34*s} {-16*s}", stroke=color, w=w * s))


# ---------- 卡片插画 ----------
def a_ne():
    """呢：手放耳边听一听，头顶小问号——在琢磨呢。"""
    g = ground()
    g += _ear_arcs(312, 208, 1.0)
    g += kid(370, 444, s=1.0, face="o", shirt=TEAL, arms="point",
             point_at=(428, 216), look=(1.4, -0.8))
    g += _qmark(490, 158, 0.8, GRAY_D, 8)
    return g


def a_o():
    """哦：恍然大悟，头顶灯泡亮了。"""
    g = ground()
    g += _bulb(380, 104, 1.0)
    g += kid(380, 444, s=0.98, face="o", arms="down", shirt=ORANGE, look=(0, -1))
    return g


def a_la():
    """啦：跳起来欢呼，四周挂彩带。"""
    g = ground()
    g += E(380, 450, 108, 14, SHADOWG)
    ribbons = wrap(
        P("M 178 66 q 26 52 -6 104 q -28 52 6 102", stroke=RED, w=9),
        P("M 252 84 q 22 44 -4 92 q -24 46 4 92", stroke=TEAL, w=8),
        P("M 508 84 q -22 44 4 92 q 24 46 -4 92", stroke=YEL, w=8),
        P("M 582 66 q -26 52 6 104 q 28 52 -6 102", stroke=BLUE, w=9))
    dots = wrap(
        C(160, 300, 8, ROSE), C(600, 292, 8, ORANGE),
        C(208, 130, 7, YEL), C(556, 122, 7, TEAL_L),
        R(140, 210, 16, 10, 4, TEAL), R(606, 202, 16, 10, 4, RED))
    g += ribbons + dots
    g += kid(380, 400, s=0.98, face="open", arms="up", shirt=ROSE)
    return g


def a_wang():
    """往：娃娃沿虚线往前走，正前方一支大红箭头。"""
    g = ground()
    g += _dash(150, 424, 420, 424, TAN, 9, "16 18")
    g += kid(280, 444, s=1.0, pose="walk", face="smile", arms="swing",
             shirt=BLUE, look=(2, 0))
    arrow = wrap(R(450, 306, 178, 42, 15, RED),
                 PG([(626, 272), (712, 327), (626, 382)], RED))
    return g + arrow


def a_gen():
    """跟：大娃娃在前走，小娃娃一前一后跟着。"""
    g = ground()
    g += _dash(150, 438, 640, 438, TAN, 8, "12 18")
    g += kid(500, 444, s=1.05, pose="walk", face="smile", arms="swing",
             shirt=ORANGE, look=(2, 0))
    g += kid(278, 424, s=0.72, pose="walk", face="smile", arms="swing",
             shirt=TEAL, look=(2, 0))
    return g


def a_yue():
    """越：三级台阶，一次跳得比一次高。"""
    g = ground()
    steps = wrap(
        R(110, 378, 150, 66, 10, TAN), R(110, 378, 150, 18, 9, TAN_L),
        R(255, 318, 150, 126, 10, TAN), R(255, 318, 150, 18, 9, TAN_L),
        R(400, 258, 150, 186, 10, TAN), R(400, 258, 150, 18, 9, TAN_L))
    arcs = wrap(
        _dash(180, 348, 300, 296, TEAL_D, 7, "2 16"),
        _dash(325, 292, 470, 226, TEAL_D, 7, "2 16"))
    g += steps + arcs
    g += E(505, 448, 66, 10, SHADOWG)
    g += kid(505, 268, s=0.78, pose="sprint", face="open", arms="pump",
             shirt=GREEN)
    return g


def a_rang():
    """让：把大苹果递给伙伴。"""
    g = ground()
    apple = wrap(
        C(470, 322, 46, RED),
        C(454, 306, 12, WHITE, 0.5),
        L(470, 280, 476, 258, "#5e8f52", 8),
        E(494, 262, 16, 8, GREEN))
    g += apple
    g += kid(240, 444, s=0.95, face="smile", shirt=YEL, arms="point",
             point_at=(428, 330), look=(2, 0))
    g += kid(614, 444, s=0.9, face="open", shirt=TEAL, arms="reach",
             look=(-1.6, 0.2))
    g += C(508, 352, 13, SKIN)
    g += heart(470, 216, 14, RED)
    return g


def a_xie():
    """些：三个球是一小些，一堆球是好多。"""
    g = ground()
    few = ball(200, 410, 27) + ball(262, 410, 27) + ball(324, 410, 27)
    pile = ""
    for cx, cy in ((470, 414), (520, 414), (570, 414), (620, 414),
                   (495, 372), (545, 372), (595, 372),
                   (520, 332), (570, 332), (545, 296)):
        pile += ball(cx, cy, 25)
    return g + few + pile


def a_huo():
    """或：左右两条岔路，站中间选一条。"""
    g = ground()
    roads = wrap(
        P("M 322 468 L 214 254", stroke=TAN, w=54),
        _dash(305, 435, 235, 295, "#b9a98c", 6, "10 14"),
        PG([(197, 220), (243, 240), (186, 268)], TAN),
        P("M 438 468 L 546 254", stroke=TAN, w=54),
        _dash(455, 435, 525, 295, "#b9a98c", 6, "10 14"),
        PG([(563, 220), (574, 268), (517, 240)], TAN))
    g += roads
    g += kid(380, 452, s=0.78, face="o", arms="down", shirt=ORANGE, look=(0, -1))
    g += _qmark(385, 150, 1.0, INK)
    return g


def a_gang():
    """刚：钟刚走到，人刚进家门。"""
    g = ground()
    clock = wrap(
        C(190, 208, 74, GRAY),
        C(184, 202, 70, "#f4ede0"),
        L(184, 142, 184, 158, INK, 6), L(184, 246, 184, 262, INK, 6),
        L(126, 202, 142, 202, INK, 6), L(226, 202, 242, 202, INK, 6),
        L(184, 202, 184, 156, INK, 10),
        L(184, 202, 218, 226, INK, 8),
        C(184, 202, 8, RED))
    door = wrap(
        R(478, 138, 202, 302, 12, WOOD_L),
        R(494, 154, 170, 286, 8, "#7a5c40"),
        E(556, 448, 82, 12, TAN_L))
    bag = wrap(R(498, 296, 46, 64, 12, RED), L(512, 296, 512, 282, RED_D, 8))
    g += clock + door + bag
    g += kid(548, 444, s=0.95, pose="stride", face="smile", arms="swing",
             shirt=BLUE, look=(0.6, 0))
    return g


def a_ge():
    """各：三只彩杯，各归各位。"""
    g = ground()
    mats = wrap(
        E(230, 432, 60, 14, "#eec3ba"),
        E(380, 432, 60, 14, "#f0dfb2"),
        E(530, 432, 60, 14, "#bcd6ea"))
    cups = ""
    for cx, col, col_d in ((230, RED, RED_D), (380, YEL, YEL_D), (530, BLUE, BLUE_D)):
        cups += wrap(
            R(cx - 30, 344, 60, 88, 10, col),
            R(cx - 30, 396, 60, 14, 6, WHITE, 0.55),
            E(cx, 344, 30, 10, col_d))
    return g + mats + cups


def a_ai():
    """爱：张开手臂抱住大爱心。"""
    g = ground()
    g += kid(380, 452, s=1.0, face="open", arms="down", shirt="#f0876f")
    g += heart(380, 322, 88, RED)
    g += C(302, 284, 15, SKIN) + C(458, 284, 15, SKIN)
    g += heart(244, 172, 14, RED) + heart(518, 160, 11, RED)
    return g


def a_ying():
    """应：举手答应，嘴边声波。"""
    g = ground()
    g += kid(360, 444, s=1.0, face="open", shirt=BLUE, arms="point",
             point_at=(474, 158), look=(1.6, -1))
    g += _voice(452, 244, 1.0)
    return g


def a_gai():
    """该：清单上该做的都打了勾。"""
    g = ground()
    board = wrap(
        R(432, 168, 228, 276, 16, WOOD_L),
        R(446, 186, 200, 242, 10, WHITE),
        R(508, 148, 76, 32, 10, GRAY_D))
    rows = ""
    for ry in (238, 306, 374):
        rows += L(470, ry, 556, ry, LGRAY, 9) + check(612, ry, 22, TEAL)
    g += board + rows
    g += kid(252, 444, s=0.92, face="smile", shirt=YEL, arms="point",
             point_at=(452, 300), look=(2, -0.2))
    return g


def a_xing():
    """行：大步向前走，举起手臂竖大拇指说声行。"""
    g = ground()
    g += kid(340, 444, s=1.0, pose="stride", face="open", shirt=GREEN,
             arms="point", point_at=(452, 232), look=(1.6, 0))
    fist = wrap(
        R(430, 206, 44, 42, 12, SKIN),
        R(444, 168, 16, 44, 8, SKIN))
    g += fist
    g += check(574, 258, 52, TEAL)
    return g


def a_neng():
    """能：双手把大皮球高高举过头顶。"""
    g = ground()
    g += kid(380, 452, s=0.92, face="open", arms="up", shirt=ORANGE)
    fore = wrap(
        L(303, 239, 330, 194, SKIN, 26) + C(332, 190, 12, SKIN),
        L(457, 239, 430, 194, SKIN, 26) + C(428, 190, 12, SKIN))
    g += fore
    g += ball(380, 150, 56, TEAL, TEAL_D, TEAL_L)
    return g


def a_yi():
    """已：旗子已经插上山顶，大勾完成。"""
    g = ground()
    mound = E(506, 438, 132, 26, SHADOWG)
    flag = wrap(
        R(494, 172, 14, 262, 6, WOOD_D),
        PG([(508, 178), (642, 214), (508, 252)], RED),
        C(501, 172, 9, "#8a5a33"))
    g += mound + flag
    g += check(300, 300, 62, TEAL)
    return g


def a_dong():
    """懂：点着头，头顶小灯泡亮了。"""
    g = ground()
    g += _bulb(380, 96, 0.82, TEAL_D)
    g += kid(380, 444, s=0.98, face="open", shirt=PURPLE, arms="down",
             look=(0, -0.8))
    g += _nod(380, 152, 1.0)
    return g


def a_en():
    """嗯：闭上眼睛点点头，轻轻应一声。"""
    closed = wrap(
        E(358, 198, 12, 15, SKIN) + E(402, 198, 12, 15, SKIN),
        P("M 344 198 Q 358 186 372 198", stroke=INK, w=6),
        P("M 388 198 Q 402 186 416 198", stroke=INK, w=6))
    g = ground()
    g += kid(380, 444, s=1.0, face="o", shirt=OLIVE, arms="down",
             extra=closed)
    g += _nod(380, 124, 1.0)
    g += _nod(380, 100, 0.62, GRAY_D, 6)
    g += _voice(452, 240, 1.0)
    return g


def arts():
    return {
        "呢": a_ne(), "哦": a_o(), "啦": a_la(), "往": a_wang(),
        "跟": a_gen(), "越": a_yue(), "让": a_rang(), "些": a_xie(),
        "或": a_huo(), "刚": a_gang(), "各": a_ge(), "爱": a_ai(),
        "应": a_ying(), "该": a_gai(), "行": a_xing(), "能": a_neng(),
        "已": a_yi(), "懂": a_dong(), "嗯": a_en(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    lg_spec = importlib.util.spec_from_file_location(
        "lg_changyong", str(ROOT.parent / "识字卡片_素材_changyong.py"))
    lg = importlib.util.module_from_spec(lg_spec)
    lg_spec.loader.exec_module(lg)
    legacy_chars = {c["char"] for c in lg.GROUP_CARDS}
    all_chars = []
    for grp in ziku.GROUPS:
        if grp["id"] == "changyong":
            all_chars = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in all_chars if c not in legacy_chars]
    assert set(all_chars) == legacy_chars | set(expect), "legacy 覆盖与字库对不上"
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"常用字组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}），legacy 已含 {len(legacy_chars)} 字")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对（去掉 legacy 37 字）：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != re.sub(r"（.*?）", "", c["tone"])]
    print(f"拼音/声调：{'与拼音表一致（括注为另读/语境注）✓' if not bad_py else '不一致 ' + str(bad_py)}")
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
