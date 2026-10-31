#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画素材：人称组（rencheng，20 字，无种子字）。

人 你 我 他 爸 妈 爷 奶 哥 姐 弟 妹 娃 朋 友 宝 叔 姨 师 医。
本组靠人物区分：全部复用 lib.kid() 及其参数（发型/身形/服装/道具），
大人 s=1.05、孩子 s=0.8~0.98 增加辨识；相邻卡服装主色彼此错开。
"""
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

from 识字卡片_素材库 import (
    BLUE, BLUE_D, GREEN, GREEN_L, HAIR, INK, PINK, RED, RED_D, SKIN, SKIN_D,
    TEAL, TEAL_D, TEAL_L, WBLUE, WHITE, WOOD, WOOD_D, WOOD_L, YEL, YEL_D, SUN_L,
    C, E, L, P, PG, R, ball, ground, hand, heart, kid, star5, wrap,
)

GROUP_CARDS = [
    {"char": "人", "pinyin": "rén", "tone": "第二声",
     "sentence": "大人牵着小孩子。",
     "say": "站着的就是人，爸爸妈妈都是人。",
     "chat": "家里一共有几个人呀？",
     "life": "数一数今天见过几个人。"},
    {"char": "你", "pinyin": "nǐ", "tone": "第三声",
     "sentence": "你好呀，小朋友。",
     "say": "指着的那个人，就是“你”。",
     "chat": "“我指的是谁呀？”被指到的小朋友答：是我！",
     "life": "和孩子面对面，互相指着说“你”和“我”。"},
    {"char": "我", "pinyin": "wǒ", "tone": "第三声",
     "sentence": "我自己会穿鞋啦。",
     "say": "手放胸口说的就是我。",
     "chat": "说说我最爱吃的水果。",
     "life": "拍拍胸口说：我自己来！"},
    {"char": "他", "pinyin": "tā", "tone": "第一声",
     "sentence": "他是我的好朋友。",
     "say": "手指着的那个男孩，就是“他”。",
     "chat": "“我指的是谁呀？”被指到的男生答：是我！",
     "life": "指着爸爸或爷爷的照片说：他。"},
    {"char": "爸", "pinyin": "bà", "tone": "第四声",
     "sentence": "爸爸牵着我散步。",
     "say": "高高短发的是爸爸。",
     "chat": "爸爸最拿手的菜是什么？",
     "life": "给爸爸一个大大的拥抱。"},
    {"char": "妈", "pinyin": "mā", "tone": "第一声",
     "sentence": "妈妈抱着宝宝笑。",
     "say": "长头发穿粉衣的是妈妈。",
     "chat": "妈妈的声音和谁的很像？",
     "life": "帮妈妈拿一双拖鞋来。"},
    {"char": "爷", "pinyin": "yé", "tone": "第二声",
     "sentence": "爷爷拄着拐杖走。",
     "say": "白胡子拄拐杖的是爷爷。",
     "chat": "爷爷讲过哪个好听的故事？",
     "life": "给爷爷捶捶背。"},
    {"char": "奶", "pinyin": "nǎi", "tone": "第三声",
     "sentence": "奶奶煮的饺子香。",
     "say": "头发白白挽髻的是奶奶。",
     "chat": "奶奶做的哪道菜最香？",
     "life": "帮奶奶择一次菜。"},
    {"char": "哥", "pinyin": "gē", "tone": "第一声",
     "sentence": "哥哥带我踢皮球。",
     "say": "戴棒球帽的高个子是哥哥。",
     "chat": "想和哥哥一起玩什么？",
     "life": "和哥哥击一次掌。"},
    {"char": "姐", "pinyin": "jiě", "tone": "第三声",
     "sentence": "姐姐扎着小辫子。",
     "say": "扎两个小辫的是姐姐。",
     "chat": "姐姐教你做过什么事？",
     "life": "跟姐姐学扎辫子。"},
    {"char": "弟", "pinyin": "dì", "tone": "第四声",
     "sentence": "小弟弟坐在地上玩。",
     "say": "坐地上玩皮球的小小孩，是弟弟。",
     "chat": "“哪个是弟弟？他比哥哥大还是小？”",
     "life": "问问孩子：家里谁是哥哥，谁是弟弟？"},
    {"char": "妹", "pinyin": "mèi", "tone": "第四声",
     "sentence": "妹妹坐着喝奶。",
     "say": "抱着奶瓶喝奶的小小孩，是妹妹。",
     "chat": "“妹妹在做什么呀？”",
     "life": "喝奶的时候说：妹妹在喝奶，宝宝也在喝奶。"},
    {"char": "娃", "pinyin": "wá", "tone": "第二声",
     "sentence": "小娃娃睡得香。",
     "say": "包在小被子里的是小娃娃。",
     "chat": "小娃娃哭了大人在做什么？",
     "life": "抱抱自己的小娃娃玩偶。"},
    {"char": "朋", "pinyin": "péng", "tone": "第二声",
     "sentence": "朋友多了真快乐。",
     "say": "一起玩不吵架的就是朋友。",
     "chat": "你最好的朋友叫什么名字？",
     "life": "约一个小朋友明天一起玩。"},
    {"char": "友", "pinyin": "yǒu", "tone": "第三声",
     "sentence": "我和你是好朋友。",
     "say": "两只手握在一起，就是好朋友。",
     "chat": "“你的好朋友是谁呀？和他握握手。”",
     "life": "见到好朋友，握握手或拉拉手。"},
    {"char": "宝", "pinyin": "bǎo", "tone": "第三声",
     "sentence": "小宝宝是家里的宝。",
     "say": "捧在手心的心肝就是宝。",
     "chat": "爸爸妈妈叫你什么小名？",
     "life": "抱紧妈妈说：我是你的宝。"},
    {"char": "叔", "pinyin": "shū", "tone": "第一声",
     "sentence": "叔叔帮我修玩具。",
     "say": "下巴刺刺的是叔叔，爸爸的朋友。",
     "chat": "小区里你认识哪位叔叔？",
     "life": "见到叔叔挥手问好。"},
    {"char": "姨", "pinyin": "yí", "tone": "第二声",
     "sentence": "小姨来看我啦。",
     "say": "妈妈的姐妹要叫姨，拎着小包。",
     "chat": "你喜欢姨带来的小礼物吗？",
     "life": "给姨一个大大的笑脸。"},
    {"char": "师", "pinyin": "shī", "tone": "第一声",
     "sentence": "老师教我画小船。",
     "say": "戴眼镜拿书的是老师。",
     "chat": "你想跟老师学什么？",
     "life": "见到老师大声问好。"},
    {"char": "医", "pinyin": "yī", "tone": "第一声",
     "sentence": "医生看病真温柔。",
     "say": "穿白大褂的是医生，看病找他。",
     "chat": "听诊器贴在身上是什么感觉？",
     "life": "用玩具听诊器给娃娃看病。"},
]


def _km(x, y, s):
    """kid 的关键坐标：头半径 / 肩线 / 头心。"""
    hd = 62 * s
    sho = y - 168 * s
    hcy = sho - 8 * s - hd
    return hd, sho, hcy


def _hair_back(x, y, s, color=HAIR):
    """长发后脑层：画在 kid 之前，从头后披到肩下。"""
    hd, sho, hcy = _km(x, y, s)
    top = hcy - hd
    return P(f"M {x - hd*1.24:.0f} {hcy + 2*s:.0f} Q {x - hd*1.30:.0f} {top - hd*0.12:.0f} "
             f"{x} {top - hd*0.16:.0f} Q {x + hd*1.30:.0f} {top - hd*0.12:.0f} "
             f"{x + hd*1.24:.0f} {hcy + 2*s:.0f} "
             f"L {x + hd*1.12:.0f} {sho + 66*s:.0f} Q {x + hd*1.02:.0f} {sho + 80*s:.0f} "
             f"{x + hd*0.78:.0f} {sho + 72*s:.0f} L {x - hd*0.78:.0f} {sho + 72*s:.0f} "
             f"Q {x - hd*1.02:.0f} {sho + 80*s:.0f} {x - hd*1.12:.0f} {sho + 66*s:.0f} Z", color)


# ---------- 各卡插画 ----------
def a_ren():
    """人：一个普通小人正面站。"""
    return ground() + kid(380, 444, s=0.98, shirt=TEAL)


def a_ni():
    """你：左边小朋友指着右边被高亮的伙伴——被指的就是「你」。
    正常短臂指到半途即停，目标用淡黄高光圆标识，不拉长手臂。"""
    return ground() + wrap(
        E(490, 298, 112, 120, "#fdeaa0", 0.35),
        kid(490, 444, s=0.98, face="smile", shirt=RED, look=(-1, 0)),
        kid(280, 444, s=0.9, face="smile", shirt="#8fb8d8",
            arms="point", point_at=(455, 300), look=(1, 0)))


def a_wo():
    """我：双手捧在胸口、竖起拇指指向自己——「就是我」。
    两臂各自连肩（clap），拇指从双拳之间竖起、贴红衣对比清晰，
    无悬空手也无第三只手（肩部折臂方案会产生肤色大块，已弃用）。"""
    s = 0.92
    x, y = 380, 444
    sho = y - 168 * s
    thumb = R(x - 6, sho + 1 * s, 12, 26, 6, SKIN)
    return ground() + kid(x, y, s=s, face="smile", shirt=RED, look=(0, 3),
                          arms="clap") + thumb


def a_ta():
    """他：小朋友指着前面背对我们的黄衣男孩——被指的那个别人就是「他」。
    背面小孩复用 dongzuo 组 a_bei 画法（后脑勺全发+双耳），全程无画外手臂。"""
    s2 = 0.95
    bx, by = 470, 444
    sho = by - 168 * s2
    hip = by - 96 * s2
    hd = 62 * s2
    hcy = sho - 8 * s2 - hd
    boy = wrap(
        E(bx, by - 145 * s2, 108, 132, "#fdeaa0", 0.35),
        R(bx - 30 * s2, hip - 10 * s2, 26 * s2, 84 * s2, 12 * s2, BLUE_D),
        R(bx + 4 * s2, hip - 10 * s2, 26 * s2, 84 * s2, 12 * s2, BLUE_D),
        E(bx - 17 * s2, by - 6 * s2, 21 * s2, 10 * s2, INK, 0.85),
        E(bx + 17 * s2, by - 6 * s2, 21 * s2, 10 * s2, INK, 0.85),
        P(f"M {bx-56*s2} {sho} Q {bx-58*s2} {hip+6*s2} {bx-40*s2} {hip+8*s2} "
          f"L {bx+40*s2} {hip+8*s2} Q {bx+58*s2} {hip+6*s2} {bx+56*s2} {sho} "
          f"Q {bx} {sho-16*s2} {bx-56*s2} {sho} Z", YEL),
        L(bx - 46 * s2, sho + 8 * s2, bx - 62 * s2, sho + 72 * s2, SKIN, 28 * s2),
        L(bx + 46 * s2, sho + 8 * s2, bx + 62 * s2, sho + 72 * s2, SKIN, 28 * s2),
        C(bx - 64 * s2, sho + 74 * s2, 12 * s2, SKIN),
        C(bx + 64 * s2, sho + 74 * s2, 12 * s2, SKIN),
        C(bx, hcy, hd, HAIR),
        C(bx - hd * 0.98, hcy + 6 * s2, 9 * s2, SKIN),
        C(bx + hd * 0.98, hcy + 6 * s2, 9 * s2, SKIN))
    return ground() + boy + kid(270, 444, s=0.82, face="smile", shirt="#8fb8d8",
                                arms="point", point_at=(450, 298), look=(1, 0))


def a_ba():
    """爸：利用两个人物本身的手掌相接，不再额外补第三条肤色手臂。"""
    dad = kid(300, 446, s=0.92, pose="walk", arms="hold_right", shirt=BLUE)
    # 两人同站在地面上，左右手掌在 (379, 360) 附近相接，不额外加连接线。
    child = kid(445, 446, s=0.65, pose="walk", arms="hold_left",
                face="smile", shirt="#f0876f")
    return ground() + wrap(dad, child)


def a_ma():
    """妈：长发妈妈横抱襁褓宝宝于胸前——头端略高、近臂环过襁褓下缘、婴儿脸清晰。"""
    # 远侧手臂（画在襁褓后面）：从左肩伸向右下
    arm_far = P("M 336 282 Q 312 330 352 370", stroke=SKIN, w=26)
    # 襁褓：横抱在胸前，头端（左）略高 —— 整体旋转 12°
    bundle = ('<g transform="rotate(12 390 350)">'
              + R(295, 322, 190, 60, 30, "#f7e6b8")
              + L(368, 326, 358, 374, "#ead9a0", 5)
              + L(410, 326, 400, 374, "#ead9a0", 5)
              + "</g>")
    # 婴儿头（襁褓左端上方，清晰露出）：闭眼+小嘴+腮红+一撮头发
    head = wrap(
        C(318, 316, 27, SKIN),
        P("M 291 308 Q 295 286 318 285 Q 341 286 345 308 "
          "Q 333 298 318 299 Q 303 298 291 308 Z", HAIR),
        P("M 306 320 Q 311 325 316 320", stroke=INK, w=3),
        P("M 322 320 Q 327 325 332 320", stroke=INK, w=3),
        P("M 310 334 Q 318 340 326 334", stroke=INK, w=3),
        E(332, 331, 6, 4.5, "#f0876f"),
        C(300, 330, 7, PINK, 0.8) + C(334, 330, 7, PINK, 0.8))
    # 近侧手臂（右）：从右肩沿襁褓下缘环抱到右端，手扶在襁褓上
    arm_near = P("M 424 282 Q 454 330 438 374", stroke=SKIN, w=26)
    hand = C(432, 380, 13, SKIN)
    return ground() + wrap(
        _hair_back(380, 448, 1.05),
        kid(380, 448, s=1.05, shirt=PINK, look=(0, 1.2), face="smile"),
        arm_far, bundle, head, arm_near, hand)


def a_ye():
    """爷：白发白胡子+拐杖。"""
    cane = wrap(
        P("M 446 334 Q 464 320 472 338 L 478 432", stroke=WOOD, w=13),
        C(458, 330, 11, WOOD), E(478, 436, 11, 6, WOOD_D))
    glasses = ('<g fill="none" stroke="#4a3226" stroke-width="6">'
               + '<circle cx="357" cy="190" r="24"/><circle cx="403" cy="190" r="24"/>'
               + '<path d="M 381 188 L 379 188"/></g>')
    beard = P("M 336 252 Q 340 300 380 304 Q 420 300 424 252 "
              "Q 404 266 380 266 Q 356 266 336 252 Z", "#d9d0c5")
    return ground() + kid(380, 446, s=1.05, shirt=WOOD_D, hair_color="#d9d0c5",
                          mustache=True, extra=cane + glasses + beard)


def a_nai():
    """奶：白发圆发髻+围裙色上衣，身旁一盘冒热气的饺子（呼应句子）。"""
    apron = wrap(
        P("M 336 326 L 424 326 L 432 382 Q 380 400 328 382 Z", "#fbf0c2"),
        L(354, 280, 346, 328, "#f4e6b8", 10), L(406, 280, 414, 328, "#f4e6b8", 10),
        C(380, 342, 7, "#e8d9a0"))
    dumplings = wrap(
        E(560, 431, 66, 14, "#8fb8d8"),
        E(560, 428, 58, 11, "#cfe6f0"),
        P("M 506 426 Q 508 400 528 396 Q 546 394 554 418 Q 530 430 506 426 Z", "#f7eeda"),
        P("M 540 428 Q 542 400 562 396 Q 580 394 588 420 Q 564 432 540 428 Z", "#f7eeda"),
        P("M 574 426 Q 578 404 594 402 Q 610 402 616 422 Q 594 432 574 426 Z", "#f7eeda"),
        P("M 518 404 Q 526 396 536 402", stroke="#d8bfa0", w=3.5),
        P("M 552 406 Q 560 398 570 404", stroke="#d8bfa0", w=3.5),
        P("M 586 408 Q 592 402 600 406", stroke="#d8bfa0", w=3.5),
        P("M 534 384 Q 528 370 536 356", stroke="#c9d8d0", w=6),
        P("M 566 382 Q 560 368 568 354", stroke="#c9d8d0", w=6))
    return ground() + kid(380, 444, s=1.02, shirt=TEAL_L,
                          hair_color="#d9d0c5", bun=True, extra=apron + dumplings)


def a_ge():
    """哥：戴棒球帽的高个男孩（帽檐抬高，不能盖住眼睛）。"""
    cap = wrap(
        '<g transform="translate(0,-22)">'
        + P("M 322 194 Q 316 118 380 114 Q 444 118 438 194 Q 380 164 322 194 Z", RED)
        + C(380, 112, 9, RED_D) + "</g>",
        E(380, 174, 72, 10, RED_D))
    ball = wrap(C(478, 424, 34, "#4fae9f"), C(466, 410, 10, "#7cc8bb", 0.9))
    return ground() + kid(380, 446, s=1.0, shirt=WBLUE, extra=cap) + ball


def a_jie():
    """姐：双马尾+裙子的女孩。"""
    tails = wrap(
        '<g transform="rotate(18 298 238)">' + E(298, 238, 17, 40, HAIR) + "</g>",
        '<g transform="rotate(-18 462 238)">' + E(462, 238, 17, 40, HAIR) + "</g>",
        C(320, 222, 9, RED), C(440, 222, 9, RED))
    return ground() + kid(380, 444, s=0.85, shirt=YEL, skirt=True, extra=tails)


def a_di():
    """弟：坐地上玩皮球的小弟弟——复用 kid 坐姿（垂臂+前伸腿），不再自画张开手臂。"""
    return ground(380, 452, 230, 20) + wrap(
        kid(370, 444, s=0.8, pose="sit", shirt=GREEN, face="open", look=(0.9, 0.4)),
        ball(475, 428, 24, TEAL, TEAL_D, TEAL_L))


def a_mei():
    """妹：坐地上抱奶瓶喝奶的小妹妹——复用 kid 坐姿（四肢相连不断开），奶瓶斜贴嘴边。"""
    bottle = ('<g transform="rotate(-30 415 341)">'
              + R(402, 312, 26, 58, 10, WBLUE)
              + R(406, 316, 18, 10, 4, WHITE)
              + C(415, 306, 9, YEL)
              + "</g>")
    grip = C(430, 376, 11, SKIN)  # 小手搭在瓶身下段，与 kid 自带右手融合
    return ground(380, 452, 230, 20) + wrap(
        kid(380, 444, s=0.78, pose="sit", bun=True, skirt=True,
            face="open", look=(0.6, 0.3)),
        bottle, grip)


def _swaddle_body():
    """襁褓婴儿本体（不含地面）：圆脸+包巾，娃/宝 两卡复用。"""
    return wrap(
        E(392, 382, 144, 76, YEL_D),
        C(384, 254, 60, SKIN_D), C(378, 248, 58, SKIN),
        P("M 358 194 Q 376 178 394 194", stroke=HAIR, w=7),
        P("M 344 248 Q 354 240 364 248", stroke=INK, w=6),
        P("M 390 248 Q 400 240 410 248", stroke=INK, w=6),
        C(340, 268, 11, PINK, 0.8), C(414, 268, 11, PINK, 0.8),
        E(377, 278, 9, 7, "#f0876f"),
        E(380, 378, 138, 76, SUN_L),
        P("M 318 304 Q 380 330 442 304 Q 438 326 380 344 Q 322 326 318 304 Z", YEL),
        P("M 268 386 Q 380 362 492 386", stroke=YEL, w=6),
        R(252, 404, 256, 22, 11, YEL),
        C(514, 392, 13, YEL))


def a_wa():
    """娃：裹襁褓的婴儿（圆脸+包巾，包巾裹住下巴以下）。"""
    return ground() + _swaddle_body()


def a_peng():
    """朋：两个小人并排挥手。"""
    return ground() + kid(262, 446, s=0.8, shirt=RED, arms="up") \
        + kid(498, 446, s=0.8, shirt=GREEN, arms="up")


def a_you():
    """友：两个好朋友面对面，相邻手臂伸向对方握在一起（照 card_hao 的 clasp：
    交握线起点在肩、与 down 臂融合，握手圆压住 down 手——每人只见两条手臂）。"""
    s = 0.88
    y = 444
    sho = y - 168 * s
    clasp = (L(310 + 44 * s, sho + 6 * s, 372, 348, SKIN, 26)
             + L(450 - 44 * s, sho + 6 * s, 388, 348, SKIN, 26)
             + C(372, 348, 12.5, SKIN) + C(388, 348, 12.5, SKIN))
    return ground(380, 452, 255, 22) + wrap(
        kid(310, y, s=s, face="smile", shirt=BLUE, look=(1, 0)),
        kid(450, y, s=s, face="smile", shirt=PINK, look=(-1, 0)),
        clasp,
        heart(380, 140, 22, RED), heart(346, 162, 10, RED), heart(414, 162, 10, RED))


def a_bao():
    """宝：爸爸妈妈从两边探头看、爱心飘着、柔光打在中间的小宝宝——全家的宝（氛围烘托）。"""
    glow = C(380, 300, 168, "#fdeaa0", 0.5)
    dad = wrap(
        R(88, 208, 152, 72, 30, BLUE),
        C(163, 158, 58, SKIN),
        P("M 106 150 A 58 58 0 0 1 220 150 Q 196 128 163 128 Q 130 128 106 150 Z", HAIR),
        P("M 136 166 Q 146 157 156 166", stroke=INK, w=5),
        P("M 170 166 Q 180 157 190 166", stroke=INK, w=5),
        P("M 148 184 Q 163 194 178 184", stroke=INK, w=5))
    mom = wrap(
        R(520, 208, 152, 72, 30, PINK),
        C(597, 158, 58, SKIN),
        P("M 539 158 A 58 58 0 0 1 655 158 L 652 178 Q 628 142 597 142 "
          "Q 566 142 542 178 Z", HAIR),
        P("M 572 166 Q 582 157 592 166", stroke=INK, w=5),
        P("M 602 166 Q 612 157 622 166", stroke=INK, w=5),
        P("M 582 184 Q 597 194 612 184", stroke=INK, w=5))
    hearts = wrap(heart(380, 156, 26, RED), heart(304, 214, 15, RED), heart(460, 218, 13, RED))
    cushion = wrap(E(380, 436, 158, 30, "#f7d9e0"), E(380, 432, 118, 20, "#fce4ec"))
    baby = wrap(
        E(380, 424, 92, 42, "#f7c14e"),
        C(380, 320, 58, SKIN),
        P("M 322 322 A 58 58 0 0 1 438 322 Q 410 290 380 290 Q 350 290 322 322 Z", HAIR),
        P("M 352 316 Q 360 308 368 316", stroke=INK, w=5),
        P("M 392 316 Q 400 308 408 316", stroke=INK, w=5),
        P("M 366 342 Q 380 354 394 342", stroke=INK, w=5),
        C(344, 334, 13, PINK), C(416, 334, 13, PINK),
        E(328, 424, 24, 15, SKIN), E(432, 424, 24, 15, SKIN))
    spark = wrap(star5(262, 148, 9, SUN_L), star5(502, 140, 9, SUN_L))
    return ground(380, 462, 230, 20) + wrap(glow, dad, mom, hearts, cushion, baby, spark)


def a_shu():
    """叔：胡子茬+polo衫，螺丝刀修翻倒的玩具车——拧螺丝才是「修」。"""
    collar = PG([(354, 266), (380, 284), (346, 292)], WHITE) \
        + PG([(406, 266), (380, 284), (414, 292)], WHITE)
    toolbox = (R(224, 400, 96, 48, 8, "#e8663c") + R(218, 392, 108, 14, 7, "#c94f36")
               + L(258, 392, 280, 364, "#c9cdd1", 8) + C(286, 360, 8, TEAL_D))
    stool = (R(470, 380, 150, 16, 6, WOOD_L)
             + R(486, 396, 14, 54, 4, WOOD_D) + R(590, 396, 14, 54, 4, WOOD_D))
    car = (C(516, 334, 15, INK) + C(576, 334, 15, INK)          # 翻倒朝上的轮子
           + C(516, 334, 6, "#c9cdd1") + C(576, 334, 6, "#c9cdd1")
           + R(484, 344, 124, 40, 10, TEAL)                     # 车底朝上
           + R(494, 352, 104, 10, 4, TEAL_D))
    screwdriver = L(448, 345, 502, 372, "#e8663c", 20) + L(470, 356, 504, 370, "#c9cdd1", 9)
    sparks = (L(514, 352, 524, 342, YEL, 5) + L(524, 372, 536, 370, YEL, 5)
              + L(506, 382, 500, 392, YEL, 5))
    return ground() + toolbox + stool + car \
        + kid(360, 446, s=1.02, shirt="#d9734f", arms="point",
              point_at=(505, 332), face="open", look=(2, 0.3)) \
        + screwdriver + sparks


def a_yi():
    """姨：长发成年女性+拎小包。"""
    bag = wrap(
        P("M 292 354 Q 313 334 334 354", stroke=WOOD_D, w=6),
        R(286, 354, 54, 58, 12, "#e8a13c"), R(286, 354, 54, 16, 8, YEL_D))
    return ground() + _hair_back(380, 446, 1.05) \
        + kid(380, 446, s=1.05, shirt=WBLUE, skirt=True, extra=bag)


def a_shi():
    """师：戴眼镜的老师站在小黑板旁，拿教鞭指着粉笔画的小船。"""
    board = wrap(
        R(414, 132, 292, 200, 14, WOOD_D),
        R(430, 146, 260, 158, 8, "#3f6f5e"),
        # 黑板上的粉笔小船（白色）
        PG([(536, 250), (584, 250), (572, 270), (548, 270)], WHITE),
        PG([(556, 196), (556, 246), (594, 246)], WHITE),
        L(548, 268, 574, 268, WHITE, 4),
        R(424, 336, 272, 14, 6, WOOD),
        R(452, 350, 16, 90, 5, WOOD_D), R(664, 350, 16, 90, 5, WOOD_D))
    pointer = wrap(
        L(397, 265, 455, 248, WOOD_D, 8),
        C(459, 246, 8, WOOD_D))
    return ground(380, 462, 250, 22) + wrap(
        board,
        kid(260, 448, s=1.05, shirt=TEAL_D, glasses=True, bun=True,
            arms="point", point_at=(560, 245), look=(6, -2), extra=pointer))


def a_yilao():
    """医：白大褂穿在身上——领口露出蓝上衣，下摆提到大腿，腿连着鞋。"""
    coat = wrap(
        P("M 330 292 Q 380 276 430 292 L 444 420 Q 445 431 429 432 "
          "L 331 432 Q 315 431 316 420 Z", "#fbfdff"),
        P("M 330 292 Q 380 276 430 292 L 444 420 Q 445 431 429 432 "
          "L 331 432 Q 315 431 316 420 Z", stroke="#c9bfae", w=5),
        L(380, 302, 380, 430, "#c9bfae", 4),
        PG([(380, 296), (368, 298), (380, 318)], BLUE),
        PG([(380, 296), (392, 298), (380, 318)], BLUE),
        L(338, 302, 318, 362, "#fbfdff", 34),
        L(422, 302, 442, 362, "#fbfdff", 34),
    )
    med = wrap(
        P("M 366 292 Q 358 330 376 356", stroke=INK, w=7),
        P("M 394 292 Q 402 330 384 356", stroke=INK, w=7),
        C(380, 362, 16, INK), C(380, 362, 9, "#9cc9e2"),
        C(368, 288, 6, INK), C(392, 288, 6, INK))
    thermo = wrap(
        R(454, 350, 10, 44, 5, "#cfe6f0"),
        L(459, 359, 459, 389, RED, 3),
        L(456, 366, 462, 366, "#7fa9c4", 2),
        C(459, 344, 8, RED))
    return ground() + kid(380, 446, s=1.05, shirt=BLUE) + wrap(coat, med, thermo)


def arts():
    return {
        "人": a_ren(), "你": a_ni(), "我": a_wo(), "他": a_ta(),
        "爸": a_ba(), "妈": a_ma(), "爷": a_ye(), "奶": a_nai(),
        "哥": a_ge(), "姐": a_jie(), "弟": a_di(), "妹": a_mei(),
        "娃": a_wa(), "朋": a_peng(), "友": a_you(), "宝": a_bao(),
        "叔": a_shu(), "姨": a_yi(), "师": a_shi(), "医": a_yilao(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    import 识字卡片_字库 as zk

    GROUP_ID = "rencheng"
    SEEDS = {"日", "山", "水", "手", "吃", "大", "小", "上", "下"}
    expect = []
    for g in zk.GROUPS:
        if g["id"] == GROUP_ID:
            for item in g["chars"]:
                k = item["char"] if isinstance(item, dict) else item
                if k not in SEEDS:
                    expect.append(k)

    chars = [c["char"] for c in GROUP_CARDS]
    art = arts()
    print(f"组「{GROUP_ID}」卡数：{len(GROUP_CARDS)}（字数 {len(''.join(chars))}）")
    print(f"arts 数：{len(art)}")
    ok = chars == expect and set(art) == set(chars) and len(art) == len(GROUP_CARDS)
    print(f"与字库比对（含顺序）：{'一致 ✓' if ok else '不一致 ✗'}")
    if not ok:
        print(f"  缺：{[c for c in expect if c not in chars]}")
        print(f"  多：{[c for c in chars if c not in expect]}")
    for c in GROUP_CARDS:
        assert set(c) == {"char", "pinyin", "tone", "sentence", "say", "chat", "life"}, c["char"]
        assert 4 <= len(c["sentence"]) <= 10, c["char"]
        for f in ("say", "chat", "life"):
            assert len(c[f]) <= 30, (c["char"], f)
    for k, v in art.items():
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        assert "<text" not in v and "<use" not in v and "<defs" not in v and "<image" not in v, k
        assert "href" not in v, k
        assert v.startswith("<ellipse"), k  # 第一笔必须是 ground()
    print("SVG 全部合法 ✓")
    assert ok, "与字库不一致"
    print("自检通过 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '们', 'pinyin': 'men', 'tone': '轻声', 'sentence': '我们都是好朋友。', 'say': '一个、两个、三个，加上们就是一群人。', 'chat': '“我们、你们、他们，都在说谁呀？”', 'life': '指着全家福说：我们一家人。'},
    {'char': '儿', 'pinyin': 'ér', 'tone': '第二声', 'sentence': '小婴儿睡得香。', 'say': '裹在襁褓里的小宝宝就是婴儿。', 'chat': '“你小时候也是小婴儿哟，记得吗？”', 'life': '看他婴儿时的照片说一说。'},
    {'char': '孩', 'pinyin': 'hái', 'tone': '第二声', 'sentence': '小鸭是鸭妈妈的孩子。', 'say': '小鸭跟着鸭妈妈，它是妈妈的孩子。', 'chat': '“你是谁家的孩子呀？”', 'life': '看全家照片说：我是爸爸妈妈的孩子。'},
    {'char': '它', 'pinyin': 'tā', 'tone': '第一声', 'sentence': '它是我的小猫。', 'say': '动物不点名字时，就说它。', 'chat': '“小猫在回头看什么呀？”', 'life': '看见小区小猫说：它在晒太阳。'},
    {'char': '己', 'pinyin': 'jǐ', 'tone': '第三声', 'sentence': '自己的事情自己做。', 'say': '拍拍胸口：自己的事情自己做。', 'chat': '“哪些事你已经能自己做啦？”', 'life': '自己穿鞋，不麻烦妈妈。'},
    {'char': '自', 'pinyin': 'zì', 'tone': '第四声', 'sentence': '这是我自己。', 'say': '指着自己的鼻子说：这是我。', 'chat': '“你自己的小名是什么？”', 'life': '照镜子指一指自己的鼻子。'},
    {'char': '谁', 'pinyin': 'shuí', 'tone': '第二声', 'sentence': '你是谁呀？', 'say': '两个小孩互相指，都在问：是谁？', 'chat': '猜一猜，敲门的是谁呀？', 'life': '玩敲门游戏：猜猜我是谁？'},
]
_arts_mig = {
    '们': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="173.5" y="362.5" width="19.5" height="63.0" rx="9.0" fill="#4a97c9"/><rect x="199.0" y="362.5" width="19.5" height="63.0" rx="9.0" fill="#4a97c9"/><ellipse cx="183.25" cy="437.5" rx="15.75" ry="7.5" fill="#4a3226" opacity="0.85"/><ellipse cx="208.75" cy="437.5" rx="15.75" ry="7.5" fill="#4a3226" opacity="0.85"/><path d="M 154.0 316.0 Q 152.5 374.5 166.0 376.0 L 226.0 376.0 Q 239.5 374.5 238.0 316.0 Q 196 304.0 154.0 316.0 Z" fill="#4fae9f"/><line x1="163.0" y1="320.5" x2="148.0" y2="374.5" stroke="#f8cba4" stroke-width="22.5" stroke-linecap="round"/><circle cx="148.0" cy="374.5" r="9.75" fill="#f8cba4"/><line x1="229.0" y1="320.5" x2="244.0" y2="374.5" stroke="#f8cba4" stroke-width="22.5" stroke-linecap="round"/><circle cx="244.0" cy="374.5" r="9.75" fill="#f8cba4"/><circle cx="152.5" cy="271.0" r="8.25" fill="#f8cba4"/><circle cx="239.5" cy="271.0" r="8.25" fill="#f8cba4"/><circle cx="196" cy="263.5" r="46.5" fill="#f8cba4"/><path d="M 150.43 247.225 Q 154.15 208.63 196 211.42 Q 237.85 208.63 241.57 247.225 Q 221.575 239.32 196 243.97 Q 170.425 239.32 150.43 247.225 Z" fill="#5a3d2b"/><ellipse cx="179.5" cy="257.5" rx="7.5" ry="9.75" fill="#4a3226"/><circle cx="179.5" cy="253.75" r="2.55" fill="#fdfdfa"/><ellipse cx="212.5" cy="257.5" rx="7.5" ry="9.75" fill="#4a3226"/><circle cx="212.5" cy="253.75" r="2.55" fill="#fdfdfa"/><path d="M 169.0 239.32 Q 179.5 234.67000000000002 190.0 238.39" fill="none" stroke="#5a3d2b" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 202.0 238.39 Q 212.5 234.67000000000002 223.0 239.32" fill="none" stroke="#5a3d2b" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 181.0 283.0 Q 196 295.0 211.0 283.0" fill="none" stroke="#4a3226" stroke-width="5.25" stroke-linecap="round" stroke-linejoin="round"/><circle cx="163.0" cy="274.0" r="8.25" fill="#f5a58c" opacity="0.8"/><circle cx="229.0" cy="274.0" r="8.25" fill="#f5a58c" opacity="0.8"/><rect x="356.6" y="363.32" width="20.28" height="65.52" rx="9.36" fill="#4a97c9"/><rect x="383.12" y="363.32" width="20.28" height="65.52" rx="9.36" fill="#4a97c9"/><ellipse cx="366.74" cy="441.32" rx="16.38" ry="7.800000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="393.26" cy="441.32" rx="16.38" ry="7.800000000000001" fill="#4a3226" opacity="0.85"/><path d="M 336.32 314.96000000000004 Q 334.76 375.8 348.8 377.36 L 411.2 377.36 Q 425.24 375.8 423.68 314.96000000000004 Q 380 302.48 336.32 314.96000000000004 Z" fill="#f2b53c"/><line x1="345.68" y1="319.64000000000004" x2="330.08" y2="375.80000000000007" stroke="#f8cba4" stroke-width="23.400000000000002" stroke-linecap="round"/><circle cx="330.08" cy="375.80000000000007" r="10.14" fill="#f8cba4"/><line x1="414.32" y1="319.64000000000004" x2="429.92" y2="375.80000000000007" stroke="#f8cba4" stroke-width="23.400000000000002" stroke-linecap="round"/><circle cx="429.92" cy="375.80000000000007" r="10.14" fill="#f8cba4"/><circle cx="334.76" cy="268.16" r="8.58" fill="#f8cba4"/><circle cx="425.24" cy="268.16" r="8.58" fill="#f8cba4"/><circle cx="380" cy="260.36" r="48.36" fill="#f8cba4"/><path d="M 332.6072 243.43400000000003 Q 336.476 203.2952 380 206.1968 Q 423.524 203.2952 427.3928 243.43400000000003 Q 406.598 235.21280000000002 380 240.04880000000003 Q 353.402 235.21280000000002 332.6072 243.43400000000003 Z" fill="#5a3d2b"/><ellipse cx="362.84" cy="254.12" rx="7.800000000000001" ry="10.14" fill="#4a3226"/><circle cx="362.84" cy="250.22000000000003" r="2.652" fill="#fdfdfa"/><ellipse cx="397.16" cy="254.12" rx="7.800000000000001" ry="10.14" fill="#4a3226"/><circle cx="397.16" cy="250.22000000000003" r="2.652" fill="#fdfdfa"/><path d="M 351.92 235.21280000000002 Q 362.84 230.3768 373.76 234.24560000000002" fill="none" stroke="#5a3d2b" stroke-width="4.68" stroke-linecap="round" stroke-linejoin="round"/><path d="M 386.24 234.24560000000002 Q 397.16 230.3768 408.08 235.21280000000002" fill="none" stroke="#5a3d2b" stroke-width="4.68" stroke-linecap="round" stroke-linejoin="round"/><path d="M 359.72 280.64 Q 380 272.84 400.28 280.64 Q 398.72 300.91999999999996 380 304.03999999999996 Q 361.28 300.91999999999996 359.72 280.64 Z" fill="#6b3325"/><path d="M 369.08 293.12 Q 380 286.88 390.92 293.12 Q 387.02 301.7 380 302.47999999999996 Q 372.98 301.7 369.08 293.12 Z" fill="#f0876f"/><circle cx="345.68" cy="271.28000000000003" r="8.58" fill="#f5a58c" opacity="0.8"/><circle cx="414.32" cy="271.28000000000003" r="8.58" fill="#f5a58c" opacity="0.8"/><rect x="541.5" y="362.5" width="19.5" height="63.0" rx="9.0" fill="#4a97c9"/><rect x="567.0" y="362.5" width="19.5" height="63.0" rx="9.0" fill="#4a97c9"/><ellipse cx="551.25" cy="437.5" rx="15.75" ry="7.5" fill="#4a3226" opacity="0.85"/><ellipse cx="576.75" cy="437.5" rx="15.75" ry="7.5" fill="#4a3226" opacity="0.85"/><path d="M 522.0 316.0 Q 520.5 374.5 534.0 376.0 L 594.0 376.0 Q 607.5 374.5 606.0 316.0 Q 564 304.0 522.0 316.0 Z" fill="#e8663c"/><line x1="531.0" y1="320.5" x2="516.0" y2="374.5" stroke="#f8cba4" stroke-width="22.5" stroke-linecap="round"/><circle cx="516.0" cy="374.5" r="9.75" fill="#f8cba4"/><line x1="597.0" y1="320.5" x2="612.0" y2="374.5" stroke="#f8cba4" stroke-width="22.5" stroke-linecap="round"/><circle cx="612.0" cy="374.5" r="9.75" fill="#f8cba4"/><circle cx="520.5" cy="271.0" r="8.25" fill="#f8cba4"/><circle cx="607.5" cy="271.0" r="8.25" fill="#f8cba4"/><circle cx="564" cy="263.5" r="46.5" fill="#f8cba4"/><path d="M 518.43 247.225 Q 522.15 208.63 564 211.42 Q 605.85 208.63 609.57 247.225 Q 589.575 239.32 564 243.97 Q 538.425 239.32 518.43 247.225 Z" fill="#5a3d2b"/><ellipse cx="547.5" cy="257.5" rx="7.5" ry="9.75" fill="#4a3226"/><circle cx="547.5" cy="253.75" r="2.55" fill="#fdfdfa"/><ellipse cx="580.5" cy="257.5" rx="7.5" ry="9.75" fill="#4a3226"/><circle cx="580.5" cy="253.75" r="2.55" fill="#fdfdfa"/><path d="M 537.0 239.32 Q 547.5 234.67000000000002 558.0 238.39" fill="none" stroke="#5a3d2b" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 570.0 238.39 Q 580.5 234.67000000000002 591.0 239.32" fill="none" stroke="#5a3d2b" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 549.0 283.0 Q 564 295.0 579.0 283.0" fill="none" stroke="#4a3226" stroke-width="5.25" stroke-linecap="round" stroke-linejoin="round"/><circle cx="531.0" cy="274.0" r="8.25" fill="#f5a58c" opacity="0.8"/><circle cx="597.0" cy="274.0" r="8.25" fill="#f5a58c" opacity="0.8"/>',
    '儿': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="380" cy="402" rx="128" ry="62" fill="#f2b53c"/><ellipse cx="380" cy="400" rx="112" ry="52" fill="#f9c95e"/><circle cx="376" cy="298" r="59" fill="#eeb28a"/><circle cx="372" cy="294" r="57" fill="#f8cba4"/><path d="M 348 244 Q 368 226 386 244" fill="none" stroke="#5a3d2b" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M 340 294 Q 350 286 360 294" fill="none" stroke="#4a3226" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 388 294 Q 398 286 408 294" fill="none" stroke="#4a3226" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="326" cy="316" r="11" fill="#f5a58c" opacity="0.8"/><circle cx="420" cy="316" r="11" fill="#f5a58c" opacity="0.8"/><ellipse cx="374" cy="326" rx="10" ry="7" fill="#f0876f"/><path d="M 314 314 Q 374 348 434 314 Q 430 352 374 366 Q 318 352 314 314 Z" fill="#f2b53c"/><path d="M 296 386 Q 378 410 462 386" fill="none" stroke="#d99a2b" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 288 372 Q 324 396 350 428" fill="none" stroke="#d99a2b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 472 372 Q 436 396 410 428" fill="none" stroke="#d99a2b" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="498" cy="396" r="12" fill="#d99a2b"/>',
    '孩': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="245.4" y="306.1" width="34.3" height="110.9" rx="15.8" fill="#4a97c9"/><rect x="290.3" y="306.1" width="34.3" height="110.9" rx="15.8" fill="#4a97c9"/><ellipse cx="262.6" cy="438.1" rx="27.7" ry="13.2" fill="#4a3226" opacity="0.85"/><ellipse cx="307.4" cy="438.1" rx="27.7" ry="13.2" fill="#4a3226" opacity="0.85"/><path d="M 211 224 Q 208 327 232 330 L 338 330 Q 362 327 359 224 Q 285 203 211 224 Z" fill="#2f9e8f"/><line x1="226.9" y1="232.2" x2="192.6" y2="290.2" stroke="#f8cba4" stroke-width="34.3" stroke-linecap="round"/><line x1="343.1" y1="232.2" x2="380.0" y2="285.0" stroke="#f8cba4" stroke-width="34.3" stroke-linecap="round"/><circle cx="208.4" cy="145.0" r="14.5" fill="#f8cba4"/><circle cx="361.6" cy="145.0" r="14.5" fill="#f8cba4"/><circle cx="285.0" cy="131.8" r="81.8" fill="#f8cba4"/><path d="M 205 103 Q 211 35 285 40 Q 359 35 365 103 Q 330 89 285 97 Q 240 89 205 103 Z" fill="#5a3d2b"/><ellipse cx="256.0" cy="121.3" rx="13.2" ry="17.2" fill="#4a3226"/><circle cx="262.0" cy="114.7" r="4.5" fill="#fdfdfa"/><ellipse cx="314.0" cy="121.3" rx="13.2" ry="17.2" fill="#4a3226"/><circle cx="320.0" cy="114.7" r="4.5" fill="#fdfdfa"/><path d="M 259 158 Q 285 148 311 158 Q 285 166 259 158 Z" fill="#d9d0c5"/><path d="M 259 166 Q 285 185 311 166" fill="none" stroke="#4a3226" stroke-width="7.9" stroke-linecap="round"/><circle cx="226.9" cy="150.3" r="14.5" fill="#f5a58c" opacity="0.8"/><circle cx="343.1" cy="150.3" r="14.5" fill="#f5a58c" opacity="0.8"/><rect x="419.4" y="378.3" width="16.1" height="52.1" rx="7.4" fill="#4a97c9"/><rect x="440.5" y="378.3" width="16.1" height="52.1" rx="7.4" fill="#4a97c9"/><ellipse cx="427.5" cy="440.3" rx="13.0" ry="6.2" fill="#4a3226" opacity="0.85"/><ellipse cx="448.5" cy="440.3" rx="13.0" ry="6.2" fill="#4a3226" opacity="0.85"/><path d="M 403 340 Q 402 388 413 389 L 463 389 Q 474 388 473 340 Q 438 330 403 340 Z" fill="#e8663c"/><line x1="410.7" y1="343.6" x2="394.6" y2="370.8" stroke="#f8cba4" stroke-width="16.1" stroke-linecap="round"/><line x1="465.3" y1="343.6" x2="482.6" y2="368.4" stroke="#f8cba4" stroke-width="16.1" stroke-linecap="round"/><circle cx="402.0" cy="302.6" r="6.8" fill="#f8cba4"/><circle cx="474.0" cy="302.6" r="6.8" fill="#f8cba4"/><circle cx="438.0" cy="296.4" r="38.4" fill="#f8cba4"/><path d="M 400 283 Q 403 251 438 253 Q 473 251 476 283 Q 459 276 438 280 Q 417 276 400 283 Z" fill="#5a3d2b"/><ellipse cx="424.4" cy="291.5" rx="6.2" ry="8.1" fill="#4a3226"/><circle cx="430.4" cy="288.4" r="2.1" fill="#fdfdfa"/><ellipse cx="451.6" cy="291.5" rx="6.2" ry="8.1" fill="#4a3226"/><circle cx="457.6" cy="288.4" r="2.1" fill="#fdfdfa"/><path d="M 426 313 Q 438 321 450 313" fill="none" stroke="#4a3226" stroke-width="3.7" stroke-linecap="round"/><circle cx="410.7" cy="305.1" r="6.8" fill="#f5a58c" opacity="0.8"/><circle cx="465.3" cy="305.1" r="6.8" fill="#f5a58c" opacity="0.8"/><line x1="410" y1="347" x2="381" y2="330" stroke="#f8cba4" stroke-width="13" stroke-linecap="round"/><circle cx="378" cy="329" r="9" fill="#f8cba4"/><line x1="471" y1="388" x2="497" y2="302" stroke="#9aa2ab" stroke-width="3"/><circle cx="502" cy="276" r="21" fill="#e8663c"/><ellipse cx="495" cy="268" rx="7" ry="5" fill="#ffffff" opacity="0.7"/>',
    '它': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><path d="M 468 404 Q 546 398 540 322 Q 536 278 500 264" fill="none" stroke="#a8a094" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/><circle cx="500" cy="262" r="11" fill="#8f887c"/><ellipse cx="400" cy="388" rx="76" ry="58" fill="#a8a094"/><ellipse cx="358" cy="440" rx="20" ry="10" fill="#c9c2b4"/><ellipse cx="430" cy="440" rx="20" ry="10" fill="#c9c2b4"/><polygon points="284,258 274,214 314,240" fill="#a8a094"/><polygon points="292,248 288,226 306,240" fill="#f5a58c"/><polygon points="330,238 350,200 368,242" fill="#a8a094"/><polygon points="338,232 350,212 358,234" fill="#f5a58c"/><circle cx="318" cy="286" r="47" fill="#a8a094"/><ellipse cx="372" cy="300" rx="13" ry="11" fill="#a8a094"/><polygon points="376,294 388,297 378,304" fill="#8f887c"/><circle cx="334" cy="276" r="5.5" fill="#4a3226"/><circle cx="358" cy="284" r="5.5" fill="#4a3226"/><circle cx="336" cy="274" r="1.7" fill="#fdfdfa"/><circle cx="360" cy="282" r="1.7" fill="#fdfdfa"/><path d="M 366 310 Q 374 317 383 311" fill="none" stroke="#4a3226" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><line x1="390" y1="296" x2="422" y2="290" stroke="#4a3226" stroke-width="3" stroke-linecap="round"/><line x1="390" y1="308" x2="422" y2="310" stroke="#4a3226" stroke-width="3" stroke-linecap="round"/><circle cx="330" cy="306" r="8" fill="#f5a58c" opacity="0.7"/>',
    '己': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="380" cy="295" rx="148" ry="172" fill="#fdf0c2"/><rect x="347.6" y="331.52" width="28.080000000000002" height="90.72" rx="12.96" fill="#4a97c9"/><rect x="384.32" y="331.52" width="28.080000000000002" height="90.72" rx="12.96" fill="#4a97c9"/><ellipse cx="361.64" cy="439.52" rx="22.68" ry="10.8" fill="#4a3226" opacity="0.85"/><ellipse cx="398.36" cy="439.52" rx="22.68" ry="10.8" fill="#4a3226" opacity="0.85"/><path d="M 319.52 264.56 Q 317.36 348.8 336.8 350.96 L 423.2 350.96 Q 442.64 348.8 440.48 264.56 Q 380 247.28 319.52 264.56 Z" fill="#5fa8d8"/><line x1="332.48" y1="271.04" x2="310.88" y2="348.8" stroke="#f8cba4" stroke-width="32.400000000000006" stroke-linecap="round"/><circle cx="310.88" cy="348.8" r="14.040000000000001" fill="#f8cba4"/><line x1="427.52" y1="271.04" x2="449.12" y2="348.8" stroke="#f8cba4" stroke-width="32.400000000000006" stroke-linecap="round"/><circle cx="449.12" cy="348.8" r="14.040000000000001" fill="#f8cba4"/><circle cx="317.36" cy="199.76000000000002" r="11.88" fill="#f8cba4"/><circle cx="442.64" cy="199.76000000000002" r="11.88" fill="#f8cba4"/><circle cx="380" cy="188.96" r="66.96000000000001" fill="#f8cba4"/><path d="M 314.37919999999997 165.524 Q 319.736 109.9472 380 113.9648 Q 440.264 109.9472 445.62080000000003 165.524 Q 416.82800000000003 154.1408 380 160.8368 Q 343.17199999999997 154.1408 314.37919999999997 165.524 Z" fill="#5a3d2b"/><ellipse cx="356.24" cy="180.32" rx="10.8" ry="14.040000000000001" fill="#4a3226"/><circle cx="356.24" cy="174.92000000000002" r="3.672" fill="#fdfdfa"/><ellipse cx="403.76" cy="180.32" rx="10.8" ry="14.040000000000001" fill="#4a3226"/><circle cx="403.76" cy="174.92000000000002" r="3.672" fill="#fdfdfa"/><path d="M 341.12 154.1408 Q 356.24 147.4448 371.36 152.8016" fill="none" stroke="#5a3d2b" stroke-width="6.48" stroke-linecap="round" stroke-linejoin="round"/><path d="M 388.64 152.8016 Q 403.76 147.4448 418.88 154.1408" fill="none" stroke="#5a3d2b" stroke-width="6.48" stroke-linecap="round" stroke-linejoin="round"/><path d="M 358.4 217.04000000000002 Q 380 234.32000000000002 401.6 217.04000000000002" fill="none" stroke="#4a3226" stroke-width="7.5600000000000005" stroke-linecap="round" stroke-linejoin="round"/><circle cx="332.48" cy="204.08" r="11.88" fill="#f5a58c" opacity="0.8"/><circle cx="427.52" cy="204.08" r="11.88" fill="#f5a58c" opacity="0.8"/><path d="M 560 330 Q 640 150 470 118" fill="none" stroke="#4fae9f" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><polygon points="452,112 492,108 470,142" fill="#4fae9f"/>',
    '自': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="328.4" y="365.68" width="18.72" height="60.48" rx="8.64" fill="#4a97c9"/><rect x="352.88" y="365.68" width="18.72" height="60.48" rx="8.64" fill="#4a97c9"/><ellipse cx="337.76" cy="437.68" rx="15.12" ry="7.199999999999999" fill="#4a3226" opacity="0.85"/><ellipse cx="362.24" cy="437.68" rx="15.12" ry="7.199999999999999" fill="#4a3226" opacity="0.85"/><path d="M 309.68 321.04 Q 308.24 377.2 321.2 378.64 L 378.8 378.64 Q 391.76 377.2 390.32 321.04 Q 350 309.52000000000004 309.68 321.04 Z" fill="#5fa8d8"/><line x1="318.32" y1="325.36" x2="289.52" y2="274.96000000000004" stroke="#f8cba4" stroke-width="21.599999999999998" stroke-linecap="round"/><circle cx="289.52" cy="274.96000000000004" r="9.36" fill="#f8cba4"/><line x1="381.68" y1="325.36" x2="410.48" y2="274.96000000000004" stroke="#f8cba4" stroke-width="21.599999999999998" stroke-linecap="round"/><circle cx="410.48" cy="274.96000000000004" r="9.36" fill="#f8cba4"/><circle cx="308.24" cy="277.84000000000003" r="7.92" fill="#f8cba4"/><circle cx="391.76" cy="277.84000000000003" r="7.92" fill="#f8cba4"/><circle cx="350" cy="270.64000000000004" r="44.64" fill="#f8cba4"/><path d="M 306.2528 255.01600000000005 Q 309.824 217.96480000000005 350 220.64320000000006 Q 390.176 217.96480000000005 393.7472 255.01600000000005 Q 374.552 247.42720000000006 350 251.89120000000005 Q 325.448 247.42720000000006 306.2528 255.01600000000005 Z" fill="#5a3d2b"/><ellipse cx="334.16" cy="264.88000000000005" rx="7.199999999999999" ry="9.36" fill="#4a3226"/><circle cx="335.024" cy="260.56" r="2.448" fill="#fdfdfa"/><ellipse cx="365.84" cy="264.88000000000005" rx="7.199999999999999" ry="9.36" fill="#4a3226"/><circle cx="366.70399999999995" cy="260.56" r="2.448" fill="#fdfdfa"/><path d="M 324.08 247.42720000000003 Q 334.16 242.96320000000003 344.24 246.53440000000003" fill="none" stroke="#5a3d2b" stroke-width="4.32" stroke-linecap="round" stroke-linejoin="round"/><path d="M 355.76 246.53440000000003 Q 365.84 242.96320000000003 375.92 247.42720000000003" fill="none" stroke="#5a3d2b" stroke-width="4.32" stroke-linecap="round" stroke-linejoin="round"/><path d="M 335.6 289.36 Q 350 300.88 364.4 289.36" fill="none" stroke="#4a3226" stroke-width="5.04" stroke-linecap="round" stroke-linejoin="round"/><circle cx="318.32" cy="280.72" r="7.92" fill="#f5a58c" opacity="0.8"/><circle cx="381.68" cy="280.72" r="7.92" fill="#f5a58c" opacity="0.8"/><rect x="398" y="242" width="24" height="46" rx="11" fill="#b57b44"/><circle cx="422" cy="180" r="68" fill="#f2b53c"/><circle cx="422" cy="180" r="55" fill="#eef6fa"/><circle cx="422" cy="187" r="35" fill="#f8cba4"/><path d="M 392 176 Q 396 145 422 143 Q 448 145 452 176 Q 437 168 422 172 Q 407 168 392 176 Z" fill="#5a3d2b"/><ellipse cx="409" cy="188" rx="5.5" ry="7" fill="#4a3226"/><circle cx="410" cy="185" r="2" fill="#fdfdfa"/><ellipse cx="435" cy="188" rx="5.5" ry="7" fill="#4a3226"/><circle cx="436" cy="185" r="2" fill="#fdfdfa"/><path d="M 411 205 Q 422 213 433 205" fill="none" stroke="#4a3226" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="400" cy="199" r="6" fill="#f5a58c" opacity="0.8"/><circle cx="444" cy="199" r="6" fill="#f5a58c" opacity="0.8"/><ellipse cx="390" cy="150" rx="8" ry="14" fill="#fdfdfa" opacity="0.7"/><polygon points="506,118 512,126 506,134 500,126" fill="#f9c95e"/>',
    '谁': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="247.4" y="351.08" width="21.32" height="68.88" rx="9.84" fill="#4a97c9"/><rect x="275.28" y="351.08" width="21.32" height="68.88" rx="9.84" fill="#4a97c9"/><ellipse cx="258.06" cy="433.08" rx="17.22" ry="8.2" fill="#4a3226" opacity="0.85"/><ellipse cx="285.94" cy="433.08" rx="17.22" ry="8.2" fill="#4a3226" opacity="0.85"/><path d="M 226.08 300.24 Q 224.44 364.2 239.2 365.84 L 304.8 365.84 Q 319.56 364.2 317.92 300.24 Q 272 287.12 226.08 300.24 Z" fill="#5fa8d8"/><g transform="rotate(8 308.08 305.16)"><line x1="308.08" y1="305.16" x2="378.59999999999997" y2="305.16" stroke="#f8cba4" stroke-width="24.599999999999998" stroke-linecap="round"/><circle cx="380.24" cy="305.16" r="10.66" fill="#f8cba4"/></g><line x1="235.92000000000002" y1="305.16" x2="217.88" y2="362.56" stroke="#f8cba4" stroke-width="24.599999999999998" stroke-linecap="round"/><circle cx="217.88" cy="362.56" r="10.66" fill="#f8cba4"/><circle cx="224.44" cy="251.04" r="9.02" fill="#f8cba4"/><circle cx="319.56" cy="251.04" r="9.02" fill="#f8cba4"/><circle cx="272" cy="242.84" r="50.839999999999996" fill="#f8cba4"/><path d="M 222.17680000000001 225.046 Q 226.244 182.8488 272 185.8992 Q 317.756 182.8488 321.8232 225.046 Q 299.962 216.4032 272 221.4872 Q 244.038 216.4032 222.17680000000001 225.046 Z" fill="#5a3d2b"/><ellipse cx="253.96" cy="236.28" rx="8.2" ry="10.66" fill="#4a3226"/><circle cx="255.6" cy="232.18" r="2.788" fill="#fdfdfa"/><ellipse cx="290.04" cy="236.28" rx="8.2" ry="10.66" fill="#4a3226"/><circle cx="291.68" cy="232.18" r="2.788" fill="#fdfdfa"/><path d="M 242.48 216.4032 Q 253.96 211.3192 265.44 215.3864" fill="none" stroke="#5a3d2b" stroke-width="4.92" stroke-linecap="round" stroke-linejoin="round"/><path d="M 278.56 215.3864 Q 290.04 211.3192 301.52 216.4032" fill="none" stroke="#5a3d2b" stroke-width="4.92" stroke-linecap="round" stroke-linejoin="round"/><path d="M 255.6 264.16 Q 272 277.28000000000003 288.4 264.16" fill="none" stroke="#4a3226" stroke-width="5.739999999999999" stroke-linecap="round" stroke-linejoin="round"/><circle cx="235.92000000000002" cy="254.32" r="9.02" fill="#f5a58c" opacity="0.8"/><circle cx="308.08" cy="254.32" r="9.02" fill="#f5a58c" opacity="0.8"/><rect x="463.4" y="351.08" width="21.32" height="68.88" rx="9.84" fill="#4a97c9"/><rect x="491.28" y="351.08" width="21.32" height="68.88" rx="9.84" fill="#4a97c9"/><ellipse cx="474.06" cy="433.08" rx="17.22" ry="8.2" fill="#4a3226" opacity="0.85"/><ellipse cx="501.94" cy="433.08" rx="17.22" ry="8.2" fill="#4a3226" opacity="0.85"/><path d="M 442.08 300.24 Q 440.44 364.2 455.2 365.84 L 520.8 365.84 Q 535.56 364.2 533.92 300.24 Q 488 287.12 442.08 300.24 Z" fill="#5fa8d8"/><g transform="rotate(175 524.08 305.16)"><line x1="524.08" y1="305.16" x2="594.6" y2="305.16" stroke="#f8cba4" stroke-width="24.599999999999998" stroke-linecap="round"/><circle cx="596.24" cy="305.16" r="10.66" fill="#f8cba4"/></g><line x1="451.92" y1="305.16" x2="433.88" y2="362.56" stroke="#f8cba4" stroke-width="24.599999999999998" stroke-linecap="round"/><circle cx="433.88" cy="362.56" r="10.66" fill="#f8cba4"/><circle cx="440.44" cy="251.04" r="9.02" fill="#f8cba4"/><circle cx="535.56" cy="251.04" r="9.02" fill="#f8cba4"/><circle cx="488" cy="242.84" r="50.839999999999996" fill="#f8cba4"/><path d="M 438.1768 225.046 Q 442.244 182.8488 488 185.8992 Q 533.756 182.8488 537.8232 225.046 Q 515.962 216.4032 488 221.4872 Q 460.038 216.4032 438.1768 225.046 Z" fill="#5a3d2b"/><ellipse cx="469.96" cy="236.28" rx="8.2" ry="10.66" fill="#4a3226"/><circle cx="468.32" cy="232.18" r="2.788" fill="#fdfdfa"/><ellipse cx="506.04" cy="236.28" rx="8.2" ry="10.66" fill="#4a3226"/><circle cx="504.40000000000003" cy="232.18" r="2.788" fill="#fdfdfa"/><path d="M 458.48 216.4032 Q 469.96 211.3192 481.44 215.3864" fill="none" stroke="#5a3d2b" stroke-width="4.92" stroke-linecap="round" stroke-linejoin="round"/><path d="M 494.56 215.3864 Q 506.04 211.3192 517.52 216.4032" fill="none" stroke="#5a3d2b" stroke-width="4.92" stroke-linecap="round" stroke-linejoin="round"/><path d="M 471.6 264.16 Q 488 277.28000000000003 504.4 264.16" fill="none" stroke="#4a3226" stroke-width="5.739999999999999" stroke-linecap="round" stroke-linejoin="round"/><circle cx="451.92" cy="254.32" r="9.02" fill="#f5a58c" opacity="0.8"/><circle cx="524.08" cy="254.32" r="9.02" fill="#f5a58c" opacity="0.8"/><path d="M 284 112.3 Q 289.1 71.5 318 71.5 Q 346.9 71.5 348.6 108.9 Q 348.6 137.8 318 149.7 L 318 168.4" fill="none" stroke="#4a3226" stroke-width="10.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="318" cy="188.8" r="6.46" fill="#4a3226"/><path d="M 408 112.3 Q 413.1 71.5 442 71.5 Q 470.9 71.5 472.6 108.9 Q 472.6 137.8 442 149.7 L 442 168.4" fill="none" stroke="#4a3226" stroke-width="10.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="442" cy="188.8" r="6.46" fill="#4a3226"/>',
}


def a_hai_fixed():
    """孩：用鸭妈妈和小鸭表达亲子关系，完全避开人物肢体。"""
    def duck(cx, cy, s):
        tail = P(
            f"M {cx-68*s} {cy-12*s} L {cx-108*s} {cy-42*s} L {cx-94*s} {cy+8*s} Z",
            YEL,
        )
        body = E(cx, cy, 82 * s, 48 * s, YEL)
        wing = E(cx - 12 * s, cy + 2 * s, 39 * s, 25 * s, YEL_D)
        neck = P(
            f"M {cx+42*s} {cy-30*s} Q {cx+52*s} {cy-64*s} {cx+68*s} {cy-68*s} "
            f"L {cx+82*s} {cy-22*s} Z",
            YEL,
        )
        head = C(cx + 69 * s, cy - 57 * s, 36 * s, YEL)
        beak = P(
            f"M {cx+99*s} {cy-57*s} L {cx+130*s} {cy-45*s} L {cx+99*s} {cy-37*s} Z",
            RED,
        )
        eye = wrap(C(cx + 78 * s, cy - 66 * s, 5.5 * s, INK),
                   C(cx + 80 * s, cy - 68 * s, 1.8 * s, WHITE))
        return wrap(tail, body, wing, neck, head, beak, eye)

    water = wrap(
        E(380, 421, 270, 30, WBLUE, 0.9),
        P("M 126 408 Q 180 392 234 408 T 342 408 T 450 408 T 558 408 T 634 408",
          stroke=WHITE, w=7),
    )
    mother = duck(292, 344, 1.08)
    duckling = duck(520, 381, 0.62)
    return wrap(water, mother, duckling, heart(447, 245, 17, RED))


_arts_mig["孩"] = a_hai_fixed()
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
