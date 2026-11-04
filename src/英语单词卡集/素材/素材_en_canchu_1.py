#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 餐厨（canchu）第 1 段插画（10 卡：bowl~kettle）。

每卡造型要点：bowl 蓝碗热汤冒气 / plate 白盘煎蛋（蛋白+黄心）/ cup 粉色带把杯冒热气 /
chopsticks 两根木筷夹饺子 / spoon 金属勺搭碗边（椭圆勺头+长柄）/ fork 银叉四齿叉苹果块 /
knife 圆钝餐刀搭面包片 / pot 深汤锅盖掀冒气（双耳）/ pan 黑柄平底锅煎饼（饼上黄斑）/
kettle 红色圆水壶提梁+壶嘴蒸汽。
器皿居中放大；金属件用浅灰族色；木质用 WOOD 族；热气一律浅灰白波浪线；主色相邻错开。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "bowl", "cn": "碗"},
    {"w": "plate", "cn": "盘子"},
    {"w": "cup", "cn": "杯子"},
    {"w": "chopsticks", "cn": "筷子"},
    {"w": "spoon", "cn": "勺子"},
    {"w": "fork", "cn": "叉子"},
    {"w": "knife", "cn": "刀"},
    {"w": "pot", "cn": "锅"},
    {"w": "pan", "cn": "平底锅"},
    {"w": "kettle", "cn": "水壶"},
]


# ---------- 本组同族补充色 ----------
STEAM = "#e2dccc"                                              # 热气浅灰白（PAGE 族）
SOUP, SOUP_L = "#f6cf8e", "#fbe3b4"                            # 汤面琥珀（YEL 族浅）
BLUE_DD = "#3d84ad"                                            # 碗口内壁深（BLUE 族深）
PINK_L, PINK_D, PINK_DD = "#fbc0aa", "#e08a6e", "#c9705a"      # 粉杯（PINK 族）
NOO, NOO_D = "#f7eeda", "#e3d3b2"                              # 饺子奶白（WHITE 族）
MET, MET_M, MET_L = "#dfe3e6", "#c9cdd1", "#eef1f3"            # 金属浅灰族
MET_D, MET_DD = "#adb2b7", "#8e939a"                           # 金属灰中/深
MET_BK, MET_BK2 = "#6f757c", "#5f656c"                         # 锅体深灰（同族深）
CRUST, CRUST_D = "#d9a05f", "#c08a4a"                          # 吐司边皮（WOOD 族）
CRUMB, CRUMB_D = "#f6e3bd", "#ecd6a4"                          # 吐司瓤（WOOD_L 族）
FLESH, FLESH_SH = "#fdf3d6", "#ecdcb2"                         # 苹果果肉（白黄浅族）
SKIN_SHINE = "#f2917a"                                         # 果皮高光（RED 族浅）
PANCAKE, PANCAKE_D = "#f2ca74", "#e6b25e"                      # 煎饼（YEL 族浅）
SPOT, SPOT_L = "#d99a2b", "#f8e3ae"                            # 煎饼黄斑（YEL 族）
TEAL_DD = "#2e7a6e"                                            # 锅口内壁深（TEAL 族深）
LID_L = "#a8ddd3"                                              # 锅盖高光（TEAL 族更浅）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色高光椭圆（可旋转）。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


# ---------- 1 bowl 蓝碗热汤冒气 ----------
def art_bowl():
    g = ground()
    g += R(342, 422, 76, 20, 10, BLUE_D)                        # 碗足
    g += P("M 250 268 Q 258 398 380 432 Q 502 398 510 268 Z", BLUE)   # 碗身
    g += shine(306, 330, 22, 54, WBLUE, 0.55, -10)              # 左侧高光
    g += E(380, 268, 130, 27, BLUE_D)                           # 碗沿
    g += E(380, 270, 108, 19, BLUE_DD)                          # 碗口内壁
    g += E(380, 272, 94, 14, SOUP)                              # 热汤
    g += E(380, 271, 78, 10, SOUP_L)
    g += E(338, 270, 8, 4.5, GREEN_L)                           # 葱花
    g += E(412, 273, 7, 4, GREEN_L)
    # 热气（浅灰白波浪线）
    g += P("M 330 252 Q 314 218 332 190 Q 348 164 336 138", stroke=STEAM, w=10)
    g += P("M 378 246 Q 366 216 380 192 Q 392 170 384 150", stroke=STEAM, w=8)
    g += P("M 424 250 Q 410 220 426 194 Q 438 172 428 152", stroke=STEAM, w=9)
    return g


# ---------- 2 plate 白盘煎蛋 ----------
EGG_PATH = ("M 306 302 Q 296 270 330 260 Q 342 234 374 246 Q 398 222 428 242 "
            "Q 458 236 466 266 Q 492 276 482 302 Q 492 330 458 338 Q 448 366 412 356 "
            "Q 384 378 356 358 Q 326 366 318 338 Q 294 330 306 302 Z")


