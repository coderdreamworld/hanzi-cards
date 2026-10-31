#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""服饰穿戴组 20 卡插画与文案（1000 字批次 B5）。

字表（与字库1000 fushi 组一致）：
裤 鞋 帽 袜 裙 扣 袋 脱 晒 衫 布 线 袖 领 套 围 晾 链 靴 带。

画法约定（服饰类）：
- 衣帽鞋袜平铺或挂衣架展示：裤=牛仔裤平铺；鞋=一双小球鞋；帽=草帽正面；
  袜=条纹短袜一双；裙=吊带裙挂衣架；衫=绿衬衫平铺；靴=一双绿雨靴+水洼。
- 穿脱/晾晒动作用 kid()/hand()：脱=kid 把上衣褪到胸口（露肚皮）+下褪箭头；
  扣=hand() 把大纽扣按进扣眼；套=手套套到一半、指尖外露；围=kid 脖子绕围巾；
  晒=太阳+绳上晒花被；晾=衣绳+夹子+湿衣裳（无太阳）。
- 小件：袋=束口袋抽绳蝴蝶结；布=花布卷+铺开方格布；线=毛线团+线头；
  领=白领特写；链=彩珠项链+爱心坠；带=皮带+金属扣。图上无文字。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
TAN, TAN_D = "#d9a55c", "#c08a44"            # 束口袋
ORG, ORG_D = "#f2a44c", "#d98a2b"            # 毛线团/晾晒衣
PINK_D = "#e8836b"                            # 裙腰带
SWEAT, SWEAT_D = "#cfd8de", "#b8c2c9"        # 领卡毛衣
STEEL, STEEL_D = "#9aa0a6", "#7c8288"        # 停牌杆/晾绳夹
BOOT_D = "#6b9459"                            # 雨靴深绿
SUN_D = "#d98a2b"                             # 太阳深一号（同 YEL_D 族）
STR_W = "#fdfdfa"                             # 袜子白


# ---------- 裤 ----------
def a_ku():
    """裤：一条蓝牛仔裤平铺（腰头+两裤腿+口袋线）。"""
    g = ground()
    g += E(380, 442, 180, 15, INK, 0.08)
    g += R(270, 142, 220, 46, 14, BLUE_D)                    # 腰头
    g += R(300, 138, 14, 52, 6, BLUE_D)                      # 裤袢
    g += R(368, 138, 14, 52, 6, BLUE_D)
    g += R(442, 138, 14, 52, 6, BLUE_D)
    g += C(380, 168, 10, YEL)                                # 腰扣
    body = ("M 276 186 L 484 186 L 512 418 Q 513 434 497 434 L 424 434 "
            "Q 410 434 408 420 L 391 300 L 380 294 L 369 300 L 352 420 "
            "Q 350 434 336 434 L 263 434 Q 247 434 248 418 Z")
    g += P(body, BLUE)
    g += P("M 292 198 Q 318 252 352 248", stroke=WHITE, w=5)  # 前袋线
    g += P("M 468 198 Q 442 252 408 248", stroke=WHITE, w=5)
    g += R(252, 412, 96, 20, 9, BLUE_D)                      # 裤脚
    g += R(412, 412, 96, 20, 9, BLUE_D)
    g += L(300, 424, 340, 424, WHITE, 4)
    g += L(420, 424, 460, 424, WHITE, 4)
    return g


# ---------- 鞋 ----------
def _shoe():
    """单只小球鞋（鞋头朝左，局部坐标）。"""
    return wrap(
        P("M -94 26 Q -96 -4 -58 -12 Q -26 -18 -2 -34 Q 26 -48 56 -38 "
          "Q 88 -28 92 26 Z", RED),
        P("M -94 26 Q -96 -4 -58 -12 Q -46 -2 -48 26 Z", WHITE),   # 鞋头
        R(72, -16, 18, 28, 8, RED_D),                              # 鞋跟提带
        R(-6, -50, 34, 16, 7, RED_D),                              # 鞋舌
        L(-22, -26, 16, -8, WHITE, 6),                             # 鞋带
        L(16, -26, -22, -8, WHITE, 6),
        L(-80, 10, 84, 10, WHITE, 5),
        R(-98, 22, 196, 30, 15, WHITE),                            # 鞋底
        R(-98, 40, 196, 12, 6, "#dcd8cc"))


def a_xie():
    """鞋：一双球鞋鞋头朝外并排。"""
    g = ground()
    g += E(262, 452, 108, 12, INK, 0.07)
    g += E(498, 452, 108, 12, INK, 0.07)
    g += f'<g transform="translate(262,398) rotate(-4)">{_shoe()}</g>'
    g += f'<g transform="translate(498,398) rotate(4) scale(-1,1)">{_shoe()}</g>'
    return g


