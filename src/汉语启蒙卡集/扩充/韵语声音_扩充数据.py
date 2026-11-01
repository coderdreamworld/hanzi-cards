#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""韵语与声音游戏 · 扩充数据（6 首新韵语 + 4 个新声音游戏 + 4 张新插画）。

主控合并方式（不改 汉语启蒙_素材.py 的现有内容）：
    from 韵语声音_扩充数据 import NEW_VERSES, NEW_GAMES, NEW_ARTS
    sucai.ARTS.update(NEW_ARTS)            # 或直接并进 NEW_ARTS
    SET_SHENGYIN["groups"][0]["cards"] += NEW_VERSES
    SET_SHENGYIN["groups"][1]["cards"] += NEW_GAMES

- 6 首新韵语各占 1 个此前空白的韵母：ai / ing / ong / eng / e / an（互不相同，
  也正好是 1000 字全集里字数最多的 6 个空白韵母）；
- 4 个新游戏补的是现有 6 个游戏没练过的耳朵能力：听音知义 / 词语接龙 /
  轻声轻重 / 快读不念错；
- 韵语正文、游戏步骤、我自己写的提示语，用的每一个汉字都在 1000 字全集内
  （只有 _verse() 共用的「怎么玩 / 打节奏」两段沿用旧文案，里面的"念""遍"
  两字不在 1000 字内 —— 与现有 8 首完全一致，不在本轮改动范围）；
- 4 张新插画只画游戏的主角要做的动作，禁 <defs>/<use>/<text>/<image>。

独立运行本文件做数据自检。
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

_HERE = Path(__file__).resolve().parent              # 汉语启蒙卡集/扩充/
_PARENT = _HERE.parent.parent                        # 孩子/
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from 识字卡片_素材库 import (  # noqa: E402
    E, C, R, L, P, PG, wrap, ground, ball, cup, kid,
    INK, PAGE, GROUND, RED, RED_D, YEL, YEL_D, TEAL, TEAL_D, TEAL_L,
    BLUE, BLUE_D, WBLUE, SKIN, SKIN_D, HAIR, WOOD, WOOD_D, WOOD_L,
    GREEN, GREEN_L, SUN, SUN_L, PINK, WHITE,
)

PINYIN_JSON = _PARENT / "识字卡片_1000字" / "拼音表1000.json"

# 现有 8 首韵语已经占掉的韵母（本轮 6 首不能再用）
COVERED_RHYMES = {"ao", "iao", "a", "ua", "ou", "u", "i", "ian", "ang", "uang"}
# 1000 字全集里"一个韵语都没有"的空白韵母
BLANK_RHYMES = {"an", "ing", "ai", "e", "eng", "ong", "uo", "ei", "en",
                 "uan", "ui", "iang", "ie", "in", "un", "ia", "ü", "iu", "er", "o"}


# ============================ 新插画 ============================

def _er(cx, cy, rx, ry, color, w):
    """只画轮廓的椭圆环（中间是空的，能互相叠出"缠在一起"的感觉）。"""
    d = (f"M {cx-rx} {cy} A {rx} {ry} 0 1 0 {cx+rx} {cy} "
         f"A {rx} {ry} 0 1 0 {cx-rx} {cy}")
    return P(d, stroke=color, w=w)


def _art_listen_find():
    """听音找物：小朋友伸手指着大苹果，旁边还摆着皮球和水杯——听词指物。"""
    apple = wrap(
        E(424, 238, 62, 58, RED_D),
        E(416, 230, 62, 58, RED),
        E(396, 208, 16, 10, "#f0876f", 0.85),
        R(411, 154, 12, 30, 6, "#8a5a33"),
        E(448, 158, 30, 14, GREEN, 0.95))
    cup_art = cup(644, 158, 118, 164, 0.55)
    pit = ball(556, 382, 46, TEAL, TEAL_D, TEAL_L)
    kidfig = kid(152, 454, 0.88, shirt=TEAL, arms="point",
                 point_at=(410, 230), face="smile")
    return wrap(ground(380, 452, 270, 24), kidfig, pit, cup_art, apple)