def art_plate():
    g = ground()
    g += E(380, 372, 214, 70, "#e6dfcf")                        # 盘底影
    g += E(380, 358, 206, 64, "#f9f5ea")                        # 盘面
    g += E(380, 360, 168, 50, "#fdfaf0")                        # 盘沿环
    g += E(380, 362, 148, 42, "#efe8d6")                        # 盘凹槽
    g += shine(280, 396, 44, 11, WHITE, 0.7, -14)               # 盘沿高光
    # 蛋白（带软影）
    g += '<g transform="translate(0,10)">' + P(EGG_PATH, "#e7dfcb") + "</g>"
    g += P(EGG_PATH, WHITE)
    g += P("M 320 330 Q 348 352 386 356", stroke=NOO_D, w=5, opacity=0.6)   # 蛋白褶影
    # 蛋黄
    g += C(396, 306, 38, YEL_D)
    g += C(388, 298, 38, YEL)
    g += C(370, 280, 10, "#f8df9c")
    # 热气
    g += P("M 372 212 Q 360 186 374 164 Q 384 148 376 134", stroke=STEAM, w=8)
    g += P("M 412 216 Q 402 192 414 172", stroke=STEAM, w=7)
    return g


# ---------- 3 cup 粉色带把杯冒热气 ----------
def art_cup():
    g = ground()
    # 把手（右侧，先画被杯身压住接口）
    g += P("M 458 300 Q 524 296 520 356 Q 516 408 452 402", stroke=PINK_D, w=17)
    g += P("M 302 252 L 312 408 Q 314 428 336 428 L 424 428 Q 446 428 448 408 L 458 252 Z", PINK)
    g += E(380, 431, 58, 9, PINK_D, 0.9)                        # 杯底
    g += R(318, 270, 15, 122, 7, PINK_L, 0.85)                  # 杯壁高光
    g += E(380, 252, 79, 19, PINK_D)                            # 杯沿
    g += E(380, 253, 64, 13, PINK_DD)                           # 杯口内壁
    # 热气
    g += P("M 344 234 Q 330 202 346 176 Q 360 154 350 132", stroke=STEAM, w=9)
    g += P("M 390 230 Q 378 204 392 180 Q 402 162 394 144", stroke=STEAM, w=8)
    g += P("M 426 236 Q 416 212 428 190", stroke=STEAM, w=7)
    return g


# ---------- 4 chopsticks 两根木筷夹饺子 ----------
def art_chopsticks():
    g = ground()
    g += E(384, 430, 112, 13, "#aed2c1", 0.85)                  # 悬空投影
    # 辅助小碟+酱油
    g += E(172, 428, 84, 16, "#e6dfcf")
    g += E(172, 424, 72, 12, WHITE)
    g += E(172, 422, 50, 9, "#8a5a33")
    # 饺子（月牙形，被夹起悬空，肚腹下垂、脊背鼓褶）
    g += P("M 262 348 Q 268 302 288 290 Q 308 266 332 276 Q 356 258 380 284 "
           "Q 404 272 420 300 Q 448 296 486 320 Q 508 330 498 348 "
           "Q 380 388 262 348 Z", NOO)
    g += shine(322, 318, 24, 15, WHITE, 0.75, -12)              # 左腹高光
    # 脊背捏褶
    g += P("M 290 292 Q 287 306 290 318", stroke=NOO_D, w=4.5)
    g += P("M 332 278 Q 330 294 334 308", stroke=NOO_D, w=5)
    g += P("M 380 286 Q 378 302 382 318", stroke=NOO_D, w=5)
    g += P("M 420 302 Q 418 318 422 332", stroke=NOO_D, w=5)
    # 热气
    g += P("M 296 254 Q 288 228 300 208", stroke=STEAM, w=7)
    g += P("M 490 266 Q 498 242 488 222", stroke=STEAM, w=7)
    # 两根木筷（右上斜下夹住饺子脊背）
    g += L(566, 108, 380, 272, WOOD_D, 12)
    g += L(566, 108, 380, 272, WOOD, 5)
    g += L(610, 136, 392, 262, WOOD_D, 12)
    g += L(610, 136, 392, 262, WOOD, 5)
    return g


