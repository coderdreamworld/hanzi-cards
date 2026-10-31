#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数字组补充 12 卡插画与文案（1000 字批次 B10）。

字表（与字库1000 shuzi 组尾部一致，legacy 已覆盖 一~十/两/半/百）：
千 万 亿 元 角 第 倍 号 减 乘 除 等。

画法约定：千=宝塔层层；万=万花筒；亿=大大的地球+仰望的小朋友；
元=小猪存钱罐（禁画钱币钞票，只画罐和投币口）；角=小羊弯弯的角；
第=领奖台第一名（星标，台面无数字）；倍=两倍大的球 vs 原球；
号=口哨+圆点号牌；减=从筐里拿走一个（−号允许）；乘=2×3 球阵列；
除=饼干平均分（4 块分成 2+2）；等=天平两端平衡。图上无文字数字。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
GRAY, GRAY_D = "#a8a094", "#8f887c"          # 天平静灰
ORANGE, ORANGE_D, ORANGE_L = "#e8742a", "#c95f1e", "#f4a76a"   # 倍数球
PAPER, PAPER_L = "#f7ecd2", "#e7d5ae"        # 万花筒盘底
PIG, PIG_D = "#f5a58c", "#ee9a80"            # 小猪罐
GOAT, GOAT_D = "#f3ead8", "#e3d7c0"          # 小羊
COOKIE, COOKIE_D = "#e0a35e", "#c78a44"      # 曲奇
WOOD = "#c89058"
WOOD_D = "#b57b44"
WOOD_L = "#e9b97e"


def a_qian():
    """千：宝塔层层，一层又一层数不清。"""
    g = ground()
    g += R(300, 380, 160, 56, 6, WOOD_L)                    # 一层
    g += PG([(272, 380), (488, 380), (448, 332), (312, 332)], RED)
    g += R(322, 296, 116, 56, 6, WOOD_L)                    # 二层
    g += PG([(300, 296), (460, 296), (424, 252), (336, 252)], RED)
    g += R(344, 216, 72, 52, 6, WOOD_L)                     # 三层
    g += PG([(322, 216), (438, 216), (380, 158)], RED)
    g += L(380, 158, 380, 122, WOOD_D, 8)                   # 塔尖
    g += C(380, 116, 10, RED_D)
    g += R(356, 398, 48, 38, 8, "#8a5a33")                  # 塔门
    return g


def a_wan():
    """万：万花筒，转一转花样千变万化（加大贴近地面，花纹盘每瓣带花芯）。"""
    g = ground()
    cols = [RED, TEAL, YEL, BLUE, "#f0876f", GREEN]
    wedges, dots = "", ""
    for i in range(6):
        a0, a1 = i * math.pi / 3, (i + 1) * math.pi / 3
        am = (i + 0.5) * math.pi / 3
        wedges += PG([(480, 330),
                      (480 + 70 * math.cos(a0), 330 + 70 * math.sin(a0)),
                      (480 + 70 * math.cos(a1), 330 + 70 * math.sin(a1))], cols[i])
        dots += C(480 + 46 * math.cos(am), 330 + 46 * math.sin(am), 9, WHITE, 0.85)
    body = wrap(
        PG([(278, 288), (452, 254), (452, 406), (278, 372)], ORANGE),   # 粗筒身
        R(336, 279, 22, 102, 6, ORANGE_D),                              # 捏握环带
        E(278, 330, 15, 44, ORANGE_D),                                  # 目镜
        C(480, 330, 80, PAPER),                                         # 花样盘
        wedges, dots,
        C(480, 330, 18, WHITE))
    return g + body + C(574, 224, 8, SUN) + C(602, 280, 6, TEAL_L) \
        + C(558, 192, 5, "#f0876f")


def a_yi():
    """亿：地球大大的，亿万人一个家。"""
    g = ground()
    g += E(340, 448, 104, 13, "#a5d0bd")
    g += C(340, 272, 150, BLUE)                              # 地球
    g += P("M 262 220 Q 302 188 346 208 Q 364 240 322 252 Q 278 258 262 220 Z", GREEN)
    g += P("M 388 300 Q 428 278 456 310 Q 448 346 406 342 Q 378 326 388 300 Z", GREEN)
    g += P("M 296 332 Q 328 320 344 346 Q 330 368 300 358 Z", GREEN)
    g += P("M 236 206 Q 258 164 304 152", stroke=WHITE, w=11, opacity=0.5)
    g += kid(600, 444, s=0.5, face="o", arms="up", shirt=RED, look=(-2.5, -1.2))
    return g


