#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 衣物·穿戴（yifu）第 2 段插画（10 卡：shoe~button）。

每卡造型要点：shoe 红运动鞋一双外八并排（交叉鞋带+白鞋头白底边）/
boot 黄小雨靴高筒（靴口深色翻边+深底防滑纹+雨滴）/ hat 宽檐草帽俯视
（同心编织圈+深棕帽带金扣）/ cap 红蓝棒球帽正面（蓝冠红舌朝前+顶钮+拼缝）/
scarf 青绿长围巾盘成一圈（线圈弧线+两端垂坠流苏）/ glove 红手套一双
五指张开（罗纹腕口）/ belt 棕皮带盘起（金色方扣环+前带一排孔眼）/
glasses 深棕圆框眼镜折起（浅蓝镜片白色反光斜条）/ pajamas 浅蓝星星睡衣
上下套装平铺（上衣门襟钉扣、长裤腰头抽绳）/ button 金色大纽扣四孔白线
交叉穿缝，旁散两粒小扣。
主体居中放大，成双的并排、折起平铺展示；主色相邻错开（与第 10 张彩条袜衔接）。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

GROUP_CARDS = [
    {"w": "shoe", "cn": "鞋"},
    {"w": "boot", "cn": "靴子"},
    {"w": "hat", "cn": "帽子"},
    {"w": "cap", "cn": "棒球帽"},
    {"w": "scarf", "cn": "围巾"},
    {"w": "glove", "cn": "手套"},
    {"w": "belt", "cn": "腰带"},
    {"w": "glasses", "cn": "眼镜"},
    {"w": "pajamas", "cn": "睡衣"},
    {"w": "button", "cn": "纽扣"},
]


# ---------- 本组同族补充色 ----------
RED_L = "#f49a7c"                                              # 红族浅（高光）
RED_DD = "#a03620"                                             # 红族深（领口内/罗纹）
YEL_L2 = "#f8d582"                                             # 黄族浅（高光/翻边亮）
YEL_DD = "#b57f1e"                                             # 黄族深（靴底）
YEL_DDD = "#9c6a12"                                            # 黄族更深（防滑纹）
STRAW, STRAW_D, STRAW_L = "#e6bd6a", "#c99a3e", "#f6e09a"      # 草帽麦秆（YEL/WOOD 族）
BAND_BR = "#7a5230"                                            # 帽带深棕（WOOD 族深）
SOLE_SH = "#ddd3ba"                                            # 白族暖深（鞋底阴影）
SOLE_SH2 = "#d3c9ae"                                           # 白族更深（鞋底底纹）
FRAME = HAIR                                                   # 镜框深棕 #5a3d2b
FRAME_D = "#412c1e"                                            # 镜框更深
LENS = "#bfe4f2"                                               # 镜片浅蓝（WBLUE 族浅）
PBLUE = "#a9d6ee"                                              # 睡衣浅蓝（WBLUE 族浅）
PBLUE_D = "#7fb8dd"                                            # 睡衣蓝深（腰头/暗边）
GOLD_D = "#c98a1e"                                             # 金族深（纽扣边/扣环暗部）
GOLD_DD = "#a8701f"                                            # 金族更深（纽孔）


def shine(cx, cy, rx, ry, col, op, rot=0):
    """同族浅色斜高光椭圆。"""
    if rot:
        return f'<g transform="rotate({rot} {cx} {cy})">' + E(cx, cy, rx, ry, col, op) + "</g>"
    return E(cx, cy, rx, ry, col, op)


# ---------- 11 shoe 红运动鞋一双，鞋带交叉白底边 ----------
UPPER = ("M 140 400 L 140 356 Q 140 318 174 310 Q 224 298 258 276 L 296 238 "
         "Q 306 228 318 232 L 326 238 Q 332 252 350 254 L 362 254 "
         "Q 382 256 386 280 Q 392 326 392 400 Z")