# ---------- 5 spoon 金属勺搭碗边 ----------
def art_spoon():
    g = ground()
    # 辅助小碗（左下，蓝）
    g += R(300, 428, 64, 16, 8, BLUE_D)                         # 碗足
    g += P("M 236 388 Q 242 440 340 452 Q 438 440 444 388 Z", BLUE)
    g += E(340, 388, 104, 22, BLUE_D)                           # 碗沿
    g += E(340, 390, 86, 15, BLUE_DD)                           # 碗口内壁
    # 金属长柄勺：头搭碗沿、柄伸向右上
    g += L(326, 372, 600, 162, MET, 26)                         # 长柄
    g += L(334, 378, 594, 171, MET_M, 9)                        # 柄下侧影
    g += ('<g transform="rotate(-37.5 326 372)">'            # 勺头（椭圆+内壁影+高光）
          + E(326, 372, 62, 42, MET)
          + E(326, 378, 46, 28, MET_M)
          + E(308, 356, 18, 10, WHITE, 0.9)
          + "</g>")
    return g


# ---------- 6 fork 银叉叉起苹果块 ----------
def art_fork():
    g = ground()
    g += E(392, 456, 98, 11, "#e6dfcf", 0.7)                    # 苹果块软影
    # 苹果块（奶白果肉+侧边红皮，先画让叉齿压上）
    for x, y, w, h in ((338, 336, 66, 56), (406, 360, 60, 54), (378, 400, 64, 58)):
        g += R(x, y, w, h, 12, FLESH)
        g += R(x + 5, y + h - 12, w - 10, 8, 4, FLESH_SH, 0.8)  # 底部果肉影
        g += R(x + w - 13, y + 5, 13, h - 10, 6, RED)           # 侧边红皮
        g += E(x + w - 9, y + 14, 5, 10, SKIN_SHINE)            # 皮高光
        g += E(x + 16, y + 13, 14, 8, WHITE, 0.7)               # 果肉高光
    # 银叉：柄→喇叭叉头→四长齿（齿朝左下扎入果块）
    fk = wrap(
        R(-13, -176, 26, 152, 12, MET),                         # 柄
        R(-8, -166, 7, 130, 3.5, WHITE, 0.55),                  # 柄高光
        P("M -15 -32 L 15 -32 L 42 8 Q 44 24 28 24 L -28 24 Q -44 24 -42 8 Z", MET),  # 喇叭叉头
        R(-36.5, 22, 13, 86, 6.5, MET),                         # 四齿
        R(-16.5, 22, 13, 86, 6.5, MET),
        R(3.5, 22, 13, 86, 6.5, MET),
        R(23.5, 22, 13, 86, 6.5, MET),
    )
    g += f'<g transform="translate(470,300) rotate(44.5)">{fk}</g>'
    return g


# ---------- 7 knife 圆钝餐刀搭面包片 ----------
def art_knife():
    g = ground()
    # 面包片（平放，边皮+瓤）
    g += R(230, 340, 320, 92, 20, CRUST_D)                      # 侧面厚
    g += P("M 230 344 L 230 280 Q 230 236 286 234 Q 312 216 354 220 Q 380 204 414 218 "
           "Q 462 214 486 232 Q 546 236 546 280 L 546 344 Q 388 368 230 344 Z", CRUST)
    g += P("M 254 336 L 254 282 Q 254 254 296 252 Q 318 238 354 242 Q 380 228 410 240 "
           "Q 450 238 470 254 Q 522 258 522 282 L 522 336 Q 388 354 254 336 Z", CRUMB)
    for dx, dy in ((330, 296), (410, 312), (462, 282), (356, 268)):
        g += E(dx, dy, 5, 4, CRUMB_D, 0.85)                     # 瓤孔
    # 餐刀（横置微斜，圆钝刀尖搭在面包上）
    kn = wrap(
        P("M 128 -26 L -104 -26 Q -178 -22 -178 4 Q -178 30 -108 28 L 128 26 "
          "Q 140 0 128 -26 Z", MET),                            # 圆钝刀身
        P("M 124 0 L -108 0 Q -160 4 -158 13 Q -156 22 -106 21 L 124 21 Z", MET_M),  # 下半刃影
        P("M 118 -19 L -98 -19", stroke=WHITE, w=5, opacity=0.85),                   # 脊线高光
        R(112, -24, 16, 52, 8, MET_M),                          # 刀颈
        R(124, -20, 132, 44, 18, MET_DD),                       # 刀柄
        R(136, -12, 24, 13, 6, MET_D),                          # 柄高光
    )
    g += f'<g transform="translate(390,286) rotate(-16)">{kn}</g>'
    return g


