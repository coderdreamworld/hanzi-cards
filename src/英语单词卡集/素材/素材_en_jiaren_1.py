#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 家庭·人物（jiaren）第 1 段插画（11 卡：family~girl）。

每卡造型要点：family 四口牵手（爸妈在外牵娃，两娃手前相搭+爱心）/ dad 爸爸手搭幼儿肩、娃举手要抱+爱心 /
mum 妈妈牵手幼儿（补一小段牵手线）/ grandpa 白发白胡拄拐杖 / grandma 白发老花坐椅织毛衣（红织片+毛线球）/
brother 兄弟牵手+皮球 / sister 姐妹牵手+小花 / baby 坐姿婴儿+奶瓶 / friend 双人举手击掌+星光 /
boy 男孩抬手打招呼 / girl 红裙女孩举手蹦跳+星光。
大人 s=1.15~1.2、大孩 s=0.85~0.95、幼儿 s=0.6、婴儿 sit s=0.95；老人发色 #d9d0c5。
主色：family 红黄青绿 / dad 蓝 / mum 粉 / grandpa 棕 / grandma 深青 / brother 橙+蓝 /
sister 粉+黄 / baby 浅黄 / friend 青+红 / boy 蓝 / girl 红。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "family", "cn": "家/家人"},
    {"w": "dad", "cn": "爸爸"},
    {"w": "mum", "cn": "妈妈"},
    {"w": "grandpa", "cn": "爷爷"},
    {"w": "grandma", "cn": "奶奶"},
    {"w": "brother", "cn": "哥哥/弟弟"},
    {"w": "sister", "cn": "姐姐/妹妹"},
    {"w": "baby", "cn": "婴儿"},
    {"w": "friend", "cn": "朋友"},
    {"w": "boy", "cn": "男孩"},
    {"w": "girl", "cn": "女孩"},
]

# ---------- 本组同族补充色 ----------
GRAY_HAIR = "#d9d0c5"     # 老人白发（与 kid 内置胡须同色）
ORANGE = "#e8873c"        # 暖橙（红黄同族）
PINK_D = "#d9826c"        # 粉族深（毛线球暗部）
BOTTLE_L = "#cfe6f0"      # 奶瓶瓶身浅蓝（素材库杯沿用色）


# ---------- 1 family 四口之家手牵手 ----------
def art_family():
    g = ground()
    # 爸爸（红）牵女儿，妈妈（黄）牵儿子，两娃另一只手在身前相搭
    g += kid(x=150, y=438, s=1.15, shirt=RED, arms="hold_right")
    g += kid(x=330, y=438, s=0.85, shirt=GREEN, skirt=True, arms="hold_left")
    g += kid(x=430, y=438, s=0.85, shirt=TEAL, arms="hold_right")
    g += kid(x=610, y=438, s=1.15, shirt=YEL, skirt=True, bun=True, arms="down")
    # 儿子右手与妈妈垂下的左手之间补一小段肤色线 = 牵手
    g += L(507, 354, 531, 339, SKIN, 24)
    g += heart(380, 80, 17, RED)
    return g


# ---------- 2 dad 爸爸手搭幼儿肩，娃举手要抱 ----------
def art_dad():
    g = ground()
    g += kid(x=310, y=438, s=1.2, shirt=BLUE, arms="down")
    g += kid(x=530, y=438, s=0.6, shirt=RED, arms="up", look=(-1, -1))
    # 爸爸右手搭在幼儿肩上
    g += L(362.8, 242.4, 518, 336, SKIN, 36) + C(518, 336, 15.6, SKIN)
    g += heart(430, 62, 16, RED)
    return g


# ---------- 3 mum 妈妈牵幼儿 ----------
def art_mum():
    g = ground()
    g += kid(x=330, y=438, s=1.15, shirt=PINK, skirt=True, bun=True, arms="hold_right")
    g += kid(x=500, y=438, s=0.62, shirt=YEL, arms="hold_left", look=(-1, -1))
    # 妈妈垂手与幼儿举手间补一小段肤色线 = 牵手
    g += L(430, 340, 436, 351, SKIN, 16)
    g += flower5(165, 420, 16)
    return g


# ---------- 4 grandpa 白发白胡拄拐杖 ----------
def art_grandpa():
    g = ground()
    # 拐杖（画在 kid 之下，手圆盖住杖身 = 握持）
    g += R(461, 296, 13, 140, 6, "#8a5a33")
    g += C(467, 300, 10, "#8a5a33")
    g += kid(x=380, y=438, s=1.18, shirt=WOOD, mustache=True, hair_color=GRAY_HAIR)
    g += star5(240, 120, 11, SUN) + star5(525, 150, 9, SUN)
    return g


