# -*- coding: utf-8 -*-
"""识字卡 v2 修复稿：别 / 了 / 肚（第二轮重画，待用户确认，不并入正式素材文件）。

v2 方向（修复方案.md「v2 方案」节，核心=简单直白，上一轮否决方向不再用）：
- 别（别跑，慢慢走）：大人拉住小孩手腕——大人立小孩身后侧，绿长袖手臂从肩
  连到手，深一号肤色的大手压在小孩腕上（两手交叠点清楚），小孩前倾迈步要跑
  +身后速度线。人与人有身体接触。
- 了（我吃完饭了）：桌上碗倒扣（ strongest 完成信号）+小孩双手叉腰看碗满足笑。
- 肚（吃饱了，肚子圆）：全身小孩（非特写），衣摆上撩露出圆肚子+肚脐，
  双手扶肚两侧，嘴角满足；脚边放空碗呼应吃饱。

通用硬规则：画布 760×480 内部标记（无 svg 包装/defs/use/text/image/文字数字）；
第一笔 ground()；只用素材库 PALETTE 及同族色；kid 头身比 1:2.2–2.6（全用
素材库 kid() 比例）、臂长≤0.55×身高；手必须连在臂端；主体居中、高度 45–75%；
友好脸；一卡一事。
"""
import importlib.util
import math
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_fix_v2", os.path.join(_HERE, "..", "识字卡片_素材库.py"))


# ---------- 本组小工具 ----------
def _kid_akimbo(x, y, s, look=(1.7, 0.5), shirt=None, skin=None, hair_color=None):
    """正面叉腰小孩（按素材库 kid() 同款比例自绘，头身 1:2.42）。

    双臂从肩出发：上臂外撑、肘顶在腰胸高度，前臂斜折回髋上手位，手长在臂端
    ——臂、腰之间露出三角空档，叉腰一眼可辨（无默认垂臂需要遮盖）。
    """
    shirt = shirt or lib.BLUE
    skin = skin or lib.SKIN
    hair_color = hair_color or lib.HAIR
    f = []
    sho, hip, hd = y - 168 * s, y - 96 * s, 62 * s
    hcy = sho - 8 * s - hd
    # 腿脚（站姿，同 kid() stand）
    f.append(lib.R(x - 30 * s, hip - 10 * s, 26 * s, 84 * s, 12 * s, lib.BLUE_D))
    f.append(lib.R(x + 4 * s, hip - 10 * s, 26 * s, 84 * s, 12 * s, lib.BLUE_D))
    f.append(lib.E(x - 17 * s, y - 6 * s, 21 * s, 10 * s, lib.INK, 0.85))
    f.append(lib.E(x + 17 * s, y - 6 * s, 21 * s, 10 * s, lib.INK, 0.85))
    # 身体
    f.append(lib.P(f"M {x-56*s} {sho} Q {x-58*s} {hip+6*s} {x-40*s} {hip+8*s} L {x+40*s} {hip+8*s} "
                   f"Q {x+58*s} {hip+6*s} {x+56*s} {sho} Q {x} {sho-16*s} {x-56*s} {sho} Z", shirt))
    # 双臂叉腰：肩→肘外撑（腰胸高）→前臂折回髋上
    for sd in (-1, 1):
        sx, sy = x + 44 * s * sd, sho + 6 * s
        jx, jy = x + 84 * s * sd, sho + 52 * s
        hx, hy = x + 50 * s * sd, sho + 74 * s
        f.append(lib.L(sx, sy, jx, jy, skin, 30 * s))
        f.append(lib.L(jx, jy, hx, hy, skin, 28 * s))
        f.append(lib.C(hx, hy, 13 * s, skin))
    # 头：耳、脸、头发
    f.append(lib.C(x - 58 * s, hcy + 10 * s, 11 * s, skin))
    f.append(lib.C(x + 58 * s, hcy + 10 * s, 11 * s, skin))
    f.append(lib.C(x, hcy, hd, skin))
    top, bang = hcy - hd, hcy - hd * 0.42
    f.append(lib.P(f"M {x-hd*0.98} {hcy-hd*0.35} Q {x-hd*0.9} {top-hd*0.18} {x} {top-hd*0.12} "
                   f"Q {x+hd*0.9} {top-hd*0.18} {x+hd*0.98} {hcy-hd*0.35} "
                   f"Q {x+hd*0.55} {bang-hd*0.1} {x} {bang} "
                   f"Q {x-hd*0.55} {bang-hd*0.1} {x-hd*0.98} {hcy-hd*0.35} Z", hair_color))
    # 眼睛（看向 look 偏移）+ 眉毛
    lx, ly = look
    for ex in (-22, 22):
        f.append(lib.E(x + ex * s, hcy - 8 * s, 10 * s, 13 * s, lib.INK))
        f.append(lib.C(x + ex * s + lx * s, hcy - 13 * s + ly * s, 3.4 * s, lib.WHITE))
    f.append(lib.P(f"M {x-36*s} {hcy-hd*0.52} Q {x-22*s} {hcy-hd*0.62} {x-8*s} {hcy-hd*0.54}",
                   stroke=hair_color, w=6 * s))
    f.append(lib.P(f"M {x+8*s} {hcy-hd*0.54} Q {x+22*s} {hcy-hd*0.62} {x+36*s} {hcy-hd*0.52}",
                   stroke=hair_color, w=6 * s))
    # 满足的笑 + 腮红
    my = hcy + 26 * s
    f.append(lib.P(f"M {x-20*s} {my} Q {x} {my+16*s} {x+20*s} {my}", stroke=lib.INK, w=7 * s))
    f.append(lib.C(x - 44 * s, hcy + 14 * s, 11 * s, lib.PINK, 0.8))
    f.append(lib.C(x + 44 * s, hcy + 14 * s, 11 * s, lib.PINK, 0.8))
    return lib.wrap(*f)


