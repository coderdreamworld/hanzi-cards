#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""形容组新增 27 卡插画与文案（1000 字批次 B12）。

字表：静吵闹整齐乱旧累困乖勇健暖凉净丑密温烫扁紧慢熟敢矮坏假
（前 12 字 好新快美响＋丽真老久全最活 在 legacy ../识字卡片_素材_xingrong.py）。

全部用「状态瞬间或对比物件」表达，与 legacy 12 卡及已产对比卡错造型：
静=夜色里摇篮睡猫+圆月、吵=两鸟对吵声波相撞、闹=红闹钟大响+kid捂耳、
整=四本书竖排上架、齐=四支蜡笔尖头排齐、乱=玩具箱打翻撒一地、旧=打补丁旧熊、
累=瘫坐擦汗头顶毛巾、困=伸懒腰打大哈欠、乖=坐好抱小熊、勇=高台披风挺胸、
健=单手举小哑铃、暖=双手戴红手套晒太阳、凉=冰淇淋凉风、净=白盘闪光带水珠、
丑=友好丑小鸭、密=层层叠叠密林、温=玻璃杯温水轻汽+暖光、烫=冒白汽热汤+kid吹、
扁=大石压扁球、紧=拉紧大运动鞋鞋带+蝴蝶结、慢=乌龟蜗牛并排爬、熟=熟透苹果落地、
敢=伸手摸小狗、矮=踮脚够不到高架子、坏=翻倒掉轮玩具车、假=真假两盆花对比。
同组邻居卡轮廓+主色错开（纯蓝底 kid 卡之间靠道具/姿势/朝向区分）。
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
NIGHT_SOFT = "#e4edf6"      # 静卡夜色（浅蓝灰，非 legacy 深夜）
CAT, CAT_D = "#f0b26a", "#d99447"          # 橘猫
BIRD_R, BIRD_B = "#e8663c", "#5fa8d8"      # 两只鸟
CRAYON_P, CRAYON_G = "#c5a8de", "#7fae70"  # 蜡笔紫/绿
BEAR, BEAR_L = "#b98a5e", "#d9c09a"        # 旧熊
BEAR2, BEAR2_L = "#d1a878", "#e8cba0"      # 乖的小熊（浅一档）
DUCK_G, DUCK_L = "#9aa5ad", "#c3cbd1"      # 丑小鸭灰
ROCK, ROCK_L = "#a3927e", "#b8a892"        # 石头
STEEL, STEEL_D = "#9aa1aa", "#7f8a92"      # 哑铃/金属
PLASTIC = "#f6a8c8"                         # 假花塑料粉


def sparkle(cx, cy, r, fill=SUN):
    """四角亮晶晶闪光。"""
    return (PG([(cx, cy - r), (cx + r * 0.26, cy), (cx, cy + r), (cx - r * 0.26, cy)], fill)
            + PG([(cx - r, cy), (cx, cy - r * 0.26), (cx + r, cy), (cx, cy + r * 0.26)], fill))


def sleepy_eyes(x, hcy, s, droop=False):
    """把 kid 的圆眼盖成闭眼/耷拉眼（画在 kid 之后）。"""
    ex, ey = 22 * s, hcy - 8 * s
    g = C(x - ex, ey, 13 * s, SKIN) + C(x + ex, ey, 13 * s, SKIN)
    if droop:   # 累：半闭下垂眼
        g += P(f"M {x-ex-12*s} {ey+1*s} Q {x-ex} {ey+8*s} {x-ex+12*s} {ey+1*s}", stroke=INK, w=5 * s)
        g += P(f"M {x+ex-12*s} {ey+1*s} Q {x+ex} {ey+8*s} {x+ex+12*s} {ey+1*s}", stroke=INK, w=5 * s)
    else:       # 困/睡：弯弯闭眼
        g += P(f"M {x-ex-11*s} {ey-2*s} Q {x-ex} {ey+7*s} {x-ex+11*s} {ey-2*s}", stroke=INK, w=5 * s)
        g += P(f"M {x+ex-11*s} {ey-2*s} Q {x+ex} {ey+7*s} {x+ex+11*s} {ey-2*s}", stroke=INK, w=5 * s)
    return g


def teddy(cx, cy, s, body=BEAR2, light=BEAR2_L):
    """小熊（坐姿正面），s=1 时头 r34。"""
    return wrap(
        C(cx - 27 * s, cy - 30 * s, 13 * s, body), C(cx + 27 * s, cy - 30 * s, 13 * s, body),
        E(cx - 27 * s, cy - 30 * s, 6.5 * s, 5 * s, light), E(cx + 27 * s, cy - 30 * s, 6.5 * s, 5 * s, light),
        E(cx, cy + 14 * s, 34 * s, 30 * s, body),                    # 身体
        E(cx - 20 * s, cy + 36 * s, 13 * s, 9 * s, body),            # 脚
        E(cx + 20 * s, cy + 36 * s, 13 * s, 9 * s, body),
        E(cx, cy + 16 * s, 18 * s, 13 * s, light),                   # 肚皮
        C(cx, cy - 8 * s, 24 * s, body),                             # 头
        E(cx, cy + 1 * s, 11 * s, 8 * s, light),                     # 口鼻
        C(cx, cy - 4 * s, 4.5 * s, INK),
        P(f"M {cx-5*s} {cy+5*s} Q {cx} {cy+9*s} {cx+5*s} {cy+5*s}", stroke=INK, w=3 * s),
        E(cx - 9 * s, cy - 14 * s, 4.5 * s, 6 * s, INK), E(cx + 9 * s, cy - 14 * s, 4.5 * s, 6 * s, INK),
        C(cx - 9 * s, cy - 16 * s, 1.6 * s, WHITE), C(cx + 9 * s, cy - 16 * s, 1.6 * s, WHITE),
        C(cx - 18 * s, cy - 2 * s, 5 * s, PINK, 0.7), C(cx + 18 * s, cy - 2 * s, 5 * s, PINK, 0.7))