# ---------- 5 grandma 白发坐椅织毛衣 ----------
def art_grandma():
    g = ground()
    # 椅子（靠背+座面+四腿，画在 kid 之下）
    g += R(282, 262, 14, 106, 7, WOOD_D) + R(390, 262, 14, 106, 7, WOOD_D)
    g += R(274, 254, 138, 16, 8, WOOD)
    g += R(285, 368, 120, 18, 9, WOOD)
    g += R(292, 386, 13, 50, 6, WOOD_D) + R(384, 386, 13, 50, 6, WOOD_D)
    g += kid(x=340, y=438, s=0.95, pose="sit", shirt=TEAL_D, bun=True,
             glasses=True, hair_color=GRAY_HAIR)
    # 织毛衣：红织片穿在棒针上 + 毛线球引线
    g += R(384, 340, 42, 50, 8, RED)
    g += L(349, 325, 456, 388, WOOD_L, 6)
    g += L(337, 333, 448, 396, WOOD_L, 6)
    g += ball(478, 400, 22, main=PINK, dark=PINK_D, hi=WHITE)
    g += P("M 466 386 Q 442 376 424 364", stroke=PINK, w=5)
    return g


# ---------- 6 brother 兄弟牵手 + 皮球 ----------
def art_brother():
    g = ground()
    g += kid(x=310, y=438, s=0.95, shirt=ORANGE, arms="hold_right")
    g += kid(x=465, y=438, s=0.62, shirt=BLUE, arms="hold_left")
    g += ball(395, 420, 18, main=RED, dark=RED_D, hi=YEL)
    g += star5(238, 130, 10, SUN)
    return g


# ---------- 7 sister 姐妹牵手 + 小花 ----------
def art_sister():
    g = ground()
    g += kid(x=310, y=438, s=0.95, shirt=PINK, skirt=True, bun=True, arms="hold_right")
    g += kid(x=465, y=438, s=0.62, shirt=YEL, skirt=True, bun=True, arms="hold_left")
    g += flower5(395, 424, 13)
    g += star5(530, 140, 10, SUN)
    return g


# ---------- 8 baby 坐姿婴儿 + 奶瓶 ----------
def art_baby():
    g = ground()
    # 软垫（画在 kid 之下，屁股落在垫上、小腿垂在垫前 = 坐姿）
    g += E(324, 376, 90, 26, "#fad2c2")
    g += E(324, 370, 90, 24, PINK)
    g += kid(x=320, y=438, s=0.95, pose="sit", shirt=SUN_L)
    # 奶瓶（放大）：浅蓝瓶身 + 奶水 + 黄奶嘴
    g += R(446, 366, 52, 74, 13, BOTTLE_L)
    g += R(452, 392, 40, 42, 8, WBLUE, 0.9)
    g += R(460, 350, 32, 18, 7, WBLUE)
    g += C(476, 344, 14, SUN_L)
    g += R(454, 374, 10, 36, 5, WHITE, 0.7)
    g += star5(208, 150, 10, SUN)
    return g


# ---------- 9 friend 两个小伙伴举手击掌 ----------
def art_friend():
    g = ground()
    g += kid(x=310, y=438, s=0.9, shirt=TEAL, arms="up")
    g += kid(x=450, y=438, s=0.9, shirt=RED, arms="up")
    g += star5(380, 180, 12, SUN) + star5(346, 208, 8, SUN) + star5(414, 208, 8, SUN)
    return g


# ---------- 10 boy 男孩抬手打招呼 ----------
def art_boy():
    g = ground()
    g += kid(x=380, y=436, s=1.0, shirt=BLUE, arms="point", point_at=(560, 200))
    g += star5(250, 130, 10, SUN)
    return g


# ---------- 11 girl 红裙女孩举手蹦跳 ----------
def art_girl():
    g = ground()
    g += kid(x=380, y=436, s=1.0, shirt=RED, skirt=True, bun=True, arms="up")
    g += star5(296, 122, 9, SUN) + star5(470, 142, 11, SUN)
    return g


def arts():
    return {
        "family": art_family(),
        "dad": art_dad(),
        "mum": art_mum(),
        "grandpa": art_grandpa(),
        "grandma": art_grandma(),
        "brother": art_brother(),
        "sister": art_sister(),
        "baby": art_baby(),
        "friend": art_friend(),
        "boy": art_boy(),
        "girl": art_girl(),
    }
