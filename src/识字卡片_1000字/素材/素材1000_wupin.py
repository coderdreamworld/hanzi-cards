#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""物品组新增 25 卡插画与文案（1000 字批次 B3）。

字表：凳筐盘勺毛巾肥皂刷枕毯垫表缸罐铁盆锅叉碟筷照筒珠瓢
（前 35 字 书本笔刀尺包伞杯桌椅门窗床车船球灯碗绳箱壶扇钟盒瓶桥井旗桶镜梳篮金衣服
 在 legacy ../识字卡片_素材_wupin.py，本文件不重复）。

与 legacy 35 卡错造型：本批全部换主体与配色——
红圆凳/绿格塑料筐+苹果/黄边大盘+馒头/银头木柄饭勺/黄毛巾挂杆/青白格方巾/
粉皂碟+泡泡/蓝皂+泡沫/青柄牙刷挤牙膏/浅蓝枕头/红条毯子/绿圆坐垫/红表带手表
(刻度无数字)/青瓷水缸/玻璃糖罐/磁铁吸回形针/青绿脸盆/平底锅煎蛋/银叉叉苹果/
叠碟+樱桃/木筷夹饺子/蓝相机+照片/青笔筒插画笔/彩色珠串/葫芦瓢舀水。

一眼可辨约定（主控硬规则）：铁=磁铁吸回形针（更直白）；照=相机拍风景（带小照片）；
表=手表表盘只画指针刻度不画数字；刷=牙刷挤牙膏；匙（gongju 组）=汤匙，与勺错形。
同组相邻卡轮廓+主色错开；760×480，第一笔 ground()，图上无文字数字。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
STOOL, STOOL_D = "#e8663c", "#d4552f"           # 凳
CRATE, CRATE_D, CRATE_H = "#7fae70", "#6b9459", "#5e8752"
PLATE_RIM, PLATE_IN = "#f2b53c", "#f9d77e"
BUN, BUN_SH = "#faf6ec", "#e8dfcc"
STEEL, STEEL_D = "#dfe3e6", "#c9cdd1"
TOWEL_L = "#f8d070"
GINGHAM = "#4fae9f"
SOAP_PINK, SOAP_PINK_D = "#f5a58c", "#e78d70"
SOAP_BLUE, SOAP_BLUE_D = "#5fa8d8", "#8ec4e8"
PILLOW, PILLOW_D = "#f7ecd2", "#e0cfa4"
BLANKET_L = "#f0876f"
MAT, MAT_D = "#7fae70", "#6b9459"
VAT, VAT_D, VAT_L = "#3e9486", "#2f7a6d", "#5fc0b0"
WATER = "#8fd8e8"
PAN, PAN_IN = "#5b6168", "#7a828a"
CHERRY = "#d9463c"
CAM, CAM_D = "#5fa8d8", "#3d7ba6"


