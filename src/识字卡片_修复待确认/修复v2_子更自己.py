#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡修复 v2（子 更 自 己）—— v1 与旧版均被否后的第三稿，核心=简单直白。

v2 方案（修复方案.md「v2 方案」节，v1 被否原因不再犯）：
- 子=切开的西瓜块：红瓤半圆（平底朝上、深绿皮弧在底）、黑籽 5 颗嵌在瓤上、
  旁边 1-2 颗放大的黑籽——"子"=籽，生活经验直给；不画手（上轮手画崩）、无土无芽。
- 更=左堆 3 颗红球、右堆 6 颗蓝球（两堆分开、都是金字塔堆、数量差一眼可比），
  小孩站中间、手臂伸向多的蓝堆——"更多"。
- 自=小孩双臂上举，右手扶着一面圆镜的柄，镜框里映出一张同款笑脸——镜中人=自己；
  不再指鼻子（上轮读成挖鼻）。
- 己=小孩弯腰，一只手按住地上的球、另一只手伸向开盖玩具箱（箱内已有玩具）——
  自己的事自己做；不再背书包（上轮读不出"自己"）。

硬规则：760×480 内部标记（无 svg 包装/defs/use/text/image/文字数字）；
第一笔 ground()；只用素材库 PALETTE 同族色；kid 头身比 1:2.2–2.6、
臂长≤0.55×身高；手必须连在臂端；主体居中、高 45–75%；友好脸；一卡一事。
己卡小孩为弯腰姿势，kid() 无此姿态，按 kid() 比例（s=0.9）自绘：
直立双腿 + 上身组（躯干/头/脸）绕髋 rotate(32) 前倾，双臂在世界坐标补画、
均从旋转后的肩位连到手端。
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_fix_v2", os.path.join(_HERE, "..", "识字卡片_素材库.py"))


def _seed(cx, cy, r, rot=0):
    """一颗黑籽（水滴形，尖朝上），rot=旋转角；小高光（别大得像眼睛）。"""
    g = f'<g transform="rotate({rot} {cx} {cy})">' + lib.drop(cx, cy, r, lib.INK) + "</g>"
    g += lib.E(cx - r * 0.15, cy + r * 0.12, r * 0.18, r * 0.3, lib.WHITE, 0.35)
    return g


# ---------- 子：切开的西瓜块 + 放大黑籽 ----------
def art_子():
    g = lib.ground()
    # 瓜皮（深绿）→ 内皮（浅绿）→ 瓤底（深红）→ 瓤（红，上移留深色弧）
    g += lib.P("M 130 252 A 200 200 0 0 0 530 252 Z", "#5f8f52")
    g += lib.P("M 157 249 A 173 173 0 0 0 503 249 Z", lib.GREEN_L)
    g += lib.P("M 180 252 A 150 150 0 0 0 480 252 Z", lib.RED_D)
    g += lib.P("M 189 247 A 141 141 0 0 0 471 247 Z", lib.RED)
    # 5 颗黑籽嵌在瓤上，尖都朝向瓜心
    g += _seed(280, 296, 14, 46)
    g += _seed(380, 296, 14, -46)
    g += _seed(330, 336, 14, 0)
    g += _seed(296, 364, 14, 16)
    g += _seed(364, 364, 14, -16)
    # 旁边放大的两颗黑籽
    g += _seed(614, 222, 46, 8)
    g += _seed(640, 346, 32, -10)
    return g


