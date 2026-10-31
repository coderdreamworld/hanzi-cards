#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""食物组插画与文案（本组无种子字）。

9 字：米 面 饭 菜 蛋 茶 糖 饼 梨
易混卡刻意区分：
- 米/饭：米=蓝碗盛满一粒粒米（碗口可见米粒排布）+桌布散粒；饭=陶碗堆尖光饭团+三道热气。
- 面=红碗波浪面+筷子+垂挂面；茶=青瓷把手杯+琥珀茶汤+热气。
- 全组一律放桌布或小碟上，有"饭桌感"。
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from 识字卡片_素材库 import (BLUE, BLUE_D, C, E, GREEN, GREEN_L, L, P, PG, R, RED, RED_D,
                          TEAL, TEAL_D, TEAL_L, WHITE, WOOD, WOOD_D, ground, wrap)

# 本组同族补充色
CLOTH, CLOTH_D = "#f7e3d3", "#f0d2bd"     # 桌布（暖粉同族）
PLATE_SH = "#d8d2c2"                      # 碟影（中性暖）
PLATE_IN = "#efe9da"                      # 碟心
CREAM = "#f5e3b8"                         # 面条奶油色（YEL 同族浅）
TEA, TEA_HL = "#c98a3a", "#e2ab62"        # 茶汤琥珀（YEL_D 同族）
BOWL_TD, BOWL_TD2 = "#d9734f", "#c05f3e"  # 陶碗（库 bowl 同族）
EGG_W, EGG_D = "#f6f1e3", "#ddd6c2"       # 蛋壳暖白
YOLK, YOLK_L = "#f2b53c", "#f9d06a"       # 蛋黄
GRAIN = "#e8e2d4"                         # 米粒暗部
COOKIE, COOKIE_D = "#e8b04a", "#cf9430"   # 饼干金
CHIP = "#8a5a33"                          # 糖芝麻棕
PEAR, PEAR_D = "#f0c94f", "#d9a832"       # 梨黄
VEG_W, VEG_W_D = "#eef3e2", "#d9e2c8"     # 菜帮白
VEG_V = "#dcebc8"                         # 叶脉浅
STEAM_C = "#e3d5bd"                       # 热气暖灰
SHADOW = "#a5d0bd"                        # 地面同族深一号（落地投影，与动作组同族）
BOWL_RED_D = "#a8441f"                    # 红碗口内壁


GROUP_CARDS = [
    {"char": "米", "pinyin": "mǐ", "tone": "第三声",
     "sentence": "碗里装着白白的米。",
     "say": "一颗颗小白粒就是米。",
     "chat": "“米饭是用什么煮出来的？”",
     "life": "晚饭找找碗里的米粒。"},
    {"char": "面", "pinyin": "miàn", "tone": "第四声",
     "sentence": "长长的面条真好吃。",
     "say": "碗里弯弯的是面条。",
     "chat": "“吃面用什么夹起来呀？”",
     "life": "闻一闻面条香不香。"},
    {"char": "饭", "pinyin": "fàn", "tone": "第四声",
     "sentence": "白米饭香喷喷。",
     "say": "堆得尖尖、冒热气的是米饭。",
     "chat": "“碗上的热气从哪来？”",
     "life": "吃饭前说：我要开动啦。"},
    {"char": "菜", "pinyin": "cài", "tone": "第四声",
     "sentence": "多吃青菜长得高。",
     "say": "绿叶子白帮子，是颗青菜。",
     "chat": "“今天餐桌上有几种菜？”",
     "life": "夹一口青菜尝一尝。"},
    {"char": "蛋", "pinyin": "dàn", "tone": "第四声",
     "sentence": "圆圆的鸡蛋有营养。",
     "say": "一个整蛋，一个磕开见蛋黄。",
     "chat": "“蛋能做哪些好吃的？”",
     "life": "早餐自己剥一个煮鸡蛋。"},
    {"char": "茶", "pinyin": "chá", "tone": "第二声",
     "sentence": "爷爷爱喝热茶。",
     "say": "杯里黄黄的是茶水。",
     "chat": "“热茶闻起来什么味道？”",
     "life": "给长辈端一杯温温的水。"},
    {"char": "糖", "pinyin": "táng", "tone": "第二声",
     "sentence": "糖果甜甜的。",
     "say": "扭着糖纸的就是糖果。",
     "chat": "“吃完糖要记得做什么？”",
     "life": "吃糖后漱漱口再喝水。"},
    {"char": "饼", "pinyin": "bǐng", "tone": "第三声",
     "sentence": "圆圆的饼干香又脆。",
     "say": "金色圆饼上点缀着小芝麻。",
     "chat": "“饼干上的小点点是什么？”",
     "life": "咬口饼干，看看月牙印。"},
    {"char": "梨", "pinyin": "lí", "tone": "第二声",
     "sentence": "梨子水分多又甜。",
     "say": "上小下大黄黄的是梨。",
     "chat": "“梨和苹果哪里不一样？”",
     "life": "请大人帮忙切块吃梨。"},
]


