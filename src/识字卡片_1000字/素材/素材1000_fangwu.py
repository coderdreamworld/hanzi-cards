#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""房屋建筑组 19 卡插画与文案（1000 字批次 B13）。

字表（字库1000 fangwu 组全组，无 legacy 卡，本文件全覆盖）：
房屋楼梯墙瓦砖柜架层厨帘席棚被厕玻璃塔。

一眼可辨约定（主控硬规则）：
房=尖顶小房（黄墙青尖顶+烟囱冒烟）；屋=圆顶小屋（粉圆顶拱门）；
楼=蓝色高层楼房（多排窗+雨棚门）；梯=楼梯侧视（六级台阶+扶手+台阶上的红球）；
墙=一段砖墙（错缝红砖+墙帽+绿丛）；瓦=坡屋顶铺满鱼鳞瓦（瓦行收进屋面轮廓+檐口一行垂下）；
砖=砖块堆叠（三五码放的橙砖堆）；柜=衣柜开门露衣服（挂衣杆三件衣+层板叠放）；
架=书架摆满（青架三格书+顶上小盆栽）；层=剖面三层楼（切开看三层家具）；
厨=灶台锅铲（抽油烟机压低+灶座坐锅+红柄炒锅+锅铲+蒸汽）；帘=窗帘半开（左帘束起右帘垂落）；
席=草席卷起（左端摊平+右段卷筒+红捆带）；棚=瓜棚藤架（叶棚盖顶+格架+藤蔓+两只吊瓜）；
被=叠好的被子（蓝被两摞+顶上白枕头+缝线波点）；厕=马桶+纸卷（友好卡通，蓝座圈+立式纸架）；
玻=透明玻璃窗（窗后绿植整株透出+两道白反光+星光亮点）；璃=玻璃鱼缸（金鱼水草鹅卵石）；
塔=宝塔（三层飞檐+金顶）。同组相邻卡轮廓+主色错开；760×480，第一笔 ground()，
图上无任何文字数字；圆润友好，配色只用 PALETTE 或同族色。
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
BRICK = "#cf6b44"        # 砖墙红棕
MORTAR = "#f4dfc4"       # 砖缝米白
TILE = "#5f7d94"         # 青瓦蓝灰
TILE_L = "#7b99b0"       # 瓦亮面
TILE_D = "#54708a"       # 瓦阴影
BRICKO = "#e0894a"       # 砖块橙
BRICKO_D = "#c26f36"
STEEL = "#dfe3e6"
STEEL_D = "#c3cad0"
CREAM = "#f9e3c8"        # 内墙奶油
ROOF_R = "#d4552f"       # 宝塔红檐
GLASS = "#cfe9f4"        # 玻璃浅蓝
GLASS_D = "#a8d8ec"


