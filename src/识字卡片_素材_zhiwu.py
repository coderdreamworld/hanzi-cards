#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""植物组插画与文案（本组无种子字）。

18 字：花 草 木 叶 树 果 瓜 苗 竹 豆 莲 杏 桃 荷 松 梅 柳 枫
易混卡刻意区分：
- 木/树：木=横放的原木（木身+右端年轮切面+树皮纹）；树=直立的完整大树（冠+干+影）。
- 莲/荷：莲=池塘全景（大圆荷叶+带莲子的莲蓬+小粉花）；荷=单支荷花大特写（花占满中上，深一号粉）。
- 叶/枫：叶=绿色椭圆叶带叶脉；枫=红色掌状五裂叶+金黄叶脉。
- 草/苗：草=一丛细长叶；苗=土堆里两三株双叶嫩芽。
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from 识字卡片_素材库 import (C, E, GREEN, GREEN_L, L, P, PG, R, RED, RED_D, SUN,
                          SUN_L, WBLUE, WHITE, WOOD, WOOD_D, WOOD_L, flower5, ground, wrap)

# 本组同族补充色
LEAF_D = "#5e8a50"      # 深叶绿（GREEN 同族）
LEAF_DD = "#46703c"     # 竹节/暗部绿
LEAF_BB = "#d4e8b0"     # 叶脉浅绿
FRESH = "#8fca6f"       # 嫩芽绿
BAMBOO = "#a9cf72"      # 竹青
PINE_D, PINE_M, PINE_L = "#3e7a4a", "#4c8f56", "#5da364"   # 松三层
PINE_DD = "#2f6238"     # 松针痕
ROSE_L, ROSE, ROSE_D = "#f7b4c6", "#f290a8", "#e06e90"     # 荷/莲花粉
PLUM, PLUM_D = "#f286a8", "#e06a90"                         # 梅花粉
APRI, APRI_D = "#f0913c", "#d97b28"                         # 杏橙
PEACH_D = "#e88a70"     # 桃凹槽/暗部（PINK 同族深）
MELON, MELON_D = "#67a95c", "#3f7f3f"                       # 瓜皮绿
MELON_VD = "#4f8a44"    # 瓜底影
SHADOW = "#aed4c2"      # 树影（GROUND 同族深）
BRANCH = "#6b4a33"      # 梅枝棕（WOOD 同族深）
STEM_BROWN = "#8a5a33"  # 果柄棕
YEL_GOLD = SUN          # 枫叶金黄叶脉