# ---------- 各卡场景 ----------
def art_jing():
    """静：浅夜色里，橘猫蜷在摇篮中睡觉，右上一轮圆月。"""
    g = ground()
    g += R(70, 48, 620, 372, 36, NIGHT_SOFT)
    # 圆月（与 legacy 月牙卡区分）
    g += C(586, 142, 46, "#f7e9b0") + C(570, 128, 9, "#ecd489") + C(600, 158, 6, "#ecd489")
    g += C(552, 150, 5, "#ecd489")
    # 摇篮背沿
    g += R(196, 296, 368, 44, 22, WOOD_D)
    # 睡猫（蜷成团，头朝左）
    g += P("M 476 340 Q 514 312 492 290 Q 472 274 454 292", stroke=CAT, w=17)       # 尾巴卷
    g += E(400, 328, 88, 48, CAT)                                                    # 身体
    g += P("M 376 292 Q 400 282 424 292", stroke=CAT_D, w=7)
    g += P("M 424 286 Q 448 278 470 288", stroke=CAT_D, w=7)
    g += C(312, 300, 40, CAT)                                                        # 头
    g += PG([(282, 276), (294, 238), (318, 268)], CAT) + PG([(322, 264), (340, 236), (350, 270)], CAT)
    g += PG([(288, 269), (295, 248), (309, 264)], PINK) + PG([(327, 262), (339, 244), (346, 266)], PINK)
    g += P("M 294 302 Q 303 310 312 302", stroke=INK, w=5)                           # 闭眼
    g += P("M 320 302 Q 329 310 338 302", stroke=INK, w=5)
    g += P("M 308 320 Q 315 325 322 320", stroke=INK, w=3.5)                         # 小嘴
    g += L(274, 314, 252, 310, CAT_D, 3) + L(276, 326, 254, 328, CAT_D, 3)           # 胡须
    # 盖毯（盖住下半身）
    g += P("M 350 306 L 474 306 Q 504 344 482 400 L 350 400 Z", TEAL_L)
    g += P("M 372 306 L 372 400", stroke=TEAL, w=6)
    g += P("M 434 306 L 434 400", stroke=TEAL, w=6)
    # 摇篮前壁（编织纹理）+ 摇弧
    g += R(200, 356, 360, 78, 28, WOOD)
    g += R(200, 356, 360, 18, 9, WOOD_L)
    g += P("M 246 376 L 246 432", stroke=WOOD_D, w=6)
    g += P("M 316 376 L 316 432", stroke=WOOD_D, w=6)
    g += P("M 386 376 L 386 432", stroke=WOOD_D, w=6)
    g += P("M 456 376 L 456 432", stroke=WOOD_D, w=6)
    g += P("M 202 400 Q 380 416 558 400", stroke=WOOD_L, w=6)
    g += P("M 214 444 Q 380 478 546 444", stroke=WOOD_D, w=13)
    g += L(252, 436, 248, 448, WOOD_D, 8) + L(508, 436, 512, 448, WOOD_D, 8)
    return g


def art_chao():
    """吵：两只小鸟张大嘴对着吵，头顶声波撞在一起。"""
    g = ground()
    # 左鸟（红，朝右）
    g += f'<g transform="rotate(-4 270 340)">'
    g += PG([(226, 318), (188, 288), (210, 336)], RED_D)                             # 尾羽上翘
    g += PG([(222, 334), (180, 326), (206, 356)], RED_D)
    g += L(250, 396, 242, 436, YEL_D, 7) + L(296, 396, 304, 436, YEL_D, 7)
    g += E(250, 440, 12, 5, YEL_D) + E(310, 440, 12, 5, YEL_D)
    g += C(270, 340, 66, BIRD_R)
    g += E(270, 364, 38, 25, "#f2916c")
    g += f'<g transform="rotate(-34 240 318)">{E(240, 318, 24, 14, RED_D)}</g>'      # 翅膀翘起
    g += C(304, 320, 11, WHITE) + C(306, 320, 5.5, INK)
    g += P("M 288 298 Q 302 290 314 300", stroke=INK, w=6)                           # 皱眉
    g += PG([(292, 276), (302, 254), (314, 276)], RED_D)                             # 头顶竖毛
    g += PG([(344, 302), (400, 288), (352, 330)], YEL_D)                             # 大上喙
    g += PG([(346, 340), (398, 350), (350, 362)], YEL)                               # 大下喙
    g += drop(322, 372, 9, "#a5d9f0")
    g += "</g>"
    # 右鸟（蓝，朝左）
    g += f'<g transform="rotate(4 496 350)">'
    g += PG([(540, 328), (578, 298), (556, 346)], BLUE_D)
    g += PG([(544, 344), (586, 336), (560, 366)], BLUE_D)
    g += L(474, 406, 466, 442, YEL_D, 7) + L(518, 406, 526, 442, YEL_D, 7)
    g += E(460, 446, 12, 5, YEL_D) + E(532, 446, 12, 5, YEL_D)
    g += C(496, 350, 60, BIRD_B)
    g += E(496, 372, 34, 23, "#8cc3e8")
    g += f'<g transform="rotate(34 524 328)">{E(524, 328, 22, 13, BLUE_D)}</g>'
    g += C(462, 330, 10, WHITE) + C(460, 330, 5, INK)
    g += P("M 444 308 Q 456 300 468 308", stroke=INK, w=6)
    g += PG([(476, 288), (486, 266), (498, 288)], BLUE_D)
    g += PG([(424, 314), (368, 300), (416, 342)], YEL_D)
    g += PG([(422, 352), (370, 362), (418, 374)], YEL)
    g += drop(444, 382, 8, "#a5d9f0")
    g += "</g>"
    # 头顶声波（两串向中间撞）
    g += P("M 350 244 Q 368 224 394 220", stroke="#e8a13c", w=8)
    g += P("M 330 270 Q 344 254 362 248", stroke="#f2b53c", w=6)
    g += P("M 416 244 Q 398 224 372 220", stroke="#e8a13c", w=8)
    g += P("M 436 270 Q 422 254 404 248", stroke="#f2b53c", w=6)
    return g


def art_nao():
    """闹：红色闹钟摇铃大响，小朋友捂着耳朵。"""
    g = ground()
    clock = wrap(
        L(228, 396, 212, 438, RED_D, 13), L(302, 396, 318, 438, RED_D, 13),
        C(274, 214, 27, YEL), C(196, 250, 27, YEL),
        C(277, 217, 27, YEL_D, 0.35), C(199, 253, 27, YEL_D, 0.35),
        C(265, 316, 100, RED_D), C(258, 310, 98, RED),
        C(258, 310, 76, WHITE),
        C(258, 254, 5, INK), C(314, 310, 5, INK), C(258, 366, 5, INK), C(202, 310, 5, INK),
        L(258, 310, 258, 264, INK, 8), L(258, 310, 290, 296, INK, 8), C(258, 310, 8, RED_D),
        R(216, 336, 84, 10, 5, "#f4a9a0"),
    )
    g += f'<g transform="rotate(-7 258 316)">{clock}</g>'
    # 铃上震波
    g += P("M 150 200 Q 138 214 146 232", stroke=YEL_D, w=6)
    g += P("M 128 186 Q 108 210 122 240", stroke=YEL_D, w=6)
    g += P("M 336 190 Q 350 202 344 222", stroke=YEL_D, w=6)
    g += P("M 360 172 Q 382 194 372 226", stroke=YEL_D, w=6)
    # 小朋友捂耳朵（双手举到耳边，身体后仰）
    g += f'<g transform="rotate(8 560 436)">'
    g += kid(560, 436, s=0.8, pose="stand", arms="up", face="o", shirt=TEAL, look=(-1, 0))
    g += "</g>"
    return g