# ---------- 帽 ----------
def a_mao():
    """帽：一顶大檐草帽正面。"""
    g = ground()
    g += E(380, 440, 190, 14, INK, 0.08)
    g += P("M 254 268 Q 258 150 380 144 Q 502 150 506 268 Z", YEL)   # 帽顶
    g += P("M 296 206 Q 318 168 362 158", stroke=SUN_L, w=12)        # 顶光
    g += P("M 260 240 Q 380 276 500 240 L 500 274 Q 380 310 260 274 Z", RED)  # 帽带
    g += E(380, 316, 206, 50, YEL)                                   # 帽檐
    g += E(380, 312, 150, 32, YEL_D, 0.35)
    g += flower5(468, 262, 16, STR_W, YEL_D)
    return g


# ---------- 袜 ----------
def _sock():
    """单只条纹短袜（袜筒竖直、袜脚弯向左，局部坐标）。"""
    return wrap(
        P("M -44 -140 L 44 -140 L 44 -16 Q 44 16 8 28 L -56 50 Q -92 62 -102 30 "
          "Q -110 2 -76 -8 Q -50 -16 -44 -40 Z", STR_W),
        P("M 44 -60 L 44 -16 Q 44 16 8 28 L -56 50 Q -92 62 -102 30 "
          "Q -108 6 -80 -6 L -60 12 Q -46 22 -30 18 L -20 -18 Q -8 -34 8 -38 "
          "L 44 -34 Z", TEAL),                              # 袜尖脚尖一体
        R(-44, -140, 88, 22, 0, TEAL),        # 袜口条纹
        R(-44, -112, 88, 16, 0, TEAL),
        heart(2, -74, 11, PINK))


def a_wa():
    """袜：一双条纹袜平铺。"""
    g = ground()
    g += E(282, 454, 118, 12, INK, 0.07)
    g += E(498, 454, 118, 12, INK, 0.07)
    g += f'<g transform="translate(285,388) rotate(-10) scale(1.2)">{_sock()}</g>'
    g += f'<g transform="translate(495,388) rotate(10) scale(-1.2,1.2)">{_sock()}</g>'
    return g


# ---------- 裙 ----------
def a_qun():
    """裙：一条粉色吊带裙挂衣架。"""
    g = ground()
    g += E(380, 452, 150, 12, INK, 0.08)
    g += P("M 380 132 Q 380 106 401 106 Q 422 106 422 126",   # 挂钩
           stroke=INK, w=7)
    g += L(380, 136, 280, 200, WOOD_D, 9)
    g += L(380, 136, 480, 200, WOOD_D, 9)
    g += L(280, 200, 480, 200, WOOD_D, 9)
    g += R(322, 196, 16, 36, 8, PINK_D)                      # 吊带
    g += R(422, 196, 16, 36, 8, PINK_D)
    g += P("M 300 226 L 460 226 L 448 294 L 312 294 Z", PINK)  # 上身
    g += P("M 312 294 L 448 294 L 498 414 Q 380 446 262 414 Z", PINK)  # 裙摆
    g += P("M 266 404 Q 380 436 494 404 L 494 424 Q 380 454 266 424 Z", PINK_D)
    g += R(306, 286, 148, 18, 9, PINK_D)                     # 腰带
    g += flower5(380, 258, 13, STR_W, YEL_D)
    g += flower5(340, 350, 11, STR_W, YEL_D)
    g += flower5(424, 372, 11, STR_W, YEL_D)
    return g


# ---------- 扣 ----------
def a_kou():
    """扣：把大纽扣按进红开衫扣眼（hand 特写，领口+肩膀让衣服一眼可辨）。"""
    g = ground()
    g += E(380, 440, 190, 14, INK, 0.08)
    g += E(380, 172, 30, 22, SKIN)                            # 领口的小脖子
    g += P("M 244 214 Q 244 182 276 178 L 358 172 L 366 428 L 240 428 "
           "Q 226 428 226 414 L 226 232 Z", RED)              # 左襟（溜肩）
    g += P("M 516 214 Q 516 182 484 178 L 402 172 L 394 428 L 520 428 "
           "Q 534 428 534 414 L 534 232 Z", RED)              # 右襟（溜肩）
    g += R(262, 320, 60, 60, 12, RED_D)                       # 口袋
    g += P("M 348 288 L 372 296 L 368 312 L 344 304 Z", RED_D)  # 扣眼开口
    g += C(398, 300, 26, YEL)                                 # 大纽扣（按进一半）
    g += C(392, 293, 4.2, RED_D) + C(405, 293, 4.2, RED_D)
    g += C(392, 307, 4.2, RED_D) + C(405, 307, 4.2, RED_D)
    g += C(424, 372, 13, YEL) + C(424, 372, 4.4, YEL_D)       # 下方小扣
    g += C(424, 410, 13, YEL) + C(424, 410, 4.4, YEL_D)
    g += hand(500, 302, rot=-100, s=0.55)                     # 按扣的手
    return g


