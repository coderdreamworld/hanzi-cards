#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""社会礼貌组 15 卡插画与文案（1000 字批次 B7，全组新增）。

字表：邻居礼貌请谢错借忙安话助卫夸赞。

一眼可辨约定（主控硬规则）：
邻=隔篱笆挥手的两娃 / 居=两座相邻冒烟的小屋 / 礼=双手捧大红礼盒蝴蝶结 /
貌=戴红帽的娃扬手问好 / 请=娃托茶盘请你喝茶 / 谢=大手递苹果娃双手接 /
错=大红叉+摇头弧 / 借=雨天两个娃共撑一把伞 / 忙=独自搬大木箱擦汗 /
安=安全帽+脚下斑马线 / 话=两个对话气泡+聊天的两娃 / 助=扶起摔倒哭的伙伴 /
卫=戴口罩在水龙头下搓手 / 夸=两只手掌夹着拍手弧（鼓掌夸奖）/
赞=竖起的大拇指+金星。友好互动为主，相邻卡轮廓+主色错开。
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
ORANGE, ORANGE_D = "#e8742a", "#c95f1e"
PURPLE = "#9a6bb0"
MAUVE = "#b57fa0"
FOREST = "#5e8f52"
ROSE = "#c96f8a"
GRAY, GRAY_D, LGRAY = "#c9cdd1", "#9aa2ab", "#d8d2c2"
SKIN_G = "#f7c49c"
SKIN_GD = "#eeb28a"

GROUP_CARDS = [
    {"char": "邻", "pinyin": "lín", "tone": "第二声",
     "sentence": "邻居隔着篱笆笑。",
     "say": "住在隔壁的是邻居。",
     "chat": "你的邻居是谁呀？",
     "life": "见到邻居挥挥手。"},
    {"char": "居", "pinyin": "jū", "tone": "第一声",
     "sentence": "小屋相邻好安居。",
     "say": "住在这里生活叫安居。",
     "chat": "你家住在哪一条街呀？",
     "life": "说说你家的门牌号。"},
    {"char": "礼", "pinyin": "lǐ", "tone": "第三声",
     "sentence": "双手捧上小礼物。",
     "say": "双手递上的心意是礼物。",
     "chat": "收到礼物先说什么呀？",
     "life": "把玩具分享给小伙伴。"},
    {"char": "貌", "pinyin": "mào", "tone": "第四声",
     "sentence": "见面问好有礼貌。",
     "say": "扬手问好是有礼貌。",
     "chat": "见到长辈怎么问好呀？",
     "life": "早上向老师问个好。"},
    {"char": "请", "pinyin": "qǐng", "tone": "第三声",
     "sentence": "端起茶，请您喝。",
     "say": "伸手相邀时说声请。",
     "chat": "你想请谁喝杯热茶呀？",
     "life": "递东西时说一声请。"},
    {"char": "谢", "pinyin": "xiè", "tone": "第四声",
     "sentence": "双手接过说谢谢。",
     "say": "别人帮了你要说谢谢。",
     "chat": "今天要谢谢谁呀？",
     "life": "收到东西大声说谢谢。"},
    {"char": "错", "pinyin": "cuò", "tone": "第四声",
     "sentence": "做错了，改就好。",
     "say": "打上叉叉表示做错了。",
     "chat": "做错了该怎么办呀？",
     "life": "做错事要说对不起。"},
    {"char": "借", "pinyin": "jiè", "tone": "第四声",
     "sentence": "下雨了，伞借给你。",
     "say": "把伞分给同伴是借。",
     "chat": "借了东西要记得什么呀？",
     "life": "借玩具要先问一声。"},
    {"char": "忙", "pinyin": "máng", "tone": "第二声",
     "sentence": "帮着搬箱子真忙。",
     "say": "事情多做不完就叫忙。",
     "chat": "家里最忙的人是谁呀？",
     "life": "给忙碌的家人递杯水。"},
    {"char": "安", "pinyin": "ān", "tone": "第一声",
     "sentence": "戴着安全帽过街。",
     "say": "平平安安没危险是安全。",
     "chat": "过马路前先看什么呀？",
     "life": "坐车系好安全带。"},
    {"char": "话", "pinyin": "huà", "tone": "第四声",
     "sentence": "你一句我一句说话。",
     "say": "气泡里是两个人在说话。",
     "chat": "你最爱和谁说悄悄话？",
     "life": "和家人聊聊今天的事。"},
    {"char": "助", "pinyin": "zhù", "tone": "第四声",
     "sentence": "伸出小手来帮助。",
     "say": "扶起摔倒的伙伴是帮助。",
     "chat": "你怎么帮助过别人呀？",
     "life": "同伴摔倒了扶一把。"},
    {"char": "卫", "pinyin": "wèi", "tone": "第四声",
     "sentence": "勤洗手，讲卫生。",
     "say": "戴口罩勤洗手讲卫生。",
     "chat": "什么时候一定要洗手？",
     "life": "饭前用肥皂搓搓手。"},
    {"char": "夸", "pinyin": "kuā", "tone": "第一声",
     "sentence": "拍拍手，把人夸。",
     "say": "说他做得好就是夸奖。",
     "chat": "你最想夸家里的谁呀？",
     "life": "今天夸夸一位家人。"},
    {"char": "赞", "pinyin": "zàn", "tone": "第四声",
     "sentence": "为他点个大大的赞。",
     "say": "竖起大拇指就是点赞。",
     "chat": "你想给谁点个赞呀？",
     "life": "谢谢家人时点个赞。"},
]


