#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""天文组新增 8 卡插画与文案（1000 字批次 B12）。

字表：雾霜雷阳露霞雹光
（legacy ../识字卡片_素材_tianwen.py 已有 月星云电风雨雪虹冰闪，种子卡「日」由构建器提供）。

与 legacy 错造型：legacy 电=紫灰底单根大闪电，本批 雷=乌云+双闪电+小鼓（雷声像鼓）；
legacy 月=深夜板月牙，本批不出月亮；legacy 雨=雨丝，雹=一颗颗小冰球；legacy 无以下造型：
雾=雾蒙蒙远山、霜=窗上冰花纹、阳=笑脸大太阳+三角光芒、露=叶上滚露珠、
霞=粉橙晚霞山影、雹=乌云落小冰粒、光=灯泡发光放射线。
"""
import importlib.util
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# ---------- 本组同族补充色 ----------
MIST1, MIST2, MIST3 = "#c7d8e6", "#adc6db", "#98b7d0"     # 远中近三层山
DUSK1, DUSK2, DUSK3 = "#f7b98a", "#f5a39c", "#c98ba8"      # 晚霞三层天
DUSK_H1, DUSK_H2 = "#8a6f9e", "#7a6190"                    # 晚霞山影
HAIL, HAIL_D = "#e8f4fb", "#c6e6f8"                        # 冰雹
CLOUD_G1, CLOUD_G2 = "#75808e", "#5f6a78"                  # 雷雨云（比雨卡更深）
STEEL, STEEL_D = "#9aa1aa", "#7f8a92"                      # 灯泡螺口金属


def sparkle(cx, cy, r, fill=SUN):
    """四角亮晶晶闪光。"""
    return (PG([(cx, cy - r), (cx + r * 0.26, cy), (cx, cy + r), (cx - r * 0.26, cy)], fill)
            + PG([(cx - r, cy), (cx, cy - r * 0.26), (cx + r, cy), (cx, cy + r * 0.26)], fill))


def bolt(x, y, h, w, main=YEL, dark=YEL_D):
    """闪电（折线粗笔，带深一号底偏移）。"""
    dx1, dx2 = -w, w * 0.45
    d = (f"M {x} {y} L {x+dx1} {y+h*0.44} L {x+dx1+22} {y+h*0.44} "
         f"L {x+dx2} {y+h} L {x+dx2-14} {y+h*0.58} L {x+dx2-14-20} {y+h*0.58} Z")
    return P(f"M {x+6} {y+8} L {x+dx1+6} {y+h*0.44+8} L {x+dx1+28} {y+h*0.44+8} L {x+dx2+6} {y+h+8} "
             f"L {x+dx2-8} {y+h*0.58+8} L {x+dx2-28} {y+h*0.58+8} Z", dark) + P(d, main)


# ---------- 各卡场景 ----------
def art_wu4():
    """雾：白雾蒙住远山，一层比一层淡。"""
    g = ground()
    g += R(70, 48, 620, 372, 36, "#e9f2f8")
    g += PG([(180, 336), (360, 148), (540, 336)], MIST1)
    g += PG([(80, 344), (244, 178), (420, 344)], MIST2)
    g += PG([(420, 350), (572, 214), (682, 350)], MIST3)
    g += PG([(560, 250), (578, 222), (596, 250)], "#7fa3a0")            # 山上小松
    g += E(380, 296, 252, 42, WHITE, 0.88)
    g += E(244, 238, 168, 30, WHITE, 0.62)
    g += E(540, 218, 148, 26, WHITE, 0.55)
    g += E(396, 350, 292, 32, WHITE, 0.95)
    g += E(160, 320, 120, 26, WHITE, 0.5)
    return g


def art_shuang1():
    """霜：冬窗玻璃上结出羽毛状的霜花。"""
    g = ground()
    g += R(196, 390, 368, 26, 9, WOOD_D)                                 # 窗台
    g += R(210, 88, 340, 304, 14, WOOD)
    g += R(230, 108, 300, 264, 8, "#dceefa")
    g += R(372, 108, 16, 264, 4, WOOD) + R(230, 232, 300, 14, 4, WOOD)
    frost = ""
    # 左上角霜羽
    frost += P("M 240 116 Q 272 152 260 196 Q 252 222 268 246", stroke=WHITE, w=5)
    frost += P("M 252 146 Q 272 152 286 168", stroke=WHITE, w=4)
    frost += P("M 256 184 Q 276 184 292 200", stroke=WHITE, w=4)
    frost += P("M 258 218 Q 276 224 286 238", stroke=WHITE, w=4)
    frost += P("M 240 116 Q 264 128 276 148", stroke=WHITE, w=4)
    # 右下角霜羽
    frost += P("M 520 364 Q 488 328 500 284 Q 508 258 492 234", stroke=WHITE, w=5)
    frost += P("M 506 334 Q 486 328 472 312", stroke=WHITE, w=4)
    frost += P("M 502 296 Q 482 296 466 280", stroke=WHITE, w=4)
    frost += P("M 500 262 Q 484 256 474 242", stroke=WHITE, w=4)
    frost += P("M 520 364 Q 496 352 484 332", stroke=WHITE, w=4)
    # 顶边冰针 + 霜点
    for x in (300, 342, 386, 428, 470):
        frost += PG([(x - 5, 108), (x + 5, 108), (x, 108 + 16 + (x % 3) * 5)], WHITE)
    for x, y in ((262, 262), (312, 300), (352, 254), (420, 288), (470, 320), (500, 180),
                 (300, 170), (350, 196), (440, 150), (268, 330), (410, 344)):
        frost += C(x, y, 3.5, WHITE)
    g += frost
    g += sparkle(500, 136, 11, "#bfe3f5") + sparkle(258, 210, 9, WHITE)
    return g


def art_lei2():
    """雷：乌云里窜出两道闪电，雷声像敲鼓。"""
    g = ground()
    g += cloud_p(330, 158, 2.1, CLOUD_G2)
    g += cloud_p(330, 138, 2.1, CLOUD_G1)
    g += C(158, 122, 34, CLOUD_G1) + C(500, 116, 32, CLOUD_G1)
    g += bolt(296, 244, 172, 44)
    g += bolt(428, 230, 134, 34)
    # 小鼓（雷声咚咚，与文体组大红鼓错色错形）
    g += P("M 552 434 L 548 452", stroke=WOOD_D, w=10) + P("M 630 434 L 634 452", stroke=WOOD_D, w=10)
    g += R(528, 372, 126, 64, 12, TEAL)
    g += R(528, 372, 126, 14, 7, YEL) + R(528, 422, 126, 14, 7, YEL)
    g += E(591, 372, 63, 15, "#f4d3a4")
    g += L(560, 352, 624, 376, WOOD, 9) + C(626, 378, 8, "#f4d3a4")
    g += L(620, 350, 566, 376, WOOD, 9) + C(564, 378, 8, "#f4d3a4")
    g += P("M 508 336 Q 490 362 506 390", stroke=YEL_D, w=7)              # 鼓声波
    g += P("M 482 320 Q 456 362 478 402", stroke=YEL_D, w=6)
    return g


def art_yang2():
    """阳：笑脸大太阳，三角光芒照四方（与种子卡「日」的无脸线条光错开）。"""
    g = ground()
    g += C(380, 256, 168, SUN_L, 0.35)
    for i in range(12):
        a = math.radians(i * 30)
        x1, y1 = 380 + 122 * math.cos(a), 256 + 122 * math.sin(a)
        x2, y2 = 380 + 182 * math.cos(a), 256 + 182 * math.sin(a)
        if i % 2 == 0:
            xa, ya = 380 + 152 * math.cos(a + 0.16), 256 + 152 * math.sin(a + 0.16)
            xb, yb = 380 + 152 * math.cos(a - 0.16), 256 + 152 * math.sin(a - 0.16)
            g += PG([(x1, y1), (xa, ya), (x2, y2), (xb, yb)], SUN)
        else:
            g += L(x1, y1, x2, y2, SUN_L, 10)
    g += C(380, 256, 112, SUN) + C(380, 256, 94, SUN_L)
    g += P("M 340 246 Q 356 232 372 246", stroke=INK, w=7)               # 笑眼
    g += P("M 388 246 Q 404 232 420 246", stroke=INK, w=7)
    g += P("M 348 282 Q 380 306 412 282", stroke=INK, w=7)               # 大笑
    g += C(324, 272, 13, PINK, 0.8) + C(436, 272, 13, PINK, 0.8)
    return g


def art_lu4():
    """露：大叶子上滚着圆滚滚的露珠。"""
    g = ground()
    g += P("M 130 372 Q 148 364 162 350", stroke="#5e8f52", w=10)         # 叶柄
    g += P("M 162 350 Q 250 196 448 190 Q 556 188 590 240 Q 500 366 300 372 Q 206 374 162 350 Z", GREEN)
    g += P("M 176 348 Q 360 300 574 244", stroke="#5e8f52", w=8)
    g += P("M 296 322 Q 312 288 354 274", stroke="#5e8f52", w=5)
    g += P("M 420 304 Q 440 278 480 268", stroke="#5e8f52", w=5)
    g += P("M 250 340 Q 262 318 294 310", stroke="#5e8f52", w=5)
    g += P("M 470 288 Q 490 272 522 264", stroke="#5e8f52", w=5)
    for cx, cy, r in ((388, 280, 30), (486, 258, 19), (308, 314, 14)):
        g += E(cx, cy + r * 0.55, r * 1.1, r * 0.3, "#5e8f52", 0.4)       # 叶面上的影
        g += C(cx + 2, cy + 3, r, "#a5d9f0")
        g += C(cx - 1, cy - 1, r * 0.85, WBLUE)
        g += C(cx - r * 0.32, cy - r * 0.36, r * 0.26, WHITE)
    g += P("M 138 432 Q 146 400 136 378", stroke="#5e8f52", w=7)          # 底下小草
    g += P("M 166 436 Q 178 410 172 390", stroke="#7fae70", w=7)
    g += P("M 612 434 Q 606 406 618 386", stroke="#5e8f52", w=7)
    return g


def art_xia2():
    """霞：太阳落山前，粉橙晚霞染红半边天。"""
    g = ground()
    g += P("M 70 84 Q 70 48 106 48 L 654 48 Q 690 48 690 84 L 690 210 L 70 210 Z", DUSK1)
    g += R(70, 196, 620, 96, 0, DUSK2)
    g += P("M 70 282 L 690 282 L 690 384 Q 690 420 654 420 L 106 420 Q 70 420 70 384 Z", DUSK3)
    g += cloud_p(540, 128, 0.9, "#fbd0c0")
    g += cloud_p(214, 106, 0.66, "#fadde0")
    g += R(320, 156, 128, 16, 8, "#f8cfc0")
    g += C(300, 330, 84, "#fbd9a0")                                      # 落日半轮
    g += PG([(70, 424), (208, 330), (368, 424)], DUSK_H1)
    g += PG([(268, 424), (506, 316), (690, 424)], DUSK_H2)
    g += R(430, 250, 110, 14, 7, "#e8a3b8")
    g += R(160, 262, 86, 12, 6, "#e8a3b8")
    return g


def art_bao2():
    """雹：乌云底下噼里啪啦掉小冰球。"""
    g = ground()
    g += cloud_p(380, 158, 2.0, "#93a3b4")
    g += cloud_p(380, 140, 2.0, "#a9b8c8")
    g += C(254, 126, 32, "#a9b8c8") + C(506, 120, 30, "#a9b8c8")
    hail = ""
    for cx, cy, r in ((262, 252, 18), (330, 302, 15), (398, 240, 19), (454, 322, 16),
                      (512, 264, 18), (240, 354, 15), (368, 368, 17), (490, 382, 15),
                      (558, 330, 14), (304, 218, 12)):
        hail += C(cx + 2, cy + 3, r, HAIL_D)
        hail += C(cx - 1, cy - 1, r * 0.85, HAIL)
        hail += C(cx - r * 0.3, cy - r * 0.35, r * 0.24, WHITE)
        hail += L(cx - r * 1.7, cy - r * 1.6, cx - r * 1.1, cy - r * 1.6, WHITE, 4)
    g += hail
    g += E(380, 430, 196, 24, HAIL_D, 0.5)
    g += C(232, 424, 14, HAIL) + C(532, 432, 13, HAIL)                   # 落地打转的小冰粒
    g += P("M 208 398 Q 217 387 228 394", stroke=HAIL_D, w=4)            # 弹跳弧
    g += P("M 548 402 Q 557 391 568 398", stroke=HAIL_D, w=4)
    return g


def art_guang1():
    """光：灯泡一亮，放射线洒满屋。"""
    g = ground()
    for i in range(12):
        a = math.radians(i * 30 + 15)
        x1, y1 = 380 + 120 * math.cos(a), 232 + 120 * math.sin(a)
        x2, y2 = 380 + 178 * math.cos(a), 232 + 178 * math.sin(a)
        g += L(x1, y1, x2, y2, SUN if i % 2 == 0 else SUN_L, 10 if i % 2 == 0 else 7)
    g += C(380, 232, 98, "#f7d95e")
    g += C(380, 232, 72, "#fdf0b8")
    g += C(346, 198, 17, WHITE, 0.85)
    g += P("M 356 284 Q 368 250 380 272 Q 392 250 404 284", stroke="#d99a2b", w=6)
    g += L(356, 286, 356, 314, "#d99a2b", 6) + L(404, 286, 404, 314, "#d99a2b", 6)
    g += R(354, 314, 52, 15, 6, STEEL) + R(358, 331, 44, 13, 6, STEEL)
    g += R(362, 346, 36, 12, 5, STEEL_D) + R(372, 360, 16, 9, 4, STEEL_D)
    g += sparkle(212, 128, 14) + sparkle(558, 150, 12) + sparkle(532, 348, 10)
    return g


# ---------- 组卡片文案数据 ----------
GROUP_CARDS = [
    {"char": "雾", "pinyin": "wù", "tone": "第四声",
     "sentence": "大雾蒙住了远山。",
     "say": "白白的雾飘在山中间，看不远。",
     "chat": "“起雾的时候像蒙了什么？”",
     "life": "烧开水时看看白汽，像小雾。"},
    {"char": "霜", "pinyin": "shuāng", "tone": "第一声",
     "sentence": "窗上开了霜花。",
     "say": "冬天窗玻璃上结出白白的霜花。",
     "chat": "“霜花摸得到吗？为什么？”",
     "life": "冬天早上找找窗上的霜。"},
    {"char": "雷", "pinyin": "léi", "tone": "第二声",
     "sentence": "轰隆隆打雷了。",
     "say": "乌云里闪电咔嚓，雷声像敲鼓。",
     "chat": "“听到打雷你会躲在哪里？”",
     "life": "打雷时待在屋里，数数雷声。"},
    {"char": "阳", "pinyin": "yáng", "tone": "第二声",
     "sentence": "太阳出来暖洋洋。",
     "say": "圆圆太阳眯眯笑，光芒照大地。",
     "chat": "“太阳出来了你感觉怎么样？”",
     "life": "早上到阳台晒晒太阳。"},
    {"char": "露", "pinyin": "lù", "tone": "第四声（另读 lòu，如“露面”）",
     "sentence": "叶子上滚着露珠。",
     "say": "清晨叶子上圆圆的水珠叫露水。",
     "chat": "“露珠什么时候最多？”",
     "life": "清晨到草地找找小露珠。"},
    {"char": "霞", "pinyin": "xiá", "tone": "第二声",
     "sentence": "晚霞染红了天。",
     "say": "太阳落山前，天边粉红粉红的。",
     "chat": "“晚霞和白云哪里不一样？”",
     "life": "傍晚抬头看看天边的霞。"},
    {"char": "雹", "pinyin": "báo", "tone": "第二声",
     "sentence": "冰雹噼里啪啦落。",
     "say": "天上掉下小冰球，砸得啪啪响。",
     "chat": "“冰雹和雨点哪里不一样？”",
     "life": "下雹时在窗边看小冰粒跳。"},
    {"char": "光", "pinyin": "guāng", "tone": "第一声",
     "sentence": "灯泡一亮满屋光。",
     "say": "灯泡发光，把屋子照得亮亮的。",
     "chat": "“晚上没有光会怎么样？”",
     "life": "按按开关，看灯亮灯灭。"},
]


def arts():
    return {"雾": art_wu4(), "霜": art_shuang1(), "雷": art_lei2(), "阳": art_yang2(),
            "露": art_lu4(), "霞": art_xia2(), "雹": art_bao2(), "光": art_guang1()}


if __name__ == "__main__":
    LEGACY10 = {"月", "星", "云", "电", "风", "雨", "雪", "虹", "冰", "闪"}
    SEED = {"日"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "tianwen":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY10 and c not in SEED]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"天文组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，legacy {len(LEGACY10)}+种子 {sorted(SEED)} 已跳过）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != re.sub(r"（.*?）", "", c["tone"])]
    print(f"拼音/声调：{'与拼音表一致 ✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    punct = "，。！？、；：·—…"
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len([t for t in c["sentence"] if t not in punct]) <= 10)]
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
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