def _art_chain():
    """词语接龙：三枚金环首尾相扣成一条链，末端还有一枚箭头往前指。"""
    def link(cx, cy, r):
        return wrap(
            _er(cx + 6, cy + 8, r, r, "#c98f1f", 22),
            _er(cx, cy, r, r, YEL, 22))
    rings = wrap(link(280, 340, 76), link(390, 296, 76), link(500, 252, 76))
    arrow = PG([(578, 236), (578, 268), (610, 252)], RED)
    return wrap(ground(380, 450, 250, 24), rings, arrow)


def _art_soft_voice():
    """轻声轻轻读：左边小朋友张大嘴大声喊（大波纹），右边小朋友抿嘴小声说（小波纹）。"""
    loud = kid(196, 440, 0.82, face="open", shirt=RED, arms="up")
    quiet = kid(524, 440, 0.82, face="smile", shirt=TEAL, arms="down")
    big = wrap(
        P("M 276 216 Q 306 252 276 288", stroke=RED_D, w=12),
        P("M 306 198 Q 348 252 306 306", stroke=RED_D, w=12),
        P("M 336 180 Q 390 252 336 324", stroke=RED_D, w=12))
    small = wrap(
        P("M 594 228 Q 614 252 594 276", stroke=TEAL_D, w=7),
        P("M 618 216 Q 646 252 618 288", stroke=TEAL_D, w=7))
    return wrap(ground(380, 452, 258, 24), loud, big, small, quiet)


def _art_tangle():
    """舌头打结：一团绕来绕去的绳结，旁边小朋友一脸茫然。"""
    knot = wrap(
        _er(298, 306, 108, 78, WOOD_D, 28),
        _er(298, 300, 108, 78, WOOD, 20),
        _er(392, 274, 74, 54, WOOD, 20),
        _er(330, 382, 66, 50, WOOD, 20),
        _er(372, 340, 44, 84, WOOD, 20),
        P("M 404 376 Q 456 392 482 424", stroke=WOOD, w=20),
        P("M 214 258 Q 190 226 210 200", stroke=WOOD, w=18))
    kidfig = kid(600, 444, 0.76, face="o", shirt=YEL, arms="down")
    return wrap(ground(380, 452, 262, 24), knot, kidfig)


NEW_ARTS = {
    "听音找东西": _art_listen_find(),
    "词语接一接": _art_chain(),
    "轻声轻轻读": _art_soft_voice(),
    "舌头打卷": _art_tangle(),
}


# ============================ 卡片数据 ============================

def _verse(title, lines, art_src, extra_tip):
    return {"type": "verse", "key": title, "title": title, "lines": lines,
            "art_src": art_src,
            "tips": [["怎么玩", "大人念一句，孩子接句尾的那个字"],
                     ["打节奏", "一个字拍一下手，一句拍一遍"],
                     ["找韵脚", extra_tip]]}


def _game(title, steps, art_src, tip):
    return {"type": "game", "key": title, "title": title, "steps": steps,
            "art_src": art_src, "tips": [["怎么玩", tip]]}


# ---- 新增 6 首韵语：6 个不同的空白韵母（ai / ing / ong / eng / e / an）----
# 顺序即建议插进现有 8 首里的相对顺序；确切插入位置见设计文档。
NEW_VERSES = [
    _verse("小白兔白又白",
           ["小白兔，白又白，",
            "两只耳朵竖起来。",
            "爱吃青菜爱吃麦，",
            "蹦蹦跳跳真可爱。"],
           "dongwu:兔",
           "白、白、来、菜、爱——都是 ai 音，嘴巴扁扁地笑出来。"),

    _verse("晚上星星亮晶晶",
           ["晚上星星亮晶晶，",
            "我和爸爸静静听。",
            "听着虫声到天明，",
            "梦里都在数星星。"],
           "tianwen:星",
           "晶、听、明、星——都是 ing 音，舌尖轻轻往上抬。"),

    _verse("雨过天晴出彩虹",
           ["雨过天晴出彩虹，",
            "弯弯挂在天空中。",
            "红色最红蓝色最浓，",
            "我拉着妈妈往前冲。"],
           "tianwen:虹",
           "虹、中、浓、冲——都是 ong 音，嘴巴圆圆地收住。"),

    _verse("小火车开进城",
           ["小火车，开进城，",
            "还有轻轻的读书声。",
            "站台挂着一排灯，",
            "开过田野和高峰。"],
           "1000:jiaotong:轨",
           "城、声、灯、峰——都是 eng 音，把声音往后拖一点。"),

    _verse("小书本有儿歌",
           ["小书本，有儿歌，",
            "我读一句你一和。",
            "读得大人也快乐，",
            "我也读给哥哥。"],
           "wupin:书",
           "歌、和、乐、哥——都是 e 音，嘴巴半开轻轻送气。"),

    _verse("小母鸡下蛋蛋",
           ["小母鸡，下蛋蛋，",
            "蛋儿放进小竹篮。",
            "摇摇摆摆下了岸，",
            "我拍着手慢慢看。"],
           "dongwu:鸡",
           "蛋、篮、岸、看——都是 an 音，嘴巴闭紧再张开。"),
]


