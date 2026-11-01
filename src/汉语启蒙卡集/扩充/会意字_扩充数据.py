#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""会意字 · 拼字魔法 —— 扩充 10 张（2026-11-01，主控补齐）。

背景：子代理因 Token 上限中断，本文件由主控按同一规范补齐。
扩充逻辑：现有 14 张的部件池只有 16 个部件（日月木人小大土手目一火不正口鸟氵），
本批真正新增 8 个部件：女 子 又 分 山 石 田 力，部件池 16 → 24。

选字原则：结果字与全部部件都在 1000 字全集内，且是孩子能讲通的会意组合；
插画必须把部件画出来（不是画字的现代意思）。

复用插画（已逐张目检，画面就是部件组合）：
  好 ← xingrong:好（女孩+男孩拉手）
  品 ← 1000:huiyi:品（三块方块品字形）
  掰 ← 1000:huiyi:掰（两只手把面饼掰成两半）
  灶 ← 1000:huiyi:灶（砖灶膛里烧火）
  岩 ← 1000:huiyi:岩（山上顶着石头）
新绘插画（现成图与部件不符，见 NEW_ARTS）：
  双（现成图是两只手套，看不出"手"）→ 两只手并排
  晶（现成图是三块冰晶，不是三个日）→ 三个太阳品字形
  朋 → 两个月亮肩并肩
  出 → 两座山一前一后
  男 → 田地+举臂出力的小孩