# ---------- 卡片文案 ----------
GROUP_CARDS = [
    {"char": "凳", "pinyin": "dèng", "tone": "第四声",
     "sentence": "小板凳，坐一坐。",
     "say": "矮矮的、没有靠背的是凳子。",
     "chat": "“凳子和椅子哪里不一样呀？”",
     "life": "请他搬小凳子坐到身边来。"},
    {"char": "筐", "pinyin": "kuāng", "tone": "第一声",
     "sentence": "菜筐里装满苹果。",
     "say": "这是筐，装菜装果都靠它。",
     "chat": "“猜猜筐里还能装什么？”",
     "life": "让他把玩具收进小筐里。"},
    {"char": "盘", "pinyin": "pán", "tone": "第二声",
     "sentence": "盘子里放着小馒头。",
     "say": "又平又浅的是盘子。",
     "chat": "“盘子和碗比，谁更深呀？”",
     "life": "吃饭前帮着摆好盘子。"},
    {"char": "勺", "pinyin": "sháo", "tone": "第二声",
     "sentence": "大勺舀起白米饭。",
     "say": "勺子圆圆的，能舀饭舀汤。",
     "chat": "“勺子拿哪一头才对呢？”",
     "life": "让他自己拿勺吃几口饭。"},
    {"char": "毛", "pinyin": "máo", "tone": "第二声",
     "sentence": "毛巾软软擦擦手。",
     "say": "毛茸茸的毛巾擦手真舒服。",
     "chat": "“小毛巾挂在哪里呀？”",
     "life": "洗完手自己取毛巾擦一擦。"},
    {"char": "巾", "pinyin": "jīn", "tone": "第一声",
     "sentence": "方巾叠得整整齐齐。",
     "say": "方方正正的小方巾，格子真好看。",
     "chat": "“方巾能叠成小方块吗？”",
     "life": "一起把手帕叠成小方块。"},
    {"char": "肥", "pinyin": "féi", "tone": "第二声",
     "sentence": "肥皂滑滑搓泡泡。",
     "say": "滑滑的肥皂搓一搓就出泡泡。",
     "chat": "“泡泡是什么形状的呀？”",
     "life": "洗手时搓出小泡泡给他看。"},
    {"char": "皂", "pinyin": "zào", "tone": "第四声",
     "sentence": "洗澡要用小香皂。",
     "say": "香皂香香的，泡沫软软的。",
     "chat": "“香皂滑不滑？抓得住吗？”",
     "life": "洗澡时让他摸摸香皂上的泡沫。"},
    {"char": "刷", "pinyin": "shuā", "tone": "第一声",
     "sentence": "牙刷挤上小牙膏。",
     "say": "小刷子蘸上牙膏刷刷牙。",
     "chat": "“早晚都要刷牙，对不对？”",
     "life": "早晚陪他刷两次小牙。"},
    {"char": "枕", "pinyin": "zhěn", "tone": "第三声",
     "sentence": "软软枕头睡得香。",
     "say": "软软的枕头枕着头睡觉。",
     "chat": "“你的枕头摸起来什么样？”",
     "life": "睡前让他自己摆好小枕头。"},
    {"char": "毯", "pinyin": "tǎn", "tone": "第三声",
     "sentence": "小毯子盖着真暖和。",
     "say": "厚厚的、软软的是毯子。",
     "chat": "“冷的时候盖上毯子暖不暖？”",
     "life": "午睡时给他盖上小毯子。"},
    {"char": "垫", "pinyin": "diàn", "tone": "第四声",
     "sentence": "小坐垫软软又圆圆。",
     "say": "圆圆软软的垫子坐着舒服。",
     "chat": "“坐垫和板凳谁软呀？”",
     "life": "把小坐垫放他常坐的位置。"},
    {"char": "表", "pinyin": "biǎo", "tone": "第三声",
     "sentence": "手表滴答告诉我时间。",
     "say": "戴在手上的表，能看时间。",
     "chat": "“表盘上的针在做什么呀？”",
     "life": "把手表凑近让他听滴答声。"},
    {"char": "缸", "pinyin": "gāng", "tone": "第一声",
     "sentence": "大水缸装满水。",
     "say": "大大的缸能装好多水。",
     "chat": "“缸和杯子哪个装得多？”",
     "life": "指指家里能存水的大家伙。"},
    {"char": "罐", "pinyin": "guàn", "tone": "第四声",
     "sentence": "玻璃罐里装糖果。",
     "say": "有盖子的罐子，装糖装饼干。",
     "chat": "“猜猜罐子里装了什么？”",
     "life": "找个空罐子装他的小宝贝。"},
    {"char": "铁", "pinyin": "tiě", "tone": "第三声",
     "sentence": "磁铁吸住回形针。",
     "say": "磁铁能把小铁器吸过来。",
     "chat": "“磁铁还能吸住什么呀？”",
     "life": "拿磁铁吸吸回形针和钥匙。"},
    {"char": "盆", "pinyin": "pén", "tone": "第二声",
     "sentence": "脸盆盛水洗洗脸。",
     "say": "又大又浅的是脸盆。",
     "chat": "“盆和桶哪个装水多？”",
     "life": "洗手时让他看看盆里的水。"},
    {"char": "锅", "pinyin": "guō", "tone": "第一声",
     "sentence": "锅里煎个荷包蛋。",
     "say": "平平的锅，能煎蛋煮汤。",
     "chat": "“家里用锅做什么好吃的？”",
     "life": "让他看看锅里的早饭。"},
    {"char": "叉", "pinyin": "chā", "tone": "第一声",
     "sentence": "叉子叉起大苹果。",
     "say": "叉子有尖齿，能叉起水果。",
     "chat": "“叉子和勺子哪里不一样？”",
     "life": "吃水果时让他拿安全餐叉。"},
    {"char": "碟", "pinyin": "dié", "tone": "第二声",
     "sentence": "小碟子里放樱桃。",
     "say": "小小的、浅浅的是碟子。",
     "chat": "“碟子和盘子谁小呀？”",
     "life": "用小碟子装两颗樱桃给他。"},
    {"char": "筷", "pinyin": "kuài", "tone": "第四声",
     "sentence": "筷子夹起小饺子。",
     "say": "两根一起用，夹菜真灵巧。",
     "chat": "“你学会用筷子了吗？”",
     "life": "饭前让他练夹小棉花球。"},
    {"char": "照", "pinyin": "zhào", "tone": "第四声",
     "sentence": "咔嚓一声拍张照。",
     "say": "相机咔嚓一下，拍下照片。",
     "chat": "“最想拍下什么开心的事？”",
     "life": "一起拍张合影看看照片。"},
    {"char": "筒", "pinyin": "tǒng", "tone": "第三声",
     "sentence": "笔筒里插着画笔。",
     "say": "直直的圆筒，能插笔插画笔。",
     "chat": "“筒里还可以插点什么？”",
     "life": "用卷纸筒做个小笔筒。"},
    {"char": "珠", "pinyin": "zhū", "tone": "第一声",
     "sentence": "彩色珠子串一串。",
     "say": "珠子圆圆的，穿起来像项链。",
     "chat": "“珠子都有什么颜色呀？”",
     "life": "陪他玩穿珠子游戏。"},
    {"char": "瓢", "pinyin": "piáo", "tone": "第二声",
     "sentence": "葫芦瓢舀水哗啦啦。",
     "say": "葫芦剖开做成舀水的瓢。",
     "chat": "“瓢和杯子哪个舀水多？”",
     "life": "玩水时用小瓢舀舀水。"},
]


# ---------- 插画 ----------
def art_deng():
    """凳：红色圆面小方凳，四条腿。"""
    g = ground()
    g += E(380, 442, 160, 15, INK, 0.08)
    # 后侧两条腿（短、深色）
    g += f'<g transform="rotate(4 348 340)">{R(334, 336, 26, 96, 11, STOOL_D)}</g>'
    g += f'<g transform="rotate(-4 412 340)">{R(400, 336, 26, 96, 11, STOOL_D)}</g>'
    # 前侧两条腿
    g += f'<g transform="rotate(9 300 340)">{R(286, 336, 28, 106, 12, STOOL)}</g>'
    g += f'<g transform="rotate(-9 462 340)">{R(448, 336, 28, 106, 12, STOOL)}</g>'
    # 坐面侧沿 + 面板
    g += P("M 230 282 L 230 314 Q 230 338 262 338 L 498 338 Q 530 338 530 314 L 530 282 Z", STOOL_D)
    g += E(380, 282, 150, 38, STOOL_D)
    g += E(380, 276, 148, 36, STOOL)
    g += P("M 300 262 Q 380 244 460 262", stroke="#f2907a", w=8)
    return g


