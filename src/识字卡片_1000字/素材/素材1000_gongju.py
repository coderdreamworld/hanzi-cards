#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""工具组新增 18 卡插画与文案（1000 字批次 B3）。

字表：剪锤钉锁钥匙锯斧铲蜡秤针网帚锄镰烛柴（gongju 组无 legacy 卡，全 18 字本文件覆盖）。

一眼可辨约定（主控硬规则，刀具类全部画使用场景、圆润友好、无伤人意象）：
剪=安全圆头剪刀剪纸条（剪下的纸片飘落）；锤=木柄锤敲木板上的钉子（带敲击动势线）；
钉=木板上大小钉子特写；锁=金色挂锁扣在门搭扣上；钥=银色钥匙系红丝带；
匙=白色汤匙舀橙汤（与 wupin 组「勺」错形错色）；锯=锯子锯圆木（木屑飞溅）；
斧=红柄斧劈柴垛（斧入木桩+劈好的木段）；铲=铲子铲雪（雪堆雪球）；
蜡=三支蜡笔+画着太阳的画纸；秤=表盘台秤称两个橘子（刻度无数字）；
针=大针引红线缝扣子；网=捕蝶网兜住蝴蝶；帚=扫帚扫落叶；
锄=锄头松土种小苗；镰=弯镰割麦捆；烛=生日蛋糕上的一支蜡烛（火苗圆润）；
柴=红头火柴堆（只画火柴棒，不画火）。同组相邻卡轮廓+主色错开。
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
STEEL, STEEL_D = "#dfe3e6", "#c9cdd1"
PAPER, PAPER_D = "#9cc98a", "#7fae70"
GOLD, GOLD_D = "#f2b53c", "#d99a2b"
REDH = "#e8663c"
WOODH = "#c89058"
ORANGE = "#f5921e"
THREAD = "#e8663c"
BTN = "#4fae9f"
WHEAT, WHEAT_D = "#f2c14e", "#d9a53c"
FROST = "#fdfdfa"
CUP = "#b57b44"


