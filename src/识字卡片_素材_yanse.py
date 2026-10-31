#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""颜色组插画与文案：红 黄 蓝 绿 白 黑 粉 灰（8 张，无种子字）。

组内规律最重要：8 张卡用完全相同的构图——浅色衬板上一朵大花 + 同款小碟，
花、碟换成本组目标色，孩子一眼学到「颜色名 = 换色」。
固定不变的部件：衬板、沙色中性地面、碟上高光、花心浅灰环 + 白盘 + 同一张笑脸。
- 白卡：花瓣加淡灰描边（用户要求的底衬/描边处理），否则白花在浅衬板上看不见。
- 黑卡：花瓣近黑暖色；笑脸画在固定白盘上，任何花色下都清晰。
- 地面用中性沙色（不与任何目标色撞色），保证每张卡上唯一的强色就是目标色。
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from 识字卡片_素材库 import (BLUE, C, E, GREEN, INK, P, PINK, R, RED, WHITE, YEL,
                          ground, wrap)

GRAY = "#b8bdc4"       # 灰（中性同族色）
BLACKISH = "#453b35"   # 近黑暖色（黑花花瓣，INK 同族更深）
BOARD = "#f3e8d0"      # 固定浅色衬板（衬出白/灰花瓣）
SANDGY = "#e8d5a8"     # 中性沙色地面（不与目标色撞）
RING = "#d8d3c6"       # 固定花心浅灰环
EDGE = "#cfc8b8"       # 白花专用淡灰描边

# (字, 拼音, 声调, 花瓣色, 描边)
COLORS = [
    ("红", "hóng", "第二声", RED, None),
    ("黄", "huáng", "第二声", YEL, None),
    ("蓝", "lán", "第二声", BLUE, None),
    ("绿", "lǜ", "第四声", GREEN, None),
    ("白", "bái", "第二声", WHITE, EDGE),
    ("黑", "hēi", "第一声", BLACKISH, None),
    ("粉", "fěn", "第三声", "#f6a8c5", None),
    ("灰", "huī", "第一声", GRAY, None),
]


GROUP_CARDS = [
    {"char": "红", "pinyin": "hóng", "tone": "第二声",
     "sentence": "红花放在红碟子上。",
     "say": "这朵花是红色，碟子也是红色。",
     "chat": "“家里还有什么东西是红色的？”",
     "life": "找一找红色的东西：红旗、红苹果。"},
    {"char": "黄", "pinyin": "huáng", "tone": "第二声",
     "sentence": "黄花放在黄碟子上。",
     "say": "这朵花是黄色，像小太阳的颜色。",
     "chat": "“香蕉是什么颜色的？”",
     "life": "找黄色的东西：香蕉、小黄鸭。"},
    {"char": "蓝", "pinyin": "lán", "tone": "第二声",
     "sentence": "蓝花放在蓝碟子上。",
     "say": "这朵花是蓝色，和天空一个颜色。",
     "chat": "“你身上有没有蓝色的东西？”",
     "life": "找蓝色的东西：天空、牛仔裤。"},
    {"char": "绿", "pinyin": "lǜ", "tone": "第四声",
     "sentence": "绿花放在绿碟子上。",
     "say": "这朵花是绿色，和叶子一个颜色。",
     "chat": "“小草是什么颜色？”",
     "life": "找绿色的东西：树叶、草地。"},
    {"char": "白", "pinyin": "bái", "tone": "第二声",
     "sentence": "白花放在白碟子上。",
     "say": "这朵花是白色，像雪一样白。",
     "chat": "“牛奶是什么颜色的？”",
     "life": "找白色的东西：牛奶、白云。"},
    {"char": "黑", "pinyin": "hēi", "tone": "第一声",
     "sentence": "黑花放在黑碟子上。",
     "say": "这朵花是黑色，黑黑的像黑夜。",
     "chat": "“关了灯屋里是什么颜色？”",
     "life": "找黑色的东西：黑豆、黑芝麻。"},
    {"char": "粉", "pinyin": "fěn", "tone": "第三声",
     "sentence": "粉花放在粉碟子上。",
     "say": "这朵花是粉色，像桃花的颜色。",
     "chat": "“你最喜欢什么粉色的东西？”",
     "life": "找粉色的东西：桃花、草莓牛奶。"},
    {"char": "灰", "pinyin": "huī", "tone": "第一声",
     "sentence": "灰花放在灰碟子上。",
     "say": "这朵花是灰色，像小老鼠的颜色。",
     "chat": "“乌云是什么颜色？”",
     "life": "找灰色的东西：水泥地、小灰兔。"},
]


