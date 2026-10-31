#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次D 残留小修（独立待确认，不并入正式文件）：柳 蜂 虎 牛 窗 发 肚 杏 枫 洋。

依据：修复方案.md 批次D + 审美教研报告审计项。多为在旧实现上小改：
- 柳：树冠顶部+多条下垂长弧枝统一向右弯+细长叶（废扁平大椭圆）。
- 蜂：腹纹从脸部移回腹部。
- 虎：体型放大一圈+橙红加深+条纹加密（与猫明显拉开）。
- 牛：牛角加大加清晰+鼻端浅灰（去猪鼻感）。
- 窗：窗格里删金鱼感杂形，改画太阳+云（例句"窗外有太阳"）。
- 发：两侧"耳机"深色圆块改浓密盖头黑发+鬓角，梳子保留。
- 肚：绿色块下移成衣摆弧贴住圆肚，肚脐居中露在圆肚上。
- 杏：枝条收进卡内不切边，果改黄橙，果下补投影。
- 枫：后层深色块改同心放大，修齐不外露。
- 洋：船放大，海占满整卡宽。
硬规则：无 svg 包装/defs/use/text/image/任何文字数字；第一笔 ground()；
只用素材库 PALETTE 及同族色；主体居中；动物友好无尖牙利爪。
自检：python3 修复D_残留小修.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from 识字卡片_素材库 import (BLUE_D, GREEN, GREEN_L, HAIR, INK, PINK, RED, SKIN, SKIN_D,
                          SUN, SUN_L, WHITE, WOOD, WOOD_D, WOOD_L, YEL, YEL_D,
                          C, E, L, P, PG, R, cloud_p, flower5, ground, wrap)

# 组内同族补充色（取自各旧素材文件的同族色）
LEAF_D = "#5e8a50"     # 深叶绿（GREEN 同族）
LEAF_BB = "#d4e8b0"    # 叶脉浅绿
SHAD = "#aed4c2"       # 果影（GROUND 同族深）
SKY = "#aee0f2"        # 窗玻璃天空蓝
TIGER, TIGER_D = "#e2682a", "#c95418"   # 虎：深橙红（比猫 #f5a044 深一档）
STRIPE = "#4a3226"     # 虎纹/蜂纹黑棕
COW_W, COW_D, SPOT = "#fbf6ea", "#e8dcc8", "#a9743f"   # 牛：白底棕斑
BEE, BEE_D = "#f2b53c", "#d99a2b"      # 蜂：黄


# ---------- 本地小部件（与旧素材文件同款） ----------
def place(inner, x, y, rot=0):
    t = f"translate({x},{y})"
    if rot:
        t += f" rotate({rot})"
    return f'<g transform="{t}">{inner}</g>'


def leaf(ln, wd, fill):
    """尖头椭圆叶：原点在叶柄，叶尖指向 +x。"""
    return P(f"M 0 0 Q {ln * 0.42} {-wd} {ln} 0 Q {ln * 0.42} {wd} 0 0 Z", fill)


def leaf_veined(ln, wd, fill, vein):
    return leaf(ln, wd, fill) + L(10, 0, ln - 12, 0, vein, 3.5)


def blob(cx, cy, rx, ry, main, dark):
    return E(cx + rx * 0.06, cy + ry * 0.09, rx, ry, dark) + \
        E(cx - rx * 0.02, cy - ry * 0.04, rx * 0.97, ry * 0.97, main)


def cblob(cx, cy, r, main, dark):
    return C(cx + r * 0.06, cy + r * 0.09, r, dark) + \
        C(cx - r * 0.02, cy - r * 0.04, r * 0.97, main)


def eyes(x1, x2, cy, r=11):
    out = []
    for x in (x1, x2):
        out.append(E(x, cy, r, r * 1.2, INK))
        out.append(C(x - r * 0.3, cy - r * 1.2 * 0.35, r * 0.3, WHITE))
    return "".join(out)


def blush(cx, cy, off, r=12, col=PINK, op=0.75):
    return C(cx - off, cy, r, col, op) + C(cx + off, cy, r, col, op)


def smile(cx, cy, w=20, lw=6, col=None):
    return P(f"M {cx - w} {cy} Q {cx} {cy + w * 0.65} {cx + w} {cy}", stroke=col or INK, w=lw)