# ---------- 卡片文案 ----------
GROUP_CARDS = [
    {"char": "剪", "pinyin": "jiǎn", "tone": "第三声",
     "sentence": "小剪刀剪纸真开心。",
     "say": "张开剪刀口，咔嚓剪开纸。",
     "chat": "“用剪刀时小手要怎么拿呀？”",
     "life": "陪他用安全剪刀剪彩纸条。"},
    {"char": "锤", "pinyin": "chuí", "tone": "第二声",
     "sentence": "小锤子咚咚敲钉子。",
     "say": "锤子一敲，咚咚咚。",
     "chat": "“敲的时候会发出什么声音？”",
     "life": "敲敲打打时让他在旁边听。"},
    {"char": "钉", "pinyin": "dīng", "tone": "第一声",
     "sentence": "木板上钉着小钉子。",
     "say": "亮亮的小钉子，一头尖一头平。",
     "chat": "“钉东西时读 dìng，对不对？”",
     "life": "摸摸家具上圆圆的小钉帽。"},
    {"char": "锁", "pinyin": "suǒ", "tone": "第三声",
     "sentence": "小锁头，锁得牢。",
     "say": "大挂锁咔哒一扣，门就锁住啦。",
     "chat": "“锁住门，谁能打开呢？”",
     "life": "出门时让他看看锁好门。"},
    {"char": "钥", "pinyin": "yào", "tone": "第四声",
     "sentence": "银色的钥匙亮闪闪。",
     "say": "钥匙对准锁孔，一转就开门。",
     "chat": "“你家的钥匙长什么样子？”",
     "life": "让他摸摸大门钥匙的形状。"},
    {"char": "匙", "pinyin": "chí", "tone": "第二声",
     "sentence": "喝汤要用小汤匙。",
     "say": "汤匙舀汤喝；‘钥匙’里它读轻声。",
     "chat": "“汤匙和筷子谁适合喝汤？”",
     "life": "喝汤时让他自己舀一勺。"},
    {"char": "锯", "pinyin": "jù", "tone": "第四声",
     "sentence": "锯子沙沙锯木头。",
     "say": "锯齿一来一回，锯开木头。",
     "chat": "“锯木头时会掉下什么呀？”",
     "life": "摸摸锯齿，说说扎不扎手。"},
    {"char": "斧", "pinyin": "fǔ", "tone": "第三声",
     "sentence": "斧头劈柴一根根。",
     "say": "斧头一劈，木头分成两半。",
     "chat": "“劈好的木头能用来做什么？”",
     "life": "讲讲冬天烧柴取暖的事。"},
    {"char": "铲", "pinyin": "chǎn", "tone": "第三声",
     "sentence": "铲子把雪铲干净。",
     "say": "铲子贴地一推，雪就起来啦。",
     "chat": "“下雪了用什么铲雪呢？”",
     "life": "冬天让他用小铲子玩雪。"},
    {"char": "蜡", "pinyin": "là", "tone": "第四声",
     "sentence": "彩色蜡笔画太阳。",
     "say": "蜡笔握在手里涂涂画画。",
     "chat": "“你想先用哪支蜡笔画？”",
     "life": "一起用蜡笔画个大太阳。"},
    {"char": "秤", "pinyin": "chèng", "tone": "第四声",
     "sentence": "秤上放两个橘子。",
     "say": "秤能称出东西有多重。",
     "chat": "“橘子和西瓜谁重呀？”",
     "life": "买菜时看看秤怎么称。"},
    {"char": "针", "pinyin": "zhēn", "tone": "第一声",
     "sentence": "长针引线缝扣子。",
     "say": "线穿过针眼，缝呀缝。",
     "chat": "“纽扣掉了请谁来缝？”",
     "life": "让他看一次穿针引线。"},
    {"char": "网", "pinyin": "wǎng", "tone": "第三声",
     "sentence": "捕蝶网轻轻捉蝴蝶。",
     "say": "网兜一捞，蝴蝶进网啦。",
     "chat": "“蝴蝶飞得快，怎么捉住它？”",
     "life": "拿小网兜捞几个小玩具。"},
    {"char": "帚", "pinyin": "zhǒu", "tone": "第三声",
     "sentence": "扫帚扫走小落叶。",
     "say": "扫帚唰唰唰，把地扫干净。",
     "chat": "“扫帚能把什么扫走呀？”",
     "life": "给他小扫帚扫扫纸屑。"},
    {"char": "锄", "pinyin": "chú", "tone": "第二声",
     "sentence": "锄头松土种小苗。",
     "say": "锄头翻翻土，好种小苗苗。",
     "chat": "“种小苗前要先做什么？”",
     "life": "在花盆松松土，种颗豆。"},
    {"char": "镰", "pinyin": "lián", "tone": "第二声",
     "sentence": "镰刀割麦闪银光。",
     "say": "弯弯的镰刀，割麦子最快。",
     "chat": "“镰刀的刀片是弯的还是直的？”",
     "life": "读绘本时找一找镰刀。"},
    {"char": "烛", "pinyin": "zhú", "tone": "第二声",
     "sentence": "生日烛光亮晶晶。",
     "say": "点上小蜡烛，许个愿吧。",
     "chat": "“吹蜡烛前要先做什么呀？”",
     "life": "生日时数一数小蜡烛。"},
    {"char": "柴", "pinyin": "chái", "tone": "第二声",
     "sentence": "火柴棒堆成小山。",
     "say": "红头的小木棒，就是火柴。",
     "chat": "“火柴头是什么颜色的呀？”",
     "life": "告诉他火柴危险，大人才能用。"},
]


# ---------- 插画 ----------
def art_jian():
    """剪：圆头安全剪刀剪绿纸条，剪下的纸片飘落。"""
    g = ground()
    g += E(360, 442, 200, 14, INK, 0.08)
    # 绿纸条（左端完整，右端进剪刀口）
    g += P("M 58 268 Q 150 250 248 262 L 262 318 Q 150 332 58 316 Z", PAPER)
    g += P("M 96 282 Q 170 268 232 276", stroke=PAPER_D, w=6, opacity=0.7)
    # 剪下的纸片（飘落）
    g += f'<g transform="rotate(-24 322 396)">'
    g += PG([(292, 380), (352, 366), (368, 404), (308, 418)], PAPER)
    g += "</g>"
    g += P("M 318 344 Q 312 356 318 366", stroke=STEEL_D, w=5)
    # 剪刀（刃朝左）
    g += P("M 400 288 L 276 210 Q 256 198 266 182 Q 276 168 296 182 L 414 268 Z", STEEL)
    g += P("M 400 306 L 286 368 Q 266 378 256 362 Q 248 346 268 338 L 414 286 Z", STEEL)
    g += P("M 282 200 L 396 276", stroke="#fdfdfa", w=6, opacity=0.8)
    g += P("M 280 360 L 396 296", stroke="#fdfdfa", w=6, opacity=0.8)
    # 轴与柄
    g += L(402, 292, 508, 244, STEEL_D, 24)
    g += L(402, 302, 514, 336, STEEL_D, 24)
    g += C(540, 238, 47, REDH)
    g += C(540, 238, 26, "#fdf8ec")
    g += C(554, 342, 47, REDH)
    g += C(554, 342, 26, "#fdf8ec")
    g += C(402, 297, 15, "#9aa0a6")
    g += C(402, 297, 6, "#6f767c")
    return g