def art_zheng():
    """整：四本书竖直排在木架上，底部对齐。"""
    g = ground()
    g += L(200, 430, 200, 452, WOOD_D, 12) + L(560, 430, 560, 452, WOOD_D, 12)
    g += R(168, 398, 424, 32, 10, WOOD)
    g += R(168, 398, 424, 12, 6, WOOD_L)
    books = [(196, 54, 158, RED, "#f2916c"), (262, 46, 176, TEAL, TEAL_L),
             (320, 58, 150, YEL, SUN_L), (390, 48, 168, BLUE, "#8cc3e8"),
             (450, 56, 146, GREEN, GREEN_L)]
    for x, w, h, c, cl in books:
        g += R(x, 398 - h, w, h, 8, c)
        g += R(x + 8, 398 - h + 14, 10, h - 28, 5, cl)
        g += R(x + w - 20, 398 - h + 14, 10, h - 28, 5, cl)
    # 架上的小相框（摆整齐的一员）
    g += R(522, 340, 56, 58, 8, WOOD_L)
    g += R(532, 350, 36, 38, 5, "#bfe3f5")
    return g


def art_qi2():
    """齐：四支蜡笔尖头朝上、笔尾对齐站一排。"""
    g = ground()
    cols = [(268, CRAYON_G, "#a3cc96"), (340, "#f0876f", "#f6b3a4"),
            (412, YEL, SUN_L), (484, CRAYON_P, "#d9c3ea")]
    for cx, c, cl in cols:
        g += PG([(cx - 15, 250), (cx + 15, 250), (cx, 216)], c)          # 笔尖
        g += R(cx - 19, 250, 38, 168, 10, c)
        g += R(cx - 19, 296, 38, 26, 6, cl)                              # 纸箍
        g += R(cx - 19, 404, 38, 14, 7, cl)                              # 笔尾
    g += L(236, 424, 524, 424, TEAL_L, 6)                                # 对齐基准线
    return g


def art_luan():
    """乱：玩具箱打翻，玩具撒了一地。"""
    g = ground()
    g += f'<g transform="rotate(-30 240 290)">{box(240, 236, 214, 120, open_top=True)}</g>'
    g += f'<g transform="rotate(24 342 320)">{R(320, 298, 44, 44, 8, GREEN) + R(320, 298, 44, 12, 6, GREEN_L)}</g>'
    g += ball(484, 396, 42, RED, RED_D, "#f2916c")
    g += f'<g transform="rotate(16 388 420)">{R(360, 396, 52, 50, 9, YEL) + R(360, 396, 52, 14, 7, SUN_L)}</g>'
    g += f'<g transform="rotate(-16 306 432)">{R(280, 408, 52, 50, 9, BLUE) + R(280, 408, 52, 14, 7, "#8cc3e8")}</g>'
    g += f'<g transform="rotate(8 596 424)">'
    g += R(544, 400, 104, 48, 16, TEAL) + R(572, 378, 48, 28, 9, TEAL_D)   # 小玩具车
    g += C(568, 450, 15, INK) + C(624, 450, 15, INK) + C(568, 450, 6, STEEL) + C(624, 450, 6, STEEL)
    g += "</g>"
    g += L(528, 320, 552, 312, TEAL_L, 6) + L(248, 372, 268, 364, TEAL_L, 5)   # 撒落的动势线
    g += P("M 418 336 Q 428 322 444 318", stroke=TEAL_L, w=5)
    return g


def art_jiu():
    """旧：打补丁、掉色的旧玩具熊。"""
    g = ground()
    g += C(316, 208, 30, BEAR) + C(444, 208, 30, BEAR)
    g += E(316, 208, 13, 10, "#a3764e") + E(444, 208, 13, 10, "#a3764e")
    g += E(380, 380, 96, 84, BEAR)
    g += E(322, 356, 26, 46, BEAR) + E(438, 356, 26, 46, BEAR)           # 手臂垂着
    g += E(330, 448, 32, 22, BEAR) + E(430, 448, 32, 22, BEAR)
    g += E(380, 396, 48, 42, "#c8a276")                                   # 肚皮（掉色浅）
    g += C(380, 282, 76, BEAR)
    g += E(380, 316, 32, 23, BEAR_L)
    g += C(380, 306, 10, INK)
    g += P("M 368 320 Q 380 328 392 320", stroke=INK, w=5)
    g += E(354, 270, 8, 11, INK) + E(406, 270, 8, 11, INK)
    g += C(356, 267, 2.8, WHITE) + C(408, 267, 2.8, WHITE)
    g += C(338, 292, 9, PINK, 0.6) + C(422, 292, 9, PINK, 0.6)
    # 补丁（肚子 + 左耳）
    g += f'<g transform="rotate(-8 372 402)">{R(344, 378, 56, 48, 8, "#dcc094")}</g>'
    for d in ("M 344 392 L 400 390", "M 346 412 L 398 410", "M 358 378 L 356 426", "M 386 378 L 384 426"):
        g += P(d, stroke="#8a6a44", w=3)
    g += C(310, 190, 14, "#a3764e")
    for d in ("M 300 182 L 320 198", "M 320 182 L 300 198"):
        g += P(d, stroke="#7a5a38", w=3)
    g += P("M 402 424 Q 416 438 410 452", stroke="#8a6a44", w=3.5)        # 脱线头
    return g


def art_lei4():
    """累：跑完瘫坐在地，头顶毛巾、直冒汗。"""
    g = ground()
    g += f'<g transform="rotate(7 380 438)">'
    g += kid(380, 438, s=0.9, pose="sit", face="sad", shirt=BLUE, look=(0.6, 0.4))
    g += sleepy_eyes(380, 238.2, 0.9, droop=True)
    g += "</g>"
    # 头顶擦汗毛巾
    g += f'<g transform="rotate(-12 380 190)">{R(346, 174, 68, 30, 12, WHITE) + L(358, 182, 402, 182, "#dfe3e6", 5)}</g>'
    g += drop(322, 214, 10) + drop(448, 238, 9) + drop(306, 266, 8) + drop(452, 300, 7)
    # 手边小水壶
    g += R(468, 388, 30, 62, 10, WBLUE) + R(474, 376, 18, 14, 5, STEEL)
    g += R(474, 398, 8, 34, 4, WHITE, 0.65)
    return g


