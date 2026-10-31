#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1000字卡集 动作·手部 新增卡（b 部分）：挑拔托切炒煮蒸尝咬嚼喊叫挤挥揉挠闻铺盖藏卖选抬理倒种堆补吸舔捆端竖抖逗靠搓（37卡）。

插画只用 素材库 组件（kid/hand/table/bowl/spoon/drop/flower5/tree_round...），
viewBox 0 0 760 480 内部标记；人物一律 kid()，手部特写一律 hand()。
"""
import sys
from pathlib import Path
sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa

B_CHARS = "挑拔托切炒煮蒸尝咬嚼喊叫挤挥揉挠闻铺盖藏卖选抬理倒种堆补吸舔捆端竖抖逗靠搓"


# ---------- 本文件小工具 ----------
def _dash(d, color, w, gap="4 9"):
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-dasharray="{gap}"/>')


def _rot(x, y, ang, inner):
    return f'<g transform="rotate({ang} {x} {y})">{inner}</g>'


def _waves(cx, cy, rs, color, w=7):
    return "".join(P(f"M {cx} {cy-r} Q {cx+r*0.82} {cy} {cx} {cy+r}", stroke=color, w=w) for r in rs)


def _steam(cx, cy, s=1.0, color="#efe8da"):
    return P(f"M {cx} {cy} Q {cx-10*s} {cy-16*s} {cx} {cy-32*s} Q {cx+10*s} {cy-46*s} {cx-2*s} {cy-60*s}",
             stroke=color, w=7 * s)


GROUP_CARDS = [
    {"char": "挑", "pinyin": "tiāo", "tone": "第一声（另读 tiǎo，如“挑战”）",
     "sentence": "挑着水桶回家。", "say": "扁担放肩上，两边挂桶是挑。",
     "chat": "两边的桶为什么一样重呀？", "life": "用小棍挑两个小篮子走走。"},
    {"char": "拔", "pinyin": "bá", "tone": "第二声",
     "sentence": "拔一个大萝卜。", "say": "攥紧了用力往上拔出来。",
     "chat": "萝卜的哪一半藏在土里呀？", "life": "玩拔萝卜，一起用力拉。"},
    {"char": "托", "pinyin": "tuō", "tone": "第一声",
     "sentence": "单手托着小蛋糕。", "say": "手心朝上稳稳接着是托。",
     "chat": "托蛋糕的手要平还是斜呀？", "life": "请他托本书走三步不掉。"},
    {"char": "切", "pinyin": "qiē", "tone": "第一声（另读 qiè，如“亲切”）",
     "sentence": "切苹果分两半。", "say": "刀轻轻往下压，苹果分两半。",
     "chat": "切开的苹果里面长什么样？", "life": "看妈妈切苹果，数切几块。"},
    {"char": "炒", "pinyin": "chǎo", "tone": "第三声",
     "sentence": "妈妈炒菜真香呀。", "say": "在锅里翻翻拌拌就是炒。",
     "chat": "你闻到炒菜的香味了吗？", "life": "玩过家家，用小铲子炒一炒。"},
    {"char": "煮", "pinyin": "zhǔ", "tone": "第三声",
     "sentence": "煮一锅香香的白粥。", "say": "锅里咕嘟咕嘟冒泡就是煮。",
     "chat": "煮粥的时候锅里什么声音？", "life": "看他煮饺子，数一数饺子。"},
    {"char": "蒸", "pinyin": "zhēng", "tone": "第一声",
     "sentence": "蒸笼蒸出小包子。", "say": "盖上盖子用水汽蒸熟是蒸。",
     "chat": "蒸笼冒出的白气是什么呀？", "life": "闻一闻刚蒸好的包子香不香。"},
    {"char": "尝", "pinyin": "cháng", "tone": "第二声",
     "sentence": "尝一口热汤。", "say": "小口试试味道就是尝。",
     "chat": "汤是咸咸的还是甜甜的呀？", "life": "尝一块水果，说说它的味道。"},
    {"char": "咬", "pinyin": "yǎo", "tone": "第三声",
     "sentence": "大口咬苹果。", "say": "牙齿咬下一口果肉是咬。",
     "chat": "咬苹果的时候会听到什么声？", "life": "咬一口苹果，听听咔嚓声。"},
    {"char": "嚼", "pinyin": "jiáo", "tone": "第二声（另读 jué，如“咀嚼”）",
     "sentence": "一口一口细细嚼。", "say": "牙齿上下磨呀磨就是嚼。",
     "chat": "为什么要把饭嚼碎再咽呀？", "life": "吃饼干时数数嚼了几下。"},
    {"char": "喊", "pinyin": "hǎn", "tone": "第三声",
     "sentence": "大声喊妈妈。", "say": "手放嘴边张大嘴，大声喊。",
     "chat": "什么时候需要大声喊人呀？", "life": "在公园远处喊：妈妈我在这里！"},
    {"char": "叫", "pinyin": "jiào", "tone": "第四声",
     "sentence": "公鸡喔喔叫。", "say": "小动物开口出声就是叫。",
     "chat": "小猫叫起来是什么声音呀？", "life": "学小猫喵喵叫，学小狗汪汪叫。"},
    {"char": "挤", "pinyin": "jǐ", "tone": "第三声",
     "sentence": "挤出小牙膏。", "say": "从下往上挤一挤就出来啦。",
     "chat": "牙膏挤黄豆大还是挤很多呀？", "life": "让他自己挤黄豆大的牙膏。"},
    {"char": "挥", "pinyin": "huī", "tone": "第一声",
     "sentence": "挥手说再见。", "say": "举起手左右摆摆就是挥手。",
     "chat": "你要跟谁挥挥手说再见呀？", "life": "出门时教他挥挥手说拜拜。"},
    {"char": "揉", "pinyin": "róu", "tone": "第二声",
     "sentence": "揉一个大面团。", "say": "手掌来回压一压转一转是揉。",
     "chat": "面团揉起来是软软的吗？", "life": "给他一小块面团揉着玩。"},
    {"char": "挠", "pinyin": "náo", "tone": "第二声",
     "sentence": "挠痒痒，咯咯笑。", "say": "轻轻抓痒痒逗人笑是挠。",
     "chat": "你怕不怕别人挠痒痒呀？", "life": "睡前互相挠痒痒笑一笑。"},
    {"char": "闻", "pinyin": "wén", "tone": "第二声",
     "sentence": "低头闻花香。", "say": "鼻子吸气闻一闻就是闻。",
     "chat": "花儿闻起来是什么味道呀？", "life": "闻闻香蕉和橘子谁更香。"},
    {"char": "铺", "pinyin": "pū", "tone": "第一声（另读 pù，如“店铺”）",
     "sentence": "铺好小床单。", "say": "把卷着的摊平铺开是铺。",
     "chat": "床单铺好后枕头放哪里呀？", "life": "请他帮忙铺自己的小床单。"},
    {"char": "盖", "pinyin": "gài", "tone": "第四声",
     "sentence": "给盒子盖上盖子。", "say": "把盖子对好合上去就是盖。",
     "chat": "盖上盖子还能看见小球吗？", "life": "让他把笔盒的小盖子盖好。"},
    {"char": "藏", "pinyin": "cáng", "tone": "第二声（另读 zàng，如“西藏”）",
     "sentence": "躲在树后捉迷藏。", "say": "躲起来不让人看见就是藏。",
     "chat": "捉迷藏时你爱藏在哪里呀？", "life": "把小熊藏起来请他去找。"},
    {"char": "卖", "pinyin": "mài", "tone": "第四声",
     "sentence": "卖水果咯，快来买。", "say": "把自己的东西换出去是卖。",
     "chat": "卖东西和买东西哪里不一样？", "life": "玩开店游戏，把玩具卖给他。"},
    {"char": "选", "pinyin": "xuǎn", "tone": "第三声",
     "sentence": "选一顶小帽子。", "say": "挑一个自己想要的就是选。",
     "chat": "两顶帽子你想选哪一顶呀？", "life": "两件衣服让他自己选一件。"},
    {"char": "抬", "pinyin": "tái", "tone": "第二声",
     "sentence": "一起抬小箱子。", "say": "两边一起用力举起来是抬。",
     "chat": "太重的东西一个人行吗？", "life": "和他一起抬小凳子挪一挪。"},
    {"char": "理", "pinyin": "lǐ", "tone": "第三声",
     "sentence": "把书本理整齐。", "say": "把乱乱的东西弄整齐是理。",
     "chat": "看完的书要放回哪里呀？", "life": "睡前和他一起理理小书架。"},
    {"char": "倒", "pinyin": "dǎo", "tone": "第三声（另读 dào，如“倒水”）",
     "sentence": "小心别摔倒。", "say": "身子歪倒在地上就是摔倒。",
     "chat": "不小心摔倒了怎么办呀？", "life": "跑慢一点，看着路别摔倒。"},
    {"char": "种", "pinyin": "zhòng", "tone": "第四声（另读 zhǒng，如“种子”）",
     "sentence": "种一棵小苗苗。", "say": "把小苗埋进土里就是种。",
     "chat": "小苗苗长大变成什么呀？", "life": "种一颗豆子，看它慢慢发芽。"},
    {"char": "堆", "pinyin": "duī", "tone": "第一声",
     "sentence": "堆一个大雪人。", "say": "一个摞一个，堆起来是堆。",
     "chat": "雪人的鼻子用什么做呀？", "life": "下雪了和他一起堆小雪人。"},
    {"char": "补", "pinyin": "bǔ", "tone": "第三声",
     "sentence": "给袜子补补丁。", "say": "破洞缝上小布块就是补。",
     "chat": "衣服破了洞要怎么办呀？", "life": "看他给娃娃衣服缝补丁。"},
    {"char": "吸", "pinyin": "xī", "tone": "第一声",
     "sentence": "用吸管吸果汁。", "say": "用吸管把果汁吸上来。",
     "chat": "吸管为什么能吸上果汁呀？", "life": "喝果汁时让他试试吸管。"},
    {"char": "舔", "pinyin": "tiǎn", "tone": "第三声",
     "sentence": "小口舔冰淇淋。", "say": "用舌头轻轻碰一下是舔。",
     "chat": "冰淇淋要慢慢舔还是大口咬？", "life": "吃冰淇淋时小口小口舔。"},
    {"char": "捆", "pinyin": "kǔn", "tone": "第三声",
     "sentence": "用绳子捆小棍。", "say": "绳子绕一圈拉紧就是捆。",
     "chat": "为什么要把它捆成一捆呀？", "life": "帮他把报纸捆成一小摞。"},
    {"char": "端", "pinyin": "duān", "tone": "第一声",
     "sentence": "端着饭碗慢慢走。", "say": "两只手把碗端得平平的。",
     "chat": "为什么端汤的时候要慢慢走？", "life": "请他端空碗帮着送到桌上。"},
    {"char": "竖", "pinyin": "shù", "tone": "第四声",
     "sentence": "把小旗竖起来。", "say": "一头朝上立得直直的是竖。",
     "chat": "旗杆是竖着的还是躺着的？", "life": "把蜡笔竖着立在桌子上。"},
    {"char": "抖", "pinyin": "dǒu", "tone": "第三声",
     "sentence": "抖一抖身上的水。", "say": "快快晃动把水珠抖下来。",
     "chat": "小狗毛湿了会怎么样呀？", "life": "洗完手甩三下，把水抖掉。"},
    {"char": "逗", "pinyin": "dòu", "tone": "第四声",
     "sentence": "拿玩具逗宝宝。", "say": "逗一逗，宝宝咯咯笑。",
     "chat": "做什么动作能把宝宝逗笑？", "life": "玩躲猫猫，逗小宝宝开心。"},
    {"char": "靠", "pinyin": "kào", "tone": "第四声",
     "sentence": "靠着大树歇一歇。", "say": "身体挨着树休息就是靠。",
     "chat": "累了的时候你想靠在哪里？", "life": "累了可以靠在妈妈身上歇。"},
    {"char": "搓", "pinyin": "cuō", "tone": "第一声",
     "sentence": "搓搓小手真暖和。", "say": "两手来回蹭一蹭就是搓。",
     "chat": "冬天小手冷了怎么办呀？", "life": "手冷了教他搓搓小手掌。"},
]


def arts():
    a = {}

    # 挑：扁担两头挂水桶
    a["挑"] = wrap(
        ground(),
        _rot(380, 258, -4, R(180, 249, 400, 18, 9, WOOD)),
        L(240, 268, 240, 328, "#8a5a33", 5),
        R(206, 328, 68, 56, 8, RED),
        R(206, 328, 68, 10, 5, RED_D),
        E(240, 334, 26, 6, WBLUE),
        R(206, 374, 68, 10, 5, RED_D),
        L(520, 250, 520, 330, "#8a5a33", 5),
        R(486, 330, 68, 56, 8, TEAL),
        R(486, 330, 68, 10, 5, TEAL_D),
        E(520, 336, 26, 6, WBLUE),
        R(486, 376, 68, 10, 5, TEAL_D),
        kid(x=380, y=430, s=1.0, pose="walk", shirt=BLUE, face="smile",
            arms="down", look=(0.5, 0)))

    # 拔：双手攥萝卜缨往上拔
    a["拔"] = wrap(
        ground(400, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=GREEN, face="o",
            arms="clap", look=(0, 0.2)),
        E(380, 428, 88, 24, WOOD_D),
        E(348, 424, 10, 6, "#a5713f"), E(420, 420, 8, 5, "#a5713f"),
        P("M 338 322 L 422 322 Q 412 402 380 424 Q 348 402 338 322 Z", RED),
        L(350, 350, 410, 350, "#d4552f", 5),
        L(348, 378, 412, 380, "#d4552f", 5),
        E(380, 258, 17, 40, GREEN_L),
        _rot(352, 272, -28, E(352, 272, 16, 36, GREEN_L)),
        _rot(408, 272, 28, E(408, 272, 16, 36, GREEN_L)),
        C(366, 292, 13, SKIN), C(394, 292, 13, SKIN),
        _dash("M 300 250 Q 320 236 344 240", TEAL, 5),
        _dash("M 460 250 Q 444 236 420 240", TEAL, 5))

    # 托：单手托平盘，盘上有小蛋糕
    a["托"] = wrap(
        ground(420, 446, 250, 24),
        kid(x=350, y=430, s=1.0, pose="stand", shirt=YEL, face="smile",
            arms="point", point_at=(490, 180), look=(0.6, -0.4)),
        E(474, 198, 58, 14, "#e9b97e"),
        E(474, 193, 56, 12, WHITE),
        R(452, 148, 40, 34, 10, "#f5a58c"),
        E(472, 142, 26, 16, WHITE),
        C(472, 118, 8, RED),
        _dash("M 552 168 Q 564 190 556 214", TEAL, 5))

    # 切：案板切苹果，一手扶刀
    a["切"] = wrap(
        ground(420, 446, 260, 24),
        table(400, 336, 310, 58),
        R(268, 344, 288, 24, 8, WOOD_L),
        C(322, 330, 36, RED_D), C(319, 327, 34, RED), C(308, 316, 8, "#f5a58c", 0.9),
        L(322, 294, 328, 280, "#5a3d2b", 5), E(334, 286, 12, 7, GREEN),
        P("M 384 332 Q 384 294 420 294 Q 456 294 456 332 Z", RED),
        E(420, 326, 32, 11, "#faeed3"),
        E(412, 324, 4, 7, INK), E(428, 324, 4, 7, INK),
        P("M 452 320 L 560 292 Q 574 289 574 303 L 574 312 L 452 340 Z", "#dfe3e6"),
        _rot(606, 296, -14, R(566, 282, 80, 28, 13, WOOD)),
        hand(636, 262, rot=-100, s=0.9))

    # 炒：妈妈在灶台前翻炒
    a["炒"] = wrap(
        ground(400, 446, 270, 24),
        kid(x=250, y=440, s=1.1, pose="stand", shirt=TEAL, bun=True, skirt=True,
            face="smile", arms="point", point_at=(420, 262), look=(0.8, -0.1)),
        R(300, 330, 240, 112, 12, "#d9d0c5"),
        R(316, 352, 90, 12, 6, "#c4b8a4"),
        P("M 326 268 Q 410 352 494 268 Z", "#6b5d52"),
        E(410, 268, 84, 13, "#8a7a6c"),
        R(380, 272, 14, 10, 3, GREEN), R(416, 278, 12, 9, 3, RED), R(444, 272, 13, 9, 3, YEL),
        _steam(376, 236, 0.9), _steam(444, 230, 0.8),
        L(386, 258, 430, 292, WOOD, 11),
        E(438, 298, 20, 11, "#c9cdd1"))

    # 煮：锅在炉火上咕嘟冒泡
    a["煮"] = wrap(
        ground(390, 446, 250, 24),
        P("M 348 392 Q 336 356 356 336 Q 358 362 372 372 Q 378 384 372 392 Z", SUN),
        P("M 356 390 Q 350 368 362 356 Q 364 372 370 380 Q 372 386 368 390 Z", "#e8823c"),
        P("M 402 392 Q 392 352 414 330 Q 416 360 430 370 Q 436 384 430 392 Z", SUN),
        P("M 410 390 Q 404 366 416 352 Q 418 370 424 378 Q 426 386 422 390 Z", "#e8823c"),
        P("M 456 392 Q 446 358 464 338 Q 466 362 478 372 Q 484 384 478 392 Z", SUN),
        R(295, 392, 190, 14, 7, "#6b5d52"),
        R(285, 268, 210, 112, 22, BLUE),
        E(390, 268, 105, 15, "#4a97c9"),
        E(278, 292, 15, 10, "#4a97c9"), E(502, 292, 15, 10, "#4a97c9"),
        _rot(390, 256, -7, wrap(E(390, 256, 92, 13, "#4a97c9"), C(448, 250, 9, "#4a97c9"))),
        C(340, 258, 9, WHITE), C(390, 252, 11, WHITE), C(436, 258, 8, WHITE),
        _steam(356, 224, 1.0), _steam(428, 214, 0.9))

    # 蒸：竹蒸笼冒大气，包子出笼
    a["蒸"] = wrap(
        ground(390, 446, 260, 24),
        table(390, 372, 270, 54),
        E(320, 362, 21, 12, WHITE), E(452, 360, 18, 11, WHITE),
        R(265, 318, 250, 56, 12, WOOD_L),
        R(275, 262, 230, 56, 12, WOOD_L),
        L(280, 336, 500, 336, "#d9a86c", 4), L(290, 280, 490, 280, "#d9a86c", 4),
        P("M 275 262 Q 390 214 505 262 Z", WOOD),
        C(390, 228, 12, WOOD_D),
        _steam(330, 212, 1.25, "#f0ece0"), _steam(396, 200, 1.45, "#f0ece0"),
        _steam(458, 212, 1.2, "#f0ece0"))

    # 尝：舀一勺汤送到嘴边尝
    a["尝"] = wrap(
        ground(420, 446, 260, 24),
        kid(x=370, y=430, s=1.0, pose="stand", shirt=RED, face="o",
            arms="point", point_at=(365, 242)),
        table(462, 368, 176, 52),
        bowl(448, 352, 46, rice=False),
        E(448, 350, 38, 9, "#f2a44c"),
        _steam(448, 322, 0.8),
        spoon(343, 232, 446, 348))

    # 咬：张嘴咬苹果，苹果缺了一口
    a["咬"] = wrap(
        ground(),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=YEL, face="open", arms="clap"),
        C(382, 268, 42, RED_D), C(379, 265, 40, RED),
        C(344, 250, 15, PAGE), C(338, 274, 12, PAGE), C(348, 294, 9, PAGE),
        C(368, 252, 9, "#f5a58c", 0.85))

    # 嚼：腮帮鼓鼓嚼饼干
    a["嚼"] = wrap(
        ground(420, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, face="smile",
            arms="point", point_at=(480, 235)),
        C(322, 212, 17, PINK, 0.85), C(438, 212, 17, PINK, 0.85),
        _dash("M 296 236 Q 290 248 296 260", TEAL, 4),
        _dash("M 464 236 Q 470 248 464 260", TEAL, 4),
        C(497, 208, 22, "#e9b97e"),
        C(490, 202, 3.5, "#8a5a33"), C(504, 212, 3.5, "#8a5a33"),
        C(494, 216, 3, "#8a5a33"),
        C(468, 258, 3, "#e9b97e"), C(478, 282, 3, "#e9b97e"), C(462, 300, 3, "#e9b97e"))

    # 喊：手拢嘴边大声喊
    a["喊"] = wrap(
        ground(400, 446, 250, 24),
        kid(x=360, y=430, s=1.0, pose="stand", shirt=RED, face="open",
            arms="point", point_at=(335, 240), look=(0.6, 0)),
        _waves(470, 222, [20, 38, 58], TEAL, 7))

    # 叫：公鸡喔喔叫
    a["叫"] = wrap(
        ground(380, 446, 250, 24),
        P("M 445 300 Q 502 262 522 202", stroke=GREEN, w=12),
        P("M 452 318 Q 518 288 548 238", stroke=TEAL, w=12),
        P("M 440 286 Q 482 252 492 216", stroke=YEL, w=12),
        E(375, 345, 88, 60, "#e9b97e"),
        _rot(370, 340, -14, E(370, 340, 42, 26, "#d99a2b")),
        L(352, 400, 350, 444, "#b57b44", 7), L(398, 400, 402, 444, "#b57b44", 7),
        L(338, 444, 362, 444, "#b57b44", 5), L(392, 444, 414, 444, "#b57b44", 5),
        C(295, 250, 40, "#f2b53c"),
        E(278, 206, 11, 16, RED), E(298, 197, 12, 18, RED), E(318, 206, 10, 14, RED),
        P("M 258 242 L 220 252 L 258 262 Z", "#e8663c"),
        P("M 260 268 L 226 278 L 262 280 Z", "#d4552f"),
        C(296, 294, 9, RED),
        C(288, 238, 6, INK), C(289, 236, 2, WHITE),
        _waves(190, 252, [16, 32], TEAL, 6))

    # 挤：手往下挤牙膏，牙膏落在牙刷上
    a["挤"] = wrap(
        ground(330, 446, 240, 22),
        table(320, 390, 280, 46),
        R(180, 380, 140, 18, 8, WOOD),
        R(296, 360, 46, 28, 6, WHITE),
        L(306, 362, 306, 386, "#e8e2d5", 3), L(320, 362, 320, 386, "#e8e2d5", 3),
        L(332, 362, 332, 386, "#e8e2d5", 3),
        P("M 262 300 Q 250 330 268 352 Q 276 362 292 368 L 300 356 Q 284 350 276 338 "
          "Q 268 322 278 306 Z", "#bfe3f2"),
        _rot(360, 292, -18, wrap(
            R(272, 264, 186, 58, 27, "#cfe6f0"),
            R(236, 270, 40, 46, 8, "#8a97a3"),
            R(306, 278, 112, 30, 13, WHITE, 0.85),
            R(444, 258, 16, 70, 5, "#a5d9f0"))),
        _dash("M 300 214 Q 288 232 300 248", TEAL, 5),
        _dash("M 452 214 Q 464 232 452 248", TEAL, 5),
        hand(362, 206, rot=180, s=0.95))

    # 挥：抬手挥别
    a["挥"] = wrap(
        ground(400, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=TEAL, face="open",
            arms="point", point_at=(492, 132), look=(0.5, -0.3)),
        _waves(500, 190, [18, 34], TEAL, 6))

    # 揉：桌上揉大面团
    a["揉"] = wrap(
        ground(390, 446, 260, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=GREEN, face="o", arms="clap"),
        table(380, 340, 270, 66),
        C(380, 312, 42, "#e3cd9e"),
        C(380, 306, 42, "#f7ecd2"),
        E(366, 296, 10, 6, "#e8dcc0"), E(396, 312, 8, 5, "#e8dcc0"),
        E(378, 322, 7, 4, "#e8dcc0"),
        C(300, 354, 6, WHITE), C(452, 358, 5, WHITE), C(320, 368, 5, WHITE),
        _dash("M 316 288 Q 304 304 316 320", TEAL, 5),
        _dash("M 444 288 Q 456 304 444 320", TEAL, 5))

    # 挠：妈妈伸手挠，宝宝笑弯了腰
    a["挠"] = wrap(
        ground(400, 446, 290, 24),
        kid(x=330, y=440, s=1.15, pose="stand", shirt="#f0876f", bun=True,
            skirt=True, face="smile", arms="reach", flip=-1, look=(0.6, 0.2)),
        _rot(480, 430, 6, wrap(
            kid(x=480, y=430, s=0.75, pose="stand", shirt=BLUE, face="open",
                arms="up", look=(-0.4, 0.2)),
            _dash("M 540 296 Q 552 306 544 318", TEAL, 4),
            _dash("M 556 282 Q 570 294 562 308", TEAL, 4))))

    # 闻：凑近大花闻香
    a["闻"] = wrap(
        ground(430, 446, 250, 24),
        L(552, 300, 544, 428, GREEN, 8),
        _rot(498, 356, -25, E(498, 356, 22, 11, GREEN_L)),
        _rot(370, 430, 12, kid(x=370, y=430, s=1.0, pose="stand", shirt=YEL,
                               face="o", arms="down", look=(1, 0))),
        flower5(552, 250, 46),
        P("M 478 214 Q 492 200 482 184", stroke=TEAL, w=5),
        P("M 488 250 Q 504 238 494 222", stroke=TEAL, w=5))

    # 铺：把床单铺平
    a["铺"] = wrap(
        ground(420, 446, 280, 24),
        R(240, 270, 26, 150, 10, WOOD_D),
        R(258, 330, 290, 86, 12, WOOD),
        R(272, 416, 22, 24, 6, WOOD_D), R(508, 416, 22, 24, 6, WOOD_D),
        R(266, 308, 274, 40, 10, WHITE),
        E(318, 314, 36, 14, "#f4f1e8"),
        kid(x=600, y=430, s=1.0, pose="stand", shirt=BLUE, face="o",
            arms="reach", look=(-0.7, 0)),
        P("M 352 306 L 540 306 Q 556 306 556 324 L 556 348 Q 556 356 546 356 "
          "L 366 356 Q 350 356 352 336 Z", RED),
        P("M 352 306 L 352 356 L 320 356 Q 316 324 352 306 Z", RED_D))

    # 盖：给开着口的盒子盖上盖子
    a["盖"] = wrap(
        ground(420, 446, 260, 24),
        kid(x=560, y=430, s=0.95, pose="stand", shirt=TEAL, face="o",
            arms="point", point_at=(490, 262), look=(-0.6, -0.2)),
        box(340, 318, 200, 112, open_top=True),
        C(360, 348, 16, RED_D), C(357, 345, 14, RED),
        lid(452, 256, 182, 46, rot=-12))

    # 藏：躲在树后捉迷藏（探出半个身子）
    a["藏"] = wrap(
        ground(430, 446, 280, 24),
        kid(x=330, y=430, s=0.95, pose="stand", shirt=RED, face="o",
            arms="down", look=(-0.6, 0)),
        tree_round(480, 435, 1.15),
        L(300, 430, 300, 414, GREEN, 5), L(286, 434, 286, 420, GREEN, 5),
        _dash("M 236 300 Q 222 330 238 360", TEAL, 5))

    # 卖：摊主站在水果摊后面，把纸袋递过柜台给顾客的手（摊位有柱子撑雨篷）
    a["卖"] = wrap(
        ground(390, 446, 260, 24),
        L(254, 130, 254, 332, "#8a5a33", 9), L(506, 130, 506, 332, "#8a5a33", 9),
        R(230, 100, 300, 30, 10, RED),
        E(266, 132, 30, 15, RED), E(326, 132, 30, 15, WHITE), E(386, 132, 30, 15, RED),
        E(446, 132, 30, 15, WHITE), E(494, 132, 26, 15, RED),
        kid(x=280, y=430, s=1.0, pose="stand", shirt=BLUE, face="smile",
            arms="point", point_at=(475, 250), look=(0.8, -0.1)),
        table(380, 330, 300, 76),
        C(300, 316, 20, RED_D), C(297, 313, 18, RED), C(330, 320, 15, RED),
        C(430, 318, 19, "#f2a44c"), C(427, 315, 17, "#f2b53c"), C(462, 322, 15, "#f2b53c"),
        _rot(440, 268, -10, wrap(R(412, 240, 56, 56, 8, "#e9b97e"),
                                 R(412, 240, 56, 14, 7, WOOD_D, 0.35))),
        _dash("M 478 260 Q 522 262 548 268", TEAL, 5),
        hand(606, 262, rot=-120, s=0.9))

    # 选：两顶帽子选一顶
    a["选"] = wrap(
        ground(390, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=YEL, face="o",
            arms="point", point_at=(490, 330), look=(0.8, 0.1)),
        E(265, 398, 62, 14, RED),
        P("M 227 398 Q 227 342 265 342 Q 303 342 303 398 Z", RED_D),
        R(229, 374, 72, 14, 7, YEL_D),
        E(495, 398, 62, 14, TEAL),
        P("M 457 398 Q 457 342 495 342 Q 533 342 533 398 Z", TEAL_D),
        R(459, 374, 72, 14, 7, YEL_D),
        P("M 360 116 Q 358 88 382 86 Q 406 84 406 108 Q 406 124 384 130 L 384 140",
          stroke="#d99a2b", w=9),
        C(384, 156, 6.5, "#d99a2b"))

    # 抬：两人一起抬小箱子
    a["抬"] = wrap(
        ground(380, 446, 280, 24),
        kid(x=310, y=430, s=0.85, pose="walk", shirt=TEAL, face="smile",
            arms="down", look=(0.5, 0)),
        kid(x=450, y=430, s=0.85, pose="walk", shirt=TEAL, face="smile",
            arms="down", look=(-0.5, 0)),
        R(338, 312, 88, 78, 10, WOOD),
        R(348, 326, 68, 12, 5, WOOD_L), R(348, 354, 68, 12, 5, WOOD_L),
        C(364, 349, 11, SKIN), C(396, 349, 11, SKIN))

    # 理：把书架上歪的书扶正
    a["理"] = wrap(
        ground(430, 446, 270, 24),
        R(455, 215, 180, 205, 10, WOOD),
        R(467, 227, 156, 181, 8, WOOD_L),
        R(467, 296, 156, 12, 6, WOOD_D),
        R(467, 368, 156, 12, 6, WOOD_D),
        R(478, 322, 24, 46, 4, RED), R(506, 322, 24, 46, 4, TEAL),
        R(534, 322, 24, 46, 4, YEL),
        _rot(585, 322, 16, R(573, 322, 24, 46, 4, WBLUE)),
        C(520, 278, 14, SUN),
        _dash("M 536 306 Q 552 296 568 300", TEAL, 4),
        kid(x=400, y=430, s=0.95, pose="stand", shirt=BLUE, face="o",
            arms="point", point_at=(545, 300), look=(0.8, 0.1)))

    # 倒：绊到皮球摔倒
    a["倒"] = wrap(
        ground(400, 446, 260, 24),
        ball(318, 416, 24, TEAL, TEAL_D, TEAL_L),
        _rot(420, 432, -22, kid(x=420, y=432, s=1.0, pose="stand", shirt=RED,
                                face="o", arms="up")),
        _dash("M 268 300 Q 252 330 268 360", TEAL, 5),
        _dash("M 300 262 Q 282 292 296 322", TEAL, 4),
        E(300, 438, 34, 8, "#b8dcc9", 0.8))

    # 种：蹲在土堆边种小苗
    a["种"] = wrap(
        ground(420, 446, 270, 24),
        kid(x=330, y=445, s=1.0, pose="sit", shirt=TEAL, face="o",
            arms="reach", flip=-1, look=(0.7, 0.2)),
        E(510, 400, 72, 24, WOOD_D),
        E(474, 396, 9, 5, "#a5713f"), E(546, 392, 8, 5, "#a5713f"),
        L(510, 386, 506, 318, GREEN, 7),
        _rot(486, 322, -22, E(486, 322, 21, 11, GREEN_L)),
        _rot(528, 322, 22, E(528, 322, 21, 11, GREEN_L)),
        _dash("M 448 372 Q 466 366 480 372", TEAL, 4))

    # 堆：堆雪人
    a["堆"] = wrap(
        ground(390, 446, 270, 24),
        E(380, 438, 200, 20, WHITE),
        C(380, 360, 62, WHITE), E(368, 344, 18, 12, "#f0ece0"),
        C(380, 268, 44, WHITE),
        C(366, 260, 5, INK), C(394, 260, 5, INK),
        P("M 398 268 L 430 276 L 398 284 Z", "#e8663c"),
        C(380, 352, 6, INK), C(380, 378, 6, INK),
        L(322, 340, 268, 306, "#8a5a33", 8), L(438, 340, 492, 306, "#8a5a33", 8),
        R(346, 298, 68, 18, 9, RED), R(398, 306, 18, 40, 8, RED),
        kid(x=490, y=430, s=0.9, pose="stand", shirt=BLUE, face="smile",
            arms="point", point_at=(430, 240), look=(-0.7, -0.1)),
        C(268, 250, 7, WHITE), C(238, 300, 6, WHITE), C(300, 210, 6, WHITE))

    # 补：给袜子缝爱心补丁
    a["补"] = wrap(
        ground(400, 446, 270, 24),
        kid(x=490, y=445, s=0.95, pose="sit", shirt=YEL, face="o",
            arms="reach", look=(-0.7, 0.3)),
        R(282, 330, 54, 60, 14, "#cfe6f0"),
        L(282, 358, 336, 358, "#a5d9f0", 4),
        R(300, 336, 110, 50, 12, WHITE),
        R(392, 368, 96, 46, 18, WHITE),
        C(440, 390, 14, "#e8dfc8"),
        heart(440, 388, 17, RED),
        P("M 424 388 A 16 16 0 1 1 456 388", stroke=RED, w=3),
        P("M 452 398 Q 436 384 410 378", stroke=RED, w=3),
        _dash("M 348 320 Q 362 308 380 310", TEAL, 4))

    # 吸：捧着杯子用吸管吸果汁
    a["吸"] = wrap(
        ground(390, 446, 240, 22),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=WBLUE, face="o", arms="clap"),
        R(368, 252, 64, 76, 12, "#f5a58c"),
        R(374, 288, 52, 34, 8, "#f2a44c"),
        C(394, 302, 4, WHITE, 0.85), C(412, 296, 3, WHITE, 0.85),
        L(402, 258, 384, 224, "#e8663c", 8),
        E(380, 222, 10, 12, "#6b3325"),
        _dash("M 452 236 Q 468 220 486 228", TEAL, 4))

    # 舔：小口舔冰淇淋
    a["舔"] = wrap(
        ground(390, 446, 240, 22),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=GREEN, face="smile",
            arms="clap", look=(0, 0.3)),
        P("M 354 300 L 406 300 L 380 354 Z", WOOD_D),
        L(360, 314, 396, 322, "#b57b44", 3), L(366, 336, 392, 326, "#b57b44", 3),
        C(380, 276, 36, "#f5a58c"),
        P("M 356 292 Q 352 312 362 316", stroke="#f5a58c", w=6),
        E(380, 248, 11, 15, "#f0876f"),
        _dash("M 470 240 Q 484 224 500 232", TEAL, 4))

    # 捆：用绳子把小棍捆紧
    a["捆"] = wrap(
        ground(400, 446, 250, 24),
        kid(x=380, y=445, s=1.0, pose="sit", shirt=TEAL, face="o", arms="clap"),
        _rot(395, 384, 3, R(320, 368, 150, 15, 7, WOOD)),
        _rot(398, 391, 1, R(323, 384, 150, 15, 7, WOOD_L)),
        _rot(400, 398, -3, R(325, 400, 150, 15, 7, WOOD)),
        L(372, 362, 375, 424, "#e8663c", 6), L(390, 360, 392, 426, "#e8663c", 6),
        C(382, 393, 9, "#d4552f"),
        P("M 373 362 Q 368 340 366 330", stroke="#e8663c", w=5),
        P("M 391 360 Q 394 340 394 330", stroke="#e8663c", w=5))

    # 端：双手端平饭碗慢慢走
    a["端"] = wrap(
        ground(390, 446, 250, 24),
        kid(x=380, y=430, s=1.0, pose="walk", shirt=YEL, face="o",
            arms="clap", look=(0, 0.2)),
        bowl(380, 306, 50, rice=True),
        _steam(368, 268, 0.8), _steam(396, 258, 0.7))

    # 竖：旗杆立在身旁竖得直直的，一只手扶在旗杆下段
    a["竖"] = wrap(
        ground(390, 446, 240, 22),
        kid(x=305, y=430, s=1.0, pose="stand", shirt=GREEN, face="smile",
            arms="point", point_at=(372, 310)),
        E(380, 400, 44, 12, WOOD_D),
        R(371, 140, 18, 256, 9, WOOD_D),
        C(380, 134, 10, YEL_D),
        R(389, 144, 92, 44, 10, RED),
        C(378, 348, 12, SKIN),
        _dash("M 500 210 Q 516 226 508 248", TEAL, 5))

    # 抖：抖掉身上的水珠
    a["抖"] = wrap(
        ground(390, 446, 250, 24),
        E(380, 444, 88, 10, WBLUE, 0.5),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, face="o", arms="down"),
        _dash("M 296 300 Q 280 340 298 380", TEAL, 5),
        _dash("M 464 300 Q 480 340 462 380", TEAL, 5),
        drop(300, 250, 10), drop(286, 332, 9), drop(462, 254, 10),
        drop(478, 342, 9), drop(340, 196, 8), drop(424, 192, 8))

    # 逗：拿小玩具逗宝宝笑
    a["逗"] = wrap(
        ground(400, 446, 290, 24),
        kid(x=300, y=440, s=1.1, pose="stand", shirt=YEL, bun=True, skirt=True,
            face="smile", arms="reach", flip=-1, look=(0.7, 0)),
        L(410, 302, 432, 284, WOOD, 8),
        _rot(448, 276, 20, E(448, 276, 16, 20, RED)),
        C(448, 258, 6, YEL),
        kid(x=500, y=445, s=0.62, pose="sit", shirt=RED, face="open",
            arms="up", look=(-0.5, 0)),
        _dash("M 560 288 Q 572 298 564 310", TEAL, 4),
        _dash("M 576 272 Q 590 284 582 298", TEAL, 4))

    # 靠：身体斜靠在树干上歇一歇，一只手搭在树干上
    a["靠"] = wrap(
        ground(360, 446, 280, 24),
        tree_round(190, 432, 1.15),
        _rot(268, 430, -7, kid(x=268, y=430, s=0.95, pose="stand", shirt=GREEN,
                               face="smile", arms="down", look=(-0.5, 0))),
        E(300, 440, 40, 8, "#b8dcc9", 0.7))

    # 搓：冬天里围着围巾搓手取暖，两手合在身前来回蹭
    a["搓"] = wrap(
        ground(390, 446, 240, 22),
        kid(x=380, y=430, s=1.0, pose="stand", shirt=BLUE, face="smile", arms="clap"),
        R(350, 254, 60, 18, 9, RED),
        R(402, 262, 18, 40, 8, RED),
        _dash("M 380 316 Q 398 324 416 316", TEAL, 5),
        cloud_p(276, 152, 0.3, WHITE),
        _dash("M 486 150 Q 502 132 522 140", "#f0ece0", 5))

    return a


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    cards = GROUP_CARDS
    assert [c["char"] for c in cards] == list(B_CHARS), "字序与 B1 分配清单不一致"
    amap = arts()
    assert list(amap.keys()) == list(B_CHARS), "arts key 与清单不一致"
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
    print(f"dongzuo4_b 自检通过：{len(cards)} 卡，SVG 全部合法")