def a_yuan():
    """元：小猪存钱罐，一元一元攒起来（不画钱币）。"""
    g = ground()
    g += E(380, 368, 122, 86, PIG)                           # 罐身
    g += R(314, 430, 28, 22, 11, PIG_D)                      # 腿
    g += R(420, 430, 28, 22, 11, PIG_D)
    g += P("M 262 350 Q 234 334 244 312", stroke=PIG_D, w=9)  # 卷尾巴
    g += PG([(420, 292), (448, 264), (456, 298)], PIG_D)      # 耳朵
    g += E(492, 362, 26, 20, PIG_D)                           # 猪鼻
    g += C(486, 358, 4, "#c96a4a") + C(498, 366, 4, "#c96a4a")
    g += C(446, 342, 6, INK) + C(448, 340, 2, WHITE)          # 眼睛
    g += C(444, 376, 10, "#f0876f", 0.7)                      # 腮红
    g += R(352, 284, 62, 12, 6, "#8a5a33")                    # 投币口
    return g


def a_jiao():
    """角：小羊头上弯弯的角（双角向两侧弯出再翘起、下巴加山羊胡，别读成牛）。"""
    g = ground()
    g += E(380, 300, 76, 88, GOAT)                            # 脸
    g += E(380, 238, 54, 28, GOAT_D)                          # 顶毛
    g += P("M 348 244 Q 292 218 288 152 Q 288 128 306 122", stroke="#d9a05b", w=22)
    g += P("M 412 244 Q 468 218 472 152 Q 472 128 454 122", stroke="#d9a05b", w=22)
    g += P("M 314 166 Q 302 170 294 162", stroke="#b5854a", w=4)   # 左角环纹
    g += P("M 446 166 Q 458 170 466 162", stroke="#b5854a", w=4)   # 右角环纹
    g += f'<g transform="rotate(-24 298 268)">{E(298, 268, 28, 14, GOAT_D)}</g>'   # 耳
    g += f'<g transform="rotate(24 462 268)">{E(462, 268, 28, 14, GOAT_D)}</g>'
    g += C(350, 292, 7, INK) + C(352, 290, 2.4, WHITE)
    g += C(410, 292, 7, INK) + C(412, 290, 2.4, WHITE)
    g += E(380, 356, 36, 26, GOAT_D)                          # 口鼻
    g += C(368, 352, 4, "#a89478") + C(392, 352, 4, "#a89478")
    g += P("M 366 368 Q 380 376 394 368", stroke="#a89478", w=4)
    g += PG([(380, 378), (362, 428), (398, 428)], GOAT_D)     # 山羊胡
    return g


def a_di():
    """第：领奖台第一名，头上顶星星（台面无数字）。"""
    g = ground()
    g += R(196, 356, 112, 76, 10, TEAL)                       # 第二高
    g += R(196, 356, 112, 14, 7, TEAL_D)
    g += R(452, 372, 112, 60, 10, YEL)                        # 第三高
    g += R(452, 372, 112, 12, 6, YEL_D)
    g += R(312, 296, 136, 136, 10, RED)                       # 第一名最高
    g += R(312, 296, 136, 18, 9, RED_D)
    g += star5(380, 254, 34)                                  # 冠军星
    g += C(262, 226, 7, "#f0876f") + C(500, 218, 6, TEAL_L)   # 少量彩点
    return g


def a_bei():
    """倍：大球的个头是小球的两倍。"""
    g = ground()
    g += ball(300, 392, 34, ORANGE, ORANGE_D, ORANGE_L)       # 原球
    g += ball(490, 358, 68, ORANGE, ORANGE_D, ORANGE_L)       # 两倍大
    g += L(348, 330, 414, 302, GRAY, 7)
    g += PG([(428, 296), (408, 290), (414, 310)], GRAY)
    return g


def a_hao():
    """号：吹口哨，领到圆点号牌。"""
    g = ground()
    g += P("M 268 316 Q 236 258 288 218", stroke=GRAY, w=5)   # 挂绳
    g += C(274, 332, 24, RED_D)                               # 挂环
    g += C(274, 332, 13, PAGE)
    g += C(326, 340, 56, RED)                                 # 哨身
    g += R(352, 304, 98, 32, 13, RED)                         # 哨嘴
    g += E(450, 320, 10, 16, RED_D)
    g += C(560, 330, 58, YEL)                                 # 号牌
    g += C(560, 330, 44, "#f9c95e")
    g += C(536, 330, 9, INK) + C(560, 330, 9, INK) + C(584, 330, 9, INK)  # 圆点号码
    return g