# ---------- 袋 ----------
def a_dai():
    """袋：束口袋（收腰+外翻袋口荷叶边），口里露出小皮球，抽绳系蝴蝶结。"""
    g = ground()
    g += E(380, 446, 170, 13, INK, 0.08)
    g += C(380, 172, 32, YEL) + C(369, 161, 8, STR_W, 0.85)   # 露出的小皮球
    g += P("M 318 196 Q 348 176 380 176 Q 412 176 442 196 Q 460 210 452 234 "
           "Q 434 252 380 252 Q 326 252 308 234 Q 300 210 318 196 Z",
           "#f6bd7d")                                         # 外翻的袋口
    for cx, cy in [(338, 202), (380, 194), (422, 202)]:       # 袋口波浪
        g += P(f"M {cx-16} {cy+8} Q {cx} {cy-10} {cx+16} {cy+8}",
               stroke="#e8a35c", w=6)
    g += P("M 332 250 Q 298 292 282 344 Q 268 398 296 418 Q 338 434 380 434 "
           "Q 422 434 464 418 Q 492 398 478 344 Q 462 292 428 250 "
           "Q 380 236 332 250 Z", ORG)                        # 袋身（收腰下鼓）
    g += P("M 470 300 Q 486 356 470 404 Q 458 420 436 426 "
           "Q 470 416 480 366 Q 486 328 470 300 Z", ORG_D, 0.5)   # 右侧影
    g += P("M 344 292 Q 380 306 416 292", stroke="#c07a2e", w=6)   # 褶线
    g += P("M 336 344 Q 380 360 424 344", stroke="#c07a2e", w=6)
    g += P("M 348 392 Q 380 404 412 392", stroke="#c07a2e", w=6)
    g += PG([(372, 254), (328, 234), (332, 276)], "#8a5a33")  # 蝴蝶结左环
    g += PG([(388, 254), (432, 234), (428, 276)], "#8a5a33")  # 蝴蝶结右环
    g += C(380, 254, 13, "#8a5a33")                           # 绳结
    g += P("M 372 260 Q 358 308 344 342", stroke="#8a5a33", w=8)   # 左垂绳
    g += P("M 388 260 Q 404 312 418 346", stroke="#8a5a33", w=8)   # 右垂绳
    g += C(344, 344, 7, "#8a5a33") + C(418, 348, 7, "#8a5a33")
    return g


# ---------- 脱 ----------
def a_tuo():
    """脱：kid 把套头衫褪到头顶（遮住脸），露小肚皮，双手抓衣摆向上拽。"""
    g = ground()
    g += kid(380, 430, s=0.95, arms="up", shirt=RED, face="o")
    g += E(380, 340, 52, 40, SKIN)                            # 露出的肚皮
    g += C(380, 350, 4, "#d9956f")                            # 肚脐
    g += P("M 292 306 Q 288 176 380 158 Q 472 176 468 306 "
           "L 468 316 Q 448 330 428 316 Q 404 332 380 316 "
           "Q 356 332 332 316 Q 312 330 292 316 Z", RED)      # 褪到头顶的衣服
    g += P("M 300 190 Q 340 168 380 166", stroke="#d4552f", w=8)   # 衣身褶
    g += L(310, 342, 322, 310, SKIN, 26)                      # 抓衣摆的小臂
    g += L(450, 342, 438, 310, SKIN, 26)
    g += C(318, 304, 13, SKIN) + C(442, 304, 13, SKIN)        # 抓衣摆的手
    g += P("M 262 330 Q 254 292 262 252", stroke=TEAL, w=9)   # 向上拽的箭头
    g += PG([(250, 258), (274, 258), (262, 232)], TEAL)
    g += P("M 498 330 Q 506 292 498 252", stroke=TEAL, w=9)
    g += PG([(486, 258), (510, 258), (498, 232)], TEAL)
    return g