def art_chui():
    """锤：木柄铁锤正敲木板上的钉子，带敲击动势线。"""
    g = ground()
    g += E(380, 448, 210, 12, INK, 0.08)
    # 木板
    g += R(180, 396, 420, 44, 16, WOOD)
    g += P("M 210 416 Q 380 424 566 414", stroke="#b57b44", w=5)
    # 钉子（半入板）
    g += R(352, 348, 14, 52, 6, STEEL)
    g += E(359, 348, 22, 8, "#9aa0a6")
    # 锤子（斜置敲下）
    g += f'<g transform="rotate(-16 400 292)">'
    g += R(384, 130, 34, 158, 15, "#e8a13c")
    g += R(300, 258, 202, 62, 26, "#9aa0a6")
    g += R(300, 258, 30, 62, 12, "#7c8288")
    g += R(316, 264, 150, 14, 7, "#c3c9cf")
    g += "</g>"
    # 动势线
    g += P("M 250 210 Q 232 240 244 272", stroke=STEEL_D, w=7)
    g += P("M 216 192 Q 192 232 208 276", stroke=STEEL_D, w=7)
    return g


def art_ding():
    """钉：木板上大小钉子特写，一根立起的大钉最醒目。"""
    g = ground()
    g += E(380, 446, 220, 12, INK, 0.08)
    # 木板
    g += R(170, 330, 420, 100, 20, WOOD)
    g += P("M 200 356 Q 380 366 560 354", stroke="#b57b44", w=5)
    g += P("M 210 396 Q 380 404 550 396", stroke="#b57b44", w=4)
    # 大钉（立在最前）
    g += R(314, 224, 32, 150, 12, STEEL)
    g += PG([(314, 370), (346, 370), (330, 400)], STEEL_D)
    g += E(330, 224, 46, 15, "#9aa0a6")
    g += E(330, 219, 46, 13, STEEL_D)
    g += L(322, 240, 322, 350, "#fdfdfa", 6)
    # 板上两根小钉
    g += R(424, 296, 13, 40, 6, STEEL)
    g += E(430, 296, 20, 7, "#9aa0a6")
    g += E(500, 336, 22, 8, "#9aa0a6")
    # 一根躺倒的钉
    g += R(540, 424, 118, 16, 8, STEEL)
    g += R(540, 419, 18, 26, 7, "#9aa0a6")
    return g


def art_suo():
    """锁：金色大挂锁扣在木搭扣上（去掉大块门板）。"""
    g = ground()
    g += E(400, 446, 160, 12, INK, 0.08)
    # 木搭扣底板
    g += R(268, 192, 224, 66, 18, WOOD)
    g += R(280, 200, 200, 20, 10, "#b57b44")
    g += C(292, 226, 8, "#8a5a33")
    g += C(468, 226, 8, "#8a5a33")
    g += R(306, 210, 148, 30, 15, STEEL_D)
    # 锁梁（穿过搭扣）
    g += P("M 348 268 L 348 212 A 62 62 0 0 1 472 212 L 472 268", stroke="#9aa0a6", w=40)
    # 锁体
    g += R(296, 258, 228, 188, 32, GOLD)
    g += R(296, 258, 228, 34, 17, "#f8d070")
    g += R(296, 398, 228, 48, 22, GOLD_D)
    g += C(410, 348, 24, "#8a5a33")
    g += PG([(388, 356), (432, 356), (410, 406)], "#8a5a33")
    g += P("M 322 280 Q 320 344 330 390", stroke="#f8d070", w=9, opacity=0.7)
    return g