def art_kuang():
    """筐：绿色塑料网格筐，装两只苹果。"""
    g = ground(380, 446, 245, 24)
    g += E(380, 440, 190, 14, INK, 0.08)
    # 筐内壁（后墙）
    g += R(236, 232, 288, 60, 14, CRATE_D)
    # 苹果（下半被前壁遮住）
    g += C(318, 262, 54, RED)
    g += C(312, 256, 10, "#f2907a", 0.9)
    g += L(322, 214, 330, 196, "#8a5a33", 6)
    g += E(346, 196, 16, 9, GREEN)
    g += C(446, 268, 48, "#e05a4e")
    g += C(441, 263, 9, "#f2907a", 0.9)
    g += L(450, 226, 458, 210, "#8a5a33", 6)
    g += E(472, 210, 14, 8, GREEN)
    # 前壁（梯形）+ 上沿
    g += PG([(202, 272), (558, 272), (538, 424), (222, 424)], CRATE)
    g += R(196, 262, 368, 26, 13, CRATE_H)
    # 网格孔
    for row, y in enumerate((316, 364)):
        for i in range(4):
            x = 244 + i * 76 + (row * 8)
            g += R(x, y, 54, 22, 11, CRATE_H)
    return g


def art_pan():
    """盘：红边大盘（与 legacy 蓝碗错色），放两只大白馒头。"""
    g = ground(380, 446, 250, 24)
    g += E(380, 434, 226, 18, INK, 0.08)
    g += E(380, 368, 230, 64, "#d4552f")
    g += E(380, 366, 216, 58, "#e8663c")
    g += E(380, 368, 172, 44, "#fdfdfa")
    g += E(380, 368, 146, 36, "#f3efe2")
    # 馒头两只（大、分开、带褶）
    g += E(316, 352, 62, 12, "#e0cfa4", 0.8)
    g += P("M 252 348 Q 252 288 316 288 Q 380 288 380 348 Q 316 362 252 348 Z", BUN)
    g += P("M 274 316 Q 290 300 306 308", stroke="#cbb98f", w=6)
    g += P("M 318 304 Q 334 296 350 306", stroke="#cbb98f", w=6)
    g += P("M 344 322 Q 356 314 368 322", stroke="#cbb98f", w=5)
    g += E(292, 310, 20, 11, "#fdfdfa", 0.9)
    g += E(452, 348, 54, 10, "#e0cfa4", 0.8)
    g += P("M 398 344 Q 398 296 452 296 Q 506 296 506 344 Q 452 356 398 344 Z", BUN)
    g += P("M 420 318 Q 434 306 450 312", stroke="#cbb98f", w=5)
    g += P("M 462 314 Q 476 306 490 316", stroke="#cbb98f", w=5)
    g += E(436, 314, 14, 8, "#fdfdfa", 0.9)
    return g


def art_shao():
    """勺：大饭勺，银勺头盛白米饭（饭堆高、有饭粒），木柄。"""
    g = ground(380, 446, 245, 24)
    g += E(330, 430, 130, 14, INK, 0.08)
    # 柄
    g += L(348, 314, 600, 186, "#e8a13c", 36)
    g += L(352, 306, 588, 184, "#f8d070", 10)
    g += C(600, 186, 19, "#e8a13c")
    # 勺头（斜置，椭圆饭勺头 + 高高的白饭）
    head = wrap(
        E(0, 0, 114, 82, STEEL_D),
        E(-4, -4, 108, 76, STEEL),
        E(0, 6, 94, 62, "#b8bec4"),
        # 白饭堆
        P("M -84 10 Q -92 -34 -46 -44 Q -34 -68 2 -60 Q 26 -78 50 -56 Q 86 -60 84 -22 "
          "Q 96 6 62 18 Q 0 32 -50 24 Q -80 22 -84 10 Z", "#fdfdfa"),
        E(-52, -22, 13, 7, "#e8dfcc"), E(-14, -40, 12, 6, "#e8dfcc"),
        E(24, -30, 12, 6, "#e8dfcc"), E(-30, 2, 12, 6, "#e8dfcc"),
        E(20, 0, 12, 6, "#e8dfcc"), E(52, -10, 10, 5, "#e8dfcc"),
        E(-40, -46, 15, 8, "#fdfdfa", 0.7),
    )
    g += f'<g transform="translate(300,336) rotate(-12)">{head}</g>'
    return g


def art_mao():
    """毛：黄毛巾搭在木杆上，毛边蓬松。"""
    g = ground()
    g += E(380, 442, 150, 13, INK, 0.07)
    # 搭过去的后襟
    g += R(268, 142, 224, 66, 12, "#d99a2b")
    # 木杆
    g += R(172, 162, 416, 24, 12, "#b57b44")
    g += C(172, 174, 15, "#8a5a33")
    g += C(588, 174, 15, "#8a5a33")
    # 前襟（底边波浪毛边）
    scallop = "M 252 178 L 252 366 "
    x0, x1 = 252, 508
    n = 8
    step = (x1 - x0) / n
    for i in range(n):
        ax = x0 + step * (i + 0.5)
        bx = x0 + step * (i + 1)
        scallop += f"Q {ax} {386 + (6 if i % 2 else 0)} {bx:.0f} 366 "
    scallop += "L 508 178 Z"
    g += P(scallop, "#f2b53c")
    g += R(252, 214, 256, 26, 13, TOWEL_L)
    g += R(252, 296, 256, 26, 13, TOWEL_L)
    g += P("M 300 190 Q 292 280 300 356", stroke="#d99a2b", w=5, opacity=0.45)
    g += P("M 380 188 Q 374 280 380 358", stroke="#d99a2b", w=5, opacity=0.45)
    g += P("M 460 190 Q 456 280 460 356", stroke="#d99a2b", w=5, opacity=0.45)
    return g