def art_kun4():
    """困：站着伸懒腰打大哈欠，眼睛眯成缝。"""
    g = ground()
    hcy = 440 - 238 * 0.92
    g += kid(380, 440, s=0.92, pose="stand", arms="up", face="o", shirt=GREEN, look=(0, 0.6))
    g += sleepy_eyes(380, hcy, 0.92)
    g += E(380, hcy + 34 * 0.92 + 4, 20, 25, "#6b3325")                   # 大哈欠
    g += E(380, hcy + 34 * 0.92 + 13, 10, 11, "#f0876f")
    g += drop(312, 246, 8) + drop(452, 268, 7)                            # 困出泪花
    # 脚边小枕头
    g += E(508, 430, 52, 22, PINK) + E(508, 424, 52, 18, "#f8c0ae")
    return g


def art_guai():
    """乖：安安静静坐好，怀里抱着小熊。"""
    g = ground()
    g += kid(380, 442, s=0.9, pose="sit", face="smile", shirt=YEL, look=(0, 0.6))
    g += teddy(380, 340, 1.1)
    # 两只手臂环抱小熊
    g += L(342, 302, 358, 344, SKIN, 25) + C(360, 348, 13, SKIN)
    g += L(418, 302, 402, 344, SKIN, 25) + C(400, 348, 13, SKIN)
    return g


def art_yong3():
    """勇：站上小高台，披着红披风挺起小胸脯。"""
    g = ground()
    g += R(272, 380, 216, 58, 12, WOOD)
    g += R(272, 380, 216, 14, 7, WOOD_L)
    g += R(284, 438, 26, 18, 6, WOOD_D) + R(450, 438, 26, 18, 6, WOOD_D)
    # 披风（身后向左飘）
    g += P("M 356 252 Q 268 272 234 352 Q 232 372 258 366 Q 300 358 330 374 L 358 320 Z", RED)
    g += kid(380, 378, s=0.78, pose="stand", arms="up", face="open", shirt=TEAL, look=(0, -0.6))
    return g


def art_jian4():
    """健：单手把小哑铃举过头顶，练得满头汗。"""
    g = ground()
    g += kid(368, 436, s=0.9, pose="stand", arms="point", point_at=(500, 186), face="o",
             shirt=BLUE, look=(0.8, -0.8))
    # 举起的哑铃（画在手端）
    g += f'<g transform="translate(466,226) rotate(44)">'
    g += R(-62, -27, 22, 54, 9, STEEL_D) + R(40, -27, 22, 54, 9, STEEL_D)
    g += R(-46, -8, 92, 16, 8, STEEL)
    g += "</g>"
    # 地上另一只哑铃
    g += f'<g transform="translate(238,418) rotate(-12)">'
    g += R(-44, -20, 16, 40, 7, STEEL_D) + R(28, -20, 16, 40, 7, STEEL_D)
    g += R(-32, -6, 64, 12, 6, STEEL)
    g += "</g>"
    g += drop(320, 208, 9) + drop(428, 196, 8)
    return g


def art_nuan3():
    """暖：小朋友举起戴着红手套的双手晒太阳（手套穿在手上，一眼可读）。"""
    g = ground()
    # 左上小太阳
    g += C(146, 122, 40, SUN)
    for i in range(8):
        a = math.radians(i * 45)
        g += L(146 + 52 * math.cos(a), 122 + 52 * math.sin(a),
               146 + 74 * math.cos(a), 122 + 74 * math.sin(a), SUN_L, 9)
    # 小朋友（双臂上举）
    g += kid(380, 448, s=0.92, pose="stand", arms="up", face="smile", shirt=PINK, look=(0, 0.3))
    hy = 448 - 168 * 0.92 - 8 * 0.92 - 62 * 0.92 + 6 * 0.92      # 手心高度 ≈234.6
    for hx in (302.7, 457.3):                                     # 左右手
        sgn = 1 if hx > 380 else -1                               # 拇指朝外侧
        g += R(hx - 27, hy - 64, 54, 68, 26, RED)                 # 手套掌身
        g += f'<g transform="rotate({-30 * sgn} {hx + 20 * sgn} {hy - 12})">' \
             f'{R(hx + (14 if sgn > 0 else -56), hy - 24, 50, 26, 13, RED)}</g>'   # 大拇指（掌侧中部）
        g += R(hx - 31, hy - 2, 62, 32, 14, WHITE)                # 加宽白袖口
        g += R(hx - 31, hy - 2, 62, 10, 5, "#dfe3e6")
        for dx in (-15, 0, 15):
            g += L(hx + dx, hy + 6, hx + dx, hy + 26, "#dfe3e6", 4)   # 袜口罗纹
    return g


def art_liang2():
    """凉：冰淇淋冒着凉气。"""
    g = ground()
    g += PG([(326, 288), (434, 288), (380, 440)], WOOD_L)
    g += L(340, 320, 422, 308, WOOD_D, 6) + L(350, 358, 414, 348, WOOD_D, 6)
    g += L(364, 394, 398, 390, WOOD_D, 6)
    g += C(380, 240, 66, "#e8f1f8") + C(380, 192, 50, WHITE) + C(380, 156, 32, WHITE)
    g += E(358, 224, 22, 34, WHITE, 0.85)
    g += C(396, 250, 12, "#d3e5f2", 0.8)
    g += P("M 306 244 Q 296 280 312 310", stroke="#a5d9f0", w=9)          # 凉风
    g += P("M 278 282 Q 272 304 284 322", stroke="#c2e4f4", w=7)
    g += P("M 454 240 Q 466 276 452 306", stroke="#a5d9f0", w=9)
    g += P("M 482 280 Q 490 302 480 320", stroke="#c2e4f4", w=7)
    g += C(252, 226, 8, "#c2e4f4") + C(510, 210, 7, "#c2e4f4") + C(478, 342, 6, "#c2e4f4")
    return g


def art_jing4():
    """净：洗得白白亮亮的盘子，闪着光、旁边有海绵泡泡。"""
    g = ground()
    g += E(380, 424, 214, 28, "#cfe0ea")
    g += E(380, 372, 204, 56, "#d8e2e8")                                  # 盘身厚度
    g += E(380, 358, 204, 56, WHITE)                                      # 盘面
    g += E(380, 356, 146, 38, "#eef2f5")                                  # 盘凹
    g += E(380, 354, 66, 16, "#fdfdfa")
    g += P("M 246 330 Q 216 348 224 380", stroke=WHITE, w=12)             # 盘沿高光
    g += P("M 514 330 Q 540 344 536 372", stroke="#eef2f5", w=9)
    g += sparkle(234, 240, 20) + sparkle(524, 258, 16) + sparkle(306, 164, 13)
    g += sparkle(466, 172, 12) + sparkle(566, 322, 13) + sparkle(198, 322, 11)
    g += drop(280, 290, 11) + drop(492, 294, 10)
    # 黄海绵 + 泡泡（刚洗完）
    g += R(560, 396, 66, 32, 12, YEL) + C(578, 412, 6, SUN_L) + C(600, 406, 5, SUN_L) + C(614, 416, 5, SUN_L)
    g += C(548, 380, 9, WBLUE, 0.6) + C(642, 388, 7, WBLUE, 0.6) + C(628, 366, 5, WBLUE, 0.55)
    return g