def a_jian():
    """减：从筐里拿走一个球（−号）。"""
    g = ground()
    g += ball(222, 282, 30, TEAL, TEAL_D, TEAL_L)             # 被拿走的球
    g += R(262, 274, 54, 15, 7, INK)                          # −号
    g += PG([(300, 352), (460, 352), (436, 442), (324, 442)], WOOD)   # 筐身
    g += ball(350, 344, 28, TEAL, TEAL_D, TEAL_L)             # 筐里剩两个
    g += ball(414, 344, 28, TEAL, TEAL_D, TEAL_L)
    g += R(292, 340, 176, 22, 11, WOOD_D)                     # 筐沿
    g += L(310, 384, 450, 384, "#a9743f", 5)
    g += L(316, 414, 444, 414, "#a9743f", 5)
    return g


def a_cheng():
    """乘：两排球，每排三个（2×3 阵列）。"""
    pts = [(280, 316), (380, 316), (480, 316), (280, 404), (380, 404), (480, 404)]
    return ground() + "".join(ball(x, y, 40, RED, RED_D, PINK) for x, y in pts)


def a_chu():
    """除：四块饼干平均分，一人两块。"""
    g = ground()

    def cookie(cx, cy, r=30):
        return C(cx, cy, r, COOKIE) + C(cx - 8, cy - 6, 5, COOKIE_D) + C(cx + 9, cy + 7, 5, COOKIE_D)

    g += E(380, 282, 136, 21, WHITE)                          # 上面一盘 4 块
    g += cookie(310, 254) + cookie(376, 242) + cookie(442, 254) + cookie(376, 268)
    g += L(322, 312, 252, 368, GRAY, 9) + PG([(234, 382), (268, 368), (254, 346)], GRAY)
    g += L(438, 312, 508, 368, GRAY, 9) + PG([(526, 382), (492, 368), (506, 346)], GRAY)
    g += E(236, 430, 120, 18, WHITE)                          # 左盘 2 块
    g += cookie(202, 402) + cookie(268, 402)
    g += E(524, 430, 120, 18, WHITE)                          # 右盘 2 块
    g += cookie(490, 402) + cookie(556, 402)
    return g


def a_deng():
    """等：天平两边一样重，平了就是等。"""
    g = ground()
    g += PG([(330, 444), (430, 444), (396, 420), (364, 420)], GRAY_D)   # 底座
    g += R(372, 250, 16, 174, 8, GRAY)                        # 立柱
    g += C(380, 238, 13, GRAY_D)
    g += R(230, 230, 300, 16, 8, GRAY)                        # 横梁
    g += L(260, 246, 260, 296, GRAY, 5) + L(500, 246, 500, 296, GRAY, 5)
    g += P("M 214 300 Q 260 348 306 300 Z", "#c9cdd1")        # 左盘
    g += P("M 454 300 Q 500 348 546 300 Z", "#c9cdd1")        # 右盘
    g += ball(260, 286, 22, TEAL, TEAL_D, TEAL_L)
    g += ball(500, 286, 22, TEAL, TEAL_D, TEAL_L)
    return g


def arts():
    return {
        "千": a_qian(), "万": a_wan(), "亿": a_yi(), "元": a_yuan(),
        "角": a_jiao(), "第": a_di(), "倍": a_bei(), "号": a_hao(),
        "减": a_jian(), "乘": a_cheng(), "除": a_chu(), "等": a_deng(),
    }


