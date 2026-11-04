#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 家庭·人物（jiaren）第 2 段插画（10 卡：man~postman）。

每卡造型要点：man kid 放大+胡茬挥手指天（动效弧线）/ woman kid+丸子头挎紫裙菜篮 /
teacher kid 指身后深绿小黑板（粉笔槽）/ student kid 坐小课桌前双手举手（桌上课本）/
doctor kid 白大褂到膝+领口内衬+听诊器+胸袋 / nurse kid 深粉裙白围裙+白护士帽红十字+端药碗 /
farmer kid 草帽怀抱绿条纹大西瓜 / firefighter kid 红盔黄徽+反光条+肩后红水管卷 /
policeman kid 藏蓝警帽黄徽+抬臂横掌示停 / postman kid 深蓝制服斜挎邮包手递白信。
人物全高 55%~78%，脚底 436~441；所有元素收在 y≤480 画布内不靠裁切；
相邻主色错开：灰蓝/紫粉/深绿+黑板/橙红/白/深粉白/黄棕+绿瓜/蓝衣红盔/藏蓝/邮差蓝棕包。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "man", "cn": "男人"},
    {"w": "woman", "cn": "女人"},
    {"w": "teacher", "cn": "老师"},
    {"w": "student", "cn": "学生"},
    {"w": "doctor", "cn": "医生"},
    {"w": "nurse", "cn": "护士"},
    {"w": "farmer", "cn": "农民"},
    {"w": "firefighter", "cn": "消防员"},
    {"w": "policeman", "cn": "警察"},
    {"w": "postman", "cn": "邮递员"},
]


# ---------- 本组同族补充色 ----------
BLUE_G = "#7f9fbe"                    # 灰蓝（BLUE 族灰调，man 衬衫）
PURPLE, PURPLE_D = "#9d85cf", "#8870b8"  # 紫（woman 裙，词库指定紫裙）
BOARD = "#3f7259"                     # 黑板深绿（GREEN/TEAL 族深）
GREEN_D = "#66965a"                   # 瓜纹深绿（GREEN 族深）
PINK_D = "#e58a70"                    # 深粉（PINK 族深，nurse 裙）
NAVY, NAVY_D = "#3d5f85", "#2f4c6e"   # 藏蓝（BLUE 族深调，police）
POST_B = "#5d89ad"                    # 邮差蓝（BLUE 族中调）
STEEL = "#5a6b7a"                     # 听诊器灰蓝（NAVY 族浅）
BTN = "#9db6cc"                       # 衣扣灰蓝（BLUE 族灰浅）
WHITE_D = "#e9e5d8"                   # 白族深（白褂阴影/围裙沿）


# ---------- 12 man 高个成年男挥手 ----------
def art_man():
    g = ground()
    g += kid(x=380, y=434, s=1.25, mustache=True, hair_color=INK,
             arms="point", point_at=(566, 108), shirt=BLUE_G)
    # 挥手动效弧线（手旁两道）
    g += P("M 549 126 Q 563 146 554 168", stroke=INK, w=5)
    g += P("M 570 112 Q 586 140 574 168", stroke=INK, w=5)
    return g


# ---------- 13 woman 成年女挎篮买菜 ----------
def art_woman():
    g = ground()
    g += kid(x=380, y=436, s=1.15, bun=True, shirt=PINK)
    # 紫裙（盖住腿部上段）
    g += P("M 322 300 L 438 300 L 450 368 L 310 368 Z", PURPLE)
    g += R(310, 352, 140, 16, 8, PURPLE_D)
    # 手挎菜篮（左手边）
    g += P("M 274 350 Q 306 314 338 350", stroke=WOOD_D, w=8)
    g += P("M 268 352 Q 272 396 306 398 Q 340 396 344 352 Z", WOOD)
    g += P("M 272 368 Q 306 376 340 368", stroke=WOOD_D, w=4)
    g += P("M 276 384 Q 306 390 336 384", stroke=WOOD_D, w=4)
    g += C(290, 344, 12, GREEN)
    g += C(318, 342, 10, RED)
    g += E(306, 352, 40, 10, WOOD_D)
    return g