schema 与 ../汉语启蒙_素材.py 一致；运行本文件做自检。
"""
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_PARENT = _HERE.parent
if str(_PARENT.parent) not in sys.path:
    sys.path.insert(0, str(_PARENT.parent))

from 识字卡片_素材库 import (  # noqa: E402
    E, C, R, L, P, PG, wrap, ground, drop, kid, hand, star5,
    INK, PAGE, GROUND, RED, RED_D, YEL, YEL_D, TEAL, TEAL_D, TEAL_L,
    BLUE, BLUE_D, WBLUE, SKIN, HAIR, GREEN, GREEN_L, SUN, SUN_L, PINK, WHITE,
)


# ---------------- 新插画 ----------------

def _art_shuang():
    """双：两只手并排放在一起，就是一双。"""
    return wrap(
        ground(),
        hand(250, 286, -8, 0.92),
        hand(510, 286, 8, 0.92),
        P("M 348 190 Q 380 168 412 190", stroke="#e8a13c", w=8),
        P("M 358 158 Q 380 140 402 158", stroke="#e8a13c", w=8),
    )


def _sun(cx, cy, r):
    rays = []
    for i in range(8):
        import math
        a = i * math.pi / 4
        x1, y1 = cx + (r + 16) * math.cos(a), cy + (r + 16) * math.sin(a)
        x2, y2 = cx + (r + 34) * math.cos(a), cy + (r + 34) * math.sin(a)
        rays.append(L(x1, y1, x2, y2, "#e89a1f", 9))
    return wrap(
        C(cx + r * 0.06, cy + r * 0.08, r, "#e89a1f"),
        C(cx, cy, r, SUN),
        C(cx - r * 0.3, cy - r * 0.3, r * 0.24, SUN_L, 0.9),
        # 笑脸
        C(cx - r * 0.28, cy - r * 0.1, r * 0.09, INK),
        C(cx + r * 0.28, cy - r * 0.1, r * 0.09, INK),
        P(f"M {cx-r*0.2} {cy+r*0.22} Q {cx} {cy+r*0.42} {cx+r*0.2} {cy+r*0.22}",
          stroke=INK, w=5),
        *rays)


def _art_jing():
    """晶：三个太阳品字形排一起，亮晶晶。"""
    return wrap(
        ground(),
        _sun(380, 172, 62),
        _sun(258, 330, 62),
        _sun(502, 330, 62),
    )


def _moon(cx, cy, r, flip=1, face=True):
    """月牙：大圆月黄 + 底色圆偏移咬出一弯月牙。"""
    g = wrap(C(cx, cy, r, "#e89a1f"), C(cx, cy - 4, r - 3, YEL))
    bite = C(cx + flip * r * 0.62, cy - r * 0.28, r * 0.82, "#fdf8ec")
    f = ""
    if face:
        f = wrap(
            C(cx - flip * r * 0.34, cy - r * 0.16, r * 0.1, INK),
            P(f"M {cx-flip*r*0.5} {cy+r*0.3} Q {cx-flip*r*0.28} {cy+r*0.52} {cx-flip*r*0.06} {cy+r*0.3}",
              stroke=INK, w=5),
            C(cx - flip * r * 0.18, cy + r * 0.62, r * 0.1, PINK, 0.8))
    return g + bite + f


def _art_peng():
    """朋：两个月亮肩并肩，手拉手。"""
    return wrap(
        ground(),
        P("M 292 236 Q 380 208 468 236", stroke="#e8a13c", w=8),
        _moon(300, 258, 96, flip=1),
        _moon(462, 258, 96, flip=-1),
    )


def _mountain(cx, base, w, h, fill):
    return PG([(cx - w / 2, base), (cx, base - h), (cx + w / 2, base)], fill)


def _art_chu():
    """出：一座山后面又钻出一座山。"""
    return wrap(
        ground(),
        _mountain(452, 428, 400, 250, "#3e9486"),
        _mountain(322, 428, 330, 196, TEAL),
        C(452, 208, 30, WHITE, 0.9),
        P("M 214 428 Q 260 400 300 428", stroke="#4a3226", w=0),
    )


def _art_nan():
    """男：在田里出力气干活的人。"""
    field = wrap(
        R(120, 372, 520, 84, 16, "#c89058"),
        R(132, 382, 496, 62, 10, GREEN),
        L(256, 382, 256, 444, "#5f8f52", 7), L(392, 382, 392, 444, "#5f8f52", 7),
        L(528, 382, 528, 444, "#5f8f52", 7),
        L(132, 413, 628, 413, "#5f8f52", 7),
    )
    return wrap(
        ground(),
        field,
        kid(380, 368, 0.94, arms="up", shirt=BLUE, face="open"),
        drop(300, 118, 12), drop(452, 108, 14),
    )


NEW_ARTS = {
    "双": _art_shuang(),
    "晶": _art_jing(),
    "朋": _art_peng(),
    "出": _art_chu(),
    "男": _art_nan(),
}


# ---------------- 卡片数据 ----------------

def _magic(result, parts, py, tone, story, art_src, life):
    return {"type": "magic", "key": result, "result": result, "parts": parts,
            "pinyin": py, "tone": tone, "story": story, "art_src": art_src,
            "tips": [["怎么玩", "遮住下半张，看两个字先猜一猜，再点「变！」"],
                     ["字的故事", story], ["生活里", life]]}


NEW_CARDS = [
    _magic("好", [["女", "女孩"], ["子", "男孩"]], "hǎo", "第三声",
           "女孩和男孩拉拉手，很好。", "xingrong:好",
           "见到小朋友说「你好」，拉拉手做好朋友。"),
    _magic("双", [["又", "一只手"], ["又", "另一只手"]], "shuāng", "第一声",
           "两只手并排放，就是一双。", "双",
           "数数自己的一双小手；找找一双鞋、一双筷子。"),
    _magic("品", [["口", "小方块"], ["口", "小方块"], ["口", "小方块"]], "pǐn", "第三声",
           "三个方块叠起来，就是品。", "1000:huiyi:品",
           "三个杯子摆成品字形；尝尝苹果说「品尝」。"),
    _magic("掰", [["手", "一只手"], ["分", "分开"], ["手", "另一只手"]], "bāi", "第一声",
           "两只手把东西分开，就是掰。", "1000:huiyi:掰",
           "掰开面包或饼干，边掰边说「掰开」。"),
    _magic("灶", [["火", "火苗"], ["土", "土台"]], "zào", "第四声",
           "土台里烧着火，烧饭的就是灶。", "1000:huiyi:灶",
           "看看家里的灶台，大人做饭时说「灶上开着火」。"),
    _magic("岩", [["山", "大山"], ["石", "石头"]], "yán", "第二声",
           "山上的大石头，就是岩。", "1000:huiyi:岩",
           "爬山时指指大石头说「岩石」，摸一摸硬不硬。"),
    _magic("晶", [["日", "太阳"], ["日", "太阳"], ["日", "太阳"]], "jīng", "第一声",
           "三个太阳亮晶晶。", "晶",
           "看窗上的冰花、天上的星星，说「亮晶晶」。"),
    _magic("朋", [["月", "月亮"], ["月", "月亮"]], "péng", "第二声",
           "两个月亮肩并肩，是好朋友。", "朋",
           "说说自己最好朋友的名字，月圆的晚上找找月亮。"),
    _magic("出", [["山", "一座山"], ["山", "又一座山"]], "chū", "第一声",
           "翻过一座山又一座山，走出来了。", "出",
           "出门时说「出门啦」，回家说「进来啦」。"),
    _magic("男", [["田", "田地"], ["力", "力气"]], "nán", "第二声",
           "在田里出力气干活的人，就是男。", "男",
           "指认家里人：爸爸是男的，爷爷也是男的。"),
]


# ---------------- 自检 ----------------

def _load(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def self_check():
    problems = []
    P = _PARENT.parent          # 孩子/
    ZK = P / "识字卡片_1000字"   # 1000 字项目目录
    ziku = _load(ZK / "字库1000.py", "zc_ziku")
    S = set()
    for g in ziku.GROUPS:
        for it in g["chars"]:
            for c in (list(it) if isinstance(it, tuple) else
                      [it.get("char", it) if isinstance(it, dict) else it]):
                S.add(c)
    py = json.loads((P / "识字卡片_1000字" / "拼音表1000.json").read_text(encoding="utf-8"))

    existing = {"明", "林", "森", "从", "众", "休", "尖", "尘", "看", "坐", "灭", "歪", "鸣", "泪"}

    # 1) SVG 合法性
    for k, v in NEW_ARTS.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except Exception as e:  # noqa: BLE001
            problems.append(f"插画 {k}: {e}")
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            if bad in v:
                problems.append(f"插画 {k} 含禁止标记 {bad}")

    # 2) 字与拼音
    for c in NEW_CARDS:
        res = c["result"]
        if res in existing:
            problems.append(f"{res} 与现有 14 张重复")
        if res not in S:
            problems.append(f"结果字 {res} 不在 1000 字全集")
        want = py.get(res, {})
        if c["pinyin"] != want.get("pinyin") or c["tone"] != want.get("tone"):
            problems.append(f"{res} 拼音/声调不符：{c['pinyin']}/{c['tone']} vs {want}")
        for p in c["parts"]:
            if p[0] not in S:
                problems.append(f"{res} 部件 {p[0]} 不在 1000 字全集")
            if len(p[1]) > 4:
                problems.append(f"{res} 部件词过长 {p[1]}")
        if len(c["story"]) > 24:
            problems.append(f"{res} story 超长（{len(c['story'])} 字）")
        if len(c["tips"][2][1]) > 30:
            problems.append(f"{res} life 超长")
        # 3) art_src 可解析
        src = c["art_src"]
        if src in NEW_ARTS:
            continue
        seg = src.split(":")
        try:
            if seg[0] == "1000":
                arts = {}
                for f in sorted((P / "识字卡片_1000字" / "素材").glob(f"素材1000_{seg[1]}*.py")):
                    arts.update(_load(f, f"zc_{f.stem}").arts())
            else:
                arts = _load(P / f"识字卡片_素材_{seg[0]}.py", f"zc_l_{seg[0]}").arts()
            if seg[-1] not in arts:
                problems.append(f"{res} art_src 指向不存在的插画 {src}")
        except Exception as e:  # noqa: BLE001
            problems.append(f"{res} art_src 解析失败 {src}: {e}")

    n_new_parts = {p[0] for c in NEW_CARDS for p in c["parts"]}
    print(f"新增 {len(NEW_CARDS)} 张；新部件 {len(n_new_parts)} 个：{' '.join(sorted(n_new_parts))}")
    if problems:
        print("问题：")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("会意字扩充数据自检通过 ✓")


if __name__ == "__main__":
    self_check()