def _shoe():
    """一只朝左的红运动鞋（鞋头左、鞋跟右），鞋底落地 y≈452。"""
    g = R(136, 402, 272, 52, 24, SOLE_SH)                    # 鞋底暗侧
    g += R(130, 396, 272, 56, 26, WHITE)                     # 白鞋底
    g += R(132, 434, 268, 14, 7, SOLE_SH2)                   # 底部防滑纹带
    g += f'<g transform="translate(6,8)">{P(UPPER, RED_D)}</g>'
    g += P(UPPER, RED)                                       # 鞋帮
    g += P("M 140 400 L 140 356 Q 140 318 174 310 Q 208 302 238 290 "
           "Q 228 342 226 400 Z", WHITE)                     # 白鞋头
    g += '<g transform="rotate(-6 350 252)">' + E(350, 252, 22, 8, RED_DD) + "</g>"  # 领口内
    g += R(372, 230, 16, 34, 7, RED_DD)                      # 后跟提环
    g += R(134, 390, 262, 12, 6, WHITE)                      # 白底边
    g += R(300, 230, 18, 14, 5, WHITE)                       # 舌标
    g += L(257, 261, 279, 283, WHITE, 9) + L(279, 261, 257, 283, WHITE, 9)  # 交叉鞋带
    g += L(275, 239, 297, 261, WHITE, 9) + L(297, 239, 275, 261, WHITE, 9)
    g += shine(324, 320, 26, 42, RED_L, 0.45, -18)
    return g


def art_shoe():
    g = ground()
    g += f'<g transform="translate(-12,0)">{_shoe()}</g>'     # 并排：前一只
    g += f'<g transform="translate(266,0)">{_shoe()}</g>'     # 并排：后一只
    return g


# ---------- 12 boot 黄小雨靴，翻边+防滑底 ----------
BOOT_D = ("M 302 148 L 302 330 Q 258 334 216 366 Q 178 394 176 428 "
          "Q 176 450 200 450 L 430 450 Q 458 450 458 424 L 458 148 "
          "Q 458 140 448 140 L 312 140 Q 302 140 302 148 Z")


def art_boot():
    g = ground()
    g += f'<g transform="translate(7,8)">{P(BOOT_D, YEL_D)}</g>'
    g += P(BOOT_D, YEL)                                      # 靴身
    g += R(302, 174, 156, 14, 7, YEL_D, 0.45)                # 翻边投影
    g += R(284, 128, 192, 46, 22, YEL_D)                     # 靴口翻边
    g += R(284, 128, 192, 16, 8, YEL_L2, 0.8)
    g += R(168, 436, 298, 26, 13, YEL_DD)                    # 靴底
    for x in (184, 234, 284, 334, 384):
        g += R(x, 448, 26, 9, 4, YEL_DDD)                    # 防滑纹
    g += R(320, 190, 24, 150, 12, YEL_L2, 0.7)               # 筒身高光
    g += '<g transform="rotate(-24 214 396)">' + E(214, 396, 22, 11, YEL_L2, 0.7) + "</g>"
    g += drop(168, 176, 15) + drop(556, 216, 13)             # 雨滴
    return g


# ---------- 13 hat 宽檐草帽，深色帽带 ----------
CROWN = ("M 282 316 Q 284 210 306 188 Q 336 164 380 164 Q 424 164 454 188 "
         "Q 476 210 478 316 Q 380 344 282 316 Z")


def art_hat():
    g = ground()
    g += E(384, 340, 216, 92, STRAW_D)                       # 帽檐暗侧
    g += E(380, 334, 214, 90, STRAW)                         # 宽帽檐
    g += P("M 246 334 A 134 52 0 1 1 514 334 A 134 52 0 1 1 246 334",
           stroke=STRAW_D, w=4)                              # 檐面编织圈
    g += f'<g transform="translate(6,8)">{P(CROWN, STRAW_D)}</g>'
    g += P(CROWN, STRAW)                                     # 帽顶
    g += P("M 280 282 Q 380 308 480 282 L 480 314 Q 380 342 280 314 Z", BAND_BR)  # 深色帽带
    g += R(366, 296, 30, 24, 5, WOOD_L)                      # 带扣
    g += R(372, 302, 18, 12, 3, BAND_BR)
    g += shine(336, 206, 30, 16, STRAW_L, 0.8, -18)
    g += shine(300, 296, 56, 18, STRAW_L, 0.45, -10)
    return g