def art_jin():
    """巾：青白格方巾，折角叠放。"""
    g = ground()
    g += E(380, 442, 170, 14, INK, 0.08)
    g += f'<g transform="rotate(-7 380 320)">'
    g += R(236, 186, 288, 268, 18, GINGHAM)
    for i in range(3):
        g += R(272 + i * 78, 186, 36, 268, 0, WHITE, 0.35)
    for j in range(3):
        g += R(236, 224 + j * 78, 288, 36, 0, WHITE, 0.35)
    g += P("M 254 204 L 506 204 L 506 436 L 254 436 Z", fill="none", stroke=WHITE, w=8)
    # 右上折角
    g += PG([(524, 186), (524, 282), (428, 186)], "#7cc8bb")
    g += P("M 428 186 L 524 282", stroke="#5bb3a5", w=7)
    g += "</g>"
    return g


def art_fei():
    """肥：粉色肥皂搁在白皂碟上，飘着泡泡。"""
    g = ground()
    g += E(380, 440, 190, 14, INK, 0.08)
    g += E(380, 404, 196, 36, "#e3ded0")
    g += E(380, 398, 196, 36, "#fdfdfa")
    g += E(380, 396, 150, 25, "#f3efe2")
    g += f'<g transform="rotate(-5 380 360)">'
    g += R(262, 316, 240, 92, 42, SOAP_PINK_D)
    g += R(256, 306, 240, 92, 42, SOAP_PINK)
    g += R(270, 314, 200, 34, 17, "#f8c0ae")
    g += P("M 300 356 Q 340 340 380 356 Q 420 372 460 356", stroke=SOAP_PINK_D, w=6)
    g += "</g>"
    # 泡泡
    for bx, by, br in ((566, 316, 30), (614, 258, 21), (548, 218, 15), (608, 184, 11)):
        g += C(bx, by, br, "#dff0fa")
        g += C(bx - br * 0.32, by - br * 0.32, max(3, br * 0.3), WHITE, 0.9)
    g += C(234, 314, 20, "#dff0fa")
    g += C(228, 308, 6, WHITE, 0.9)
    return g


def art_zao():
    """皂：蓝色香皂（大而醒目）顶着绵密泡沫，坐在浴缸沿。"""
    g = ground()
    g += E(380, 442, 200, 14, INK, 0.08)
    g += R(180, 402, 400, 40, 20, "#fdfdfa")
    g += R(180, 424, 400, 18, 9, "#cfe0ea")
    # 蓝香皂（放大，让皂体一眼可辨）
    g += R(248, 292, 264, 122, 44, SOAP_BLUE_D)
    g += R(242, 284, 264, 122, 44, SOAP_BLUE)
    g += R(258, 294, 200, 30, 15, "#a8d4f0")
    # 泡沫云（收小成盖在皂顶的一层）
    foam = ""
    for fx, fy, fr in ((298, 276, 30), (348, 260, 38), (408, 270, 34), (458, 286, 24),
                       (270, 290, 20), (486, 298, 16)):
        foam += C(fx, fy, fr, WHITE) + C(fx - fr * 0.3, fy - fr * 0.3, fr * 0.32, "#eef4f8")
    g += foam
    g += C(236, 342, 13, WHITE)
    g += C(524, 348, 11, WHITE)
    return g


def art_shua():
    """刷：斜置牙刷，白刷毛一簇簇（灰底白条）+ 白牙膏。"""
    g = ground()
    g += E(430, 442, 160, 13, INK, 0.07)
    brush = wrap(
        # 牙膏（白带，压在刷毛上）
        P("M 240 250 Q 232 224 254 216 Q 256 198 280 200 Q 288 184 310 190 Q 330 182 340 198 "
          "Q 358 200 354 218 Q 360 234 342 240 Q 292 252 240 250 Z", "#fdfdfa"),
        P("M 256 232 Q 292 222 330 226", stroke="#dbe7ee", w=5),
        # 刷毛座（灰底）+ 一簇簇白毛
        R(238, 244, 152, 66, 18, "#dfe7ec"),
        R(238, 294, 152, 16, 8, "#c3ced6"),
        R(248, 250, 16, 54, 8, "#fdfdfa"), R(278, 250, 16, 54, 8, "#fdfdfa"),
        R(308, 250, 16, 54, 8, "#fdfdfa"), R(338, 250, 16, 54, 8, "#fdfdfa"),
        R(366, 250, 14, 54, 7, "#fdfdfa"),
        # 颈 + 柄
        R(376, 254, 64, 46, 16, "#3e9486"),
        R(428, 246, 212, 66, 32, "#4fae9f"),
        C(472, 279, 10, "#a8dcd0"), C(510, 279, 10, "#a8dcd0"), C(548, 279, 10, "#a8dcd0"),
        R(616, 258, 44, 42, 20, "#3e9486"),
        C(628, 279, 8, "#eafaf5"),
    )
    g += f'<g transform="rotate(28 380 280)">{brush}</g>'
    return g