def wmouth(cx, cy, w=12, lw=5, col=None):
    return (P(f"M {cx} {cy} Q {cx + 1} {cy + w * 0.5} {cx - w} {cy + w * 0.62}", stroke=col or INK, w=lw)
            + P(f"M {cx} {cy} Q {cx - 1} {cy + w * 0.5} {cx + w} {cy + w * 0.62}", stroke=col or INK, w=lw))


def paw(x, y, rx, ry, fill, dark=None):
    g = E(x, y, rx, ry, fill)
    if dark:
        g += L(x - rx * 0.35, y - ry * 0.35, x - rx * 0.35, y + ry * 0.3, dark, 4)
        g += L(x + rx * 0.3, y - ry * 0.35, x + rx * 0.3, y + ry * 0.3, dark, 4)
    return g


def _face(r=162, cx=380, cy=278, hair_color=HAIR, hair=True, ears=True,
          eyes_mode="open", brows=True, nose=True, mouth="smile", blush=0.11):
    """整幅画就是一张大圆脸（人体组同款）。"""
    p = []
    if ears:
        p.append(C(cx - r, cy + r * 0.05, r * 0.155, SKIN))
        p.append(C(cx + r, cy + r * 0.05, r * 0.155, SKIN))
        p.append(E(cx - r * 1.02, cy + r * 0.05, r * 0.07, r * 0.10, SKIN_D))
        p.append(E(cx + r * 1.02, cy + r * 0.05, r * 0.07, r * 0.10, SKIN_D))
    p.append(C(cx + r * 0.05, cy + r * 0.06, r, SKIN_D))
    p.append(C(cx, cy, r * 0.985, SKIN))
    if hair:
        top, bang = cy - r, cy - r * 0.42
        p.append(P(f"M {cx - r*0.98:.0f} {cy - r*0.35:.0f} Q {cx - r*0.9:.0f} {top - r*0.18:.0f} "
                   f"{cx} {top - r*0.12:.0f} Q {cx + r*0.9:.0f} {top - r*0.18:.0f} "
                   f"{cx + r*0.98:.0f} {cy - r*0.35:.0f} "
                   f"Q {cx + r*0.55:.0f} {bang - r*0.1:.0f} {cx} {bang:.0f} "
                   f"Q {cx - r*0.55:.0f} {bang - r*0.1:.0f} {cx - r*0.98:.0f} {cy - r*0.35:.0f} Z",
                   hair_color))
    if brows:
        w = max(6, r * 0.045)
        p.append(P(f"M {cx - r*0.56:.0f} {cy - r*0.22:.0f} Q {cx - r*0.34:.0f} {cy - r*0.35:.0f} "
                   f"{cx - r*0.12:.0f} {cy - r*0.24:.0f}", stroke=hair_color, w=w))
        p.append(P(f"M {cx + r*0.12:.0f} {cy - r*0.24:.0f} Q {cx + r*0.34:.0f} {cy - r*0.35:.0f} "
                   f"{cx + r*0.56:.0f} {cy - r*0.22:.0f}", stroke=hair_color, w=w))
    if eyes_mode == "open":
        for sgn in (-1, 1):
            ex = cx + sgn * r * 0.32
            p.append(E(ex, cy - r * 0.10, r * 0.075, r * 0.105, INK))
            p.append(C(ex - sgn * r * 0.02, cy - r * 0.15, r * 0.026, WHITE))
    if nose:
        p.append(E(cx, cy + r * 0.11, r * 0.06, r * 0.05, SKIN_D))
    p.append(C(cx - r * 0.64, cy + r * 0.24, r * blush, PINK, 0.8))
    p.append(C(cx + r * 0.64, cy + r * 0.24, r * blush, PINK, 0.8))
    if mouth == "smile":
        p.append(P(f"M {cx - r*0.19:.0f} {cy + r*0.44:.0f} Q {cx:.0f} {cy + r*0.55:.0f} "
                   f"{cx + r*0.19:.0f} {cy + r*0.44:.0f}", stroke=INK, w=max(6, r * 0.045)))
    return wrap(*p)


