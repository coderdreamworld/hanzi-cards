#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画素材库：统一画风的原语与组件。

所有插画都是 viewBox="0 0 760 480" 画布的【内部内容】字符串：
- 只返回 <g> 内部的形状标记，不带 <svg> 包装、不带 xmlns；
- 禁止 <defs>/<use>/<text>/<image>（grid 模式 282 张卡同页，ID 会互相污染；图上不许出现任何文字）；
- 画风：扁平绘本、圆角、暖色，深一号底色偏移制造体积，无描边，无渐变；
- 地面统一用 ground() 青绿椭圆（呼应孩子的情绪怪兽卡）。

原语（E 椭圆 / C 圆 / R 圆角矩形 / L 线段 / P 路径 / PG 多边形）+ 已验证的成品组件
（ball/table/box/cup/jug/bowl/spoon/hand/kid 等，取自试制 8 张卡）。
设计新组件时：先摆 ground()，主体居中偏下，配色只用 PALETTE 或其同族色。
"""

# ---------- 色板 ----------
INK = "#4a3226"        # 深暖棕（线条/五官/头发）
PAGE = "#fdf8ec"       # 卡底奶油
PANEL_Y = "#fbf0c2"    # 字面板浅黄
PANEL_T = "#d9f0ea"    # 句面板浅青
BORDER = "#f2c14e"     # 金边
GROUND = "#c8e6d8"     # 地面青绿
RED, RED_D = "#e8663c", "#d4552f"
YEL, YEL_D = "#f2b53c", "#d99a2b"
TEAL, TEAL_D, TEAL_L = "#4fae9f", "#3e9486", "#7cc8bb"
BLUE, BLUE_D = "#5fa8d8", "#4a97c9"
WBLUE = "#79c2e6"      # 水
SKIN, SKIN_D = "#f8cba4", "#eeb28a"
HAIR = "#5a3d2b"
WOOD, WOOD_D, WOOD_L = "#c89058", "#b57b44", "#e9b97e"
GREEN, GREEN_L = "#7fae70", "#9cc98a"
SUN, SUN_L = "#f7ae35", "#f9c95e"
PINK = "#f5a58c"
WHITE = "#fdfdfa"


# ---------- 原语 ----------
def E(cx, cy, rx, ry, fill, opacity=None):
    o = f' opacity="{opacity}"' if opacity else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"{o}/>'


def C(cx, cy, r, fill, opacity=None):
    o = f' opacity="{opacity}"' if opacity else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{o}/>'


def R(x, y, w, h, rx, fill, opacity=None):
    o = f' opacity="{opacity}"' if opacity else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{o}/>'


def L(x1, y1, x2, y2, stroke, w, cap="round"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}" stroke-linecap="{cap}"/>'


def P(d, fill=None, stroke=None, w=None, cap="round", opacity=None):
    a = f' fill="{fill}"' if fill else ' fill="none"'
    if stroke:
        a += f' stroke="{stroke}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round"'
    if opacity:
        a += f' opacity="{opacity}"'
    return f'<path d="{d}"{a}/>'


def PG(points, fill):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}"/>'


def wrap(*parts):
    return "".join(parts)


# ---------- 场景组件 ----------
def ground(cx=380, cy=446, rx=240, ry=24, fill=GROUND):
    return E(cx, cy, rx, ry, fill)


def ball(cx, cy, r, main=TEAL, dark=TEAL_D, hi=TEAL_L):
    """球：深一号底 + 主体 + 左上高光，底部 cy+r 落地。"""
    return wrap(
        C(cx + r * 0.05, cy + r * 0.08, r, dark),
        C(cx - r * 0.03, cy - r * 0.05, r * 0.955, main),
        C(cx - r * 0.34, cy - r * 0.32, max(6, r * 0.24), hi, 0.9))


def table(cx=380, top=330, w=244, leg_h=78, slab=42):
    """木桌：top=桌面顶 y，桌腿到 top+slab+leg_h。"""
    x0 = cx - w / 2
    lx1, lx2 = cx - w / 2 + 34, cx + w / 2 - 64
    return wrap(
        R(lx1, top + slab, 30, leg_h, 11, WOOD_D),
        R(lx2, top + slab, 30, leg_h, 11, WOOD_D),
        R(x0, top, w, slab, 14, WOOD),
        R(x0, top + slab - 22, w, 20, 10, WOOD_D))


def lid(cx, cy, w=230, h=52, rot=-10, knob=True):
    """盒盖（含提钮），配合 box() 表达开/关。"""
    g = wrap(
        R(-w / 2, -h / 2, w, h, 14, WOOD_L),
        R(-w / 2, h / 2 - 14, w, 20, 10, WOOD),
        R(-w / 2 + 16, -h / 2 + 10, w * 0.42, 14, 7, "#f4d3a4", 0.8),
        C(0, -h / 2 - 13, 15, WOOD) if knob else "")
    return f'<g transform="translate({cx},{cy}) rotate({rot})">{g}</g>'


def box(cx=380, top=318, w=230, h=126, open_top=True):
    """纸箱：open_top=True 时顶部有深色开口缝。"""
    return wrap(
        R(cx - w / 2 + 10, top, w - 20, 30, 10, "#8a5a33") if open_top else "",
        R(cx - w / 2, top + 16, w, h, 16, WOOD),
        R(cx - w / 2 + 22, top + 38, w - 44, h - 44, 12, WOOD_L))


def cup(cx=380, top=268, w=142, h=172, water=0.55):
    """玻璃杯，water=水位 0~1。"""
    x0 = cx - w / 2
    body = P(f"M {x0} {top} L {x0+13} {top+h-16} Q {x0+15} {top+h} {x0+32} {top+h} "
             f"L {x0+w-32} {top+h} Q {x0+w-15} {top+h} {x0+w-13} {top+h-16} L {x0+w} {top} Z")
    wy0 = top + h * (1 - water)
    water_p = P(f"M {x0+7} {wy0} Q {cx-35} {wy0-12} {cx} {wy0-2} Q {cx+35} {wy0+8} {x0+w-7} {wy0} "
                f"L {x0+w-16} {top+h-16} Q {x0+w-18} {top+h-8} {x0+w-32} {top+h-8} "
                f"L {x0+32} {top+h-8} Q {x0+18} {top+h-8} {x0+16} {top+h-16} Z", fill=WBLUE)
    return wrap(
        E(cx, top, w / 2, 14, "#cfe6f0"),
        body, water_p,
        E(cx, wy0, w * 0.43, 9, "#a5d9f0", 0.9),
        R(x0 + 22, top + 18, 14, h * water - 10, 7, WHITE, 0.6))


def jug(cx=545, cy=150, rot=-38):
    """倾斜水壶（嘴朝左下），配水流 stream()。"""
    g = wrap(
        PG([(-44, -56), (-100, -34), (-44, -22)], "#9cc9e2"),
        P("M -44 -56 L 44 -56 L 52 40 Q 54 56 38 56 L -38 56 Q -54 56 -52 40 Z", "#9cc9e2"),
        R(-24, -70, 48, 18, 7, "#7fa9c4"),
        P("M 46 -30 Q 100 -6 48 26", stroke="#9cc9e2", w=15),
        R(-24, -34, 16, 70, 8, "#b7d8ec", 0.8))
    return f'<g transform="translate({cx},{cy}) rotate({rot})">{g}</g>'


def stream(x0, y0, x1, y1, bend=40, w0=22, w1=13, color=WBLUE):
    """锥形水流：(x0,y0)壶嘴→(x1,y1)水面，上粗下细。"""
    d = (f"M {x0-w0/2} {y0+6} Q {x0-bend} {(y0+y1)/2} {x1-w1/2} {y1} "
         f"L {x1+w1/2} {y1-6} Q {x0+bend} {(y0+y1)/2-8} {x0+w0/2} {y0-8} Z")
    return P(d, color)


def bowl(cx=238, cy=412, r=52, rice=True):
    """饭碗（可带米饭）。"""
    s = wrap(
        P(f"M {cx-r} {cy-2} Q {cx-r+8} {cy-28} {cx-r+28} {cy-22} Q {cx-r+40} {cy-36} {cx-r+58} {cy-26} "
          f"Q {cx-r+74} {cy-34} {cx-r+80} {cy-18} Q {cx-r+96} {cy-20} {cx+r} {cy-2} "
          f"Q {cx} {cy+12} {cx-r} {cy-2} Z", WHITE)) if rice else ""
    b = P(f"M {cx-r-2} {cy} Q {cx} {cy+14} {cx+r+2} {cy} Q {cx+r-2} {cy+32} {cx} {cy+34} "
          f"Q {cx-r+2} {cy+32} {cx-r-2} {cy} Z", "#d9734f")
    return s + b


def spoon(hx, hy, tx, ty, rice=True):
    """勺子：手位(hx,hy)→勺头(tx,ty)，勺头带饭。"""
    import math
    ang = math.degrees(math.atan2(ty - hy, tx - hx))
    head = (f'<g transform="rotate({ang:.1f} {tx} {ty})">'
            + E(tx, ty, 32, 21, "#dfe3e6") + E(tx, ty + 4, 24, 13, "#c9cdd1")
            + (P(f"M {tx-28} {ty-13} Q {tx-24} {ty-28} {tx-10} {ty-22} Q {tx-4} {ty-36} {tx+10} {ty-28} "
                 f"Q {tx+24} {ty-33} {tx+26} {ty-17} Q {tx+36} {ty-13} {tx+27} {ty-6} "
                 f"Q {tx} {ty+3} {tx-21} {ty-4} Q {tx-29} {ty-8} {tx-28} {ty-13} Z", WHITE) if rice else "")
            + "</g>")
    return L(hx, hy, tx + (tx - hx) * 0.12, ty + (ty - hy) * 0.12, "#e8a13c", 13) + head


def hand(x, y, rot=0, s=1.0):
    """单只手（手掌朝前、五指张开、芥末色袖口），已验证画法。"""
    g = wrap(
        R(-50, -52, 100, 124, 36, "#f7c49c"),
        R(-50, -102, 28, 76, 14, "#f7c49c") if False else "",
        f'<g transform="rotate(-8 -36 -30)">{R(-50, -102, 28, 76, 14, "#f7c49c")}</g>',
        f'<g transform="rotate(-2 -1 -30)">{R(-16, -112, 30, 86, 15, "#f7c49c")}</g>',
        f'<g transform="rotate(5 32 -30)">{R(18, -106, 29, 80, 14.5, "#f7c49c")}</g>',
        f'<g transform="rotate(12 64 -30)">{R(52, -86, 25, 62, 12.5, "#f7c49c")}</g>',
        f'<g transform="rotate(-30 -52 20)">{R(-86, -34, 34, 88, 17, "#f7c49c")}</g>',
        E(0, 46, 38, 20, SKIN_D, 0.3),
        R(-50, 64, 100, 56, 20, "#f2b03c"),
        R(-50, 64, 100, 18, 9, "#e8a13c"))
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">{g}</g>'


# ---------- 小朋友（本库最重要的组件） ----------
def kid(x=380, y=430, s=1.0, flip=1, pose="stand", face="smile", shirt=BLUE,
        skin=SKIN, hair_color=HAIR, hair="boy", arms="down", look=(0, 0),
        mustache=False, glasses=False, bun=False, skirt=False, point_at=None,
        item=None, extra=""):
    """扁平小朋友。y=脚底。pose: stand|sit|walk|run|sleep；face: smile|open|sad|cry|o；
    arms: down|up|cross|point|clap；point_at=(x,y) 相对画布坐标；item 为手持物的 SVG 串（在手之后画）。"""
    if pose == "sleep":
        return _kid_sleep(x, y, s, flip, face, shirt, skin, hair_color, extra)
    f = []
    H = 300 * s          # 总高
    hd = 62 * s          # 头半径
    hip = y - 96 * s     # 髋部
    sho = y - 168 * s    # 肩
    hcy = sho - 8 * s - hd  # 头心
    # 腿
    if pose == "sit":
        hip = y - 78 * s
        sho = hip - 74 * s
        hcy = sho - 8 * s - hd
        f.append(R(x - 30 * s, hip - 12 * s, 26 * s, 66 * s, 12 * s, BLUE_D))
        f.append(R(x + 4 * s, hip - 12 * s, 26 * s, 66 * s, 12 * s, BLUE_D))
        f.append(E(x - 18 * s, y - 8 * s, 22 * s, 10 * s, INK, 0.85))
        f.append(E(x + 54 * s, y - 8 * s, 22 * s, 10 * s, INK, 0.85))
    elif pose == "sprint":
        # 奔跑腾空：前腿屈膝高抬（大腿+小腿两段）、后腿向后蹬直，双脚离地
        f.append(f'<g transform="rotate(-47 {x} {hip})">'
                 + R(x - 13 * s, hip - 14 * s, 26 * s, 68 * s, 13 * s, BLUE_D) + "</g>")
        f.append(f'<g transform="rotate(-10 {x + 39 * s} {y - 59 * s})">'
                 + R(x + 28 * s, y - 67 * s, 22 * s, 44 * s, 11 * s, BLUE_D) + "</g>")
        f.append(f'<g transform="rotate(40 {x} {hip})">'
                 + R(x - 13 * s, hip - 14 * s, 26 * s, 100 * s, 13 * s, BLUE_D) + "</g>")
        f.append(f'<g transform="rotate(-12 {x + 45 * s} {y - 26 * s})">'
                 + E(x + 45 * s, y - 26 * s, 20 * s, 9 * s, INK, 0.85) + "</g>")
        f.append(f'<g transform="rotate(32 {x - 53 * s} {y - 31 * s})">'
                 + E(x - 53 * s, y - 31 * s, 20 * s, 9 * s, INK, 0.85) + "</g>")
    elif pose == "stride":
        # 大步走：前腿迈出、后腿蹬地脚跟抬起，跨步一眼可辨
        f.append(f'<g transform="rotate(-28 {x} {hip})">'
                 + R(x - 13 * s, hip - 14 * s, 26 * s, 114 * s, 13 * s, BLUE_D) + "</g>")
        f.append(f'<g transform="rotate(22 {x} {hip})">'
                 + R(x - 13 * s, hip - 14 * s, 26 * s, 102 * s, 13 * s, BLUE_D) + "</g>")
        f.append(E(x + 46 * s, y - 7 * s, 22 * s, 10 * s, INK, 0.85))
        f.append(f'<g transform="rotate(16 {x - 33 * s} {y - 11 * s})">'
                 + E(x - 33 * s, y - 11 * s, 21 * s, 9 * s, INK, 0.85) + "</g>")
    elif pose in ("walk", "run"):
        lean = 8 if pose == "run" else 4
        f.append(f'<g transform="rotate({flip*lean} {x} {hip})">'
                 + R(x - 34 * s, hip - 12 * s, 26 * s, 84 * s, 12 * s, BLUE_D)
                 + R(x + 8 * s, hip - 12 * s, 26 * s, 78 * s, 12 * s, BLUE_D) + "</g>")
        f.append(E(x - 26 * s, y - 6 * s, 21 * s, 10 * s, INK, 0.85))
        f.append(E(x + 24 * s, y - 10 * s, 21 * s, 10 * s, INK, 0.85))
    else:
        f.append(R(x - 30 * s, hip - 10 * s, 26 * s, 84 * s, 12 * s, BLUE_D))
        f.append(R(x + 4 * s, hip - 10 * s, 26 * s, 84 * s, 12 * s, BLUE_D))
        f.append(E(x - 17 * s, y - 6 * s, 21 * s, 10 * s, INK, 0.85))
        f.append(E(x + 17 * s, y - 6 * s, 21 * s, 10 * s, INK, 0.85))
    # 身体
    body = (P(f"M {x-56*s} {sho} Q {x-58*s} {hip+6*s} {x-40*s} {hip+8*s} L {x+40*s} {hip+8*s} "
              f"Q {x+58*s} {hip+6*s} {x+56*s} {sho} Q {x} {sho-16*s} {x-56*s} {sho} Z", shirt))
    if skirt:
        body += P(f"M {x-52*s} {hip-24*s} L {x+52*s} {hip-24*s} L {x+66*s} {hip+44*s} "
                  f"L {x-66*s} {hip+44*s} Z", RED)
    f.append(body)
    # 手臂
    def arm(x1, y1, x2, y2):
        return (L(x1, y1, x2, y2, skin, 30 * s), C(x2, y2, 13 * s, skin))
    sh_l, sh_r = (x - 44 * s, sho + 6 * s), (x + 44 * s, sho + 6 * s)
    if arms == "up":
        f += arm(*sh_l, x - 84 * s, hcy + 6 * s)
        f += arm(*sh_r, x + 84 * s, hcy + 6 * s)
    elif arms == "reach":
        # 双臂一齐伸向前下方（洗手：两手伸到水流下搓洗）
        f += arm(*sh_l, x - 110 * s, sho + 70 * s)
        f += arm(*sh_r, x - 88 * s, sho + 80 * s)
    elif arms == "pump":
        # 跑步摆臂：左臂向后摆起、右臂向前上方扬，不交叉身体
        f += arm(sh_l[0], sh_l[1], x - 78 * s, sho + 52 * s)
        f += arm(sh_r[0], sh_r[1], x + 84 * s, sho + 26 * s)
    elif arms == "swing":
        # 走路摆臂：左臂向后外侧摆、右臂向前外侧微抬（与前迈右腿异侧），不交叉身体
        f += arm(sh_l[0], sh_l[1], x - 72 * s, sho + 74 * s)
        f += arm(sh_r[0], sh_r[1], x + 80 * s, sho + 56 * s)
    elif arms == "hold_right":
        # 右手牵身旁较矮的人；另一只手自然垂下。
        f += arm(*sh_l, x - 64 * s, sho + 78 * s)
        f += arm(*sh_r, x + 84 * s, sho + 75 * s)
    elif arms == "hold_left":
        # 左手牵身旁较高的人；接手点靠上，避免额外补一条“连接臂”。
        f += arm(*sh_l, x - 100 * s, sho + 36 * s)
        f += arm(*sh_r, x + 64 * s, sho + 78 * s)
    elif arms == "cross":
        # 两条肩到对侧手掌的完整手臂已经组成 X；不要再叠加第二个 X，
        # 否则缩略图会像四只手。
        f += arm(*sh_l, x + 20 * s, sho + 66 * s)
        f += arm(*sh_r, x - 20 * s, sho + 66 * s)
    elif arms == "clap":
        f += arm(*sh_l, x - 10 * s, sho + 34 * s)
        f += arm(*sh_r, x + 12 * s, sho + 34 * s)
        f.append(C(x - 14 * s, sho + 30 * s, 13 * s, skin))
        f.append(C(x + 14 * s, sho + 30 * s, 13 * s, skin))
    elif arms == "point" and point_at:
        import math
        px, py = point_at
        ang = math.degrees(math.atan2(py - (sho + 10 * s), px - sh_r[0]))
        f.append(f'<g transform="rotate({ang:.0f} {sh_r[0]} {sh_r[1]})">'
                 + L(sh_r[0], sh_r[1], sh_r[0] + 86 * s, sh_r[1], skin, 30 * s)
                 + C(sh_r[0] + 88 * s, sh_r[1], 13 * s, skin) + "</g>")
        f += arm(*sh_l, x - 66 * s, sho + 76 * s)
    else:  # down
        f += arm(*sh_l, x - 64 * s, sho + 78 * s)
        f += arm(*sh_r, x + 64 * s, sho + 78 * s)
    # 头
    f.append(C(x - 58 * s, hcy + 10 * s, 11 * s, skin))
    f.append(C(x + 58 * s, hcy + 10 * s, 11 * s, skin))
    f.append(C(x, hcy, hd, skin))
    # 头发
    top = hcy - hd
    bang = hcy - hd * 0.42
    hair_p = (P(f"M {x-hd*0.98} {hcy-hd*0.35} Q {x-hd*0.9} {top-hd*0.18} {x} {top-hd*0.12} "
                f"Q {x+hd*0.9} {top-hd*0.18} {x+hd*0.98} {hcy-hd*0.35} "
                f"Q {x+hd*0.55} {bang-hd*0.1} {x} {bang} "
                f"Q {x-hd*0.55} {bang-hd*0.1} {x-hd*0.98} {hcy-hd*0.35} Z", hair_color))
    f.append(hair_p)
    if bun:
        f.append(C(x, top - 16 * s, 20 * s, hair_color))
    # 眼睛（看向 look 偏移）
    lx, ly = look
    for ex in (-22, 22):
        f.append(E(x + ex * s, hcy - 8 * s, 10 * s, 13 * s, INK))
        f.append(C(x + ex * s + lx * s, hcy - 13 * s + ly * s, 3.4 * s, WHITE))
    # 眉毛
    f.append(P(f"M {x-36*s} {hcy-hd*0.52} Q {x-22*s} {hcy-hd*0.62} {x-8*s} {hcy-hd*0.54}",
               stroke=hair_color, w=6 * s))
    f.append(P(f"M {x+8*s} {hcy-hd*0.54} Q {x+22*s} {hcy-hd*0.62} {x+36*s} {hcy-hd*0.52}",
               stroke=hair_color, w=6 * s))
    # 嘴
    my = hcy + 26 * s
    if face == "open":
        f.append(P(f"M {x-26*s} {my} Q {x} {my-10*s} {x+26*s} {my} Q {x+24*s} {my+26*s} {x} {my+30*s} "
                   f"Q {x-24*s} {my+26*s} {x-26*s} {my} Z", "#6b3325"))
        f.append(P(f"M {x-14*s} {my+16*s} Q {x} {my+8*s} {x+14*s} {my+16*s} "
                   f"Q {x+9*s} {my+27*s} {x} {my+28*s} Q {x-9*s} {my+27*s} {x-14*s} {my+16*s} Z", "#f0876f"))
    elif face == "sad":
        f.append(P(f"M {x-18*s} {my+10*s} Q {x} {my} {x+18*s} {my+10*s}", stroke=INK, w=7 * s))
    elif face == "cry":
        f.append(P(f"M {x-18*s} {my+8*s} Q {x} {my-2*s} {x+18*s} {my+8*s}", stroke=INK, w=7 * s))
        f.append(E(x - 24 * s, hcy + 6 * s, 6 * s, 10 * s, WBLUE))
        f.append(E(x + 24 * s, hcy + 6 * s, 6 * s, 10 * s, WBLUE))
    elif face == "o":
        f.append(E(x, my + 4 * s, 10 * s, 12 * s, "#6b3325"))
    else:  # smile
        f.append(P(f"M {x-20*s} {my} Q {x} {my+16*s} {x+20*s} {my}", stroke=INK, w=7 * s))
    # 腮红
    f.append(C(x - 44 * s, hcy + 14 * s, 11 * s, PINK, 0.8))
    f.append(C(x + 44 * s, hcy + 14 * s, 11 * s, PINK, 0.8))
    if mustache:
        f.append(P(f"M {x-20*s} {my-6*s} Q {x} {my-14*s} {x+20*s} {my-6*s} "
                   f"Q {x} {my-2*s} {x-20*s} {my-6*s} Z", "#d9d0c5"))
    if glasses:
        f.append(f'<g fill="none" stroke="{INK}" stroke-width="{5*s}">'
                 + f'<circle cx="{x-22*s}" cy="{hcy-8*s}" r="{16*s}"/>'
                 + f'<circle cx="{x+22*s}" cy="{hcy-8*s}" r="{16*s}"/>'
                 + L(x - 6 * s, hcy - 8 * s, x + 6 * s, hcy - 8 * s, INK, 5 * s) + "</g>")
    f.append(extra)
    return f'<g transform="translate({x*(1-flip)},0) scale({flip},1)">{wrap(*f)}</g>' if flip == -1 else wrap(*f)


def _kid_sleep(x, y, s, flip, face, shirt, skin, hair_color, extra):
    """躺着睡：头在左，身体在右，盖小被子。"""
    f = []
    f.append(E(x + 10 * s, y - 20 * s, 120 * s, 40 * s, GROUND, 0.6))
    f.append(P(f"M {x-30*s} {y-52*s} L {x+140*s} {y-52*s} L {x+140*s} {y-16*s} "
               f"Q {x+60*s} {y-2*s} {x-30*s} {y-16*s} Z", TEAL_L))
    f.append(R(x + 20 * s, y - 88 * s, 118 * s, 44 * s, 20 * s, shirt))
    f.append(C(x - 60 * s, y - 70 * s, 46 * s, skin))
    f.append(P(f"M {x-104*s} {y-70*s} A 46 46 0 0 1 {x-16*s} {y-78*s} "
               f"Q {x-50*s} {y-96*s} {x-80*s} {y-92*s} Q {x-100*s} {y-86*s} {x-104*s} {y-70*s} Z", hair_color))
    f.append(P(f"M {x-74*s} {y-64*s} Q {x-64*s} {y-56*s} {x-54*s} {y-64*s}", stroke=INK, w=6 * s))
    f.append(E(x - 82 * s, y - 66 * s, 7 * s, 9 * s, INK))
    f.append(C(x - 44 * s, y - 52 * s, 8 * s, PINK, 0.8))
    f.append(extra)
    return wrap(*f)


# ---------- 常用小物件 ----------
def star5(cx, cy, r, fill=SUN):
    import math
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return PG(pts, fill)


def heart(cx, cy, r, fill=RED):
    return P(f"M {cx} {cy+r*0.9} C {cx-r*1.2} {cy} {cx-r*0.7} {cy-r*0.9} {cx} {cy-r*0.3} "
             f"C {cx+r*0.7} {cy-r*0.9} {cx+r*1.2} {cy} {cx} {cy+r*0.9} Z", fill)


def drop(cx, cy, r, fill=WBLUE):
    return P(f"M {cx} {cy-r} Q {cx+r*0.85} {cy+r*0.25} {cx} {cy+r} "
             f"Q {cx-r*0.85} {cy+r*0.25} {cx} {cy-r} Z", fill)


def cloud_p(cx, cy, s=1.0, fill=WHITE):
    return wrap(C(cx - 42 * s, cy, 30 * s, fill), C(cx, cy - 20 * s, 38 * s, fill),
                C(cx + 42 * s, cy, 30 * s, fill), R(cx - 60 * s, cy - 6 * s, 120 * s, 36 * s, 18 * s, fill))


def flower5(cx, cy, r, petal="#f0876f", core=SUN):
    import math
    g = ""
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        g += C(cx + r * math.cos(a), cy + r * math.sin(a), r * 0.62, petal)
    return g + C(cx, cy, r * 0.5, core)


def tree_round(cx=380, base=430, s=1.0, leaf=GREEN, leaf_l=GREEN_L):
    trunk = R(cx - 16 * s, base - 90 * s, 32 * s, 92 * s, 10 * s, WOOD_D)
    crown = wrap(C(cx, base - 170 * s, 86 * s, leaf), C(cx - 62 * s, base - 130 * s, 62 * s, leaf),
                 C(cx + 62 * s, base - 130 * s, 62 * s, leaf), C(cx - 20 * s, base - 200 * s, 55 * s, leaf_l, 0.85))
    return trunk + crown


def check(cx, cy, r, color=TEAL, w=None):
    w = w or r * 0.42
    return P(f"M {cx-r*0.75} {cy+r*0.05} L {cx-r*0.15} {cy+r*0.6} L {cx+r*0.8} {cy-r*0.55}",
             stroke=color, w=w)