# ---------- 8 pot 深汤锅盖掀冒气（双耳） ----------
def art_pot():
    g = ground()
    # 双耳
    g += P("M 258 306 Q 220 304 222 340 Q 224 370 258 368", stroke=TEAL_D, w=14)
    g += P("M 502 306 Q 540 304 538 340 Q 536 370 502 368", stroke=TEAL_D, w=14)
    g += R(258, 276, 244, 162, 26, TEAL)                        # 深锅身
    g += R(258, 396, 244, 30, 15, TEAL_D)                       # 底部沉色
    g += R(280, 296, 18, 100, 9, TEAL_L, 0.6)                   # 侧高光
    g += E(380, 276, 122, 24, TEAL_D)                           # 锅沿
    g += E(380, 278, 104, 17, TEAL_DD)                          # 锅口内壁
    g += E(326, 280, 52, 10, SOUP)                              # 掀缝处的汤
    g += E(316, 279, 34, 6, SOUP_L)
    # 掀开的锅盖（斜搭右沿）
    lid = wrap(
        E(444, 264, 96, 22, TEAL_D),
        E(444, 254, 88, 18, TEAL_L),
        E(424, 250, 20, 8, LID_L, 0.8),
        R(431, 222, 26, 16, 8, TEAL_D),
        C(444, 224, 6, TEAL_L),
    )
    g += f'<g transform="rotate(-16 444 262)">{lid}</g>'
    # 锅口冒气
    g += P("M 306 262 Q 292 232 308 204 Q 322 180 312 156", stroke=STEAM, w=10)
    g += P("M 344 258 Q 332 230 346 206 Q 356 186 348 168", stroke=STEAM, w=9)
    g += P("M 284 264 Q 274 242 284 222", stroke=STEAM, w=7)
    return g


# ---------- 9 pan 黑柄平底锅煎饼（饼上黄斑） ----------
def art_pan():
    g = ground()
    # 黑柄（先画，接口压在锅下）
    g += L(468, 228, 636, 140, "#565b62", 36)
    g += L(478, 232, 616, 152, "#767c83", 7)
    g += C(622, 146, 8, PAGE)                                   # 挂孔
    # 锅体（俯视）
    g += C(368, 328, 146, MET_BK)
    g += C(368, 326, 134, MET_BK2)
    g += P("M 262 302 Q 296 286 336 292", stroke="#9aa0a7", w=5, opacity=0.7)   # 油光
    g += P("M 448 372 Q 420 386 392 380", stroke="#9aa0a7", w=5, opacity=0.7)
    # 煎饼+黄斑
    g += C(352, 322, 100, PANCAKE_D)
    g += C(348, 318, 98, PANCAKE)
    g += shine(318, 282, 30, 11, SPOT_L, 0.9, -12)
    for dx, dy, rx, ry in ((312, 298, 10, 7), (390, 292, 9, 6), (372, 354, 11, 7),
                           (302, 342, 8, 6), (418, 334, 8, 6)):
        g += E(dx, dy, rx, ry, SPOT)
    for dx, dy in ((352, 312), (330, 362)):
        g += E(dx, dy, 7, 5, SPOT_L, 0.9)
    # 热气
    g += P("M 330 214 Q 318 188 332 164 Q 342 146 334 130", stroke=STEAM, w=9)
    g += P("M 378 210 Q 368 186 380 164", stroke=STEAM, w=8)
    return g


# ---------- 10 kettle 红色圆水壶（提梁+壶嘴蒸汽） ----------
def art_kettle():
    g = ground()
    g += E(380, 446, 74, 12, RED_D)                             # 底座圈
    # 提梁（金属灰，拱过壶盖）
    g += P("M 292 282 Q 376 60 460 282", stroke=MET_DD, w=16)   # 提梁
    # 壶身（圆）
    g += E(380, 338, 124, 112, RED_D)
    g += E(378, 334, 120, 106, RED)
    g += shine(328, 300, 26, 50, SKIN_SHINE, 0.7, -14)
    g += E(446, 396, 38, 24, RED_D, 0.3)
    # 壶嘴（右上，嘴口张开）
    g += P("M 492 296 Q 544 262 558 206 L 528 198 Q 510 242 474 268 Z", RED)
    g += P("M 500 284 Q 532 256 546 218", stroke=SKIN_SHINE, w=5, opacity=0.8)
    g += '<g transform="rotate(-30 544 202)">' + E(544, 202, 16, 11, RED_D) + "</g>"
    # 壶盖+钮
    g += E(380, 228, 56, 14, RED_D)
    g += E(380, 216, 44, 16, RED)
    g += C(380, 196, 13, RED_D)
    g += C(376, 192, 5, SKIN_SHINE)
    # 壶嘴蒸汽
    g += P("M 544 188 Q 530 160 544 134 Q 556 112 546 92", stroke=STEAM, w=10)
    g += P("M 570 194 Q 560 168 572 144", stroke=STEAM, w=8)
    g += P("M 522 192 Q 514 168 524 148", stroke=STEAM, w=7)
    return g


def arts():
    return {
        "bowl": art_bowl(),
        "plate": art_plate(),
        "cup": art_cup(),
        "chopsticks": art_chopsticks(),
        "spoon": art_spoon(),
        "fork": art_fork(),
        "knife": art_knife(),
        "pot": art_pot(),
        "pan": art_pan(),
        "kettle": art_kettle(),
    }
