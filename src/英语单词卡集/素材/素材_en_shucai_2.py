#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 蔬菜（shucai）第 2 段插画（10 卡：eggplant~peanut）。

每卡造型要点：eggplant 深紫亮皮弯把绿萼 / cucumber 深绿条形刺点，旁立切一段露浅瓤 /
pea 黄绿豆荚裂口露圆豆排，散两粒 / green bean 草绿两根弯豆荚并排，荚内豆痕 /
chili 鲜红弯尖发亮，绿萼把 / lettuce 浅绿波浪散叶丛 / spinach 深绿成把束带红根 /
radish 白身青缨半埋土丘 / cauliflower 白花菜球面凸点衬大叶 / peanut 黄褐网纹壳裂口露红衣仁。
主体居中放大，辅件不喧宾夺主；主色相邻错开，与上段第 10 张白蒜衔接。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "eggplant", "cn": "茄子"},
    {"w": "cucumber", "cn": "黄瓜"},
    {"w": "pea", "cn": "豌豆"},
    {"w": "green bean", "cn": "四季豆"},
    {"w": "chili", "cn": "辣椒"},
    {"w": "lettuce", "cn": "生菜"},
    {"w": "spinach", "cn": "菠菜"},
    {"w": "radish", "cn": "白萝卜"},
    {"w": "cauliflower", "cn": "花菜"},
    {"w": "peanut", "cn": "花生"},
]


# ---------- 本组同族补充色 ----------
STEMG = "#5d8a52"                                                 # 绿族深（把/萼/叶脉）
EGG, EGG_D, EGG_L = "#7a4a9c", "#5f3679", "#c4a6dc"               # 茄深紫（紫族，接上段葡萄/李族）
CUC, CUC_D, CUC_L = "#578a48", "#416b35", "#a3cc8e"               # 黄瓜深绿（GREEN 族深）
CUC_F = "#e4efc9"                                                 # 切面浅瓤（绿族极浅）
POD, POD_D, POD_IN = "#b8c455", "#96a23e", "#e3e79b"              # 豆荚黄绿（GREEN×YEL 族）
PEAD = "#628a54"                                                  # 豆豆暗部（GREEN 族）
GB, GB_D, GB_L = "#7fae70", "#628a54", "#b5d9a0"                  # 四季豆草绿（GREEN 族）
CHILI, CHILI_D, CHILI_L = "#e2574a", "#c43a30", "#f59b78"         # 辣椒鲜红（RED 族）
LG, LG_D, LG_L = "#9cc98a", "#7fae70", "#c6e2b0"                  # 生菜浅绿（GREEN 族浅）
SPIN, SPIN_D, SPIN_L = "#4f7d44", "#3b6133", "#8fb87e"            # 菠菜深绿（GREEN 族更深）
SPST = "#c9dba6"                                                  # 菠菜茎浅绿
SOIL, SOIL_D = "#b57b44", "#a06536"                               # 土丘棕（WOOD 族）
RADF, RADF_D = "#f3eedd", "#ddd5c0"                               # 萝卜白身（WHITE 暖族）
CFD, CFD_D, CF_B = "#f6f1e1", "#ddd2b4", "#fbf8ec"                # 花菜奶白（WHITE 暖族）
CF_DOT = "#e0d5b5"                                                # 花菜凸点影
PN, PN_D, PN_L = "#d9a866", "#b98a4c", "#f0cd93"                  # 花生黄褐（WOOD 族）
KRN, KRN_L = "#cf5646", "#f0968a"                                 # 花生红衣（RED 族）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色斜高光椭圆。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