# ---------- 本地组件 ----------
def plate(cx=380, cy=410, rx=180, ry=34):
    """小碟：碟影 + 白碟 + 碟心。"""
    return (E(cx, cy + 8, rx, ry, PLATE_SH) + E(cx, cy, rx, ry, WHITE)
            + E(cx, cy, rx * 0.68, ry * 0.64, PLATE_IN))


def cloth(cx=380, top=356, w=580, h=100):
    """桌布：圆角暖粉布 + 底边深一号 + 两道小白条纹。"""
    return (R(cx - w / 2, top, w, h, 26, CLOTH) + R(cx - w / 2, top + h - 24, w, 24, 12, CLOTH_D)
            + R(cx - w / 2 + 36, top + 18, 26, 8, 4, WHITE, 0.7)
            + R(cx + w / 2 - 62, top + 18, 26, 8, 4, WHITE, 0.7))


def steam_wisp(x, y, h, lean=18, w=11):
    """一道 S 形热气。"""
    return P(f"M {x} {y} Q {x - lean} {y - h * 0.32} {x} {y - h * 0.58} "
             f"Q {x + lean} {y - h * 0.82} {x - 2} {y - h}", stroke=STEAM_C, w=w, opacity=0.9)


def bowl_body(cx, rim_y, r, depth, main, dark, foot=True):
    """侧视碗身：rim_y=碗口沿 y，depth=碗深，可带圈足。"""
    g = P(f"M {cx - r} {rim_y} Q {cx - r + 2} {rim_y + depth * 0.62} {cx - r * 0.42} {rim_y + depth * 0.88} "
          f"Q {cx} {rim_y + depth} {cx + r * 0.42} {rim_y + depth * 0.88} "
          f"Q {cx + r - 2} {rim_y + depth * 0.62} {cx + r} {rim_y} Z", main)
    if foot:
        g += R(cx - r * 0.26, rim_y + depth - 4, r * 0.52, 16, 8, dark)
    return g


def grain(x, y, rot):
    """一粒米：小白椭圆 + 暖灰投影。"""
    return (f'<g transform="rotate({rot} {x} {y})">'
            + E(x + 1.5, y + 1.5, 12, 5.5, GRAIN) + E(x, y, 12, 5.5, WHITE) + "</g>")


def candy(cx, cy, s, main, dark, stripe_col, rot):
    """扭糖纸的糖果：糖体椭圆 + 斜纹 + 两端扇形糖纸。"""
    g = ""
    for sgn in (-1, 1):
        g += PG([(sgn * 74 * s, -6 * s), (sgn * 126 * s, -36 * s),
                 (sgn * 114 * s, 0), (sgn * 126 * s, 36 * s), (sgn * 74 * s, 6 * s)], main)
        g += L(sgn * 114 * s, 0, sgn * 96 * s, 0, dark, 4 * s)
    g += E(0, 0, 82 * s, 58 * s, main)
    for sx, wd in ((-34, 13), (4, 15), (40, 11)):
        g += P(f"M {sx * s} {-50 * s} Q {sx * s - 8 * s} 0 {sx * s} {50 * s}",
               stroke=stripe_col, w=wd * s)
    g += E(-26 * s, -20 * s, 18 * s, 10 * s, WHITE, 0.7)
    return f'<g transform="translate({cx},{cy}) rotate({rot})">{g}</g>'