# ---------- 14 cap 红蓝棒球帽，帽舌朝前+顶钮 ----------
DOME = "M 226 372 Q 380 402 534 372 Q 534 218 380 200 Q 226 218 226 372 Z"


def art_cap():
    g = ground()
    g += f'<g transform="translate(6,8)">{P(DOME, BLUE_D)}</g>'
    g += P(DOME, BLUE)                                       # 蓝帽冠
    g += P("M 314 222 Q 302 292 306 380", stroke=BLUE_D, w=5)   # 拼缝线
    g += P("M 446 222 Q 458 292 454 380", stroke=BLUE_D, w=5)
    g += C(330, 280, 6, BLUE_D) + C(430, 280, 6, BLUE_D)     # 气眼
    g += E(385, 384, 172, 50, RED_D)                         # 帽舌暗侧
    g += E(380, 378, 170, 48, RED)                           # 红帽舌朝前
    g += shine(330, 392, 40, 10, RED_L, 0.55, -10)
    g += C(383, 199, 17, RED_D)
    g += C(380, 196, 16, RED) + C(374, 190, 6, RED_L, 0.9)   # 顶钮
    return g


# ---------- 15 scarf 青绿长围巾盘圈流苏 ----------
def art_scarf():
    g = ground()
    g += E(386, 342, 208, 118, TEAL_D)                       # 圈身暗侧
    g += E(380, 336, 206, 116, TEAL)                         # 盘起的围巾圈
    g += E(380, 336, 118, 58, TEAL_D)                        # 圈心暗缘
    g += E(380, 336, 106, 48, PAGE)                          # 圈心
    g += P("M 192 322 Q 380 140 568 322", stroke=TEAL_D, w=6)   # 线圈分弧
    g += P("M 216 392 Q 380 456 544 392", stroke=TEAL_D, w=6)
    for x1, y1, x2, y2 in ((322, 240, 338, 262), (372, 232, 386, 254), (424, 238, 436, 260),
                           (300, 396, 314, 418), (360, 402, 372, 422), (428, 394, 440, 414)):
        g += L(x1, y1, x2, y2, TEAL_D, 5)                    # 针织斜纹
    # 右端垂坠+流苏
    drape_r = "M 548 344 Q 600 372 594 424 Q 592 442 572 444 L 548 438 Q 556 394 534 366 Z"
    g += f'<g transform="translate(5,6)">{P(drape_r, TEAL_D)}</g>'
    g += P(drape_r, TEAL)
    g += L(556, 442, 553, 464, TEAL_D, 7) + L(574, 444, 572, 466, TEAL_D, 7) + L(590, 440, 591, 460, TEAL_D, 7)
    # 左端垂坠+流苏
    drape_l = "M 212 340 Q 160 366 166 418 Q 168 436 188 438 L 212 432 Q 204 392 226 364 Z"
    g += f'<g transform="translate(5,6)">{P(drape_l, TEAL_D)}</g>'
    g += P(drape_l, TEAL)
    g += L(190, 438, 187, 460, TEAL_D, 7) + L(174, 436, 171, 456, TEAL_D, 7)
    return g