def art_yao():
    """钥：银色大钥匙（大圆头大孔 + 粗杆 + 两枚大方齿），系红丝带蝴蝶结。"""
    g = ground()
    g += E(370, 446, 185, 13, INK, 0.08)
    key = wrap(
        # 钥匙头（大圆环）
        C(0, 0, 86, STEEL_D),
        C(0, 0, 79, STEEL),
        C(0, 0, 46, STEEL_D),
        C(0, 0, 34, "#fdf8ec"),
        P("M -54 -36 Q -32 -62 -4 -66", stroke="#fdfdfa", w=9, opacity=0.7),
        # 红丝带蝴蝶结
        P("M -10 -70 Q -52 -104 -80 -80 Q -88 -52 -32 -56 Z", THREAD),
        P("M 10 -70 Q 52 -104 80 -80 Q 88 -52 32 -56 Z", THREAD),
        C(0, -62, 16, THREAD),
        P("M -10 -50 Q -28 -24 -20 -2", stroke=THREAD, w=11),
        P("M 10 -50 Q 28 -24 20 -2", stroke=THREAD, w=11),
        # 钥匙杆与两枚大方齿
        R(-24, 68, 48, 178, 22, STEEL),
        R(24, 148, 70, 46, 15, STEEL),
        R(24, 208, 54, 38, 14, STEEL),
        L(-12, 90, -12, 232, "#fdfdfa", 8),
    )
    g += f'<g transform="rotate(-24 330 200) translate(330 200)">{key}</g>'
    return g


def art_shi():
    """匙：白瓷汤匙搭在青瓷汤碗沿上（避免平底锅既视感）。"""
    g = ground()
    g += E(380, 446, 180, 13, INK, 0.08)
    # 汤碗（配角）
    g += E(380, 434, 66, 10, "#5bb3a5")
    g += P("M 240 352 Q 250 424 380 428 Q 510 424 520 352 "
           "Q 450 336 380 338 Q 310 336 240 352 Z", "#7cc8bb")
    g += E(380, 352, 142, 26, "#5bb3a5")
    g += E(380, 353, 118, 19, "#f2a03c")
    g += P("M 320 354 Q 352 348 384 354", stroke="#f8c07a", w=5)
    # 汤匙（椭圆匙窝，斜搭碗沿）
    g += f'<g transform="rotate(-14 330 318)">'
    g += P("M 236 318 Q 236 252 330 246 Q 424 252 424 318 Q 424 380 330 384 "
           "Q 236 380 236 318 Z", "#fdfdfa")
    g += E(330, 318, 76, 54, "#eef2f5")
    g += E(330, 320, 62, 43, "#f2a03c")
    g += P("M 300 322 Q 330 314 360 322", stroke="#f8c07a", w=6)
    g += "</g>"
    g += f'<g transform="rotate(-26 416 296)">'
    g += R(408, 278, 244, 42, 21, "#fdfdfa")
    g += R(408, 306, 244, 14, 7, "#d8dee3")
    g += C(646, 299, 15, "#d8dee3")
    g += "</g>"
    # 热气
    g += P("M 262 244 Q 252 222 264 204", stroke="#eef2f5", w=7, opacity=0.85)
    g += P("M 470 234 Q 460 214 472 196", stroke="#eef2f5", w=7, opacity=0.85)
    return g


def art_ju():
    """锯：木柄锯锯圆木，木屑飞溅。"""
    g = ground()
    g += E(400, 448, 230, 12, INK, 0.08)
    # 锯条（斜置，尖端插入木头）
    teeth = [(252, 238)]
    x = 252
    while x < 552:
        teeth += [(x, 264), (x + 14, 288)]
        x += 28
    teeth += [(566, 262), (566, 214), (252, 214)]
    g += PG(teeth, STEEL)
    g += L(252, 224, 566, 224, STEEL_D, 6)
    g += f'<g transform="rotate(-6 610 236)">'
    g += R(560, 196, 104, 76, 26, WOODH)
    g += R(586, 214, 52, 40, 17, "#fdf8ec")
    g += "</g>"
    # 圆木（盖住锯条尖端）
    g += R(150, 330, 400, 104, 44, "#b57b44")
    g += E(552, 382, 36, 52, "#e9b97e")
    g += C(552, 382, 15, "#c89058")
    g += P("M 190 356 Q 340 348 470 358", stroke="#8a5a33", w=5, opacity=0.6)
    g += R(240, 320, 64, 18, 9, "#6f4e33")
    # 木屑
    g += C(330, 312, 7, "#e9c88f")
    g += C(362, 300, 5, "#e9c88f")
    g += C(300, 302, 4, "#e9c88f")
    return g