# ---- 新增 4 个声音游戏：补现有 6 个游戏没练过的耳朵能力 ----
NEW_GAMES = [
    _game("听音找东西",
          ["家长说：苹果。",
           "孩子指一指苹果。",
           "家长说：皮球、水杯。",
           "指对一个，拍一次手。"],
          "听音找东西",
          "挑孩子见过的词，指对三个再换新词；没听对就用手比划。"),

    _game("词语接一接",
          ["家长说一个词：苹果。",
           "家长只说最后一个字：果。",
           "孩子接一个词：果子。",
           "轮到孩子出题，家长来接。"],
          "词语接一接",
          "接不上就换一个词玩；接对了全家拍手。"),

    _game("轻声轻轻读",
          ["家长说“爸爸”，让孩子指指轻的那个字。",
           "孩子指一指第二个“爸”。",
           "再换“妈妈”“桌子”“我们”。",
           "孩子自己读一读，轻重对了就拍手。"],
          "轻声轻轻读",
          "有的字读得又轻又短，有的字读得响；比的是轻重，不是快慢。"),

    _game("舌头打卷",
          ["家长说：四是四，十是十。",
           "孩子跟着说，慢慢说一回。",
           "再说快一点，不说错。",
           "说对了全家拍手。"],
          "舌头打卷",
          "舌头打了卷，慢慢说就不会错；错了就从头说。"),
]


# ============================ 自检 ============================

_TONE_MAP = {"ā": "a", "á": "a", "ǎ": "a", "à": "a",
             "ē": "e", "é": "e", "ě": "e", "è": "e",
             "ī": "i", "í": "i", "ǐ": "i", "ì": "i",
             "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
             "ū": "u", "ú": "u", "ǔ": "u", "ù": "u",
             "ǖ": "ü", "ǘ": "ü", "ǚ": "ü", "ǜ": "ü",
             "ń": "n", "ň": "n", "ǹ": "n", "ḿ": "m"}


def _final(py):
    """韵母：去调号 → 剥声母；零声母 y/w 特殊处理（yu→ü、yi→i、wu→u）。"""
    s = "".join(_TONE_MAP.get(c, c) for c in py)
    if s.startswith("y"):
        rest = s[1:]
        if rest.startswith("u"):
            return "ü" + rest[1:]
        if rest.startswith("i"):
            return "i" + rest[1:]
        return rest
    if s.startswith("w"):
        rest = s[1:]
        if rest.startswith("u"):
            return "u" + rest[1:]
        return rest
    m = re.match(r"^(zh|ch|sh|b|p|m|f|d|t|n|l|g|k|h|j|q|x|r|z|c|s)", s)
    return s[len(m.group(1)):] if m else s


def _load_pinyin():
    with open(PINYIN_JSON, encoding="utf-8") as f:
        return json.load(f)


def _han(text):
    return [c for c in text if "一" <= c <= "鿿"]


def _line_tail(line):
    """模板的正则：行末最后一个汉字（标点前那个）才是被染色的韵脚字。"""
    m = re.match(r"^(.*)([一-鿿])([，。；！？]?)$", line)
    return m.group(2) if m else None