GROUP_CARDS = [
    {"char": "花", "pinyin": "huā", "tone": "第一声",
     "sentence": "花开了，真好看。",
     "say": "圆圆花瓣、黄色花心，这就是花。",
     "chat": "“你在哪里见过和它一样的花？”",
     "life": "去楼下找一朵花，轻轻闻一闻。"},
    {"char": "草", "pinyin": "cǎo", "tone": "第三声",
     "sentence": "小草从土里钻出来。",
     "say": "一丛细细长长的是小草。",
     "chat": "“轻轻摸摸小草，什么感觉？”",
     "life": "蹲下来摸一摸身边的小草。"},
    {"char": "木", "pinyin": "mù", "tone": "第四声",
     "sentence": "木，就是一棵小树。",
     "say": "你看，木字就像一棵小树：下面是根，上面是枝和叶。",
     "chat": "“木字像不像一棵小树呀？”",
     "life": "看到大树，想一想木字的样子。"},
    {"char": "叶", "pinyin": "yè", "tone": "第四声",
     "sentence": "树叶随风飘呀飘。",
     "say": "一片大叶子，中间是细细的叶脉。",
     "chat": "“叶子是什么颜色的？”",
     "life": "捡一片叶子，和手掌比大小。"},
    {"char": "树", "pinyin": "shù", "tone": "第四声",
     "sentence": "大树高又壮。",
     "say": "上面绿绿的树冠，下面粗粗的树干。",
     "chat": "“夏天站在大树下是什么感觉？”",
     "life": "去小区里找一棵最大的树。"},
    {"char": "果", "pinyin": "guǒ", "tone": "第三声",
     "sentence": "树上结满红苹果。",
     "say": "树上红红的就是果子。",
     "chat": "“你最爱吃哪种水果？”",
     "life": "吃苹果前先闻一闻香味。"},
    {"char": "瓜", "pinyin": "guā", "tone": "第一声",
     "sentence": "西瓜大大的，甜甜的。",
     "say": "地上带条纹的大瓜是西瓜。",
     "chat": "“西瓜里面是什么颜色？”",
     "life": "抱抱大西瓜，掂掂重不重。"},
    {"char": "苗", "pinyin": "miáo", "tone": "第二声",
     "sentence": "小苗慢慢长高高。",
     "say": "刚从土里冒头的嫩芽叫小苗。",
     "chat": "“小苗长大能变成什么？”",
     "life": "泡一颗绿豆，看它发小芽。"},
    {"char": "竹", "pinyin": "zhú", "tone": "第二声",
     "sentence": "竹子一节又一节。",
     "say": "青竹有节，叶子细细尖尖。",
     "chat": "“谁最爱抱着竹子啃呀？”",
     "life": "数一数竹竿上有几道节。"},
    {"char": "豆", "pinyin": "dòu", "tone": "第四声",
     "sentence": "豆荚里睡着豆宝宝。",
     "say": "豆荚裂开，里面藏着圆豆子。",
     "chat": "“豆子是什么形状的？”",
     "life": "剥一颗毛豆，数数有几粒。"},
    {"char": "莲", "pinyin": "lián", "tone": "第二声",
     "sentence": "池塘里有大荷叶和莲蓬。",
     "say": "圆圆的大荷叶，还有结莲子的莲蓬，都是莲。",
     "chat": "“莲蓬里藏着什么呀？是一粒粒莲子。”",
     "life": "去公园池塘找一找莲蓬和荷叶。"},
    {"char": "杏", "pinyin": "xìng", "tone": "第四声",
     "sentence": "杏子黄黄的真好吃。",
     "say": "黄黄的杏子长在树枝上，切开来里面藏着杏核。",
     "chat": "“杏子里面的核，像什么呀？”",
     "life": "吃到杏子时，看看里面的杏核。"},
    {"char": "桃", "pinyin": "táo", "tone": "第二声",
     "sentence": "桃子甜甜的，我爱吃。",
     "say": "粉桃子上有条小沟，顶上尖尖。",
     "chat": "“桃子摸上去毛不毛？”",
     "life": "洗个桃子分给家人吃。"},
    {"char": "荷", "pinyin": "hé", "tone": "第二声（另读 hè，负荷）",
     "sentence": "荷花开了，粉粉的。",
     "say": "一支大荷花，花瓣尖尖向上。",
     "chat": "“荷花长在水里还是土里？”",
     "life": "张开小手学花瓣，做朵荷花。"},
    {"char": "松", "pinyin": "sōng", "tone": "第一声",
     "sentence": "松树叶子像细针。",
     "say": "松树一层层，像绿色宝塔。",
     "chat": "“松树的叶子和别的树一样吗？”",
     "life": "捡一根松针，小心摸一摸。"},
    {"char": "梅", "pinyin": "méi", "tone": "第二声",
     "sentence": "梅花冬天悄悄开。",
     "say": "光枝子上开出粉色小梅花。",
     "chat": "“梅花在哪个季节开？”",
     "life": "用手指蘸粉色点几朵梅花。"},
    {"char": "柳", "pinyin": "liǔ", "tone": "第三声",
     "sentence": "柳条随风摆呀摆。",
     "say": "柳树枝条细细长长往下垂。",
     "chat": "“柳条像不像长头发？”",
     "life": "手臂垂下来，学柳条摇一摇。"},
    {"char": "枫", "pinyin": "fēng", "tone": "第一声",
     "sentence": "枫叶红了，秋天到了。",
     "say": "红枫叶像张开的小手掌。",
     "chat": "“数数枫叶有几个尖角？”",
     "life": "把手掌按在纸上画枫叶。"},
]


# ---------- 本地组件 ----------
def place(inner, x, y, rot=0, s=1.0):
    """把以原点为基准的图形平移/旋转/缩放到 (x,y)。"""
    t = f"translate({x},{y})"
    if rot:
        t += f" rotate({rot})"
    if s != 1.0:
        t += f" scale({s})"
    return f'<g transform="{t}">{inner}</g>'


def leaf(ln, wd, fill):
    """尖头椭圆叶：原点在叶柄，叶尖指向 +x 方向。"""
    return P(f"M 0 0 Q {ln * 0.42} {-wd} {ln} 0 Q {ln * 0.42} {wd} 0 0 Z", fill)


def leaf_veined(ln, wd, fill, vein):
    """带主脉的叶子。"""
    return leaf(ln, wd, fill) + L(10, 0, ln - 12, 0, vein, 3.5)


def lotus_petal(ln, wd, fill):
    """尖头花瓣：原点在花蒂，花瓣指向 -y（向上）。"""
    return P(f"M 0 0 Q {-wd} {-ln * 0.45} 0 {-ln} Q {wd} {-ln * 0.45} 0 0 Z", fill)


def lotus_flower(cx, base_y, s, outer, inner, core="#f2d06a"):
    """荷花/莲花头：外层 7 瓣摊开，内层 5 瓣立起，底有花芯。"""
    g = ""
    for a in (-72, -48, -24, 0, 24, 48, 72):
        g += f'<g transform="translate({cx},{base_y}) rotate({a})">{lotus_petal(105 * s, 34 * s, outer)}</g>'
    for a in (-34, -17, 0, 17, 34):
        g += f'<g transform="translate({cx},{base_y}) rotate({a})">{lotus_petal(76 * s, 26 * s, inner)}</g>'
    return g + E(cx, base_y - 14 * s, 24 * s, 13 * s, core)


