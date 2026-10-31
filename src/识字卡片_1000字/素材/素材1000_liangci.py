#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量词组 15 卡插画与文案（1000 字批次 B10）。

字表（与字库1000 liangci 组尾部一致，legacy 已覆盖 只/个/几/片/串）：
支 棵 朵 辆 匹 束 滴 份 张 枚 座 栋 间 次 排。

画法约定：数量用同一物件表达——每张卡就是"一 + 量词"的那个物件，
主角占画面大半；次=跳跃瞬间（腾空+影子+弹跳弧），排=三个球并排。
图上无文字数字；马/车/桥等造型圆润友好。
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
ORANGE, ORANGE_D = "#e8742a", "#c95f1e"      # 跳跳衣
HORSE, HORSE_D, HORSE_L = "#c89058", "#a9743f", "#e9b97e"   # 棕马
PAPER, PAPER_D = "#f7ecd2", "#efe0bc"        # 画卷纸
COOKIE, COOKIE_D = "#e0a35e", "#c78a44"      # 曲奇
BLD, BLD_D = "#9cc9e2", "#7cc8bb"            # 楼体浅蓝
GRAY = "#a8a094"
STEEL = "#c9cdd1"                             # 金属/弹跳弧


def a_zhi():
    """支：一支大大的铅笔。"""
    g = ground()
    inner = wrap(
        R(262, 308, 208, 44, 4, YEL),                      # 笔杆
        L(272, 330, 466, 330, YEL_D, 4),                   # 笔杆棱线
        PG([(470, 308), (510, 330), (470, 352)], WOOD_L),  # 笔尖木
        PG([(496, 323), (510, 330), (496, 337)], INK),     # 铅芯
        R(238, 308, 26, 44, 12, "#f0876f"),                # 橡皮
        R(260, 308, 14, 44, 2, STEEL))                     # 金属箍
    return g + f'<g transform="rotate(-22 380 330)">{inner}</g>'


def a_ke():
    """棵：一棵大树。"""
    return ground() + tree_round(380, 446, s=1.25)


def a_duo():
    """朵：一朵花（花头 + 茎 + 叶）。"""
    g = ground()
    g += L(380, 428, 380, 306, GREEN, 12)
    g += f'<g transform="rotate(-28 330 382)">{E(330, 382, 30, 13, GREEN)}</g>'
    g += f'<g transform="rotate(28 432 348)">{E(432, 348, 30, 13, GREEN)}</g>'
    g += flower5(380, 252, 56, "#f0876f", SUN)
    return g


def a_liang():
    """辆：一辆小汽车。"""
    g = ground()
    g += R(288, 262, 186, 96, 22, RED)                     # 车厢
    g += R(306, 278, 66, 48, 9, "#bfe3f2")                 # 车窗
    g += R(390, 278, 66, 48, 9, "#bfe3f2")
    g += R(216, 330, 328, 88, 26, RED)                     # 车身
    g += R(216, 388, 328, 18, 9, RED_D)                    # 车裙
    g += C(536, 356, 10, SUN)                              # 车灯
    g += C(300, 420, 36, INK) + C(300, 420, 15, STEEL)     # 车轮
    g += C(462, 420, 36, INK) + C(462, 420, 15, STEEL)
    return g