def art_chou3():
    """丑：灰灰的丑小鸭，乖乖站在水边（友好的丑）。"""
    g = ground()
    g += E(380, 424, 210, 34, WBLUE)
    g += P("M 220 424 Q 380 396 540 424", stroke="#a5d9f0", w=5)
    g += E(380, 352, 82, 58, DUCK_G)
    g += E(380, 372, 56, 30, DUCK_L)
    g += PG([(462, 340), (492, 322), (486, 356)], DUCK_G)                 # 小翘尾
    g += C(380, 258, 52, DUCK_G)
    g += P("M 358 214 Q 352 196 366 202", stroke="#7f8a92", w=5)          # 乱蓬蓬的毛
    g += P("M 380 208 Q 380 188 392 196", stroke="#7f8a92", w=5)
    g += P("M 402 214 Q 410 196 418 206", stroke="#7f8a92", w=5)
    g += PG([(404, 262), (444, 272), (404, 282)], "#f2a03c")              # 扁嘴
    g += E(358, 246, 9, 12, INK) + E(382, 244, 9, 12, INK)
    g += C(360, 242, 3, WHITE) + C(384, 240, 3, WHITE)
    g += C(344, 268, 8, PINK, 0.7) + C(396, 268, 8, PINK, 0.7)
    g += E(352, 340, 22, 34, "#7f8a92", 0.75)                             # 翅膀
    g += E(542, 416, 22, 8, WHITE, 0.9)                                   # 水面白羽毛
    g += E(236, 434, 16, 6, WHITE, 0.85)
    return g


def art_mi4():
    """密：一棵挨一棵的密林，树冠层层叠叠。"""
    g = ground()
    g += C(300, 210, 104, "#5e8f52") + C(470, 200, 112, "#5e8f52") + C(620, 250, 96, "#5e8f52")
    g += C(160, 260, 92, "#6a9a5c")
    g += C(230, 320, 98, "#7fae70") + C(400, 330, 104, "#7fae70") + C(570, 330, 96, "#7fae70")
    g += C(680, 340, 84, "#7fae70") + C(96, 350, 80, "#7fae70")
    g += C(320, 274, 60, "#9cc98a", 0.85) + C(520, 286, 54, "#9cc98a", 0.85)
    for x in (250, 386, 520, 640):
        g += R(x - 15, 396, 30, 56, 9, WOOD_D)
    g += E(160, 420, 60, 18, "#5e8f52") + E(600, 424, 66, 18, "#5e8f52")  # 灌木填满
    g += E(380, 434, 90, 18, "#6a9a5c")
    return g


def art_wen1():
    """温：玻璃杯温水冒出小小热气，杯后有暖光。"""
    g = ground()
    g += E(380, 368, 172, 102, "#f9e2b8", 0.8)                            # 暖光晕
    g += cup(380, top=278, w=150, h=176, water=0.64)
    # 热气（暖灰打底 + 白芯，粗一点才看得见）
    for d, extra in (("M 344 254 Q 328 226 346 200 Q 362 180 348 154", 0),
                     ("M 394 250 Q 380 222 398 194 Q 414 174 402 148", 0),
                     ("M 438 258 Q 428 234 442 210", 0)):
        g += P(d, stroke="#e8dbc8", w=13)
        g += P(d, stroke=WHITE, w=6)
    return g


def art_tang4():
    """烫：一大碗冒白汽的热汤，小朋友鼓着腮帮吹一吹。"""
    g = ground()
    g += E(340, 442, 84, 14, "#b3542f")                                   # 碗脚
    g += P("M 192 348 Q 202 424 262 438 L 418 438 Q 478 424 488 348 Q 340 378 192 348 Z", "#d9734f")
    g += P("M 192 348 Q 202 424 262 438 L 300 438 Q 254 414 246 352 Q 216 350 192 348 Z", "#c05f3e")
    g += E(340, 348, 148, 32, "#c05f3e")                                  # 碗沿
    g += E(340, 346, 124, 25, "#f2b53c")                                  # 汤面
    g += E(310, 342, 46, 10, "#f8dc8e", 0.9)
    # 大团白汽
    for cx, s in ((296, 1.15), (346, 1.35), (394, 1.0)):
        g += C(cx, 268, 27 * s, WHITE, 0.92)
        g += C(cx - 10 * s, 224, 21 * s, WHITE, 0.85)
        g += C(cx + 8 * s, 186, 15 * s, WHITE, 0.75)
    g += C(438, 296, 17, WHITE, 0.8) + C(244, 300, 15, WHITE, 0.8)
    # 小朋友凑近吹
    g += kid(606, 446, s=0.72, pose="sit", flip=-1, face="o", shirt=TEAL, look=(-1, -0.6))
    g += P("M 534 336 Q 498 342 474 356", stroke="#d8e6ee", w=9)          # 吹气
    g += P("M 538 362 Q 506 366 482 378", stroke="#d8e6ee", w=8)
    return g


def art_bian3():
    """扁：圆圆的球被大石头压得扁扁的。"""
    g = ground()
    g += E(368, 404, 126, 46, RED_D)
    g += E(360, 394, 122, 42, RED)
    g += E(330, 380, 30, 11, "#f2916c", 0.9)
    g += C(452, 396, 7, RED_D)                                            # 气嘴
    g += E(388, 318, 108, 64, ROCK)
    g += E(362, 300, 64, 34, ROCK_L)
    g += P("M 208 388 Q 196 400 208 412", stroke=RED_D, w=6)              # 压出的气
    g += P("M 190 372 Q 172 392 190 414", stroke="#f2916c", w=5)
    return g