def a_lin():
    """邻：木篱笆隔开两家，两娃隔栏挥手问好。"""
    g = ground()
    pickets = ""
    for px in (326, 354, 382, 410, 438):
        pickets += R(px, 296, 16, 136, 6, WOOD_L)
    fence = pickets + R(300, 314, 170, 12, 5, WOOD) + R(300, 374, 170, 12, 5, WOOD) \
        + R(292, 288, 18, 146, 6, WOOD_D) + R(452, 288, 18, 146, 6, WOOD_D)
    g += fence
    g += tree_round(110, 438, 0.55)
    g += flower5(662, 410, 13)
    g += kid(220, 444, s=0.85, shirt="#7fae70", arms="up", face="smile",
             look=(1, 0))
    g += kid(548, 444, s=0.85, shirt=ORANGE, arms="up", face="smile",
             look=(-1, 0))
    return g


def a_ju():
    """居：两座相邻的小屋，烟囱都冒着炊烟。"""
    g = ground()
    left = wrap(
        R(170, 250, 190, 172, 10, YEL),
        PG([(152, 254), (378, 254), (265, 178)], "#e8663c"),
        R(330, 196, 26, 48, 4, WOOD_D),
        C(343, 172, 12, LGRAY), C(354, 148, 9, "#e3d5bd"), C(366, 130, 6, "#e3d5bd"),
        R(240, 344, 50, 78, 6, WOOD_D),
        C(206, 300, 17, WBLUE), C(330, 300, 17, WBLUE))
    right = wrap(
        R(430, 270, 172, 152, 10, "#7cc8bb"),
        PG([(412, 274), (620, 274), (516, 202)], TEAL_D),
        R(576, 220, 22, 44, 4, WOOD_D),
        C(587, 196, 10, LGRAY), C(596, 176, 8, "#e3d5bd"),
        R(486, 348, 44, 74, 6, WOOD_D),
        C(556, 318, 15, WBLUE))
    return g + left + right


def a_li():
    """礼：紫衣娃娃双手捧着系蝴蝶结的大红礼盒。"""
    g = ground()
    g += kid(380, 444, s=1.0, shirt=PURPLE, look=(0, 0.5))
    gift = wrap(
        R(300, 292, 160, 118, 14, RED),
        R(288, 268, 184, 42, 12, RED_D),
        R(368, 268, 24, 142, 0, YEL),
        R(288, 284, 184, 18, 0, YEL),
        E(350, 254, 28, 17, YEL), E(410, 254, 28, 17, YEL),
        C(380, 258, 12, YEL_D),
        C(342, 312, 13, SKIN), C(418, 312, 13, SKIN))
    return g + gift + star5(258, 200, 10) + star5(508, 210, 8)


def a_mao():
    """貌：戴红绒线帽的娃扬手大声问好。"""
    g = ground()
    cap = wrap(
        P("M 300 172 Q 306 120 360 116 Q 414 120 420 172 Q 360 152 300 172 Z", RED),
        R(298, 156, 124, 18, 9, RED_D),
        C(360, 110, 12, WHITE))
    g += kid(360, 444, s=1.0, shirt=YEL, arms="point",
             point_at=(510, 190), look=(2.2, -0.5))
    hearts = heart(500, 150, 12, RED) + heart(536, 196, 8, RED)
    return g + cap + hearts