def bamboo_stalk(x, top, base, w):
    """青竹竿：竖竿 + 每隔一段一道深色竹节 + 左侧高光条。"""
    g = R(x - w / 2, top, w, base - top, w * 0.45, BAMBOO)
    g += R(x - w / 2, top, w * 0.32, base - top, w * 0.16, WHITE, 0.28)
    ny = base - 58
    while ny > top + 24:
        g += R(x - w / 2 - 2, ny, w + 4, 8, 4, LEAF_DD)
        ny -= 58
    return g


def bamboo_leaf_cluster(x, y, rot0=96):
    """一簇垂下的细竹叶。"""
    out = ""
    for rot in (rot0 - 24, rot0 + 8, rot0 + 34):
        out += place(leaf(72, 13, GREEN), x, y, rot)
    return out


def pod_half(length, depth, fill):
    """半月形豆荚瓣：平边朝上、弧背朝下，原点在平边中点。"""
    h = length / 2
    return P(f"M {-h} 0 Q 0 {depth} {h} 0 Q 0 {depth * 0.3} {-h} 0 Z", fill)


def maple(cx, cy, r, main, dark, vein_col, stem_col):
    """掌状五裂枫叶：每瓣带两枚小尖齿，金黄主脉，下接叶柄。"""
    pts = []
    for i in range(5):
        b = -90 + i * 72
        for off, rr in ((-34, 0.40), (-23, 0.66), (-11, 0.55),
                        (0, 1.0), (11, 0.55), (23, 0.66), (34, 0.40)):
            a = math.radians(b + off)
            pts.append((cx + r * rr * math.cos(a), cy + r * rr * math.sin(a)))
    g = PG([(x + 5, y + 6) for x, y in pts], dark) + PG(pts, main)
    for i in range(5):
        a = math.radians(-90 + i * 72)
        g += L(cx, cy + r * 0.42, cx + r * 0.92 * math.cos(a),
               cy + r * 0.92 * math.sin(a), vein_col, 5)
    return g + L(cx, cy + r * 0.40, cx, cy + r * 1.12, stem_col, 11)


# ---------- 各卡插画 ----------
def art_hua():
    stem = P("M 380 446 Q 386 390 380 330", stroke=LEAF_D, w=13)
    lf1 = place(leaf_veined(88, 30, GREEN, LEAF_BB), 380, 396, -155)
    lf2 = place(leaf_veined(80, 27, GREEN_L, LEAF_BB), 382, 416, -28)
    head = flower5(380, 242, 84, "#f0876f", SUN) + C(380, 242, 20, SUN_L, 0.9)
    return wrap(ground(), stem, lf1, lf2, head)


def art_cao():
    blades = [(-46, -132, 128, LEAF_D), (-30, -112, 168, GREEN), (-14, -96, 196, GREEN_L),
              (2, -84, 205, GREEN), (18, -68, 188, GREEN_L), (34, -52, 158, GREEN),
              (48, -36, 126, LEAF_D), (-40, -150, 92, GREEN_L), (42, -22, 96, LEAF_D)]
    g = ground()
    for dx, rot, ln, col in blades:
        g += place(leaf(ln, 10, col), 380 + dx, 444, rot)
    return g


def art_mu():
    """木：一棵枝干根都看得见的发芽小树——形状正像「木」字（象形呼应）。"""
    g = ground(380, 446, 205, 20)
    g += P("M 356 428 L 364 318 L 396 318 L 404 428 Z", "#a9743f")            # 树干
    g += P("M 372 314 Q 334 282 300 254", stroke="#a9743f", w=15)             # 左枝
    g += P("M 388 314 Q 428 286 460 260", stroke="#a9743f", w=15)             # 右枝
    g += P("M 380 316 L 380 214", stroke="#a9743f", w=15)                     # 中枝
    g += P("M 372 428 Q 356 440 336 448", stroke="#a9743f", w=9)              # 根
    g += P("M 388 428 Q 404 440 424 448", stroke="#a9743f", w=9)
    g += C(294, 238, 40, GREEN) + C(468, 246, 38, GREEN) + C(380, 192, 46, GREEN_L)
    g += C(338, 230, 27, GREEN_L, 0.85) + C(432, 228, 26, GREEN_L, 0.8)
    g += C(294, 238, 16, "#c4debb", 0.8) + C(380, 178, 17, "#c4debb", 0.8)
    return g


