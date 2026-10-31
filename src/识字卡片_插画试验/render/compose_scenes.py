#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把三个部件库方案统一拼装成「找」场景卡（760×480，与识字卡同规格）。

- 02 Open Peeps：node 渲染的全身小人 + 代码画放大镜挂到指尖
- 03 Humaaans：standing-5 前伸手姿 + 放大镜，色板映射到本库 PALETTE
- 04 DiceBear：四种头像风 + 放大镜（头像无动作，考察"只能当名词卡"的短板）
"""
import re

HERE = "/Users/ping/C 行动_与人交流/孩子/识字卡片_插画试验"

PAGE, GROUND = "#fdf8ec", "#c8e6d8"
WOOD, WOOD_D, WBLUE, RED, INK = "#c89058", "#b57b44", "#79c2e6", "#e8663c", "#4a3226"


def magnifier(cx, cy, ring=WOOD, handle_from=None, s=1.0):
    """放大镜：圆心 (cx,cy)，可指定把手起点。"""
    parts = []
    if handle_from:
        hx, hy = handle_from
        dx, dy = cx - hx, cy - hy
        n = (dx * dx + dy * dy) ** 0.5
        ex, ey = hx + dx * (n - 46 * s) / n, hy + dy * (n - 46 * s) / n
        parts.append(f'<line x1="{hx}" y1="{hy}" x2="{ex}" y2="{ey}" stroke="{WOOD}" stroke-width="{16*s}" stroke-linecap="round"/>')
    parts += [
        f'<circle cx="{cx}" cy="{cy}" r="{56*s}" fill="{WOOD_D}"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{47*s}" fill="{ring}"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{40*s}" fill="{WBLUE}" opacity="0.35"/>',
        f'<circle cx="{cx+8*s}" cy="{cy+8*s}" r="{11*s}" fill="{RED}"/>',
        f'<line x1="{cx+8*s}" y1="{cy-3*s}" x2="{cx+8*s}" y2="{cy+19*s}" stroke="{INK}" stroke-width="{3*s}"/>',
        f'<circle cx="{cx+3*s}" cy="{cy+4*s}" r="{1.8*s}" fill="{INK}"/>',
        f'<circle cx="{cx+13*s}" cy="{cy+4*s}" r="{1.8*s}" fill="{INK}"/>',
        f'<circle cx="{cx-14*s}" cy="{cy-14*s}" r="{9*s}" fill="#ffffff" opacity="0.5"/>',
    ]
    return "".join(parts)


def card(inner):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
            f'<rect width="760" height="480" fill="{PAGE}"/>'
            f'<ellipse cx="380" cy="446" rx="240" ry="24" fill="{GROUND}"/>' + inner + "</svg>")


# ---------- 02 Open Peeps ----------
peep = open(f"{HERE}/02_openpeeps/peep_body.svg").read()
inner = re.sub(r"^.*?<svg[^>]*>", "", peep, flags=re.S).replace("</svg>", "")
# 指尖(body画布约 1516,121) 映射到卡片 (390,212)；脚底 2186 → 卡 445
s02, tx02, ty02 = 0.145, 170, 128
tip = (tx02 + 1516 * s02, ty02 + (121 + 460) * s02)
glass = (tip[0] + 28, tip[1] - 44)
scene02 = card(
    f'<g transform="translate({tx02},{ty02}) scale({s02})" style="fill-rule:evenodd">{inner}</g>'
    + magnifier(glass[0], glass[1], handle_from=tip)
)
open(f"{HERE}/02_openpeeps/找_openpeeps.svg", "w").write(scene02)

# ---------- 03 Humaaans ----------
hum = open(f"{HERE}/humaaans/Flat Assets/Humaaans/standing-5.svg").read()
hum = re.sub(r"<\?xml[^>]*\?>", "", hum)
inner3 = re.sub(r"^.*?<svg[^>]*>", "", hum, flags=re.S).replace("</svg>", "")
remap = {
    "191847": "4a3226",  # 深藏青（头发/裤/鞋）→ 深暖棕
    "1F28CF": "4a97c9",  # 蓝毛衣深 → BLUE_D
    "2B44FF": "5fa8d8",  # 蓝毛衣亮 → BLUE
    "69A1AC": "f8cba4",  # 冷皮 → SKIN
    "915B3C": "eeb28a",  # 暖皮 → SKIN_D
    "C5CFD6": "d9d0c5",  # 浅灰 → 暖灰
    "DDE3E9": "e9dfc8",
    "000000": "5a3d2b",
}
for a, b in remap.items():
    inner3 = inner3.replace("#" + a, "#" + b).replace('"' + a.lower() + '"', '"' + b + '"')
# 手在 humaaans 画布约 (258,118)；脚 ~470。缩放 0.85，脚底落 445
s03, tx03, ty03 = 0.85, 150, 445 - 470 * 0.85
hand = (tx03 + 258 * s03, ty03 + 118 * s03)
glass3 = (hand[0] + 66, hand[1] - 30)
scene03 = card(
    f'<g transform="translate({tx03},{ty03}) scale({s03})">{inner3}</g>'
    + magnifier(glass3[0], glass3[1], handle_from=hand)
)
open(f"{HERE}/03_humaaans/找_humaaans.svg", "w").write(scene03)

# ---------- 04 DiceBear（2×2 连拍） ----------
styles = ["croodles", "open-peeps", "big-smile", "adventurer"]
cells = []
for idx, st in enumerate(styles):
    d = open(f"{HERE}/04_dicebear/{st}.svg").read()
    d = re.sub(r"<\?xml[^>]*\?>", "", d)
    di = re.sub(r"^.*?<svg[^>]*>", "", d, flags=re.S).replace("</svg>", "")
    x, y = (idx % 2) * 380, (idx // 2) * 240
    # 头像画布约 200×200，缩放到 170 放入 380×240 的格子底部居中
    sc = 170 / 200
    tx, ty = x + (380 - 200 * sc) / 2, y + 240 - 200 * sc - 14
    # 放大镜放在头像手边（右下），模拟"拿着"——头像本身无动作
    cells.append(
        f'<g transform="translate({tx},{ty}) scale({sc})">{di}</g>'
        + magnifier(x + 380 - 78, y + 240 - 52, s=0.55)
    )
scene04 = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
           f'<rect width="760" height="480" fill="{PAGE}"/>' + "".join(cells) + "</svg>")
open(f"{HERE}/04_dicebear/找_dicebear_四风格.svg", "w").write(scene04)

print("written 3 scenes")