def lleaf(cx, by, w, h, col, rot=0, vein=None):
    """波浪圆齿叶：底脚 (cx,by)，上宽下窄喇叭形，顶部三圆凸，可带中脉。"""
    d = (f"M {cx-w*0.5} {by} "
         f"Q {cx-w*0.5-10} {by-h*0.5} {cx-w*0.42} {by-h*0.62} "
         f"Q {cx-w*0.5} {by-h*0.95} {cx-w*0.24} {by-h*0.85} "
         f"Q {cx-w*0.06} {by-h*1.06} {cx+w*0.1} {by-h*0.88} "
         f"Q {cx+w*0.34} {by-h*1.02} {cx+w*0.42} {by-h*0.62} "
         f"Q {cx+w*0.5+10} {by-h*0.5} {cx+w*0.5} {by} Z")
    s = P(d, col)
    if vein:
        s += L(cx, by - h * 0.55, cx, by - 16, vein, 4)
    if rot:
        return f'<g transform="rotate({rot} {cx} {by})">' + s + "</g>"
    return s


# ---------- 11 eggplant 深紫亮皮，弯把绿萼 ----------
def art_eggplant():
    g = ground()
    # 果身：上小下大泪滴形（深一号衬底 + 本体）
    g += E(390, 246, 82, 78, EGG_D) + E(396, 330, 114, 108, EGG_D) + R(346, 274, 92, 120, 42, EGG_D)
    g += E(382, 238, 80, 76, EGG) + E(388, 322, 112, 108, EGG) + R(338, 268, 88, 120, 42, EGG)
    g += E(384, 164, 15, 7, EGG_D)                          # 顶部凹陷
    # 亮皮高光
    g += shine(338, 272, 18, 42, EGG_L, 0.75, -18)
    g += shine(326, 372, 12, 26, EGG_L, 0.45, -14)
    g += shine(446, 306, 12, 30, EGG_L, 0.35, 18)
    # 弯把
    g += P("M 384 166 Q 396 136 434 124", stroke=STEMG, w=13)
    # 绿萼四片垂披果顶
    for a, col in ((-55, STEMG), (-20, GREEN), (20, GREEN), (55, STEMG)):
        g += f'<g transform="rotate({a} 384 172)">' + E(384, 204, 13, 34, col) + "</g>"
    g += C(384, 172, 11, STEMG)
    return g


# ---------- 12 cucumber 深绿条形刺点 + 切一段 ----------
def art_cucumber():
    g = ground()
    body = wrap(
        R(-206, -56, 412, 112, 56, CUC_D),
        R(-212, -62, 412, 112, 56, CUC),
        L(-180, -26, 180, -26, CUC_D, 7),
        L(-186, 0, 186, 0, CUC_D, 6),
        L(-180, 26, 180, 26, CUC_D, 7),
        C(-196, 2, 10, "#3d5c33"),                          # 蒂疤
        E(-120, -24, 42, 12, CUC_L, 0.5),
    )
    for dx, dy in ((-150, 12), (-100, -14), (-60, 24), (-10, -4), (40, -24),
                   (80, 16), (130, -6), (160, 22), (-30, 20), (10, -28)):
        body += C(dx, dy, 5, CUC_L) + C(dx, dy, 2.2, CUC_D, 0.6)   # 刺点
    g += f'<g transform="translate(356,310) rotate(-20)">{body}</g>'
    # 切一段（辅）：立着的瓜段，顶面浅瓤带籽
    g += R(566, 336, 70, 100, 20, CUC_D) + R(560, 330, 70, 100, 20, CUC)
    g += E(595, 331, 34, 13, CUC_F) + E(595, 331, 23, 8.5, "#f2f7dd")
    for sx in (580, 595, 610):
        g += E(sx, 331, 4, 6.5, CUC_L, 0.95)
    return g