# ---------- 16 glove 红手套一双五指张开，罗纹腕口 ----------
def _glove():
    """掌心朝前、五指张开的一只红手套，原点在掌心，腕口底 y≈112。"""
    g = R(-54, -152, 26, 92, 13, RED)                        # 食指
    g += R(-22, -164, 26, 104, 13, RED)                      # 中指
    g += R(10, -158, 26, 98, 13, RED)                        # 无名指
    g += R(42, -142, 24, 82, 12, RED)                        # 小指
    g += '<g transform="rotate(-32 -58 -30)">' + R(-86, -98, 26, 86, 13, RED) + "</g>"  # 拇指
    g += R(-58, -72, 116, 132, 34, RED)                      # 手掌
    g += shine(-22, -16, 24, 44, RED_L, 0.5, 12)
    g += R(-62, 54, 124, 58, 18, RED_D)                      # 罗纹腕口
    for x in (-46, -24, -2, 20, 42):
        g += L(x, 60, x, 106, RED_DD, 6)                     # 罗纹竖条
    return g


def art_glove():
    g = ground()
    g += '<g transform="translate(292,314) rotate(-9)">' + _glove() + "</g>"
    g += '<g transform="translate(468,314) rotate(9) scale(-1,1)">' + _glove() + "</g>"
    return g


# ---------- 17 belt 棕皮带盘起，金属扣环 ----------
def art_belt():
    g = ground()
    g += E(382, 334, 176, 130, WOOD_D)                       # 盘圈暗侧
    g += E(376, 328, 174, 128, WOOD)                         # 皮带盘
    g += E(376, 328, 96, 64, WOOD_D)                         # 圈心暗缘
    g += E(376, 328, 84, 54, PAGE)                           # 圈心
    g += P("M 208 318 Q 376 148 544 318", stroke=WOOD_D, w=6)   # 盘绕分弧
    g += P("M 234 386 Q 376 454 518 386", stroke=WOOD_D, w=6)
    for hx, hy in ((310, 416), (348, 426), (388, 430), (426, 424)):
        g += C(hx, hy, 5, "#8a5a33")                         # 带孔一排
    # 从盘圈里抽出的带头（垂在右前）
    g += R(452, 246, 46, 200, 21, WOOD_D)
    g += R(446, 240, 46, 200, 21, WOOD)
    g += C(469, 344, 6, "#8a5a33") + C(469, 388, 6, "#8a5a33")   # 带尾孔
    # 穿过扣环的带头（绕过盘圈顶部）
    strap = "M 276 224 Q 376 192 476 224 L 476 276 Q 376 246 276 276 Z"
    g += f'<g transform="translate(0,6)">{P(strap, WOOD_D)}</g>'
    g += P(strap, WOOD_L)
    g += R(336, 194, 80, 64, 12, SUN)                        # 金色方扣环
    g += R(352, 210, 48, 32, 6, WOOD_L)
    g += L(376, 210, 376, 242, GOLD_D, 6)                    # 扣针
    g += shine(296, 282, 28, 44, WOOD_L, 0.5, -18)
    return g


# ---------- 18 glasses 深棕圆框眼镜，镜片反光斜条 ----------
def art_glasses():
    g = ground()
    g += P("M 150 322 Q 104 322 108 366 Q 112 394 148 394", stroke=FRAME, w=13)   # 折起的左镜腿
    g += P("M 610 322 Q 656 322 652 366 Q 648 394 612 394", stroke=FRAME, w=13)   # 折起的右镜腿
    g += C(262, 327, 108, FRAME_D) + C(506, 327, 108, FRAME_D)  # 框暗侧
    g += C(258, 322, 108, FRAME) + C(502, 322, 108, FRAME)      # 深棕圆框
    g += C(258, 322, 98, LENS) + C(502, 322, 98, LENS)          # 浅蓝镜片
    g += P("M 214 378 L 284 250", stroke=WHITE, w=13, opacity=0.55)   # 反光斜条
    g += P("M 242 388 L 300 284", stroke=WHITE, w=8, opacity=0.45)
    g += P("M 458 378 L 528 250", stroke=WHITE, w=13, opacity=0.55)
    g += P("M 486 388 L 544 284", stroke=WHITE, w=8, opacity=0.45)
    g += R(348, 306, 64, 18, 9, FRAME)                          # 鼻梁
    g += C(366, 342, 7, FRAME) + C(394, 342, 7, FRAME)          # 鼻托
    return g