# ---------- 各卡插画 ----------
def art_mi():
    """米：满满一大碗米粒——颗颗分明（碗占满画面，无多余元素）。"""
    g = ground(380, 442, 235, 24)
    g += E(380, 296, 190, 30, "#3a7aa8")                       # 碗口内壁（深蓝）
    for row, yy in enumerate((276, 290, 304)):                  # 米粒铺满碗口
        for i in range(9):
            gx = 216 + i * 41 + (row % 2) * 15
            g += grain(gx, yy, (row * 33 + i * 17) % 180 - 90)
    g += wrap(grain(306, 268, -14), grain(436, 266, 12))
    g += P("M 186 296 A 194 30 0 0 0 574 296 Q 568 392 380 398 Q 194 392 186 296 Z", "#5fa8d8")
    g += R(352, 396, 56, 15, 8, "#4a97c8")
    g += E(298, 340, 26, 11, WHITE, 0.5)
    g += wrap(grain(240, 428, -18), grain(532, 424, 20))
    return g


def art_mian():
    """面：筷子挑起长长的面条，垂进红碗里。"""
    g = ground(380, 442, 235, 24)
    g += E(380, 296, 190, 30, "#a8441f")
    for yy, ph in ((282, 26), (292, -24)):
        g += P(f"M 214 {yy} Q 258 {yy + ph} 302 {yy} Q 346 {yy - ph} 390 {yy} "
               f"Q 434 {yy + ph} 478 {yy} Q 522 {yy - ph} 546 {yy}", stroke=CREAM, w=10)
    g += P("M 186 296 A 194 30 0 0 0 574 296 Q 568 392 380 398 Q 194 392 186 296 Z", "#d9734f")
    g += R(352, 396, 56, 15, 8, "#b85a3a")
    g += wrap(L(470, 148, 396, 262, WOOD_D, 10), L(494, 160, 406, 268, WOOD, 10))
    for dx, sway in ((-6, 10), (4, -12), (14, 6)):
        g += P(f"M {388 + dx} 266 Q {388 + dx + sway} 296 {376 + dx * 0.6} 322 "
               f"Q {370 + dx * 0.5} 340 {376 + dx * 0.4} 356", stroke=CREAM, w=9)
    g += P("M 300 190 q 9 -15 0 -30 q -9 -15 0 -30", stroke=STEAM_C, w=9, opacity=0.9)
    g += P("M 340 178 q 9 -15 0 -30", stroke=STEAM_C, w=8, opacity=0.9)
    return g


def art_fan():
    """饭：堆得尖尖的白米饭冒热气（主角撑满画面），青瓷碗坐在小餐垫上。"""
    g = ground() + cloth(380, 398, 560, 78)
    dome = ("M 218 322 Q 220 272 268 258 Q 282 226 322 230 Q 340 200 382 206 "
            "Q 424 198 440 232 Q 480 228 492 262 Q 540 276 542 322 Z")
    g += P(dome, WHITE)
    g += bowl_body(380, 322, 162, 96, TEAL, TEAL_D)
    g += R(300, 356, 160, 15, 7, WHITE, 0.85)
    for gx, gy in [(330, 268), (384, 246), (428, 272)]:
        g += E(gx, gy, 8, 4, GRAIN)
    g += steam_wisp(330, 192, 108, 16)
    g += steam_wisp(382, 172, 128, -18)
    g += steam_wisp(432, 190, 106, 16)
    return g


