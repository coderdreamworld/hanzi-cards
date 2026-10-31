#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1000字卡集 动作·手部 新增卡（a 部分）：拎扛掀按压捏摸撕拖叠折系解换捉抓捧捡投抛传拧扔接递贴修扶握追逃赶转摇摆收泼洒（38卡）。

插画只用 素材库 组件（kid/hand/table/box/lid/bowl/drop/star5/flower5...），
viewBox 0 0 760 480 内部标记；人物一律 kid()，手部特写一律 hand()。
"""
import sys
from pathlib import Path
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa

A_CHARS = "拎扛掀按压捏摸撕拖叠折系解换捉抓捧捡投抛传拧扔接递贴修扶握追逃赶转摇摆收泼洒"


# ---------- 本文件小工具 ----------
def _dash(d, color, w, gap="4 9"):
    """虚线动效弧。"""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-dasharray="{gap}"/>')


def _rot(x, y, ang, inner):
    return f'<g transform="rotate({ang} {x} {y})">{inner}</g>'


def _waves(cx, cy, rs, color, w=7):
    """朝右开口的声波弧。"""
    return "".join(P(f"M {cx} {cy-r} Q {cx+r*0.82} {cy} {cx} {cy+r}", stroke=color, w=w) for r in rs)


def _steam(cx, cy, s=1.0, color="#efe8da"):
    return P(f"M {cx} {cy} Q {cx-10*s} {cy-16*s} {cx} {cy-32*s} Q {cx+10*s} {cy-46*s} {cx-2*s} {cy-60*s}",
             stroke=color, w=7 * s)


def _bucket(cx, top, w, h, main, dark):
    return wrap(
        E(cx, top + 5, w * 0.42, 7, WBLUE),
        R(cx - w / 2, top, w, h, 9, main),
        R(cx - w / 2, top, w, 12, 6, dark),
        R(cx - w / 2, top + h - 10, w, 10, 5, dark))


def _tee(cx, top, main, dark):
    """挂着的小衣服。"""
    return wrap(
        P(f"M {cx-34} {top} L {cx+34} {top} L {cx+48} {top+20} L {cx+30} {top+32} "
          f"L {cx+30} {top+136} Q {cx} {top+150} {cx-30} {top+148} L {cx-30} {top+32} "
          f"L {cx-48} {top+20} Z", main),
        E(cx, top + 4, 13, 6, dark))


GROUP_CARDS = [
    {"char": "拎", "pinyin": "līn", "tone": "第一声",
     "sentence": "拎起小水桶。", "say": "手指勾住提手，往上一提就是拎。",
     "chat": "这一小桶水，你拎得动吗？", "life": "出门时让他拎自己的小水壶。"},
    {"char": "扛", "pinyin": "káng", "tone": "第二声",
     "sentence": "扛着小木棍出发啦。", "say": "长东西放在肩膀上扛着走。",
     "chat": "家里什么长长的东西能扛？", "life": "把长枕头放肩上试一试扛。"},
    {"char": "掀", "pinyin": "xiān", "tone": "第一声",
     "sentence": "掀开小被子看一看。", "say": "把盖着的一角掀起来就是掀。",
     "chat": "掀开看看，下面藏着什么呀？", "life": "玩掀手帕，猜下面的小玩具。"},
    {"char": "按", "pinyin": "àn", "tone": "第四声",
     "sentence": "轻轻按门铃。", "say": "手指往下压一下就是按。",
     "chat": "按门铃要轻轻按还是重重按？", "life": "到门口请他自己按一按门铃。"},
    {"char": "压", "pinyin": "yā", "tone": "第一声",
     "sentence": "把面团压扁。", "say": "手掌用力往下压，面团变扁啦。",
     "chat": "压一压，面团像什么呀？", "life": "玩橡皮泥，用手掌压一压。"},
    {"char": "捏", "pinyin": "niē", "tone": "第一声",
     "sentence": "捏一只小泥鸭。", "say": "指尖捏一捏，泥巴变成小鸭子。",
     "chat": "捏泥巴的时候用哪两根手指？", "life": "给他橡皮泥，捏个小丸子。"},
    {"char": "摸", "pinyin": "mō", "tone": "第一声",
     "sentence": "轻轻摸小兔。", "say": "手背轻轻碰一碰就是摸。",
     "chat": "小兔的毛摸起来什么感觉？", "life": "轻轻摸摸小猫的小脑袋。"},
    {"char": "撕", "pinyin": "sī", "tone": "第一声",
     "sentence": "把纸撕成两半。", "say": "两手往两边拉，刺啦撕开了。",
     "chat": "哪些纸可以撕着玩一玩？", "life": "给他废纸，撕成小纸条。"},
    {"char": "拖", "pinyin": "tuō", "tone": "第一声",
     "sentence": "帮妈妈拖地板。", "say": "拖把来回推，地板亮晶晶。",
     "chat": "拖完的地板走路要小心什么？", "life": "给他小拖把，拖拖自己房间。"},
    {"char": "叠", "pinyin": "dié", "tone": "第二声",
     "sentence": "把衣服叠一叠。", "say": "一件压一件，叠得整整齐齐。",
     "chat": "你的小衣服想跟谁学叠？", "life": "先叠袜子给他看，请他学。"},
    {"char": "折", "pinyin": "zhé", "tone": "第二声",
     "sentence": "折一张小纸飞机。", "say": "对折再对折，纸就变了样。",
     "chat": "折好的纸飞机想飞给谁看？", "life": "一起折纸飞机，比比谁飞得远。"},
    {"char": "系", "pinyin": "jì", "tone": "第四声（另读 xì，如“关系”）",
     "sentence": "系好小鞋带。", "say": "鞋带打个蝴蝶结就是系。",
     "chat": "你的鞋子是谁帮你系的呀？", "life": "教他给大鞋带打个结试试。"},
    {"char": "解", "pinyin": "jiě", "tone": "第三声",
     "sentence": "解开蝴蝶结。", "say": "轻轻一拉绳子头，结就解开了。",
     "chat": "礼物上的结怎么解开呀？", "life": "让他自己解开小书包的扣子。"},
    {"char": "换", "pinyin": "huàn", "tone": "第四声",
     "sentence": "给玩具换电池。", "say": "旧的拿出来，新的放进去是换。",
     "chat": "玩具没电了要怎么办呀？", "life": "回家换拖鞋，请他自己换好。"},
    {"char": "捉", "pinyin": "zhuō", "tone": "第一声",
     "sentence": "捉住花蝴蝶。", "say": "网子轻轻一罩，捉住啦。",
     "chat": "捉到的蝴蝶要不要放走呀？", "life": "吹泡泡给他，追着捉泡泡。"},
    {"char": "抓", "pinyin": "zhuā", "tone": "第一声",
     "sentence": "一把抓住小气球。", "say": "五根手指一合拢，抓住啦。",
     "chat": "抓气球要抓绳子的哪里呀？", "life": "抛小沙包给他，一把抓住。"},
    {"char": "捧", "pinyin": "pěng", "tone": "第三声",
     "sentence": "双手捧着小鸭子。", "say": "两只手心向上，稳稳捧着。",
     "chat": "捧小鸭子要轻轻的还是重重的？", "life": "请他双手捧个小橘子给你。"},
    {"char": "捡", "pinyin": "jiǎn", "tone": "第三声",
     "sentence": "把玩具捡起来。", "say": "蹲下来拾起地上的东西是捡。",
     "chat": "玩具掉地上了该怎么办呀？", "life": "玩捡球游戏，捡满一小筐。"},
    {"char": "投", "pinyin": "tóu", "tone": "第二声",
     "sentence": "把球投进篮筐。", "say": "瞄准篮筐，把球扔进去是投。",
     "chat": "投球的时候眼睛要看哪里？", "life": "拿袜子团投纸箱，比比谁准。"},
    {"char": "抛", "pinyin": "pāo", "tone": "第一声",
     "sentence": "把球抛得高高的。", "say": "手往上一丢，球飞上天是抛。",
     "chat": "球抛上去以后会怎么样呀？", "life": "抛气球给他，看谁抛得高。"},
    {"char": "传", "pinyin": "chuán", "tone": "第二声",
     "sentence": "把皮球传给我。", "say": "你扔给我，我扔给你，传来传去。",
     "chat": "和小朋友玩球，怎么传给他？", "life": "面对面坐好，玩滚球传球。"},
    {"char": "拧", "pinyin": "nǐng", "tone": "第三声",
     "sentence": "把毛巾拧干。", "say": "两手反着转一转，水就出来啦。",
     "chat": "湿毛巾怎么才能变干呀？", "life": "洗完手帮他拧干小毛巾。"},
    {"char": "扔", "pinyin": "rēng", "tone": "第一声",
     "sentence": "垃圾扔进纸篓里。", "say": "松开手丢出去就是扔。",
     "chat": "香蕉皮应该扔到哪里去呀？", "life": "把废纸团成球，扔进纸篓。"},
    {"char": "接", "pinyin": "jiē", "tone": "第一声",
     "sentence": "稳稳接住大皮球。", "say": "球飞过来，用手接住是接。",
     "chat": "接球的时候眼睛看哪里呀？", "life": "轻轻滚球给他，练习接住。"},
    {"char": "递", "pinyin": "dì", "tone": "第四声",
     "sentence": "把苹果递给妈妈。", "say": "把东西送到别人手里是递。",
     "chat": "你想把苹果递给谁吃呀？", "life": "吃饭时请他递一双筷子。"},
    {"char": "贴", "pinyin": "tiē", "tone": "第一声",
     "sentence": "把星星贴上墙。", "say": "按平粘住不掉下来就是贴。",
     "chat": "这颗星星贴在谁的旁边呀？", "life": "给他贴纸，贴到画册上去。"},
    {"char": "修", "pinyin": "xiū", "tone": "第一声",
     "sentence": "修好小玩具车。", "say": "用工具把坏的弄好就是修。",
     "chat": "玩具车的轮子坏了怎么办？", "life": "给他小螺丝刀拧一拧玩具。"},
    {"char": "扶", "pinyin": "fú", "tone": "第二声",
     "sentence": "扶老奶奶慢慢走。", "say": "用手搀住别人帮她站稳是扶。",
     "chat": "看到老爷爷走路慢怎么办呀？", "life": "过马路时紧紧扶好大人的手。"},
    {"char": "握", "pinyin": "wò", "tone": "第四声",
     "sentence": "握握手，好朋友。", "say": "两只手握在一起，问声好。",
     "chat": "见到新朋友要怎么说呀？", "life": "见到小伙伴，握握手问个好。"},
    {"char": "追", "pinyin": "zhuī", "tone": "第一声",
     "sentence": "追着皮球跑。", "say": "快快跑着赶上它就是追。",
     "chat": "皮球滚远了要怎么办呀？", "life": "在草地上追着泡泡跑一跑。"},
    {"char": "逃", "pinyin": "táo", "tone": "第二声",
     "sentence": "小狗追，快快逃。", "say": "跑开躲开不追了就是逃。",
     "chat": "玩老鹰捉小鸡谁要逃呀？", "life": "玩追跑游戏，喊开始就逃开。"},
    {"char": "赶", "pinyin": "gǎn", "tone": "第三声",
     "sentence": "赶着小鸭回家去。", "say": "跟在后面让它往前走是赶。",
     "chat": "小鸭子被赶到哪里去呀？", "life": "推着小球走，玩赶小猪游戏。"},
    {"char": "转", "pinyin": "zhuàn", "tone": "第四声（另读 zhuǎn，如“转弯”）",
     "sentence": "转个圈圈真好玩。", "say": "原地画圈圈，转呀转呀转。",
     "chat": "转完圈圈停下来什么感觉呀？", "life": "张开手臂，原地慢慢转三圈。"},
    {"char": "摇", "pinyin": "yáo", "tone": "第二声",
     "sentence": "摇一摇拨浪鼓。", "say": "拿在手里晃来晃去就是摇。",
     "chat": "拨浪鼓摇起来是什么声音？", "life": "小瓶装豆子，摇一摇听声音。"},
    {"char": "摆", "pinyin": "bǎi", "tone": "第三声",
     "sentence": "把鞋子摆整齐。", "say": "一样一样排好队就是摆。",
     "chat": "你的小鞋子怎么摆才整齐？", "life": "回家把鞋子在门口摆一排。"},
    {"char": "收", "pinyin": "shōu", "tone": "第一声",
     "sentence": "把衣服收回来。", "say": "把晾好的衣服拿回家是收。",
     "chat": "下雨了晒的衣服怎么办呀？", "life": "帮他取下晾干的小袜子。"},
    {"char": "泼", "pinyin": "pō", "tone": "第一声",
     "sentence": "泼水花，哗啦啦。", "say": "把水用力扬出去就是泼。",
     "chat": "泼出去的水花像什么呀？", "life": "洗澡时轻轻泼小水花玩。"},
    {"char": "洒", "pinyin": "sǎ", "tone": "第三声",
     "sentence": "把水洒向小花。", "say": "细细的水点落下来是洒。",
     "chat": "小水点都洒到哪里去了呀？", "life": "用小喷壶给花洒洒水。"},
]


def arts():
    a = {}

    # 拎：右手拎红桶，桶明显离地、滴水落小水洼（legacy 提=青桶静止）
    a["拎"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, arms="down",
            face="smile", look=(0.4, 0.1)),
        P("M 414 368 Q 444 316 474 368", stroke="#8a5a33", w=7),
        _bucket(444, 364, 88, 46, RED, RED_D),
        drop(460, 424, 7), drop(474, 440, 6),
        E(478, 450, 24, 5, WBLUE, 0.5))

    # 扛：木棍斜扛右肩，右手上举握棍，棍端挂小包袱
    a["扛"] = wrap(
        ground(380, 446, 250, 24),
        C(252, 258, 26, RED_D), C(249, 255, 24, RED), C(243, 249, 7, "#f5a58c", 0.9),
        _rot(400, 240, -20, R(250, 229, 300, 22, 11, WOOD)),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=RED, face="smile",
            arms="point", point_at=(520, 196)),
        R(336, 268, 88, 20, 9, SKIN_D, 0.35))

    # 掀：掀开毯子一角，露出红色皮球
    a["掀"] = wrap(
        ground(420, 446, 270, 24),
        R(452, 384, 224, 48, 16, TEAL_L),
        L(470, 408, 658, 408, TEAL, 4),
        C(508, 406, 30, RED_D), C(505, 403, 28, RED), C(494, 392, 7, "#f5a58c", 0.9),
        kid(x=370, y=430, s=0.95, pose="stand", shirt=TEAL, face="o",
            arms="reach", flip=-1, look=(0.6, 0.2)),
        P("M 430 434 Q 420 350 492 334 L 524 434 Z", TEAL),
        P("M 430 434 Q 420 350 492 334", stroke=TEAL_D, w=5))

    # 按：伸手按门板上的大按钮
    a["按"] = wrap(
        ground(420, 446, 260, 24),
        R(560, 116, 176, 292, 18, "#e9b97e"),
        R(572, 128, 152, 268, 14, "#f4d3a4"),
        C(525, 296, 62, WOOD_D),
        C(525, 296, 52, RED),
        C(510, 280, 11, WHITE, 0.8),
        _waves(640, 280, [20, 38], TEAL, 6),
        kid(x=360, y=430, s=1.0, pose="stand", shirt=BLUE, face="o",
            arms="point", point_at=(500, 288), look=(0.8, 0)))

    # 压：桌上大面团被手掌压扁
    a["压"] = wrap(
        ground(),
        table(380, 330, 272, 62),
        E(386, 316, 66, 36, "#e3cd9e"),
        E(380, 310, 64, 34, "#f7ecd2"),
        C(360, 302, 8, "#efe0bd"), C(402, 306, 6, "#efe0bd"),
        _dash("M 296 250 Q 282 276 298 300", TEAL, 5),
        _dash("M 466 250 Q 480 276 464 300", TEAL, 5),
        hand(380, 152, rot=180, s=1.05))

    # 捏：坐在小桌前捏黄色泥鸭，两只手指尖捏在鸭身两侧，旁边还有小泥团
    a["捏"] = wrap(
        ground(380, 450, 240, 22),
        kid(x=380, y=470, s=1.0, pose="sit", shirt=YEL, face="o", arms="clap"),
        table(380, 372, 240, 58),
        E(378, 352, 38, 21, "#f2b53c"),
        C(352, 324, 16, "#f2b53c"),
        E(332, 328, 9, 5, "#e8663c"),
        C(348, 320, 4, INK), C(349, 319, 1.4, WHITE),
        E(396, 352, 14, 9, "#d99a2b"),
        C(366, 348, 13, "#e8a97e"), C(366, 348, 11, SKIN),
        C(394, 348, 13, "#e8a97e"), C(394, 348, 11, SKIN),
        C(442, 364, 9, "#f2b53c"), C(458, 368, 6, "#f2b53c"))

    # 摸：手轻轻碰小兔的头
    a["摸"] = wrap(
        ground(400, 446, 250, 24),
        E(475, 398, 52, 42, WHITE),
        E(468, 402, 44, 34, "#f4f1e8"),
        _rot(446, 272, -10, R(436, 236, 20, 74, 10, WHITE)),
        _rot(486, 268, 8, R(476, 230, 20, 78, 10, WHITE)),
        _rot(446, 274, -10, E(446, 272, 7, 26, PINK, 0.75)),
        _rot(486, 270, 8, E(486, 268, 7, 28, PINK, 0.75)),
        C(462, 332, 34, WHITE),
        E(462, 342, 6, 4, PINK),
        C(452, 326, 5, INK), C(474, 326, 5, INK),
        C(450, 320, 1.6, WHITE), C(472, 320, 1.6, WHITE),
        C(444, 344, 7, PINK, 0.7), C(482, 344, 7, PINK, 0.7),
        hand(330, 322, rot=78, s=0.95))

    # 撕：两只手把白纸撕成两半
    a["撕"] = wrap(
        ground(380, 446, 250, 22),
        R(236, 244, 134, 184, 10, "#ece2cc"),
        P("M 240 240 L 362 240 L 348 272 L 366 302 L 346 332 L 364 362 L 348 392 L 364 420 L 240 420 Z", WHITE),
        R(392, 244, 134, 184, 10, "#ece2cc"),
        P("M 520 240 L 398 240 L 412 272 L 394 302 L 414 332 L 396 362 L 412 392 L 398 420 L 520 420 Z", WHITE),
        _dash("M 380 222 Q 392 208 406 222", TEAL, 5),
        _dash("M 380 438 Q 392 452 406 438", TEAL, 5),
        hand(226, 330, rot=90),
        hand(534, 330, rot=-90))

    # 拖：边走边拖地，拖把+水痕
    a["拖"] = wrap(
        ground(),
        E(258, 440, 84, 10, WBLUE, 0.5),
        E(186, 446, 48, 7, WBLUE, 0.35),
        kid(x=320, y=430, s=1.0, pose="walk", shirt=GREEN, face="smile",
            arms="point", point_at=(450, 240)),
        L(345, 392, 468, 208, WOOD, 11),
        E(330, 404, 56, 20, YEL_D),
        L(306, 430, 318, 440, YEL, 6), L(320, 432, 330, 442, YEL, 6),
        L(336, 432, 344, 442, YEL, 6), L(352, 430, 358, 440, YEL, 6),
        L(330, 398, 348, 416, "#f9c95e", 5),
        _dash("M 392 300 Q 408 286 428 288", TEAL, 5))

    # 叠：桌上叠好的衣摞 + 正在抚平的一件
    a["叠"] = wrap(
        ground(),
        table(390, 336, 250, 70),
        R(300, 314, 110, 22, 10, BLUE),
        R(303, 292, 104, 22, 10, RED),
        R(306, 270, 98, 22, 10, YEL),
        R(430, 306, 110, 30, 10, TEAL),
        L(436, 321, 534, 321, "#3e9486", 4),
        kid(x=560, y=430, s=0.95, pose="stand", shirt=WBLUE, face="smile",
            arms="point", point_at=(500, 300), look=(-0.5, 0.1)))

    # 折：桌上白纸对折，右半边向上折起，手压住左半边
    a["折"] = wrap(
        ground(420, 446, 250, 24),
        kid(x=330, y=430, s=1.0, pose="stand", shirt=RED, face="o",
            arms="point", point_at=(452, 320)),
        table(505, 330, 224, 62),
        PG([(425, 354), (425, 314), (512, 314), (512, 354)], WHITE),
        _rot(512, 334, -38, R(512, 314, 92, 40, 6, "#ece2cc")),
        L(512, 312, 512, 356, "#c9bfa8", 4))

    # 系：红色小球鞋 + 蝴蝶结，两只手在系
    a["系"] = wrap(
        ground(395, 446, 250, 22),
        R(268, 390, 254, 46, 22, WHITE),
        P("M 298 392 Q 296 306 356 296 L 420 296 Q 468 302 492 348 L 520 392 Z", RED),
        E(322, 366, 42, 26, WHITE),
        E(438, 302, 30, 13, RED_D),
        P("M 356 300 L 424 300 L 444 344 L 372 350 Z", "#d4552f"),
        L(368, 308, 430, 326, WHITE, 7), L(430, 308, 368, 326, WHITE, 7),
        L(376, 330, 434, 344, WHITE, 6), L(434, 330, 376, 344, WHITE, 6),
        _rot(448, 292, -32, E(448, 292, 22, 12, WHITE)),
        _rot(494, 288, 26, E(494, 288, 22, 12, WHITE)),
        C(470, 296, 11, WHITE),
        L(478, 304, 500, 344, WHITE, 7),
        hand(230, 352, rot=100), hand(580, 312, rot=-95))

    # 解：拉开礼物盒的丝带
    a["解"] = wrap(
        ground(380, 446, 240, 22),
        P("M 396 300 Q 468 272 516 254", stroke=RED, w=9),
        R(300, 326, 180, 112, 14, YEL),
        R(312, 338, 156, 88, 10, "#f9c95e"),
        R(290, 300, 200, 36, 12, YEL_D),
        R(376, 300, 26, 138, 6, RED),
        _rot(346, 290, -25, E(346, 290, 24, 13, RED)),
        C(384, 296, 11, RED_D),
        _dash("M 508 236 Q 522 222 538 226", TEAL, 5),
        hand(218, 382, rot=75), hand(585, 225, rot=-114))

    # 换：给玩具机器人换电池
    a["换"] = wrap(
        ground(420, 446, 250, 24),
        kid(x=320, y=430, s=1.0, pose="stand", shirt=GREEN, face="o",
            arms="point", point_at=(430, 365)),
        R(560, 412, 34, 20, 6, "#cfe6f0"),
        _rot(577, 422, 12, R(560, 412, 34, 20, 6, "#cfe6f0")),
        R(460, 414, 80, 16, 6, "#7fa9c4"),
        R(450, 330, 100, 86, 14, "#9cc9e2"),
        R(462, 268, 76, 54, 12, "#9cc9e2"),
        L(500, 268, 500, 242, "#7fa9c4", 5), C(500, 234, 8, RED),
        C(482, 292, 7, INK), C(518, 292, 7, INK),
        C(484, 290, 2, WHITE), C(520, 290, 2, WHITE),
        R(444, 344, 12, 36, 4, INK, 0.5),
        _rot(416, 342, 34, wrap(R(398, 330, 36, 22, 6, YEL), R(432, 336, 8, 10, 3, "#c9cdd1"))))

    # 捉：跑动中用网罩住蝴蝶
    a["捉"] = wrap(
        ground(400, 446, 260, 24),
        _dash("M 226 300 Q 246 320 240 350", TEAL, 5),
        _dash("M 204 320 Q 220 340 214 366", TEAL, 4),
        kid(x=330, y=430, s=1.0, pose="sprint", shirt=BLUE, face="open",
            arms="up", look=(0.5, 0)),
        L(424, 198, 498, 250, WOOD, 9),
        P("M 502 302 Q 530 356 558 302", stroke="#dfe3e6", w=5),
        E(518, 288, 13, 18, PINK), E(542, 288, 13, 18, PINK),
        E(530, 292, 5, 13, INK),
        L(526, 280, 520, 268, INK, 2.5), L(534, 280, 540, 268, INK, 2.5),
        f'<circle cx="530" cy="272" r="46" fill="none" stroke="#8a5a33" stroke-width="8"/>')

    # 抓：跳起抓住气球绳，绳从拳头中穿过、拳下还留一小段绳头
    a["抓"] = wrap(
        ground(380, 446, 230, 22),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, face="open",
            arms="up", look=(0.3, -0.4)),
        C(492, 106, 44, RED_D), C(489, 103, 42, RED), C(476, 90, 10, "#f5a58c", 0.9),
        PG([(484, 148), (500, 148), (492, 162)], RED_D),
        P("M 492 162 Q 476 180 464 198", stroke=INK, w=3.5),
        P("M 464 198 Q 458 212 464 226", stroke=INK, w=3.5),
        C(464, 198, 9, SKIN_D))

    # 捧：双手捧着小鸭子
    a["捧"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=YEL, face="smile",
            arms="clap", look=(0, 0.3)),
        E(380, 272, 30, 24, "#f2b53c"),
        C(380, 240, 19, "#f2b53c"),
        E(401, 242, 9, 5, "#e8663c"),
        C(374, 236, 4, INK), C(375, 235, 1.4, WHITE),
        E(370, 272, 12, 9, "#d99a2b"))

    # 捡：弯身伸手朝地上的皮球，球沿弧线刚被拾起，旁边散着玩具和小筐
    a["捡"] = wrap(
        ground(390, 446, 260, 24),
        ball(468, 420, 22, RED, RED_D, "#f5a58c"),
        R(540, 420, 28, 18, 5, YEL), R(576, 426, 24, 13, 5, TEAL),
        P("M 598 398 Q 642 444 686 398 Z", WOOD_L),
        L(598, 398, 686, 398, WOOD_D, 6),
        C(642, 410, 10, RED_D),
        kid(x=330, y=430, s=1.0, pose="stand", shirt=BLUE, face="smile",
            arms="point", point_at=(452, 380), look=(0.8, 0.3)),
        _dash("M 452 402 Q 428 388 426 356", TEAL, 5))

    # 投：瞄准篮筐投球
    a["投"] = wrap(
        ground(430, 446, 260, 24),
        kid(x=290, y=430, s=1.0, pose="stand", shirt=RED, face="open",
            arms="point", point_at=(505, 125), look=(0.7, -0.4)),
        R(556, 110, 22, 95, 8, WOOD_L),
        R(562, 205, 12, 235, 6, WOOD_D),
        f'<ellipse cx="522" cy="212" rx="38" ry="9" fill="none" stroke="{RED}" stroke-width="6"/>',
        L(504, 216, 512, 262, "#dfe3e6", 3), L(522, 218, 522, 264, "#dfe3e6", 3),
        L(540, 216, 532, 262, "#dfe3e6", 3),
        ball(472, 148, 30, RED, RED_D, "#f5a58c"),
        _dash("M 402 208 Q 428 158 452 152", TEAL, 5))

    # 抛：双手向上抛球
    a["抛"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=TEAL, face="open",
            arms="up", look=(0, -0.5)),
        ball(380, 108, 36, TEAL, TEAL_D, TEAL_L),
        _dash("M 318 192 Q 334 140 356 126", TEAL, 5),
        _dash("M 442 192 Q 426 140 404 126", TEAL, 5))

    # 传：两个小朋友传皮球
    a["传"] = wrap(
        ground(380, 446, 300, 24),
        kid(x=250, y=430, s=0.9, pose="stand", shirt=YEL, face="smile",
            arms="point", point_at=(390, 300), look=(0.6, 0)),
        kid(x=510, y=430, s=0.9, pose="stand", shirt=RED, face="open",
            arms="reach", look=(-0.5, 0)),
        ball(380, 290, 30, TEAL, TEAL_D, TEAL_L),
        _dash("M 296 236 Q 380 206 464 244", TEAL, 5))

    # 拧：两手反方向拧毛巾（中间拧成 V 形）
    a["拧"] = wrap(
        ground(380, 446, 240, 22),
        drop(372, 396, 10), drop(404, 408, 9), drop(346, 410, 8),
        E(388, 446, 62, 8, WBLUE, 0.4),
        _rot(322, 330, 13, wrap(R(240, 310, 156, 42, 18, WBLUE),
                                L(258, 322, 300, 344, TEAL_L, 8),
                                L(310, 320, 352, 342, TEAL_L, 8))),
        _rot(438, 330, -13, wrap(R(364, 310, 156, 42, 18, WBLUE),
                                 L(388, 322, 430, 344, TEAL_L, 8),
                                 L(440, 320, 482, 342, TEAL_L, 8))),
        hand(216, 322, rot=100), hand(544, 322, rot=-100))

    # 扔：废纸团扔进纸篓
    a["扔"] = wrap(
        ground(430, 446, 250, 24),
        kid(x=300, y=430, s=1.0, pose="stand", shirt=GREEN, face="open",
            arms="point", point_at=(452, 280), look=(0.6, -0.2)),
        C(462, 262, 21, WHITE), P("M 452 254 Q 462 248 470 256", stroke="#d9d0c5", w=3),
        P("M 456 272 Q 468 266 474 272", stroke="#d9d0c5", w=3),
        R(470, 324, 110, 18, 9, "#5f8f52"),
        R(478, 336, 94, 92, 14, "#7fae70"),
        R(492, 344, 66, 12, 6, "#4a6b4a"),
        _dash("M 408 250 Q 434 250 450 260", TEAL, 5))

    # 接：双臂前伸，大皮球正落到两只手上，虚线示球飞来的轨迹
    a["接"] = wrap(
        ground(380, 446, 250, 24),
        kid(x=330, y=430, s=1.0, pose="stand", shirt=BLUE, face="open",
            arms="reach", flip=-1, look=(0.8, 0)),
        ball(470, 316, 27, RED, RED_D, "#f5a58c"),
        _dash("M 598 244 Q 542 256 494 296", TEAL, 5),
        _dash("M 602 298 Q 546 310 500 330", TEAL, 4))

    # 递：一只手把苹果递给另一只手
    a["递"] = wrap(
        ground(390, 446, 260, 24),
        C(385, 288, 41, RED_D), C(382, 285, 39, RED), C(368, 271, 9, "#f5a58c", 0.9),
        L(382, 246, 388, 230, "#5a3d2b", 5),
        E(396, 236, 13, 7, GREEN, 0.95),
        hand(282, 292, rot=100), hand(545, 322, rot=-85))

    # 贴：往展示板上贴星星
    a["贴"] = wrap(
        ground(430, 446, 250, 24),
        R(470, 200, 180, 220, 12, WOOD),
        R(482, 212, 156, 196, 8, WHITE),
        star5(560, 280, 30, SUN),
        kid(x=300, y=430, s=1.0, pose="stand", shirt=TEAL, face="smile",
            arms="point", point_at=(560, 300), look=(0.8, 0.1)),
        star5(452, 274, 27, SUN))

    # 修：坐地拿扳手修翻倒的玩具车
    a["修"] = wrap(
        ground(420, 446, 250, 24),
        kid(x=330, y=445, s=1.0, pose="sit", shirt=YEL, face="o", arms="point",
            point_at=(455, 345)),
        R(460, 396, 130, 40, 12, WBLUE),
        C(485, 388, 17, INK), C(485, 388, 7, "#c9cdd1"),
        C(560, 388, 17, INK), C(560, 388, 7, "#c9cdd1"),
        R(480, 404, 40, 18, 6, "#cfe6f0"),
        _rot(455, 340, 26, wrap(R(400, 332, 112, 16, 8, "#aab3ba"),
                                C(516, 340, 15, "#aab3ba"),
                                R(506, 322, 20, 14, 5, PAGE))))

    # 扶：小朋友双手扶住拿拐杖的老奶奶的后腰帮她站稳（不再做成牵手）
    a["扶"] = wrap(
        ground(420, 446, 290, 24),
        _rot(555, 435, 5, wrap(
            kid(x=555, y=435, s=1.1, pose="stand", shirt="#f5a58c",
                hair_color="#d9d0c5", bun=True, glasses=True, skirt=True,
                arms="down", face="smile"),
            L(628, 330, 648, 452, WOOD, 10), C(648, 454, 11, WOOD_D))),
        kid(x=440, y=430, s=0.9, pose="stand", shirt=BLUE, face="smile",
            arms="reach", flip=-1, look=(0.6, 0.1)))

    # 握：两个小朋友握手
    a["握"] = wrap(
        ground(380, 446, 300, 24),
        kid(x=300, y=430, s=0.95, pose="stand", shirt=RED, face="smile",
            arms="point", point_at=(380, 335), look=(0.6, 0.2)),
        kid(x=460, y=430, s=0.95, pose="stand", shirt=TEAL, face="smile",
            flip=-1, arms="point", point_at=(540, 335), look=(0.6, 0.2)),
        C(382, 348, 16, SKIN), C(376, 342, 10, SKIN_D, 0.5))

    # 追：奔跑追皮球
    a["追"] = wrap(
        ground(420, 446, 270, 24),
        ball(560, 412, 34, RED, RED_D, "#f5a58c"),
        _dash("M 486 430 Q 500 436 514 430", TEAL, 5),
        _dash("M 250 300 Q 232 330 250 360", TEAL, 5),
        kid(x=330, y=430, s=1.05, pose="sprint", shirt=GREEN, face="open",
            arms="pump", look=(0.8, 0)))

    # 逃：小狗在后面追，小朋友往前逃
    a["逃"] = wrap(
        ground(400, 446, 280, 24),
        C(200, 392, 14, WOOD),
        E(246, 412, 56, 38, WOOD),
        E(238, 414, 42, 26, WOOD_L, 0.5),
        E(300, 380, 32, 27, WOOD),
        E(318, 366, 10, 18, WOOD_D), E(290, 364, 11, 20, WOOD_D),
        E(312, 378, 12, 9, "#e9b97e"), C(318, 382, 4, INK),
        C(296, 374, 5, INK), C(297, 373, 1.8, WHITE),
        E(322, 390, 7, 5, PINK),
        E(254, 388, 9, 6, PINK),
        L(216, 452, 214, 434, WOOD_D, 7), L(258, 452, 260, 434, WOOD_D, 7),
        L(292, 452, 290, 436, WOOD_D, 7),
        _waves(352, 392, [14, 28], TEAL, 5),
        _dash("M 396 366 Q 412 380 406 404", TEAL, 4),
        kid(x=470, y=430, s=1.0, pose="sprint", shirt=RED, face="o",
            arms="pump", look=(-0.7, -0.2)))

    # 赶：张开手臂赶小鸭
    a["赶"] = wrap(
        ground(420, 446, 280, 24),
        kid(x=300, y=430, s=1.0, pose="stride", shirt=WBLUE, face="smile",
            arms="swing", look=(0.7, 0)),
        E(540, 402, 58, 40, WHITE),
        C(586, 352, 30, WHITE),
        E(622, 356, 15, 8, "#e8663c"),
        C(592, 344, 6, INK), C(593, 343, 2, WHITE),
        E(528, 400, 25, 16, "#d9d0c5"),
        L(524, 440, 520, 452, "#e8a13c", 5), L(556, 440, 560, 452, "#e8a13c", 5))

    # 转：张臂转圈，裙摆飞扬
    a["转"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt="#f0876f", skirt=True,
            face="o", arms="up", look=(0, -0.3)),
        _dash("M 250 320 Q 228 260 268 208", TEAL, 5),
        _dash("M 510 320 Q 532 260 492 208", TEAL, 5),
        _dash("M 216 350 Q 190 300 200 250", "#f0876f", 5))

    # 摇：举着拨浪鼓摇
    a["摇"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, face="open",
            arms="up", look=(0.4, 0)),
        L(464, 198, 498, 238, WOOD, 10),
        C(522, 262, 36, RED),
        R(488, 256, 68, 12, 6, YEL),
        C(522, 262, 8, "#f9c95e"),
        L(520, 296, 496, 330, INK, 3), L(520, 296, 546, 330, INK, 3),
        C(494, 336, 9, YEL), C(548, 336, 9, YEL),
        _dash("M 452 246 Q 440 262 452 278", TEAL, 5),
        _dash("M 592 246 Q 604 262 592 278", TEAL, 5))

    # 摆：把鞋子一双双摆整齐
    def _shoe(cx, main, dark, ang=0.0, s=1.0):
        return _rot(cx, 415, ang, wrap(
            R(cx - 30 * s, 415, 60 * s, 15 * s, 7 * s, dark),
            P(f"M {cx-30*s} {417} Q {cx-32*s} {417-24*s} {cx-8*s} {417-28*s} "
              f"Q {cx+16*s} {417-30*s} {cx+30*s} {417} Z", main),
            C(cx - 4 * s, 399, 3.5 * s, WHITE)))

    a["摆"] = wrap(
        ground(430, 446, 290, 24),
        _shoe(272, RED, RED_D), _shoe(344, RED, RED_D),
        _shoe(428, TEAL, TEAL_D), _shoe(500, TEAL, TEAL_D),
        kid(x=605, y=430, s=0.9, pose="stand", shirt=GREEN, face="smile",
            arms="point", point_at=(545, 398), look=(-0.7, 0.3)),
        _rot(600, 340, -18, wrap(R(570, 336, 60, 15, 7, TEAL_D),
                                 P("M 570 338 Q 568 314 592 310 Q 616 308 630 338 Z", TEAL),
                                 C(596, 320, 3.5, WHITE))))

    # 收：踮脚把晾衣绳上的衣服收下来
    a["收"] = wrap(
        ground(390, 446, 280, 24),
        P("M 130 168 Q 390 192 650 168", stroke="#8a5a33", w=5),
        R(262, 172, 10, 13, 3, WOOD), R(280, 172, 10, 13, 3, WOOD),
        _rot(272, 254, -4, _tee(272, 180, RED, RED_D)),
        R(476, 172, 10, 13, 3, WOOD), R(494, 172, 10, 13, 3, WOOD),
        _tee(485, 180, TEAL, TEAL_D),
        P("M 560 392 Q 604 440 648 392 Z", WOOD_L),
        L(560, 392, 648, 392, WOOD_D, 6),
        R(582, 376, 44, 18, 8, YEL),
        kid(x=390, y=430, s=1.12, pose="stand", shirt=WBLUE, face="smile",
            arms="up", look=(-0.3, 0.3)))

    # 泼：端盆泼水，水花四溅
    a["泼"] = wrap(
        ground(430, 446, 280, 24),
        E(600, 438, 72, 12, WBLUE, 0.55),
        kid(x=290, y=430, s=1.0, pose="stand", shirt=YEL, face="open",
            arms="reach", flip=-1, look=(0.7, 0)),
        _rot(452, 342, -24, wrap(
            P("M 386 336 Q 452 382 518 336 Z", RED),
            E(452, 336, 66, 15, RED_D),
            E(452, 334, 56, 10, WBLUE))),
        P("M 508 318 Q 574 268 632 314", stroke=WBLUE, w=12),
        P("M 514 340 Q 592 318 644 366", stroke=WBLUE, w=9),
        drop(566, 286, 12), drop(614, 350, 11), drop(578, 240, 9), drop(646, 300, 8))

    # 洒：甩手把杯里的水向外扬出去，水点在空中散开，小花只沾到几滴
    a["洒"] = wrap(
        ground(440, 446, 250, 24),
        E(545, 440, 92, 13, GREEN_L),
        flower5(566, 426, 13),
        flower5(500, 430, 9, "#f2b53c"),
        kid(x=310, y=430, s=1.0, pose="stand", shirt=RED, face="smile",
            arms="point", point_at=(500, 250), look=(0.8, -0.2)),
        _rot(462, 276, 50, wrap(R(436, 256, 52, 40, 8, BLUE), E(462, 258, 20, 7, WBLUE))),
        drop(510, 240, 8), drop(540, 260, 9), drop(562, 290, 8), drop(576, 328, 7),
        drop(548, 318, 6), drop(590, 300, 7), drop(560, 384, 6), drop(534, 360, 6))

    return a


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    cards = GROUP_CARDS
    assert [c["char"] for c in cards] == list(A_CHARS), "字序与 B1 分配清单不一致"
    amap = arts()
    assert list(amap.keys()) == list(A_CHARS), "arts key 与清单不一致"
    tone_marks = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"
    for c in cards:
        k = c["char"]
        assert k in c["sentence"], f"{k}: sentence 未含目标字"
        body = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        assert 4 <= body <= 10, f"{k}: sentence 长度 {body}"
        for fld in ("say", "chat", "life"):
            assert len(c[fld]) <= 30, f"{k}: {fld} 超长"
            assert c[fld], f"{k}: 缺 {fld}"
        assert any(m in c["pinyin"] for m in tone_marks), f"{k}: 拼音缺调号"
        v = amap[k]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">{v}</svg>')
        low = v.lower()
        assert not any(t in low for t in ("<text", "<use", "<defs", "<image", "href")), k
    print(f"dongzuo4_a 自检通过：{len(cards)} 卡，SVG 全部合法")