GROUP_CARDS = [
    {"char": "千", "pinyin": "qiān", "tone": "第一声",
     "sentence": "千层宝塔节节高。",
     "say": "宝塔一层又一层，数不清就说千。",
     "chat": "“一千比一百多吗？多多少？”",
     "life": "搭积木塔，数数能搭多少层。"},
    {"char": "万", "pinyin": "wàn", "tone": "第四声",
     "sentence": "万花筒转一转。",
     "say": "筒里的花纹变呀变，多到上万。",
     "chat": "“转一下万花筒，花样变了吗？”",
     "life": "对着光转万花筒，看千变万化。"},
    {"char": "亿", "pinyin": "yì", "tone": "第四声",
     "sentence": "亿万人一个家。",
     "say": "地球好大好大，住着亿万人。",
     "chat": "“地球这么大，咱们家在哪呀？”",
     "life": "抱抱地球仪，找找中国在哪。"},
    {"char": "元", "pinyin": "yuán", "tone": "第二声",
     "sentence": "一块钱是一元。",
     "say": "钱要说几元，存进罐里攒起来。",
     "chat": "“一元钱能买到什么呀？”",
     "life": "把零钱存进小猪罐里。"},
    {"char": "角", "pinyin": "jiǎo", "tone": "第三声",
     "sentence": "羊儿角弯弯。",
     "say": "羊头上弯弯的是角。",
     "chat": "“桌子的角尖尖的，碰到会疼吗？”",
     "life": "摸摸纸卷的弯角，再看看桌角。"},
    {"char": "第", "pinyin": "dì", "tone": "第四声",
     "sentence": "我是第一名。",
     "say": "站得最高、头顶星星是第一名。",
     "chat": "“第一名站在哪一层呀？”",
     "life": "比赛完说说自己得了第几名。"},
    {"char": "倍", "pinyin": "bèi", "tone": "第四声",
     "sentence": "大球是两倍大。",
     "say": "小球变大球，个头大了两倍。",
     "chat": "“两倍是多大？比一比就知道。”",
     "life": "把积木叠成两倍高比一比。"},
    {"char": "号", "pinyin": "hào", "tone": "第四声（号另读 háo，如“号叫”）",
     "sentence": "吹口哨，领号牌。",
     "say": "哨子呜呜叫，号牌上有号码。",
     "chat": "“号牌上的圆点，你能数清吗？”",
     "life": "玩排队游戏，抽一个号牌。"},
    {"char": "减", "pinyin": "jiǎn", "tone": "第三声",
     "sentence": "拿走一个就减。",
     "say": "从筐里拿走一个，就是减。",
     "chat": "“三个球减掉一个，还剩几个？”",
     "life": "吃掉一块饼干，饼干就减少了。"},
    {"char": "乘", "pinyin": "chéng", "tone": "第二声",
     "sentence": "球儿排队学乘法。",
     "say": "一排三个，两排就是三乘二。",
     "chat": "“两排球，每排三个，一共几个？”",
     "life": "摆豆子：一行三个，摆两行。"},
    {"char": "除", "pinyin": "chú", "tone": "第二声",
     "sentence": "分一分就用除。",
     "say": "平均分给大家，就是除。",
     "chat": "“四块饼干分给两个人，一人几块？”",
     "life": "分水果啦，一人一份真公平。"},
    {"char": "等", "pinyin": "děng", "tone": "第三声",
     "sentence": "天平平，两边等。",
     "say": "两边一样重，天平就平了，这叫等。",
     "chat": "“再放一个球上去，天平还等吗？”",
     "life": "两手当跷跷板，比比两个玩具。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "shuzi" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B10"] if e["file"] == "素材1000_shuzi.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"数字组补充：卡数 {len(GROUP_CARDS)}")
    print(f"arts 数：{len(a)}")
    print(f"与批次分配比对：{'一致 ✓' if mine == expect else '不一致 ✗ ' + str(expect) + ' vs ' + str(mine)}")
    idx = [ziku_chars.index(ch) for ch in mine]
    print(f"字库顺序：{'递增一致 ✓' if idx == sorted(idx) else '顺序错 ✗'}")
    keys_ok = set(a) == set(mine)
    print(f"arts key：{'齐全 ✓' if keys_ok else '不匹配 ✗'}")

    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad = []
    for c in GROUP_CARDS:
        w = py[c["char"]]
        if c["pinyin"] != w["pinyin"]:
            bad.append((c["char"], "pinyin", c["pinyin"], w["pinyin"]))
        if not (c["tone"] == w["tone"] or c["tone"].startswith(w["tone"] + "（")):
            bad.append((c["char"], "tone", c["tone"], w["tone"]))
        hanzi = sum(1 for ch in c["sentence"] if "\u4e00" <= ch <= "\u9fff")
        if not (4 <= hanzi <= 10):
            bad.append((c["char"], "句长", hanzi))
        if c["char"] not in c["sentence"]:
            bad.append((c["char"], "句缺字"))
        for f in ("say", "chat", "life"):
            if len(c[f]) > 30:
                bad.append((c["char"], f, len(c[f])))
    print(f"拼音/声调/文案：{'全部通过 ✓' if not bad else str(bad)}")

    svgbad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            svgbad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                svgbad.append((k, t))
        if not v.startswith("<ellipse"):
            svgbad.append((k, "首笔非 ground"))
    print("SVG 校验：全部合法 ✓" if not svgbad else f"SVG 问题：{svgbad}")

    assert mine == expect and keys_ok and idx == sorted(idx) and not bad and not svgbad, "自检未通过"
    print("自检通过 ✓")