def art_cai():
    """菜：一颗大青菜立在小碟上——三片厚白帮撑在下层，大绿叶占上层并左右外翻。"""
    g = ground(380, 442, 235, 24)
    g += E(380, 426, 212, 36, PLATE_SH) + E(380, 419, 202, 32, WHITE) + E(380, 415, 136, 22, PLATE_IN)

    def choy(s, rot, tx, ty):
        # 三片厚白帮（上探进叶层，无圆球底，避免读成萝卜）+ 小白底
        stalks = (R(-56, -30, 36, 120, 17, VEG_W) + R(-18, -34, 36, 126, 17, VEG_W)
                  + R(20, -30, 36, 120, 17, VEG_W))
        base = E(0, 86, 46, 13, VEG_W)
        seams = (L(-37, -20, -37, 78, VEG_W_D, 4) + L(37, -20, 37, 78, VEG_W_D, 4))
        # 大绿叶：中间直立 + 左右斜外翻（叶盖住帮顶）
        leaves = ('<g transform="rotate(-16 -18 -30)">' + E(-18, -100, 40, 66, GREEN_L) + "</g>"
                  + '<g transform="rotate(16 18 -30)">' + E(18, -100, 40, 66, GREEN_L) + "</g>"
                  + E(-68, -72, 40, 58, GREEN) + E(68, -72, 40, 58, GREEN)
                  + E(0, -120, 36, 62, GREEN))
        # 叶脉
        veins = (L(0, -62, 0, -178, VEG_V, 4)
                 + L(-68, -18, -80, -122, VEG_V, 3) + L(68, -18, 80, -122, VEG_V, 3))
        return f'<g transform="translate({tx},{ty}) rotate({rot}) scale({s})">{stalks}{base}{seams}{leaves}{veins}</g>'

    g += choy(0.6, 44, 534, 398)     # 后侧小半颗
    g += choy(1.0, 0, 366, 346)      # 前面整颗大青菜
    g += E(238, 434, 32, 10, GREEN_L, 0.9)
    return g

def art_dan():
    g = ground() + plate(380, 414, 180, 35)
    # 整蛋（右）
    g += E(524, 350, 58, 76, EGG_D) + E(516, 344, 58, 76, EGG_W)
    g += C(498, 316, 12, WHITE, 0.9)
    # 磕开的蛋（左）：蛋黄 + 锯齿蛋壳
    g += C(330, 344, 40, YOLK) + C(318, 332, 11, YOLK_L) + C(314, 328, 4, WHITE, 0.9)
    shell = ("M 264 352 L 284 330 L 304 352 L 324 328 L 344 352 L 364 330 L 384 352 "
             "Q 390 388 358 404 Q 324 414 294 400 Q 262 386 264 352 Z")
    g += P(shell, EGG_W)
    g += P("M 264 352 L 284 330 L 304 352 L 324 328 L 344 352 L 364 330 L 384 352",
           stroke=EGG_D, w=5)
    return g


def art_cha():
    """茶：茶壶 + 玻璃杯绿茶 + 飘着两片茶叶——三重信号都是茶。"""
    g = ground(380, 442, 250, 24)
    g += E(232, 424, 102, 15, SHADOW)                                                    # 壶影（与杯子同落地面）
    g += E(485, 424, 64, 11, SHADOW)                                                     # 杯影
    # 茶壶（后左，落地与杯子同一重力）
    g += C(232, 324, 96, "#b5763a")
    g += E(232, 238, 54, 15, "#8a5a33")
    g += C(232, 220, 14, "#8a5a33") + C(232, 220, 6, "#c89058")
    g += P("M 322 302 Q 368 278 354 224", stroke="#b5763a", w=24)
    g += E(352, 228, 13, 16, "#8a5a33", 0.8)
    g += P("M 142 314 Q 84 330 130 402", stroke="#8a5a33", w=15)
    # 玻璃杯（前右）+ 绿茶汤
    g += E(480, 306, 66, 13, "#cfe6d8")
    g += P("M 428 304 L 440 408 Q 442 420 456 420 L 514 420 Q 528 420 530 408 L 542 304 Z", "#dff0f7", 0.92)
    g += P("M 434 314 L 444 394 Q 446 404 458 404 L 512 404 Q 524 404 526 394 L 536 314 Z", "#b5c95a")
    g += E(485, 314, 54, 11, "#c9d95a")
    # 飘着的三片茶叶
    g += P("M 462 310 Q 474 300 486 310 Q 474 318 462 310 Z", "#6a9a5c")
    g += P("M 424 320 Q 436 310 448 320 Q 436 328 424 320 Z", "#8fb872")
    g += P("M 492 318 Q 502 310 512 318 Q 502 326 492 318 Z", "#8fb872")
    # 热气
    g += P("M 470 262 q 9 -15 0 -30 q -9 -15 0 -30", stroke=STEAM_C, w=8, opacity=0.9)
    g += P("M 512 268 q 8 -13 0 -26", stroke=STEAM_C, w=7, opacity=0.9)
    return g