def art_zhen():
    """枕：鼓鼓的白枕头（蓝滚边 + 两端蓬圆压痕 + 中央睡窝），去掉翻盖防止像拖鞋。"""
    g = ground()
    g += E(380, 440, 205, 16, INK, 0.08)
    g += f'<g transform="rotate(-4 380 330)">'
    body = ("M 240 262 Q 260 238 310 232 Q 380 224 450 232 Q 500 238 520 262 "
            "Q 544 286 546 330 Q 544 374 520 398 Q 500 422 450 428 Q 380 436 310 428 "
            "Q 260 422 240 398 Q 216 374 214 330 Q 216 286 240 262 Z")
    g += P(body, "#fdfdfa")
    # 中央睡窝（偏一侧）
    g += E(330, 330, 62, 42, "#c9dcea", 0.55)
    g += E(330, 330, 38, 24, "#b8d4e6", 0.5)
    # 软褶与两端蓬圆压痕
    g += P("M 262 278 Q 296 300 322 306", stroke="#b8d4e6", w=6, opacity=0.8)
    g += P("M 268 384 Q 304 362 336 356", stroke="#b8d4e6", w=6, opacity=0.8)
    g += P("M 534 300 Q 546 330 534 362", stroke="#b8d4e6", w=6, opacity=0.8)
    g += P("M 226 300 Q 214 330 226 362", stroke="#b8d4e6", w=6, opacity=0.8)
    # 高光 + 蓝滚边
    g += E(436, 274, 52, 14, WHITE, 0.9)
    g += P(body, fill="none", stroke="#5fa8d8", w=9)
    g += "</g>"
    return g


def art_tan():
    """毯：红橙条纹毯子叠成两层，两端流苏。"""
    g = ground()
    g += E(380, 442, 220, 15, INK, 0.08)
    # 下层
    g += R(180, 352, 400, 84, 24, "#d4552f")
    g += R(196, 352, 368, 22, 11, "#e06a48")
    # 上层
    g += R(198, 262, 364, 100, 24, "#e8663c")
    g += R(198, 262, 364, 36, 18, BLANKET_L)
    g += R(198, 316, 364, 16, 8, "#fbe8cf")
    g += R(198, 338, 364, 8, 4, "#fbe8cf")
    # 侧缝
    g += R(180, 352, 16, 84, 8, "#b23f22")
    g += R(564, 352, 16, 84, 8, "#b23f22")
    # 流苏
    for x in range(206, 560, 32):
        g += L(x, 436, x, 462, "#fbe8cf", 7)
    return g


def art_dian():
    """垫：圆鼓鼓的厚坐垫（蒲团式：厚侧墙竖绗缝 + 顶面放射绗缝 + 中央包扣）。"""
    g = ground()
    g += E(380, 448, 215, 14, INK, 0.09)
    # 厚侧墙（深一号）
    g += P("M 175 308 L 175 362 Q 175 424 380 424 Q 585 424 585 362 L 585 308 Z", MAT_D)
    # 侧墙竖绗缝（沿底缘弧线）
    for i in range(1, 6):
        x = 175 + i * (410 / 6)
        t = (x - 380) / 205.0
        k = math.sqrt(max(0.0, 1 - t * t))
        g += L(x, 308 + 62 * k + 3, x, 362 + 60 * k - 5, "#4c6e46", 4)
    # 顶面
    g += E(380, 308, 205, 62, MAT)
    # 顶面放射绗缝（从包扣弯向边缘）
    for rx, ry in ((182, 308), (202, 277), (380, 248), (252, 266), (578, 308),
                   (502, 352), (258, 352)):
        mx, my = (380 + rx) / 2, (306 + ry) / 2
        g += P(f"M 380 306 Q {mx} {my} {rx} {ry}", stroke="#4c6e46", w=4, opacity=0.65)
    # 高光 + 中央包扣
    g += E(296, 280, 64, 18, "#9cc98a", 0.55)
    g += C(380, 306, 19, "#4c6e46")
    g += C(373, 299, 6, "#8fba80", 0.9)
    return g


def _ticks(cx, cy, r_out, r_in, r_in_minor, n=12, color="#9aa0a6"):
    import math as _m
    s = ""
    for i in range(n):
        a = i * 2 * _m.pi / n
        r1 = r_out
        r2 = r_in if i % 3 == 0 else r_in_minor
        s += L(cx + r1 * _m.sin(a), cy - r1 * _m.cos(a),
               cx + r2 * _m.sin(a), cy - r2 * _m.cos(a), color, 6 if i % 3 == 0 else 4)
    return s


def art_biao():
    """表：红表带手表，表盘只有刻度和指针（无数字）。"""
    g = ground()
    g += E(380, 452, 120, 11, INK, 0.08)
    # 表带
    g += R(332, 100, 96, 96, 26, STOOL)
    g += R(332, 380, 96, 86, 26, STOOL)
    g += R(322, 436, 116, 26, 12, STOOL_D)
    g += L(380, 436, 380, 462, "#f2b53c", 8)
    # 表壳
    g += C(380, 290, 108, "#d99a2b")
    g += C(380, 290, 100, "#f2b53c")
    g += C(380, 290, 84, "#fdfdfa")
    g += _ticks(380, 290, 72, 58, 64)
    # 指针
    g += L(380, 290, 380, 248, INK, 11)
    g += L(380, 290, 428, 260, INK, 7)
    g += C(380, 290, 9, STOOL)
    g += C(377, 287, 3, "#fdfdfa")
    # 表冠
    g += R(488, 276, 20, 28, 8, "#d99a2b")
    return g