# ---------- 各卡插画 ----------
def art_liu():
    """柳：圆簇树冠在顶，多条长弧枝统一向右弯垂下，枝上细长叶。"""
    g = ground()
    g += P("M 352 448 Q 362 384 356 312 Q 352 268 366 224", stroke=WOOD, w=26)
    crown = (C(380, 190, 72, GREEN) + C(380, 226, 56, GREEN)
             + C(304, 216, 50, LEAF_D) + C(456, 216, 50, LEAF_D)
             + C(336, 156, 44, GREEN_L, 0.92) + C(428, 160, 42, GREEN_L, 0.88)
             + C(380, 130, 36, GREEN_L, 0.85))
    strands = [(266, 224, 344, 80), (288, 238, 376, 96), (318, 252, 404, 100),
               (348, 258, 420, 104), (378, 262, 432, 106), (408, 262, 424, 100),
               (436, 256, 408, 96), (462, 244, 390, 92), (302, 228, 358, 90),
               (448, 232, 374, 88), (276, 246, 372, 88)]
    out = ""
    for i, (sx, sy, ey, dx) in enumerate(strands):
        col = (GREEN, LEAF_D, GREEN_L)[i % 3]
        mx, my = sx + dx * 0.72, (sy + ey) / 2
        ex = sx + dx
        out += P(f"M {sx} {sy} Q {mx:.0f} {my:.0f} {ex} {ey}", stroke=col, w=6)
        for j, t in enumerate((0.3, 0.5, 0.68, 0.84, 0.96)):
            x = (1 - t) ** 2 * sx + 2 * t * (1 - t) * mx + t * t * ex
            y = (1 - t) ** 2 * sy + 2 * t * (1 - t) * my + t * t * ey
            ddx = 2 * (1 - t) * (mx - sx) + 2 * t * (ex - mx)
            ddy = 2 * (1 - t) * (my - sy) + 2 * t * (ey - my)
            ang = math.degrees(math.atan2(ddy, ddx)) + (14 if j % 2 else -14)
            out += place(leaf(48, 10, col), x, y, ang)
    return g + crown + out


def art_feng():
    """枫：后层深色块改同心放大，修齐不外露。"""
    def maple(cx, cy, r, main, dark, vein, stem_c):
        pts = []
        for i in range(5):
            b = -90 + i * 72
            for off, rr in ((-34, 0.40), (-23, 0.66), (-11, 0.55),
                            (0, 1.0), (11, 0.55), (23, 0.66), (34, 0.40)):
                a = math.radians(b + off)
                pts.append((cx + r * rr * math.cos(a), cy + r * rr * math.sin(a)))
        g2 = PG([(cx + (x - cx) * 1.075, cy + (y - cy) * 1.075) for x, y in pts], dark)
        g2 += PG(pts, main)
        for i in range(5):
            a = math.radians(-90 + i * 72)
            g2 += L(cx, cy + r * 0.42, cx + r * 0.92 * math.cos(a),
                    cy + r * 0.92 * math.sin(a), vein, 5)
        return g2 + L(cx, cy + r * 0.40, cx, cy + r * 1.12, stem_c, 11)

    g = ground()
    g += maple(380, 272, 140, "#d4552f", "#b53a20", SUN, "#a83a22")
    g += place(maple(0, 0, 34, "#e8663c", "#c94a2e", SUN, "#a83a22"), 600, 146, 24)
    return g


def art_bee():
    """蜂：条纹全部移到下腹（脸部干净），黄身圆翅小触角。"""
    g = ground()
    g += flower5(478, 426, 22, "#f0876f", WHITE)
    for wx in (298, 462):
        g += C(wx + 4, 216, 40, "#bcd8ea") + C(wx, 210, 40, "#dff1fa", 0.92)
    g += P("M 362 224 Q 350 196 338 186", stroke=STRIPE, w=5) + C(336, 182, 7, STRIPE)
    g += P("M 398 224 Q 410 196 422 186", stroke=STRIPE, w=5) + C(424, 182, 7, STRIPE)
    g += blob(380, 300, 112, 86, BEE, BEE_D)
    # 腹纹：两条横带嵌在肚皮弧线内（不再压脸）
    g += PG([(288, 336), (472, 336), (459, 352), (301, 352)], STRIPE)
    g += PG([(312, 362), (448, 362), (422, 376), (338, 376)], STRIPE)
    g += eyes(346, 414, 286, r=10)
    g += smile(380, 314, 20, 6)
    g += blush(380, 320, 48, r=10)
    return g