def art_ye():
    inner = E(387, 295, 118, 156, LEAF_D) + E(380, 290, 118, 156, GREEN)
    inner += L(380, 138, 380, 442, LEAF_BB, 6)
    for i in range(5):
        y = 180 + i * 50
        inner += L(380, y, 324, y - 32, LEAF_BB, 4) + L(380, y, 436, y - 32, LEAF_BB, 4)
    return ground() + f'<g transform="rotate(-12 380 290)">{inner}</g>' + L(410, 438, 418, 464, LEAF_D, 10)


def art_shu():
    sh = E(380, 448, 152, 17, SHADOW)
    trunk_d = P("M 398 300 L 398 444 L 424 444 L 410 300 Z", WOOD_D)
    trunk = P("M 352 444 L 360 292 Q 362 274 378 268 L 398 268 Q 412 274 414 292 L 422 444 Z", WOOD)
    crown = (C(380, 196, 96, GREEN) + C(296, 244, 68, GREEN) + C(464, 244, 68, GREEN)
             + C(380, 252, 74, GREEN) + C(340, 168, 34, GREEN_L, 0.9) + C(432, 208, 26, GREEN_L, 0.8))
    return wrap(ground(), sh, trunk_d, trunk, crown)


def art_guo():
    sh = E(380, 448, 148, 16, SHADOW)
    trunk = P("M 356 444 L 364 320 Q 366 304 380 300 L 396 300 Q 408 304 410 320 L 418 444 Z", WOOD)
    trunk_d = R(392, 320, 14, 118, 7, WOOD_D)
    crown = (C(380, 220, 88, GREEN) + C(306, 262, 62, GREEN) + C(454, 262, 62, GREEN)
             + C(342, 182, 30, GREEN_L, 0.85))
    apples = ""
    for ax, ay, ar in [(334, 238, 30), (428, 268, 30), (378, 186, 26)]:
        apples += (C(ax + 3, ay + 4, ar, RED_D) + C(ax, ay, ar, RED)
                   + C(ax - ar * 0.32, ay - ar * 0.34, ar * 0.24, WHITE, 0.75)
                   + L(ax, ay - ar, ax, ay - ar - 9, STEM_BROWN, 5))
    return wrap(ground(), sh, trunk_d, trunk, crown, apples)


def art_gua():
    cx, cy, rx, ry = 380, 330, 152, 118
    vine = (P("M 500 375 Q 560 388 602 372 Q 636 360 648 378", stroke=LEAF_D, w=8)
            + place(leaf_veined(54, 17, GREEN, LEAF_BB), 600, 372, -28)
            + P("M 648 378 Q 664 370 666 384 Q 667 394 656 392", stroke=LEAF_D, w=5))
    g = ground() + vine + E(cx + 5, cy + 6, rx, ry, MELON_VD) + E(cx, cy, rx, ry, MELON)
    for k, off in zip((-0.66, -0.33, 0.0, 0.33, 0.66), (10, -10, 10, -10, 10)):
        dx = k * rx
        hh = ry * math.sqrt(1 - k * k) - 12
        g += P(f"M {cx + dx:.0f} {cy - hh:.0f} Q {cx + dx + off:.0f} {cy} {cx + dx:.0f} {cy + hh:.0f}",
               stroke=MELON_D, w=15)
    g += E(cx - 52, cy - 52, 34, 20, WHITE, 0.45)
    g += P("M 380 216 Q 376 196 386 184", stroke=LEAF_D, w=10)
    g += P("M 386 184 Q 402 168 416 178 Q 428 188 416 196 Q 408 200 406 192", stroke=LEAF_D, w=6)
    return g


def art_miao():
    def sprout(x, base, h, s=1.0):
        top = base - h
        st = P(f"M {x} {base} Q {x + 6} {base - h * 0.5} {x} {top}", stroke=LEAF_D, w=10 * s)
        lf_l = place(leaf(66 * s, 24 * s, FRESH), x - 4, top + 6, -142)
        lf_r = place(leaf(66 * s, 24 * s, GREEN_L), x + 4, top + 6, -38)
        return st + lf_l + lf_r

    g = ground()
    g += E(380, 438, 132, 26, "#8a5a38") + E(380, 432, 128, 24, "#a9744a")
    g += sprout(300, 424, 92, 0.85)
    g += sprout(452, 428, 104, 0.9)
    g += sprout(380, 428, 140, 1.15)
    return g


def art_zhu():
    g = ground()
    g += bamboo_stalk(318, 190, 446, 19)
    g += bamboo_stalk(446, 210, 446, 19)
    g += bamboo_stalk(382, 158, 446, 24)
    g += bamboo_leaf_cluster(382, 162, 96)
    g += bamboo_leaf_cluster(318, 196, 118)
    g += bamboo_leaf_cluster(446, 216, 72)
    g += bamboo_leaf_cluster(340, 320, 122)
    g += bamboo_leaf_cluster(430, 350, 68)
    return g