def art_jin3():
    """紧：小朋友把大运动鞋的鞋带拉得笔直，蝴蝶结系得紧紧的。"""
    g = ground()
    # 大运动鞋（侧视，鞋头朝左）：鞋底 + 鞋身 + 白鞋头
    g += R(140, 416, 306, 40, 18, "#c9cdd1")
    g += R(140, 416, 306, 12, 6, "#b3b9bf")
    g += P("M 150 418 L 150 388 Q 154 352 202 344 Q 240 338 264 354 L 302 370 "
           "Q 354 336 390 318 Q 428 312 436 334 L 440 360 L 442 418 Z", "#5fa8d8")
    g += P("M 150 418 L 150 388 Q 154 352 202 344 Q 226 340 244 348 L 238 418 Z", "#f4f2ec")
    g += R(408, 302, 26, 16, 8, "#4a97c9")                                # 鞋后跟提环
    # 鞋喉交叉鞋带
    g += L(298, 362, 332, 378, RED, 8) + L(332, 360, 298, 378, RED, 8)
    # 蝴蝶结（系在鞋帮顶，结在中间、两耳在左右、两尾垂在鞋帮）
    g += f'<g transform="rotate(-12 362 312)">{E(362, 312, 36, 23, RED)}</g>'
    g += f'<g transform="rotate(12 418 312)">{E(418, 312, 36, 23, RED)}</g>'
    g += R(376, 302, 30, 30, 10, RED_D)
    g += PG([(396, 338), (386, 374), (408, 368)], RED_D)
    g += PG([(412, 338), (432, 372), (408, 376)], "#e05a30")
    # 拉得笔直的两根鞋带（绷紧）
    g += L(398, 306, 508, 270, RED, 10)
    g += L(404, 330, 520, 330, RED, 10)
    g += L(456, 282, 462, 270, RED_D, 5) + L(460, 324, 466, 334, RED_D, 5)   # 绷紧震颤短线
    # 小朋友双手各攥一根鞋带使劲拉（两臂一上一下明显分开）
    g += kid(620, 450, s=0.86, pose="stand", arms="down", face="o", shirt="#f0876f", look=(-0.9, -0.4))
    g += L(581, 312, 524, 274, SKIN, 20) + C(516, 268, 12, SKIN)
    g += L(585, 322, 534, 328, SKIN, 20) + C(524, 328, 12, SKIN)
    return g


def art_man4():
    """慢：乌龟和蜗牛并排慢慢爬。"""
    g = ground()
    g += L(160, 380, 196, 380, GREEN_L, 7) + L(146, 402, 174, 402, GREEN_L, 6)
    g += L(470, 356, 502, 356, "#e9d3a8", 7) + L(458, 378, 486, 378, "#e9d3a8", 6)
    # 乌龟
    g += P("M 194 414 Q 280 268 366 414 Z", "#6f9a60")
    g += P("M 236 400 Q 280 320 324 400", stroke="#5e8f52", w=6)
    g += P("M 258 414 Q 280 356 302 414", stroke="#5e8f52", w=6)
    g += E(212, 420, 22, 13, "#8fbf7f") + E(340, 420, 22, 13, "#8fbf7f")
    g += C(368, 396, 22, "#8fbf7f")
    g += C(374, 390, 5, INK) + P("M 372 404 Q 380 410 388 404", stroke=INK, w=4)
    g += PG([(186, 408), (162, 400), (180, 422)], "#8fbf7f")
    # 蜗牛
    g += P("M 496 428 L 588 428 Q 606 428 606 412 Q 606 398 590 398 L 516 398 Q 496 398 496 414 Z", "#e2b07e")
    g += P("M 508 400 Q 498 384 506 366", stroke="#e2b07e", w=13)
    g += L(504, 366, 498, 348, "#e2b07e", 5) + C(497, 344, 6, "#e2b07e")
    g += L(514, 364, 520, 346, "#e2b07e", 5) + C(521, 342, 6, "#e2b07e")
    g += C(510, 382, 4, INK)
    g += C(556, 352, 46, "#b57b44")
    g += P("M 556 352 Q 574 344 574 358 Q 574 374 554 374 Q 532 374 532 354 Q 532 328 558 326",
           stroke="#8a5a33", w=7)
    g += P("M 606 428 Q 620 424 628 428", stroke="#e2b07e", w=10)         # 尾巴
    g += P("M 590 428 Q 604 434 616 430", stroke="#c89468", w=8, opacity=0.7)
    return g


def art_shu2():
    """熟：苹果红透了，一个挂在枝头、一个熟落地上。"""
    g = ground()
    g += P("M 700 130 Q 570 150 452 178 Q 400 190 372 214", stroke=WOOD_D, w=20)
    g += f'<g transform="rotate(-28 520 150)">{E(520, 150, 44, 20, GREEN)}</g>'
    g += f'<g transform="rotate(18 600 178)">{E(600, 178, 40, 18, "#7fae70")}</g>'
    g += f'<g transform="rotate(-58 430 200)">{E(430, 200, 38, 17, "#7fae70")}</g>'
    # 枝头熟苹果
    g += L(470, 196, 470, 226, "#8a5a33", 7)
    g += f'<g transform="rotate(24 486 216)">{E(486, 216, 20, 9, GREEN)}</g>'
    g += C(476, 276, 48, RED_D) + C(470, 270, 46, RED)
    g += C(454, 254, 11, "#f2916c", 0.9)
    # 落地熟苹果
    g += C(268, 404, 42, RED_D) + C(262, 398, 40, RED)
    g += C(248, 384, 9, "#f2916c", 0.9)
    g += P("M 268 360 Q 262 348 268 338", stroke="#8a5a33", w=6)
    g += f'<g transform="rotate(-30 282 352)">{E(282, 352, 18, 8, GREEN)}</g>'
    g += L(330, 420, 356, 414, RED_D, 5) + L(334, 434, 356, 434, RED_D, 5)   # 落地弹跳线
    return g


def art_gan3():
    """敢：大胆伸手轻轻摸小狗的头。"""
    g = ground()
    g += kid(300, 436, s=0.9, pose="stand", arms="point", point_at=(478, 336), face="smile",
             shirt=BLUE, look=(1, 0))
    g += L(338, 290, 446, 314, SKIN, 27) + C(454, 316, 14, SKIN)          # 伸出的手
    # 小狗（坐姿，垂耳朵，抬头看小朋友）
    g += E(512, 398, 60, 48, "#c89058")
    g += E(512, 412, 38, 26, "#e9b97e")
    g += R(490, 426, 16, 24, 8, "#c89058") + R(524, 426, 16, 24, 8, "#c89058")
    g += C(494, 330, 42, "#c89058")
    g += f'<g transform="rotate(14 460 336)">{E(460, 336, 14, 27, "#a3764e")}</g>'    # 垂耳
    g += f'<g transform="rotate(-12 528 332)">{E(528, 332, 14, 27, "#a3764e")}</g>'
    g += E(492, 348, 23, 15, "#e9b97e")
    g += C(492, 340, 8, INK)
    g += P("M 482 356 Q 492 362 502 356", stroke=INK, w=4)
    g += E(508, 360, 7, 11, "#f0876f")                                    # 小舌头
    g += E(480, 322, 7, 9, INK) + E(508, 320, 7, 9, INK)
    g += C(482, 319, 2.4, WHITE) + C(510, 317, 2.4, WHITE)
    g += R(468, 362, 52, 13, 6, RED)                                      # 红项圈
    g += C(494, 374, 7, SUN)                                              # 铃铛
    g += P("M 568 396 Q 594 382 598 360", stroke="#c89058", w=12)         # 摇尾巴
    g += P("M 602 372 Q 616 368 622 358", stroke="#c89058", w=8, opacity=0.6)
    return g