# ---------- 19 pajamas 浅蓝星星睡衣套装平铺 ----------
def art_pajamas():
    g = ground()
    # 上衣（左上，平铺）
    g += '<g transform="rotate(-24 180 190)">' + R(112, 172, 70, 118, 28, PBLUE) + "</g>"
    g += '<g transform="rotate(24 370 190)">' + R(368, 172, 70, 118, 28, PBLUE) + "</g>"
    g += R(174, 166, 210, 192, 30, PBLUE_D)                  # 衣身暗侧
    g += R(168, 160, 210, 192, 30, PBLUE)
    g += E(273, 160, 34, 12, BLUE_D)                         # 领口
    g += R(263, 176, 20, 168, 8, "#cde8f6")                  # 门襟
    g += C(273, 210, 6, WHITE) + C(273, 254, 6, WHITE) + C(273, 298, 6, WHITE)  # 钉扣
    for sx, sy, sr in ((210, 200, 14), (332, 226, 14), (196, 258, 11), (222, 300, 12), (328, 320, 13)):
        g += star5(sx, sy, sr, SUN)                          # 星星图案
    # 长裤（右下，平铺）
    g += R(430, 240, 200, 42, 14, PBLUE_D)                   # 腰头
    g += R(436, 276, 92, 182, 20, PBLUE_D) + R(544, 276, 92, 182, 20, PBLUE_D)  # 裤腿暗侧
    g += R(430, 270, 92, 182, 20, PBLUE) + R(538, 270, 92, 182, 20, PBLUE)
    g += R(430, 434, 92, 18, 9, PBLUE_D) + R(538, 434, 92, 18, 9, PBLUE_D)      # 裤脚罗纹
    g += L(512, 262, 505, 290, WHITE, 6) + L(524, 262, 531, 288, WHITE, 6)      # 抽绳
    for sx, sy, sr in ((472, 330, 12), (584, 356, 12), (492, 404, 11), (566, 424, 12)):
        g += star5(sx, sy, sr, SUN)
    return g


# ---------- 20 button 金色大纽扣四孔穿线，旁散两粒小扣 ----------
def art_button():
    g = ground()
    g += C(308, 330, 128, GOLD_D)                            # 大扣暗侧
    g += C(300, 324, 126, SUN)
    g += C(300, 324, 96, SUN_L, 0.5)                         # 扣面微亮
    for hx, hy in ((272, 296), (328, 296), (272, 352), (328, 352)):
        g += C(hx, hy, 13, GOLD_DD)                          # 四孔
    g += L(272, 296, 328, 352, WHITE, 9) + L(328, 296, 272, 352, WHITE, 9)  # 白线交叉穿缝
    g += shine(258, 262, 32, 18, SUN_L, 0.9, -32)
    g += shine(396, 386, 18, 10, SUN_L, 0.5, 28)
    # 小扣一（右下）
    g += C(528, 392, 46, GOLD_D) + C(522, 386, 44, SUN)
    for hx, hy in ((508, 372), (536, 372), (508, 400), (536, 400)):
        g += C(hx, hy, 7, GOLD_DD)
    g += L(508, 372, 536, 400, WHITE, 5) + L(536, 372, 508, 400, WHITE, 5)
    # 小扣二（右上）
    g += C(596, 258, 32, GOLD_D) + C(590, 252, 30, SUN)
    for hx, hy in ((578, 240), (602, 240), (578, 264), (602, 264)):
        g += C(hx, hy, 5, GOLD_DD)
    g += L(578, 240, 602, 264, WHITE, 4) + L(602, 240, 578, 264, WHITE, 4)
    return g


def arts():
    return {
        "shoe": art_shoe(),
        "boot": art_boot(),
        "hat": art_hat(),
        "cap": art_cap(),
        "scarf": art_scarf(),
        "glove": art_glove(),
        "belt": art_belt(),
        "glasses": art_glasses(),
        "pajamas": art_pajamas(),
        "button": art_button(),
    }