def a_qing():
    """请：青衣娃托着茶盘请客人喝茶，茶杯冒热气。"""
    g = ground()
    g += kid(320, 444, s=1.0, shirt=TEAL, arms="point",
             point_at=(560, 300), look=(2, 0))
    tray = wrap(
        E(516, 300, 58, 14, WOOD_L),
        E(516, 296, 54, 12, WOOD),
        R(500, 258, 32, 32, 6, WHITE),
        E(516, 266, 12, 4, "#b57b44"),
        P("M 532 268 q 14 4 0 14", stroke=WHITE, w=6),
        P("M 510 248 q -6 -14 2 -24", stroke=LGRAY, w=5),
        C(511, 296, 13, SKIN))
    return g + tray


def a_xie():
    """谢：画面右侧大手递来红苹果，娃娃双手捧接，爱心飘飘。"""
    g = ground()
    g += kid(420, 444, s=0.95, face="open", arms="clap", shirt="#e8a13c",
             look=(1.5, -0.3))
    g += C(448, 312, 25, RED) + L(448, 288, 452, 274, "#5e8f52", 5) \
        + E(456, 278, 10, 5, GREEN)
    g += hand(560, 292, rot=-90)
    g += heart(520, 190, 13, RED) + star5(360, 170, 10)
    return g


def a_cuo():
    """错：伤心娃摇头（两侧摇头弧），旁边一个大红叉。"""
    g = ground()
    shake = wrap(
        P("M 240 222 q -14 12 -4 26", stroke=GRAY, w=5),
        P("M 226 208 q -20 18 -6 42", stroke=GRAY, w=5),
        P("M 452 222 q 14 12 4 26", stroke=GRAY, w=5),
        P("M 466 208 q 20 18 6 42", stroke=GRAY, w=5))
    cross = wrap(
        L(520, 196, 644, 328, "#e8663c", 28),
        L(644, 196, 520, 328, "#e8663c", 28))
    g += kid(340, 444, s=0.95, face="sad", shirt=BLUE, look=(-1, 0.3))
    return g + shake + cross


def a_jie():
    """借：雨天两个娃共撑一把伞，四只手都扶着伞柄。"""
    g = ground()
    rain = ""
    for rx, ry, rr in ((180, 150, 8), (262, 110, 7), (350, 140, 6),
                       (470, 120, 8), (560, 150, 7), (640, 110, 6),
                       (610, 240, 6), (150, 250, 6)):
        rain += drop(rx, ry, rr)
    dome = wrap(
        P("M 250 210 Q 380 76 510 210 Q 448 196 380 210 Q 312 196 250 210 Z", TEAL),
        L(380, 146, 380, 120, "#8a5a33", 8),
        L(380, 208, 380, 398, "#8a5a33", 10),
        P("M 380 398 q 0 22 -22 22", stroke="#8a5a33", w=10))
    g += rain + dome
    g += kid(318, 444, s=0.78, shirt=PURPLE, face="smile", look=(1, 0))
    g += kid(448, 444, s=0.78, shirt="#7fae70", face="smile", look=(-1, 0))
    g += C(374, 374, 10, SKIN) + C(388, 374, 10, SKIN)
    return g


def a_mang():
    """忙：红衣娃独自抱起大木箱，忙得满头大汗。"""
    g = ground()
    g += kid(360, 444, s=1.0, face="open", arms="clap", shirt=RED,
             look=(0, 0.5))
    crate = box(360, 296, 180, 118, open_top=False)
    grips = C(346, 314, 12, SKIN) + C(374, 314, 12, SKIN)
    sweat = drop(298, 178, 10) + drop(322, 150, 8) + drop(424, 166, 9)
    return g + crate + grips + sweat


def a_an():
    """安：戴黄色安全帽的娃站在斑马线上。"""
    g = ground()
    road = wrap(
        R(120, 396, 520, 62, 12, "#8a8f98"),
        R(150, 416, 56, 24, 4, WHITE),
        R(242, 416, 56, 24, 4, WHITE),
        R(334, 416, 56, 24, 4, WHITE),
        R(426, 416, 56, 24, 4, WHITE),
        R(518, 416, 56, 24, 4, WHITE))
    helmet = wrap(
        P("M 318 164 Q 324 102 380 98 Q 436 102 442 164 Q 380 144 318 164 Z", YEL),
        E(380, 166, 70, 13, YEL_D),
        R(366, 94, 28, 16, 7, YEL_D),
        C(348, 126, 9, WHITE, 0.7))
    g += road
    g += kid(380, 400, s=1.0, shirt="#f0876f", face="smile")
    return g + helmet