# ---------- 13 pea 黄绿豆荚裂口露圆豆排 ----------
def art_pea():
    g = ground()
    pod = wrap(
        P("M -186 -12 Q -146 -44 0 -50 Q 146 -44 186 -12 Q 154 92 0 104 Q -154 92 -186 -12 Z", POD_D),
        P("M -191 -18 Q -151 -50 0 -56 Q 141 -50 181 -18 Q 149 86 0 98 Q -159 86 -191 -18 Z", POD),
        P("M -160 -10 Q -126 -34 0 -38 Q 126 -34 160 -10 Q 132 68 0 78 Q -132 68 -160 -10 Z", POD_IN),
    )
    for px, py, r in ((-110, 2, 33), (-56, 14, 34), (0, 18, 34), (56, 14, 34), (110, 2, 33)):
        pod += C(px + 3, py + 4, r, PEAD)
        pod += C(px, py, r - 1, GREEN)
        pod += C(px - r * 0.3, py - r * 0.32, r * 0.22, GREEN_L, 0.9)
    pod += P("M -186 -12 L -208 -17", stroke=STEMG, w=8)        # 左柄尖
    pod += P("M 186 -12 Q 224 -26 216 -56", stroke=STEMG, w=8)  # 右卷须
    g += f'<g transform="translate(368,280) rotate(-30)">{pod}</g>'
    for px, py, r in ((142, 420, 26), (596, 414, 23)):          # 散落两粒
        g += C(px + 3, py + 4, r, PEAD) + C(px, py, r - 1, GREEN)
        g += C(px - 8, py - 9, 6, GREEN_L, 0.9)
    return g


# ---------- 14 green bean 草绿两根弯豆荚并排 ----------
GBEAN = "M -230 30 Q -80 110 90 76 Q 186 55 232 -16 Q 175 30 66 41 Q -106 53 -230 30 Z"


def art_green_bean():
    g = ground()
    for tx, ty, rot in ((358, 322, -14), (408, 182, 6)):
        bean = f'<g transform="translate({tx},{ty}) rotate({rot})">'
        bean += f'<g transform="translate(5,8)">{P(GBEAN, GB_D)}</g>'
        bean += P(GBEAN, GB)
        bean += L(-150, 40, -40, 50, GB_L, 4) + L(-20, 48, 80, 40, GB_L, 4)
        for bx, by in ((-120, 68), (-40, 74), (40, 64)):        # 荚内豆痕
            bean += E(bx, by, 15, 9, GB_L, 0.5)
        bean += C(-226, 28, 7, "#8a5a33")                       # 果柄点
        bean += P("M 232 -16 Q 254 -24 260 -46", stroke=GB_D, w=6)  # 小卷尖
        bean += "</g>"
        g += bean
    return g


# ---------- 15 chili 鲜红弯尖发亮，绿萼把 ----------
CHILIB = ("M 332 188 Q 296 268 318 336 Q 344 420 448 436 L 464 422 "
          "Q 402 402 388 332 Q 378 262 398 190 Z")


def art_chili():
    g = ground()
    g += f'<g transform="translate(7,9)">{P(CHILIB, CHILI_D)}</g>'
    g += P(CHILIB, CHILI)
    g += shine(342, 278, 10, 40, CHILI_L, 0.65, -8)             # 纵向亮条
    g += shine(368, 382, 9, 24, CHILI_L, 0.5, -24)
    g += C(350, 222, 7, CHILI_L, 0.6)
    # 绿把：果梗 + 萼帽 + 三小萼片披果肩
    g += P("M 360 184 Q 350 150 366 120", stroke=STEMG, w=12)
    g += E(364, 188, 42, 17, STEMG)
    for a in (-28, 0, 28):
        g += f'<g transform="rotate({a} 364 192)">' + E(364, 206, 8, 15, "#4c7a44") + "</g>"
    return g


# ---------- 16 lettuce 浅绿波浪散叶丛 ----------
def art_lettuce():
    g = ground()
    # 后排深叶，外圈叶向外倾
    g += lleaf(255, 390, 170, 190, LG_D, rot=-14)
    g += lleaf(505, 390, 170, 190, LG_D, rot=14)
    g += lleaf(380, 382, 180, 215, LG_D)
    g += E(380, 390, 172, 40, LG_D)                             # 叶基裙（补缝）
    # 中排主叶带中脉
    g += lleaf(300, 400, 160, 180, LG, rot=-8, vein=LG_L)
    g += lleaf(462, 400, 160, 180, LG, rot=8, vein=LG_L)
    # 基部短梗
    g += E(380, 404, 54, 20, LG_D) + E(380, 406, 34, 16, "#dcebc4")
    # 前排最浅嫩叶
    g += lleaf(352, 412, 150, 150, LG_L, rot=-4, vein="#eaf4da")
    g += lleaf(430, 412, 140, 145, LG_L, rot=4, vein="#eaf4da")
    return g