def art_hu():
    """虎：体格放大一圈、深橙红、条纹加密，与猫明显拉开。"""
    g = ground()
    g += P("M 528 398 Q 604 396 608 320 Q 610 276 570 276", stroke=TIGER, w=24)   # 粗尾
    g += '<g transform="translate(586 378) rotate(-44)">' + R(-6, -16, 12, 32, 6, STRIPE) + "</g>"
    g += '<g transform="translate(604 295) rotate(66)">' + R(-6, -16, 12, 32, 6, STRIPE) + "</g>"
    g += C(572, 276, 13, TIGER)
    g += P("M 296 160 Q 278 104 308 98 Q 332 104 336 156 Z", fill=TIGER_D)        # 尖耳黑内耳
    g += P("M 305 144 Q 296 112 312 108 Q 322 114 323 142 Z", fill=STRIPE)
    g += P("M 464 160 Q 482 104 452 98 Q 428 104 424 156 Z", fill=TIGER_D)
    g += P("M 455 144 Q 464 112 448 108 Q 438 114 437 142 Z", fill=STRIPE)
    g += blob(380, 382, 150, 80, TIGER, TIGER_D)
    g += E(380, 402, 78, 44, WHITE)
    g += paw(304, 444, 33, 18, TIGER, TIGER_D) + paw(456, 444, 33, 18, TIGER, TIGER_D)
    g += cblob(380, 220, 102, TIGER, TIGER_D)
    g += L(354, 138, 406, 138, STRIPE, 10)                                        # 额头"王"
    g += L(346, 155, 414, 155, STRIPE, 10)
    g += L(356, 172, 404, 172, STRIPE, 10)
    g += L(380, 126, 380, 176, STRIPE, 9)
    g += P("M 306 318 Q 328 326 346 320", stroke=STRIPE, w=10)                    # 肩纹
    g += P("M 454 318 Q 432 326 414 320", stroke=STRIPE, w=10)
    for d in ("M 252 344 Q 278 352 290 368", "M 240 388 Q 264 392 278 404",
              "M 260 428 Q 280 432 294 440",                                      # 侧纹 ×3/侧
              "M 508 344 Q 482 352 470 368", "M 520 388 Q 496 392 482 404",
              "M 500 428 Q 480 432 466 440"):
        g += P(d, stroke=STRIPE, w=11)
    g += E(380, 272, 50, 34, WHITE)
    g += PG([(368, 258), (392, 258), (380, 272)], "#8a5a33")
    g += wmouth(380, 274, 12)
    g += eyes(344, 416, 196)
    g += blush(380, 238, 78)
    return g


def art_niu():
    """牛：牛角加大加清晰（识别特征），鼻吻改浅灰去猪鼻感，其余沿用旧画法。"""
    g = ground()
    g += P("M 512 380 Q 556 384 560 428", stroke=COW_D, w=10) + C(561, 432, 12, SPOT)
    g += P("M 342 134 Q 306 130 292 106 Q 286 96 294 90", stroke="#e6d3a8", w=24)  # 大牛角（外弯）
    g += P("M 338 126 Q 310 122 300 104 Q 296 97 301 93", stroke="#f2e6c8", w=10)
    g += P("M 418 134 Q 454 130 468 106 Q 474 96 466 90", stroke="#e6d3a8", w=24)
    g += P("M 422 126 Q 450 122 460 104 Q 464 97 459 93", stroke="#f2e6c8", w=10)
    g += E(296, 162, 32, 18, COW_W) + E(296, 163, 18, 10, "#f2bfa8")
    g += E(464, 162, 32, 18, COW_W) + E(464, 163, 18, 10, "#f2bfa8")
    g += cblob(380, 208, 92, COW_W, COW_D)
    g += blob(380, 372, 140, 88, COW_W, COW_D)
    for sx, sy, srx, sry in ((302, 348, 34, 26), (458, 396, 30, 24), (420, 330, 22, 17), (330, 420, 20, 15)):
        g += E(sx, sy, srx, sry, SPOT)
    g += E(332, 152, 30, 20, SPOT)
    g += E(380, 250, 56, 36, "#ddd6c8")                                           # 浅灰鼻吻
    g += E(362, 250, 7, 10, "#a89c8a") + E(398, 250, 7, 10, "#a89c8a")
    g += smile(380, 272, 12, 4, "#8f8676")
    g += eyes(344, 416, 196)
    g += blush(380, 232, 70)
    g += E(286, 424, 24, 16, COW_D) + E(474, 424, 24, 16, COW_D)
    g += paw(318, 432, 28, 18, COW_W, COW_D) + paw(442, 432, 28, 18, COW_W, COW_D)
    return g


