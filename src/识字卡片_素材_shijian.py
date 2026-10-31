#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画——时间组（12 字）：年分时早午晚春夏秋冬今昨。

年=红灯笼+烟花+鞭炮；分=绿挂钟特写（红长分针走一格）；
时=红闹钟指 8 点（红短针+月亮星星）；早=太阳爬上地平线+小花；
午=太阳正头顶+小影子；晚=月亮星星；春=新芽小花；夏=大太阳+西瓜；
秋=飘落的枫叶；冬=雪人；今=日历勾出今天+太阳+小朋友；
昨=月亮+睡着的小朋友+日历翻页。
日/月另有专卡，这里只把它们当作场景配角，不重复日卡月卡的构图。
"""
import importlib.util
import math
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_shijian", os.path.join(_HERE, "识字卡片_素材库.py"))


# ---------- 通用小件 ----------
def sun(cx, cy, r, face=False):
    """圆太阳 + 八向光芒（同 ball 的深一号底画法）。"""
    g = ""
    for i in range(8):
        a = math.radians(i * 45)
        x1, y1 = cx + (r + 16) * math.cos(a), cy + (r + 16) * math.sin(a)
        x2, y2 = cx + (r + 46) * math.cos(a), cy + (r + 46) * math.sin(a)
        g += lib.L(x1, y1, x2, y2, lib.YEL_D, 9)
    g += lib.C(cx + r * 0.05, cy + r * 0.06, r, "#e2952a")
    g += lib.C(cx - r * 0.04, cy - r * 0.04, r * 0.94, lib.SUN)
    g += lib.C(cx - r * 0.32, cy - r * 0.32, r * 0.2, lib.SUN_L, 0.9)
    if face:
        g += lib.C(cx - 20, cy - 10, 6, lib.INK)
        g += lib.C(cx + 20, cy - 10, 6, lib.INK)
        g += lib.P(f"M {cx-20} {cy+12} Q {cx} {cy+28} {cx+20} {cy+12}", stroke=lib.INK, w=6)
    return g


def crescent(cx, cy, r, fill=lib.SUN):
    """弯月：鼓包朝左、月口朝右。"""
    d = (f"M {cx} {cy - r} "
         f"C {cx - r * 1.18} {cy - r * 0.52} {cx - r * 1.18} {cy + r * 0.52} {cx} {cy + r} "
         f"C {cx - r * 0.42} {cy + r * 0.48} {cx - r * 0.42} {cy - r * 0.48} {cx} {cy - r} Z")
    return lib.P(d, fill)


def _clock_pt(cx, cy, deg, ln):
    """钟面方向：deg 从 12 点方向顺时针计。"""
    a = math.radians(deg)
    return cx + ln * math.sin(a), cy - ln * math.cos(a)


def clock_face(cx, cy, r_face, hour_deg, min_deg, rim=lib.TEAL, rim_d=lib.TEAL_D,
               hour_col=None, min_col=None, wedge=False):
    """钟面：只有刻度点，不写数字。指针=时针粗、分针细；可配色，可选高亮 12→1 格。"""
    g = lib.C(cx + 6, cy + 6, r_face + 16, rim_d)
    g += lib.C(cx, cy, r_face + 16, rim)
    g += lib.C(cx, cy, r_face, lib.WHITE)
    if wedge:
        a = _clock_pt(cx, cy, 0, r_face * 0.86)
        b = _clock_pt(cx, cy, 30, r_face * 0.86)
        g += lib.PG([(cx, cy), a, b], "#f7e2a0")
    for i in range(12):
        r1 = r_face * (0.74 if i % 3 == 0 else 0.8)
        x1, y1 = _clock_pt(cx, cy, i * 30, r1)
        x2, y2 = _clock_pt(cx, cy, i * 30, r_face * 0.9)
        g += lib.L(x1, y1, x2, y2, lib.INK, 6 if i % 3 == 0 else 3.5)
    hx, hy = _clock_pt(cx, cy, hour_deg, r_face * 0.5)
    mx, my = _clock_pt(cx, cy, min_deg, r_face * 0.74)
    g += lib.L(cx, cy, hx, hy, hour_col or lib.INK, 14)
    g += lib.L(cx, cy, mx, my, min_col or lib.INK, 8)
    g += lib.C(cx, cy, 9, "#e8a13c")
    return g


def lantern(cx, cy, s=1.0):
    """红灯笼：金盖金底、灯笼筋、挂绳和流苏。"""
    g = lib.L(cx, cy - 210 * s, cx, cy - 112 * s, lib.INK, 7)
    g += lib.E(cx + 6 * s, cy + 7 * s, 128 * s, 102 * s, lib.RED_D)
    g += lib.E(cx, cy, 128 * s, 102 * s, lib.RED)
    g += lib.P(f"M {cx-62*s} {cy-88*s} Q {cx-94*s} {cy} {cx-62*s} {cy+88*s}",
               stroke=lib.RED_D, w=5 * s)
    g += lib.P(f"M {cx+62*s} {cy-88*s} Q {cx+94*s} {cy} {cx+62*s} {cy+88*s}",
               stroke=lib.RED_D, w=5 * s)
    g += lib.L(cx, cy - 96 * s, cx, cy + 96 * s, lib.RED_D, 4 * s)
    g += lib.R(cx - 56 * s, cy - 124 * s, 112 * s, 26 * s, 10 * s, lib.YEL)
    g += lib.R(cx - 46 * s, cy + 96 * s, 92 * s, 20 * s, 9 * s, lib.YEL)
    g += lib.L(cx, cy + 116 * s, cx, cy + 148 * s, lib.YEL_D, 7)
    g += lib.R(cx - 9 * s, cy + 146 * s, 18 * s, 32 * s, 8 * s, lib.YEL_D)
    for dx in (-7, 0, 7):
        g += lib.L(cx + dx * s, cy + 178 * s, cx + dx * s * 1.4, cy + 208 * s, lib.YEL_D, 4)
    return g


def maple_leaf(cx, cy, s, rot, fill):
    """简笔枫叶：三大瓣 + 叶柄，可旋转，表示飘落。"""
    segs = [
        ("M", [(0, -100)]),
        ("C", [(18, -66), (20, -60), (45, -58)]),
        ("C", [(40, -30), (42, -26), (70, -20)]),
        ("C", [(50, 5), (50, 10), (55, 35)]),
        ("C", [(30, 30), (20, 32), (8, 50)]),
        ("L", [(5, 95)]), ("L", [(-5, 95)]), ("L", [(-8, 50)]),
        ("C", [(-20, 32), (-30, 30), (-55, 35)]),
        ("C", [(-50, 10), (-50, 5), (-70, -20)]),
        ("C", [(-42, -26), (-40, -30), (-45, -58)]),
        ("C", [(-20, -60), (-18, -66), (0, -100)]),
        ("Z", []),
    ]
    d = ""
    for tag, ps in segs:
        d += " " + tag + "".join(f" {cx + x * s:.1f} {cy + y * s:.1f}" for x, y in ps)
    return f'<g transform="rotate({rot} {cx} {cy})">' + lib.P(d, fill) + "</g>"


def calendar(cx=470, top=170, frame=lib.YEL, header=lib.RED, cell=lib.PANEL_Y, today=None):
    """小日历：格子里没有任何数字，只用颜色。today=(行,列) 时该格金色高亮加勾。"""
    x0 = cx - 155
    g = lib.R(x0 - 8, top - 8, 326, 266, 26, frame)
    g += lib.R(x0 + 6, top + 6, 298, 238, 18, lib.WHITE)
    g += lib.R(x0 + 6, top + 6, 298, 56, 18, header)
    for rx in (cx - 70, cx + 70):
        g += lib.R(rx - 7, top - 26, 14, 46, 7, "#9aa5ad")
    for ri in range(3):
        for ci in range(5):
            x = x0 + 47 + 54 * ci
            y = top + 112 + 50 * ri
            if today == (ri, ci):
                g += lib.C(x, y, 27, lib.SUN, 0.35)
                g += lib.R(x - 22, y - 20, 44, 40, 10, lib.SUN)
                g += lib.check(x, y, 13, lib.RED)
            else:
                g += lib.R(x - 22, y - 20, 44, 40, 10, cell)
    return g


# ---------- 各卡场景 ----------
def card_nian():
    """年：大红灯笼 + 烟花 + 鞭炮串——红金配色的过年场景。"""
    g = lib.ground(380, 452, 235, 24)
    g += lib.C(280, 262, 165, "#fdeaa0", 0.4)          # 金色柔光
    g += lib.L(280, 66, 280, 138, lib.INK, 6)          # 挂绳
    g += lantern(280, 262, 1.0)                        # 大红灯笼
    for cx, cy, rr, col in ((110, 108, 46, lib.YEL), (652, 104, 40, lib.RED)):
        for i in range(8):
            a = math.radians(i * 45 + 12)
            g += lib.L(cx + rr * 0.42 * math.cos(a), cy + rr * 0.42 * math.sin(a),
                       cx + rr * math.cos(a), cy + rr * math.sin(a), col, 7)
        g += lib.C(cx, cy, 9, col)
    g += lib.L(640, 36, 640, 138, lib.INK, 5)
    for bx, by, ba in ((616, 158, 14), (656, 190, -14), (620, 222, 14), (658, 254, -14)):
        g += f'<g transform="rotate({ba} {bx} {by})">' + lib.R(bx - 13, by - 20, 26, 40, 8, lib.RED_D) + "</g>"
        g += lib.L(bx, by - 20, bx, by - 6, lib.YEL_D, 4)
    g += lib.L(640, 138, 640, 156, lib.YEL_D, 5)
    return g


def card_fen():
    """分：绿挂钟放大特写——红色长分针刚走过 12 一小格（淡黄高亮格=一分钟）。"""
    import math
    g = lib.ground(380, 452, 235, 24)
    a0 = (380 + 158 * math.cos(math.radians(0)), 240 - 158 * math.sin(math.radians(0)))
    a1 = (380 + 158 * math.cos(math.radians(30)), 240 - 158 * math.sin(math.radians(30)))
    g += lib.PG([(380, 240), a0, a1], "#f7e2a0")
    g += clock_face(380, 240, 172, 30, 30, rim=lib.TEAL, rim_d=lib.TEAL_D,
                    hour_col="#b7bcc2", min_col=lib.RED)
    g += lib.C(458, 108, 10, lib.RED)
    return g


def card_shi():
    """时：红闹钟指 8 点睡觉——红色短时针 + 灰长分针 + 月亮星星。"""
    g = lib.ground()
    g += lib.L(320, 406, 296, 458, lib.WOOD_D, 15)
    g += lib.L(440, 406, 464, 458, lib.WOOD_D, 15)
    g += lib.C(306, 148, 42, lib.YEL_D)
    g += lib.C(300, 144, 36, lib.YEL)
    g += lib.C(454, 148, 42, lib.YEL_D)
    g += lib.C(448, 144, 36, lib.YEL)
    g += lib.R(374, 118, 12, 32, 6, "#c9cdd1")
    g += lib.P("M 118 96 A 44 44 0 1 0 118 178 A 35 35 0 1 1 118 96 Z", lib.YEL)
    g += lib.wrap(lib.C(178, 108, 7, lib.YEL_D), lib.C(96, 220, 6, lib.YEL_D))
    g += clock_face(380, 290, 128, 240, 0, rim=lib.RED, rim_d=lib.RED_D,
                    hour_col=lib.RED, min_col="#b7bcc2")
    return g


def card_zao():
    # 太阳爬上地平线：半轮日头 + 光芒，配一朵小花
    g = lib.ground()
    for deg in (-70, -35, 0, 35, 70):
        a = math.radians(deg)
        x1, y1 = 380 + 104 * math.sin(a), 424 - 104 * math.cos(a)
        x2, y2 = 380 + 134 * math.sin(a), 424 - 134 * math.cos(a)
        g += lib.L(x1, y1, x2, y2, lib.YEL_D, 9)
    g += lib.P("M 290 424 C 290 356 328 318 380 318 C 432 318 470 356 470 424 Z", lib.SUN)
    g += lib.C(348, 376, 20, lib.SUN_L, 0.8)
    g += lib.L(568, 452, 568, 398, lib.GREEN, 8)
    g += lib.flower5(568, 384, 24)
    return g


def card_wu():
    # 太阳正头顶：大太阳悬在画布上方，下面小朋友脚下只有短短一截影子
    g = lib.ground()
    g += sun(380, 122, 66)
    g += lib.E(380, 440, 44, 9, lib.INK, 0.32)
    g += lib.kid(380, 436, s=0.62, face="smile")
    return g


def card_wan():
    # 月亮星星出来了
    g = lib.ground()
    g += lib.star5(206, 150, 30)
    g += lib.star5(618, 196, 24)
    g += lib.star5(566, 112, 17)
    g += crescent(430, 240, 105)
    g += lib.P("M 396 268 Q 414 284 432 268", stroke=lib.INK, w=6)
    return g


def card_chun():
    # 春：土里钻出新芽，旁边一朵小花
    g = lib.ground()
    g += lib.E(380, 436, 66, 14, lib.WOOD_D)
    g += lib.L(380, 434, 380, 330, lib.GREEN, 13)
    g += lib.P("M 380 344 C 318 338 292 296 306 268 C 344 266 376 300 380 340 Z", lib.GREEN)
    g += lib.P("M 380 344 C 442 338 468 296 454 268 C 416 266 384 300 380 340 Z", lib.GREEN_L)
    g += lib.C(380, 326, 13, lib.GREEN_L)
    g += lib.L(196, 452, 196, 404, lib.GREEN, 8)
    g += lib.flower5(196, 390, 22, "#f0876f")
    return g


def card_xia():
    # 夏：大太阳 + 一牙西瓜
    g = lib.ground()
    g += sun(196, 148, 76)
    g += lib.P("M 250 330 C 265 420 320 455 380 455 C 440 455 495 420 510 330 Z", lib.GREEN)
    g += lib.P("M 270 330 C 282 405 325 434 380 434 C 435 434 478 405 490 330 Z", lib.RED)
    for sx, sy, sr in ((330, 392, 9), (378, 410, 9), (426, 392, 9), (378, 366, 8)):
        g += lib.drop(sx, sy, sr, lib.INK)
    return g


def card_qiu():
    # 秋：枫叶一片片飘下来
    g = lib.ground()
    g += maple_leaf(236, 196, 0.62, -24, lib.RED)
    g += maple_leaf(520, 226, 0.54, 18, lib.YEL)
    g += maple_leaf(384, 316, 0.68, 4, "#f0876f")
    g += maple_leaf(612, 356, 0.44, -14, lib.RED_D)
    return g


def card_dong():
    # 冬：戴红围巾的雪人
    g = lib.ground()
    for sx, sy, sr in ((172, 132, 10), (596, 116, 8), (646, 268, 9), (124, 262, 7)):
        g += lib.C(sx, sy, sr, "#cfe0ec")
    g += lib.L(322, 340, 262, 296, "#8a5a33", 10)
    g += lib.L(438, 340, 498, 296, "#8a5a33", 10)
    g += lib.C(383, 373, 58, "#d7e5ee")
    g += lib.C(378, 368, 58, "#eef5f9")
    g += lib.C(382, 256, 42, "#d7e5ee")
    g += lib.C(377, 251, 42, "#eef5f9")
    g += lib.P("M 340 290 Q 380 306 420 290 L 420 308 Q 380 324 340 308 Z", lib.RED)
    g += lib.R(392, 306, 22, 48, 10, lib.RED)
    g += lib.C(366, 240, 6, lib.INK)
    g += lib.C(394, 240, 6, lib.INK)
    g += lib.PG([(382, 248), (382, 260), (416, 254)], "#f0876f")
    g += lib.P("M 366 266 Q 380 276 394 266", stroke=lib.INK, w=5)
    g += lib.C(380, 344, 7, lib.INK)
    g += lib.C(380, 374, 7, lib.INK)
    return g


def card_jin():
    """今：太阳当空，日历上勾出今天。"""
    g = lib.ground(380, 452, 235, 24)
    g += lib.C(140, 132, 54, lib.SUN)
    for i in range(8):
        a = math.radians(i * 45 + 8)
        g += lib.L(140 + 72 * math.cos(a), 132 + 72 * math.sin(a),
                   140 + 104 * math.cos(a), 132 + 104 * math.sin(a), lib.YEL_D, 8)
    g += lib.R(320, 236, 300, 186, 16, lib.WHITE)
    g += lib.R(320, 236, 300, 54, 12, lib.RED)
    g += lib.L(320, 292, 620, 292, "#e8d9a0", 5)
    g += lib.L(470, 292, 470, 422, "#e8d9a0", 5)
    g += lib.L(320, 356, 620, 356, "#e8d9a0", 5)
    g += lib.R(324, 296, 142, 116, 12, "#f7e2a0")
    g += lib.P("M 350 350 L 382 384 L 444 306", stroke="#c96a4a", w=16)
    g += lib.kid(150, 448, s=0.95, shirt=lib.RED)
    g += lib.P("M 196 336 Q 250 322 300 330", stroke="#f7c49c", w=24)
    g += lib.C(304, 330, 14, "#f7c49c")
    return g


def card_zuo():
    """昨：月亮出来了，日历翻过一页，小朋友睡着了——已经过去的就是昨天。"""
    g = lib.ground(380, 452, 235, 24)
    g += lib.C(120, 130, 44, "#f2c14e")
    g += lib.C(104, 118, 34, "#fdf8ec")
    g += lib.C(590, 120, 7, "#d9c27a") + lib.C(640, 170, 6, "#d9c27a") + lib.C(560, 200, 5, "#d9c27a")
    g += lib.E(300, 420, 62, 18, "#cfe6f7")
    g += lib.C(255, 398, 42, "#f7c49c")
    g += lib.P("M 224 388 Q 244 372 266 386", stroke="#5a3d2b", w=8)
    g += lib.P("M 246 402 Q 252 398 258 402", stroke="#3a2418", w=4)
    g += lib.E(340, 416, 92, 34, "#9cc9e2")
    g += lib.E(430, 402, 16, 22, "#b8d4ea")
    g += lib.R(430, 240, 260, 170, 14, "#cfdce8")
    g += lib.R(430, 240, 260, 46, 12, "#9db4cc")
    g += lib.P("M 470 240 L 480 268 L 456 262 L 466 286 L 490 268", stroke="#9db4cc", w=5)
    return g


def arts():
    return {
        "年": card_nian(),
        "分": card_fen(),
        "时": card_shi(),
        "早": card_zao(),
        "午": card_wu(),
        "晚": card_wan(),
        "春": card_chun(),
        "夏": card_xia(),
        "秋": card_qiu(),
        "冬": card_dong(),
        "今": card_jin(),
        "昨": card_zuo(),
    }


GROUP_CARDS = [
    {"char": "年", "pinyin": "nián", "tone": "第二声",
     "sentence": "大红灯笼迎新年。",
     "say": "挂起大红灯笼，就是过年啦。",
     "chat": "过年时你最想做什么？",
     "life": "过年帮家里挂一个小灯笼。"},
    {"char": "分", "pinyin": "fēn", "tone": "第一声",
     "sentence": "等一分钟就好。",
     "say": "红色的长针是分针，走一小格就是一分。",
     "chat": "长针走一小格，几分钟过去啦？",
     "life": "想说“等我一分钟”的时候，就说这句。"},
    {"char": "时", "pinyin": "shí", "tone": "第二声",
     "sentence": "按时上床睡觉啦。",
     "say": "短短的红针指到 8，就是 8 点（时）。",
     "chat": "现在几点啦？",
     "life": "每天晚上 8 点，按时睡觉。"},
    {"char": "早", "pinyin": "zǎo", "tone": "第三声",
     "sentence": "早上的太阳爬上来。",
     "say": "红彤彤的太阳爬上地平线。",
     "chat": "早起的太阳从哪里升起来？",
     "life": "早点起床，和太阳问个早。"},
    {"char": "午", "pinyin": "wǔ", "tone": "第三声",
     "sentence": "太阳晒得暖洋洋。",
     "say": "太阳升到头顶，影子变短。",
     "chat": "什么时候影子最短呀？",
     "life": "中午的影子最短，踩踩影子。"},
    {"char": "晚", "pinyin": "wǎn", "tone": "第三声",
     "sentence": "月亮星星出来了。",
     "say": "天黑了，月亮星星出来了。",
     "chat": "晚上天上有什么？",
     "life": "晚上找一找月亮和星星。"},
    {"char": "春", "pinyin": "chūn", "tone": "第一声",
     "sentence": "春天花开芽儿冒。",
     "say": "天气变暖，小草发芽花开。",
     "chat": "春天和冬天有什么不一样？",
     "life": "春天去看发芽的小草。"},
    {"char": "夏", "pinyin": "xià", "tone": "第四声",
     "sentence": "夏天西瓜甜又大。",
     "say": "夏天太阳大，吃西瓜真凉快。",
     "chat": "夏天你最爱吃什么？",
     "life": "夏天和爸爸妈妈一起吃西瓜。"},
    {"char": "秋", "pinyin": "qiū", "tone": "第一声",
     "sentence": "秋天枫叶飘下来。",
     "say": "秋天叶子变红飘下来。",
     "chat": "秋天的叶子是什么颜色？",
     "life": "捡一片落叶看看纹路。"},
    {"char": "冬", "pinyin": "dōng", "tone": "第一声",
     "sentence": "冬天下雪啦。",
     "say": "冬天下雪，雪人戴围巾。",
     "chat": "冬天和夏天哪个冷？",
     "life": "冬天戴上围巾和手套。"},
    {"char": "今", "pinyin": "jīn", "tone": "第一声",
     "sentence": "日历上勾出今天。",
     "say": "日历上勾出的是今天。",
     "chat": "今天日历上勾了哪一天？",
     "life": "早上在日历上勾出今天。"},
    {"char": "昨", "pinyin": "zuó", "tone": "第二声",
     "sentence": "日历翻过是昨天。",
     "say": "日历翻过去的那页，就是昨天。",
     "chat": "昨天你做了什么开心的事？",
     "life": "睡前说一件昨天开心的事。"},
]


def arts():
    return {
        "年": card_nian(),
        "分": card_fen(),
        "时": card_shi(),
        "早": card_zao(),
        "午": card_wu(),
        "晚": card_wan(),
        "春": card_chun(),
        "夏": card_xia(),
        "秋": card_qiu(),
        "冬": card_dong(),
        "今": card_jin(),
        "昨": card_zuo(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    ziku = _load("scys_ziku_shijian", os.path.join(_HERE, "识字卡片_字库.py"))
    grp = next(g for g in ziku.GROUPS if g["id"] == "shijian")
    expect = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    mine = [c["char"] for c in GROUP_CARDS]
    assert mine == expect, f"卡序与字库不一致：{mine} vs {expect}"

    cards = arts()
    assert set(cards) == set(mine), "arts 键与 GROUP_CARDS 不一致"
    punct = "，。！？、；：·—…"
    for c in GROUP_CARDS:
        ch = c["char"]
        core = [t for t in c["sentence"] if t not in punct]
        assert 4 <= len(core) <= 10, f"{ch} sentence 长度 {len(core)}"
        assert ch in c["sentence"], f"{ch} sentence 未含目标字"
        for k in ("say", "chat", "life"):
            assert len(c[k]) <= 30, f"{ch} {k} 超长：{len(c[k])}"
        v = cards[ch]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            assert bad not in v, f"{ch} 含禁止标记 {bad}"
    print(f"时间组：卡数 {len(GROUP_CARDS)}，arts {len(cards)}，与字库比对一致 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '候', 'pinyin': 'hòu', 'tone': '第四声', 'sentence': '现在是什么时候？', 'say': '看看表等一等，等着的时候。', 'chat': '“等车的时候可以做什么？”', 'life': '等开饭时看看钟，等一等。'},
]
_arts_mig = {
    '候': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="70" y="48" width="620" height="336" rx="30" fill="#f6e7cd"/><circle cx="252" cy="190" r="90" fill="#b57b44"/><circle cx="252" cy="184" r="88" fill="#c89058"/><circle cx="252" cy="184" r="72" fill="#fdfdfa"/><circle cx="312.0" cy="184.0" r="4.5" fill="#4a3226"/><circle cx="303.9615242270663" cy="214.0" r="4.5" fill="#4a3226"/><circle cx="282.0" cy="235.96152422706632" r="4.5" fill="#4a3226"/><circle cx="252.0" cy="244.0" r="4.5" fill="#4a3226"/><circle cx="222.0" cy="235.96152422706632" r="4.5" fill="#4a3226"/><circle cx="200.03847577293368" cy="214.0" r="4.5" fill="#4a3226"/><circle cx="192.0" cy="184.0" r="4.5" fill="#4a3226"/><circle cx="200.03847577293368" cy="154.0" r="4.5" fill="#4a3226"/><circle cx="221.99999999999997" cy="132.03847577293368" r="4.5" fill="#4a3226"/><circle cx="252.0" cy="124.0" r="4.5" fill="#4a3226"/><circle cx="282.0" cy="132.03847577293368" r="4.5" fill="#4a3226"/><circle cx="303.9615242270663" cy="153.99999999999997" r="4.5" fill="#4a3226"/><line x1="252" y1="184" x2="252" y2="134" stroke="#4a3226" stroke-width="7" stroke-linecap="round"/><line x1="252" y1="184" x2="284" y2="202" stroke="#4a3226" stroke-width="8" stroke-linecap="round"/><circle cx="252" cy="184" r="8" fill="#e8663c"/><rect x="292" y="382" width="22" height="60" rx="9" fill="#b57b44"/><rect x="486" y="382" width="22" height="60" rx="9" fill="#b57b44"/><rect x="286" y="296" width="228" height="18" rx="9" fill="#c89058"/><rect x="278" y="360" width="244" height="22" rx="10" fill="#c89058"/><rect x="386.0" y="342.0" width="20.8" height="52.800000000000004" rx="9.600000000000001" fill="#4a97c9"/><rect x="413.2" y="342.0" width="20.8" height="52.800000000000004" rx="9.600000000000001" fill="#4a97c9"/><ellipse cx="395.6" cy="407.6" rx="17.6" ry="8.0" fill="#4a3226" opacity="0.85"/><ellipse cx="453.2" cy="407.6" rx="17.6" ry="8.0" fill="#4a3226" opacity="0.85"/><path d="M 365.2 292.40000000000003 Q 363.6 356.40000000000003 378.0 358.0 L 442.0 358.0 Q 456.4 356.40000000000003 454.8 292.40000000000003 Q 410 279.6 365.2 292.40000000000003 Z" fill="#5fa8d8"/><line x1="374.8" y1="297.20000000000005" x2="358.8" y2="354.80000000000007" stroke="#f8cba4" stroke-width="24.0" stroke-linecap="round"/><circle cx="358.8" cy="354.80000000000007" r="10.4" fill="#f8cba4"/><line x1="445.2" y1="297.20000000000005" x2="461.2" y2="354.80000000000007" stroke="#f8cba4" stroke-width="24.0" stroke-linecap="round"/><circle cx="461.2" cy="354.80000000000007" r="10.4" fill="#f8cba4"/><circle cx="363.6" cy="244.40000000000006" r="8.8" fill="#f8cba4"/><circle cx="456.4" cy="244.40000000000006" r="8.8" fill="#f8cba4"/><circle cx="410" cy="236.40000000000006" r="49.6" fill="#f8cba4"/><path d="M 361.392 219.04000000000008 Q 365.36 177.87200000000007 410 180.84800000000007 Q 454.64 177.87200000000007 458.608 219.04000000000008 Q 437.28000000000003 210.60800000000006 410 215.56800000000007 Q 382.71999999999997 210.60800000000006 361.392 219.04000000000008 Z" fill="#5a3d2b"/><ellipse cx="392.4" cy="230.00000000000006" rx="8.0" ry="10.4" fill="#4a3226"/><circle cx="390.79999999999995" cy="225.04000000000005" r="2.72" fill="#fdfdfa"/><ellipse cx="427.6" cy="230.00000000000006" rx="8.0" ry="10.4" fill="#4a3226"/><circle cx="426.0" cy="225.04000000000005" r="2.72" fill="#fdfdfa"/><path d="M 381.2 210.60800000000006 Q 392.4 205.64800000000005 403.6 209.61600000000007" fill="none" stroke="#5a3d2b" stroke-width="4.800000000000001" stroke-linecap="round" stroke-linejoin="round"/><path d="M 416.4 209.61600000000007 Q 427.6 205.64800000000005 438.8 210.60800000000006" fill="none" stroke="#5a3d2b" stroke-width="4.800000000000001" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="410" cy="260.40000000000003" rx="8.0" ry="9.600000000000001" fill="#6b3325"/><circle cx="374.8" cy="247.60000000000005" r="8.8" fill="#f5a58c" opacity="0.8"/><circle cx="445.2" cy="247.60000000000005" r="8.8" fill="#f5a58c" opacity="0.8"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
