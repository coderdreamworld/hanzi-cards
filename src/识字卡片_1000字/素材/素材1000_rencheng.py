#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""人称组新增 21 卡插画与文案（1000 字批次 B7）。

字表：婶伯客姥农兵警护司员姑舅婆娘父母伙伴孙咱您
（legacy ../识字卡片_素材_rencheng.py 已有 27 卡 人你我他爸妈爷奶哥姐弟妹娃
朋友宝叔姨师医+们儿孩它己自谁，本文件只做增量，不重复）。

与 legacy 27 卡错姿态主色：legacy 是 站立青衣(人)/指点(你我他)/牵手散步蓝爸/
横抱襁褓粉妈/白胡拐杖棕爷/白发白髻青奶/红帽水蓝哥/黄裙双辫姐/坐地绿弟/
坐地抱瓶粉妹/襁褓黄娃/举手上红绿朋/握手蓝粉友/全家宝/修车砖红叔/拎包水蓝姨/
黑板深青师/白大褂蓝医。本批全部换道具与主色：
紫衣婶+菜篮 / 棕衣伯+大西瓜 / 敲门橙客+礼袋 / 灰发织毛衣姥 / 蓝衣草帽锄头农 /
军绿吹号兵 / 藏青警+信号灯 / 白衣护士帽针筒 / 青衣司机+方向盘 / 柜台店员 /
粉衣围裙姑姑+饼干盘 / 绿衣公文包舅 / 栗红摇扇婆 / 橙衣围裙娘+汤锅 /
琥珀父抱娃坐手臂 / 蓝母竖抱襁褓 / 双娃抬箱 / 红蓝并肩散步 / 陶红爷爷牵孙 /
三娃拉手咱 / 绿衣让座您。