def art_chuang():
    """窗：黄框方窗，窗格里太阳+云（例句"窗外有太阳"）。"""
    rays = "".join(
        L(450 + 31 * math.cos(math.radians(i * 45)), 198 + 31 * math.sin(math.radians(i * 45)),
          450 + 45 * math.cos(math.radians(i * 45)), 198 + 45 * math.sin(math.radians(i * 45)),
          "#d99a2b", 6)
        for i in range(8))
    return wrap(
        ground(),
        E(380, 430, 182, 14, INK, 0.08),
        R(228, 126, 304, 260, 22, YEL),
        R(252, 150, 256, 212, 8, SKY),
        rays,
        C(450, 198, 26, SUN),
        C(450, 198, 19, SUN_L),
        cloud_p(310, 206, 0.62),
        cloud_p(452, 318, 0.5),
        R(368, 150, 24, 212, 10, YEL),
        R(252, 242, 256, 24, 10, YEL),
        R(212, 384, 336, 28, 13, YEL_D),
    )


def art_fa():
    """发：浓密盖头黑发+两侧鬓角连成一体（去"耳机"块），梳子保留。"""
    teeth = "".join(R(-58 + i * 15, 10, 9, 50, 4.5, WOOD_L) for i in range(8))
    return ground(380, 452, 255, 22) + _face(hair=False, brows=False) + wrap(
        P("M 221 221 Q 234 87 380 97 Q 526 87 539 221 Q 469 190 380 239 Q 291 190 221 221 Z", INK),
        P("M 240 202 Q 216 244 220 292 Q 222 316 242 334 Q 240 298 252 262 Q 258 228 252 204 Z", INK),
        P("M 520 202 Q 544 244 540 292 Q 538 316 518 334 Q 520 298 508 262 Q 502 228 508 204 Z", INK),
        P("M 296 158 Q 324 132 362 124", stroke="#7a5a40", w=9),
        P("M 262 196 Q 288 164 322 148", stroke="#7a5a40", w=8),
        P("M 386 120 Q 424 122 452 136", stroke="#7a5a40", w=7),
        '<g transform="translate(600 188) rotate(35)">'
        + R(-66, -13, 132, 26, 13, WOOD)
        + R(-58, -9, 92, 8, 4, "#f4d3a4", 0.8) + teeth + "</g>")


def art_du():
    """肚：圆肚居中，肚脐露在圆肚正中；绿色下移成裤腰弧、下接蓝色裤身（不再像帽子）。"""
    return ground(380, 452, 245, 22) + wrap(
        E(388, 344, 132, 108, SKIN_D), E(380, 338, 130, 106, SKIN),
        E(380, 352, 76, 44, "#fad4b0"),
        C(380, 342, 22, PINK, 0.4),
        E(380, 342, 12, 16, SKIN_D), E(380, 344, 6, 9, "#c9835a"),
        P("M 254 366 A 130 106 0 0 0 506 366 Z", GREEN),
        P("M 254 366 Q 380 384 506 366", stroke=GREEN_L, w=9),
        P("M 287 414 A 130 106 0 0 0 473 414 Z", BLUE_D),
        P("M 287 414 Q 380 428 473 414", stroke="#5fa8d8", w=8))


def _apricot(cx, cy, r):
    """整颗黄橙杏。"""
    return wrap(
        C(cx + 4, cy + 5, r, "#d97b28"), C(cx, cy, r, "#f2a44c"),
        E(cx + r * 0.3, cy + r * 0.25, r * 0.62, r * 0.72, "#f0913c", 0.75),
        P(f"M {cx} {cy - r + 6} Q {cx + r * 0.16} {cy} {cx - r * 0.05} {cy + r - 4}",
          stroke="#d97b28", w=4, opacity=0.6),
        C(cx - r * 0.32, cy - r * 0.36, r * 0.18, WHITE, 0.7),
        L(cx, cy - r, cx + 4, cy - r - 14, "#8a5a33", 6))