def art_gang():
    """缸：青瓷大水缸——宽口沿 + 鼓腹深身，缸口水面明显（与浅盆错形）。"""
    g = ground(380, 446, 250, 24)
    g += E(380, 440, 190, 13, INK, 0.08)
    # 缸身（深鼓腹，口沿略收）
    g += P("M 244 226 Q 206 268 200 336 Q 196 424 380 428 Q 564 424 560 336 "
           "Q 554 268 516 226 Z", VAT)
    # 高光与两道棱
    g += P("M 300 300 Q 286 360 300 412", stroke=VAT_L, w=14, opacity=0.5)
    g += P("M 212 336 Q 380 366 548 336", stroke=VAT_D, w=6, opacity=0.6)
    g += P("M 208 378 Q 380 406 552 378", stroke=VAT_D, w=6, opacity=0.6)
    # 宽口沿 + 满缸水
    g += E(380, 226, 158, 30, VAT_D)
    g += E(380, 223, 136, 24, "#2a6b60")
    g += E(380, 226, 112, 18, "#1f5a50")
    g += E(380, 228, 94, 14, WATER)
    g += P("M 342 229 Q 380 224 418 230", stroke="#c8ecf5", w=5)
    return g


def art_guan():
    """罐：玻璃糖罐，金色圆盖，装彩色糖果。"""
    g = ground()
    g += E(380, 442, 160, 13, INK, 0.08)
    # 罐身（玻璃）
    g += P("M 300 240 L 300 252 Q 268 282 266 342 L 266 396 Q 266 424 296 424 "
           "L 464 424 Q 494 424 494 396 L 494 342 Q 492 282 460 252 L 460 240 Z", "#e8f2f7")
    # 糖果
    for cx, cy, cr, col in ((330, 384, 34, RED), (402, 396, 36, "#f2b53c"),
                            (356, 340, 28, "#7fae70"), (446, 352, 26, "#5fa8d8")):
        g += C(cx, cy, cr, col)
        g += C(cx - cr * 0.32, cy - cr * 0.34, cr * 0.3, WHITE, 0.75)
    # 玻璃反光
    g += R(292, 274, 20, 122, 10, WHITE, 0.55)
    g += R(458, 300, 13, 92, 7, WHITE, 0.4)
    # 瓶口与盖
    g += R(296, 220, 168, 28, 10, "#d5e4ec")
    g += P("M 288 222 Q 288 170 380 170 Q 472 170 472 222 Z", "#f2b53c")
    g += R(282, 214, 196, 18, 9, "#d99a2b")
    g += C(380, 162, 15, "#d99a2b")
    g += C(375, 157, 5, "#f8d070", 0.9)
    return g


def art_tie():
    """铁：马蹄形磁铁吸住回形针（含被吸过去的动态）。"""
    g = ground(380, 446, 250, 24)
    g += E(380, 446, 150, 12, INK, 0.07)
    # 磁铁 U 形
    g += P("M 315 350 L 315 265 A 65 65 0 0 1 445 265 L 445 350", stroke=RED, w=72)
    g += R(279, 344, 72, 38, 10, STEEL)
    g += R(409, 344, 72, 38, 10, STEEL)
    g += P("M 315 300 Q 316 250 352 232", stroke="#f2907a", w=10, opacity=0.7)
    # 被吸住的回形针
    def clip(x, y, h=58, w=24):
        return R(x, y, w, h, w / 2, "#9aa0a6") + R(x + 6, y + 8, w - 12, h - 18, (w - 12) / 2, STEEL)
    g += clip(302, 382)
    g += clip(433, 382, 52)
    g += clip(437, 424, 46)
    # 空中正被吸过去的回形针 + 动势线
    g += clip(532, 284, 56)
    g += P("M 578 270 Q 594 306 578 342", stroke=STEEL_D, w=6)
    g += P("M 600 258 Q 620 306 600 354", stroke=STEEL_D, w=6)
    return g


def art_pen():
    """盆：青绿搪瓷脸盆盛水。"""
    g = ground(380, 446, 250, 24)
    g += E(380, 440, 170, 12, INK, 0.08)
    g += E(380, 434, 124, 14, "#3e9486")
    g += P("M 180 302 Q 222 392 266 410 L 266 420 Q 266 434 294 434 "
           "L 466 434 Q 494 434 494 420 L 494 410 Q 538 392 580 302 Z", "#4fae9f")
    g += P("M 214 352 Q 380 396 546 352", stroke="#fdfdfa", w=12, opacity=0.5)
    g += E(380, 302, 206, 50, "#3e9486")
    g += E(380, 302, 186, 42, "#5fc0b0")
    g += E(380, 305, 160, 33, "#2f7a6d")
    g += E(380, 307, 138, 26, WATER)
    g += P("M 310 308 Q 340 300 370 308", stroke="#c8ecf5", w=5)
    g += P("M 400 314 Q 428 308 452 314", stroke="#c8ecf5", w=4)
    return g


def art_guo():
    """锅：平底锅煎荷包蛋，冒着热气。"""
    g = ground(380, 446, 250, 24)
    g += E(400, 442, 200, 13, INK, 0.08)
    # 锅柄
    g += f'<g transform="rotate(-16 560 322)">'
    g += R(560, 300, 150, 44, 20, "#43484e")
    g += R(566, 306, 138, 10, 5, "#5b6168")
    g += C(692, 322, 9, "#2f343a")
    g += "</g>"
    # 锅体
    g += E(380, 332, 208, 74, PAN)
    g += E(380, 330, 188, 62, PAN_IN)
    # 荷包蛋
    g += P("M 270 330 Q 262 296 296 288 Q 300 262 340 268 Q 360 252 396 266 "
           "Q 436 258 448 288 Q 470 300 456 326 Q 462 352 430 360 Q 420 380 384 372 "
           "Q 350 386 322 370 Q 286 372 280 350 Q 264 344 270 330 Z", "#fdfdfa")
    g += C(356, 322, 34, "#f7ae35")
    g += C(346, 312, 9, "#fbe8cf")
    # 热气
    g += P("M 318 240 Q 304 214 320 192", stroke="#eef2f5", w=8, opacity=0.85)
    g += P("M 388 232 Q 374 206 390 184", stroke="#eef2f5", w=8, opacity=0.85)
    return g


