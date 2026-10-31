#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""情绪组 11 卡插画与文案（1000 字批次 B7，全组新增）。

字表：喜怒怕惊欢慌羞急烦忘悲。

一眼可辨约定（主控硬规则）：大表情为主——多数卡用 kid() 的 face 参数
（smile/open/sad/cry/o）+ 身体语言，怒用大圆脸+五官（规范允许）：
喜=双手捧大红心咧嘴笑 / 怒=大红脸竖眉喷气 / 怕=缩坐抱枕发抖冒冷汗+乌云闪电 /
惊=气球爆开瞪眼张嘴双手举起 / 欢=跳起来欢呼撒彩点 / 慌=满头大汗乱跑 /
羞=双手贴脸大红晕低头 / 急=盯着大钟跺脚冒汗 / 烦=捂耳朵+头顶乱线团 /
忘=挠头+两个大问号 / 悲=流泪低头看掉在地上的冰淇淋。
问号为允许符号；相邻卡轮廓+主色错开，无恐怖画面。
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
MAUVE = "#b57fa0"
OLIVE = "#8a9e5c"
LGRAY, GRAY = "#d8d2c2", "#c9cdd1"
SHADOWG = "#a5d0bd"

GROUP_CARDS = [
    {"char": "喜", "pinyin": "xǐ", "tone": "第三声",
     "sentence": "哈哈笑，真欢喜。",
     "say": "笑得甜甜的就是欢喜。",
     "chat": "什么事让你最欢喜？",
     "life": "把开心的事讲给妈妈听。"},
    {"char": "怒", "pinyin": "nù", "tone": "第四声",
     "sentence": "气呼呼，怒冲冲。",
     "say": "皱眉瞪眼是发怒了。",
     "chat": "生气时可以怎么做呀？",
     "life": "怒了先深呼吸三次。"},
    {"char": "怕", "pinyin": "pà", "tone": "第四声",
     "sentence": "打雷了，我怕怕。",
     "say": "缩成一团抱紧是害怕。",
     "chat": "你害怕时会找谁呀？",
     "life": "害怕时抱抱家人或玩偶。"},
    {"char": "惊", "pinyin": "jīng", "tone": "第一声",
     "sentence": "气球砰砰吓一惊。",
     "say": "瞪大眼张嘴是大吃一惊。",
     "chat": "什么事让你大吃一惊？",
     "life": "吃惊时说哎呀吓一跳。"},
    {"char": "欢", "pinyin": "huān", "tone": "第一声",
     "sentence": "小娃欢呼跳起来。",
     "say": "高兴得跳起来叫欢呼。",
     "chat": "你欢呼过哪件开心事？",
     "life": "开心时和家人击个掌。"},
    {"char": "慌", "pinyin": "huāng", "tone": "第一声",
     "sentence": "要迟到了，好慌张。",
     "say": "满头大汗乱跑是慌张。",
     "chat": "慌乱时先停下来做什么？",
     "life": "再着急也先深呼吸。"},
    {"char": "羞", "pinyin": "xiū", "tone": "第一声",
     "sentence": "听到夸奖害羞了。",
     "say": "脸红红的不好意思叫害羞。",
     "chat": "你什么时候会脸红呀？",
     "life": "害羞也可以小声问好。"},
    {"char": "急", "pinyin": "jí", "tone": "第二声",
     "sentence": "钟表滴答，我着急。",
     "say": "盯着钟跺脚是着急。",
     "chat": "什么时候你会着急呀？",
     "life": "着急时数三个数再行动。"},
    {"char": "烦", "pinyin": "fán", "tone": "第二声",
     "sentence": "太吵了，好心烦。",
     "say": "捂住耳朵皱眉是心烦。",
     "chat": "什么声音让你心烦呀？",
     "life": "烦了就换个地方静一静。"},
    {"char": "忘", "pinyin": "wàng", "tone": "第四声",
     "sentence": "咦，我忘带东西了。",
     "say": "挠头想不起来是忘了。",
     "chat": "你有没有忘带过东西呀？",
     "life": "睡前和妈妈一起理书包。"},
    {"char": "悲", "pinyin": "bēi", "tone": "第一声",
     "sentence": "冰淇淋掉了真悲伤。",
     "say": "流眼泪低头是悲伤。",
     "chat": "你难过时会找谁说呀？",
     "life": "难过时说出来会好些。"},
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


def a_xi():
    """喜：蓝衣娃双手捧大红心，咧嘴笑，小爱心飘着。"""
    g = ground()
    g += kid(380, 444, s=1.0, face="open", arms="clap", shirt=BLUE)
    g += heart(380, 308, 62, RED)
    g += C(334, 316, 12, SKIN) + C(426, 316, 12, SKIN)
    g += heart(284, 194, 14, RED) + heart(474, 184, 11, RED)
    return g


def a_nu():
    """怒：大红脸竖眉瞪眼，头顶喷气，嘴角下撇。"""
    g = ground()
    face = wrap(
        C(384, 298, 152, "#d4552f"),
        C(376, 290, 147, "#e8663c"),
        C(330, 250, 20, "#f0876f", 0.5), C(420, 250, 20, "#f0876f", 0.5))
    brows = wrap(
        P("M 288 218 L 356 250", stroke="#8a3216", w=17),
        P("M 472 218 L 404 250", stroke="#8a3216", w=17))
    eyes = wrap(
        C(330, 284, 17, WHITE), C(332, 286, 8, INK),
        C(430, 284, 17, WHITE), C(428, 286, 8, INK))
    mouth = wrap(
        P("M 328 372 Q 380 334 432 372", stroke="#8a3216", w=12))
    steam = wrap(
        P("M 258 176 q -16 -26 2 -46 q 14 -14 4 -34", stroke=GRAY, w=10),
        P("M 502 176 q 16 -26 -2 -46 q -14 -14 -4 -34", stroke=GRAY, w=10))
    return ground() + face + brows + eyes + mouth + steam


def a_pa():
    """怕：缩坐着紧紧抱住条纹枕，眯眼张嘴，身侧发抖弧+冷汗，左上角乌云闪电（打雷）。"""
    g = ground()
    g += kid(360, 440, s=0.95, pose="sit", face="o", shirt=MAUVE,
             look=(-0.5, -0.6))
    pillow = wrap(
        R(296, 312, 130, 82, 26, "#7cc8bb"),
        L(304, 353, 418, 353, "#5aa89a", 5),
        C(361, 353, 8, "#5aa89a"),
        C(310, 320, 11, SKIN), C(412, 320, 11, SKIN))
    quiver = wrap(
        P("M 252 236 q -14 12 -2 26", stroke=GRAY, w=5),
        P("M 238 226 q -20 16 -4 38", stroke=GRAY, w=5),
        P("M 462 236 q 14 12 2 26", stroke=GRAY, w=5),
        P("M 476 226 q 20 16 4 38", stroke=GRAY, w=5))
    thunder = wrap(
        E(146, 128, 34, 17, GRAY),
        E(184, 136, 28, 14, GRAY),
        E(114, 138, 24, 12, GRAY),
        PG([(150, 148), (180, 148), (164, 188), (186, 188), (146, 246),
            (160, 198), (140, 198)], YEL))
    return g + pillow + quiver + thunder + drop(438, 196, 9)


def a_jing():
    """惊：红气球爆开（碎线飞溅），绿衣娃瞪眼张嘴双手举起。"""
    g = ground()
    g += kid(290, 444, s=0.95, face="o", arms="up", shirt="#7fae70",
             look=(2, -1))
    balloon = wrap(
        C(560, 190, 46, "#e8663c"),
        C(544, 174, 14, WHITE, 0.55),
        PG([(550, 232), (570, 232), (560, 246)], "#c94f36"),
        P("M 560 246 Q 548 300 566 356", stroke=GRAY, w=4),
        L(518, 152, 498, 134, YEL, 8),
        L(540, 130, 530, 106, YEL, 8),
        L(578, 126, 586, 100, YEL, 8),
        L(606, 148, 628, 132, YEL, 8),
        L(612, 196, 640, 190, YEL, 8))
    return g + balloon


def a_huan():
    """欢：黄衣娃跳离地面欢呼，彩点星星撒开，脚下投影。"""
    g = ground()
    g += E(380, 450, 120, 15, SHADOWG)
    g += kid(380, 396, s=0.95, face="open", arms="up", shirt=YEL)
    g += C(262, 168, 8, "#e8663c") + C(500, 158, 7, TEAL) \
        + C(238, 250, 6, "#f0876f") + C(524, 246, 6, "#5fa8d8")
    g += star5(470, 214, 11) + star5(292, 208, 9)
    g += R(320, 130, 16, 9, 4, "#f0876f") + R(430, 118, 16, 9, 4, TEAL_L)
    return g


def a_huang():
    """慌：橙衣娃满头大汗向前狂奔，身后尘土+气流弧。"""
    g = ground()
    dust = wrap(
        C(298, 428, 12, LGRAY), C(276, 436, 9, LGRAY), C(258, 424, 7, LGRAY),
        P("M 300 352 q -26 14 -22 42", stroke=GRAY, w=6),
        P("M 316 318 q -32 20 -28 56", stroke=GRAY, w=6))
    sweat = wrap(
        drop(348, 168, 11), drop(322, 196, 8), drop(376, 148, 7))
    g += dust + kid(410, 444, s=0.95, pose="sprint", face="o",
                    shirt=ORANGE, look=(1.5, 0.2))
    return g + sweat


def a_xiu():
    """羞：粉衣娃双手捂着嘴低头偷笑，脸颊两团大红晕全露出来。"""
    s = 0.95
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    g = ground()
    g += kid(x, y, s=s, face="smile", arms="up", shirt="#f0876f",
             look=(0, 1.4))
    cheeks = C(x - 46 * s, hcy + 14 * s, 24, PINK, 0.95) \
        + C(x + 46 * s, hcy + 14 * s, 24, PINK, 0.95)
    hands = wrap(
        P(f"M {x-79.8:.0f} {hcy+5.7:.0f} Q {x-66:.0f} {hcy+42*s:.0f} {x-19*s:.0f} {hcy+36*s:.0f}",
          stroke=SKIN, w=17),
        P(f"M {x+79.8:.0f} {hcy+5.7:.0f} Q {x+66:.0f} {hcy+42*s:.0f} {x+19*s:.0f} {hcy+36*s:.0f}",
          stroke=SKIN, w=17),
        C(x - 19 * s, hcy + 36 * s, 14, SKIN),
        C(x + 19 * s, hcy + 36 * s, 14, SKIN))
    return g + cheeks + hands + heart(296, 152, 10, RED) + heart(464, 144, 8, RED)


def a_ji():
    """急：大钟指向快迟到，青衣娃盯着钟冒汗张嘴。"""
    g = ground()
    clock = wrap(
        C(568, 258, 100, GRAY),
        C(560, 250, 98, "#f4ede0"),
        L(560, 166, 560, 186, INK, 6),
        L(560, 314, 560, 334, INK, 6),
        L(476, 250, 496, 250, INK, 6),
        L(624, 250, 644, 250, INK, 6),
        L(560, 250, 560, 188, INK, 11),
        L(560, 250, 612, 274, INK, 9),
        C(560, 250, 9, "#e8663c"))
    g += kid(270, 444, s=0.95, face="o", shirt=TEAL, look=(2.5, -0.6))
    return g + clock + drop(318, 182, 9)


def a_fan():
    """烦：绿衣娃双手捂住耳朵皱眉，头顶乱线团，两侧吵闹弧。"""
    s = 0.95
    x, y = 380, 444
    hd, sho, hcy, hip = _km(x, y, s)
    tangle = wrap(
        P("M 336 112 q 20 -26 44 -8 q 22 16 40 -6 q 16 -20 36 -2", stroke=INK, w=5),
        P("M 344 134 q 26 -18 50 0 q 22 16 44 -6", stroke=INK, w=5),
        P("M 356 154 q 20 -10 38 2", stroke=INK, w=5))
    noise = wrap(
        P("M 232 238 q -18 16 -6 36", stroke=GRAY, w=6),
        P("M 214 224 q -26 22 -10 50", stroke=GRAY, w=6),
        P("M 528 238 q 18 16 6 36", stroke=GRAY, w=6),
        P("M 546 224 q 26 22 10 50", stroke=GRAY, w=6))
    g = ground()
    g += kid(x, y, s=s, face="sad", arms="up", shirt=OLIVE,
             look=(0, 0.6))
    # 捂耳朵：从举起的手掌折回，两只手盖在耳朵上
    ears = wrap(
        L(x - 79.8, hcy + 5.7, x - 55, hcy + 9.5, SKIN, 16),
        L(x + 79.8, hcy + 5.7, x + 55, hcy + 9.5, SKIN, 16),
        C(x - 55, hcy + 9.5, 13, SKIN), C(x + 55, hcy + 9.5, 13, SKIN))
    return g + tangle + noise + ears


def a_wang():
    """忘：紫衣娃挠头，头顶一大一小两个问号（与相邻悲的蓝衣错开主色）。"""
    g = ground()
    g += kid(380, 444, s=0.95, face="o", arms="point",
             point_at=(452, 130), look=(0.5, -1), shirt="#9a6bb0")
    q1 = wrap(
        P("M 244 176 q -10 -56 36 -62 q 44 -6 46 32 q 2 32 -30 42 l 0 22",
          stroke=INK, w=11),
        C(296, 236, 8, INK))
    q2 = wrap(
        P("M 470 208 q -4 -36 26 -40 q 28 -4 29 22 q 1 22 -20 28 l 0 14",
          stroke=GRAY, w=8),
        C(505, 248, 6, GRAY))
    return g + q1 + q2


def a_bei():
    """悲：蓝衣娃低头流泪，脚边是掉在地上的冰淇淋。"""
    g = ground()
    g += kid(340, 444, s=0.95, face="cry", shirt=BLUE, look=(1.2, 1.2))
    g += drop(292, 258, 9) + drop(388, 258, 9)
    mess = wrap(
        PG([(452, 392), (494, 392), (476, 444)], "#d9a05b"),
        L(458, 410, 490, 410, "#b57b44", 3),
        L(464, 426, 486, 426, "#b57b44", 3),
        C(548, 420, 22, "#f0876f"),
        C(542, 412, 8, WHITE, 0.5),
        E(548, 440, 36, 9, "#f0876f", 0.5))
    return g + mess


def arts():
    return {
        "喜": a_xi(), "怒": a_nu(), "怕": a_pa(), "惊": a_jing(),
        "欢": a_huan(), "慌": a_huang(), "羞": a_xiu(), "急": a_ji(),
        "烦": a_fan(), "忘": a_wang(), "悲": a_bei(),
    }


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    expect = []
    for grp in ziku.GROUPS:
        if grp["id"] == "qingxu":
            expect = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"情绪组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
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