# ---------- 晒 ----------
def a_shai():
    """晒：大太阳下，花被子搭在绳上晒暖。"""
    g = ground()
    for i in range(8):                                        # 太阳光芒
        a = i * math.pi / 4
        g += L(140 + 62 * math.cos(a), 112 + 62 * math.sin(a),
               140 + 86 * math.cos(a), 112 + 86 * math.sin(a), SUN, 9)
    g += C(140, 112, 46, SUN) + C(137, 109, 42, SUN_L)
    g += P("M 80 210 Q 380 262 680 210", stroke="#a9743f", w=9)  # 晒绳
    g += P("M 258 208 Q 380 168 502 208 L 502 388 Q 380 420 258 388 Z", TEAL)
    g += P("M 258 208 Q 380 168 502 208 L 502 228 Q 380 190 258 228 Z", TEAL_D)
    g += flower5(322, 302, 16, STR_W, SUN_D)
    g += flower5(436, 332, 14, "#f9c95e", TEAL_D)
    g += C(380, 262, 6, STR_W, 0.85) + C(300, 362, 7, STR_W, 0.7)
    g += C(470, 272, 6, STR_W, 0.7)
    g += f'<g transform="rotate(-18 300 196)">{R(292, 178, 16, 38, 6, WOOD_L)}</g>'
    g += f'<g transform="rotate(18 460 196)">{R(452, 178, 16, 38, 6, WOOD_L)}</g>'
    return g


# ---------- 衫 ----------
def a_shan():
    """衫：一件绿衬衫平铺（翻领+扣子+短袖）。"""
    g = ground()
    g += E(380, 442, 180, 14, INK, 0.08)
    g += f'<g transform="rotate(28 268 224)">{R(212, 204, 92, 64, 26, GREEN)}' \
         f'{R(212, 248, 92, 20, 9, BOOT_D)}</g>'              # 左短袖
    g += f'<g transform="rotate(-28 492 224)">{R(456, 204, 92, 64, 26, GREEN)}' \
         f'{R(456, 248, 92, 20, 9, BOOT_D)}</g>'
    g += R(268, 186, 224, 230, 28, GREEN)                     # 衣身
    g += R(268, 396, 224, 20, 9, BOOT_D)                      # 下摆
    g += R(344, 180, 72, 14, 6, STR_W)                        # 领座
    g += P("M 344 186 L 380 224 L 380 186 Z", STR_W)          # 翻领
    g += P("M 416 186 L 380 224 L 380 186 Z", STR_W)
    g += R(372, 220, 16, 176, 7, GREEN_L)                     # 门襟
    g += C(380, 258, 9, YEL) + C(380, 258, 3.4, YEL_D)
    g += C(380, 304, 9, YEL) + C(380, 304, 3.4, YEL_D)
    g += C(380, 350, 9, YEL) + C(380, 350, 3.4, YEL_D)
    g += R(300, 250, 44, 40, 8, BOOT_D)                       # 胸袋
    return g


# ---------- 布 ----------
def a_bu():
    """布：一卷布+铺开的大方圆点花布（波浪垂边+掀起卷角）。"""
    g = ground()
    g += PG([(120, 424), (430, 424), (560, 312), (250, 312)], TEAL)  # 铺开的布
    g += P("M 120 424 Q 152 444 186 428 Q 220 412 254 430 Q 288 448 "
           "322 430 Q 356 412 390 428 Q 412 438 430 424 L 430 440 "
           "Q 396 456 362 440 Q 328 424 294 442 Q 260 460 226 442 "
           "Q 192 424 158 442 Q 136 452 120 440 Z", TEAL_D)   # 波浪垂边
    for cx, cy in [(175, 404), (245, 402), (315, 400), (385, 398),
                   (215, 368), (285, 367), (355, 365), (425, 363),
                   (255, 332), (325, 331), (395, 330), (465, 329)]:
        g += C(cx, cy, 12, STR_W)
    for cx, cy in [(395, 368), (465, 332), (215, 404)]:
        g += C(cx, cy, 12, "#f9c95e")
    g += P("M 430 424 Q 474 400 486 356 Q 490 336 476 330 "
           "Q 466 344 458 366 Q 448 394 424 412 Z", TEAL_L)   # 掀起的卷角
    g += P("M 476 330 Q 486 342 480 362", stroke=TEAL_D, w=5)
    g += E(405, 310, 130, 10, TEAL_D, 0.5)
    g += R(240, 254, 330, 56, 28, TEAL)                       # 布卷
    g += E(242, 282, 22, 28, TEAL_D)
    g += E(568, 282, 24, 30, TEAL_D)
    g += C(568, 282, 10, TEAL_L)
    return g