def a_pi():
    """匹：一匹小马（短粗脖前倾 + 大长脸马头 + 飘鬃毛 + 粗马尾，避免读成骆驼/羊驼）。"""
    g = ground()
    g += P("M 288 318 Q 240 342 246 404", stroke=HORSE_D, w=15)   # 粗马尾
    g += P("M 252 398 Q 246 416 254 430", stroke=HORSE_D, w=9)
    for lx in (318, 352, 414, 448):                        # 四条腿 + 蹄
        g += R(lx, 380, 22, 64, 10, HORSE)
        g += E(lx + 11, 446, 15, 9, "#6e4526")
    g += E(380, 332, 106, 62, HORSE)                       # 身体
    g += PG([(436, 302), (498, 212), (548, 240), (472, 344)], HORSE)  # 短粗脖（前倾）
    g += P("M 442 304 Q 468 246 502 210", stroke=HORSE_D, w=18)   # 鬃毛沿脖后
    g += E(566, 224, 54, 30, HORSE)                        # 马头（长脸平伸向右）
    g += E(606, 234, 22, 15, HORSE_L)                      # 口鼻
    g += C(610, 230, 4, HORSE_D)                           # 鼻孔
    g += PG([(532, 202), (546, 160), (562, 200)], HORSE_D)  # 两只耳朵
    g += PG([(560, 200), (578, 162), (588, 202)], HORSE_D)
    g += P("M 538 194 Q 530 184 532 172", stroke=HORSE_D, w=10)   # 额发小撮
    g += C(560, 216, 6, INK)                               # 眼睛
    g += C(562, 214, 2.2, WHITE)
    return g


def a_shu():
    """束：一束花，扎个蝴蝶结。"""
    heads = [(318, 208, "#f0876f"), (362, 172, YEL), (412, 178, "#b57fa0"),
             (448, 214, "#f0876f"), (378, 232, YEL)]
    g = ground()
    for x, y, _c in heads:
        g += L(380, 398, x, y + 14, GREEN, 8)
    for x, y, c in heads:
        g += flower5(x, y, 27, c, SUN)
    g += PG([(380, 396), (338, 378), (342, 414)], RED)     # 左结
    g += PG([(380, 396), (422, 378), (418, 414)], RED)     # 右结
    g += C(380, 396, 11, RED_D)
    g += L(372, 404, 358, 442, RED, 9)                     # 飘带
    g += L(390, 404, 404, 440, RED, 9)
    return g


def a_di():
    """滴：一颗大水滴 + 水面涟漪。"""
    g = ground()
    g += drop(380, 296, 92)
    g += C(352, 268, 15, WHITE, 0.7)
    g += E(380, 428, 92, 14, WBLUE, 0.55)
    g += E(380, 428, 54, 8, WBLUE, 0.85)
    return g


def a_fen():
    """份：一份切好的蛋糕（切块加大、层纹加粗，缩略图也能看出草莓夹层）。"""
    g = ground()
    g += E(380, 424, 190, 24, WHITE)
    g += E(380, 420, 156, 16, "#f4f1e6")
    slice_ = wrap(
        PG([(240, 404), (500, 404), (500, 268)], "#fbeec9"),              # 蛋糕切面
        PG([(288, 380), (500, 380), (500, 356), (330, 356)], "#f5a58c"),  # 草莓层
        PG([(346, 348), (500, 348), (500, 324), (396, 324)], "#f0987e"),  # 果酱层
        C(486, 252, 16, RED),                                            # 樱桃
        L(486, 236, 494, 218, "#6e4526", 4))
    return g + f'<g transform="translate(380,404) scale(1.18) translate(-380,-404)">{slice_}</g>'


def a_zhang():
    """张：一张白纸（折角 + 画了颗小心心）。"""
    g = ground()
    g += E(382, 434, 150, 16, "#a5d0bd", 0.8)
    sheet = wrap(
        R(266, 196, 228, 246, 8, WHITE),
        PG([(494, 196), (494, 248), (442, 196)], "#e3ded2"),   # 折角
        L(442, 196, 494, 248, "#d5d0c2", 3),
        heart(360, 320, 30, "#f0876f"))
    return g + f'<g transform="rotate(-7 380 320)">{sheet}</g>'


def a_mei():
    """枚：一枚亮闪闪的奖章。"""
    g = ground()
    g += PG([(344, 142), (376, 142), (366, 262), (340, 248)], RED)      # 左绶带
    g += PG([(384, 142), (416, 142), (420, 248), (394, 262)], BLUE)     # 右绶带
    g += C(380, 332, 80, YEL_D)
    g += C(380, 330, 72, YEL)
    g += C(380, 330, 54, "#f9c95e")
    g += star5(380, 330, 32, WHITE)
    g += L(330, 292, 316, 306, WHITE, 6)
    return g