def art_fu():
    """斧：红柄斧劈进木桩（大斧头 + 裂口），旁边是劈开的木段。"""
    g = ground()
    g += E(400, 448, 230, 12, INK, 0.08)
    # 木桩
    g += R(252, 336, 256, 104, 22, "#b57b44")
    g += P("M 282 352 Q 274 386 284 416", stroke="#8a5a33", w=5, opacity=0.6)
    g += P("M 486 350 Q 494 384 484 414", stroke="#8a5a33", w=5, opacity=0.6)
    g += E(380, 336, 128, 30, "#e9b97e")
    g += E(380, 336, 86, 20, "#dda775")
    g += E(380, 336, 46, 11, "#e9b97e")
    # 斧柄（斜上）
    g += f'<g transform="rotate(38 452 236)">'
    g += R(430, 66, 44, 210, 20, REDH)
    g += R(437, 72, 13, 198, 7, "#f2907a")
    g += "</g>"
    # 劈入木桩的裂口
    g += f'<g transform="rotate(14 448 326)">'
    g += R(406, 318, 88, 16, 8, "#8a5a33")
    g += "</g>"
    # 斧头（大，刃朝左下劈入）
    g += P("M 352 290 L 470 250 L 512 334 L 394 370 Z", STEEL)
    g += P("M 356 294 L 398 364", stroke="#fdfdfa", w=9)
    g += R(470, 250, 44, 88, 16, STEEL_D)
    # 劈开的木段（带平面）
    g += R(150, 410, 120, 38, 15, WOODH)
    g += PG([(158, 410), (262, 410), (250, 394), (172, 394)], "#e9b97e")
    g += R(462, 414, 116, 36, 15, WOODH)
    g += PG([(470, 414), (570, 414), (558, 398), (482, 398)], "#e9b97e")
    g += R(548, 332, 58, 112, 20, WOODH)
    g += E(577, 334, 29, 12, "#e9b97e")
    g += C(577, 334, 11, "#c89058")
    return g


def art_chan():
    """铲：雪铲斜插进雪堆正铲雪（铲尖埋入雪里），长柄 D 把。"""
    g = ground()
    g += E(360, 446, 240, 13, INK, 0.08)
    # 雪堆
    g += E(400, 424, 180, 42, WHITE)
    g += C(340, 396, 42, WHITE)
    g += C(420, 384, 48, WHITE)
    g += C(492, 398, 38, WHITE)
    # 雪花
    g += C(600, 210, 8, WHITE)
    g += C(644, 252, 6, WHITE, 0.9)
    g += C(180, 250, 7, WHITE, 0.9)
    # 铲（斜插雪堆）
    g += f'<g transform="rotate(-38 430 330)">'
    g += L(430, 250, 580, 90, WOODH, 26)
    g += f'<g transform="rotate(43 580 90)">'
    g += R(528, 74, 104, 32, 16, WOODH)
    g += R(558, 104, 46, 12, 6, "#a9743f")
    g += "</g>"
    g += R(400, 246, 60, 28, 12, "#3e9486")
    g += P("M 345 274 L 515 274 Q 530 276 528 292 Q 522 354 490 396 "
           "Q 460 430 430 430 Q 400 430 370 396 Q 338 354 332 292 Q 330 276 345 274 Z", "#4fae9f")
    g += P("M 500 284 Q 494 348 466 390 Q 448 414 424 424 Q 462 414 482 382 "
           "Q 508 344 514 286 Z", "#3e9486")
    g += E(430, 356, 42, 26, WHITE, 0.85)
    g += "</g>"
    # 铲尖前的雪盖住铲口下缘
    g += E(420, 416, 120, 34, WHITE)
    g += C(470, 402, 30, WHITE)
    return g


def art_la():
    """蜡：三支蜡笔伏在画纸上，纸上画着太阳。"""
    g = ground()
    g += E(380, 444, 220, 13, INK, 0.08)
    # 画纸
    g += f'<g transform="rotate(-7 560 380)">'
    g += R(468, 296, 190, 158, 12, "#fdfdfa")
    g += C(560, 366, 34, "#f7ae35")
    for i in range(8):
        a = i * math.pi / 4
        g += L(560 + 44 * math.cos(a), 366 + 44 * math.sin(a),
               560 + 60 * math.cos(a), 366 + 60 * math.sin(a), "#f7ae35", 7)
    g += P("M 480 440 Q 520 428 560 438 Q 604 448 646 438", stroke=PAPER, w=7)
    g += "</g>"
    # 三支蜡笔（斜放，笔尖朝左上）
    for i, (col, col_d) in enumerate((("#f2b53c", "#d99a2b"), (REDH, "#d4552f"), ("#4fae9f", "#3e9486"))):
        g += f'<g transform="translate({272 + i * 54},{396 - i * 8}) rotate({-46 + i * 10})">'
        g += R(-24, -190, 48, 210, 12, col)
        g += R(-24, -110, 48, 46, 8, col_d)
        g += PG([(-24, -190), (24, -190), (0, -232)], col_d)
        g += C(0, -228, 11, col_d)
        g += "</g>"
    return g