# ---------- 线 ----------
def a_xian():
    """线：一团橙毛线，线头拖出打卷。"""
    g = ground()
    g += E(360, 428, 130, 13, INK, 0.08)
    g += C(360, 298, 112, ORG)
    for a0 in (200, 260, 320, 20, 80):                        # 绕线纹
        a1 = a0 + 150
        x1 = 360 + 112 * math.cos(math.radians(a0))
        y1 = 298 + 112 * math.sin(math.radians(a0))
        x2 = 360 + 112 * math.cos(math.radians(a1))
        y2 = 298 + 112 * math.sin(math.radians(a1))
        cx = 360 + 24 * math.cos(math.radians(a0 + 75))
        cy = 298 + 24 * math.sin(math.radians(a0 + 75))
        g += P(f"M {x1:.1f} {y1:.1f} Q {cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}",
               stroke=ORG_D, w=9)
    g += C(322, 258, 18, STR_W, 0.5)
    g += P("M 452 356 Q 566 400 512 440 Q 470 468 596 442", stroke=ORG, w=11)
    g += C(600, 440, 8, ORG)
    return g


# ---------- 袖 ----------
def a_xiu():
    """袖：袖筒朝下，一只小手从袖口伸出来。"""
    g = ground()
    g += E(380, 444, 120, 12, INK, 0.08)
    g += R(304, 112, 152, 88, 38, BLUE_D)                     # 肩
    g += R(334, 186, 92, 148, 22, BLUE_D)                     # 袖筒
    g += P("M 348 226 Q 380 236 412 226", stroke=BLUE, w=6)   # 袖褶
    g += R(356, 344, 48, 60, 20, SKIN)                        # 手腕
    g += hand(380, 426, s=0.66)                               # 伸出的小手
    g += R(318, 326, 124, 32, 14, BLUE)                       # 袖口
    return g


# ---------- 领 ----------
def a_ling():
    """领：小朋友半身特写——脑袋+脖子+大翻领（两片尖角）+领扣。"""
    g = ground()
    g += P("M 128 436 L 128 330 Q 128 276 190 252 L 270 224 "
           "Q 380 194 490 224 L 570 252 Q 632 276 632 330 L 632 436 Z", SWEAT)  # 肩背
    g += P("M 224 242 Q 212 336 220 436", stroke=SWEAT_D, w=6)   # 袖窿线
    g += P("M 536 242 Q 548 336 540 436", stroke=SWEAT_D, w=6)
    g += R(128, 344, 504, 24, 0, SWEAT_D)                     # 毛衣条纹
    g += R(128, 400, 504, 24, 0, SWEAT_D)
    g += R(358, 218, 44, 62, 16, SKIN)                        # 脖子
    g += C(380, 162, 68, SKIN)                                # 头
    g += P("M 312 156 Q 316 92 380 88 Q 444 92 448 156 "
           "Q 416 136 380 138 Q 344 136 312 156 Z", HAIR)     # 头发
    g += C(356, 168, 8, INK) + C(404, 168, 8, INK)            # 眼睛
    g += C(338, 190, 10, PINK, 0.75) + C(422, 190, 10, PINK, 0.75)  # 腮红
    g += P("M 362 196 Q 380 210 398 196", stroke=INK, w=5)    # 笑
    g += P("M 286 254 Q 380 292 474 254 L 474 300 Q 380 338 286 300 Z",
           "#f0f0ea")                                         # 领座一圈
    g += P("M 288 256 Q 338 278 376 284 L 368 356 L 292 316 "
           "Q 264 286 288 256 Z", STR_W)                      # 左领尖
    g += P("M 472 256 Q 422 278 384 284 L 392 356 L 468 316 "
           "Q 496 286 472 256 Z", STR_W)                      # 右领尖
    g += C(380, 380, 13, YEL) + C(380, 380, 5, YEL_D)         # 领下扣子
    return g


# ---------- 套 ----------
def a_tao():
    """套：手套正往手上套，指尖还露在外面。"""
    g = ground()
    g += E(380, 442, 130, 12, INK, 0.08)
    g += hand(380, 318, s=1.02)
    inner = wrap(
        f'<g transform="rotate(-8 -36 -30)">{R(-50, -70, 28, 48, 13, RED)}</g>',
        f'<g transform="rotate(-2 -1 -30)">{R(-16, -74, 30, 52, 14, RED)}</g>',
        f'<g transform="rotate(5 32 -30)">{R(18, -68, 29, 46, 13, RED)}</g>',
        f'<g transform="rotate(12 64 -30)">{R(52, -56, 25, 34, 11, RED)}</g>',
        f'<g transform="rotate(-30 -52 20)">{R(-86, -10, 34, 32, 14, RED)}</g>',
        R(-56, -24, 112, 98, 26, RED),                        # 手套掌面
        R(-40, -16, 20, 78, 10, STR_W, 0.25),                 # 高光
        R(-62, 56, 124, 30, 13, STR_W),                       # 手套口
        R(-62, 60, 124, 9, 5, RED_D))
    g += f'<g transform="translate(380,318) scale(1.02)">{inner}</g>'
    g += P("M 296 172 Q 288 202 296 228", stroke=TEAL, w=6)   # 往下套箭头
    g += PG([(289, 224), (303, 224), (296, 240)], TEAL)
    g += P("M 464 172 Q 472 202 464 228", stroke=TEAL, w=6)
    g += PG([(457, 224), (471, 224), (464, 240)], TEAL)
    return g