def art_dou():
    body = pod_half(330, 150, LEAF_D) + pod_half(310, 132, "#6a9a5c")
    peas = ""
    for px, py, pr in [(-98, 44, 40), (0, 58, 42), (98, 44, 40)]:
        peas += (C(px + 4, py + 5, pr, "#67955a") + C(px, py, pr, GREEN_L)
                 + C(px - pr * 0.3, py - pr * 0.32, pr * 0.26, WHITE, 0.8))
    g = ground()
    g += f'<g transform="translate(380,342) rotate(-10)">{body}{peas}</g>'
    g += f'<g transform="translate(370,296) rotate(-26) scale(1,-1)">{pod_half(300, 120, "#6a9a5c")}</g>'
    g += L(540, 380, 566, 396, LEAF_D, 8)
    g += place(leaf_veined(64, 20, GREEN, LEAF_BB), 566, 396, 22)
    return g


def art_lian():
    """莲=池塘全景：大圆荷叶为主体 + 突出的莲蓬（莲子可见）+ 一朵小粉花配角。"""
    g = ground()
    g += E(380, 414, 258, 42, WBLUE) + E(380, 410, 238, 33, "#9ed7ef", 0.85)
    # 大圆荷叶（左，主体）：深底 + 绿面 + 放射叶脉 + 缺口
    disk = C(302, 360, 100, LEAF_D) + C(300, 356, 98, GREEN)
    for i in range(9):
        a = math.radians(i * 40 + 12)
        disk += L(300, 356, 300 + 80 * math.cos(a), 356 + 80 * math.sin(a), LEAF_BB, 3.5)
    disk += PG([(300, 356), (388, 312), (398, 334)], "#9ed7ef")
    g += disk
    # 莲蓬：莲座杯身 + 平顶面 + 一粒粒莲子
    g += P("M 470 340 Q 466 384 462 408", stroke=LEAF_D, w=11)
    g += P("M 424 296 Q 428 332 448 338 Q 470 344 492 338 Q 512 332 516 296 Z", LEAF_D)
    g += E(470, 296, 46, 15, "#6a9a5c")
    for sx, sy in [(448, 292), (470, 288), (492, 292), (459, 301), (481, 301)]:
        g += C(sx, sy, 7, "#f2e6c0") + C(sx, sy, 3, "#b89a5a")
    # 配角：右侧一片小小的浮叶（花留给「荷」卡）
    g += L(560, 366, 552, 402, LEAF_D, 8)
    g += E(556, 386, 44, 15, GREEN_L)
    g += P("M 180 428 Q 220 436 260 430", stroke=WHITE, w=5, opacity=0.6)
    g += P("M 560 438 Q 596 444 630 438", stroke=WHITE, w=5, opacity=0.6)
    return g


def art_xing():
    """杏：枝头挂着黄杏子，其中一颗切开露出棕色杏核——一眼认出杏。"""
    g = ground()
    g += P("M 20 152 Q 200 116 380 142 Q 560 168 740 144", stroke="#a9743f", w=15)
    g += place(leaf_veined(76, 26, GREEN, LEAF_BB), 150, 156, -30)
    g += place(leaf_veined(70, 24, GREEN_L, LEAF_BB), 560, 152, 25)
    g += L(280, 160, 272, 216, "#8a5a33", 7)
    g += L(470, 164, 462, 248, "#8a5a33", 7)
    g += L(600, 154, 596, 230, "#8a5a33", 7)
    for cx, cy, r in ((272, 302, 82), (600, 294, 64)):
        g += wrap(
            C(cx + 4, cy + 5, r, "#d98a3a"), C(cx, cy, r, "#f2b04e"),
            E(cx + r * 0.3, cy + r * 0.25, r * 0.62, r * 0.72, "#f0913f", 0.75),
            P(f"M {cx} {cy - r + 6} Q {cx + r * 0.16} {cy} {cx - r * 0.05} {cy + r - 4}",
              stroke="#d98a3a", w=4, opacity=0.6),
            C(cx - r * 0.32, cy - r * 0.36, r * 0.18, WHITE, 0.7),
            L(cx, cy - r, cx + 4, cy - r - 14, "#8a5a33", 6))
    g += wrap(
        C(462, 340, 90, "#f5c95c"),
        C(462, 338, 74, "#f8b45c"),
        C(462, 338, 32, "#8a5a33"),
        C(462, 338, 13, "#6e4322"),
        P("M 438 332 Q 462 318 486 332", stroke="#6e4322", w=4, opacity=0.6),
        P("M 440 346 Q 462 358 484 346", stroke="#6e4322", w=4, opacity=0.6),
        C(452, 328, 8, WHITE, 0.55),
        L(462, 248, 462, 262, "#8a5a33", 7))
    return g


