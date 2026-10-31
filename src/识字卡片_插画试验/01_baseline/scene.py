#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""基线组：用现有素材库组件画「找」场景（小孩举放大镜）。

验证点：kid() 组件用对姿势时人体比例是否成立；手持物需要自行计算手端点
（素材库的 item 参数只有签名没有实现）。
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "识字卡片_素材库.py")

spec = importlib.util.spec_from_file_location("suk", LIB)
suk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(suk)

x, y, s = 330, 430, 1.15          # kid 站位与脚底
px, py = 470, 242                  # point 手势指向（放大镜把手位置）

# 复刻 kid() 内部的 point 手臂数学，算出手端点，让放大镜正好握在手里
sho = y - 168 * s
sh_r = (x + 44 * s, sho + 6 * s)
ang = math.atan2(py - (sho + 10 * s), px - sh_r[0])
hx = sh_r[0] + 86 * s * math.cos(ang)
hy = sh_r[1] + 86 * s * math.sin(ang)
gx, gy = hx + 42 * math.cos(ang), hy + 42 * math.sin(ang)   # 玻璃圆心沿手臂方向延长

mag = suk.wrap(
    suk.L(hx, hy, gx, gy, suk.WOOD, 16),                 # 把手
    suk.C(gx, gy, 56, suk.WOOD_D),                       # 镜框外圈
    suk.C(gx, gy, 47, suk.WOOD),                         # 镜框内圈
    suk.C(gx, gy, 40, suk.WBLUE, 0.35),                  # 玻璃
    suk.C(gx + 8, gy + 8, 11, suk.RED),                  # 镜下小瓢虫（被找到的目标）
    suk.L(gx + 8, gy - 3, gx + 8, gy + 19, suk.INK, 3),  # 瓢虫翅缝
    suk.C(gx + 3, gy + 4, 1.8, suk.INK),
    suk.C(gx + 13, gy + 4, 1.8, suk.INK),
    suk.C(gx - 14, gy - 14, 9, "#ffffff", 0.5),          # 玻璃高光
)

kid = suk.kid(x=x, y=y, s=s, pose="stand", face="smile", shirt=suk.BLUE,
              arms="point", point_at=(px, py), look=(34, -18))

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
       f'<rect width="760" height="480" fill="{suk.PAGE}"/>'
       + suk.ground() + kid + mag + "</svg>")

out = os.path.join(HERE, "找_baseline.svg")
with open(out, "w") as f:
    f.write(svg)
print(out, len(svg), "bytes")