def _hand_on_belly(sho, x, s, side, hand_x, hand_y):
    """把 kid() 默认下垂臂覆盖成「扶肚臂」：第一段盖默认臂线，第二段折向肚侧。"""
    sx, sy = x + 44 * s * side, sho + 6 * s
    ex, ey = x + 64 * s * side, sho + 78 * s
    hx, hy = x + hand_x * s * side, hand_y
    return lib.wrap(
        lib.L(sx, sy, ex, ey, lib.SKIN, 36 * s),
        lib.L(ex, ey, hx, hy, lib.SKIN, 30 * s),
        lib.C(hx, hy, 14 * s, lib.SKIN))


def _upside_down_bowl(cx, by, r=48, h=38):
    """倒扣的碗：桌面上一圈碗口沿（扣地）+ 穹顶碗身 + 顶上碗足圈 + 高光。"""
    return lib.wrap(
        lib.E(cx, by + 2, r + 8, 7, "#b45a3c", 0.4),                # 桌面落影
        lib.E(cx, by + 1, r + 4, 6.5, "#b45a3c"),                   # 扣在桌上的碗口沿
        lib.P(f"M {cx - r} {by} A {r} {h} 0 0 1 {cx + r} {by} "
              f"Q {cx + r - 7} {by + 5} {cx} {by + 5} "
              f"Q {cx - r + 7} {by + 5} {cx - r} {by} Z", "#d9734f"),
        lib.E(cx, by - h + 3, r * 0.5, 6, "#b45a3c"),               # 碗足（朝上）
        lib.P(f"M {cx - r * 0.55} {by - h * 0.26} Q {cx - r * 0.62} {by - h * 0.6} "
              f"{cx - r * 0.44} {by - h * 0.8}", stroke=lib.WHITE, w=6, opacity=0.55))


# ---------- 插画 ----------
def art_bie():
    """别：插座+电线+插头，红圈斜杠罩在插头上——'别碰插头'；小孩在旁边看。"""
    g = lib.ground()
    # 墙面竖条 + 墙上的插座面板（两孔）
    g += lib.R(64, 56, 210, 392, 18, "#f0e8d2")
    g += lib.R(136, 186, 92, 112, 12, lib.WHITE)
    g += lib.C(163, 224, 7, lib.INK)
    g += lib.C(201, 224, 7, lib.INK)
    # 电线从插座垂下、拖到地上，末端是两脚插头
    g += lib.P("M 182 298 Q 196 380 268 410 Q 318 430 372 424",
               stroke=lib.INK, w=8)
    g += lib.R(370, 404, 58, 34, 9, lib.INK)
    g += lib.L(428, 412, 452, 408, lib.INK, 7)
    g += lib.L(428, 426, 452, 430, lib.INK, 7)
    # 红圈斜杠罩在插头上
    cx, cy, r = 398, 356, 132
    g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{lib.RED}" stroke-width="20" opacity="0.94"/>'
    d = r * 0.70
    g += lib.L(cx - d, cy - d, cx + d, cy + d, lib.RED, 20)
    # 小孩站右侧看着（不伸手，保持"在旁边"）
    g += lib.kid(600, 444, s=0.95, arms="down", face="o",
                 look=(-1.6, 0.2), shirt=lib.BLUE)
    return g