def art_tao():
    bx, by, rx, ry = 380, 330, 106, 98
    top = by - ry
    stem = L(bx, top + 14, bx, top - 14, STEM_BROWN, 9)
    lvs = (place(leaf_veined(78, 27, GREEN, LEAF_BB), bx - 4, top - 12, -150)
           + place(leaf(70, 24, GREEN_L), bx + 8, top - 12, -35))
    g = ground() + stem + lvs
    g += E(bx + 6, by + 6, rx, ry, PEACH_D) + E(bx, by, rx, ry, "#f5a58c")
    g += P(f"M {bx - 15} {top + 20} Q {bx} {top - 26} {bx + 15} {top + 20} "
           f"Q {bx} {top + 6} {bx - 15} {top + 20} Z", "#f5a58c")
    g += P(f"M {bx - 15} {top + 20} Q {bx} {top - 26} {bx + 15} {top + 20}", stroke=PEACH_D, w=6)
    g += P(f"M {bx} {top + 22} Q {bx - 9} {top + 60} {bx - 3} {top + 98}", stroke=PEACH_D, w=8, opacity=0.8)
    g += C(bx - 40, by - 34, 24, WHITE, 0.5)
    return g


def art_he():
    """荷=单支荷花大特写：花占满中上画面，只留细茎和一线水面（与莲的全景区分）。"""
    g = ground()
    g += E(380, 444, 132, 18, WBLUE) + E(380, 441, 112, 13, "#9ed7ef", 0.8)
    # 细花茎
    g += P("M 380 340 Q 394 396 380 446", stroke=LEAF_D, w=18)
    # 特写大荷花（花瓣横跨约一半画面，花顶到 y≈140）
    g += lotus_flower(380, 340, 1.9, ROSE, ROSE_D)
    g += P("M 430 452 Q 465 458 500 452", stroke=WHITE, w=5, opacity=0.6)
    g += P("M 262 450 Q 296 456 330 450", stroke=WHITE, w=5, opacity=0.6)
    return g


def art_song():
    g = ground() + E(380, 448, 150, 16, SHADOW)
    g += R(362, 396, 36, 50, 9, WOOD_D)
    for half, ybot, h, col in [(218, 404, 96, PINE_D), (254, 332, 86, PINE_M), (292, 262, 76, PINE_L)]:
        g += PG([(380 - half, ybot), (380 + half, ybot), (380, ybot - h)], col)
    for tx, ty in [(322, 372), (430, 372), (300, 340), (456, 340), (380, 344),
                   (318, 306), (432, 306), (312, 276), (448, 276),
                   (330, 236), (430, 236), (352, 210), (412, 210)]:
        g += L(tx, ty, tx + 26, ty, PINE_DD, 5)
    return g


def art_mei():
    g = ground()
    g += P("M 196 440 Q 246 382 310 342 Q 386 296 452 262 Q 500 238 548 228", stroke=BRANCH, w=17)
    g += P("M 452 262 Q 492 246 520 196", stroke=BRANCH, w=10)
    g += P("M 310 342 Q 288 300 296 258", stroke=BRANCH, w=9)
    g += P("M 500 246 Q 546 258 566 296", stroke=BRANCH, w=8)
    for bx, by in [(258, 372), (318, 330), (388, 292), (452, 258), (506, 236)]:
        g += flower5(bx, by, 17, PLUM, "#f2c14e")
    for bx, by in [(296, 252), (518, 198), (566, 300)]:
        g += C(bx, by, 9, PLUM_D)
    return g


def art_liu():
    g = ground()
    g += P("M 366 446 Q 374 400 370 340 Q 368 306 378 276", stroke=WOOD, w=26)
    g += L(374, 300, 322, 252, WOOD_D, 13) + L(376, 292, 438, 248, WOOD_D, 13)
    g += E(380, 226, 182, 74, GREEN) + E(380, 206, 148, 56, GREEN_L, 0.85)
    strands = [(216, 262, 396, 24), (254, 278, 428, -20), (292, 288, 442, 26),
               (330, 296, 452, -24), (368, 300, 430, 20), (406, 298, 450, -26),
               (444, 292, 440, 24), (482, 280, 420, -20), (518, 264, 392, 22)]
    for i, (sx, sy, sy1, sway) in enumerate(strands):
        col = GREEN_L if i % 2 else GREEN
        g += P(f"M {sx} {sy} Q {sx + sway} {(sy + sy1) / 2:.0f} {sx + sway * 0.4:.0f} {sy1}",
               stroke=col, w=7)
        mx, my = sx + sway * 0.55, (sy + sy1) / 2
        g += f'<g transform="rotate({sway * 0.8:.0f} {mx:.0f} {my:.0f})">' + E(mx, my, 6, 15, col) + "</g>"
        ex, ey = sx + sway * 0.75, sy1 - 46
        g += f'<g transform="rotate({-sway * 0.6:.0f} {ex:.0f} {ey:.0f})">' + E(ex, ey, 6, 14, col) + "</g>"
    return g