def art_cheng():
    """秤：表盘台秤称两个橘子，刻度无数字。"""
    g = ground()
    g += E(380, 442, 190, 12, INK, 0.08)
    # 橘子
    g += C(338, 218, 42, ORANGE)
    g += C(324, 204, 10, "#fbb35a", 0.9)
    g += C(352, 176, 9, "#7fae70")
    g += C(424, 226, 37, ORANGE)
    g += C(412, 214, 9, "#fbb35a", 0.9)
    g += C(436, 188, 8, "#7fae70")
    # 秤盘
    g += R(226, 250, 308, 34, 16, "#c9bfa0")
    g += R(234, 250, 292, 14, 7, "#d9cfae")
    # 秤身
    g += PG([(252, 284), (508, 284), (536, 426), (224, 426)], "#f3ead4")
    g += R(224, 390, 312, 36, 18, "#4fae9f")
    # 表盘（刻度 + 指针）
    g += C(380, 356, 78, "#e3d5bd")
    g += C(380, 356, 68, "#fdfdfa")
    for i in range(7):
        a = math.radians(205 + i * 25)
        g += L(380 + 60 * math.cos(a), 356 - 60 * math.sin(a),
               380 + 47 * math.cos(a), 356 - 47 * math.sin(a), "#8a8f96", 5)
    g += L(380, 356, 336, 326, REDH, 8)
    g += C(380, 356, 9, "#d4552f")
    return g


def art_zhen():
    """针：大针（粗杆大针眼）引红线在布上缝扣子（缝纫场景）。"""
    g = ground()
    g += E(390, 448, 230, 12, INK, 0.08)
    # 布（配角）
    g += R(170, 336, 480, 118, 22, "#aee0f2")
    g += R(170, 430, 480, 24, 12, "#8ec4e8")
    for x in range(200, 620, 64):
        g += L(x, 366, x + 34, 366, "#fdfdfa", 6)
        g += L(x + 16, 402, x + 50, 402, "#fdfdfa", 6)
    # 扣子缝在布上
    g += C(238, 420, 44, BTN)
    g += C(238, 420, 33, "#5fc0b0")
    g += L(224, 406, 252, 434, THREAD, 6)
    g += L(252, 406, 224, 434, THREAD, 6)
    g += wrap(C(224, 406, 6, "#fdf8ec"), C(252, 406, 6, "#fdf8ec"),
              C(224, 434, 6, "#fdf8ec"), C(252, 434, 6, "#fdf8ec"))
    # 大针（斜指布面）
    g += f'<g transform="rotate(30 420 300)">'
    g += R(250, 280, 330, 40, 20, STEEL)
    g += R(234, 274, 28, 52, 13, STEEL_D)
    g += PG([(578, 280), (662, 299), (578, 320)], STEEL)
    g += E(298, 300, 15, 26, "#fdf8ec")
    g += L(262, 290, 560, 290, "#fdfdfa", 7)
    g += "</g>"
    # 红线（针眼 → 布上扣子）
    g += P("M 316 254 Q 280 320 246 384", stroke=THREAD, w=10)
    g += P("M 316 254 Q 336 276 322 292", stroke=THREAD, w=8)
    return g


def art_wang():
    """网：捕蝶网，蝴蝶正被兜在网口。"""
    g = ground()
    g += E(400, 444, 220, 13, INK, 0.08)
    # 网袋（深兜）
    g += P("M 224 180 Q 230 336 322 372 Q 426 394 404 206 "
           "Q 354 248 304 246 Q 254 242 224 180 Z", "#eef4f8", 0.92)
    g += P("M 244 234 Q 254 330 324 362", stroke="#cdd6db", w=3)
    g += P("M 282 242 Q 292 320 344 356", stroke="#cdd6db", w=3)
    g += P("M 324 250 Q 338 314 376 350", stroke="#cdd6db", w=3)
    g += P("M 366 224 Q 380 294 396 340", stroke="#cdd6db", w=3)
    # 大蝴蝶（兜在网口，翅膀压住网圈下缘）
    g += f'<g transform="rotate(-6 306 218)">'
    g += E(262, 186, 46, 33, "#f5a58c")
    g += E(350, 186, 46, 33, "#5fa8d8")
    g += E(268, 248, 33, 25, "#f8b7a0", 0.95)
    g += E(344, 248, 33, 25, "#8ec4e8", 0.95)
    g += wrap(C(254, 178, 9, WHITE, 0.9), C(358, 178, 9, WHITE, 0.9),
              C(272, 244, 7, WHITE, 0.8), C(340, 244, 7, WHITE, 0.8))
    g += E(306, 214, 17, 42, "#4a3226")
    g += P("M 296 178 Q 284 154 270 150", stroke="#4a3226", w=5)
    g += P("M 316 178 Q 328 154 342 150", stroke="#4a3226", w=5)
    g += "</g>"
    # 网圈（细一点）与网面
    g += C(300, 148, 88, "#9aa0a6")
    g += C(300, 148, 79, "#fdf8ec")
    for x in range(228, 380, 22):
        dy = math.sqrt(max(0.0, 79 ** 2 - (x - 300) ** 2))
        g += L(x, 148 - dy, x, 148 + dy, "#cdd6db", 2.5)
    for y in range(76, 228, 22):
        dx = math.sqrt(max(0.0, 79 ** 2 - (y - 148) ** 2))
        g += L(300 - dx, y, 300 + dx, y, "#cdd6db", 2.5)
    # 网柄
    g += L(374, 186, 656, 440, WOODH, 22)
    g += C(376, 184, 16, "#8a5a33")
    return g


