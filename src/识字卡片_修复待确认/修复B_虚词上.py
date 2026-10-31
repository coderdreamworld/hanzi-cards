#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡修复批次B（虚词上）：真 边 旁 子 什——待用户确认，不并入正式文件。

按 修复方案.md 批次B逐字实现（按例句画场景）：
- 真（真心送给你）：小孩双手捧大红心递给对面张开手的小孩（捧出真心），
  心的物件与"送"（礼盒）、"给"（苹果）区分。
- 边（杯子放在桌边）：杯子放在桌面边缘、约一半探出微倾要掉，小孩伸手扶住杯子。
- 旁（球在桌子旁边）：桌子居中，红球紧贴桌腿放置（球缘与腿缘相触），小孩站在球旁看。
- 子（种子）：两只手从下方摊掌捧 3 颗深色水滴形种子；无土无芽（避免与"芽"卡撞车）。
- 什（这是什么东西？）：小孩指着桌上新奇玩具（小机器人）发问，头顶问号；
  用"指实物发问"与"问"卡（举手问号）区分。

硬规则：760×480 内部标记（无 svg 包装/defs/use/text/image/文字数字）；
第一笔 ground()；只用素材库 PALETTE 及同族色；主体居中偏移≤15%、高 45–75%；
手必须连在臂端；一张卡只讲一件事。
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_fix_b", os.path.join(_HERE, "..", "识字卡片_素材库.py"))


def qmark(cx, cy, s, color=lib.INK):
    """大问号（钩+柄+点），提问专用符号。"""
    g = lib.P(f"M {cx - s} {cy - 1.05 * s} Q {cx - s * 0.85} {cy - 2.25 * s} {cx} {cy - 2.25 * s} "
              f"Q {cx + s * 0.85} {cy - 2.25 * s} {cx + s * 0.9} {cy - 1.15 * s} "
              f"Q {cx + s * 0.9} {cy - 0.3 * s} {cx} {cy + 0.05 * s} L {cx} {cy + 0.6 * s}",
              stroke=color, w=0.3 * s)
    return g + lib.C(cx, cy + 1.2 * s, 0.19 * s, color)


# ---------- 插画 ----------
def art_真():
    """真心送给你：左孩双手捧大红心递出，右孩高举双手开心来接。"""
    g = lib.ground()
    # 捧心的小孩（左）：双臂合拢到胸前
    g += lib.kid(272, 446, s=0.85, arms="clap", face="smile", look=(1, -1))
    # 大红心画在胸前手上（心顶低于下巴，不遮笑脸）
    g += lib.heart(288, 348, 52, lib.RED_D)
    g += lib.heart(284, 344, 52, lib.RED)
    g += lib.C(262, 322, 8, lib.WHITE, 0.75)
    # 双手按在心上的小手圆+短腕（与臂端相连）
    g += lib.L(256, 314, 260, 326, lib.SKIN, 17)
    g += lib.L(288, 314, 284, 326, lib.SKIN, 17)
    g += lib.C(260, 330, 11.5, lib.SKIN)
    g += lib.C(284, 330, 11.5, lib.SKIN)
    # 接心的小孩（右）：双手高举张开，开心大叫
    g += lib.kid(560, 446, s=0.85, arms="up", face="open", look=(-1, -1), shirt=lib.TEAL)
    return g


def art_边():
    """杯子放在桌边：半只杯子探出桌沿微倾要掉，小孩伸手扶住。"""
    g = lib.ground()
    g += lib.E(330, 450, 250, 12, "#a5d0bd", 0.55)                      # 桌影
    g += lib.table(cx=320, top=322, w=300, leg_h=76, slab=42)           # 桌（右沿 x=470）
    g += lib.R(444, 322, 26, 42, 12, lib.TEAL)                          # 桌边抹青（提示"边"）
    g += lib.E(504, 316, 52, 7, lib.INK, 0.07)                          # 杯在桌上的影
    # 不透明水杯：中心压在桌沿 470 上，约一半探出，整体微倾要掉
    cup = lib.wrap(
        lib.R(410, 182, 120, 140, 18, lib.WBLUE),                       # 杯身
        lib.R(417, 246, 106, 66, 12, "#a5d9f0"),                        # 水
        lib.E(470, 246, 53, 10, "#c9e9f7"),                             # 水面
        lib.R(422, 196, 13, 44, 6.5, lib.WHITE, 0.6))                   # 高光
    g += f'<g transform="rotate(7 470 322)">{cup}</g>'
    g += lib.L(558, 204, 580, 194, lib.WBLUE, 6)                        # 晃动小线
    g += lib.L(554, 248, 578, 244, lib.WBLUE, 6)
    g += lib.drop(542, 354, 10, lib.WBLUE)                              # 檐角欲滴的水珠
    g += lib.E(544, 446, 24, 6, lib.INK, 0.07)                          # 探出部分的落点影
    # 小孩伸手扶杯（臂端手落在杯身右侧）
    g += lib.kid(606, 446, s=0.85, arms="point", point_at=(506, 288),
                 face="o", look=(1, -1))
    return g


def art_旁():
    """球在桌子旁边：红球紧贴右桌腿，小孩站在球旁边看。"""
    g = lib.ground()
    g += lib.E(340, 450, 220, 12, "#a5d0bd", 0.55)                      # 桌影
    g += lib.table(cx=340, top=320, w=260, leg_h=82, slab=42)           # 右腿 406..436
    g += lib.ball(484, 398, 48, lib.RED, lib.RED_D, lib.PINK)           # 球左缘 436=腿右缘，紧贴
    # 小孩站在球旁边看球
    g += lib.kid(590, 446, s=0.78, arms="down", face="smile", look=(-1, -1))
    return g