def _petal(px, py, fill, stroke=None):
    if stroke:
        return f'<circle cx="{px}" cy="{py}" r="66" fill="{fill}" stroke="{stroke}" stroke-width="6"/>'
    return C(px, py, 66, fill)


def _card(petal, stroke=None):
    """统一构图：衬板 → 小碟（目标色+固定高光） → 大花（目标色） → 固定花心与笑脸。"""
    flower = ""
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        flower += _petal(380 + 92 * math.cos(a), 222 + 92 * math.sin(a), petal, stroke)
    return wrap(
        ground(fill=SANDGY),
        R(70, 52, 620, 380, 40, BOARD),
        E(380, 406, 128, 17, INK, 0.1),          # 碟影（固定）
        E(380, 400, 104, 30, petal),             # 小碟：与花同色
        E(380, 394, 74, 19, WHITE, 0.45),        # 碟面高光（固定）
        flower,
        C(380, 222, 50, RING),                   # 花心浅灰环（固定）
        C(380, 222, 42, WHITE),                  # 白盘（固定）
        C(364, 216, 6.5, INK), C(396, 216, 6.5, INK),
        C(366, 214, 2.2, WHITE), C(398, 214, 2.2, WHITE),
        P("M 368 234 Q 380 244 392 234", stroke=INK, w=5.5),
        C(348, 228, 8, PINK, 0.75), C(412, 228, 8, PINK, 0.75),
    )