# ---------- 围 ----------
def a_wei():
    """围：小朋友脖子上一条黄围巾。"""
    g = ground()
    g += kid(380, 436, s=0.92, arms="down", shirt=BLUE)
    g += P("M 320 264 Q 380 298 440 264 L 440 298 Q 380 332 320 298 Z", YEL)
    g += P("M 340 298 L 330 396 Q 344 408 360 398 L 368 302 Z", YEL)   # 左垂尾
    g += P("M 420 298 L 430 392 Q 444 402 458 392 L 448 300 Z", YEL)   # 右垂尾
    for x1, y1, x2, y2 in [(334, 400, 330, 418), (346, 404, 344, 422),
                           (358, 402, 356, 420), (434, 396, 432, 414),
                           (446, 400, 444, 418), (456, 396, 454, 414)]:
        g += L(x1, y1, x2, y2, YEL_D, 5)                      # 围巾穗
    g += C(380, 304, 13, YEL_D)
    return g


# ---------- 晾 ----------
def a_liang():
    """晾：衣绳+夹子晾衣裳（湿袜子滴水，无太阳）。"""
    g = ground()
    g += P("M 80 168 Q 380 224 680 168", stroke="#a9743f", w=9)
    g += f'<g transform="rotate(26 158 198)">{R(100, 192, 62, 42, 14, ORG)}</g>'
    g += f'<g transform="rotate(-26 260 198)">{R(258, 192, 62, 42, 14, ORG)}</g>'
    g += R(150, 190, 118, 116, 16, ORG)                       # 小上衣
    g += P("M 182 192 Q 209 214 236 192", stroke=STR_W, w=8)
    g += f'<g transform="rotate(-14 198 182)">{R(192, 166, 13, 34, 5, WOOD_L)}</g>'
    g += f'<g transform="rotate(14 222 182)">{R(216, 166, 13, 34, 5, WOOD_L)}</g>'
    g += P("M 322 196 L 360 196 L 360 254 Q 360 270 344 276 L 322 284 "
           "Q 300 292 294 272 Q 290 256 308 250 Q 320 246 322 234 Z", TEAL)
    g += R(320, 194, 42, 14, 6, STR_W)                        # 袜口
    g += E(302, 270, 12, 10, STR_W) + E(312, 280, 10, 8, STR_W)
    g += R(336, 178, 12, 32, 5, WOOD_L)                       # 袜夹
    g += R(462, 192, 84, 118, 10, STR_W)                      # 毛巾
    g += R(462, 216, 84, 13, 0, TEAL) + R(462, 246, 84, 13, 0, TEAL)
    g += R(474, 176, 12, 32, 5, WOOD_L) + R(520, 176, 12, 32, 5, WOOD_L)
    g += drop(318, 316, 10) + drop(338, 344, 7)               # 湿袜子滴水
    return g


# ---------- 链 ----------
def a_lian():
    """链：彩珠项链+爱心坠子。"""
    g = ground()
    g += E(380, 448, 140, 12, INK, 0.08)
    cols = [RED, YEL, TEAL]
    for i in range(13):                                       # 珠链
        t = 0.04 + i * (0.92 / 12)
        mt = 1 - t
        x = mt * mt * 252 + 2 * mt * t * 380 + t * t * 508
        y = mt * mt * 172 + 2 * mt * t * 468 + t * t * 172
        g += C(x, y, 17, cols[i % 3])
        g += C(x - 5, y - 5, 4.5, STR_W, 0.85)
    g += heart(380, 356, 24, RED)                             # 爱心坠
    return g


# ---------- 靴 ----------
def _boot():
    """单只雨靴（靴头朝左，局部坐标）。"""
    return wrap(
        R(-12, -150, 72, 104, 16, GREEN),                     # 靴筒
        R(-16, -160, 80, 24, 10, BOOT_D),                     # 筒口
        R(-22, -150, 14, 30, 7, BOOT_D) + R(56, -150, 14, 30, 7, BOOT_D),  # 提手
        P("M -12 -60 L 60 -60 L 60 2 Q 60 8 52 8 L -68 8 Q -86 8 -86 -12 "
          "Q -86 -38 -58 -52 L -12 -60 Z", GREEN),            # 靴脚
        R(-86, -2, 148, 14, 6, BOOT_D),                       # 靴底
        C(24, -110, 8, GREEN_L, 0.7))


