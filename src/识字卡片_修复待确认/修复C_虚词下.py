#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画——批次C 修复（虚词下 5 字）：更 自 己 就 了。

修复要点（修复方案.md 批次C，独立待确认稿，确认后才并入正式文件）：
- 更=地面两组脚印落点（第一近第二远、都画圈），小孩正向远落点腾空；
- 自=食指点自己鼻尖（正面，胳膊自然弯不横穿脸：肘向外、前臂贴脸侧上去，
  只有手指碰到鼻尖；因 kid() 单臂不可替换且直臂点鼻必横穿脸，本卡用
  素材库原语按 kid() 比例自绘，头身比与画法一致）；
- 己=自己背书包（书包在身后露边，胸前红肩带，双手拉肩带，自信笑）；
- 就=球放矮凳上，小孩微笑伸手即将碰到（指尖与球留一指缝，轻松不使劲）；
- 了=坐桌前拍肚皮满足笑，桌上空碗见底+立勺（吃完的完成态）。

通用硬规则：画布 760×480 内部标记（无 svg 包装/defs/use/text/image/文字数字）；
第一笔 ground()；只用素材库 PALETTE 及同族色；kid 头身比 1:2.2–2.6、
臂长≤0.55×身高；手必须连在臂端；一卡一事。
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_fix_c", os.path.join(_HERE, "..", "识字卡片_素材库.py"))


# ---------- 本组小工具 ----------
def _dash_arc(d, color=lib.TEAL_D, w=6):
    """点状虚线弧（跳远轨迹）。"""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            'stroke-linecap="round" stroke-dasharray="1 16"/>')


def _print(x, y, rot):
    """一个鞋底脚印。"""
    return (f'<g transform="rotate({rot} {x} {y})">'
            + lib.E(x, y, 11.5, 6.8, lib.INK, 0.9) + "</g>")


def _cover_bent_arm(sho, x, s, side, gx, gy):
    """把 kid() 的默认下垂臂原地覆盖成「肘向外、手扣在目标位」的弯臂。

    上臂沿原臂线（肩→原手位）加宽覆盖（同线同端点，宽 34s>30s，圆头
    端帽半径 17s>原手 13s，正好盖住原臂与原手）；前臂从原臂末端折向
    (gx,gy)（相对 (x,sho) 的 s 单位坐标）；手长在臂端。sho 由调用方按
    姿势给出（站姿 y-168s，坐姿 y-152s）。
    """
    sx, sy = x + 44 * s * side, sho + 6 * s
    ex, ey = x + 64 * s * side, sho + 78 * s
    hx, hy = x + gx * s * side, sho + gy * s
    return lib.wrap(
        lib.L(sx, sy, ex, ey, lib.SKIN, 34 * s),
        lib.L(ex, ey, hx, hy, lib.SKIN, 30 * s),
        lib.C(hx, hy, 13 * s, lib.SKIN))


# ---------- 插画 ----------
def art_更():
    """更：第二跳更远——近落点与远落点都画圈放脚印，小孩正向远点腾空。"""
    g = lib.ground()
    # 跳跃轨迹（垫底，从近落点甩向远落点）
    g += _dash_arc("M 270 404 Q 424 292 586 414")
    # 第一落点（近）：圈 + 一组脚印
    g += lib.E(246, 434, 52, 15, lib.TEAL_L)
    g += lib.E(246, 434, 40, 10, lib.PAGE)
    g += _print(232, 431, -14)
    g += _print(260, 435, 10)
    # 第二落点（远）：更大的圈 + 张得更开的脚印
    g += lib.E(606, 436, 58, 17, lib.TEAL_L)
    g += lib.E(606, 436, 45, 11.5, lib.PAGE)
    g += _print(582, 430, -22)
    g += _print(630, 437, 18)
    # 腾空的小孩（奔跑姿势双脚离地，朝右边远点飞跃）
    kid_air = lib.kid(402, 386, s=0.78, pose="sprint", arms="up",
                      face="open", look=(1.5, -0.4))
    g += f'<g transform="rotate(6 402 386)">{kid_air}</g>'
    # 起跳速度线
    g += lib.L(306, 296, 274, 286, lib.TEAL_L, 6)
    g += lib.L(296, 346, 262, 338, lib.TEAL_L, 5)
    return g