def art_feng():
    g = ground()
    g += maple(380, 278, 138, "#d4552f", "#b53a20", YEL_GOLD, "#a83a22")
    # 配角：右上飘落的小枫叶
    g += place(maple(0, 0, 34, "#e8663c", "#c94a2e", YEL_GOLD, "#a83a22"), 596, 150, 24)
    return g


def arts():
    return {
        "花": art_hua(), "草": art_cao(), "木": art_mu(), "叶": art_ye(),
        "树": art_shu(), "果": art_guo(), "瓜": art_gua(), "苗": art_miao(),
        "竹": art_zhu(), "豆": art_dou(), "莲": art_lian(), "杏": art_xing(),
        "桃": art_tao(), "荷": art_he(), "松": art_song(), "梅": art_mei(),
        "柳": art_liu(), "枫": art_feng(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import 识字卡片_字库 as ZIKU

    GID, SEEDS = "zhiwu", set()
    expect = []
    for g in ZIKU.GROUPS:
        if g["id"] == GID:
            for item in g["chars"]:
                k = item["char"] if isinstance(item, dict) else item
                if k not in SEEDS:
                    expect.append(k)
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"植物组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，种子字 {sorted(SEEDS) or '无'}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad, "自检未通过"
    print("自检通过 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '子', 'pinyin': 'zǐ', 'tone': '第三声', 'sentence': '种子发芽长大了。', 'say': '种子埋在土里，发芽长成小苗苗。', 'chat': '“把种子种下去，会冒出什么呀？”', 'life': '种一颗豆子，天天看它发芽。'},
    {'char': '皮', 'pinyin': 'pí', 'tone': '第二声', 'sentence': '香蕉剥了皮。', 'say': '香蕉外面黄黄的皮，剥开才能吃。', 'chat': '“剥下来的橘子皮放哪里？”', 'life': '吃橘子时自己动手剥剥皮。'},
    {'char': '禾', 'pinyin': 'hé', 'tone': '第二声', 'sentence': '禾苗长出金谷穗。', 'say': '看，一株禾：细长叶，弯弯的金谷穗。', 'chat': '“禾苗长大后会结出什么呀？”', 'life': '吃饭时指指米饭：这是禾结的谷子。'},
    {'char': '芽', 'pinyin': 'yá', 'tone': '第二声', 'sentence': '小芽长出来了。', 'say': '土里冒出两片小叶子，就是嫩芽。', 'chat': '种子发芽先冒出什么呀？', 'life': '种一颗小豆子，天天看它发芽。'},
    {'char': '苹', 'pinyin': 'píng', 'tone': '第二声', 'sentence': '苹果红红真好吃。', 'say': '这个红红的水果叫苹果。', 'chat': '“苹果和梨长得哪里不一样？”', 'life': '洗个苹果，闻一闻再咬一口。'},
]
_arts_mig = {
    '子': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><path d="M 130 252 A 200 200 0 0 0 530 252 Z" fill="#5f8f52"/><path d="M 157 249 A 173 173 0 0 0 503 249 Z" fill="#9cc98a"/><path d="M 180 252 A 150 150 0 0 0 480 252 Z" fill="#d4552f"/><path d="M 189 247 A 141 141 0 0 0 471 247 Z" fill="#e8663c"/><g transform="rotate(46 280 296)"><path d="M 280 282 Q 291.9 299.5 280 310 Q 268.1 299.5 280 282 Z" fill="#4a3226"/></g><ellipse cx="277.9" cy="297.68" rx="2.52" ry="4.2" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(-46 380 296)"><path d="M 380 282 Q 391.9 299.5 380 310 Q 368.1 299.5 380 282 Z" fill="#4a3226"/></g><ellipse cx="377.9" cy="297.68" rx="2.52" ry="4.2" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(0 330 336)"><path d="M 330 322 Q 341.9 339.5 330 350 Q 318.1 339.5 330 322 Z" fill="#4a3226"/></g><ellipse cx="327.9" cy="337.68" rx="2.52" ry="4.2" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(16 296 364)"><path d="M 296 350 Q 307.9 367.5 296 378 Q 284.1 367.5 296 350 Z" fill="#4a3226"/></g><ellipse cx="293.9" cy="365.68" rx="2.52" ry="4.2" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(-16 364 364)"><path d="M 364 350 Q 375.9 367.5 364 378 Q 352.1 367.5 364 350 Z" fill="#4a3226"/></g><ellipse cx="361.9" cy="365.68" rx="2.52" ry="4.2" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(8 614 222)"><path d="M 614 176 Q 653.1 233.5 614 268 Q 574.9 233.5 614 176 Z" fill="#4a3226"/></g><ellipse cx="607.1" cy="227.52" rx="8.28" ry="13.799999999999999" fill="#fdfdfa" opacity="0.35"/><g transform="rotate(-10 640 346)"><path d="M 640 314 Q 667.2 354.0 640 378 Q 612.8 354.0 640 314 Z" fill="#4a3226"/></g><ellipse cx="635.2" cy="349.84" rx="5.76" ry="9.6" fill="#fdfdfa" opacity="0.35"/>',
    '皮': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="380" cy="442" rx="118" ry="15" fill="#b57b44" opacity="0.25"/><path d="M 356 262 Q 348 196 386 158 Q 400 144 414 156 Q 430 172 420 210 Q 404 246 398 286 Q 394 300 380 300 Q 362 298 356 262 Z" fill="#f7f0d8"/><path d="M 382 170 Q 366 212 370 268" fill="none" stroke="#e5d9b8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="402" cy="152" r="8" fill="#b57b44"/><path d="M 360 292 Q 296 318 272 396 Q 266 424 294 428 Q 332 420 356 350 Q 368 316 372 296 Z" fill="#f2b53c"/><path d="M 392 296 Q 456 322 484 398 Q 490 426 462 430 Q 424 422 398 352 Q 388 318 384 298 Z" fill="#d99a2b"/><path d="M 372 298 Q 366 348 372 396 Q 376 418 392 418 Q 404 414 402 392 Q 400 344 396 298 Z" fill="#f2b53c"/><circle cx="286" cy="424" r="7" fill="#b57b44"/><circle cx="468" cy="426" r="7" fill="#b57b44"/>',
    '禾': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="380" cy="444" rx="78" ry="15" fill="#b57b44" opacity="0.5"/><path d="M 380 442 Q 372 330 380 240" fill="none" stroke="#5f8f52" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M 378 400 Q 272 380 220 280" fill="none" stroke="#7fae70" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/><path d="M 379 360 Q 468 340 520 250" fill="none" stroke="#9cc98a" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path d="M 379 420 Q 322 392 282 348" fill="none" stroke="#5f8f52" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><path d="M 380 240 Q 430 150 510 170 Q 570 185 575 255" fill="none" stroke="#d9ae4a" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><g transform="rotate(35 396 216)"><ellipse cx="396" cy="216" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="394.5" cy="214.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(20 419 190)"><ellipse cx="419" cy="190" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="417.5" cy="188.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(6 444 174)"><ellipse cx="444" cy="174" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="442.5" cy="172.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(-8 472 167)"><ellipse cx="472" cy="167" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="470.5" cy="165.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(-15 497 168)"><ellipse cx="497" cy="168" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="495.5" cy="166.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(40 545 187)"><ellipse cx="545" cy="187" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="543.5" cy="185.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(62 562 208)"><ellipse cx="562" cy="208" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="560.5" cy="206.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(78 571 229)"><ellipse cx="571" cy="229" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="569.5" cy="227.5" rx="11" ry="18" fill="#f2b53c"/></g><g transform="rotate(86 574 248)"><ellipse cx="574" cy="248" rx="12" ry="19" fill="#d99a2b"/><ellipse cx="572.5" cy="246.5" rx="11" ry="18" fill="#f2b53c"/></g>',
    '芽': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><path d="M 230 446 Q 240 396 380 392 Q 520 396 530 446 Z" fill="#b57b44"/><path d="M 350 420 Q 344 340 356 300" fill="none" stroke="#7fae70" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/><path d="M 352 302 Q 316 296 300 258 Q 344 258 356 292 Z" fill="#9cc98a"/><path d="M 358 300 Q 396 290 410 254 Q 366 256 354 290 Z" fill="#7fae70"/><path d="M 446 428 Q 442 376 450 348" fill="none" stroke="#7fae70" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/><path d="M 448 350 Q 424 344 414 318 Q 444 320 452 342 Z" fill="#9cc98a"/><path d="M 452 348 Q 478 340 488 316 Q 458 318 450 340 Z" fill="#7fae70"/><path d="M 292 206 Q 303.9 223.5 292 234 Q 280.1 223.5 292 206 Z" fill="#79c2e6"/><path d="M 494 245 Q 503.35 258.75 494 267 Q 484.65 258.75 494 245 Z" fill="#79c2e6"/>',
    '苹': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><circle cx="392" cy="344" r="116" fill="#d4552f"/><circle cx="380" cy="336" r="114" fill="#e8663c"/><ellipse cx="338" cy="298" rx="34" ry="22" fill="#f5a58c" opacity="0.75"/><ellipse cx="380" cy="230" rx="30" ry="12" fill="#d4552f"/><path d="M 380 228 Q 378 198 390 176" fill="none" stroke="#b57b44" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><g transform="translate(412,190) rotate(18)"><path d="M 0 0 Q 38 -26 80 0 Q 38 26 0 0 Z" fill="#7fae70"/><line x1="8" y1="0" x2="68" y2="0" stroke="#d4e8b0" stroke-width="4" stroke-linecap="round"/></g>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