def art_zhou():
    """帚：扫帚斜立，扫起落叶和尘土。"""
    g = ground()
    g += E(380, 444, 210, 13, INK, 0.08)
    # 落叶
    g += f'<g transform="rotate(-20 232 428)">'
    g += E(232, 428, 27, 11, "#e8663c")
    g += L(208, 428, 256, 428, "#c25a3a", 4)
    g += "</g>"
    g += f'<g transform="rotate(16 522 432)">'
    g += E(522, 432, 25, 10, "#9cc98a")
    g += L(500, 432, 544, 432, "#7fae70", 4)
    g += "</g>"
    g += P("M 176 414 Q 196 396 220 404", stroke="#d9cfae", w=6)
    g += P("M 556 420 Q 574 406 592 412", stroke="#d9cfae", w=5)
    # 扫帚
    g += f'<g transform="rotate(12 380 300)">'
    g += R(364, 72, 32, 234, 14, WOODH)
    g += R(370, 78, 10, 220, 5, "#e9b97e")
    g += PG([(338, 300), (422, 300), (478, 436), (282, 436)], "#e9b97e")
    g += PG([(332, 314), (428, 314), (434, 344), (326, 344)], REDH)
    g += PG([(324, 344), (436, 344), (444, 370), (316, 370)], "#d4552f")
    for i in range(9):
        xt = 340 + i * 17
        xb = 282 + i * 24.5
        g += L(xt, 370, xb, 434, "#d9a55c", 5)
    g += "</g>"
    return g


def art_chu():
    """锄：锄头翻松泥土，土堆旁冒出小苗。"""
    g = ground()
    g += E(400, 444, 230, 13, INK, 0.08)
    # 土堆
    g += E(400, 428, 145, 28, "#8a6a48")
    g += C(330, 414, 13, "#75573a")
    g += C(470, 412, 11, "#75573a")
    g += C(430, 434, 10, "#75573a")
    # 小苗
    g += P("M 528 428 Q 528 408 528 396", stroke="#6b9459", w=6)
    g += f'<g transform="rotate(-28 512 392)">'
    g += E(512, 392, 18, 10, "#7fae70")
    g += "</g>"
    g += f'<g transform="rotate(28 544 392)">'
    g += E(544, 392, 18, 10, "#7fae70")
    g += "</g>"
    # 锄
    g += f'<g transform="rotate(-28 420 300)">'
    g += R(404, 58, 34, 250, 16, WOODH)
    g += R(410, 64, 10, 236, 5, "#e9b97e")
    g += R(408, 302, 28, 38, 10, "#8a5a33")
    g += PG([(384, 336), (462, 330), (478, 398), (368, 404)], "#7c8288")
    g += P("M 368 404 L 478 398", stroke="#aeb6bd", w=6)
    g += "</g>"
    return g