def art_tang():
    g = ground() + plate(380, 414, 190, 36)
    g += candy(462, 378, 0.72, "#f2b53c", "#d99a2b", WHITE, 16)
    g += candy(330, 342, 0.95, RED, RED_D, "#fdf8ec", -10)
    return g


def art_bing():
    g = ground() + plate(380, 416, 192, 36)
    g += C(386, 322, 108, COOKIE_D) + C(380, 316, 108, COOKIE)
    # 芝麻点：一颗颗圆润小点（不用扁长椭圆，避免看成小虫）
    for chx, chy, chz in [(330, 270, 7), (414, 252, 6), (456, 320, 7), (388, 300, 8),
                          (326, 346, 6), (404, 364, 6), (354, 310, 5), (444, 282, 6),
                          (372, 382, 7), (300, 318, 6), (352, 244, 5)]:
        g += C(chx, chy, chz, CHIP)
    for sx, sy in [(296, 246), (462, 254), (300, 388)]:
        g += C(sx, sy, 3.5, COOKIE_D)
    # 上缘一口月牙咬印（卡底奶油色遮出缺口）+ 两粒饼干屑
    g += C(452, 232, 28, "#fdf8ec")
    g += C(480, 264, 4, COOKIE_D) + C(494, 278, 3, COOKIE_D)
    return g


def art_li():
    g = ground() + plate(380, 418, 178, 34)
    body = ("M 380 136 "
            "C 398 148 410 176 414 214 "
            "C 420 252 470 258 478 306 "
            "C 486 360 442 392 380 392 "
            "C 318 392 274 360 282 306 "
            "C 290 258 340 252 346 214 "
            "C 350 176 362 148 380 136 Z")
    g += f'<g transform="translate(6,8)">{P(body, PEAR_D)}</g>'
    g += P(body, PEAR)
    g += E(344, 300, 20, 34, WHITE, 0.5)
    g += P("M 380 138 Q 390 116 408 104", stroke="#8a5a33", w=11)
    stem_leaf = (P("M 0 0 Q 30 -11 72 0 Q 30 11 0 0 Z", GREEN)
                 + L(8, 0, 58, 0, VEG_V, 3))
    g += f'<g transform="translate(414,108) rotate(26)">{stem_leaf}</g>'
    return g


def arts():
    return {
        "米": art_mi(), "面": art_mian(), "饭": art_fan(), "菜": art_cai(),
        "蛋": art_dan(), "茶": art_cha(), "糖": art_tang(), "饼": art_bing(),
        "梨": art_li(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import 识字卡片_字库 as ZIKU

    GID, SEEDS = "shiwu", set()
    expect = []
    for g in ZIKU.GROUPS:
        if g["id"] == GID:
            for item in g["chars"]:
                k = item["char"] if isinstance(item, dict) else item
                if k not in SEEDS:
                    expect.append(k)
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"食物组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，种子字 {sorted(SEEDS) or '无'}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
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
    assert got == expect and set(a) == set(got) and not bad, "自检未通过"
    print("自检通过 ✓")
