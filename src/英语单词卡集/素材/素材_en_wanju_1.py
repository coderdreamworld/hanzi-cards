#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 玩具（wanju）第 1 段插画（11 卡：toy~slide）。

每卡造型要点：toy 木玩具箱盖掀开玩具满出顶（球积木泰迪头星星魔法棒）/
ball 红白弧条大沙滩球 / balloon 红气球飘线白云衬 / doll 粉衣花裙娃娃坐姿
（kid 组件+发髻蝴蝶结裙上小花）/ teddy bear 棕泰迪圆耳坐姿露肚皮 /
kite 燕子风筝双翼叉尾牵线地上线轴 / blocks 四色积木叠塔顶球+旁斜靠一块 /
robot 方头机器人天线蓝耳红顶灯履带轮 / puzzle 青底拼图缺一块+旁边红拼块 /
yoyo 黄盘红心悠悠球顺线手握上下 / slide 红滑梯扶手平台木梯+kid 坐姿下滑。
设施与运动本身为主，kid 用组件；主体居中放大，相邻主色错开，每卡第一笔
ground()；无描边无渐变，图上无文字数字。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "toy", "cn": "玩具"},
    {"w": "ball", "cn": "球"},
    {"w": "balloon", "cn": "气球"},
    {"w": "doll", "cn": "洋娃娃"},
    {"w": "teddy bear", "cn": "泰迪熊"},
    {"w": "kite", "cn": "风筝"},
    {"w": "blocks", "cn": "积木"},
    {"w": "robot", "cn": "机器人"},
    {"w": "puzzle", "cn": "拼图"},
    {"w": "yoyo", "cn": "悠悠球"},
    {"w": "slide", "cn": "滑梯"},
]


# ---------- 本组同族补充色 ----------
WOOD_TAN = "#f4d3a4"                                        # 泰迪肚皮/鼓皮（WOOD_L 族）
STEEL_L = "#c9cdd1"                                         # 运动轨迹浅灰（STEELC 族）
GREY_D = "#46535f"                                          # 深灰机械（jiaju GREY 族）
GREY_M = "#9aa0a7"                                          # 中灰
SILVER = "#b7bcc2"                                          # 浅银（GREY 族浅，yanse 组）
ORANGE = "#f0923c"                                          # 暖橙（jiaju 沙发族）
SUN_D = "#d99a2b"                                           # 黄深（SUN 族深，同 YEL_D）
STRING = "#8a5a33"                                          # 线绳深棕（WOOD 族深）
GLASS_L = "#eaf5fb"                                         # 积木内衬浅蓝


# ---------- 1 toy 玩具箱盖掀开，玩具满出 ----------
def art_toy():
    g = ground()
    # 掀开的盖（铰链右上）
    g += f'<g transform="rotate(58 448 220)">{R(312, 204, 136, 34, 14, WOOD_D)}{R(312, 204, 136, 10, 5, WOOD_L)}</g>'
    # 满出的玩具堆轮廓
    g += P("M 250 302 Q 268 272 300 278 Q 318 244 354 254 Q 382 228 412 250 "
           "Q 444 238 470 264 Q 498 272 510 302 Z", WOOD_L)
    # 玩具：小球 / 积木×2 / 泰迪头 / 星星魔法棒
    g += C(324, 262, 24, RED_D)
    g += C(320, 258, 22, RED)
    g += C(312, 250, 7, WHITE)
    g += R(368, 238, 44, 44, 6, BLUE)
    g += R(376, 246, 28, 28, 4, GLASS_L)
    g += R(420, 252, 38, 38, 6, GREEN)
    g += C(439, 271, 9, GREEN_L)
    g += C(452, 252, 22, WOOD)
    g += C(440, 236, 9, WOOD)
    g += C(464, 236, 9, WOOD)
    g += C(446, 250, 4, INK)
    g += C(458, 250, 4, INK)
    g += L(500, 244, 520, 214, WOOD_D, 6)
    g += star5(524, 204, 14, SUN)
    # 箱体 + 板条 + 两侧包角
    g += R(240, 300, 280, 140, 14, WOOD)
    g += R(240, 300, 18, 140, 8, WOOD_D)
    g += R(502, 300, 18, 140, 8, WOOD_D)
    g += L(258, 342, 502, 342, WOOD_D, 6)
    g += L(258, 384, 502, 384, WOOD_D, 6)
    return g


