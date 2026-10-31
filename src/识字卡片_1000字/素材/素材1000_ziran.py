#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自然组新增 18 卡插画与文案（1000 字批次 B6）。

字表：岸波浪坡谷岛穴岭峰池泉崖原野沟湖溪湾
（前 15 字 天地山石田土火沙洞河海洋江气影贝 在 legacy ../识字卡片_素材_ziran.py，
 山/水 为种子卡，本文件不重复）。

与 legacy 错造型：legacy 是 天空太阳/绿地/灰石/格田/土堆铲子/火苗/沙丘桶/
绿坡兔洞/弯河/海浪沙滩/深海洋面/宽江行船/气球/影子/贝壳，本批全部换构图：
斜岸水线/满幅波纹带/卷头浪/斜坡小径/两山夹谷/水中央岛/土坡穴口/
连绵山岭/独峰雪顶/圆池石沿+小鸭/石缝涌泉/高耸岩壁/地平线平原/
野花草甸/深沟剖面/静湖远岸/蜿蜒小溪/月牙海湾。
自然景观层次感约定（主控硬规则）：湖溪湾=水面+岸、泉=石缝冒水、崖=高耸岩壁、
波=波浪弧线、原野=地平线+草、岛=水中央小山、穴=山体洞口、岭峰=连绵山/独峰、
沟=深沟、坡=斜坡小径。同组邻居卡轮廓+主色错开。
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
LEAF_D, LEAF_DD = "#5e8f52", "#4a7a3e"
SEA, SEA_M, SEA_L = "#4a97c9", "#5fa8d8", "#79c2e6"      # 水三层
SKIN_W = "#a5d9f0"                                        # 浅水/高光
ROCK, ROCK_D, ROCK_L = "#a3927e", "#8a7a68", "#b8a892"    # 崖壁岩层
ROCK_G, ROCK_GD = "#9aa1aa", "#8a929c"                    # 灰石（泉/池沿用石族）
EARTH, EARTH_D, EARTH_L = "#8a6242", "#7a5236", "#a9744a" # 沟剖面土层
SAND = "#f2ddb0"
FIELD, FIELD_L, FIELD_D = "#9cc98a", "#a9d49a", "#8abc78" # 草地三层
MEADOW, MEADOW_D = "#8abc78", "#6a9a5c"                   # 野草甸
SNOW = "#fdfdfa"
PATH_C, PATH_D = "#e9d3a8", "#d9bd8a"