# ---------- 17 spinach 深绿叶成把，红根 ----------
def spade(x, y, rx, ry, rot, col):
    """菠菜铲形叶：上尖下圆，带浅色中脉。"""
    d = (f"M {x} {y-ry} Q {x+rx} {y-ry*0.55} {x+rx*0.8} {y+ry*0.45} "
         f"Q {x+rx*0.35} {y+ry} {x} {y+ry} "
         f"Q {x-rx*0.35} {y+ry} {x-rx*0.8} {y+ry*0.45} "
         f"Q {x-rx} {y-ry*0.55} {x} {y-ry} Z")
    return (f'<g transform="rotate({rot} {x} {y})">' + P(d, col)
            + L(x, y - ry * 0.72, x, y + ry * 0.72, SPIN_L, 3.5) + "</g>")


def art_spinach():
    g = ground()
    for x2, y2 in ((292, 300), (348, 268), (412, 272), (466, 312)):   # 茎丛
        g += L(380, 408, x2, y2, SPST, 10)
    g += L(380, 408, 380, 330, SPST, 10)
    g += spade(290, 248, 44, 60, -20, SPIN_D)
    g += spade(468, 260, 44, 60, 22, SPIN_D)
    g += spade(346, 214, 46, 64, -8, SPIN)
    g += spade(414, 220, 46, 64, 10, SPIN)
    g += spade(378, 260, 54, 78, 0, SPIN)
    g += R(354, 384, 52, 26, 12, "#f2b03c") + R(354, 384, 52, 9, 5, "#e8a13c")  # 束带
    g += E(380, 414, 18, 10, "#e08573")                              # 红根颈
    for rx1, ry1, rx2, ry2 in ((370, 420, 364, 438), (380, 422, 381, 442), (390, 420, 396, 437)):
        g += L(rx1, ry1, rx2, ry2, RED_D, 5)                         # 红根须
    return g


# ---------- 18 radish 白身青缨，半埋土丘 ----------
def art_radish():
    g = ground()
    # 青缨（先画，身顶压住叶脚）
    g += lleaf(282, 246, 62, 96, GREEN_L, rot=-12)
    g += lleaf(488, 248, 60, 92, GREEN_L, rot=12)
    g += lleaf(326, 238, 78, 128, GREEN, rot=-6)
    g += lleaf(450, 240, 74, 120, GREEN, rot=6)
    g += lleaf(384, 230, 84, 142, GREEN)
    # 白身（深衬 + 本体，下端收在土丘弦线内）
    g += P("M 284 240 Q 272 332 302 402 Q 330 440 380 440 Q 430 440 458 402 "
           "Q 488 332 476 240 Q 438 210 380 210 Q 322 210 284 240 Z", RADF_D)
    g += P("M 278 234 Q 266 330 296 402 Q 324 436 380 436 Q 436 436 464 402 "
           "Q 494 330 482 234 Q 440 204 380 204 Q 320 204 278 234 Z", RADF)
    g += P("M 300 288 Q 380 302 460 288", stroke="#e4dcc4", w=6)     # 浅环纹
    g += P("M 294 322 Q 380 338 466 322", stroke="#e4dcc4", w=5)
    g += shine(324, 268, 14, 34, WHITE, 0.8, -12)
    g += E(464, 306, 10, 40, "#e2dac2", 0.55)
    # 土丘（盖住下半截）
    g += P("M 204 438 Q 262 366 380 362 Q 498 366 556 438 Z", SOIL)
    for dx, dy, r in ((270, 402, 7), (330, 384, 5), (420, 388, 6), (480, 408, 7), (380, 376, 4)):
        g += C(dx, dy, r, SOIL_D)
    return g