def art_cha():
    """叉：短柄银叉（齿宽分明）叉起一只大红苹果。"""
    g = ground()
    g += E(330, 442, 150, 13, INK, 0.07)
    fork = wrap(
        R(310, 190, 18, 84, 9, "#b8bec4"), R(342, 190, 18, 84, 9, "#b8bec4"),
        R(374, 190, 18, 84, 9, "#b8bec4"), R(406, 190, 18, 84, 9, "#b8bec4"),
        R(312, 196, 14, 74, 7, STEEL), R(344, 196, 14, 74, 7, STEEL),
        R(376, 196, 14, 74, 7, STEEL), R(408, 196, 14, 74, 7, STEEL),
        P("M 306 268 L 306 296 Q 306 320 334 322 L 396 322 Q 424 320 424 296 L 424 268 Z", "#b8bec4"),
        R(342, 318, 46, 172, 23, "#b8bec4"),
        R(348, 324, 13, 154, 6, STEEL),
        L(316, 200, 316, 264, "#fdfdfa", 5), L(348, 200, 348, 264, "#fdfdfa", 5),
        L(380, 200, 380, 264, "#fdfdfa", 5),
    )
    g += f'<g transform="rotate(-26 380 330)">{fork}</g>'
    # 大苹果（几乎与叉头同宽）
    g += C(282, 168, 74, RED)
    g += P("M 258 122 Q 282 108 306 122", stroke="#c94f30", w=6)
    g += C(258, 146, 15, "#f2907a", 0.9)
    g += L(292, 100, 300, 74, "#8a5a33", 8)
    g += E(320, 72, 22, 12, GREEN)
    return g


def art_die():
    """碟：三只小碟叠放，顶上两颗樱桃。"""
    g = ground()
    g += E(380, 442, 180, 13, INK, 0.08)
    # 底碟
    g += E(380, 402, 172, 40, "#3e9486")
    g += E(380, 398, 150, 33, "#4fae9f")
    # 中碟（白）
    g += E(380, 364, 158, 38, "#c9cdd1")
    g += E(380, 361, 136, 31, "#fdfdfa")
    # 顶碟
    g += E(380, 330, 150, 36, "#3e9486")
    g += E(380, 327, 128, 29, "#4fae9f")
    g += E(380, 328, 100, 21, "#2f7a6d")
    # 樱桃
    g += P("M 350 306 Q 366 274 382 266", stroke="#8a5a33", w=6)
    g += P("M 398 308 Q 392 280 382 266", stroke="#8a5a33", w=6)
    g += E(390, 258, 16, 9, GREEN)
    g += C(348, 314, 26, CHERRY)
    g += C(340, 307, 7, "#f2907a", 0.9)
    g += C(398, 318, 24, "#e05a4e")
    g += C(391, 312, 6, "#f2907a", 0.9)
    return g


def art_kuai():
    """筷：一双木筷夹起一只白饺子（饺子加深色，配阴影）。"""
    g = ground(380, 446, 250, 24)
    g += E(400, 442, 160, 12, INK, 0.07)
    # 饺子（奶黄白 + 明显描影）
    g += E(385, 354, 96, 13, INK, 0.10)
    g += P("M 285 320 Q 300 240 385 236 Q 470 240 485 320 "
           "Q 445 344 385 346 Q 325 344 285 320 Z", "#f7ecd2")
    g += P("M 285 320 Q 325 344 385 346 Q 445 344 485 320 "
           "Q 445 356 385 358 Q 325 356 285 320 Z", "#e0cfa4")
    g += P("M 336 262 Q 350 248 364 258", stroke="#cbb98f", w=6)
    g += P("M 372 256 Q 386 244 400 254", stroke="#cbb98f", w=6)
    g += P("M 410 264 Q 424 252 436 264", stroke="#cbb98f", w=6)
    g += E(330, 280, 18, 10, "#fdfdfa", 0.9)
    # 筷子两根
    g += L(636, 412, 332, 242, WOOD, 17)
    g += L(332, 242, 396, 278, "#b57b44", 17)
    g += L(668, 392, 366, 224, WOOD, 15)
    g += L(366, 224, 430, 260, "#b57b44", 15)
    g += C(636, 412, 11, "#8a5a33")
    g += C(668, 392, 11, "#8a5a33")
    return g


def art_zhao():
    """照：蓝色相机咔嚓拍照，右下刚吐出一张风景照。"""
    g = ground(380, 446, 250, 24)
    g += E(400, 440, 210, 13, INK, 0.08)
    # 机身
    g += R(250, 178, 180, 44, 18, CAM_D)
    g += R(430, 166, 46, 26, 10, "#f2b53c")
    g += R(300, 166, 42, 24, 8, "#4a3226")
    g += R(220, 210, 330, 182, 36, CAM)
    g += R(238, 226, 40, 150, 20, "#a8d4f0", 0.6)
    # 镜头
    g += C(385, 300, 88, CAM_D)
    g += C(385, 300, 64, "#2f4858")
    g += C(385, 300, 44, WATER)
    g += C(371, 286, 12, WHITE, 0.85)
    # 快照照片
    g += f'<g transform="rotate(8 556 396)">'
    g += R(470, 330, 172, 132, 10, WHITE)
    g += R(481, 341, 150, 96, 6, "#aee0f2")
    g += C(606, 364, 15, "#f7ae35")
    g += PG([(481, 437), (548, 382), (631, 437)], GREEN)
    g += PG([(548, 437), (610, 398), (631, 437)], "#6b9459")
    g += "</g>"
    return g