# ---------- 14 teacher 老师指小黑板 ----------
def art_teacher():
    g = ground()
    # 身后小黑板：木框 + 深绿板面 + 粉笔槽
    g += R(150, 96, 300, 210, 18, WOOD_D)
    g += R(166, 112, 268, 178, 10, BOARD)
    g += P("M 204 156 Q 226 144 248 156 Q 270 168 292 156", stroke=WHITE, w=5)
    g += P("M 214 196 Q 248 184 282 196", stroke=WHITE, w=5)
    g += R(240, 306, 120, 14, 7, WOOD_L)
    g += R(268, 300, 26, 9, 4, WHITE)
    # 老师指板
    g += kid(x=545, y=436, s=1.15, arms="point", point_at=(300, 200), shirt=GREEN)
    return g


# ---------- 15 student 课桌前举手娃 ----------
def art_student():
    g = ground()
    g += kid(x=380, y=438, s=0.95, pose="sit", arms="up", face="open", shirt=RED)
    # 小课桌（身前）：桌腿 + 桌面
    g += R(272, 336, 26, 100, 10, WOOD_D)
    g += R(462, 336, 26, 100, 10, WOOD_D)
    g += R(256, 312, 248, 24, 11, WOOD)
    g += R(288, 296, 44, 16, 5, TEAL)
    g += R(338, 298, 40, 14, 5, BLUE)
    return g


# ---------- 16 doctor 白大褂挂听诊器 ----------
def art_doctor():
    g = ground()
    # 白褂下摆底影（先铺，制造深一号偏移）
    g += P("M 318 310 Q 380 322 442 310 L 450 390 Q 380 402 310 390 Z", WHITE_D)
    g += kid(x=380, y=436, s=1.2, shirt=WHITE, hair_color=INK)
    # 白大褂下摆（肩到膝）
    g += P("M 322 312 Q 380 322 438 312 L 444 384 Q 380 396 316 384 Z", WHITE)
    # 白褂侧影
    g += P("M 322 242 Q 316 286 324 320 L 338 318 Q 330 286 336 244 Z", WHITE_D)
    g += P("M 438 242 Q 444 286 436 320 L 422 318 Q 430 286 424 244 Z", WHITE_D)
    # 领口内衬 + 衣扣 + 胸袋
    g += P("M 356 234 L 380 274 L 404 234 Q 380 224 356 234 Z", BLUE_G)
    g += C(380, 288, 6.5, BTN)
    g += C(380, 354, 6.5, BTN)
    g += R(406, 330, 34, 32, 7, WHITE_D)
    # 听诊器：颈挂 U 管 + 听头
    g += P("M 350 238 Q 348 300 380 308 Q 412 300 410 238", stroke=STEEL, w=8)
    g += C(380, 318, 14, STEEL) + C(380, 318, 7, "#c9ccd4")
    return g


# ---------- 17 nurse 护士帽端药碗 ----------
def art_nurse():
    g = ground()
    g += kid(x=380, y=436, s=1.15, shirt=PINK_D, arms="clap")
    # 白围裙（加宽加长，盖到大腿）
    g += P("M 350 288 L 410 288 L 420 380 L 340 380 Z", WHITE)
    # 药碗（双手端，碗沿压住指尖）
    g += P("M 330 296 Q 336 338 380 340 Q 424 338 430 296 Q 380 308 330 296 Z", "#8fc6e8")
    g += E(380, 296, 50, 11, "#a9d8ef")
    g += R(376, 308, 8, 22, 2, RED)
    g += R(369, 317, 22, 8, 2, RED)
    # 白护士帽：帽带 + 红十字（两根交叉矩形）
    g += R(344, 84, 72, 24, 10, WHITE)
    g += R(376, 88, 8, 17, 2, RED)
    g += R(371.5, 92.5, 17, 8, 2, RED)
    return g