# ---------- 19 cauliflower 白花菜球面凸点，衬大叶 ----------
def art_cauliflower():
    g = ground()
    # 后侧两片大叶（环抱球底）
    g += P("M 266 436 Q 198 398 188 322 Q 192 278 226 286 Q 274 340 292 436 Z", GREEN)
    g += P("M 494 436 Q 562 398 572 322 Q 568 278 534 286 Q 486 340 468 436 Z", GREEN)
    g += L(224, 306, 268, 424, STEMG, 5) + L(536, 306, 492, 424, STEMG, 5)
    g += R(348, 418, 64, 28, 12, "#e8dfc6")                  # 短茎
    # 花球：深衬 + 奶白球面 + 凸点簇
    g += E(388, 324, 165, 118, CFD_D) + E(380, 316, 163, 118, CFD)
    bumps = [(316, 220, 22), (384, 210, 24), (444, 224, 20),
             (280, 262, 23), (350, 256, 25), (420, 252, 23), (482, 268, 21),
             (258, 314, 21), (330, 306, 24), (402, 306, 22), (468, 318, 20),
             (292, 362, 23), (366, 356, 25), (438, 364, 21), (248, 362, 13), (512, 368, 12)]
    for bx, by, br in bumps:
        g += C(bx, by, br, CF_B)
    for bx, by in ((316, 220), (384, 210), (444, 224), (350, 256), (420, 252),
                   (330, 306), (402, 306), (366, 356), (292, 362)):
        g += C(bx + 5, by + 4, 5.5, CF_DOT)
    # 前侧浅叶护球底
    g += P("M 252 440 Q 226 390 250 338 Q 296 354 304 440 Z", GREEN_L)
    g += P("M 508 440 Q 534 390 510 338 Q 464 354 456 440 Z", GREEN_L)
    return g


# ---------- 20 peanut 黄褐网纹壳，裂口露红衣仁 ----------
PNUT = ("M 375 136 Q 292 140 286 206 Q 281 254 326 278 Q 348 288 328 300 "
        "Q 284 330 290 378 Q 298 424 375 428 "
        "Q 452 424 460 378 Q 466 330 422 300 "
        "Q 402 288 422 278 Q 469 254 464 206 Q 458 140 375 136 Z")


def art_peanut():
    g = ground()
    g += f'<g transform="translate(7,9)">{P(PNUT, PN_D)}</g>'
    g += P(PNUT, PN)
    for x1, y1, x2, y2 in ((300, 170, 336, 222), (328, 158, 360, 206), (290, 214, 320, 258),
                           (352, 228, 380, 262), (358, 164, 326, 214), (334, 212, 304, 254),
                           (382, 178, 356, 222), (312, 332, 344, 382), (340, 364, 368, 408),
                           (298, 372, 326, 412), (424, 336, 394, 386), (446, 364, 418, 408),
                           (408, 394, 382, 420)):
        g += L(x1, y1, x2, y2, PN_D, 3.5)                    # 网纹
    g += P("M 340 292 Q 375 300 412 292", stroke=PN_D, w=4)  # 腰缝
    # 裂口（右上）+ 红衣仁探出
    g += P("M 396 152 Q 428 170 436 212 Q 440 244 424 264 L 406 252 "
           "Q 418 224 412 192 Q 408 168 398 158 Z", "#7a4c26")
    g += f'<g transform="rotate(24 456 198)">' + E(456, 198, 23, 34, KRN) + "</g>"
    g += E(450, 186, 9, 15, KRN_L, 0.85)
    # 壳面高光
    g += shine(330, 186, 20, 36, PN_L, 0.7, -24)
    g += shine(322, 366, 16, 30, PN_L, 0.5, -20)
    # 地上一粒剥好的红衣仁
    g += C(576, 402, 19, KRN) + C(591, 411, 16, KRN)
    g += C(570, 396, 6, KRN_L, 0.85) + C(586, 406, 5, KRN_L, 0.85)
    return g


def arts():
    return {
        "eggplant": art_eggplant(),
        "cucumber": art_cucumber(),
        "pea": art_pea(),
        "green bean": art_green_bean(),
        "chili": art_chili(),
        "lettuce": art_lettuce(),
        "spinach": art_spinach(),
        "radish": art_radish(),
        "cauliflower": art_cauliflower(),
        "peanut": art_peanut(),
    }