def arts():
    return {ch: _card(color, stroke) for ch, _, _, color, stroke in COLORS}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import 识字卡片_字库 as ZIKU

    GID, SEEDS = "yanse", set()
    expect = []
    for g in ZIKU.GROUPS:
        if g["id"] == GID:
            for item in g["chars"]:
                k = item["char"] if isinstance(item, dict) else item
                if k not in SEEDS:
                    expect.append(k)
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"颜色组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，无种子字）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
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
    assert got == expect and set(a) == set(got) and not bad, "自检未通过"
    print("自检通过 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '彩', 'pinyin': 'cǎi', 'tone': '第三声', 'sentence': '彩色气球飞上天。', 'say': '好多颜色在一起，就是彩色。', 'chat': '“这束气球有哪几种颜色？”', 'life': '用彩笔画一道小彩虹。'},
    {'char': '色', 'pinyin': 'sè', 'tone': '第四声', 'sentence': '调色盘上颜色多。', 'say': '画画的颜料有好多种，这就是色。', 'chat': '“你最喜欢哪一种颜色？”', 'life': '画画时说出每种颜色的名字。'},
    {'char': '青', 'pinyin': 'qīng', 'tone': '第一声', 'sentence': '青山下面青草绿。', 'say': '青是像小草那样的颜色，青青的山。', 'chat': '“青色和哪种颜色最像？”', 'life': '到楼下找一找青青的草。'},
]
_arts_mig = {
    '彩': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="382" cy="430" rx="40" ry="16" fill="#b8bdc4"/><ellipse cx="382" cy="424" rx="40" ry="15" fill="#cdd2d8"/><line x1="300" y1="236" x2="382" y2="412" stroke="#a89577" stroke-width="3.5" stroke-linecap="round"/><polygon points="292,222 308,222 300,236" fill="#d4552f"/><ellipse cx="303" cy="172" rx="46" ry="56" fill="#d4552f"/><ellipse cx="300" cy="168" rx="46" ry="56" fill="#e8663c"/><ellipse cx="283.9" cy="148.4" rx="12.88" ry="12.32" fill="#f5a58c" opacity="0.9"/><line x1="380" y1="186" x2="382" y2="412" stroke="#a89577" stroke-width="3.5" stroke-linecap="round"/><polygon points="372,172 388,172 380,186" fill="#3e9486"/><ellipse cx="383" cy="120" rx="48" ry="58" fill="#3e9486"/><ellipse cx="380" cy="116" rx="48" ry="58" fill="#4fae9f"/><ellipse cx="363.2" cy="95.7" rx="13.440000000000001" ry="12.76" fill="#7cc8bb" opacity="0.9"/><line x1="458" y1="220" x2="382" y2="412" stroke="#a89577" stroke-width="3.5" stroke-linecap="round"/><polygon points="450,206 466,206 458,220" fill="#d99a2b"/><ellipse cx="461" cy="156" rx="46" ry="56" fill="#d99a2b"/><ellipse cx="458" cy="152" rx="46" ry="56" fill="#f2b53c"/><ellipse cx="441.9" cy="132.4" rx="12.88" ry="12.32" fill="#f9c95e" opacity="0.9"/><line x1="246" y1="336" x2="382" y2="412" stroke="#a89577" stroke-width="3.5" stroke-linecap="round"/><polygon points="238,322 254,322 246,336" fill="#4a97c9"/><ellipse cx="249" cy="276" rx="42" ry="52" fill="#4a97c9"/><ellipse cx="246" cy="272" rx="42" ry="52" fill="#5fa8d8"/><ellipse cx="231.3" cy="253.8" rx="11.760000000000002" ry="11.44" fill="#fdfdfa" opacity="0.9"/><line x1="512" y1="338" x2="382" y2="412" stroke="#a89577" stroke-width="3.5" stroke-linecap="round"/><polygon points="504,324 520,324 512,338" fill="#e08a70"/><ellipse cx="515" cy="278" rx="42" ry="52" fill="#e08a70"/><ellipse cx="512" cy="274" rx="42" ry="52" fill="#f5a58c"/><ellipse cx="497.3" cy="255.8" rx="11.760000000000002" ry="11.44" fill="#fdfdfa" opacity="0.9"/>',
    '色': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="390" cy="330" rx="192" ry="132" fill="#b57b44"/><ellipse cx="380" cy="322" rx="192" ry="132" fill="#e9b97e"/><circle cx="282" cy="368" r="22" fill="#fdf8ec"/><circle cx="320" cy="300" r="17" fill="#e8663c"/><circle cx="378" cy="282" r="17" fill="#f2b53c"/><circle cx="436" cy="296" r="17" fill="#5fa8d8"/><circle cx="462" cy="352" r="17" fill="#7fae70"/><circle cx="408" cy="392" r="17" fill="#f5a58c"/><circle cx="330" cy="388" r="17" fill="#4fae9f"/><g transform="translate(600,120) rotate(138)"><rect x="0" y="-8" width="130" height="16" rx="8" fill="#b57b44"/><rect x="130" y="-8" width="24" height="16" rx="4" fill="#c9cdd1"/><path d="M 154 -8 Q 186 -4 198 0 Q 186 4 154 8 Z" fill="#e8663c"/></g>',
    '青': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><path d="M 118 436 Q 266 152 414 436 Z" fill="#7cc8bb"/><path d="M 298 436 Q 468 112 640 436 Z" fill="#4fae9f"/><path d="M 452 214 Q 492 290 508 366" fill="none" stroke="#7cc8bb" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><path d="M 196 430 Q 182.0 420.0 170.0 402.0" fill="none" stroke="#5f8f52" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 202.0 430 Q 194.0 418.0 188.0 396.0" fill="none" stroke="#5f8f52" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 286 438 Q 274.1 429.5 263.9 414.2" fill="none" stroke="#5f8f52" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 291.1 438 Q 284.3 427.8 279.2 409.1" fill="none" stroke="#5f8f52" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 478 432 Q 463.3 421.5 450.7 402.6" fill="none" stroke="#5f8f52" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 484.3 432 Q 475.9 419.4 469.6 396.3" fill="none" stroke="#5f8f52" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M 566 440 Q 553.4 431.0 542.6 414.8" fill="none" stroke="#5f8f52" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 571.4 440 Q 564.2 429.2 558.8 409.4" fill="none" stroke="#5f8f52" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