def a_xue():
    """靴：一双绿雨靴，旁边有小水洼。"""
    g = ground()
    g += E(190, 442, 46, 10, WBLUE, 0.75)                     # 水洼
    g += E(580, 438, 62, 12, WBLUE, 0.85)
    g += C(560, 428, 4, WBLUE, 0.9) + C(602, 426, 5, WBLUE, 0.9)
    g += f'<g transform="translate(298,416) rotate(-4)">{_boot()}</g>'
    g += f'<g transform="translate(470,416) rotate(4) scale(-1,1)">{_boot()}</g>'
    return g


# ---------- 带 ----------
def a_dai2():
    """带：一条皮带，金色扣头。"""
    g = ground()
    g += E(390, 440, 210, 14, INK, 0.08)
    g += P("M 150 330 Q 380 296 610 330 L 610 394 Q 380 362 150 394 Z",
           "#b57b44")                                        # 带身
    g += P("M 610 330 L 668 340 L 668 386 L 610 394 Z", "#b57b44")  # 带尾尖
    g += P("M 162 336 Q 380 304 598 336", stroke="#d9a05b", w=4)
    g += P("M 162 388 Q 380 356 598 388", stroke="#d9a05b", w=4)
    for cx, cy in [(480, 348), (516, 350), (552, 353), (588, 355)]:
        g += C(cx, cy, 6, "#8a5a33")                          # 扣眼孔
    g += R(96, 300, 86, 124, 18, YEL)                         # 金属扣
    g += R(118, 324, 42, 76, 8, "#f9c95e")
    g += L(139, 312, 139, 412, YEL_D, 8)                      # 扣针
    return g


def arts():
    return {
        "裤": a_ku(), "鞋": a_xie(), "帽": a_mao(), "袜": a_wa(),
        "裙": a_qun(), "扣": a_kou(), "袋": a_dai(), "脱": a_tuo(),
        "晒": a_shai(), "衫": a_shan(), "布": a_bu(), "线": a_xian(),
        "袖": a_xiu(), "领": a_ling(), "套": a_tao(), "围": a_wei(),
        "晾": a_liang(), "链": a_lian(), "靴": a_xue(), "带": a_dai2(),
    }