def art_ai3():
    """矮：踮起脚尖也够不到高架子上的玩具。"""
    g = ground()
    g += R(430, 196, 258, 26, 9, WOOD)
    g += R(430, 196, 258, 9, 4, WOOD_L)
    g += PG([(456, 222), (486, 222), (456, 258)], WOOD_D)
    g += PG([(660, 222), (690, 222), (690, 258)], WOOD_D)
    g += ball(486, 178, 26, TEAL, TEAL_D, TEAL_L)
    g += R(560, 162, 46, 36, 7, YEL) + R(560, 162, 46, 10, 5, SUN_L)
    g += kid(360, 436, s=0.92, pose="stand", arms="point", point_at=(420, 180), face="o",
             shirt=BLUE, look=(0.7, -1))
    g += drop(300, 250, 8)                                                # 急出小汗
    g += P("M 402 208 Q 416 214 418 228", stroke=TEAL_D, w=4)             # 手和玩具之间的差距
    return g


def art_huai4():
    """坏：玩具车摔翻四轮朝天，还掉了一个轮子。"""
    g = ground()
    g += f'<g transform="rotate(180 380 350)">'
    g += R(266, 300, 228, 70, 26, RED)
    g += R(322, 258, 116, 56, 18, RED_D)
    g += R(336, 268, 44, 26, 8, "#bfe3f5") + R(390, 268, 34, 26, 8, "#bfe3f5")
    g += C(310, 374, 27, INK) + C(310, 374, 11, STEEL)
    g += C(450, 374, 27, INK) + C(450, 374, 11, STEEL)
    g += L(320, 320, 348, 344, "#8a3a22", 5) + L(348, 344, 336, 362, "#8a3a22", 5)   # 裂纹
    g += "</g>"
    g += C(584, 420, 28, INK) + C(584, 420, 11, STEEL)                    # 掉落的轮子
    g += L(548, 380, 560, 398, YEL_D, 6) + L(620, 378, 610, 396, YEL_D, 6)
    g += L(200, 330, 224, 348, YEL_D, 6) + L(196, 380, 222, 386, YEL_D, 5)  # 撞击线
    return g


def art_jia3():
    """假：左盆真花引蝴蝶，右盆塑料假花光溜溜。"""
    g = ground()
    # 左：真花
    g += PG([(206, 384), (274, 384), (264, 436), (216, 436)], "#d9734f")
    g += R(200, 366, 80, 22, 9, "#e8896b")
    g += E(240, 370, 32, 7, "#7a5236")
    g += P("M 240 366 Q 232 330 244 300", stroke="#5e8f52", w=9)
    g += f'<g transform="rotate(-34 218 342)">{E(218, 342, 22, 11, GREEN)}</g>'
    g += f'<g transform="rotate(28 264 330)">{E(264, 330, 20, 10, "#7fae70")}</g>'
    g += flower5(244, 272, 34, petal="#f0876f", core=SUN)
    g += drop(252, 322, 7)
    # 右：假花（塑料：笔直杆、无叶、花瓣一模一样、高光发亮）
    g += PG([(486, 384), (554, 384), (544, 436), (496, 436)], "#5fa8d8")
    g += R(480, 366, 80, 22, 9, "#4a97c9")
    g += R(514, 302, 10, 66, 4, "#8fbf7f")
    for i in range(6):
        a = math.radians(i * 60 - 90)
        g += C(518 + 26 * math.cos(a), 270 + 26 * math.sin(a), 19, PLASTIC)
    g += C(518, 270, 15, "#f9c95e")
    g += C(506, 254, 6, WHITE, 0.85) + C(534, 250, 4, WHITE, 0.7)
    # 蝴蝶只往真花飞
    g += C(302, 206, 12, "#f0876f") + C(322, 206, 12, "#f0876f")
    g += C(305, 220, 8, YEL) + C(319, 220, 8, YEL)
    g += E(312, 214, 4, 12, INK)
    g += L(310, 202, 306, 192, INK, 2.5) + L(314, 202, 318, 192, INK, 2.5)
    return g