GROUP_CARDS = [
    {"char": "岸", "pinyin": "àn", "tone": "第四声",
     "sentence": "小鱼游到岸边了。",
     "say": "水和陆地相接的地方就是岸。",
     "chat": "“岸的这边是水，那边是什么？”",
     "life": "到河边站一站，指指哪里是岸。"},
    {"char": "波", "pinyin": "bō", "tone": "第一声",
     "sentence": "湖面上波纹一圈圈。",
     "say": "风吹过水面，起了细细的波纹。",
     "chat": "“往水里丢颗小石子会怎么样？”",
     "life": "吹一吹盆里的水，看波纹散开。"},
    {"char": "浪", "pinyin": "làng", "tone": "第四声",
     "sentence": "大浪卷起白花花。",
     "say": "浪头卷起来，顶着白色的浪花。",
     "chat": "“大浪冲过来，你想做什么？”",
     "life": "在浴缸里推水，制造小浪花。"},
    {"char": "坡", "pinyin": "pō", "tone": "第一声",
     "sentence": "沿着坡路爬上小山。",
     "say": "斜斜的路是坡，一步比一步高。",
     "chat": "“上坡费劲还是下坡费劲？”",
     "life": "骑滑板车感受上坡和下坡。"},
    {"char": "谷", "pinyin": "gǔ", "tone": "第三声",
     "sentence": "小溪在山谷里流。",
     "say": "两座山中间低低的地方叫山谷。",
     "chat": "“山谷里住着谁？猜一猜。”",
     "life": "出游时对着山谷喊一喊，听回声。"},
    {"char": "岛", "pinyin": "dǎo", "tone": "第三声",
     "sentence": "海中央有一座小岛。",
     "say": "四面都是水，中间露出的陆地叫岛。",
     "chat": "“去小岛要坐什么过去？”",
     "life": "在地图上找一个岛。"},
    {"char": "穴", "pinyin": "xué", "tone": "第二声",
     "sentence": "土坡上藏着一个小穴。",
     "say": "黑黑的洞口就是穴，是小动物的家。",
     "chat": "“谁可能住在这个穴里？”",
     "life": "找找树下土坡上有没有小洞穴。"},
    {"char": "岭", "pinyin": "lǐng", "tone": "第三声",
     "sentence": "山岭一座连一座。",
     "say": "连在一起、起起伏伏的山叫山岭。",
     "chat": "“像不像趴着的一条大龙？”",
     "life": "翻看山景照片，找连绵的山岭。"},
    {"char": "峰", "pinyin": "fēng", "tone": "第一声",
     "sentence": "高峰顶上盖白雪。",
     "say": "又高又尖的山头叫山峰，山顶快碰到云了。",
     "chat": "“为什么峰顶会有雪？”",
     "life": "画一画你心中的最高峰。"},
    {"char": "池", "pinyin": "chí", "tone": "第二声",
     "sentence": "鸭子在池里游水。",
     "say": "小小的、圆圆的水塘叫池塘。",
     "chat": "“池塘里还能养什么？”",
     "life": "去公园池塘边数数小鸭。"},
    {"char": "泉", "pinyin": "quán", "tone": "第二声",
     "sentence": "石缝里涌出清泉。",
     "say": "泉水从石头缝里咕嘟咕嘟冒出来。",
     "chat": "“泉水摸上去凉凉的吗？”",
     "life": "接一杯矿泉水尝尝，它来自山泉。"},
    {"char": "崖", "pinyin": "yá", "tone": "第二声",
     "sentence": "高崖直直像堵墙。",
     "say": "又高又陡的岩石大墙壁叫山崖。",
     "chat": "“站在崖边往下看会害怕吗？”",
     "life": "看悬崖图片，说说它多高多陡。"},
    {"char": "原", "pinyin": "yuán", "tone": "第二声",
     "sentence": "草原平得像地毯。",
     "say": "又平又宽、一眼望不到边的是草原。",
     "chat": "“草原上会有哪些动物？”",
     "life": "躺在草坪上，看看天有多宽。"},
    {"char": "野", "pinyin": "yě", "tone": "第三声",
     "sentence": "野花开满山坡。",
     "say": "没人种也自己开的花，叫野花。",
     "chat": "“你见过哪些颜色的野花？”",
     "life": "散步时认一种野花，记住它。"},
    {"char": "沟", "pinyin": "gōu", "tone": "第一声",
     "sentence": "水沟里淌着细细的水。",
     "say": "地面上窄窄深深的槽是沟，水爱往沟里流。",
     "chat": "“雨水多的时候沟里会怎样？”",
     "life": "雨后看看路边水沟的水流向哪。"},
    {"char": "湖", "pinyin": "hú", "tone": "第二声",
     "sentence": "湖水静静的像镜子。",
     "say": "大大的、安安静静的水是湖。",
     "chat": "“湖水和河水谁更安静？”",
     "life": "去湖边放片树叶，看它漂。"},
    {"char": "溪", "pinyin": "xī", "tone": "第一声",
     "sentence": "溪水绕着石头流。",
     "say": "细细弯弯、叮叮咚咚的小流水是溪。",
     "chat": "“小溪唱起歌来像什么声音？”",
     "life": "踩踩浅浅的溪水，凉凉脚。"},
    {"char": "湾", "pinyin": "wān", "tone": "第一声",
     "sentence": "海湾弯弯像月牙。",
     "say": "水岸弯进去、像月牙一样的地方叫湾。",
     "chat": "“月亮湾的名字是怎么来的？”",
     "life": "用手臂围个小圈，演一演湾。"},
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
    """尖头叶：原点在叶柄，叶尖指向 +x。"""
    return P(f"M 0 0 Q {ln * 0.42} {-wd} {ln} 0 Q {ln * 0.42} {wd} 0 0 Z", fill)


def grass_tuft(x, y, s=1.0, col=LEAF_D):
    """一小丛草：三片尖叶。"""
    return (place(leaf(34 * s, 8 * s, col), x, y, -118)
            + place(leaf(40 * s, 9 * s, col), x + 4 * s, y, -90)
            + place(leaf(34 * s, 8 * s, col), x + 8 * s, y, -62))


# ---------- 各卡插画 ----------
def art_an():
    """岸：斜斜的绿岸探进水里，水线、沙滩、卵石画在交界上，水里一条小鱼。"""
    g = ground()
    g += P("M 760 480 L 760 262 Q 620 302 500 358 Q 400 404 330 452 L 326 480 Z", SEA)
    g += P("M 760 480 L 760 306 Q 644 340 544 386 Q 452 426 386 462 L 384 480 Z", SEA_M)
    g += P("M 0 480 L 0 214 Q 150 266 280 328 Q 362 368 424 424 L 428 480 Z", FIELD)
    g += P("M 0 480 L 0 262 Q 132 306 252 360 Q 328 394 384 442 L 386 480 Z", FIELD_L)
    g += P("M 268 334 Q 352 376 420 428 Q 386 444 344 450 Q 296 412 244 366 "
           "Q 254 348 268 334 Z", SAND)
    g += P("M 560 330 Q 630 302 700 272", stroke=SKIN_W, w=7)
    g += P("M 520 396 Q 590 368 660 340", stroke=SKIN_W, w=6)
    g += P("M 440 440 Q 500 416 560 392", stroke=SKIN_W, w=6)
    fish = (E(568, 428, 32, 17, "#f2b53c") + PG([(596, 428), (616, 416), (616, 440)], "#e8a13c")
            + C(552, 424, 3.6, INK))
    g += fish
    g += P("M 536 448 Q 566 454 596 448", stroke=SKIN_W, w=5)
    g += C(452, 460, 13, ROCK_G) + C(486, 470, 10, ROCK_GD) + C(420, 470, 9, ROCK_G)
    g += grass_tuft(150, 322, 1.1) + grass_tuft(88, 288, 0.9, LEAF_DD) + grass_tuft(224, 366, 1.0)
    g += place(leaf(60, 14, LEAF_D), 42, 244, -30)
    return g


def art_bo():
    """波：满幅水面，一层层波纹带 + 白色弧线。"""
    g = R(52, 128, 656, 300, 34, SEA)
    band1 = P("M 52 236 Q 116 208 180 236 Q 244 264 308 236 Q 372 208 436 236 "
              "Q 500 264 564 236 Q 628 208 692 236 L 708 236 L 708 428 L 52 428 Z", SEA_M)
    band2 = P("M 52 322 Q 116 296 180 322 Q 244 348 308 322 Q 372 296 436 322 "
              "Q 500 348 564 322 Q 628 296 692 322 L 708 322 L 708 428 L 52 428 Z", SEA_L)
    g += band1 + band2
    for i, yy in enumerate((188, 262, 344)):
        y0 = yy + (i % 2) * 8
        g += P(f"M 96 {y0} Q 140 {y0 - 22} 184 {y0} Q 228 {y0 + 22} 272 {y0}", stroke=SKIN_W, w=8)
        g += P(f"M 420 {y0 + 14} Q 464 {y0 - 8} 508 {y0 + 14} Q 552 {y0 + 36} 596 {y0 + 14}",
               stroke=SKIN_W, w=8)
        g += P(f"M 240 {y0 + 44} Q 280 {y0 + 24} 320 {y0 + 44}", stroke=SKIN_W, w=7)
    g += P("M 96 434 Q 380 448 668 434", stroke="#3d84b8", w=10)
    g += E(120, 452, 40, 9, SKIN_W, 0.55)
    return g


def art_lang():
    """浪：一个大浪卷头，顶着白色浪花和水珠。"""
    g = ground()
    g += P("M 0 480 L 0 372 Q 130 344 260 366 Q 420 392 560 372 Q 670 356 760 380 L 760 480 Z", SEA)
    wave = P("M 96 452 Q 108 300 226 224 Q 336 156 404 214 Q 446 254 414 300 "
             "Q 384 336 336 322 Q 380 366 470 452 Z", SEA_M)
    g += wave
    g += P("M 226 224 Q 300 172 372 206 Q 416 228 404 264", stroke=SKIN_W, w=16)
    for fx, fy, fr in [(240, 208, 16), (292, 186, 19), (346, 180, 15), (392, 204, 13), (414, 244, 11)]:
        g += C(fx, fy, fr, SNOW)
    for dx, dy, dr in [(430, 168, 9), (466, 208, 7), (356, 128, 8), (300, 116, 6), (250, 150, 7)]:
        g += C(dx, dy, dr, SKIN_W)
    g += P("M 500 420 Q 570 380 660 400 Q 710 412 740 444 L 740 460 Q 640 428 540 448 Z", SEA_L)
    g += P("M 520 452 Q 590 440 660 452", stroke=SKIN_W, w=6)
    g += P("M 120 430 Q 180 422 240 430", stroke=SKIN_W, w=6)
    return g


def art_po():
    """坡：斜斜的绿坡 + 一条盘上去的小路。"""
    g = ground()
    g += P("M 0 480 L 0 372 Q 200 330 380 274 Q 560 218 760 156 L 760 480 Z", FIELD)
    g += P("M 0 372 Q 200 330 380 274 Q 560 218 760 156", stroke=FIELD_L, w=18)
    g += P("M 336 474 Q 372 408 448 366 Q 528 322 592 292 Q 656 262 706 236",
           stroke=PATH_D, w=38)
    g += P("M 336 474 Q 372 408 448 366 Q 528 322 592 292 Q 656 262 706 236",
           stroke=PATH_C, w=24)
    g += P("M 300 340 Q 330 322 360 330", stroke=LEAF_DD, w=5)
    g += P("M 480 250 Q 514 234 546 244", stroke=LEAF_DD, w=5)
    g += grass_tuft(160, 360, 1.1) + grass_tuft(90, 400, 1.0, LEAF_DD)
    g += grass_tuft(600, 300, 1.0) + grass_tuft(680, 240, 0.9, LEAF_DD)
    g += C(700, 300, 13, ROCK_G) + C(230, 420, 11, ROCK_GD)
    g += E(380, 446, 90, 14, FIELD_D, 0.7)
    return g


def art_gu():
    """谷：两座大山夹出深谷，谷底草地上一条小溪流向眼前，尽头是矮峰。"""
    g = ground()
    # 谷底草地（远窄近宽的楔形）
    g += P("M 268 330 Q 380 296 492 330 L 640 480 L 120 480 Z", FIELD_L)
    # 谷底尽头的矮峰（压低，给中间豁口让位）
    g += P("M 300 336 Q 340 252 382 246 Q 424 252 464 336 Z", "#c4e0b4")
    g += P("M 236 344 Q 270 292 298 288 Q 320 292 338 344 Z", "#cfe6c0")
    # 两侧大山（高而陡，内壁加深色阴影）
    g += P("M -10 480 L -10 88 Q 96 56 176 152 L 336 480 Z", FIELD)
    g += P("M 176 152 L 336 480 L 268 480 Q 210 296 156 188 Z", FIELD_D)
    g += P("M 770 480 L 770 66 Q 664 40 586 140 L 424 480 Z", MEADOW_D)
    g += P("M 586 140 L 424 480 L 494 480 Q 554 296 606 180 Z", "#5a8550")
    # 山体高光与灌木
    g += P("M 56 152 Q 102 124 148 140", stroke=FIELD_L, w=9)
    g += P("M 648 122 Q 700 96 746 110", stroke="#8abc78", w=9)
    g += C(118, 252, 15, LEAF_DD) + C(646, 244, 17, LEAF_DD) + C(86, 336, 12, LEAF_DD)
    g += cloud_p(312, 118, 0.42)
    # 小溪：从矮峰脚下流向观者，越近越宽
    g += P("M 372 318 Q 356 384 332 480 L 468 480 Q 444 384 440 318 Z", SEA)
    g += P("M 382 326 Q 368 386 350 480 L 452 480 Q 434 386 430 326 Z", SKIN_W)
    g += P("M 362 430 Q 378 418 392 428 Q 408 440 428 426", stroke=WHITE, w=6, opacity=0.85)
    g += P("M 370 376 Q 384 366 398 374 Q 410 380 422 372", stroke=WHITE, w=5, opacity=0.8)
    # 谷底与山脚草丛
    g += grass_tuft(180, 452, 1.1) + grass_tuft(292, 424, 0.9)
    g += grass_tuft(566, 446, 1.1, LEAF_DD) + grass_tuft(498, 392, 0.9, LEAF_DD)
    g += grass_tuft(58, 430, 1.0)
    return g


def art_dao3():
    """岛：大水中央一座小山岛，沙环 + 棕榈树。"""
    g = ground()
    g += E(380, 322, 330, 122, SEA)
    g += E(380, 318, 292, 102, SEA_M)
    g += E(380, 314, 130, 38, SAND)
    g += P("M 268 314 Q 282 244 380 232 Q 478 244 492 314 Q 380 336 268 314 Z", FIELD)
    g += P("M 300 296 Q 330 258 380 252 Q 430 258 460 296 Q 380 312 300 296 Z", FIELD_L)
    g += P("M 384 296 Q 376 250 392 208", stroke="#8a5a33", w=13)
    for rot in (200, 236, 270, 306, 342):
        g += place(leaf(94, 21, LEAF_DD), 392, 204, rot)
    g += C(384, 210, 7, "#8a5a33") + C(398, 214, 7, "#8a5a33")
    g += P("M 130 320 Q 180 308 230 318", stroke=SKIN_W, w=7)
    g += P("M 540 330 Q 600 320 650 330", stroke=SKIN_W, w=7)
    g += P("M 170 380 Q 240 392 310 384", stroke=SKIN_W, w=6)
    g += P("M 460 392 Q 530 400 600 390", stroke=SKIN_W, w=6)
    return g


def art_xue2():
    """穴：土坡上黑黑的穴口，洞边一圈石头。"""
    g = ground()
    g += P("M 110 448 Q 130 306 292 262 Q 420 228 530 276 Q 636 322 656 448 Z", EARTH)
    g += P("M 200 448 Q 218 340 320 306 Q 420 276 512 320 Q 580 358 596 448 Z", EARTH_L)
    g += P("M 196 300 Q 232 276 268 270", stroke=EARTH_D, w=6)
    g += P("M 420 282 Q 470 274 512 292", stroke=EARTH_D, w=6)
    g += P("M 300 448 Q 302 348 380 336 Q 458 348 460 448 Z", "#41301f")
    g += P("M 322 448 Q 324 372 380 362 Q 436 372 438 448 Z", "#241a10")
    g += C(288, 440, 16, ROCK_G) + C(264, 448, 11, ROCK_GD)
    g += C(472, 438, 17, ROCK_G) + C(500, 450, 10, ROCK_GD)
    g += grass_tuft(238, 288, 1.0) + grass_tuft(530, 306, 1.0, LEAF_DD)
    g += place(leaf(56, 12, FIELD_L), 210, 262, -24)
    g += C(560, 320, 9, FIELD_L, 0.9) + C(160, 330, 8, FIELD_L, 0.8)
    return g


def art_ling():
    """岭：山岭连绵，三层山脊一层压一层。"""
    g = ground()
    g += P("M 0 480 L 0 258 Q 96 208 196 250 Q 296 292 396 240 Q 500 186 600 240 "
           "Q 684 276 760 238 L 760 480 Z", FIELD_L)
    g += P("M 0 480 L 0 330 Q 120 278 240 330 Q 380 392 520 318 Q 640 258 760 322 "
           "L 760 480 Z", FIELD)
    g += P("M 0 480 L 0 402 Q 160 350 320 402 Q 480 454 760 378 L 760 480 Z", MEADOW)
    g += P("M 60 262 Q 120 230 180 258", stroke="#c4e0b4", w=7)
    g += P("M 420 250 Q 490 212 560 246", stroke="#c4e0b4", w=7)
    g += P("M 150 342 Q 240 306 330 344", stroke="#c4e0b4", w=6)
    g += grass_tuft(120, 428, 1.0, LEAF_DD) + grass_tuft(300, 452, 1.0)
    g += grass_tuft(540, 430, 1.0) + grass_tuft(660, 452, 0.9, LEAF_DD)
    return g


def art_feng():
    """峰：一座高尖峰顶着白雪，山脚两座小绿丘。"""
    g = ground()
    g += P("M 380 104 L 224 440 L 536 440 Z", ROCK_D)
    g += P("M 380 104 L 224 440 L 380 440 Z", ROCK)
    g += P("M 336 196 Q 358 218 380 198 Q 404 224 426 198 L 380 106 Z", SNOW)
    g += P("M 366 154 L 356 178", stroke=SNOW, w=7)
    g += P("M 396 148 L 404 172", stroke=SNOW, w=6)
    for yy in (260, 322, 384):
        g += L(298, yy, 470, yy, ROCK_L, 6)
    g += L(330, 300, 356, 262, ROCK_L, 5)
    g += E(196, 438, 148, 34, FIELD) + E(574, 438, 148, 34, MEADOW_D)
    g += E(380, 444, 120, 24, EARTH_L)
    g += cloud_p(596, 150, 0.62) + cloud_p(150, 210, 0.45)
    g += grass_tuft(130, 424, 0.9) + grass_tuft(630, 424, 0.9, LEAF_DD)
    return g


def art_chi():
    """池：圆圆的小池塘，石块砌沿，一只小鸭游水。"""
    g = ground()
    g += E(380, 392, 286, 86, FIELD_L)
    g += E(380, 396, 236, 66, SEA)
    g += E(380, 394, 204, 54, SEA_M)
    for sx, sy, sr in [(150, 396, 17), (196, 428, 14), (560, 388, 18), (516, 430, 14),
                       (270, 448, 12), (470, 452, 12), (330, 340, 12), (428, 342, 11)]:
        g += C(sx, sy, sr, ROCK_G) + C(sx - 3, sy - 3, sr * 0.6, ROCK_L)
    duck = (E(312, 366, 44, 27, SNOW) + E(306, 364, 30, 16, "#e0dad0")
            + C(344, 344, 19, SNOW)
            + PG([(361, 340), (378, 346), (361, 352)], "#f2b53c")
            + C(349, 339, 3.4, INK))
    g += duck
    g += P("M 254 390 Q 286 384 318 390", stroke=SKIN_W, w=6)
    g += P("M 360 396 Q 392 390 424 396", stroke=SKIN_W, w=6)
    g += P("M 430 366 Q 458 360 486 366", stroke=SKIN_W, w=5)
    g += grass_tuft(116, 350, 1.0) + grass_tuft(636, 344, 1.0, LEAF_DD)
    return g


def art_quan():
    """泉：石堆石缝里涌出水，流进小水潭。"""
    g = ground()
    g += E(430, 418, 250, 44, SEA)
    g += E(452, 414, 214, 34, SEA_M)
    g += E(372, 286, 116, 86, ROCK_G)
    g += E(356, 278, 104, 76, ROCK_L)
    g += E(510, 330, 96, 64, ROCK_GD)
    g += E(258, 342, 76, 52, ROCK_GD)
    g += E(268, 336, 64, 42, ROCK_G)
    g += P("M 386 300 Q 410 292 434 302 L 440 330 L 380 334 Z", "#5a4a3a")
    g += P("M 396 322 Q 384 368 372 410 Q 366 428 356 438", stroke=SEA, w=28)
    g += P("M 400 326 Q 390 368 380 406 Q 374 424 364 436", stroke=SKIN_W, w=12)
    for dx, dy, dr in [(316, 306, 8), (348, 280, 7), (452, 356, 8), (300, 366, 7)]:
        g += C(dx, dy, dr, SKIN_W)
    g += P("M 320 428 Q 360 420 400 428", stroke=SKIN_W, w=6)
    g += P("M 480 424 Q 520 418 560 424", stroke=SKIN_W, w=6)
    g += grass_tuft(150, 440, 1.0) + grass_tuft(620, 446, 1.0, LEAF_DD)
    return g


def art_ya():
    """崖：一面高耸的岩壁，一层层岩层清晰可见。"""
    g = ground()
    g += P("M 420 480 L 420 116 Q 428 76 478 68 L 690 68 Q 736 76 738 128 L 738 480 Z", ROCK)
    g += P("M 420 480 L 420 116 Q 428 76 478 68 L 500 68 Q 460 90 456 140 L 452 480 Z", ROCK_L)
    for yy, wgt in [(140, 8), (196, 7), (252, 9), (310, 7), (368, 8), (426, 7)]:
        g += L(448, yy, 726, yy, ROCK_D, wgt)
    g += L(520, 196, 560, 168, ROCK_D, 6)
    g += L(600, 310, 640, 282, ROCK_D, 6)
    g += E(580, 68, 150, 16, FIELD) + E(700, 70, 60, 12, FIELD_L)
    g += grass_tuft(500, 64, 1.0) + grass_tuft(650, 60, 1.0, LEAF_DD)
    g += C(384, 452, 15, ROCK_G) + C(350, 458, 10, ROCK_GD)
    g += cloud_p(200, 170, 0.55)
    g += grass_tuft(250, 440, 1.0)
    return g


def art_yuan():
    """原：平平的原野，一条清晰的地平线。"""
    g = ground()
    g += R(0, 74, 760, 160, 30, "#dff0f8")
    g += P("M 0 480 L 0 246 Q 200 232 380 240 Q 560 246 760 234 L 760 480 Z", FIELD)
    g += P("M 0 246 Q 200 232 380 240 Q 560 246 760 234", stroke=FIELD_D, w=9)
    for yy in (300, 352, 406):
        for xx in range(120, 700, 150):
            g += L(xx, yy, xx + 66, yy, FIELD_L, 7)
    g += grass_tuft(170, 330, 1.0) + grass_tuft(470, 356, 1.0, LEAF_DD)
    g += grass_tuft(640, 316, 0.9) + grass_tuft(300, 416, 1.0)
    g += R(596, 196, 12, 46, 5, "#8a5a33") + C(602, 178, 34, LEAF_DD) + C(586, 190, 22, FIELD_L)
    g += E(602, 246, 40, 8, FIELD_D, 0.7)
    return g


def art_ye():
    """野：起伏的野地，野花、高草和一只小蝴蝶。"""
    g = ground()
    g += P("M 0 480 L 0 296 Q 140 254 300 292 Q 460 330 760 268 L 760 480 Z", MEADOW)
    g += P("M 0 296 Q 140 254 300 292 Q 460 330 760 268", stroke=FIELD_L, w=12)
    for cx, cy, rr, col in [(300, 330, 17, "#f2b53c"), (480, 352, 14, "#f0876f"),
                            (566, 318, 12, "#c79ad6"), (210, 366, 13, "#f2b53c")]:
        g += flower5(cx, cy, rr, col, "#f7ae35")
    for cx, cy in [(300, 330), (480, 352), (566, 318), (210, 366)]:
        g += L(cx, cy + 16, cx, cy + 44, LEAF_D, 5)
    g += grass_tuft(360, 420, 1.3, LEAF_DD) + grass_tuft(150, 428, 1.2)
    g += grass_tuft(610, 430, 1.3, LEAF_DD) + grass_tuft(450, 452, 1.1)
    g += place(leaf(52, 11, LEAF_DD), 700, 330, -40)
    g += place(leaf(52, 11, LEAF_DD), 700, 330, -140)
    g += E(700, 330, 5, 12, INK)
    g += C(692, 320, 10, "#f2b53c", 0.95) + C(708, 320, 10, "#f2b53c", 0.95)
    return g


def art_gou():
    """沟：剖开的深沟，两岸夹着窄窄的水。"""
    g = ground()
    g += P("M 0 480 L 0 292 Q 150 292 286 322 L 352 336 Q 372 388 372 448 L 372 480 Z", EARTH)
    g += P("M 760 480 L 760 274 Q 610 278 474 312 L 408 328 Q 388 388 388 448 L 388 480 Z", EARTH_D)
    g += P("M 40 292 Q 160 296 270 320", stroke=LEAF_DD, w=10)
    g += P("M 480 310 Q 600 292 720 280", stroke=LEAF_DD, w=10)
    g += grass_tuft(120, 292, 1.1) + grass_tuft(230, 314, 1.0)
    g += grass_tuft(540, 300, 1.0, LEAF_DD) + grass_tuft(680, 282, 1.0, LEAF_DD)
    g += P("M 356 462 Q 380 452 404 462", stroke=SEA, w=16)
    g += P("M 366 462 Q 380 456 394 462", stroke=SKIN_W, w=7)
    for dx, dy, dr in [(200, 380, 7), (300, 430, 6), (560, 380, 7), (470, 436, 6)]:
        g += C(dx, dy, dr, "#6b4a33")
    return g


def art_hu():
    """湖：宽宽的静水，对岸小树，水面亮线。"""
    g = ground()
    g += P("M 30 336 Q 200 240 380 248 Q 560 254 730 336 Q 560 300 380 298 Q 200 300 30 336 Z", FIELD_L)
    g += E(380, 356, 336, 112, SEA)
    g += E(380, 352, 296, 92, SEA_M)
    for cx, cy, s in [(170, 296, 0.5), (250, 286, 0.42), (560, 292, 0.5), (640, 300, 0.42)]:
        g += tree_round(cx, cy, s, LEAF_DD, LEAF_D)
    g += P("M 120 356 Q 220 348 320 356", stroke=SKIN_W, w=7)
    g += P("M 440 384 Q 540 376 640 384", stroke=SKIN_W, w=7)
    g += P("M 200 414 Q 300 406 400 414", stroke=SKIN_W, w=6)
    g += E(380, 444, 300, 26, SAND)
    g += grass_tuft(96, 346, 1.0) + grass_tuft(672, 350, 1.0, LEAF_DD)
    return g


def art_xi():
    """溪：窄窄的溪水弯弯地绕过石头，两岸青草。"""
    g = ground()
    g += R(0, 150, 760, 300, 40, FIELD)
    # 弯弯的溪水（S 形，从右上流向左下）
    g += P("M 790 196 Q 630 208 540 258 Q 450 308 350 316 Q 250 324 170 380 "
           "Q 100 430 -30 448", stroke=SEA, w=46)
    g += P("M 790 202 Q 638 214 548 262 Q 458 310 354 318 Q 256 326 178 380 "
           "Q 108 428 -30 444", stroke=SKIN_W, w=16)
    # 溪里的石头（水绕着石头流，石头下游带白色水纹）
    for sx, sy, sr in [(620, 226, 14), (505, 272, 12), (400, 312, 14),
                       (300, 328, 11), (205, 366, 13), (112, 420, 9)]:
        g += C(sx, sy, sr, ROCK_G) + C(sx - 3, sy - 3, sr * 0.6, ROCK_L)
    g += P("M 596 244 Q 620 254 644 244", stroke=WHITE, w=5, opacity=0.9)
    g += P("M 380 332 Q 402 342 424 332", stroke=WHITE, w=5, opacity=0.9)
    g += P("M 184 384 Q 206 394 228 384", stroke=WHITE, w=4, opacity=0.85)
    # 岸边石头与青草
    g += C(700, 160, 11, ROCK_GD) + C(240, 258, 10, ROCK_GD) + C(475, 398, 10, ROCK_L)
    g += C(668, 392, 9, ROCK_G)
    g += grass_tuft(120, 300, 1.1) + grass_tuft(300, 252, 1.0, LEAF_DD)
    g += grass_tuft(560, 334, 1.1) + grass_tuft(680, 270, 1.0)
    g += grass_tuft(60, 320, 1.0) + grass_tuft(430, 430, 1.0, LEAF_DD)
    g += P("M 540 208 Q 620 194 700 204", stroke=FIELD_L, w=8)
    return g


def art_wan():
    """湾：两侧山脚抱着一弯月牙形的海水，湾头嵌一道月牙形沙滩。"""
    g = ground()
    # 海（先铺满下半，湾口开在上方的岸边）
    g += R(0, 236, 760, 244, 0, SEA)
    # 上方的岸：两侧山脚探进海里，中间弯进一道宽宽的月牙湾
    g += P("M 0 480 L 0 118 Q 190 104 380 112 Q 570 104 760 118 L 760 252 "
           "Q 690 272 630 310 Q 600 330 585 342 Q 520 306 460 276 Q 415 256 380 254 "
           "Q 345 256 300 276 Q 240 306 175 342 Q 160 330 130 310 Q 70 272 0 252 Z", FIELD)
    # 湾头浅水与月牙形沙滩
    g += P("M 196 336 Q 290 292 380 268 Q 470 292 564 336", stroke=SKIN_W, w=13, opacity=0.8)
    g += P("M 188 330 Q 285 284 380 260 Q 475 284 572 330", stroke=SAND, w=24)
    # 跟着湾岸弯的波纹
    g += P("M 170 392 Q 380 344 590 392", stroke=SKIN_W, w=7)
    g += P("M 100 444 Q 380 396 660 444", stroke=SKIN_W, w=7)
    g += P("M 180 468 Q 380 444 580 468", stroke=SKIN_W, w=6)
    # 两侧山脚的草与灌木
    g += P("M 40 180 Q 92 164 146 178", stroke=FIELD_L, w=9)
    g += P("M 614 174 Q 670 158 726 174", stroke=FIELD_L, w=9)
    g += C(150, 236, 13, LEAF_DD) + C(610, 230, 15, LEAF_DD)
    g += C(320, 152, 10, LEAF_DD) + C(450, 148, 11, LEAF_DD)
    g += grass_tuft(90, 290, 1.0) + grass_tuft(676, 284, 1.0, LEAF_DD)
    g += grass_tuft(230, 150, 0.9) + grass_tuft(540, 146, 0.9, LEAF_DD)
    return g


def arts():
    return {
        "岸": art_an(), "波": art_bo(), "浪": art_lang(), "坡": art_po(),
        "谷": art_gu(), "岛": art_dao3(), "穴": art_xue2(), "岭": art_ling(),
        "峰": art_feng(), "池": art_chi(), "泉": art_quan(), "崖": art_ya(),
        "原": art_yuan(), "野": art_ye(), "沟": art_gou(), "湖": art_hu(),
        "溪": art_xi(), "湾": art_wan(),
    }


if __name__ == "__main__":
    LEGACY15 = {"天", "地", "山", "石", "田", "土", "火", "沙", "洞",
                "河", "海", "洋", "江", "气", "影", "贝"}
    SEEDS2 = {"山", "水"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "ziran":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY15 and c not in SEEDS2]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"自然组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，种子字 {sorted(SEEDS2)}）")
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