# ---------- 2 ball 红白弧条大沙滩球 ----------
def art_ball():
    g = ground()
    # 球体（深沿 + 白底 + 三道红弧条 + 高光）
    g += C(388, 308, 150, RED_D)
    g += C(380, 300, 150, WHITE)
    g += P("M 372 152 Q 356 300 372 448 L 388 448 Q 372 300 388 152 Z", RED)
    g += P("M 330 164 Q 296 300 330 436 L 352 441 Q 324 300 352 159 Z", RED)
    g += P("M 430 164 Q 464 300 430 436 L 408 441 Q 436 300 408 159 Z", RED)
    g += C(330, 240, 20, PINK, 0.75)
    return g


# ---------- 3 balloon 红气球飘线，白云衬 ----------
def art_balloon():
    g = ground()
    # 云两朵
    g += cloud_p(220, 170, 0.85, WHITE)
    g += cloud_p(584, 260, 0.6, WHITE)
    # 气球（深沿 + 红体 + 高光 + 气结）
    g += E(408, 198, 107, 127, RED_D)
    g += E(400, 190, 105, 125, RED)
    g += E(360, 148, 30, 42, PINK, 0.8)
    g += PG([(400, 313), (386, 335), (414, 335)], RED_D)
    # 飘线（垂到地面打卷）
    g += P("M 400 335 Q 356 380 398 410 Q 432 434 396 446", stroke=STRING, w=5)
    return g


# ---------- 4 doll 粉衣花裙娃娃坐姿（kid 组件） ----------
def art_doll():
    g = ground()
    g += kid(380, 430, 1.0, pose="sit", face="smile", shirt=PINK,
             arms="clap", bun=True, skirt=True)
    # 发髻蝴蝶结
    g += PG([(352, 122), (376, 114), (352, 106)], RED)
    g += PG([(408, 122), (384, 114), (408, 106)], RED)
    g += C(380, 114, 8, RED_D)
    # 花裙上的小花点
    g += C(340, 352, 8, SUN)
    g += C(390, 364, 8, SUN)
    g += C(430, 348, 8, SUN)
    g += C(362, 382, 7, SUN)
    g += C(416, 384, 7, SUN)
    return g


# ---------- 5 teddy bear 棕泰迪圆耳坐姿 ----------
def art_teddy_bear():
    g = ground()
    # 圆耳（深耳 + 浅内耳）
    g += C(326, 162, 27, WOOD_D)
    g += C(326, 162, 14, WOOD_TAN)
    g += C(434, 162, 27, WOOD_D)
    g += C(434, 162, 14, WOOD_TAN)
    # 头 + 眼 + 口鼻
    g += C(380, 222, 72, WOOD_D)
    g += C(380, 220, 70, WOOD)
    g += C(354, 204, 8, INK)
    g += C(406, 204, 8, INK)
    g += C(351, 201, 3, WHITE)
    g += C(403, 201, 3, WHITE)
    g += E(380, 244, 35, 26, WOOD_TAN)
    g += C(380, 236, 10, INK)
    g += P("M 380 246 L 380 254", stroke=INK, w=4)
    g += P("M 368 258 Q 380 266 392 258", stroke=INK, w=4)
    # 身体 + 肚皮 + 手臂
    g += E(380, 342, 90, 92, WOOD_D)
    g += E(380, 338, 88, 90, WOOD)
    g += E(380, 352, 54, 58, WOOD_TAN)
    g += f'<g transform="rotate(24 300 322)">{E(300, 322, 25, 44, WOOD)}</g>'
    g += f'<g transform="rotate(-24 460 322)">{E(460, 322, 25, 44, WOOD)}</g>'
    # 坐姿双腿 + 脚掌
    g += E(314, 424, 34, 26, WOOD)
    g += E(446, 424, 34, 26, WOOD)
    g += E(310, 424, 14, 18, WOOD_TAN)
    g += E(450, 424, 14, 18, WOOD_TAN)
    return g