def a_zuo():
    """座：一座跨河的拱桥。"""
    g = ground()
    g += E(380, 444, 238, 20, WBLUE, 0.75)
    g += P("M 200 444 Q 230 436 260 444", stroke="#a5d9f0", w=5)
    g += P("M 500 446 Q 530 438 560 446", stroke="#a5d9f0", w=5)
    g += P("M 186 328 Q 380 452 574 328", stroke=WOOD_D, w=26)          # 桥拱
    g += R(150, 296, 460, 32, 10, WOOD)                                 # 桥面
    g += R(150, 320, 460, 10, 5, WOOD_D)
    for bx in (178, 254, 330, 430, 506, 582):
        g += L(bx, 296, bx, 268, WOOD_D, 7)                             # 栏杆柱
    g += L(168, 264, 592, 264, WOOD_D, 8)
    return g


def a_dong():
    """栋：一栋高高的楼房。"""
    g = ground()
    g += R(292, 132, 176, 300, 14, BLD)
    g += R(292, 132, 176, 26, 12, BLD_D)
    for row in range(4):
        for col in range(4):
            g += R(310 + col * 38, 174 + row * 46, 26, 30, 4, "#e8f4f9")
    g += R(352, 376, 56, 56, 8, "#8a5a33")                              # 大门
    g += C(396, 406, 5, SUN)
    return g


def a_jian():
    """间：一间小房子。"""
    g = ground()
    g += R(258, 262, 244, 168, 12, WOOD_L)                              # 墙
    g += PG([(236, 268), (524, 268), (380, 164)], RED)                  # 屋顶
    g += C(304, 314, 26, "#bfe3f2")                                     # 一扇圆窗
    g += R(352, 340, 58, 90, 10, "#8a5a33")                             # 门
    g += C(398, 388, 5, SUN)
    g += R(366, 292, 44, 26, 6, "#e3d7c0")                              # 小雨棚
    return g


def a_ci():
    """次：跳一次的瞬间（腾空 + 影子 + 弹跳弧）。"""
    g = ground()
    g += E(380, 450, 98, 13, "#a5d0bd")
    g += kid(380, 398, s=0.95, pose="run", arms="up", face="open", shirt=ORANGE)
    g += P("M 312 438 Q 346 456 380 438", stroke=STEEL, w=5)
    g += P("M 380 438 Q 414 456 448 438", stroke=STEEL, w=5)
    return g


def a_pai():
    """排：一排三个红球并排站好（红球与 legacy 几 的青球区分，避免同组撞车）。"""
    return ground() + ball(262, 382, 46, RED, RED_D, PINK) \
        + ball(380, 382, 46, RED, RED_D, PINK) + ball(498, 382, 46, RED, RED_D, PINK)


def arts():
    return {
        "支": a_zhi(), "棵": a_ke(), "朵": a_duo(), "辆": a_liang(),
        "匹": a_pi(), "束": a_shu(), "滴": a_di(), "份": a_fen(),
        "张": a_zhang(), "枚": a_mei(), "座": a_zuo(), "栋": a_dong(),
        "间": a_jian(), "次": a_ci(), "排": a_pai(),
    }