GROUP_CARDS = [
    {"char": "裤", "pinyin": "kù", "tone": "第四声",
     "sentence": "穿上裤子去玩耍。",
     "say": "两条裤腿的叫裤子，穿腿上。",
     "chat": "“你的裤子是什么颜色？”",
     "life": "自己把裤子提到腰上。"},
    {"char": "鞋", "pinyin": "xié", "tone": "第二声",
     "sentence": "穿上小鞋跑得快。",
     "say": "脚上穿的鞋，走路护小脚。",
     "chat": "“你的鞋带会自己系了吗？”",
     "life": "出门前自己穿好小鞋。"},
    {"char": "帽", "pinyin": "mào", "tone": "第四声",
     "sentence": "太阳大，快戴帽。",
     "say": "戴在头上的叫帽子。",
     "chat": "“太阳大的时候要戴什么？”",
     "life": "出门让他自己挑顶帽子。"},
    {"char": "袜", "pinyin": "wà", "tone": "第四声",
     "sentence": "穿上袜子脚不冷。",
     "say": "套在脚上的短短软软是袜。",
     "chat": "“袜子和鞋谁穿在外面？”",
     "life": "自己把袜子提到脚后跟。"},
    {"char": "裙", "pinyin": "qún", "tone": "第二声",
     "sentence": "妹妹的裙子转圈圈。",
     "say": "下摆飘飘的是裙子。",
     "chat": "“转个圈裙子会飞起来吗？”",
     "life": "穿上裙子转个圈看看。"},
    {"char": "扣", "pinyin": "kòu", "tone": "第四声",
     "sentence": "我把扣子扣好啦。",
     "say": "把扣子塞进扣眼就是扣。",
     "chat": "“外套上有几颗扣子？”",
     "life": "从最下面一颗开始练扣。"},
    {"char": "袋", "pinyin": "dài", "tone": "第四声",
     "sentence": "袋子里装满玩具。",
     "say": "能装东西的袋子叫袋。",
     "chat": "“你的口袋装过什么宝贝？”",
     "life": "往小袋子里装件玩具。"},
    {"char": "脱", "pinyin": "tuō", "tone": "第一声",
     "sentence": "自己脱下小上衣。",
     "say": "把衣服从身上褪下来是脱。",
     "chat": "“回家第一件事先脱什么？”",
     "life": "进门自己脱鞋脱外套。"},
    {"char": "晒", "pinyin": "shài", "tone": "第四声",
     "sentence": "晒被子，暖洋洋。",
     "say": "太阳晒过就暖暖的，是晒。",
     "chat": "“被子晒过太阳什么味道？”",
     "life": "帮着把小枕头拿去晒晒。"},
    {"char": "衫", "pinyin": "shān", "tone": "第一声",
     "sentence": "衬衫扣好去上学。",
     "say": "有领子有扣子的是衬衫。",
     "chat": "“衬衫的领子在哪里？”",
     "life": "把小衬衫的领子翻平整。"},
    {"char": "布", "pinyin": "bù", "tone": "第四声",
     "sentence": "这块花布真漂亮。",
     "say": "做衣服的软软面料是布。",
     "chat": "“摸摸沙发套，是布的吗？”",
     "life": "找三样家里布做的东西。"},
    {"char": "线", "pinyin": "xiàn", "tone": "第四声",
     "sentence": "毛线团绕呀绕。",
     "say": "绕成一团细细的是线。",
     "chat": "“毛线能织成什么呀？”",
     "life": "绕一团毛线给他看看。"},
    {"char": "袖", "pinyin": "xiù", "tone": "第四声",
     "sentence": "袖口里伸出小手。",
     "say": "胳膊穿进去的筒是袖子。",
     "chat": "“袖子太长遮手了怎么办？”",
     "life": "把外套袖子卷起来洗手。"},
    {"char": "领", "pinyin": "lǐng", "tone": "第三声",
     "sentence": "翻好衣领再出门。",
     "say": "脖子周围的一圈叫领子。",
     "chat": "“衣领为什么要翻好？”",
     "life": "出门前检查衣领翻好没。"},
    {"char": "套", "pinyin": "tào", "tone": "第四声",
     "sentence": "把手套套上小手。",
     "say": "从头上手上滑进去是套。",
     "chat": "“手套是怎么穿到手上？”",
     "life": "让他自己把手套套上。"},
    {"char": "围", "pinyin": "wéi", "tone": "第二声",
     "sentence": "围巾围得暖和和。",
     "say": "绕在脖子上的叫围巾。",
     "chat": "“围巾围几圈最暖和？”",
     "life": "给他围上围巾照照镜子。"},
    {"char": "晾", "pinyin": "liàng", "tone": "第四声",
     "sentence": "衣服洗好晾起来。",
     "say": "用夹子挂起来晾干是晾。",
     "chat": "“湿衣服挂在哪里晾？”",
     "life": "把小袜子夹上晾衣绳。"},
    {"char": "链", "pinyin": "liàn", "tone": "第四声",
     "sentence": "项链戴上真好看。",
     "say": "一颗颗珠子穿成项链。",
     "chat": "“项链挂在哪个部位？”",
     "life": "看看家里有没有项链。"},
    {"char": "靴", "pinyin": "xuē", "tone": "第一声",
     "sentence": "下雨穿雨靴踩水洼。",
     "say": "筒筒很高的鞋叫靴子。",
     "chat": "“雨靴和运动鞋哪里不一样？”",
     "life": "下雨天穿上雨靴踩踩水。"},
    {"char": "带", "pinyin": "dài", "tone": "第四声",
     "sentence": "裤腰上系着皮带。",
     "say": "围在腰上扣紧的是皮带。",
     "chat": "“爸爸的皮带上有什么？”",
     "life": "摸摸皮带上的小孔。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "fushi" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B5"] if e["file"] == "素材1000_fushi.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"服饰穿戴组：卡数 {len(GROUP_CARDS)}")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    idx = [ziku_chars.index(ch) for ch in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = set(a) == set(mine)
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad = []
    for c in GROUP_CARDS:
        w = py[c["char"]]
        if c["pinyin"] != w["pinyin"]:
            bad.append((c["char"], "pinyin", c["pinyin"], w["pinyin"]))
        if not (c["tone"] == w["tone"] or c["tone"].startswith(w["tone"] + "（")):
            bad.append((c["char"], "tone", c["tone"], w["tone"]))
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((c["char"], "句长", hanzi))
        if c["char"] not in c["sentence"]:
            bad.append((c["char"], "句缺字"))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((c["char"], f, len(c[f])))
    print(f"拼音/声调/文案：{'全部通过 ✓' if not bad else str(bad)}")

    svgbad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            svgbad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                svgbad.append((k, t))
        if not v.startswith("<ellipse"):
            svgbad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not svgbad else f"SVG 问题：{svgbad}")

    assert mine == expect and keys_ok and idx == sorted(idx) and not bad and not svgbad, "自检未通过"
    print("自检通过 ✓")