# ---------- 组卡片文案数据 ----------
GROUP_CARDS = [
    {"char": "静", "pinyin": "jìng", "tone": "第四声",
     "sentence": "小猫睡着了，真静。",
     "say": "夜深了，猫宝宝在摇篮里睡得香。",
     "chat": "“静下来能听见哪些小声音？”",
     "life": "一起安静坐一分钟，体会一下静。"},
    {"char": "吵", "pinyin": "chǎo", "tone": "第三声",
     "sentence": "两只小鸟吵起来。",
     "say": "两只小鸟对着叫，谁也不让谁。",
     "chat": "“什么时候你会觉得吵呀？”",
     "life": "轻声说话不吵，大声喊叫就吵。"},
    {"char": "闹", "pinyin": "nào", "tone": "第四声",
     "sentence": "闹钟响了真吵闹。",
     "say": "闹钟叮铃铃大叫，赶紧捂住耳朵。",
     "chat": "“早上闹钟响了你要做什么？”",
     "life": "定个小闹钟，铃一响就起床。"},
    {"char": "整", "pinyin": "zhěng", "tone": "第三声",
     "sentence": "小书架整理好了。",
     "say": "书一本一本竖着放，整整齐齐。",
     "chat": "“看完的书应该放回哪里？”",
     "life": "一起把桌上的书整理好。"},
    {"char": "齐", "pinyin": "qí", "tone": "第二声",
     "sentence": "四支蜡笔排齐啦。",
     "say": "笔尾对着同一条线，一枝也不乱。",
     "chat": "“排队时要怎样才算齐？”",
     "life": "把蜡笔按颜色排齐试试看。"},
    {"char": "乱", "pinyin": "luàn", "tone": "第四声",
     "sentence": "玩具扔得乱糟糟。",
     "say": "箱子翻了，玩具撒了一地真乱。",
     "chat": "“玩具玩完该收到哪里？”",
     "life": "一起收玩具，把乱变整齐。"},
    {"char": "旧", "pinyin": "jiù", "tone": "第四声",
     "sentence": "这只小熊变旧了。",
     "say": "熊熊缝了补丁、掉了色，旧旧的。",
     "chat": "“你有没有用旧的宝贝？”",
     "life": "把旧衣服叠好送去捐掉。"},
    {"char": "累", "pinyin": "lèi", "tone": "第四声（另读 lěi，如“积累”）",
     "sentence": "跑完步好累呀。",
     "say": "瘫坐在地上直冒汗，就是累了。",
     "chat": "“做什么事以后你会觉得累？”",
     "life": "累了就坐下喝口水歇一歇。"},
    {"char": "困", "pinyin": "kùn", "tone": "第四声",
     "sentence": "打个大哈欠，困了。",
     "say": "张大嘴巴打哈欠，眼皮直打架。",
     "chat": "“你一天里什么时候最困？”",
     "life": "困了就早点上床睡觉。"},
    {"char": "乖", "pinyin": "guāi", "tone": "第一声",
     "sentence": "抱着小熊真乖。",
     "say": "安安静静坐好抱熊，乖宝宝。",
     "chat": "“大人夸你乖是夸你什么？”",
     "life": "安静坐五分钟，当次乖宝宝。"},
    {"char": "勇", "pinyin": "yǒng", "tone": "第三声",
     "sentence": "站上高台真勇敢。",
     "say": "披着披风挺起胸，勇敢站高高。",
     "chat": "“你做过哪件勇敢的事？”",
     "life": "试试自己滑下小滑梯。"},
    {"char": "健", "pinyin": "jiàn", "tone": "第四声",
     "sentence": "小哑铃举高高，真健壮。",
     "say": "天天举一举、练一练，身体健。",
     "chat": "“做什么运动身体会更好？”",
     "life": "伸伸手弯弯腰，做套早操。"},
    {"char": "暖", "pinyin": "nuǎn", "tone": "第三声",
     "sentence": "戴上手套真暖和。",
     "say": "太阳照着，红手套暖暖的。",
     "chat": "“冬天什么让你觉得暖？”",
     "life": "给妈妈捂捂手，暖一暖。"},
    {"char": "凉", "pinyin": "liáng", "tone": "第二声",
     "sentence": "冰淇淋凉凉的。",
     "say": "冰淇淋凉风丝丝，吃一口真凉。",
     "chat": "“凉凉的东西摸着像什么？”",
     "life": "喝口凉开水，说说凉的感觉。"},
    {"char": "净", "pinyin": "jìng", "tone": "第四声",
     "sentence": "盘子亮晶晶，真干净。",
     "say": "洗过的盘子白白亮亮会发光。",
     "chat": "“饭前怎样手才干净？”",
     "life": "把小桌子擦得干干净净。"},
    {"char": "丑", "pinyin": "chǒu", "tone": "第三声",
     "sentence": "丑小鸭也想抱抱。",
     "say": "灰灰的丑小鸭，长大变天鹅。",
     "chat": "“丑小鸭孤单时谁陪它？”",
     "life": "抱抱不好看的旧玩具。"},
    {"char": "密", "pinyin": "mì", "tone": "第四声",
     "sentence": "树林长得真密。",
     "say": "树挨着树、叶叠着叶，密密的。",
     "chat": "“密林里能玩捉迷藏吗？”",
     "life": "看灌木丛，说哪里密哪里疏。"},
    {"char": "温", "pinyin": "wēn", "tone": "第一声",
     "sentence": "温水冒出小热气。",
     "say": "温水不烫也不凉，冒小小热气。",
     "chat": "“温水喝起来什么感觉？”",
     "life": "倒杯温水给爷爷奶奶。"},
    {"char": "烫", "pinyin": "tàng", "tone": "第四声",
     "sentence": "汤太烫了吹一吹。",
     "say": "冒白汽的汤很烫，吹凉再喝。",
     "chat": "“烫的东西碰到会怎样？”",
     "life": "吃饭前吹一吹，小心烫。"},
    {"char": "扁", "pinyin": "biǎn", "tone": "第三声",
     "sentence": "球被压得扁扁的。",
     "say": "大石头一压，圆圆球变扁了。",
     "chat": "“家里哪些东西扁扁的？”",
     "life": "捏橡皮泥，把它压成扁片。"},
    {"char": "紧", "pinyin": "jǐn", "tone": "第三声",
     "sentence": "蝴蝶结系得紧。",
     "say": "鞋带拉得紧紧的，结就不松。",
     "chat": "“鞋带松了走路会怎样？”",
     "life": "学系鞋带，拉紧打个结。"},
    {"char": "慢", "pinyin": "màn", "tone": "第四声",
     "sentence": "乌龟蜗牛慢慢爬。",
     "say": "一步一步不着急，就是慢。",
     "chat": "“和爸爸比赛谁跑得慢？”",
     "life": "学乌龟慢慢走五步试试。"},
    {"char": "熟", "pinyin": "shú", "tone": "第二声",
     "sentence": "熟透的苹果落下来。",
     "say": "苹果红透了熟了，就会掉下来。",
     "chat": "“生苹果和熟苹果哪里不一样？”",
     "life": "闻闻香蕉，熟了有香味。"},
    {"char": "敢", "pinyin": "gǎn", "tone": "第三声",
     "sentence": "敢摸小狗真棒。",
     "say": "轻轻摸摸小狗头，胆子真大。",
     "chat": "“你敢摸小动物吗？”",
     "life": "试一试新滑梯，敢玩敢滑。"},
    {"char": "矮", "pinyin": "ǎi", "tone": "第三声",
     "sentence": "踮脚也够不着，太矮啦。",
     "say": "踮起脚尖还差一点，个子矮。",
     "chat": "“家里谁高谁矮呀？”",
     "life": "和爸爸背靠背比高矮。"},
    {"char": "坏", "pinyin": "huài", "tone": "第四声",
     "sentence": "玩具车摔坏了。",
     "say": "车子翻过来，轮子也摔掉了。",
     "chat": "“玩具坏了该怎么办？”",
     "life": "和爸爸一起修好坏玩具。"},
    {"char": "假", "pinyin": "jiǎ", "tone": "第三声（另读 jià，如“放假”）",
     "sentence": "一朵真花，一朵假花。",
     "say": "真花有叶有蝴蝶，假花是塑料。",
     "chat": "“怎么分清真花和假花？”",
     "life": "闻一闻家里的花，找真花。"},
]


def arts():
    return {
        "静": art_jing(), "吵": art_chao(), "闹": art_nao(), "整": art_zheng(),
        "齐": art_qi2(), "乱": art_luan(), "旧": art_jiu(), "累": art_lei4(),
        "困": art_kun4(), "乖": art_guai(), "勇": art_yong3(), "健": art_jian4(),
        "暖": art_nuan3(), "凉": art_liang2(), "净": art_jing4(), "丑": art_chou3(),
        "密": art_mi4(), "温": art_wen1(), "烫": art_tang4(), "扁": art_bian3(),
        "紧": art_jin3(), "慢": art_man4(), "熟": art_shu2(), "敢": art_gan3(),
        "矮": art_ai3(), "坏": art_huai4(), "假": art_jia3(),
    }


if __name__ == "__main__":
    LEGACY12 = {"好", "新", "快", "美", "响", "丽", "真", "老", "久", "全", "最", "活"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "xingrong":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY12]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"形容组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，legacy {len(LEGACY12)} 字已跳过）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != re.sub(r"（.*?）", "", c["tone"])]
    print(f"拼音/声调：{'与拼音表一致（括注为另读注）✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    punct = "，。！？、；：·—…"
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len([t for t in c["sentence"] if t not in punct]) <= 10)]
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
