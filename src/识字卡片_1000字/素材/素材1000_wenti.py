#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1000字卡集 文体游戏 19 卡：舞琴鼓笛运动赛队铃涂弹吹筝积曲锣牌琵琶。

注：批次分配清单里 wenti 名下多写了「号」——经查 号 属 字库1000 的 shuzi 组
（素材1000_shuzi.py 已生产），加入本组会触发构建器「重复卡/多余卡」硬错误，故不出卡。

插画只用 素材库 组件（kid/ground/ball/hand/heart/star5/flower5/cloud_p...），
人物一律 kid()；音符/风筝尾结等为符号（允许），图上无文字。
"""
import sys
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa

W_CHARS = "舞琴鼓笛运动赛队铃涂弹吹筝积曲锣牌琵琶"


# ---------- 本文件小工具 ----------
def _dash(d, color, w, gap="4 9"):
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-dasharray="{gap}"/>')


def _rot(x, y, ang, inner):
    return f'<g transform="rotate({ang} {x} {y})">{inner}</g>'


def _head(cx, cy, s, look=(0, 0), face="smile", hair_color=HAIR, skin=SKIN):
    """kid() 同款头（自组姿态用），坐标=头心。"""
    hd = 62 * s
    top = cy - hd
    bang = cy - hd * 0.42
    f = [C(cx - 58 * s, cy + 10 * s, 11 * s, skin), C(cx + 58 * s, cy + 10 * s, 11 * s, skin),
         C(cx, cy, hd, skin)]
    f.append(P(f"M {cx-hd*0.98} {cy-hd*0.35} Q {cx-hd*0.9} {top-hd*0.18} {cx} {top-hd*0.12} "
               f"Q {cx+hd*0.9} {top-hd*0.18} {cx+hd*0.98} {cy-hd*0.35} "
               f"Q {cx+hd*0.55} {bang-hd*0.1} {cx} {bang} "
               f"Q {cx-hd*0.55} {bang-hd*0.1} {cx-hd*0.98} {cy-hd*0.35} Z", hair_color))
    lx, ly = look
    for ex in (-22, 22):
        f.append(E(cx + ex * s, cy - 8 * s, 10 * s, 13 * s, INK))
        f.append(C(cx + ex * s + lx * s, cy - 13 * s + ly * s, 3.4 * s, WHITE))
    f.append(P(f"M {cx-36*s} {cy-hd*0.52} Q {cx-22*s} {cy-hd*0.62} {cx-8*s} {cy-hd*0.54}",
               stroke=hair_color, w=6 * s))
    f.append(P(f"M {cx+8*s} {cy-hd*0.54} Q {cx+22*s} {cy-hd*0.62} {cx+36*s} {cy-hd*0.52}",
               stroke=hair_color, w=6 * s))
    my = cy + 26 * s
    if face == "open":
        f.append(P(f"M {cx-26*s} {my} Q {cx} {my-10*s} {cx+26*s} {my} Q {cx+24*s} {my+26*s} {cx} {my+30*s} "
                   f"Q {cx-24*s} {my+26*s} {cx-26*s} {my} Z", "#6b3325"))
        f.append(P(f"M {cx-14*s} {my+16*s} Q {cx} {my+8*s} {cx+14*s} {my+16*s} "
                   f"Q {cx+9*s} {my+27*s} {cx} {my+28*s} Q {cx-9*s} {my+27*s} {cx-14*s} {my+16*s} Z", "#f0876f"))
    elif face == "o":
        f.append(E(cx, my + 4 * s, 10 * s, 12 * s, "#6b3325"))
    else:
        f.append(P(f"M {cx-20*s} {my} Q {cx} {my+16*s} {cx+20*s} {my}", stroke=INK, w=7 * s))
    f.append(C(cx - 44 * s, cy + 14 * s, 11 * s, PINK, 0.8))
    f.append(C(cx + 44 * s, cy + 14 * s, 11 * s, PINK, 0.8))
    return wrap(*f)


def _note(cx, cy, s, color, rot=-12):
    """八分音符（符号）。"""
    g = wrap(
        E(0, 0, 22 * s, 15 * s, color),
        L(20 * s, -2 * s, 20 * s, -66 * s, color, 7 * s),
        P(f"M {20*s} {-66*s} Q {46*s} {-58*s} {40*s} {-32*s}", stroke=color, w=6 * s))
    return f'<g transform="translate({cx},{cy}) rotate({rot})">{g}</g>'


def _black_keys(x0, y, pattern, kw=9, kh=15):
    """钢琴黑键，pattern 为每组黑键数（2/3 交替）。"""
    out = ""
    x = x0
    for n in pattern:
        for i in range(n):
            out += R(x + i * (kw + 3), y, kw, kh, 2, INK)
        x += n * (kw + 3) + 14
    return out


def _bow(x, y, color, s=1.0):
    """风筝尾巴上的小蝴蝶结（两个对顶三角）。"""
    return wrap(PG([(x - 10 * s, y - 6 * s), (x, y), (x - 10 * s, y + 6 * s)], color),
                PG([(x + 10 * s, y - 6 * s), (x, y), (x + 10 * s, y + 6 * s)], color))


GROUP_CARDS = [
    {"char": "舞", "pinyin": "wǔ", "tone": "第三声",
     "sentence": "穿上裙子跳舞啦。", "say": "跟着音乐扭动身体就是跳舞。",
     "chat": "你最喜欢跟着哪首歌跳舞？", "life": "放首儿歌，一起跳一支。"},
    {"char": "琴", "pinyin": "qín", "tone": "第二声",
     "sentence": "家里有一架钢琴。", "say": "黑白键按下去会响，这是钢琴。",
     "chat": "钢琴的键是什么颜色的呀？", "life": "去商场让他按一按琴键。"},
    {"char": "鼓", "pinyin": "gǔ", "tone": "第三声",
     "sentence": "咚咚咚，敲大鼓。", "say": "两根鼓棒敲下去，咚咚响。",
     "chat": "鼓的声音是什么样的？", "life": "用小棒敲纸箱当小鼓。"},
    {"char": "笛", "pinyin": "dí", "tone": "第二声",
     "sentence": "吹笛子给妈妈听。", "say": "横着拿、轻轻吹的是笛子。",
     "chat": "笛子的声音细细的还是粗粗的？", "life": "卷张纸当笛子吹一吹。"},
    {"char": "运", "pinyin": "yùn", "tone": "第四声",
     "sentence": "天天运动身体好。", "say": "跑步、跳绳都是运动。",
     "chat": "你最喜欢什么运动呀？", "life": "每天下楼运动半小时。"},
    {"char": "动", "pinyin": "dòng", "tone": "第四声",
     "sentence": "大家一起动起来。", "say": "胳膊腿都动起来就是动。",
     "chat": "机器人不动了，怎么让它动？", "life": "喊口令：动动胳膊动动腿。"},
    {"char": "赛", "pinyin": "sài", "tone": "第四声",
     "sentence": "赛跑比赛开始啦。", "say": "两个人比谁跑得快就是赛。",
     "chat": "赛跑时你在前面还是后面？", "life": "和他赛跑一趟去拿小球。"},
    {"char": "队", "pinyin": "duì", "tone": "第四声",
     "sentence": "排队一个跟一个。", "say": "一个跟着一个走就是排队。",
     "chat": "排队时能不能挤到前面呀？", "life": "买菜时教他跟着排队。"},
    {"char": "铃", "pinyin": "líng", "tone": "第二声",
     "sentence": "摇铃铛，叮叮响。", "say": "拿住铃柄摇一摇，叮叮响。",
     "chat": "铃铛为什么不摇就不响呢？", "life": "摇铃铛让他猜在哪里响。"},
    {"char": "涂", "pinyin": "tú", "tone": "第二声",
     "sentence": "拿蜡笔涂颜色。", "say": "用蜡笔来回涂出颜色就是涂。",
     "chat": "这片太阳想涂什么颜色？", "life": "给画里的大苹果涂红色。"},
    {"char": "弹", "pinyin": "tán", "tone": "第二声（另读 dàn，如“子弹”）",
     "sentence": "弹琴要轻轻弹。", "say": "手指按琴键、抬起按下就是弹。",
     "chat": "弹琴用一根手指还是十根？", "life": "一起按琴键弹首小曲。"},
    {"char": "吹", "pinyin": "chuī", "tone": "第一声",
     "sentence": "吹泡泡，追泡泡。", "say": "嘴巴呼气吹出泡泡就是吹。",
     "chat": "泡泡为什么会飞起来又破掉？", "life": "吹泡泡给他追着玩。"},
    {"char": "筝", "pinyin": "zhēng", "tone": "第一声",
     "sentence": "风筝飞得好高呀。", "say": "拉着线跑，风筝就飞上天。",
     "chat": "风筝为什么要有长尾巴？", "life": "风好的时候去公园放风筝。"},
    {"char": "积", "pinyin": "jī", "tone": "第一声",
     "sentence": "积木搭得高又高。", "say": "一块一块往上积成高塔。",
     "chat": "积木塔搭几块会不倒？", "life": "和他比赛谁的塔搭得高。"},
    {"char": "曲", "pinyin": "qǔ", "tone": "第三声（另读 qū，如“弯曲”）",
     "sentence": "哼一支小曲儿。", "say": "好听的调子就是曲子。",
     "chat": "你还会哼哪首曲子呀？", "life": "睡前哼一首摇篮曲。"},
    {"char": "锣", "pinyin": "luó", "tone": "第二声",
     "sentence": "敲起小锣哐哐响。", "say": "用小槌敲锣边，哐哐响。",
     "chat": "锣和鼓的声音哪里不一样？", "life": "轻轻敲敲锅盖当小锣。"},
    {"char": "牌", "pinyin": "pái", "tone": "第二声",
     "sentence": "轮流出牌真好玩。", "say": "把牌张开发给每个人。",
     "chat": "你抽到了什么牌呀？", "life": "玩配对小牌，轮流出牌。"},
    {"char": "琵", "pinyin": "pí", "tone": "第二声",
     "sentence": "怀抱琵琶轻轻弹。", "say": "抱在怀里竖着弹的是琵琶。",
     "chat": "琵琶的身体像什么形状呀？", "life": "看一小段琵琶演奏视频。"},
    {"char": "琶", "pinyin": "pá", "tone": "第二声",
     "sentence": "琵琶一弹叮叮咚。", "say": "琵琶的声音像小珠子落盘。",
     "chat": "琵琶的声音像什么呀？", "life": "听一首琵琶曲，点头打拍子。"},
]


def arts():
    a = {}

    # 舞：裙摆飘、双臂扬（区别 legacy 歌=举臂+音符）
    a["舞"] = wrap(
        ground(380, 446, 240, 22),
        kid(x=380, y=430, s=1.05, pose="stand", shirt="#f0876f", skirt=True,
            arms="up", face="open", look=(0, -0.2)),
        _dash("M 258 300 Q 236 254 262 212", "#f0876f", 6),
        _dash("M 502 300 Q 524 254 498 212", "#f0876f", 6),
        _dash("M 262 402 Q 240 376 252 340", TEAL, 5),
        _dash("M 498 402 Q 520 376 508 340", TEAL, 5))

    # 琴：一架立式钢琴，黑白键清楚（区别 弹=人弹琴）
    a["琴"] = wrap(
        ground(380, 446, 270, 24),
        R(240, 150, 280, 210, 16, "#8a5a33"),
        R(230, 138, 300, 26, 10, WOOD_D),
        R(258, 170, 244, 118, 10, "#6b4a2e"),
        R(298, 184, 164, 66, 8, "#f4d3a4"),
        R(310, 196, 140, 10, 5, "#d9b98c"), R(310, 220, 140, 10, 5, "#d9b98c"),
        R(230, 356, 300, 36, 8, WOOD_L),
        R(238, 360, 284, 26, 4, WHITE),
        _black_keys(252, 360, [2, 3, 2, 3, 2, 3], kw=9, kh=16),
        R(244, 392, 22, 54, 8, WOOD_D), R(494, 392, 22, 54, 8, WOOD_D))

    # 鼓：大红包身鼓+双槌敲下（无人物，区别 锣=人提锣敲）
    a["鼓"] = wrap(
        ground(380, 446, 250, 24),
        L(330, 424, 308, 448, "#8a5a33", 10), L(430, 424, 452, 448, "#8a5a33", 10),
        R(270, 300, 220, 128, 22, RED),
        E(380, 300, 110, 26, "#f4d3a4"),
        R(270, 300, 220, 18, 9, YEL), R(270, 410, 220, 18, 9, YEL),
        C(310, 309, 4, "#d99a2b"), C(380, 309, 4, "#d99a2b"), C(450, 309, 4, "#d99a2b"),
        C(310, 419, 4, "#d99a2b"), C(380, 419, 4, "#d99a2b"), C(450, 419, 4, "#d99a2b"),
        L(244, 212, 358, 290, WOOD, 13), C(362, 294, 9, WOOD_L),
        L(516, 212, 402, 290, WOOD, 13), C(398, 294, 9, WOOD_L),
        _dash("M 352 268 Q 366 254 382 262", TEAL, 5),
        _dash("M 408 268 Q 394 254 378 262", TEAL, 5),
        P("M 320 240 Q 342 220 364 240", stroke=TEAL, w=6),
        P("M 396 240 Q 418 220 440 240", stroke=TEAL, w=6))

    # 笛：横吹长笛，手指按孔，笛尾飘小音符（区别 号）
    a["笛"] = wrap(
        ground(370, 446, 250, 24),
        kid(x=350, y=430, s=1.0, pose="stand", shirt=GREEN, face="o",
            arms="point", point_at=(500, 218), look=(0.6, 0)),
        R(392, 210, 212, 15, 7, "#cfd6da"),
        E(600, 217, 9, 7, "#aab3ba"),
        C(446, 217, 4, INK), C(478, 217, 4, INK), C(510, 217, 4, INK), C(542, 217, 4, INK),
        C(452, 224, 11, SKIN), C(506, 222, 11, SKIN),
        _note(636, 176, 0.55, TEAL, -14), _note(672, 132, 0.45, "#7cc8bb", 10))

    # 运：跳绳（绳从两手甩到脚下成大弧，区别 legacy 玩/拍=小孩+皮球）
    a["运"] = wrap(
        ground(380, 446, 250, 22),
        kid(x=380, y=424, s=1.05, pose="stand", shirt=YEL, arms="down",
            face="smile", look=(0.3, 0.2)),
        L(313, 330, 290, 354, RED, 11),
        L(447, 330, 470, 354, RED, 11),
        P("M 290 354 Q 234 394 252 430 Q 294 458 380 460 Q 466 458 508 430 "
          "Q 526 394 470 354", stroke=RED, w=6.5),
        _dash("M 322 452 Q 380 466 438 452", "#7cc8bb", 5))

    # 动：张臂踢腿动起来（原地运动操），两侧动效弧
    a["动"] = wrap(
        ground(380, 446, 240, 22),
        _head(380, 176, 0.95, look=(0, -0.3), face="open"),
        R(352, 236, 56, 76, 24, TEAL),
        L(356, 250, 292, 194, SKIN, 26), C(288, 190, 13, SKIN),
        L(404, 250, 468, 194, SKIN, 26), C(472, 190, 13, SKIN),
        L(366, 310, 306, 402, BLUE_D, 30), E(300, 410, 20, 9, INK),
        L(394, 310, 454, 402, BLUE_D, 30), E(460, 410, 20, 9, INK),
        _dash("M 254 300 Q 234 350 256 400", TEAL, 5),
        _dash("M 506 300 Q 526 350 504 400", TEAL, 5))

    # 赛：两人一前一后奋力赛跑，右侧小红旗（区别 队=三人同速排队）
    a["赛"] = wrap(
        ground(390, 446, 300, 24),
        R(676, 250, 10, 196, 5, WOOD_D),
        PG([(686, 254), (740, 272), (686, 290)], YEL),
        kid(x=490, y=430, s=0.95, pose="sprint", shirt=RED, arms="pump",
            face="open", look=(0.8, 0)),
        kid(x=250, y=430, s=0.9, pose="sprint", shirt=BLUE, arms="pump",
            face="o", look=(0.8, 0)),
        _dash("M 148 320 L 214 316", TEAL, 5),
        _dash("M 140 362 L 206 360", TEAL, 5))

    # 队：三个同色小朋友一前一后纵深前行（区别 散=两人牵手并排走）
    a["队"] = wrap(
        ground(390, 446, 300, 24),
        kid(x=566, y=432, s=0.92, pose="walk", shirt=TEAL, arms="swing",
            face="smile", look=(0.5, 0)),
        kid(x=412, y=416, s=0.9, pose="walk", shirt=TEAL, arms="swing",
            face="smile", look=(0.5, 0)),
        kid(x=258, y=400, s=0.88, pose="walk", shirt=TEAL, arms="swing",
            face="smile", look=(0.5, 0)))

    # 铃：手摇大铃铛，左右摆动+声波（手为 hand 组件）
    a["铃"] = wrap(
        ground(380, 446, 230, 22),
        R(366, 192, 28, 42, 12, WOOD_D),
        P("M 304 336 Q 296 238 380 228 Q 464 238 456 336 Q 466 348 482 352 "
          "L 278 352 Q 294 348 304 336 Z", YEL),
        R(270, 344, 220, 18, 9, YEL_D),
        C(380, 374, 15, "#b57b44"),
        E(326, 264, 12, 30, WHITE, 0.55),
        hand(428, 216, rot=-90, s=0.78),
        _dash("M 244 246 Q 222 292 246 336", TEAL, 5),
        _dash("M 516 246 Q 538 292 514 336", TEAL, 5),
        P("M 534 176 Q 558 206 534 236", stroke=TEAL, w=6),
        P("M 560 156 Q 594 200 560 244", stroke="#7cc8bb", w=6))

    # 涂：画纸上涂色，太阳涂了一半，蜡笔+手（区别 legacy 画=画架+整幅花）
    a["涂"] = wrap(
        ground(400, 446, 260, 24),
        _rot(400, 292, -3, wrap(
            R(248, 182, 304, 224, 12, WHITE),
            f'<circle cx="366" cy="282" r="64" fill="none" stroke="{YEL_D}" stroke-width="7"/>',
            PG([(366, 282), (366, 218), (424, 240), (430, 282)], YEL),
            PG([(366, 282), (430, 282), (410, 338), (366, 346)], "#f9c95e"),
            L(380, 236, 408, 260, "#e8a13c", 5), L(384, 300, 404, 322, "#e8a13c", 5))),
        _rot(560, 348, 34, wrap(
            R(512, 336, 96, 21, 10, RED),
            PG([(608, 334), (632, 346), (608, 358)], "#f4d3a4"),
            R(526, 340, 15, 13, 4, WHITE, 0.7))),
        hand(618, 306, rot=-34, s=0.85),
        _rot(196, 428, -14, wrap(R(150, 420, 92, 17, 8, BLUE),
                                 PG([(150, 420), (132, 428), (150, 437)], BLUE_D))),
        _rot(232, 452, 10, wrap(R(186, 444, 92, 17, 8, GREEN),
                                PG([(278, 444), (296, 452), (278, 461)], "#5f8f52"))))

    # 弹：坐姿弹琴，双手按在琴键上（区别 琴=钢琴物件）
    a["弹"] = wrap(
        ground(380, 450, 250, 22),
        kid(x=380, y=470, s=1.0, pose="sit", shirt=BLUE, face="o",
            arms="down", look=(0, 0.45)),
        L(292, 410, 284, 446, WOOD_D, 10), L(468, 410, 476, 446, WOOD_D, 10),
        R(246, 372, 268, 42, 10, "#8a5a33"),
        R(254, 378, 252, 26, 4, WHITE),
        _black_keys(268, 378, [2, 3, 2, 3, 2, 3], kw=8, kh=14),
        C(342, 376, 14, SKIN), C(418, 376, 14, SKIN))

    # 吹：吹出一串泡泡（区别 笛=横笛）
    a["吹"] = wrap(
        ground(370, 446, 250, 24),
        kid(x=320, y=430, s=1.0, pose="stand", shirt=PINK, face="o",
            arms="point", point_at=(444, 198), look=(0.8, -0.15)),
        L(404, 226, 448, 200, WOOD, 8),
        f'<circle cx="466" cy="188" r="16" fill="none" stroke="#aab3ba" stroke-width="5"/>',
        C(528, 156, 24, WBLUE, 0.6), C(532, 150, 6, WHITE, 0.9),
        C(576, 112, 18, WBLUE, 0.6), C(579, 107, 5, WHITE, 0.9),
        C(616, 78, 12, WBLUE, 0.6), C(618, 74, 3.5, WHITE, 0.9),
        C(500, 100, 10, WBLUE, 0.55),
        _dash("M 486 176 Q 502 166 516 168", TEAL, 4),
        _dash("M 470 150 Q 482 142 494 144", "#7cc8bb", 4))

    # 筝：天上菱形风筝长尾，线握在手中
    a["筝"] = wrap(
        ground(340, 446, 260, 24),
        cloud_p(560, 190, 0.5, WHITE),
        cloud_p(214, 120, 0.45, WHITE),
        PG([(470, 22), (562, 112), (470, 202), (378, 112)], RED),
        PG([(470, 62), (524, 112), (470, 162), (416, 112)], YEL),
        L(470, 22, 470, 202, "#c9cdd1", 3), L(378, 112, 562, 112, "#c9cdd1", 3),
        P("M 470 202 Q 506 238 480 274 Q 454 310 492 340", stroke=RED, w=5),
        _bow(497, 252, TEAL), _bow(470, 314, YEL_D),
        P("M 470 200 Q 448 260 404 296", stroke=INK, w=3.5),
        kid(x=330, y=430, s=1.0, pose="stand", shirt=GREEN, arms="point",
            point_at=(404, 296), look=(0.7, -0.5), face="open"),
        C(404, 296, 13, SKIN))

    # 积：积木一块块叠高，最上一块正落下
    a["积"] = wrap(
        ground(380, 446, 250, 24),
        R(306, 396, 148, 48, 9, TEAL),
        R(314, 348, 132, 48, 9, RED),
        R(306, 300, 148, 48, 9, YEL),
        R(318, 252, 124, 48, 9, BLUE),
        R(324, 204, 112, 48, 9, GREEN),
        R(330, 148, 100, 48, 9, "#f0876f"),
        R(320, 406, 40, 10, 5, WHITE, 0.6), R(328, 358, 36, 10, 5, WHITE, 0.6),
        R(320, 310, 40, 10, 5, WHITE, 0.6), R(330, 262, 34, 10, 5, WHITE, 0.6),
        R(336, 214, 30, 10, 5, WHITE, 0.6),
        _dash("M 380 138 L 380 120", "#f0876f", 5, "5 9"),
        _dash("M 404 142 L 414 128", "#f0876f", 5, "5 9"))

    # 曲：音符从琴键上飘出（区别 legacy 音=单个大音符）
    a["曲"] = wrap(
        ground(380, 446, 250, 22),
        _rot(250, 402, -7, wrap(
            R(118, 376, 250, 46, 9, "#8a5a33"),
            R(126, 382, 234, 28, 4, WHITE),
            _black_keys(140, 382, [2, 3, 2, 3], kw=9, kh=15))),
        P("M 236 344 Q 252 322 276 316", stroke=TEAL, w=6),
        P("M 282 322 Q 296 300 320 294", stroke=TEAL, w=6),
        _note(368, 296, 1.0, "#e8663c", -14),
        _note(452, 226, 1.15, "#4fae9f", 8),
        _note(540, 156, 1.3, "#f2b53c", -10))

    # 锣：锣挂在木架上，小孩举槌敲锣边（槌不碰脸，区别 鼓=物件+双槌）
    a["锣"] = wrap(
        ground(430, 446, 310, 24),
        kid(x=330, y=430, s=1.0, pose="stand", shirt=BLUE, arms="up",
            face="open", look=(0.5, 0.1)),
        R(470, 200, 14, 246, 7, WOOD_D),
        R(614, 200, 14, 246, 7, WOOD_D),
        R(452, 192, 194, 18, 8, WOOD),
        L(549, 210, 549, 246, INK, 3),
        C(549, 308, 62, YEL),
        f'<circle cx="549" cy="308" r="62" fill="none" stroke="{YEL_D}" stroke-width="8"/>',
        C(549, 308, 16, YEL_D, 0.7),
        L(414, 206, 490, 258, WOOD, 11),
        C(498, 264, 15, WOOD_L),
        _dash("M 478 236 Q 466 224 450 220", TEAL, 5),
        P("M 636 268 Q 660 308 636 348", stroke=TEAL, w=6),
        P("M 664 250 Q 698 308 664 366", stroke="#7cc8bb", w=6))

    # 牌：手里扇形三张牌（桃心/星星/花 为符号），加色边框避免白牌融进米色底
    a["牌"] = wrap(
        ground(430, 446, 210, 24),
        _rot(380, 452, -22, wrap(
            R(238, 258, 134, 190, 14, RED),
            R(246, 268, 118, 170, 12, WHITE),
            R(256, 278, 98, 150, 8, "#fbf6ea"),
            heart(305, 348, 25, RED))),
        _rot(380, 452, 22, wrap(
            R(488, 258, 134, 190, 14, "#4fae9f"),
            R(496, 268, 118, 170, 12, WHITE),
            R(506, 278, 98, 150, 8, "#fbf6ea"),
            flower5(555, 348, 26, "#f0876f", SUN))),
        R(314, 254, 132, 182, 14, "#f2b53c"),
        R(322, 262, 116, 168, 12, WHITE),
        R(332, 272, 96, 148, 8, WHITE),
        star5(380, 340, 29, SUN),
        hand(380, 408, s=0.62))

    # 琵：怀抱琵琶拨弦（琴斜抱胸前、琴头在头侧上方，脸全露；区别 琶=琵琶特写）
    a["琵"] = wrap(
        ground(380, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=TEAL, face="smile",
            look=(0, 0.2)),
        f'<g transform="rotate(-18 380 330) translate(-50,40)">'
        + P("M 380 204 Q 342 204 332 244 Q 324 278 350 308 Q 368 328 380 328 "
            "Q 392 328 410 308 Q 436 278 428 244 Q 418 204 380 204 Z", RED)
        + R(372, 152, 16, 56, 6, WOOD_D)
        + R(360, 130, 40, 28, 9, WOOD_D)
        + C(368, 136, 5, YEL) + C(382, 136, 5, YEL) + C(394, 136, 5, YEL)
        + L(374, 168, 372, 300, "#e8e4da", 2) + L(380, 168, 380, 302, "#e8e4da", 2)
        + L(386, 168, 388, 300, "#e8e4da", 2)
        + R(366, 298, 28, 9, 4, INK)
        + C(368, 220, 13, SKIN)
        + C(398, 292, 14, SKIN)
        + _dash("M 404 300 Q 418 306 430 302", TEAL, 4)
        + "</g>")

    # 琶：琵琶特写+拨弦的手（区别 琵=怀抱人）
    a["琶"] = wrap(
        ground(380, 446, 250, 24),
        R(368, 96, 24, 84, 8, WOOD_D),
        R(350, 66, 60, 36, 10, WOOD),
        C(362, 76, 6, YEL), C(380, 72, 6, YEL), C(398, 76, 6, YEL),
        L(372, 120, 372, 132, "#8a5a33", 3), L(388, 120, 388, 132, "#8a5a33", 3),
        P("M 380 168 Q 318 172 304 232 Q 292 296 336 350 Q 362 378 380 378 "
          "Q 398 378 424 350 Q 468 296 456 232 Q 442 172 380 168 Z", WOOD),
        L(348, 210, 412, 210, "#8a5a33", 3), L(342, 240, 418, 240, "#8a5a33", 3),
        L(338, 272, 422, 272, "#8a5a33", 3),
        L(370, 128, 368, 336, "#e8e4da", 2.5), L(380, 128, 380, 338, "#e8e4da", 2.5),
        L(390, 128, 392, 336, "#e8e4da", 2.5),
        R(354, 332, 52, 11, 4, INK),
        hand(516, 300, rot=-104, s=0.88),
        _dash("M 470 320 Q 452 328 438 324", TEAL, 4),
        _note(600, 200, 0.6, "#e8663c", -12), _note(646, 150, 0.5, "#4fae9f", 10))

    return a


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    cards = GROUP_CARDS
    assert [c["char"] for c in cards] == list(W_CHARS), "字序与清单不一致（号属 shuzi 组，不在本组）"
    amap = arts()
    assert list(amap.keys()) == list(W_CHARS), "arts key 与清单不一致"
    tone_marks = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    for c in cards:
        k = c["char"]
        assert k in c["sentence"], f"{k}: sentence 未含目标字"
        body = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        assert 4 <= body <= 10, f"{k}: sentence 长度 {body}"
        for fld in ("say", "chat", "life"):
            assert len(c[fld]) <= 30, f"{k}: {fld} 超长({len(c[fld])})"
            assert c[fld], f"{k}: 缺 {fld}"
        assert any(m in c["pinyin"] for m in tone_marks), f"{k}: 拼音缺调号"
        v = amap[k]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">{v}</svg>')
        low = v.lower()
        assert not any(t in low for t in ("<text", "<use", "<defs", "<image", "href")), k
    print(f"wenti 自检通过：{len(cards)} 卡，SVG 全部合法")