def art_xing():
    """杏：枝条收进卡内不切边，黄橙杏子挂枝头，果下补投影理顺支撑。"""
    g = ground()
    g += E(268, 446, 62, 11, SHAD) + E(462, 448, 72, 12, SHAD) + E(596, 442, 50, 10, SHAD)
    g += P("M 88 170 Q 240 132 400 152 Q 540 170 672 150", stroke="#a9743f", w=15)
    g += place(leaf_veined(76, 26, GREEN, LEAF_BB), 150, 164, -30)
    g += place(leaf_veined(70, 24, GREEN_L, LEAF_BB), 560, 160, 25)
    g += L(282, 152, 268, 238, "#8a5a33", 7)
    g += L(470, 158, 462, 254, "#8a5a33", 7)
    g += L(598, 152, 596, 236, "#8a5a33", 7)
    g += _apricot(268, 318, 84)
    g += _apricot(596, 296, 62)
    g += wrap(
        C(466, 345, 90, "#d97b28"), C(462, 340, 90, "#f2a44c"),
        C(462, 338, 72, "#f8c06a"),
        C(462, 338, 30, "#8a5a33"), C(462, 338, 12, "#6e4322"),
        P("M 438 332 Q 462 324 486 332", stroke="#6e4322", w=4, opacity=0.6),
        P("M 440 346 Q 462 354 484 346", stroke="#6e4322", w=4, opacity=0.6),
        C(444, 322, 9, WHITE, 0.55),
        L(462, 252, 462, 270, "#8a5a33", 7))
    return g


def art_yang():
    """洋：海占满整卡宽（不见岸），远处一艘大轮船点出辽阔。"""
    g = ground(fill="#2f6a94")
    g += R(0, 0, 760, 480, 0, "#3d84b8")
    g += P("M 0 250 Q 106 180 212 250 Q 318 320 424 250 Q 530 180 636 250 "
           "Q 700 294 760 252 L 760 480 L 0 480 Z", "#4a97c9")
    g += wrap(
        PG([(150, 242), (334, 242), (310, 280), (174, 280)], RED),
        R(198, 208, 84, 36, 8, WHITE),
        R(270, 184, 26, 30, 7, "#9aa1aa"),
        C(304, 166, 11, WHITE, 0.9), C(324, 148, 8, WHITE, 0.8),
        C(220, 226, 7, "#aee0f2"), C(244, 226, 7, "#aee0f2"), C(262, 226, 7, "#aee0f2"))
    g += P("M 0 340 Q 116 276 232 340 Q 348 404 464 340 Q 580 276 696 340 "
           "Q 732 360 760 344 L 760 480 L 0 480 Z", "#5fa8d8")
    g += P("M 0 430 Q 126 376 252 430 Q 378 484 504 430 Q 630 376 760 434 "
           "L 760 480 L 0 480 Z", "#79c2e6")
    g += (C(106, 218, 12, WHITE) + C(130, 224, 8, WHITE) + C(530, 218, 11, WHITE)
          + C(552, 225, 7, WHITE) + C(116, 310, 10, WHITE) + C(138, 316, 7, WHITE)
          + C(580, 310, 10, WHITE) + C(126, 404, 9, WHITE) + C(150, 410, 7, WHITE)
          + C(634, 404, 8, WHITE))
    return g


ARTS = {
    "柳": art_liu(), "蜂": art_bee(), "虎": art_hu(), "牛": art_niu(),
    "窗": art_chuang(), "发": art_fa(), "肚": art_du(),
    "杏": art_xing(), "枫": art_feng(), "洋": art_yang(),
}

if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    expect = ["柳", "蜂", "虎", "牛", "窗", "发", "肚", "杏", "枫", "洋"]
    assert sorted(ARTS) == sorted(expect), list(ARTS)
    for k, v in ARTS.items():
        low = v.lower()
        for bad in ("<svg", "<defs", "<use", "<text", "<image"):
            assert bad not in low, (k, bad)
        ET.fromstring(f'<g xmlns="http://www.w3.org/2000/svg">{v}</g>')
        assert v.startswith("<ellipse"), k  # 第一笔必须是 ground()
    print("修复D 自检通过：", " ".join(ARTS))