def _self_check():
    pinyin = _load_pinyin()
    problems = []

    def check_text(label, text):
        miss = [c for c in _han(text) if c not in pinyin]
        if miss:
            problems.append(f"{label} 用字不在 1000 字: {''.join(miss)}")

    # ① 韵语：≤4 行、每行 ≤12 字
    for v in NEW_VERSES:
        if len(v["lines"]) > 4:
            problems.append(f"{v['title']} 超过 4 行")
        for ln in v["lines"]:
            if len(ln) > 12:
                problems.append(f"{v['title']} 有超过 12 字的句子: {ln}")

    # ② 韵语正文 / 韵语自写的「找韵脚」/ 游戏步骤 / 游戏玩法提示：字都在 1000 字内
    #    （_verse() 共用的「怎么玩」「打节奏」两段是全组共用旧文案，不在此列）
    for v in NEW_VERSES:
        for ln in v["lines"]:
            check_text(f"{v['title']} 韵语", ln)
        check_text(f"{v['title']} 找韵脚", v["tips"][2][1])
    for g in NEW_GAMES:
        check_text(f"{g['title']} 标题", g["title"])
        for s in g["steps"]:
            check_text(f"{g['title']} 步骤", s)
        for _, t in g["tips"]:
            check_text(f"{g['title']} 玩法提示", t)

    # ③ 每首韵语行尾字韵母相同、6 首互不相同、且都落在空白韵母里
    seen = {}
    for v in NEW_VERSES:
        fins = []
        for ln in v["lines"]:
            tail = _line_tail(ln)
            if tail is None:
                problems.append(f"{v['title']} 行尾不是「句子+汉字+标点」: {ln}")
                continue
            if tail not in pinyin:
                problems.append(f"{v['title']} 韵脚字 {tail} 不在 1000 字")
                continue
            fins.append(_final(pinyin[tail]["pinyin"]))
        if not fins:
            continue
        if len(set(fins)) != 1:
            problems.append(f"{v['title']} 行尾韵母不一致: {fins}")
        fin = fins[0]
        if fin in seen:
            problems.append(f"{v['title']} 与 {seen[fin]} 韵母重复: {fin}")
        seen[fin] = v["title"]
        if fin in COVERED_RHYMES:
            problems.append(f"{v['title']} 韵母 {fin} 已被现有 8 首占用")
        if fin not in BLANK_RHYMES:
            problems.append(f"{v['title']} 韵母 {fin} 不在空白韵母表里")
    if len(seen) != len(NEW_VERSES):
        problems.append(f"韵语韵母互不相同未通过：{seen}")

    # ④ 4 个新游戏各 4 步
    if len(NEW_GAMES) != 4:
        problems.append(f"新游戏数量是 {len(NEW_GAMES)}，应为 4")
    for g in NEW_GAMES:
        if len(g["steps"]) != 4:
            problems.append(f"{g['title']} 步骤是 {len(g['steps'])} 条，应为 4 条")

    # ⑤ 每条 NEW_ARTS 的 SVG 合法且不含禁止标记
    for k, svg in NEW_ARTS.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" '
                          f'viewBox="0 0 760 480"><g>{svg}</g></svg>')
        except Exception as exc:  # noqa: BLE001
            problems.append(f"插画 {k}: {exc}")
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            if bad in svg:
                problems.append(f"插画 {k} 含禁止标记 {bad}")

    # 附：art_src 必须能解析（NEW_ARTS 的 key，或"组id:字"/"1000:组id:字"复用写法）
    for c in NEW_VERSES + NEW_GAMES:
        src = c["art_src"]
        if ":" not in src and src not in NEW_ARTS:
            problems.append(f"{c['key']} art_src 无法解析: {src}")

    print(f"新增 {len(NEW_VERSES)} 首韵语 / {len(NEW_GAMES)} 个游戏 / {len(NEW_ARTS)} 张新插画")
    for v in NEW_VERSES:
        tails = [_line_tail(ln) for ln in v["lines"]]
        fins = [_final(pinyin[t]["pinyin"]) if t in pinyin else "?" for t in tails]
        print(f"  · {v['title']}：{' '.join(tails)} → 韵母 {fins[0]}")
    if problems:
        print("问题：")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("数据自检通过 ✓")


if __name__ == "__main__":
    _self_check()