def art_自():
    """自：正面小孩食指点自己鼻尖——肘向外自然弯，前臂贴脸侧上去，不横穿脸。"""
    g = lib.ground()
    x, hcy, hd = 368, 210, 57
    # 腿和脚
    g += lib.R(338, 342, 26, 84, 12, lib.BLUE_D)
    g += lib.R(372, 342, 26, 84, 12, lib.BLUE_D)
    g += lib.E(351, 430, 21, 10, lib.INK, 0.85)
    g += lib.E(385, 430, 21, 10, lib.INK, 0.85)
    # 身体（蓝衫，与正式组自卡同色）
    g += lib.P("M 312 282 Q 310 358 328 360 L 408 360 Q 426 358 424 282 "
               "Q 368 266 312 282 Z", lib.BLUE)
    # 左臂自然下垂
    g += lib.L(324, 288, 304, 360, lib.SKIN, 30)
    g += lib.C(304, 360, 13, lib.SKIN)
    # 头：耳、脸、头发
    g += lib.C(312, 220, 10, lib.SKIN)
    g += lib.C(424, 220, 10, lib.SKIN)
    g += lib.C(x, hcy, hd, lib.SKIN)
    g += lib.P("M 312 190 Q 317 143 368 140 Q 419 143 424 190 "
               "Q 399 180 368 186 Q 337 180 312 190 Z", lib.HAIR)
    # 五官（眼、眉、鼻、笑、腮红）
    for ex in (346, 390):
        g += lib.E(ex, 202, 10, 13, lib.INK)
        g += lib.C(ex, 197, 3.4, lib.WHITE)
    g += lib.P("M 332 180 Q 346 171 360 177", stroke=lib.HAIR, w=6)
    g += lib.P("M 376 177 Q 390 171 404 180", stroke=lib.HAIR, w=6)
    g += lib.E(370, 224, 8, 6, lib.SKIN_D)              # 小鼻子（指尖点这里）
    g += lib.P("M 348 238 Q 368 252 388 238", stroke=lib.INK, w=7)
    g += lib.C(322, 226, 11, lib.PINK, 0.8)
    g += lib.C(414, 226, 11, lib.PINK, 0.8)
    # 右臂：肩→肘向外→前臂贴脸侧外上行→手停在脸旁（不贴脸），食指伸向鼻尖；
    # 指腹下加一道 SKIN_D 细影，手指压在脸颊上时也能看清轮廓
    g += lib.L(412, 288, 444, 322, lib.SKIN, 30)
    g += lib.L(444, 322, 436, 252, lib.SKIN, 28)
    g += lib.C(435, 246, 12, lib.SKIN)
    g += lib.L(424, 242, 379, 228, lib.SKIN, 11)
    g += lib.L(422, 247, 381, 233, lib.SKIN_D, 3)
    g += lib.C(377, 227, 6, lib.SKIN)
    return g


def art_己():
    """己：自己的事情自己做——小孩自己背书包，双手拉住胸前肩带，自信笑。"""
    x, y, s = 380, 436, 0.9
    sho = y - 168 * s
    g = lib.ground()
    # 身后的书包（先画：中间被身体挡住，露出颈旁上沿和两侧）
    g += lib.R(x - 58 * s, sho - 26 * s, 116 * s, 116 * s, 24 * s, lib.YEL)
    g += lib.R(x - 58 * s, sho + 62 * s, 116 * s, 20 * s, 10 * s, lib.YEL_D)
    # 小孩（青衫，与自卡蓝衫区分）
    g += lib.kid(x, y, s=s, arms="down", face="smile", look=(0, 0.3),
                 shirt=lib.TEAL)
    # 红肩带：先扣过两肩，再垂到胸前
    g += lib.R(x - 40 * s, sho - 9 * s, 20 * s, 15 * s, 7 * s, lib.RED)
    g += lib.R(x + 20 * s, sho - 9 * s, 20 * s, 15 * s, 7 * s, lib.RED)
    g += lib.R(x - 38 * s, sho + 2 * s, 20 * s, 58 * s, 9 * s, lib.RED)
    g += lib.R(x + 18 * s, sho + 2 * s, 20 * s, 58 * s, 9 * s, lib.RED)
    # 双手拉肩带：肘向外，手扣在胸前肩带上（手上方留出一截红带）
    g += _cover_bent_arm(sho, x, s, -1, 28, 44)
    g += _cover_bent_arm(sho, x, s, +1, 28, 44)
    # 自信的小闪光
    g += lib.star5(300, 176, 13, lib.SUN_L)
    g += lib.star5(462, 196, 11, lib.SUN_L)
    return g