def art_lian():
    """镰：大弯镰（主体）搭割麦捆，麦穗带芒。"""
    g = ground()
    g += E(400, 446, 220, 13, INK, 0.08)
    # 麦秆（右移让位给镰刀）
    tops = [(412, 258), (432, 236), (454, 228), (476, 234), (494, 250)]
    for tx, ty in tops:
        g += L(468, 430, tx, ty, WHEAT_D, 7)
    for tx, ty in tops:
        for k in range(6):
            gy = ty - 16 - k * 14
            s = 1 if k % 2 == 0 else -1
            g += E(tx + 10 * s, gy, 9, 14, WHEAT)
            g += E(tx - 10 * s, gy + 7, 9, 14, WHEAT)
        for k in range(3):
            g += L(tx, ty - 96, tx - 9 + k * 9, ty - 126, "#e9d8a6", 3)
    g += f'<g transform="rotate(-30 456 380)">'
    g += R(420, 368, 72, 24, 11, "#d4552f")
    g += "</g>"
    # 大镰刀（弯刃搭向麦捆）
    g += P("M 226 412 Q 208 250 356 202 Q 394 190 392 218 Q 294 268 284 400 "
           "Q 283 430 254 430 Q 228 430 226 412 Z", STEEL)
    g += P("M 284 396 Q 294 272 386 222", stroke="#c9cdd1", w=8)
    g += f'<g transform="rotate(18 298 420)">'
    g += R(240, 404, 116, 40, 19, WOODH)
    g += R(246, 410, 104, 11, 5, "#e9b97e")
    g += "</g>"
    return g


def art_zhu2():
    """烛：生日纸杯蛋糕上的一支粉白条纹蜡烛。"""
    g = ground()
    g += E(380, 448, 150, 12, INK, 0.08)
    # 光晕
    g += C(382, 132, 56, "#f9c95e", 0.28)
    # 火苗
    g += P("M 382 92 Q 410 130 382 160 Q 354 130 382 92 Z", "#f7ae35")
    g += P("M 382 116 Q 396 138 382 156 Q 368 138 382 116 Z", "#fbe8cf")
    # 蜡烛
    g += L(382, 160, 382, 178, "#4a3226", 5)
    g += R(356, 174, 52, 198, 16, "#f5a58c")
    g += L(358, 224, 406, 206, "#fdfdfa", 10)
    g += L(358, 284, 406, 266, "#fdfdfa", 10)
    g += L(358, 342, 406, 324, "#fdfdfa", 10)
    g += P("M 356 218 Q 346 240 356 254 Q 364 240 358 220 Z", "#f8c0ae")
    g += P("M 408 248 Q 418 268 408 284 Q 400 268 406 250 Z", "#f8c0ae")
    # 奶油
    g += P("M 296 398 Q 282 352 326 348 Q 334 318 380 322 Q 426 318 434 348 "
           "Q 478 352 464 398 Z", FROST)
    g += P("M 312 374 Q 344 388 380 382 Q 420 388 448 374", stroke="#f0e4d8", w=6)
    # 纸杯
    g += PG([(300, 398), (460, 398), (438, 458), (322, 458)], CUP)
    g += L(334, 402, 328, 454, "#8a5a33", 5)
    g += L(380, 402, 380, 456, "#8a5a33", 5)
    g += L(426, 402, 432, 454, "#8a5a33", 5)
    return g


def art_chai():
    """柴：红头火柴交错叠成小山（棒粗头大，只画火柴棒不画火）。"""
    g = ground()
    g += E(380, 444, 205, 16, INK, 0.09)

    def match(cx, cy, ang):
        return (f'<g transform="translate({cx},{cy}) rotate({ang})">'
                + R(-86, -8, 172, 16, 8, "#e9b97e")
                + L(-72, 0, 72, 0, "#f4d9ac", 5)
                + C(-74, 0, 13, REDH)
                + C(-78, -4, 4, "#f2907a")
                + "</g>")

    # 底层三根
    for cx, cy, ang in ((280, 428, 5), (472, 428, -6), (376, 434, 1)):
        g += match(cx, cy, ang)
    # 中层交错
    for cx, cy, ang in ((322, 400, 15), (434, 398, -13)):
        g += match(cx, cy, ang)
    # 上层与顶
    for cx, cy, ang in ((348, 372, -9), (412, 374, 10)):
        g += match(cx, cy, ang)
    g += match(380, 348, 2)
    # 两侧斜靠
    g += match(252, 420, 24)
    g += match(508, 418, -24)
    return g


def arts():
    return {
        "剪": art_jian(), "锤": art_chui(), "钉": art_ding(), "锁": art_suo(),
        "钥": art_yao(), "匙": art_shi(), "锯": art_ju(), "斧": art_fu(),
        "铲": art_chan(), "蜡": art_la(), "秤": art_cheng(), "针": art_zhen(),
        "网": art_wang(), "帚": art_zhou(), "锄": art_chu(), "镰": art_lian(),
        "烛": art_zhu2(), "柴": art_chai(),
    }


if __name__ == "__main__":
    LEGACY = set()
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "gongju":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"工具组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
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