def _palm_up(cx, cy, s):
    """一只摊掌向上的手（侧上视角）：袖口+四根圆头手指（指尖朝卡心上方）+
    椭圆掌压住指根+拇指圆。s=1 画左手，s=-1 镜像画右手。"""
    g = ""
    # 袖口（最底层，在外侧下角，掌根压住）
    scx = cx - s * 105
    g += (f'<g transform="rotate({s * -18} {scx} {cy + 48})">'
          + lib.R(scx - 39, cy + 8, 78, 80, 24, "#f2b03c")
          + lib.R(scx - 39, cy + 8, 78, 18, 9, "#e8a13c") + "</g>")
    # 四根手指：从掌缘立起、指尖向内上收拢成碗沿
    for fx, fy, rot in ((86.5, -47, 18), (56.5, -54, 10), (26.5, -57, 3), (-4, -57, -4)):
        fcx, fcy = cx + s * fx, cy + fy
        g += (f'<g transform="rotate({s * rot} {fcx} {fcy})">'
              + lib.R(fcx - 13.5, fcy - 40, 27, 78, 13.5, lib.SKIN) + "</g>")
    # 手掌（盖住指根）+ 拇指圆
    g += (f'<ellipse cx="{cx}" cy="{cy}" rx="100" ry="62" fill="{lib.SKIN}" '
          f'transform="rotate({s * -18} {cx} {cy})"/>')
    g += lib.C(cx - s * 49, cy - 56, 19, lib.SKIN)
    return g


def art_子():
    """种子：两只手从下方摊掌向上、指尖合围成碗，捧 3 颗深色水滴形种子（无土无芽）。"""
    g = lib.ground()
    g += _palm_up(245, 380, 1)
    g += _palm_up(515, 380, -1)
    # 3 颗深色水滴形种子（尖朝上），品字形躺在两掌合围的碗里
    for sx, sy, sr in ((365, 340, 32), (395, 340, 32), (380, 280, 35)):
        g += lib.drop(sx, sy, sr, lib.INK)
        g += lib.E(sx - sr * 0.28, sy + sr * 0.2, sr * 0.22, sr * 0.32, lib.WHITE, 0.45)
    return g


def art_什():
    """这是什么：小孩指着桌上新奇玩具小机器人发问，头顶问号。"""
    g = lib.ground()
    g += lib.E(510, 450, 210, 11, "#a5d0bd", 0.55)                      # 桌影
    g += lib.table(cx=510, top=318, w=250, leg_h=78, slab=40)           # 桌面 385..635
    # 新奇玩具：小机器人（天线圆球+方头圆眼+方身按钮+短臂短腿）
    g += lib.L(530, 162, 530, 140, lib.INK, 5)
    g += lib.C(530, 133, 9, lib.RED)                                    # 天线球
    g += lib.R(468, 222, 20, 48, 10, lib.BLUE_D)                        # 左臂
    g += lib.R(572, 222, 20, 48, 10, lib.BLUE_D)                        # 右臂
    g += lib.R(503, 280, 16, 22, 6, lib.BLUE_D)                         # 左腿
    g += lib.R(541, 280, 16, 22, 6, lib.BLUE_D)                         # 右腿
    g += lib.R(497, 298, 24, 20, 8, lib.TEAL_D)                         # 左脚
    g += lib.R(539, 298, 24, 20, 8, lib.TEAL_D)                         # 右脚
    g += lib.R(486, 214, 88, 70, 16, lib.TEAL)                          # 身体
    g += lib.R(500, 228, 60, 42, 10, lib.TEAL_L)                        # 肚panel
    g += lib.C(530, 249, 8, lib.RED)                                    # 按钮灯
    g += lib.R(494, 162, 72, 46, 14, lib.BLUE)                          # 头
    g += lib.C(515, 184, 9, lib.WHITE)
    g += lib.C(545, 184, 9, lib.WHITE)
    g += lib.C(512, 185, 4, lib.INK)                                    # 眼珠看向小孩
    g += lib.C(542, 185, 4, lib.INK)
    g += lib.P("M 522 196 Q 530 202 538 196", stroke=lib.INK, w=4)      # 微笑
    # 小孩指着机器人发问（臂端手落在机器人手臂上）
    g += lib.kid(280, 446, s=0.92, arms="point", point_at=(462, 254),
                 face="o", look=(2, -1))
    g += qmark(372, 138, 44)                                            # 头顶大问号
    return g


ARTS = {"真": art_真(), "边": art_边(), "旁": art_旁(), "子": art_子(), "什": art_什()}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    expect = {"真", "边", "旁", "子", "什"}
    bad = []
    for k, v in ARTS.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, f"解析失败 {e}"))
        for t in ("<text", "<use", "<defs", "<image", "href", "<svg", "xmlns"):
            if t in v:
                bad.append((k, f"违禁标记 {t}"))
        if not v.startswith("<ellipse"):                                # 第一笔必须是 ground()
            bad.append((k, "第一笔不是 ground"))
    if set(ARTS) != expect:
        bad.append(f"键集合不一致：{sorted(set(ARTS) ^ expect)}")
    print(f"批次B arts 数：{len(ARTS)}")
    print("SVG 校验：" + ("全部通过 ✓" if not bad else f"问题 {bad}"))
    assert set(ARTS) == expect and not bad, "自检未通过"
    print("自检通过 ✓")