# ---------- 18 farmer 草帽农人抱大西瓜 ----------
def art_farmer():
    g = ground()
    g += kid(x=380, y=436, s=1.15, shirt=WOOD_L, arms="cross")
    # 大西瓜（怀抱，画在手臂之后）
    g += ball(380, 310, 62, main=GREEN, dark=GREEN_D, hi=GREEN_L)
    g += P("M 380 250 Q 380 310 380 370", stroke=GREEN_D, w=10)
    g += P("M 346 258 Q 330 310 346 362", stroke=GREEN_D, w=10)
    g += P("M 414 258 Q 430 310 414 362", stroke=GREEN_D, w=10)
    g += P("M 380 246 Q 386 234 396 236", stroke=WOOD_D, w=7)
    # 草帽：宽檐 + 帽顶 + 红帽带
    g += E(380, 84, 46, 26, YEL_D)
    g += E(380, 102, 94, 20, YEL)
    g += R(336, 92, 88, 11, 5, RED)
    return g


# ---------- 19 firefighter 红盔背水管 ----------
def art_firefighter():
    g = ground()
    # 肩后橙红水管卷（画在人前面之前 = 背在身后）
    g += C(462, 196, 50, RED_D)
    g += C(462, 196, 38, RED)
    g += C(462, 196, 14, PAGE)
    g += P("M 498 232 Q 514 278 498 316", stroke=RED_D, w=13)
    g += kid(x=380, y=436, s=1.2, shirt=BLUE_D, hair_color=INK)
    # 战斗服反光条
    g += R(322, 306, 116, 14, 7, YEL)
    # 红头盔：半圆盔 + 帽檐 + 黄徽圆点
    g += P("M 317 100 Q 317 56 380 56 Q 443 56 443 100 Z", RED)
    g += R(314, 98, 132, 13, 6, RED_D)
    g += C(380, 82, 10, YEL)
    return g


# ---------- 20 policeman 抬臂横掌示停 ----------
def art_policeman():
    g = ground()
    g += kid(x=380, y=436, s=1.2, shirt=NAVY, hair_color=INK,
             arms="point", point_at=(620, 150))
    # 藏蓝警帽：帽冠 + 帽箍 + 帽檐 + 黄徽圆点
    g += R(320, 62, 120, 40, 15, NAVY)
    g += R(320, 90, 120, 12, 6, NAVY_D)
    g += R(312, 100, 136, 12, 6, NAVY_D)
    g += C(380, 80, 10, YEL)
    # 前伸横掌（盖住 point 手圆，掌心向前的扁掌）
    g += ('<g transform="translate(527,193) rotate(-27)">'
          + R(-23, -27, 46, 54, 20, SKIN) + E(-28, -8, 9, 12, SKIN) + "</g>")
    return g


# ---------- 21 postman 挎包递信 ----------
def art_postman():
    g = ground()
    g += kid(x=380, y=436, s=1.15, shirt=POST_B, arms="point", point_at=(566, 322))
    # 斜挎背带 + 邮包（棕方包，白信探出，信上无文字）
    g += L(430, 252, 366, 350, WOOD_D, 13)
    g += R(304, 320, 46, 32, 4, WHITE)
    g += P("M 310 328 L 327 343 L 344 328", stroke="#d9d5c8", w=3)
    g += R(288, 344, 80, 64, 12, WOOD)
    g += R(288, 344, 80, 24, 10, WOOD_D)
    g += C(360, 356, 6, WOOD_L)
    # 手递的一封信（白信封 + 红心封蜡）
    g += ('<g transform="translate(521,295) rotate(27)">'
          + R(-25, -34, 50, 68, 6, WHITE)
          + P("M -25 -12 L 0 6 L 25 -12", stroke="#d9d5c8", w=3)
          + heart(0, -16, 7, RED) + "</g>")
    return g


def arts():
    return {
        "man": art_man(),
        "woman": art_woman(),
        "teacher": art_teacher(),
        "student": art_student(),
        "doctor": art_doctor(),
        "nurse": art_nurse(),
        "farmer": art_farmer(),
        "firefighter": art_firefighter(),
        "policeman": art_policeman(),
        "postman": art_postman(),
    }