# ---------- 6 kite 燕子风筝双翼叉尾，牵线地上线轴 ----------
def art_kite():
    g = ground()
    # 云 + 太阳
    g += cloud_p(212, 140, 0.8, WHITE)
    g += cloud_p(608, 200, 0.55, WHITE)
    g += C(646, 108, 30, SUN)
    g += C(636, 100, 9, SUN_L)
    # 双翼（燕子翅）
    g += P("M 420 196 Q 338 152 288 184 Q 330 206 402 214 Z", TEAL)
    g += P("M 420 196 Q 502 152 552 184 Q 510 206 438 214 Z", TEAL)
    # 身体 + 头 + 喙 + 眼
    g += E(420, 202, 26, 40, TEAL_D)
    g += C(420, 160, 17, TEAL_D)
    g += PG([(420, 144), (442, 154), (420, 161)], SUN)
    g += C(414, 154, 4, WHITE)
    g += C(426, 154, 4, WHITE)
    # 翅上白斑
    g += E(360, 186, 16, 9, TEAL_L, 0.9)
    g += E(484, 186, 16, 9, TEAL_L, 0.9)
    # 叉尾
    g += P("M 414 240 Q 398 284 378 302", stroke=TEAL_D, w=9)
    g += P("M 426 240 Q 444 286 464 300", stroke=TEAL_D, w=9)
    # 牵线 + 线轴
    g += P("M 444 234 Q 420 322 468 378 Q 498 412 474 438", stroke=STRING, w=4)
    g += R(452, 430, 44, 15, 7, WOOD)
    g += C(474, 434, 6, WOOD_D)
    return g


# ---------- 7 blocks 四色积木叠塔 + 斜靠一块 ----------
def art_blocks():
    g = ground()
    # 塔：下宽上窄四层 + 顶球
    g += R(314, 380, 132, 56, 10, RED)
    g += C(380, 408, 14, WHITE)
    g += R(328, 324, 104, 56, 10, BLUE)
    g += PG([(362, 366), (380, 338), (398, 366)], WHITE)
    g += R(342, 268, 76, 56, 10, YEL)
    g += R(370, 286, 20, 20, 4, WHITE)
    g += R(356, 212, 48, 56, 10, GREEN)
    g += C(380, 240, 10, WHITE)
    g += C(384, 194, 22, RED_D)
    g += C(380, 190, 20, RED)
    g += C(374, 184, 6, WHITE)
    # 斜靠的一块
    g += f'<g transform="rotate(10 540 436)">{R(500, 380, 80, 56, 10, TEAL)}{C(540, 408, 12, TEAL_L)}</g>'
    return g


# ---------- 8 robot 方头机器人天线 ----------
def art_robot():
    g = ground()
    # 天线 + 顶灯
    g += L(380, 178, 380, 142, GREY_D, 8)
    g += C(380, 132, 13, RED)
    g += C(376, 128, 4, PINK)
    # 方头 + 深色脸屏 + 方眼 + 嘴栅
    g += R(306, 214, 16, 34, 6, BLUE)
    g += R(438, 214, 16, 34, 6, BLUE)
    g += R(320, 178, 120, 102, 16, SILVER)
    g += R(336, 194, 88, 70, 10, GREY_D)
    g += R(352, 212, 22, 22, 4, SUN)
    g += R(390, 212, 22, 22, 4, SUN)
    g += C(363, 218, 5, WHITE)
    g += C(401, 218, 5, WHITE)
    g += L(358, 252, 366, 252, "#7d8791", 5)
    g += L(372, 252, 380, 252, "#7d8791", 5)
    g += L(386, 252, 394, 252, "#7d8791", 5)
    # 脖颈 + 身体 + 面板按钮
    g += R(368, 276, 24, 16, 6, GREY_D)
    g += R(330, 292, 100, 106, 14, SILVER)
    g += R(346, 306, 68, 48, 8, GREY_D)
    g += L(354, 318, 406, 318, "#7d8791", 5)
    g += L(354, 330, 406, 330, "#7d8791", 5)
    g += C(356, 374, 9, RED)
    g += C(380, 374, 9, GREEN)
    g += C(404, 374, 9, SUN)
    # 手臂（线段臂）+ 手
    g += L(330, 306, 296, 344, GREY_D, 16)
    g += C(292, 348, 14, BLUE)
    g += L(430, 306, 464, 344, GREY_D, 16)
    g += C(468, 348, 14, BLUE)
    # 履带底座 + 轮
    g += R(320, 398, 120, 42, 18, GREY_D)
    g += C(340, 424, 12, "#2f363d")
    g += C(380, 424, 12, "#2f363d")
    g += C(420, 424, 12, "#2f363d")
    g += C(340, 424, 5, SILVER)
    g += C(380, 424, 5, SILVER)
    g += C(420, 424, 5, SILVER)
    return g