def art_le():
    """了：我吃完饭了——桌上碗倒扣，小孩双手叉腰看碗满足笑。"""
    g = lib.ground()
    # 小孩（桌左，双手叉腰，眼看倒扣的碗，满足笑）
    g += _kid_akimbo(258, 442, 0.92, look=(1.7, 0.5))
    # 小桌
    g += lib.table(480, top=320, w=252, leg_h=84, slab=40)
    # 倒扣的碗（ strongest 完成信号）
    g += _upside_down_bowl(480, 320)
    # 桌上躺着的小勺（吃完放下的）
    g += f'<g transform="rotate(14 566 336)">' + lib.L(534, 336, 566, 336, "#e8a13c", 8) \
        + lib.E(578, 336, 14, 9, "#dfe3e6") + lib.E(578, 338, 9, 5, "#c9cdd1") + "</g>"
    # 桌上饭粒（吃干净的余韵）
    g += lib.C(412, 327, 3.5, lib.YEL_D)
    g += lib.C(552, 325, 3, lib.YEL_D)
    # 满足小闪光
    g += lib.star5(306, 158, 12, lib.SUN_L)
    g += lib.star5(560, 244, 9, lib.SUN_L)
    return g


def art_du():
    """肚：全身小孩，衣摆上撩露出圆肚子+肚脐，双手扶肚两侧，脚边空碗。"""
    g = lib.ground()
    x, y, s = 350, 444, 1.05
    sho, hip = y - 168 * s, y - 96 * s
    # 全身小孩（先按默认画法出腿、身子、头脸）
    g += lib.kid(x, y, s=s, arms="down", face="smile", look=(0, 0.6), shirt=lib.TEAL)
    # 裤腰（比肚子宽，露出两侧+下沿）
    g += lib.R(x - 56 * s, hip + 4 * s, 112 * s, 42 * s, 14, lib.BLUE_D)
    # 圆肚子：盖住下段衣身、鼓在裤腰上（吃饱的弧度，一眼是圆肚皮）
    g += lib.E(x, hip + 4 * s, 52.5, 42, lib.SKIN)
    g += lib.E(x, hip + 20 * s, 38, 13, "#fad4b0", 0.6)          # 饱肚高光
    # 撩起的衣摆：沿肚顶弧盖一条衫色边（下缘内收成卷边，衣摆明显在上）
    g += lib.P(f"M {x - 54.5} {hip + 4 * s} A 54.5 44.5 0 0 1 {x + 54.5} {hip + 4 * s} "
               f"Q {x} {hip - 30 * s} {x - 54.5} {hip + 4 * s} Z", lib.TEAL)
    # 肚脐（圆肚正中）
    g += lib.E(x, hip + 13 * s, 9.5, 12.5, lib.SKIN_D)
    g += lib.E(x, hip + 15 * s, 4.5, 7, "#c9835a")
    # 双手托在肚子下缘两侧（让开肚缘，给箭头留出干净的指向位）
    g += _hand_on_belly(sho, x, s, -1, 64, hip + 22 * s)
    g += _hand_on_belly(sho, x, s, +1, 64, hip + 22 * s)
    # 手指扣住肚下缘的指缝线
    for sd in (-1, 1):
        fx = x + 58 * s * sd
        g += lib.P(f"M {fx} {hip + 10 * s} Q {fx - 5 * sd} {hip + 18 * s} {fx} {hip + 26 * s}",
                   stroke=lib.SKIN_D, w=5)
    # 纯粹小箭头：水平从右指向肚缘（尖端贴着肚子，不再落在手上）
    g += lib.L(x + 186, hip + 4, x + 80, hip + 4, lib.INK, 9)
    g += f'<polygon points="{x + 64},{hip + 4} {x + 88},{hip - 9} {x + 88},{hip + 17}" fill="{lib.INK}"/>'
    return g


ARTS = {"别": art_bie(), "了": art_le(), "肚": art_du()}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    expect = {"别", "了", "肚"}
    assert set(ARTS) == expect, f"键不一致：多 {set(ARTS) - expect} 缺 {expect - set(ARTS)}"

    g0 = lib.ground()
    problems = []
    for k, v in ARTS.items():
        try:
            ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
                          + v + "</svg>")
        except ET.ParseError as e:
            problems.append((k, f"XML {e}"))
        low = v.lower()
        for bad in ("<svg", "<defs", "<use", "<text", "<image", "href"):
            if bad in low:
                problems.append((k, bad))
        if not v.startswith(g0):
            problems.append((k, "第一笔不是 ground()"))
    print("v2 自检：" + ("全部通过" if not problems else f"问题 {problems}"))
    assert not problems, "自检未通过"