# ---------- 更：3 红球 vs 6 蓝球，小孩伸向多的那堆 ----------
def art_更():
    g = lib.ground()
    # 左堆：3 颗红球（2 下 1 上）
    g += lib.ball(150, 412, 32, lib.RED, lib.RED_D, lib.PINK)
    g += lib.ball(214, 412, 32, lib.RED, lib.RED_D, lib.PINK)
    g += lib.ball(182, 352, 32, lib.RED, lib.RED_D, lib.PINK)
    # 右堆：6 颗蓝球（3 下 2 中 1 上）
    g += lib.ball(516, 412, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    g += lib.ball(580, 412, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    g += lib.ball(644, 412, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    g += lib.ball(548, 356, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    g += lib.ball(612, 356, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    g += lib.ball(580, 300, 32, lib.BLUE, lib.BLUE_D, lib.WBLUE)
    # 小孩站中间，手指伸向蓝堆（多的一边）
    g += lib.kid(380, 440, s=0.75, arms="point", point_at=(560, 330),
                 face="open", look=(1.5, -0.6))
    # 蓝堆上方两粒小星光（多的那堆）
    g += lib.PG([(585, 232), (592, 241), (585, 250), (578, 241)], lib.SUN_L)
    g += lib.PG([(640, 262), (645, 269), (640, 276), (635, 269)], lib.SUN_L)
    return g


# ---------- 自：举圆镜照自己，镜中映出笑脸 ----------
def art_自():
    g = lib.ground()
    # 小孩双臂上举（右手正好扶到镜柄），蓝衫
    g += lib.kid(350, 442, s=0.72, arms="up", face="smile",
                 look=(1.2, -1), shirt=lib.BLUE)
    # 圆镜：柄（下端落在右手）→ 金框 → 浅色镜面
    g += lib.R(398, 242, 24, 46, 11, lib.WOOD_D)
    g += lib.C(422, 180, 68, lib.YEL)
    g += lib.C(422, 180, 55, "#eef6fa")
    # 镜中人：同款头发的一张笑脸
    g += lib.C(422, 187, 35, lib.SKIN)
    g += lib.P("M 392 176 Q 396 145 422 143 Q 448 145 452 176 "
               "Q 437 168 422 172 Q 407 168 392 176 Z", lib.HAIR)
    for ex in (409, 435):
        g += lib.E(ex, 188, 5.5, 7, lib.INK)
        g += lib.C(ex + 1, 185, 2, lib.WHITE)
    g += lib.P("M 411 205 Q 422 213 433 205", stroke=lib.INK, w=4.5)
    g += lib.C(400, 199, 6, lib.PINK, 0.8)
    g += lib.C(444, 199, 6, lib.PINK, 0.8)
    # 镜面高光（压在映像上）
    g += lib.E(390, 150, 8, 14, lib.WHITE, 0.7)
    # 镜角小星光
    g += lib.PG([(506, 118), (512, 126), (506, 134), (500, 126)], lib.SUN_L)
    return g


# ---------- 己：弯腰把地上的球捡进玩具箱 ----------
def art_己():
    """己（用户已选定）：淡黄高亮套住小孩 + 一支箭头绕一圈指回本人——'指回自己'。"""
    g = lib.ground()
    g += lib.E(380, 295, 148, 172, "#fdf0c2")
    g += lib.kid(380, 446, s=1.08, pose="stand", face="smile", shirt=lib.BLUE)
    g += lib.P("M 560 330 Q 640 150 470 118", stroke=lib.TEAL, w=10)
    g += f'<polygon points="452,112 492,108 470,142" fill="{lib.TEAL}"/>'
    return g


ARTS = {"子": art_子(), "更": art_更(), "自": art_自(), "己": art_己()}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    expect = {"子", "更", "自", "己"}
    assert set(ARTS) == expect, f"键不一致：多 {set(ARTS) - expect} 缺 {expect - set(ARTS)}"

    g0 = lib.ground()
    problems = []
    for k, v in ARTS.items():
        try:
            ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
                          + v + "</svg>")
        except ET.ParseError as e:
            problems.append((k, f"XML {e}"))
        for bad in ("<svg", "<defs", "<use", "<text", "<image", "href"):
            if bad in v:
                problems.append((k, f"违禁标记 {bad}"))
        if not v.startswith(g0):
            problems.append((k, "第一笔不是 ground()"))
    print("v2 自检（子更自己）：" + ("全部通过 ✓" if not problems else f"问题 {problems}"))
    assert not problems, "自检未通过"