# ---------- 9 puzzle 青底拼图缺一块 + 红拼块 ----------
def art_puzzle():
    g = ground()
    board = wrap(
        R(230, 180, 300, 220, 14, "#7cc8bb"),
        R(244, 194, 272, 192, 8, TEAL_L),
        # 拼缝
        L(334, 194, 334, 386, WHITE, 6),
        L(426, 194, 426, 386, WHITE, 6),
        L(244, 290, 516, 290, WHITE, 6),
        # 凸扣圆点
        C(334, 242, 11, TEAL_L),
        C(380, 290, 11, TEAL_L),
        C(426, 338, 11, TEAL_L),
        # 各块装饰：星 / 圆 / 三角
        star5(288, 240, 15, SUN),
        C(378, 238, 13, WHITE),
        PG([(478, 256), (500, 222), (522, 256)], RED),
        C(288, 340, 13, PINK),
        PG([(362, 366), (384, 336), (406, 366)], GREEN_L),
    )
    g += f'<g transform="rotate(-5 380 290)">{board}</g>'
    # 缺块凹槽（右下角深色空位）
    g += f'<g transform="rotate(-5 380 290)">{R(428, 292, 88, 94, 10, "#46535f")}{C(472, 339, 11, "#2f363d")}</g>'
    # 旁边待放的红色拼块（带凸扣）
    piece = wrap(R(452, 352, 88, 78, 10, RED_D), R(456, 356, 80, 70, 8, RED),
                 C(496, 350, 12, RED), star5(496, 396, 15, SUN),
                 E(462, 364, 16, 24, WHITE, 0.35))
    g += f'<g transform="rotate(9 496 396)">{piece}</g>'
    return g


# ---------- 10 yoyo 黄盘红心悠悠球，手握线一上一下 ----------
def art_yoyo():
    g = ground()
    # 上方小手（组件，掌心向下握线）
    g += hand(468, 180, rot=180, s=0.85)
    # 线（手 → 球）
    g += P("M 468 268 Q 462 320 466 352", stroke=STRING, w=5)
    g += L(460, 374, 460, 408, STRING, 5)
    # 悠悠球（黄盘 + 红心）
    g += C(466, 414, 58, SUN_D)
    g += C(460, 408, 56, SUN)
    g += E(434, 384, 18, 24, SUN_L, 0.85)
    g += C(460, 408, 21, RED_D)
    g += C(460, 408, 12, RED)
    g += C(456, 403, 4, WHITE, 0.85)
    # 上下运动轨迹弧
    g += P("M 366 330 Q 346 402 366 470", stroke=STEEL_L, w=7)
    g += P("M 554 330 Q 574 402 554 470", stroke=STEEL_L, w=7)
    return g


# ---------- 11 slide 红滑梯平台木梯，kid 坐姿下滑 ----------
def art_slide():
    g = ground()
    # 滑道（粗线滑面 + 双侧轨）
    g += L(308, 254, 560, 434, RED, 40)
    g += L(300, 244, 552, 424, RED_D, 12)
    g += L(320, 268, 570, 448, RED_D, 12)
    # 平台 + 护栏
    g += R(250, 226, 112, 26, 10, TEAL)
    g += L(262, 226, 262, 194, TEAL_D, 9)
    g += L(348, 226, 348, 194, TEAL_D, 9)
    g += L(258, 196, 352, 196, TEAL_D, 9)
    # 平台支柱 + 木梯
    g += R(312, 252, 18, 184, 8, WOOD_D)
    g += L(236, 244, 236, 436, WOOD_D, 13)
    g += L(274, 252, 274, 436, WOOD_D, 13)
    for y in (292, 332, 372, 412):
        g += L(230, y, 280, y, WOOD_L, 9)
    # 下滑的小朋友（坐姿后仰，脚顺滑道）
    g += f'<g transform="rotate(-36 440 326)">{kid(440, 388, 0.8, pose="sit", face="open", arms="up", shirt=SUN)}</g>'
    return g


def arts():
    return {
        "toy": art_toy(), "ball": art_ball(), "balloon": art_balloon(),
        "doll": art_doll(), "teddy bear": art_teddy_bear(), "kite": art_kite(),
        "blocks": art_blocks(), "robot": art_robot(), "puzzle": art_puzzle(),
        "yoyo": art_yoyo(), "slide": art_slide(),
    }