一眼可辨约定（主控硬规则）：全部 kid() 组件+标志道具，身份不靠衣服发型——
农=草帽+锄头+禾苗、兵=军帽红星+军号、警=警帽+白手套指挥信号灯、护=护士帽红十字+
针筒、司=大方向盘、员=柜台+果蔬、父=把娃举在手臂上、母=竖抱襁褓低头看、
孙=爷爷灰发胡子眼镜拐杖牵孙、咱=三娃拉手同行、您=让座（指空长椅）。
问号/蒸汽/气流弧为语义符号。相邻卡轮廓+主色错开，圆润友好无恐怖无武器。
"""
import importlib.util
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
PURPLE = "#9a6bb0"      # 婶
BROWN_U = "#a9743f"     # 伯
GUEST = "#e8923c"       # 客
ROSE = "#c96f8a"        # 姥
OLIVE = "#8a9e5c"       # 备用
MILG, MILG_D = "#6b7f4e", "#4e5e33"   # 兵军绿
NAVY = "#3d5a80"        # 警
MAROON = "#a05252"      # 婆
AMBER = "#d9822b"       # 父
GRAY, GRAY_D, LGRAY = "#c9cdd1", "#9aa2ab", "#d8d2c2"
GRAYHAIR = "#cfc8bc"

GROUP_CARDS = [
    {"char": "婶", "pinyin": "shěn", "tone": "第三声",
     "sentence": "婶婶拎着菜篮来。",
     "say": "拎菜篮的阿姨是婶婶。",
     "chat": "婶婶篮子里装的什么呀？",
     "life": "见到婶婶大声问个好。"},
    {"char": "伯", "pinyin": "bó", "tone": "第二声",
     "sentence": "伯伯抱来大西瓜。",
     "say": "爸爸的哥哥是伯伯。",
     "chat": "西瓜是甜的还是咸的？",
     "life": "夏天和伯伯分西瓜吃。"},
    {"char": "客", "pinyin": "kè", "tone": "第四声",
     "sentence": "客人来了，咚咚咚。",
     "say": "来家里做客的是客人。",
     "chat": "叮咚！猜猜是谁来了？",
     "life": "客人来了说声您好。"},
    {"char": "姥", "pinyin": "lǎo", "tone": "第三声",
     "sentence": "姥姥织毛衣真好看。",
     "say": "妈妈的妈妈是姥姥。",
     "chat": "姥姥最拿手的是什么？",
     "life": "给姥姥捶捶背吧。"},
    {"char": "农", "pinyin": "nóng", "tone": "第二声",
     "sentence": "农民下田种稻子。",
     "say": "戴草帽拿锄头的是农民。",
     "chat": "稻子长大变成什么呀？",
     "life": "吃饭时不浪费粮食。"},
    {"char": "兵", "pinyin": "bīng", "tone": "第一声",
     "sentence": "小兵吹起小军号。",
     "say": "戴军帽的是解放军战士。",
     "chat": "军号声在叫谁起床呀？",
     "life": "学小兵挺胸站站好。"},
    {"char": "警", "pinyin": "jǐng", "tone": "第三声",
     "sentence": "警察指挥马路车。",
     "say": "戴警帽的是交通警察。",
     "chat": "红灯亮了该怎么办呀？",
     "life": "过马路跟紧大人走。"},
    {"char": "护", "pinyin": "hù", "tone": "第四声",
     "sentence": "护士打针轻轻的。",
     "say": "戴护士帽的是护士。",
     "chat": "打针时你可以怎么说？",
     "life": "生病看医生别害怕。"},
    {"char": "司", "pinyin": "sī", "tone": "第一声",
     "sentence": "司机手握方向盘。",
     "say": "开车的人叫司机。",
     "chat": "坐车时要系好什么呀？",
     "life": "下车时对司机说谢谢。"},
    {"char": "员", "pinyin": "yuán", "tone": "第二声",
     "sentence": "店员阿姨对我笑。",
     "say": "柜台里帮忙的是店员。",
     "chat": "买完东西要说什么呀？",
     "life": "接过东西说声谢谢。"},
    {"char": "姑", "pinyin": "gū", "tone": "第一声",
     "sentence": "姑姑烤了小饼干。",
     "say": "爸爸的姐妹是姑姑。",
     "chat": "饼干是什么形状的呀？",
     "life": "和姑姑分享小饼干。"},
    {"char": "舅", "pinyin": "jiù", "tone": "第四声",
     "sentence": "舅舅提包来看我。",
     "say": "妈妈的兄弟是舅舅。",
     "chat": "舅舅的包里有什么呀？",
     "life": "舅舅来了说声好。"},
    {"char": "婆", "pinyin": "pó", "tone": "第二声",
     "sentence": "婆婆摇扇讲故事。",
     "say": "摇着蒲扇的老太太是婆婆。",
     "chat": "婆婆讲过什么故事呀？",
     "life": "给婆婆端一杯水。"},
    {"char": "娘", "pinyin": "niáng", "tone": "第二声",
     "sentence": "娘系围裙做饭香。",
     "say": "系围裙做饭的是娘。",
     "chat": "锅里煮着什么好吃的？",
     "life": "帮娘递一双筷子。"},
    {"char": "父", "pinyin": "fù", "tone": "第四声",
     "sentence": "父亲抱着我哈哈笑。",
     "say": "抱着孩子的爸爸是父亲。",
     "chat": "坐在父亲手臂上像什么？",
     "life": "让父亲抱你转个圈吧。"},
    {"char": "母", "pinyin": "mǔ", "tone": "第三声",
     "sentence": "母亲抱着小宝宝。",
     "say": "妈妈就是你的母亲。",
     "chat": "小宝宝饿了谁喂呀？",
     "life": "抱抱妈妈说声爱你。"},
    {"char": "伙", "pinyin": "huǒ", "tone": "第三声",
     "sentence": "小伙伴一起抬箱子。",
     "say": "一起做事的叫小伙伴。",
     "chat": "箱子里装着什么呀？",
     "life": "和小伙伴一起收玩具。"},
    {"char": "伴", "pinyin": "bàn", "tone": "第四声",
     "sentence": "我和同伴去散步。",
     "say": "肩并肩同行的是同伴。",
     "chat": "散步时你们聊什么呀？",
     "life": "和小伙伴并排走一段。"},
    {"char": "孙", "pinyin": "sūn", "tone": "第一声",
     "sentence": "爷爷带孙孙散步。",
     "say": "儿子的孩子叫孙子。",
     "chat": "爷爷奶奶怎么疼你呀？",
     "life": "出门牵好长辈的手。"},
    {"char": "咱", "pinyin": "zán", "tone": "第二声",
     "sentence": "咱们一起手拉手。",
     "say": "把大家算进来就说咱们。",
     "chat": "咱们全家去哪儿玩好？",
     "life": "喊上小伙伴一起玩。"},
    {"char": "您", "pinyin": "nín", "tone": "第二声",
     "sentence": "您请坐，奶奶。",
     "say": "对长辈说话要用您。",
     "chat": "什么时候要说您呀？",
     "life": "见到长辈说您好。"},
]


def _km(x, y, s, pose="stand"):
    """kid 的关键坐标：头半径 / 肩线 / 头心 / 髋部。"""
    hd = 62 * s
    if pose == "sit":
        hip = y - 78 * s
        sho = hip - 74 * s
    else:
        hip = y - 96 * s
        sho = y - 168 * s
    hcy = sho - 8 * s - hd
    return hd, sho, hcy, hip


# ---------- 各卡插画 ----------
def a_shen():
    """婶：紫衣阿姨手里拎着菜篮（提手顶点正好握在右手里，篮里冒青菜）。"""
    g = ground()
    g += kid(380, 444, s=1.02, bun=True, shirt=PURPLE, look=(0.9, 0.4))
    basket = wrap(
        C(432, 362, 10, GREEN), C(450, 355, 11, "#5e8f52"), C(466, 364, 9, GREEN_L),
        P("M 413 372 Q 445 330 477 372", stroke=WOOD_D, w=7),
        PG([(415, 370), (475, 370), (466, 424), (424, 424)], WOOD),
        PG([(421, 378), (469, 378), (462, 416), (428, 416)], WOOD_L),
        L(419, 388, 471, 388, WOOD_D, 5),
        L(422, 404, 468, 404, WOOD_D, 5),
        C(445, 352, 13, SKIN))
    return g + basket


def a_bo():
    """伯：壮实伯伯（胡子+大一号身形）双手抱大西瓜。"""
    s = 1.12
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    my = sho + 62
    melon = wrap(
        C(x, my + 5, 60, "#5e8f52"),
        C(x - 4, my, 57, "#7fae70"),
        P(f"M {x-30} {my-48} Q {x-44} {my} {x-30} {my+48}", stroke="#5e8f52", w=9),
        P(f"M {x+2} {my-55} Q {x-8} {my} {x+2} {my+55}", stroke="#5e8f52", w=9),
        P(f"M {x+30} {my-48} Q {x+40} {my} {x+30} {my+48}", stroke="#5e8f52", w=9),
        P(f"M {x-12} {my-55} q 9 10 0 18", stroke=WOOD_D, w=7),
        C(x - 22, my - 30, 12, SKIN), C(x + 24, my - 30, 12, SKIN))
    return ground() + kid(x, y, s=s, shirt=BROWN_U, mustache=True,
                          look=(0, 0.6), arms="clap") + melon


def a_ke():
    """客：大木门+拎礼袋的客人伸手敲门（拳头落在门板上+敲击弧）。"""
    door = wrap(
        R(470, 140, 190, 310, 14, WOOD),
        R(490, 160, 150, 270, 10, WOOD_L),
        R(508, 182, 50, 100, 8, "#d8b87e"),
        R(572, 182, 50, 100, 8, "#d8b87e"),
        R(508, 302, 50, 100, 8, "#d8b87e"),
        R(572, 302, 50, 100, 8, "#d8b87e"),
        C(492, 306, 10, YEL_D))
    knock = wrap(
        P("M 516 272 q 12 -10 24 -2", stroke=GRAY, w=5),
        P("M 520 330 q 14 8 26 0", stroke=GRAY, w=5))
    bag = wrap(
        P("M 288 350 Q 302 332 316 350", stroke=WOOD_D, w=6),
        R(276, 350, 60, 62, 10, RED_D),
        R(276, 350, 60, 14, 7, RED),
        heart(306, 384, 10, WHITE))
    g = ground() + door
    g += kid(380, 444, s=1.0, bun=True, shirt=GUEST, arms="point",
             point_at=(520, 300), look=(2, 0.2))
    return g + knock + bag


def a_lao():
    """姥：灰发戴老花镜的姥姥坐着织毛衣——两根棒针尾端正好握在垂下的双手里，
    针尖在胸前交叉，织了一半的毛衣片垂在针下，线团的红线连到毛衣片。"""
    g = ground()
    g += kid(380, 440, s=1.05, pose="sit", bun=True, glasses=True,
             hair_color=GRAYHAIR, shirt=ROSE, look=(0, 0.8))
    yarn = wrap(
        C(242, 416, 36, RED),
        P("M 210 400 Q 230 384 254 396", stroke=WHITE, w=5),
        P("M 214 430 Q 240 414 268 426", stroke=WHITE, w=5),
        P("M 268 414 Q 312 426 352 412", stroke=RED, w=5))
    knit = wrap(
        L(313, 362, 462, 296, GRAY_D, 10),
        L(447, 362, 298, 294, GRAY_D, 10),
        C(468, 293, 8, GRAY), C(292, 291, 8, GRAY),
        R(352, 346, 56, 72, 8, "#f0876f"),
        L(356, 368, 404, 368, "#d96a52", 4),
        L(356, 388, 404, 388, "#d96a52", 4),
        L(356, 406, 404, 406, "#d96a52", 4))
    grips = C(313, 362, 13, SKIN) + C(447, 362, 13, SKIN)
    return g + yarn + knit + grips


def a_nong():
    """农：蓝衣草帽农民拿锄头看禾苗。"""
    g = ground()
    hat = wrap(
        E(380, 168, 98, 20, YEL),
        P("M 322 166 Q 328 116 380 112 Q 432 116 438 166 Q 380 146 322 166 Z", YEL_D),
        R(330, 148, 100, 12, 6, RED_D))
    hoe = wrap(
        L(445, 358, 528, 440, WOOD, 12),
        PG([(516, 432), (556, 448), (540, 464), (504, 448)], GRAY_D))
    sprouts = ""
    for mx in (268, 318):
        sprouts += wrap(
            E(mx, 442, 26, 7, "#a5d0bd"),
            L(mx, 438, mx, 416, "#5e8f52", 5),
            C(mx - 8, 414, 7, GREEN), C(mx + 8, 414, 7, GREEN_L))
    return g + sprouts + kid(380, 444, s=1.05, shirt=BLUE, look=(1, 0.5)) \
        + hat + hoe


def a_bing():
    """兵：军帽红星小兵立正吹军号。"""
    s = 1.0
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    cap = wrap(
        P("M 322 186 Q 326 126 380 122 Q 434 126 438 186 Q 380 166 322 186 Z", MILG_D),
        E(380, 186, 66, 12, "#3c4a28"),
        C(380, 120, 8, "#3c4a28"),
        star5(380, 154, 13, RED))
    bugle = wrap(
        L(392, 310, 386, 242, YEL_D, 16),
        PG([(388, 264), (452, 228), (458, 298)], YEL),
        E(455, 263, 10, 36, "#c98a45"),
        E(455, 263, 5, 26, "#b57b44"),
        C(385, 238, 8, "#b57b44"),
        C(374, 300, 14, SKIN), C(402, 304, 14, SKIN))
    return ground() + kid(x, y, s=s, face="o", shirt=MILG,
                          look=(0.8, -0.3)) + cap + bugle


def a_jing():
    """警：藏青警帽警察白手套指向信号灯。"""
    g = ground()
    light = wrap(
        R(598, 210, 13, 236, 6, GRAY_D),
        E(604, 448, 26, 7, GRAY_D),
        R(576, 122, 58, 130, 12, INK),
        C(605, 148, 16, RED),
        C(605, 188, 16, YEL, 0.55),
        C(605, 228, 16, "#3e9486", 0.45))
    cap = wrap(
        P("M 320 184 Q 326 124 380 120 Q 434 124 440 184 Q 380 164 320 184 Z", "#2f4a6e"),
        E(380, 186, 68, 12, "#1f3247"),
        C(380, 150, 10, YEL))
    g += kid(380, 444, s=1.0, shirt=NAVY, arms="point",
             point_at=(620, 235), look=(2.2, -0.6))
    glove = C(509, 258, 14, WHITE)
    return g + light + cap + glove


def a_hu():
    """护：白裙护士帽（红十字）双手横握大针筒（clap 手位正好落在针筒上）。"""
    s = 1.02
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    cap = wrap(
        R(352, 122, 56, 26, 8, WHITE),
        R(346, 142, 68, 10, 5, "#dfe6ec"),
        R(376, 124, 8, 20, 2, RED),
        R(368, 130, 24, 8, 2, RED))
    syringe = f'<g transform="rotate(14 {x} 306)">' + wrap(
        R(322, 294, 108, 24, 8, "#dff0f8"),
        R(330, 301, 46, 10, 4, RED),
        L(322, 306, 296, 306, GRAY_D, 5),
        R(430, 299, 28, 14, 5, "#cfe6f0"),
        R(456, 290, 10, 32, 4, GRAY_D)) + "</g>"
    drop_tip = drop(288, 318, 6)
    dress = wrap(
        PG([(356, 262), (380, 280), (344, 288)], "#dfe6ec"),
        PG([(404, 262), (380, 280), (416, 288)], "#dfe6ec"),
        C(380, 336, 6, RED), C(380, 368, 6, RED))
    g = ground() + kid(x, y, s=s, bun=True, shirt="#f4f8fb",
                       look=(-0.8, 0.3), arms="clap")
    grips = C(366, 305, 13.5, SKIN) + C(394, 305, 13.5, SKIN)
    return g + dress + syringe + drop_tip + cap + grips


def a_si():
    """司：司机双手握大方向盘——镂空轮辋+三辐条+中毂，双手搭在轮辋左右。"""
    g = ground()
    g += kid(380, 444, s=1.0, shirt=TEAL, look=(0, 0.3))
    wheel = wrap(
        '<g fill="none" stroke="#3a2c22" stroke-width="14">'
        '<circle cx="380" cy="354" r="64"/>'
        '<path d="M 380 354 L 380 290"/>'
        '<path d="M 380 354 L 325 386"/>'
        '<path d="M 380 354 L 435 386"/></g>',
        C(380, 354, 16, YEL_D),
        C(316, 354, 14, SKIN), C(444, 354, 14, SKIN))
    return g + wheel


def a_yuan():
    """员：店员站在柜台后，柜台上摆着水果。"""
    g = ground()
    g += kid(380, 444, s=1.0, bun=True, shirt="#e8a13c", look=(0, 0.3))
    counter = wrap(
        R(232, 362, 296, 80, 12, WOOD_D),
        R(252, 382, 60, 40, 8, WOOD),
        R(378, 382, 60, 40, 8, WOOD),
        R(220, 344, 320, 22, 10, WOOD_L),
        C(300, 327, 17, RED),
        L(300, 310, 300, 302, "#5e8f52", 4),
        E(308, 304, 9, 5, GREEN),
        C(455, 328, 16, "#f5921e"))
    return g + counter


def a_gu():
    """姑：围裙姑姑端着一盘小饼干。"""
    g = ground()
    g += kid(380, 444, s=1.0, bun=True, shirt="#f0876f", look=(0, 0.5))
    apron = wrap(
        P("M 340 300 L 420 300 L 432 400 Q 380 416 328 400 Z", "#fbf0c2"),
        L(348, 282, 344, 304, "#f4e6b8", 9),
        L(412, 282, 416, 304, "#f4e6b8", 9))
    tray = wrap(
        E(380, 348, 88, 18, GRAY),
        E(380, 344, 84, 15, "#dfe3e6"),
        C(352, 330, 15, WOOD), C(384, 324, 16, WOOD), C(414, 332, 14, WOOD),
        C(348, 326, 3, "#8a5a33"), C(358, 336, 3, "#8a5a33"),
        C(380, 320, 3, "#8a5a33"), C(390, 330, 3, "#8a5a33"),
        C(410, 328, 3, "#8a5a33"), C(420, 336, 3, "#8a5a33"),
        C(316, 350, 12, SKIN), C(444, 350, 12, SKIN))
    return g + apron + tray


def a_jiu():
    """舅：绿衣舅舅一手提公文包一手扬手打招呼。"""
    g = ground()
    g += kid(380, 444, s=1.05, shirt="#5e8f52", mustache=True,
             arms="point", point_at=(580, 190), look=(2, -0.6))
    wave = wrap(
        P("M 512 208 q 12 -10 24 -4", stroke=GRAY, w=5),
        P("M 520 236 q 14 6 26 -2", stroke=GRAY, w=5))
    case = wrap(
        P("M 302 352 Q 313 334 324 352", stroke="#6e4526", w=7),
        R(276, 350, 76, 58, 9, "#8a5a33"),
        R(276, 350, 76, 14, 7, "#6e4526"),
        R(304, 372, 18, 10, 3, YEL_D))
    return g + wave + case


def a_po():
    """婆：栗红衣盘发老太坐小凳摇蒲扇。"""
    g = ground()
    g += kid(370, 440, s=1.0, pose="sit", hair_color=GRAYHAIR, bun=True,
             shirt=MAROON, look=(1, 0.2))
    stool = wrap(
        R(300, 372, 140, 18, 8, WOOD_L),
        L(318, 390, 310, 440, WOOD_D, 12),
        L(422, 390, 430, 440, WOOD_D, 12))
    fan = wrap(
        L(434, 366, 458, 324, WOOD_D, 9),
        P("M 456 326 Q 460 258 518 248 Q 552 292 510 332 Q 480 348 456 326 Z", "#ecd2a0"),
        L(474, 322, 484, 268, "#d8b87e", 5),
        L(494, 316, 510, 268, "#d8b87e", 5),
        P("M 462 316 Q 494 322 512 322", stroke="#d8b87e", w=4))
    return g + stool + fan


def a_niang():
    """娘：橙衣围裙娘在锅前搅拌，锅上冒热气。"""
    g = ground()
    g += kid(380, 444, s=1.02, shirt="#e8742a", look=(0, 0.8))
    apron = wrap(
        P("M 340 306 L 420 306 L 430 420 Q 380 434 330 420 Z", "#fbf0c2"),
        L(348, 288, 344, 310, "#f4e6b8", 9),
        L(412, 288, 416, 310, "#f4e6b8", 9))
    pot = wrap(
        R(322, 336, 116, 72, 14, "#8a4a2a"),
        R(314, 328, 132, 18, 9, "#6e3a20"),
        C(310, 344, 9, "#6e3a20"), C(450, 344, 9, "#6e3a20"),
        E(380, 338, 54, 7, "#f7c531"),
        L(394, 308, 386, 344, WOOD, 11),
        C(385, 348, 10, WOOD_D),
        P("M 352 318 q -12 -22 0 -38 q 10 -12 2 -26", stroke=LGRAY, w=7),
        P("M 410 318 q 12 -22 0 -38 q -10 -12 -2 -26", stroke=LGRAY, w=7))
    return g + apron + pot


def a_fu():
    """父：高大父亲把娃托在手臂上（娃臀部落前臂，双脚离地），两人相视而笑。"""
    g = ground(380, 452, 230, 20)
    g += kid(380, 444, s=1.08, shirt=AMBER, arms="hold_right",
             look=(2, -0.6))
    child = kid(464, 378, s=0.55, shirt="#9cc98a", arms="up",
                face="open", look=(-1.5, 0))
    return g + child


def a_mu():
    """母：蓝衣母亲低头看怀里竖抱的襁褓宝宝。"""
    s = 1.05
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    g = ground() + kid(x, y, s=s, bun=True, shirt=BLUE, look=(0, 1.2),
                       arms="clap")
    bundle = wrap(
        R(349, 288, 62, 118, 28, "#f7e6b8"),
        L(352, 330, 408, 330, "#ead9a0", 5),
        L(352, 370, 408, 370, "#ead9a0", 5),
        C(380, 276, 26, SKIN),
        P("M 356 266 Q 366 252 380 252 Q 394 252 404 266 Q 392 260 380 260 Q 368 260 356 266 Z", HAIR),
        P("M 366 276 Q 372 281 378 276", stroke=INK, w=3.5),
        P("M 384 276 Q 390 281 396 276", stroke=INK, w=3.5),
        E(380, 290, 7, 5, "#f0876f"),
        C(360, 288, 6, PINK, 0.8), C(400, 288, 6, PINK, 0.8))
    return g + bundle + heart(456, 250, 16, RED)


def a_huo():
    """伙：两个小伙伴一左一右抬木箱。"""
    g = ground()
    g += kid(275, 444, s=0.85, shirt="#e8a13c", arms="clap",
             face="smile", look=(1, 0))
    g += kid(485, 444, s=0.85, shirt=TEAL, arms="clap",
             face="smile", look=(-1, 0))
    crate = box(380, 296, 190, 112, open_top=False)
    grips = C(287, 330, 12, SKIN) + C(473, 330, 12, SKIN)
    return g + crate + grips


def a_ban():
    """伴：红蓝两个小伙伴并肩散步（摆臂大步走）。"""
    g = ground()
    g += kid(295, 444, s=0.9, pose="walk", arms="swing", shirt=RED,
             face="smile", look=(1, 0))
    g += kid(475, 444, s=0.9, pose="walk", arms="swing", shirt=BLUE,
             face="smile", look=(1, 0))
    return g


def a_sun():
    """孙：灰发眼镜爷爷拄拐杖牵着小孙子散步。"""
    g = ground()
    g += kid(280, 446, s=1.0, pose="walk", arms="hold_right",
             hair_color=GRAYHAIR, mustache=True, glasses=True,
             shirt="#c96f4a", look=(2, 0))
    cane = wrap(
        C(216, 352, 10, WOOD),
        L(216, 356, 208, 440, WOOD, 11),
        E(208, 442, 9, 5, WOOD_D))
    child = kid(420, 446, s=0.62, pose="walk", arms="hold_left",
                shirt="#7cc8bb", face="smile", look=(-1, 0))
    grip = C(361, 358, 12, SKIN)
    return g + cane + child + grip


def a_zan():
    """咱：三个小伙伴站成一排手拉手（垂臂相邻手正好相接，握手圆压住接点）。"""
    g = ground(380, 452, 255, 22)
    g += kid(270, 444, s=0.8, shirt=BLUE, face="smile", look=(1, 0))
    g += kid(380, 444, s=0.8, shirt=YEL, face="open", look=(0, 0))
    g += kid(470, 444, s=0.8, shirt="#7fae70", face="smile", look=(-1, 0))
    link = C(320, 372, 11, SKIN) + C(420, 372, 11, SKIN)
    return g + link


def a_nin():
    """您：绿衣小孩指着中间的空长椅请坐，奶奶从右侧走来——让座。"""
    g = ground()
    bench = wrap(
        R(368, 278, 20, 92, 8, WOOD),
        R(300, 366, 210, 20, 9, WOOD_L),
        R(314, 386, 16, 58, 6, WOOD_D),
        R(486, 386, 16, 58, 6, WOOD_D))
    g += kid(180, 444, s=0.88, shirt="#7fae70", arms="point",
             point_at=(400, 320), look=(2, 0))
    granny = kid(630, 446, s=0.95, pose="walk", hair_color=GRAYHAIR, bun=True,
                 shirt=PURPLE, look=(-1.5, 0.2))
    return g + bench + granny


def arts():
    return {
        "婶": a_shen(), "伯": a_bo(), "客": a_ke(), "姥": a_lao(),
        "农": a_nong(), "兵": a_bing(), "警": a_jing(), "护": a_hu(),
        "司": a_si(), "员": a_yuan(), "姑": a_gu(), "舅": a_jiu(),
        "婆": a_po(), "娘": a_niang(), "父": a_fu(), "母": a_mu(),
        "伙": a_huo(), "伴": a_ban(), "孙": a_sun(), "咱": a_zan(),
        "您": a_nin(),
    }


if __name__ == "__main__":
    LEGACY27 = {"人", "你", "我", "他", "爸", "妈", "爷", "奶", "哥", "姐",
                "弟", "妹", "娃", "朋", "友", "宝", "叔", "姨", "师", "医",
                "它", "们", "儿", "自", "己", "孩", "谁"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "rencheng":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY27]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"人称组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != c["tone"]]
    print(f"拼音/声调：{'与拼音表逐一一致 ✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len(c["sentence"]) - 1 <= 10)]
    miss = [c["char"] for c in GROUP_CARDS if c["char"] not in c["sentence"]]
    print(f"三段长度：{'全部 ≤30 ✓' if not lens else str(lens)}")
    print(f"句长 4–10：{'全部达标 ✓' if not sl else str(sl)}")
    print(f"句含目标字：{'全部 ✓' if not miss else str(miss)}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
        if not v.startswith("<ellipse"):
            bad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