# ---------- 卡片文案 ----------
GROUP_CARDS = [
    {"char": "房", "pinyin": "fáng", "tone": "第二声",
     "sentence": "新房盖好啦。",
     "say": "尖尖屋顶、方方墙，这是一座房。",
     "chat": "“你家的房顶是什么样子的？”",
     "life": "用积木搭一座小房给他看。"},
    {"char": "屋", "pinyin": "wū", "tone": "第一声",
     "sentence": "圆顶小屋真可爱。",
     "say": "圆圆屋顶的小房子，叫小屋。",
     "chat": "“小屋和楼房哪里不一样？”",
     "life": "画画时让他添一个圆屋顶。"},
    {"char": "楼", "pinyin": "lóu", "tone": "第二声",
     "sentence": "高楼一层又一层。",
     "say": "很高很高、有很多窗户的是楼房。",
     "chat": "“你家住在第几层呀？”",
     "life": "在窗边数一数远处的高楼。"},
    {"char": "梯", "pinyin": "tī", "tone": "第一声",
     "sentence": "楼梯一级又一级。",
     "say": "一级一级往上的是楼梯。",
     "chat": "“上下楼梯要靠哪边走？”",
     "life": "扶好扶手，带他走一段楼梯。"},
    {"char": "墙", "pinyin": "qiáng", "tone": "第二声",
     "sentence": "砖块砌成一面墙。",
     "say": "一块块砖叠起来，就是墙。",
     "chat": "“我们家的墙是什么颜色的？”",
     "life": "把手掌轻轻贴在墙上摸一摸。"},
    {"char": "瓦", "pinyin": "wǎ", "tone": "第三声",
     "sentence": "屋顶铺满小青瓦。",
     "say": "屋顶上一片片弯弯的是瓦。",
     "chat": "“下雨时雨水往哪里流呀？”",
     "life": "看屋顶照片，指认一片片瓦。"},
    {"char": "砖", "pinyin": "zhuān", "tone": "第一声",
     "sentence": "方方砖块叠高高。",
     "say": "方方的砖块，用来砌墙盖房。",
     "chat": "“砖块是什么形状的呀？”",
     "life": "用积木当砖，叠一叠。"},
    {"char": "柜", "pinyin": "guì", "tone": "第四声",
     "sentence": "衣服叠好放进柜。",
     "say": "关上门能放衣服的大箱子是柜。",
     "chat": "“你的衣服放在哪个柜里？”",
     "life": "收衣服时让他递衣服进柜。"},
    {"char": "架", "pinyin": "jià", "tone": "第四声",
     "sentence": "书架上摆满了书。",
     "say": "一层层放书放玩具的是架子。",
     "chat": "“书架最高层放着什么呀？”",
     "life": "把绘本一本本插回书架。"},
    {"char": "层", "pinyin": "céng", "tone": "第二声",
     "sentence": "这栋楼有三层。",
     "say": "切开看看，楼房里面一层一层。",
     "chat": "“你家住第几层？数数看。”",
     "life": "坐电梯时报楼层：三层到啦。"},
    {"char": "厨", "pinyin": "chú", "tone": "第二声",
     "sentence": "厨房里炒菜香喷喷。",
     "say": "烧饭炒菜的房间叫厨房。",
     "chat": "“今晚厨房做什么菜呀？”",
     "life": "做饭时让他远远看锅铲翻炒。"},
    {"char": "帘", "pinyin": "lián", "tone": "第二声",
     "sentence": "拉开窗帘晒太阳。",
     "say": "窗户两边挂的布帘叫窗帘。",
     "chat": "“拉上窗帘屋里会怎么样？”",
     "life": "早上让他帮忙拉开窗帘。"},
    {"char": "席", "pinyin": "xí", "tone": "第二声",
     "sentence": "草席卷起来收好。",
     "say": "卷成圆筒的草席，夏天铺着睡。",
     "chat": "“凉席摸上去是什么感觉？”",
     "life": "铺凉席时让他压住一个角。"},
    {"char": "棚", "pinyin": "péng", "tone": "第二声",
     "sentence": "瓜棚下结满大瓜。",
     "say": "架子爬满藤、挂着瓜，是瓜棚。",
     "chat": "“瓜为什么要搭架子呀？”",
     "life": "去菜园找找爬藤的瓜棚。"},
    {"char": "被", "pinyin": "bèi", "tone": "第四声",
     "sentence": "被子叠得方方正正。",
     "say": "睡觉盖的软软的就是被子。",
     "chat": "“你睡觉盖什么颜色的被子？”",
     "life": "起床后一起把被子叠起来。"},
    {"char": "厕", "pinyin": "cè", "tone": "第四声",
     "sentence": "上厕所要冲水。",
     "say": "有马桶和小卷纸的房间是厕所。",
     "chat": "“上完厕所第一件事做什么？”",
     "life": "带他自己按冲水按钮。"},
    {"char": "玻", "pinyin": "bō", "tone": "第一声",
     "sentence": "玻璃窗亮又透明。",
     "say": "窗上亮亮的透明片是玻璃。",
     "chat": "“隔着玻璃能看见外面吗？”",
     "life": "轻轻摸摸玻璃窗，说说感觉。"},
    {"char": "璃", "pinyin": "lí", "tone": "第二声",
     "sentence": "鱼缸是玻璃做的。",
     "say": "透明的玻璃缸，能看见小鱼。",
     "chat": "“玻璃为什么是透明的呀？”",
     "life": "隔着鱼缸玻璃看小鱼游。"},
    {"char": "塔", "pinyin": "tǎ", "tone": "第三声",
     "sentence": "尖尖宝塔高又高。",
     "say": "一层比一层小的尖塔是宝塔。",
     "chat": "“数数宝塔有几层呀？”",
     "life": "用积木叠一座小宝塔。"},
]