def art_就():
    """就：伸手就够到——球放矮凳上，小孩微笑伸手即将碰到，指尖与球留一指缝。"""
    import math
    g = lib.ground()
    # 矮凳（比桌子矮一截）
    g += lib.R(446, 378, 20, 64, 8, lib.WOOD_D)
    g += lib.R(524, 378, 20, 64, 8, lib.WOOD_D)
    g += lib.R(432, 356, 126, 24, 10, lib.WOOD)
    g += lib.R(432, 374, 126, 10, 5, lib.WOOD_D)
    # 凳上的球
    bcx, bcy, br = 495, 322, 36
    g += lib.ball(bcx, bcy, br, lib.YEL, lib.YEL_D, lib.SUN_L)
    # 小孩伸手：臂指向球心方向，kid() 手心在肩前 88s 处，指尖补一小段食指
    kx, ky, s = 313, 436, 0.9
    sho = ky - 168 * s
    sx, sy = kx + 44 * s, sho + 6 * s
    dl = math.hypot(bcx - sx, bcy - sy)
    ux, uy = (bcx - sx) / dl, (bcy - sy) / dl
    g += lib.kid(kx, ky, s=s, arms="point",
                 point_at=(sx + 170 * ux, sy + 170 * uy),
                 face="smile", look=(1.8, -0.5))
    hcx, hcy = sx + 88 * s * ux, sy + 88 * s * uy       # 手心位置（同 kid()）
    fx, fy = hcx + 14.5 * ux, hcy + 14.5 * uy           # 食指尖：距球面约一指缝
    g += lib.L(hcx + 6 * ux, hcy + 6 * uy, fx, fy, lib.SKIN, 9)
    g += lib.C(fx, fy, 4, lib.SKIN)
    # 轻松感：球上小闪光（不使劲、没汗珠）
    g += lib.PG([(544, 272), (551, 281), (544, 290), (537, 281)], lib.SUN_L)
    g += lib.PG([(566, 306), (570, 312), (566, 318), (562, 312)], lib.SUN_L)
    return g


def art_了():
    """了：我吃完饭了——坐桌前拍肚皮满足笑，桌上空碗见底+立勺（完成态）。"""
    x, y, s = 320, 428, 0.85
    sho = y - 152 * s                                   # 坐姿肩高（kid() sit 分支）
    g = lib.ground()
    # 坐着的小孩
    g += lib.kid(x, y, s=s, pose="sit", face="smile", look=(0.6, 0.3))
    # 双手拍肚皮：肘向外，两手扣在肚皮两侧
    g += _cover_bent_arm(sho, x, s, -1, 20, 52)
    g += _cover_bent_arm(sho, x, s, +1, 20, 52)
    # 拍拍小动线
    g += lib.P("M 283 334 Q 274 346 282 356", stroke=lib.TEAL_L, w=5)
    g += lib.P("M 357 334 Q 366 346 358 356", stroke=lib.TEAL_L, w=5)
    # 小桌（在小孩身前，桌面低于肚皮，拍肚皮的手露在桌沿上方）
    g += lib.table(x, top=362, w=260, leg_h=52, slab=40)
    # 空碗见底（无饭）+ 碗内空膛 + 立着的勺
    g += lib.bowl(400, 328, 42, rice=False)
    g += lib.E(400, 332, 33, 8, "#b45a3c")
    g += lib.E(386, 352, 9, 4, lib.WHITE, 0.6)
    g += lib.L(400, 268, 400, 334, "#e8a13c", 9)
    g += lib.E(400, 344, 19, 13, "#dfe3e6")
    g += lib.E(400, 346, 13, 8, "#c9cdd1")
    # 吃得干干净净的小闪光
    g += lib.PG([(368, 182), (375, 191), (368, 200), (361, 191)], lib.SUN_L)
    g += lib.PG([(470, 250), (476, 258), (470, 266), (464, 258)], lib.SUN_L)
    return g


ARTS = {"更": art_更(), "自": art_自(), "己": art_己(), "就": art_就(), "了": art_了()}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    expect = {"更", "自", "己", "就", "了"}
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
                problems.append((k, bad))
        if not v.startswith(g0):
            problems.append((k, "第一笔不是 ground()"))
    print("批次C 自检：" + ("全部通过 ✓" if not problems else f"问题 {problems}"))
    assert not problems, "自检未通过"