def art_tong():
    """筒：青色笔筒，插着画笔铅笔蜡笔。"""
    g = ground()
    g += E(380, 442, 150, 13, INK, 0.08)
    # 筒内与插着的笔
    g += E(380, 252, 100, 24, "#255c52")
    g += f'<g transform="rotate(-12 340 180)">'
    g += R(326, 108, 30, 140, 9, "#f2b53c")
    g += PG([(326, 108), (356, 108), (341, 74)], "#e9b97e")
    g += PG([(336, 86), (346, 86), (341, 74)], INK)
    g += "</g>"
    g += f'<g transform="rotate(8 430 170)">'
    g += R(418, 84, 28, 130, 12, WOOD)
    g += R(416, 204, 32, 24, 7, "#c9cdd1")
    g += P("M 418 226 Q 432 252 446 226 Z", "#b57b44")
    g += "</g>"
    g += f'<g transform="rotate(-3 386 200)">'
    g += R(374, 130, 26, 110, 8, RED)
    g += PG([(374, 130), (400, 130), (387, 106)], "#d4552f")
    g += "</g>"
    # 筒身
    g += R(280, 252, 200, 182, 20, GINGHAM)
    g += E(380, 252, 100, 24, "#3e9486")
    g += P("M 280 252 Q 280 240 292 232 L 468 232 Q 480 240 480 252 L 480 258 "
           "Q 380 292 280 258 Z", "#5fc0b0")
    g += P("M 296 330 Q 380 356 464 330", stroke=WHITE, w=9, opacity=0.5)
    g += P("M 296 380 Q 380 404 464 380", stroke=WHITE, w=9, opacity=0.5)
    return g


def art_zhu():
    """珠：彩色大珠子串成一圈项链。"""
    g = ground()
    g += E(380, 440, 210, 13, INK, 0.07)
    cols = [RED, "#f2b53c", "#4fae9f", "#5fa8d8", "#f5a58c", "#8ec4e8"]
    n = 11
    pts = []
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        pts.append((380 + 195 * math.cos(a), 302 + 116 * math.sin(a)))
    for i, (x, y) in enumerate(sorted(pts, key=lambda p: p[1])):
        col = cols[i % len(cols)]
        g += C(x, y, 27, col)
        g += C(x - 8, y - 9, 8, WHITE, 0.85)
    return g


def art_piao():
    """瓢：葫芦瓢侧视——瓢身与葫芦颈柄连成一体（柄端带小圆肚），瓢内盛水。"""
    g = ground()
    g += E(380, 446, 200, 14, INK, 0.09)
    # 葫芦颈柄（先画，根部被瓢口沿盖住 → 连体）
    g += P("M 306 328 Q 262 286 248 234 Q 240 198 260 176", stroke="#a8823a", w=46)
    g += C(264, 166, 40, "#a8823a")
    g += C(256, 156, 22, "#c9a24b", 0.6)
    g += C(258, 132, 8, "#8a6a2e")
    # 瓢身（半球，口朝上）
    g += P("M 262 318 Q 268 414 380 424 Q 492 414 498 318 Z", "#a8823a")
    g += P("M 452 332 Q 446 392 410 416 Q 478 400 496 338 Z", "#8a6a2e")
    g += P("M 322 344 Q 314 384 330 410", stroke="#8a6a2e", w=5, opacity=0.5)
    # 瓢口与水
    g += E(380, 318, 118, 26, "#d9b56a")
    g += E(380, 320, 96, 19, "#f2e3bd")
    g += E(380, 322, 80, 14, WATER)
    g += P("M 336 324 Q 372 318 408 324", stroke="#c8ecf5", w=5)
    # 水滴
    g += drop(548, 408, 13)
    g += C(528, 366, 6, "#c8ecf5", 0.9)
    return g


def arts():
    return {
        "凳": art_deng(), "筐": art_kuang(), "盘": art_pan(), "勺": art_shao(),
        "毛": art_mao(), "巾": art_jin(), "肥": art_fei(), "皂": art_zao(),
        "刷": art_shua(), "枕": art_zhen(), "毯": art_tan(), "垫": art_dian(),
        "表": art_biao(), "缸": art_gang(), "罐": art_guan(), "铁": art_tie(),
        "盆": art_pen(), "锅": art_guo(), "叉": art_cha(), "碟": art_die(),
        "筷": art_kuai(), "照": art_zhao(), "筒": art_tong(), "珠": art_zhu(),
        "瓢": art_piao(),
    }


if __name__ == "__main__":
    LEGACY35 = {"书", "本", "笔", "刀", "尺", "包", "伞", "杯", "桌", "椅", "门", "窗",
                "床", "车", "船", "球", "灯", "碗", "绳", "箱", "壶", "扇", "钟", "盒",
                "瓶", "桥", "井", "旗", "桶", "镜", "梳", "篮", "金", "衣", "服"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "wupin":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY35]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"物品组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != c["tone"]]
    print(f"拼音/声调：{'与拼音表逐一一致 ✓' if not bad_py else '不一致 ' + str(bad_py)}")
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