# ---------- 插画 ----------
def art_fang():
    """房：黄墙青尖顶小房，烟囱冒烟，圆窗木门。"""
    g = ground()
    # 主体：房身
    g += R(260, 270, 240, 170, 10, SUN_L)
    g += R(260, 424, 240, 16, 8, YEL_D)
    # 尖顶
    g += PG([(232, 278), (528, 278), (380, 150)], TEAL)
    g += PG([(232, 278), (528, 278), (528, 268), (380, 148), (232, 268)], TEAL_D)
    # 烟囱 + 烟
    g += R(430, 150, 32, 65, 6, WOOD_D)
    g += R(430, 150, 32, 12, 6, RED)
    g += C(462, 122, 14, WHITE, 0.9)
    g += C(486, 100, 10, WHITE, 0.75)
    # 圆窗
    g += C(300, 330, 27, WOOD)
    g += C(300, 330, 21, SUN)
    g += L(279, 330, 321, 330, WOOD_D, 5)
    g += L(300, 309, 300, 351, WOOD_D, 5)
    # 门 + 台阶
    g += R(344, 356, 72, 84, 10, WOOD_D)
    g += C(404, 400, 5, SUN)
    g += R(336, 438, 88, 12, 6, WOOD)
    # 门口小丛绿
    g += C(232, 428, 20, GREEN)
    g += C(212, 436, 14, GREEN_L)
    return g


def art_wu():
    """屋：粉色圆顶小屋，拱形门，圆天窗。"""
    g = ground()
    # 圆顶
    g += P("M 250 300 A 130 118 0 0 1 510 300 Z", PINK)
    g += P("M 300 300 A 80 74 0 0 1 460 300", stroke="#f9c5b4", w=14)
    # 顶上小圆烟囱
    g += R(288, 170, 26, 48, 8, TEAL_D)
    g += R(288, 170, 26, 12, 6, TEAL_L)
    # 屋身
    g += R(266, 300, 228, 140, 16, WOOD_L)
    g += R(266, 420, 228, 20, 10, WOOD)
    # 拱门
    g += P("M 348 440 L 348 372 A 32 32 0 0 1 412 372 L 412 440 Z", WOOD_D)
    g += C(400, 408, 5, SUN)
    # 圆天窗
    g += C(380, 252, 23, WHITE)
    g += C(380, 252, 17, SUN)
    g += L(363, 252, 397, 252, WOOD_D, 5)
    g += L(380, 235, 380, 269, WOOD_D, 5)
    # 旁边小圆石
    g += E(516, 436, 18, 10, "#d9d0c5")
    return g


def art_lou():
    """楼：蓝色高层楼房，三排窗+雨棚门。"""
    g = ground()
    g += R(276, 162, 208, 278, 10, BLUE)
    g += R(276, 162, 208, 18, 9, BLUE_D)
    # 窗 3 列 3 排
    for row, y in enumerate((192, 248, 304)):
        for x in (296, 358, 420):
            g += R(x, y, 44, 36, 5, SUN_L)
            g += R(x + 5, y + 5, 34, 26, 4, SUN)
    # 雨棚 + 门
    g += R(336, 382, 88, 14, 7, SUN)
    g += R(350, 396, 60, 44, 8, TEAL_D)
    # 楼顶小天线
    g += L(380, 162, 380, 132, BLUE_D, 6)
    g += C(380, 126, 7, RED)
    return g


def art_ti():
    """梯：楼梯侧视，六级木台阶+扶手，台阶上一颗红球。"""
    g = ground(380, 446, 260, 24)
    # 楼梯整体（侧视剪影）
    g += PG([(140, 440), (140, 410), (202, 410), (202, 380), (264, 380), (264, 350),
             (326, 350), (326, 320), (388, 320), (388, 290), (450, 290), (450, 260),
             (512, 260), (512, 440)], WOOD_L)
    # 每级踏面
    for x, y in ((140, 410), (202, 380), (264, 350), (326, 320), (388, 290), (450, 260)):
        g += R(x, y, 62, 8, 3, WOOD)
    # 扶手立柱 + 扶手
    g += L(171, 410, 171, 352, WOOD_D, 12)
    g += L(295, 350, 295, 292, WOOD_D, 12)
    g += L(419, 290, 419, 232, WOOD_D, 12)
    g += L(140, 363, 512, 183, WOOD_D, 13)
    # 台阶上的红球
    g += ball(262, 364, 16, RED, RED_D, "#f5a58c")
    return g


def art_qiang():
    """墙：一段错缝砖墙，墙帽+旁边绿丛。"""
    g = ground()
    # 墙体
    g += R(180, 252, 400, 188, 10, BRICK)
    # 砖缝：横缝
    for y in (289, 326, 363, 400):
        g += L(184, y, 576, y, MORTAR, 7)
    # 砖缝：竖缝（逐行错开）
    for i in range(5):
        y0 = 252 + 37 * i
        off = 33 if i % 2 == 0 else 0
        for k in range(1, 6):
            x = 180 + 66 * k + off
            if x < 574:
                g += L(x, y0 + 4, x, y0 + 33, MORTAR, 7)
    # 墙帽
    g += R(170, 240, 420, 18, 9, "#e8ded0")
    # 墙边绿丛
    g += C(560, 428, 26, GREEN)
    g += C(590, 436, 18, GREEN_L)
    return g