def a_hua():
    """话：两个娃面对面聊天，头顶各漂着一个对话气泡。"""
    g = ground()
    g += kid(240, 444, s=0.9, shirt=ORANGE, arms="point",
             point_at=(330, 250), look=(1.5, -0.3))
    g += kid(520, 444, s=0.9, shirt=TEAL, arms="clap", look=(-1.5, -0.3))
    b1 = wrap(
        E(226, 176, 76, 46, GRAY),
        E(226, 176, 70, 40, WHITE),
        PG([(262, 210), (290, 248), (296, 204)], WHITE),
        C(200, 176, 6, GRAY_D), C(226, 176, 6, GRAY_D), C(252, 176, 6, GRAY_D))
    b2 = wrap(
        E(566, 206, 62, 38, GRAY),
        E(566, 206, 56, 32, WHITE),
        PG([(536, 236), (512, 268), (522, 230)], WHITE),
        C(546, 206, 6, GRAY_D), C(572, 206, 6, GRAY_D))
    return g + b1 + b2


def a_zhu():
    """助：绿衣伙伴伸手拉坐在地上哭的粉衣娃，皮球滚在一边。"""
    g = ground()
    g += kid(260, 444, s=0.95, shirt=FOREST, arms="point",
             point_at=(420, 330), look=(2, 0.4))
    g += kid(490, 444, s=0.85, pose="sit", face="cry", shirt=ROSE,
             look=(-1.2, 0.4))
    g += ball(614, 430, 20)
    return g


def a_wei():
    """卫：戴口罩的娃在水龙头下搓手洗手，泡泡飞着。"""
    g = ground()
    faucet = wrap(
        R(180, 218, 132, 26, 10, GRAY_D),
        R(284, 238, 26, 42, 8, GRAY_D),
        L(206, 200, 206, 176, "#6b7280", 8),
        L(192, 184, 220, 184, "#6b7280", 8))
    water = wrap(
        P("M 292 280 Q 288 314 282 344", stroke=WBLUE, w=14),
        E(282, 388, 64, 11, WBLUE, 0.7))
    suds = wrap(
        C(252, 332, 10, "#cfe6f0"), C(234, 316, 7, "#cfe6f0"),
        C(312, 320, 8, "#cfe6f0"), C(264, 344, 12, WHITE, 0.85),
        C(300, 352, 9, WHITE, 0.85))
    mask = wrap(
        R(344, 218, 72, 44, 18, WHITE),
        L(350, 236, 386, 240, "#dfe6ec", 4),
        L(374, 248, 410, 244, "#dfe6ec", 4),
        L(344, 232, 318, 222, WHITE, 6),
        L(416, 232, 442, 222, WHITE, 6))
    g += kid(380, 444, s=1.0, shirt="#7cc8bb", arms="reach", look=(0, -0.3))
    return g + faucet + water + suds + mask


def a_kua():
    """夸：两只手掌拍出夸奖的掌声弧，被夸的娃笑开花。"""
    g = ground()
    g += kid(300, 444, s=0.95, face="open", shirt=MAUVE, look=(2, -0.5))
    g += C(262, 240, 20, PINK, 0.9) + C(338, 240, 20, PINK, 0.9)
    g += hand(508, 296, rot=68) + hand(618, 296, rot=-68)
    g += P("M 540 232 q 16 -12 32 0", stroke=YEL, w=6) \
        + P("M 546 256 q 11 -9 22 0", stroke=YEL, w=5)
    g += star5(470, 158, 13) + star5(648, 180, 9) + star5(580, 140, 8)
    return g


def a_zan():
    """赞：竖起的大拇指特写，金星围着点赞。"""
    g = ground()
    thumb = wrap(
        R(432, 148, 56, 164, 28, SKIN_GD),
        R(392, 268, 150, 142, 44, SKIN_G),
        L(428, 300, 428, 340, SKIN_GD, 6),
        L(466, 300, 466, 340, SKIN_GD, 6),
        L(504, 300, 504, 340, SKIN_GD, 6),
        R(392, 396, 150, 42, 16, "#f2b03c"),
        R(392, 406, 150, 14, 7, "#e8a13c"))
    stars = star5(300, 190, 24) + star5(610, 160, 16) + star5(590, 330, 11) \
        + heart(310, 320, 15, RED)
    return g + thumb + stars


def arts():
    return {
        "邻": a_lin(), "居": a_ju(), "礼": a_li(), "貌": a_mao(),
        "请": a_qing(), "谢": a_xie(), "错": a_cuo(), "借": a_jie(),
        "忙": a_mang(), "安": a_an(), "话": a_hua(), "助": a_zhu(),
        "卫": a_wei(), "夸": a_kua(), "赞": a_zan(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    expect = []
    for grp in ziku.GROUPS:
        if grp["id"] == "shehui":
            expect = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"社会礼貌组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
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