GROUP_CARDS = [
    {"char": "支", "pinyin": "zhī", "tone": "第一声",
     "sentence": "一支铅笔画画。",
     "say": "细细长长的一支，说的是铅笔。",
     "chat": "“你有几支铅笔？数一数。”",
     "life": "画完画，把一支铅笔放回笔筒。"},
    {"char": "棵", "pinyin": "kē", "tone": "第一声",
     "sentence": "门前一棵大树。",
     "say": "高高的一棵树，用棵来数。",
     "chat": "“院子里有几棵树呀？”",
     "life": "散步时数一数路边的树。"},
    {"char": "朵", "pinyin": "duǒ", "tone": "第三声",
     "sentence": "一朵花开了。",
     "say": "花儿一朵一朵地开。",
     "chat": "“这一朵花是什么颜色的？”",
     "life": "闻一朵花，轻轻的别摘。"},
    {"char": "辆", "pinyin": "liàng", "tone": "第四声",
     "sentence": "一辆车开过。",
     "say": "数车要说一辆、两辆。",
     "chat": "“马路上开过了几辆车？”",
     "life": "坐上车系好安全带再出发。"},
    {"char": "匹", "pinyin": "pǐ", "tone": "第三声",
     "sentence": "一匹马儿跑。",
     "say": "马要说一匹，不说一个哦。",
     "chat": "“一匹马和一辆车，谁跑得快？”",
     "life": "学小马跑一跑，嘴里喊驾。"},
    {"char": "束", "pinyin": "shù", "tone": "第四声",
     "sentence": "一束花送妈妈。",
     "say": "好多花扎在一起，是一束。",
     "chat": "“这束花有几朵？数数看。”",
     "life": "把小花扎起来送给妈妈吧。"},
    {"char": "滴", "pinyin": "dī", "tone": "第一声",
     "sentence": "一滴水落下。",
     "say": "小小圆圆的一滴水，是一滴。",
     "chat": "“水龙头没关紧，会滴几滴呀？”",
     "life": "拧紧水龙头，一滴也不漏。"},
    {"char": "份", "pinyin": "fèn", "tone": "第四声",
     "sentence": "一份切好的蛋糕。",
     "say": "切成一块分给你，就是一份。",
     "chat": "“每人一份，怎么分才公平？”",
     "life": "分蛋糕啦，你一份我一份。"},
    {"char": "张", "pinyin": "zhāng", "tone": "第一声",
     "sentence": "一张纸折飞机。",
     "say": "薄薄平平的一张纸。",
     "chat": "“一张纸能折什么？试试看。”",
     "life": "抽一张纸巾，擦擦小手。"},
    {"char": "枚", "pinyin": "méi", "tone": "第二声",
     "sentence": "一枚亮奖章。",
     "say": "圆圆的奖章，要说一枚。",
     "chat": "“得到一枚奖章，开心吗？”",
     "life": "做对一件事，奖自己一枚贴纸。"},
    {"char": "座", "pinyin": "zuò", "tone": "第四声",
     "sentence": "一座桥跨河。",
     "say": "架在河上的桥，说一座。",
     "chat": "“走过一座桥，桥下是什么呀？”",
     "life": "过桥时说：我们走一座桥。"},
    {"char": "栋", "pinyin": "dòng", "tone": "第四声",
     "sentence": "一栋大楼真高。",
     "say": "高高的一整栋房子，叫一栋。",
     "chat": "“咱们住的一栋楼有几层呀？”",
     "life": "回家路上数数小区有几栋楼。"},
    {"char": "间", "pinyin": "jiān", "tone": "第一声（间另读 jiàn，如“间隔”）",
     "sentence": "一间小房子。",
     "say": "一个房间一间屋，用间来数。",
     "chat": "“咱们家有几间房？”",
     "life": "说说你的小房间里有啥。"},
    {"char": "次", "pinyin": "cì", "tone": "第四声",
     "sentence": "跳一次给我看。",
     "say": "跳一下就是一次，做一回是一回。",
     "chat": "“你能单脚跳几次呀？”",
     "life": "拍一次手，就说一次。"},
    {"char": "排", "pinyin": "pái", "tone": "第二声",
     "sentence": "三个球排一排。",
     "say": "一个挨一个站好，就是一排。",
     "chat": "“排队的时候，你排在第几个？”",
     "life": "把玩具车排成一排收好。"},
]


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    ziku_chars = [it["char"] if isinstance(it, dict) else it
                  for g in ziku.GROUPS if g["id"] == "liangci" for it in g["chars"]]

    batch = json.loads((ROOT / "tools" / "批次分配.json").read_text(encoding="utf-8"))
    entry = next(e for e in batch["B10"] if e["file"] == "素材1000_liangci.py")
    expect = list(entry["单字"])

    mine = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"量词组：卡数 {len(GROUP_CARDS)}")
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