def art_wa():
    """瓦：坡屋顶侧面铺满鱼鳞瓦——瓦行全部收进屋面轮廓，檐口一行自然垂下。"""
    g = ground(380, 446, 300, 20)
    # 屋面（梯形轮廓，孩子一眼读出"屋顶"）
    g += PG([(230, 190), (530, 190), (610, 430), (150, 430)], TILE_D)
    # 鱼鳞瓦行：逐行算出左右边界，瓦片只画在屋面内，行行错缝
    top_w, bot_w, y0, y1 = 300.0, 460.0, 190.0, 430.0

    def edges(y):
        t = (y - y0) / (y1 - y0)
        return 230 - 80 * t, 530 + 80 * t

    rows = ((244, TILE), (306, TILE_L), (368, TILE), (430, TILE_L))
    W, H, OFF = 72, 34, 36
    for yb, col in rows:
        xl, xr = edges(yb)
        x = xl + OFF if ((yb - 244) // 62) % 2 == 0 else xl
        while x + W <= xr + 1:
            g += P(f"M {x:.0f} {yb} A {W / 2:.0f} {H} 0 0 0 {x + W:.0f} {yb} Z", col)
            x += W
    # 檐口滴水线 + 屋脊
    g += R(150, 424, 460, 10, 5, TILE_D)
    g += R(206, 172, 348, 20, 10, TILE_D)
    g += R(214, 168, 332, 8, 4, TILE_L)
    return g


def art_zhuan():
    """砖：橙砖码成小堆+侧靠一块。"""
    g = ground()

    def brick(x, y, w=120, h=44):
        return wrap(
            R(x, y, w, h, 8, BRICKO),
            R(x, y + h - 10, w, 10, 5, BRICKO_D),
            R(x + 8, y + 6, w * 0.4, 8, 4, "#f0a868", 0.8))

    # 3-2-1 码放
    g += brick(212, 396) + brick(338, 396) + brick(464, 396)
    g += brick(275, 348) + brick(401, 348)
    g += brick(338, 300)
    # 侧面斜靠一块
    g += f'<g transform="translate(566,414) rotate(20)">{brick(-60, -22)}</g>'
    return g


def art_gui():
    """柜：衣柜右门敞开，挂衣杆三件衣+层板叠放。"""
    g = ground()
    # 柜体
    g += R(250, 208, 260, 224, 12, WOOD)
    g += R(238, 194, 284, 20, 9, WOOD_D)
    g += R(262, 430, 26, 16, 6, WOOD_D)
    g += R(472, 430, 26, 16, 6, WOOD_D)
    # 左门（关）
    g += R(262, 220, 116, 200, 8, WOOD_L)
    g += R(272, 232, 96, 176, 8, WOOD, 0.35)
    g += C(368, 320, 6, WOOD_D)
    # 右门内（开）
    g += R(390, 220, 110, 200, 8, "#8a5a33")
    g += L(396, 258, 494, 258, WOOD_L, 6)
    for x, col in ((400, TEAL), (434, RED), (468, SUN)):
        g += C(x + 14, 266, 4, INK)
        g += R(x, 268, 28, 52, 6, col)
    g += R(396, 342, 98, 12, 4, WOOD_L)
    g += R(402, 320, 36, 20, 5, SUN)
    g += R(442, 322, 32, 18, 5, TEAL_L)
    # 敞开的右门板（侧视）
    g += R(502, 222, 22, 196, 8, WOOD_L)
    g += C(511, 320, 4, WOOD_D)
    return g


def art_jia():
    """架：青色书架三格摆满书，顶上一盆小绿植。"""
    g = ground()
    # 框架
    g += R(230, 196, 300, 244, 12, TEAL)
    g += R(246, 212, 268, 212, 6, "#3e9486")
    g += R(246, 272, 268, 12, 4, TEAL)
    g += R(246, 332, 268, 12, 4, TEAL)
    # 第一格：竖排书
    books1 = ((254, 52, 18, RED), (274, 46, 16, SUN), (292, 54, 20, BLUE),
              (314, 44, 16, PINK), (332, 50, 18, WHITE), (352, 46, 16, GREEN_L),
              (370, 52, 18, YEL))
    for x, h, w, col in books1:
        g += R(x, 272 - h, w, h, 3, col)
    # 斜靠一本
    g += f'<g transform="rotate(-14 404 268)">{R(396, 218, 18, 50, 3, RED_D)}</g>'
    # 第二格：矮书 + 小球
    for x, h, w, col in ((254, 38, 18, BLUE_D), (274, 34, 16, WHITE), (292, 40, 18, GREEN),
                         (312, 34, 16, SUN), (330, 38, 18, PINK)):
        g += R(x, 332 - h, w, h, 3, col)
    g += ball(392, 314, 15, RED, RED_D, "#f5a58c")
    # 第三格：横叠书 + 玩具块
    g += R(254, 404, 80, 14, 4, RED)
    g += R(258, 390, 72, 14, 4, BLUE)
    g += R(256, 376, 76, 14, 4, YEL)
    g += R(356, 388, 36, 30, 6, TEAL_L)
    g += C(374, 380, 9, SUN)
    # 顶上盆栽
    g += R(352, 170, 36, 26, 6, "#d9734f")
    g += C(370, 156, 14, GREEN)
    g += C(354, 164, 10, GREEN_L)
    g += C(386, 164, 10, GREEN_L)
    return g


def art_ceng():
    """层：剖面三层楼，切开看见每层的床、桌、沙发。"""
    g = ground()
    # 屋顶
    g += PG([(226, 204), (534, 204), (380, 118)], ROOF_R)
    # 外壳与内部
    g += R(240, 200, 280, 240, 12, "#f0a48a")
    g += R(254, 214, 252, 226, 8, CREAM)
    # 楼板两道 → 三个房间
    g += R(254, 290, 252, 14, 4, WOOD_D)
    g += R(254, 366, 252, 14, 4, WOOD_D)
    # 顶屋：小床
    g += R(268, 262, 70, 26, 6, BLUE)
    g += R(272, 256, 18, 14, 4, WHITE)
    g += R(356, 270, 14, 18, 4, WOOD_D)
    # 中层：小桌+花瓶
    g += R(298, 344, 68, 8, 3, WOOD_D)
    g += R(304, 352, 8, 14, 3, WOOD_D)
    g += R(352, 352, 8, 14, 3, WOOD_D)
    g += R(338, 326, 14, 18, 4, TEAL)
    g += C(345, 320, 7, PINK)
    # 底层：沙发+电视
    g += R(278, 404, 90, 34, 8, GREEN_L)
    g += R(278, 392, 90, 16, 8, GREEN_L)
    g += R(418, 394, 62, 40, 6, "#5a6b7a")
    g += R(424, 400, 50, 28, 4, TEAL_L)
    return g


def art_chu():
    """厨：抽油烟机压低+灶台坐锅——锅坐在灶上不沉进台面，锅铲斜靠。"""
    g = ground(380, 446, 260, 22)
    # 抽油烟机（加大、压低，贴近锅）
    g += R(356, 168, 48, 30, 6, TEAL_D)
    g += P("M 286 198 L 474 198 L 442 252 L 318 252 Z", TEAL)
    g += R(314, 246, 132, 10, 4, TEAL_D)
    # 蒸汽（从锅沿升到烟机）
    g += P("M 336 296 Q 326 276 338 260", stroke="#c9cdd1", w=8)
    g += P("M 366 296 Q 376 276 364 260", stroke="#c9cdd1", w=7)
    # 灶台柜 + 台面
    g += R(230, 348, 300, 86, 12, STEEL)
    g += L(380, 356, 380, 426, STEEL_D, 4)
    g += R(338, 396, 28, 8, 4, "#aab4bc")
    g += R(394, 396, 28, 8, 4, "#aab4bc")
    g += R(222, 330, 316, 18, 9, WOOD_L)
    # 灶座（锅坐在上面）
    g += R(296, 306, 88, 26, 6, "#6b7680")
    # 炒锅（坐姿：沿在灶座上沿）
    g += P("M 270 310 A 61 30 0 0 0 392 310 Z", "#5a646e")
    g += L(268, 310, 392, 310, "#8a939c", 6)
    g += C(262, 310, 8, RED_D)
    g += C(398, 310, 8, RED_D)
    # 锅铲
    g += L(352, 302, 420, 248, "#b57b44", 10)
    g += f'<g transform="rotate(48 428 242)">{E(428, 242, 13, 19, STEEL_D)}</g>'
    return g


def art_lian():
    """帘：窗帘半开，左帘束起、右帘垂落，窗里小云。"""
    g = ground(380, 446, 250, 22)
    # 窗框与玻璃
    g += R(250, 190, 260, 220, 10, WOOD_D)
    g += R(262, 202, 236, 196, 8, GLASS)
    g += cloud_p(320, 254, 0.45, WHITE)
    g += C(444, 244, 18, SUN_L, 0.95)
    # 窗台
    g += R(238, 404, 284, 18, 9, WOOD_L)
    # 窗帘杆
    g += R(226, 172, 308, 12, 6, WOOD_D)
    g += C(222, 178, 9, WOOD_D)
    g += C(538, 178, 9, WOOD_D)
    # 左帘（束起）
    g += P("M 252 184 L 322 184 Q 316 250 306 300 Q 322 350 314 404 L 258 404 "
           "Q 246 340 258 292 Q 248 236 252 184 Z", RED)
    g += R(250, 320, 64, 14, 7, YEL_D)
    g += P("M 282 192 Q 278 250 284 300", stroke="#c4532e", w=4)
    # 右帘（半开垂落）
    g += P("M 438 184 L 508 184 Q 512 240 504 300 Q 512 350 506 404 L 444 404 "
           "Q 438 300 438 184 Z", RED_D)
    g += P("M 470 192 Q 474 260 468 340", stroke="#b04a28", w=4)
    return g


def art_xi():
    """席：草席卷起，左端摊平，卷筒带红捆带。"""
    g = ground(380, 446, 260, 22)
    # 摊平的一端
    g += PG([(84, 378), (218, 376), (222, 432), (76, 432)], "#f2c14e")
    g += L(96, 392, 212, 390, "#d9a53c", 4)
    g += L(92, 410, 214, 408, "#d9a53c", 4)
    g += L(88, 424, 216, 422, "#d9a53c", 4)
    # 卷筒
    g += '<g transform="translate(370,404) rotate(-6)">'
    g += R(-150, -52, 300, 104, 48, "#f2c14e")
    for dy in (-26, 0, 26):
        g += L(-140, dy, 130, dy, "#d9a53c", 5)
    # 右端卷芯
    g += E(150, 0, 32, 52, "#e0ac38")
    g += E(150, 0, 22, 36, "#f2c14e")
    g += E(150, 0, 12, 20, "#e0ac38")
    g += C(150, 0, 5, "#c89028")
    g += "</g>"
    # 红捆带
    g += '<g transform="translate(370,404) rotate(-6)">' + R(-24, -56, 30, 112, 10, RED) + "</g>"
    return g


def art_peng():
    """棚：瓜棚藤架，格架爬藤，两只吊瓜。"""
    g = ground(380, 446, 260, 22)
    # 立柱与横梁
    g += L(240, 438, 240, 240, WOOD_D, 14)
    g += L(520, 438, 520, 240, WOOD_D, 14)
    g += R(220, 228, 320, 14, 7, WOOD_D)
    g += R(220, 282, 320, 12, 6, WOOD)
    # 顶格架（斜撑）
    for x in (252, 332, 412, 492):
        g += L(x, 294, x + 70, 242, WOOD_D, 5)
        g += L(x + 70, 294, x, 242, WOOD_D, 5)
    # 顶上叶棚（盖满横梁，一眼读出"棚"）
    leaf = ((232, 222, 30, 13, GREEN), (284, 216, 34, 14, GREEN_L), (336, 222, 32, 13, GREEN),
            (390, 214, 34, 14, GREEN_L), (444, 222, 32, 13, GREEN), (498, 216, 34, 14, GREEN_L),
            (548, 224, 28, 12, GREEN), (258, 238, 28, 12, GREEN_L), (312, 240, 30, 12, GREEN),
            (366, 238, 28, 12, GREEN_L), (420, 240, 30, 12, GREEN), (474, 238, 28, 12, GREEN_L),
            (524, 240, 26, 11, GREEN))
    for cx, cy, rx, ry, col in leaf:
        g += E(cx, cy, rx, ry, col)
    # 藤蔓
    g += P("M 240 436 Q 220 380 246 330 Q 260 300 244 262", stroke=GREEN, w=8)
    g += P("M 244 262 Q 262 250 258 234", stroke=GREEN, w=6)
    g += P("M 520 436 Q 540 384 514 336 Q 500 306 516 266", stroke=GREEN, w=8)
    g += E(268, 300, 15, 9, GREEN_L)
    g += E(226, 352, 15, 9, GREEN_L)
    g += E(536, 320, 15, 9, GREEN_L)
    g += E(500, 372, 14, 8, GREEN_L)

    def melon(cx, cy, rx, ry):
        return wrap(
            E(cx, cy, rx, ry, "#6aa85e"),
            P(f"M {cx - rx * 0.45} {cy - ry * 0.8} Q {cx - rx * 0.75} {cy} {cx - rx * 0.45} {cy + ry * 0.8}",
              stroke="#4c7f44", w=5),
            P(f"M {cx + rx * 0.1} {cy - ry * 0.95} Q {cx - rx * 0.15} {cy} {cx + rx * 0.1} {cy + ry * 0.95}",
              stroke="#4c7f44", w=5),
            P(f"M {cx + rx * 0.55} {cy - ry * 0.7} Q {cx + rx * 0.4} {cy} {cx + rx * 0.55} {cy + ry * 0.7}",
              stroke="#4c7f44", w=5))

    # 吊瓜
    g += L(300, 242, 300, 300, "#5a8a4e", 6)
    g += L(440, 242, 440, 318, "#5a8a4e", 6)
    g += melon(300, 334, 44, 34)
    g += melon(440, 350, 40, 30)
    return g


def art_bei():
    """被：蓝色被子两摞，缝线与波点。"""
    g = ground(380, 446, 220, 22)
    # 下层大被
    g += R(240, 330, 280, 110, 26, GLASS_D)
    g += L(250, 385, 510, 385, "#5aa9cf", 5)
    g += R(240, 424, 280, 16, 8, "#5aa9cf")
    # 上层小被（带翻口+竖向折缝）
    g += R(270, 252, 220, 84, 22, TEAL)
    g += R(270, 310, 220, 26, 13, "#a8d8ec")
    g += L(352, 262, 352, 304, "#3e9486", 4)
    g += L(408, 262, 408, 304, "#3e9486", 4)
    # 顶上白枕头（点出"睡的被褥"而不是沙发）
    g += f'<g transform="rotate(-6 380 234)">{R(312, 212, 136, 44, 20, WHITE)}</g>'
    g += f'<g transform="rotate(-6 380 234)">{R(330, 222, 100, 12, 6, "#e8e4dc", 0.8)}</g>'
    # 缝线（虚线）
    g += '<line x1="286" y1="270" x2="474" y2="270" stroke="#3e9486" stroke-width="4" stroke-dasharray="10 8"/>'
    g += '<line x1="262" y1="352" x2="498" y2="352" stroke="#7cc8bb" stroke-width="4" stroke-dasharray="10 8"/>'
    # 下层被竖折缝
    g += L(320, 396, 320, 420, "#5aa9cf", 4)
    g += L(440, 396, 440, 420, "#5aa9cf", 4)
    return g


def art_ce():
    """厕：友好卡通马桶+立式纸架。"""
    g = ground()
    # 马桶水箱
    g += R(300, 254, 112, 84, 12, "#eef2f4")
    g += R(336, 264, 40, 12, 6, "#c3cdd3")
    # 座圈与桶口
    g += E(356, 338, 58, 17, "#79c2e6")
    g += E(356, 338, 34, 10, "#eef2f4")
    g += E(356, 340, 26, 7, "#a9bdc5")
    # 桶身与底座
    g += P("M 306 344 Q 302 400 356 404 Q 410 400 406 344 Z", "#eef2f4")
    g += R(336, 404, 40, 36, 8, "#e2e8ea")
    # 前面小地垫
    g += E(380, 452, 74, 11, GLASS_D, 0.85)
    # 立式纸架
    g += E(211, 438, 26, 8, "#aab4bc")
    g += R(206, 344, 10, 96, 5, "#aab4bc")
    g += L(211, 352, 238, 352, "#aab4bc", 10)
    g += C(240, 322, 30, "#f6f1e6")
    g += C(240, 322, 9, "#c9bfae")
    g += P("M 226 336 Q 222 392 228 428 L 252 428 Q 258 390 254 336 Z", "#f6f1e6")
    return g


def art_bo():
    """玻：透明玻璃窗——窗后绿植整株透出来+两道白反光+星光亮点，一眼读出"透明"。"""
    g = ground(380, 446, 230, 22)
    # 白窗框 + 玻璃底色
    g += R(240, 180, 280, 250, 12, WHITE)
    g += R(254, 194, 252, 222, 8, GLASS)
    # 窗后绿植（实色，隔着玻璃也能看清）
    g += P("M 316 364 L 368 364 L 359 406 L 325 406 Z", "#d9734f")
    g += R(312, 358, 60, 12, 5, "#c05f3e")
    g += C(342, 314, 28, GREEN)
    g += C(312, 336, 20, GREEN_L)
    g += C(372, 334, 20, GREEN_L)
    g += C(342, 350, 18, GREEN)
    # 玻璃罩层（压在绿植上，透出"隔着一层"的感觉）
    g += R(254, 194, 252, 222, 8, GLASS, 0.42)
    # 斜向反光
    g += P("M 288 416 L 452 194 L 486 194 L 322 416 Z", WHITE, 0.5)
    g += P("M 396 416 L 500 272 L 506 296 L 414 416 Z", WHITE, 0.32)
    # 星光亮点（玻璃才有的闪光）
    g += L(288, 230, 306, 230, WHITE, 5)
    g += L(297, 221, 297, 239, WHITE, 5)
    g += C(484, 250, 5, WHITE, 0.95)
    g += C(474, 262, 3, WHITE, 0.9)
    # 窗台与把手
    g += R(228, 424, 304, 18, 9, WHITE)
    g += C(508, 300, 7, "#aab4bc")
    return g


def art_li():
    """璃：玻璃鱼缸，金鱼水草鹅卵石+玻璃描边高光。"""
    g = ground()
    # 缸体
    g += C(380, 330, 112, "#dff0f8")
    # 水（下半球）
    g += P("M 268 322 A 112 112 0 0 0 492 322 Q 380 306 268 322 Z", GLASS_D)
    # 缸口
    g += E(380, 310, 48, 13, "#bcdcec")
    g += E(380, 310, 36, 9, "#8fc3dd")
    # 水草
    g += P("M 320 430 Q 306 396 322 366 Q 334 344 322 322", stroke="#6aa85e", w=7)
    g += P("M 344 432 Q 352 398 340 372", stroke="#7fae70", w=6)
    # 鹅卵石
    g += E(320, 428, 18, 10, "#e0a868")
    g += E(360, 436, 20, 11, WOOD)
    g += E(404, 430, 17, 10, "#e0a868")
    g += E(438, 424, 14, 8, "#d9a53c")
    # 金鱼
    g += P("M 402 352 L 434 338 L 426 352 L 434 366 Z", "#e07b30")
    g += E(378, 352, 30, 22, "#f5921e")
    g += P("M 370 334 L 380 318 L 390 334 Z", "#e07b30")
    g += C(362, 346, 5, INK)
    g += C(360, 344, 1.8, WHITE)
    # 气泡
    g += C(330, 296, 6, "#cfe9f4")
    g += C(318, 278, 4, "#cfe9f4")
    g += C(326, 262, 3, "#cfe9f4")
    # 玻璃描边与高光
    g += '<circle cx="380" cy="330" r="112" fill="none" stroke="#bcdcec" stroke-width="8"/>'
    g += P("M 300 262 A 92 92 0 0 1 352 230", stroke=WHITE, w=10, )
    return g


def art_ta():
    """塔：三层飞檐宝塔+金顶。"""
    g = ground(380, 446, 200, 20)

    def pagroof(cx, y, w, h, fill):
        return P(f"M {cx - w} {y} Q {cx - w * 0.45} {y - h * 0.5} {cx} {y - h} "
                 f"Q {cx + w * 0.45} {y - h * 0.5} {cx + w} {y} "
                 f"L {cx + w * 0.55} {y + 12} L {cx - w * 0.55} {y + 12} Z", fill)

    # 底座
    g += R(250, 414, 260, 26, 8, WOOD_D)
    # 一层
    g += R(304, 348, 152, 66, 6, CREAM)
    g += P("M 366 414 L 366 384 A 14 14 0 0 1 394 384 L 394 414 Z", "#8a5a33")
    g += pagroof(380, 350, 168, 46, ROOF_R)
    # 二层
    g += R(320, 256, 120, 50, 6, CREAM)
    g += R(368, 272, 24, 26, 4, "#8a5a33")
    g += pagroof(380, 258, 132, 42, ROOF_R)
    # 三层
    g += R(334, 176, 92, 42, 6, CREAM)
    g += R(370, 192, 20, 20, 4, "#8a5a33")
    g += pagroof(380, 178, 100, 38, ROOF_R)
    # 金顶
    g += L(380, 140, 380, 108, YEL_D, 8)
    g += R(372, 122, 16, 8, 4, YEL_D)
    g += C(380, 98, 14, YEL)
    g += C(376, 94, 5, SUN_L)
    return g


def arts():
    return {
        "房": art_fang(), "屋": art_wu(), "楼": art_lou(), "梯": art_ti(),
        "墙": art_qiang(), "瓦": art_wa(), "砖": art_zhuan(), "柜": art_gui(),
        "架": art_jia(), "层": art_ceng(), "厨": art_chu(), "帘": art_lian(),
        "席": art_xi(), "棚": art_peng(), "被": art_bei(), "厕": art_ce(),
        "玻": art_bo(), "璃": art_li(), "塔": art_ta(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "fangwu":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = list(full)
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"房屋建筑组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
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
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
