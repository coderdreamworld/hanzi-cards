# -*- coding: utf-8 -*-
"""批次A修复稿：别 / 洗 / 爷 / 哥（待用户确认，不并入正式素材文件）。

别：大人从右侧伸臂拦住奔跑的小孩——手臂从肩连到手端，hand 只画在臂端；小孩 sprint 急停+速度线。
洗：台盆（柜体落地+台面+盆体）支撑链完整，水龙头立在台面上，水流入手盆，小孩伸手在水下搓洗。
爷：白发白眉 + 鼻下白色半圆垂坠胡子 + 眼镜 + 拐杖（插在 swing 右手端）+ stride 大步走。
哥：哥哥（高、戴棒球帽）踢球，皮球悬在两人之间，弟弟（矮）张手接球。
"""
import importlib.util, math, pathlib

spec = importlib.util.spec_from_file_location("suk", str(pathlib.Path(__file__).parent / ".." / "识字卡片_素材库.py"))
suk = importlib.util.module_from_spec(spec); spec.loader.exec_module(suk)

ARTS = {}


def _bie():
    """别：大人拦臂 + 小孩急停。臂端坐标按 kid 内部画法计算（角度取整一致）。"""
    ax, ay, s = 590, 452, 1.15
    sho = ay - 168 * s                       # 肩高
    pat = (735.0, 288.0)                     # point_at（局部坐标；flip=-1 镜像后指向左侧小孩）
    ang = round(math.degrees(math.atan2(pat[1] - (sho + 10 * s), pat[0] - (ax + 44 * s))))
    rad = math.radians(ang)
    ex = 2 * ax - (ax + 44 * s + 86 * s * math.cos(rad))   # 臂端（画布坐标）
    ey = sho + 6 * s + 86 * s * math.sin(rad)
    g = suk.ground()
    g += suk.kid(250, 446, s=0.72, pose="sprint", arms="pump", face="o", look=(2, -0.2))
    g += suk.L(148, 296, 202, 296, suk.TEAL_L, 7)          # 身后速度线
    g += suk.L(134, 340, 188, 340, suk.TEAL_L, 7)
    g += suk.kid(ax, ay, s=s, flip=-1, arms="point", point_at=pat, face="o",
                 look=(-2, -0.2), shirt=suk.GREEN)
    g += suk.hand(ex, ey, rot=-18, s=0.58)                 # 手掌长在臂端：停！
    return g


def _xi():
    """洗：落地台盆 + 台面立管龙头 + 水流入盆 + 小孩伸手在水下。"""
    cx = 300
    g = suk.ground()
    g += suk.R(cx - 85, 356, 170, 90, 12, "#cfe6f0")       # 柜体（底 446 落地）
    g += suk.R(cx - 105, 340, 210, 20, 8, suk.TEAL_L)      # 台面
    g += suk.E(cx, 341, 76, 15, suk.TEAL_D)                # 盆沿
    g += suk.E(cx, 339, 60, 11, suk.WBLUE)                 # 盆中水
    g += suk.R(cx - 72, 268, 20, 74, 9, suk.TEAL_D)        # 龙头立管（底 342 站在台面上）
    g += suk.C(cx - 62, 261, 10, suk.TEAL_L)               # 开关
    g += suk.C(cx - 62, 261, 4.5, suk.WHITE)
    g += suk.R(cx - 62, 268, 112, 20, 10, suk.TEAL_D)      # 横臂（连立管 → 盆上方）
    g += suk.R(cx + 30, 284, 20, 14, 5, suk.TEAL_D)        # 出水口
    g += suk.R(cx + 31, 296, 18, 48, 8, suk.WBLUE)         # 水流（落进盆里的水）
    g += suk.kid(430, 446, s=0.95, arms="reach", face="smile", look=(-1.6, 0.5), shirt=suk.YEL)
    g += suk.C(318, 333, 9, "#cfe6f0") + suk.C(318, 333, 6, suk.WHITE)   # 泡泡
    g += suk.C(350, 329, 8, "#cfe6f0") + suk.C(350, 329, 5, suk.WHITE)
    g += suk.C(337, 350, 7, suk.WHITE, 0.9)                # 手边的泡泡
    g += suk.C(264, 322, 6, "#cfe6f0", 0.9)
    return g


def _ye():
    """爷：stride 走姿 + 眼镜 + 拐杖（连在 swing 右手端）+ 鼻下白色垂坠胡。"""
    x, y, s = 380, 446, 1.05
    sho = y - 168 * s
    hx, hy = x + 80 * s, sho + 56 * s        # swing 右手端（kid 内部臂端）
    beard = suk.P(f"M {x - 28} 229 Q {x - 31} 273 {x} 287 Q {x + 31} 273 {x + 28} 229 "
                  f"Q {x} 242 {x - 28} 229 Z", "#d9d0c5")  # 鼻下半圆垂坠，不盖嘴
    g = suk.ground()
    g += suk.kid(x, y, s=s, pose="stride", arms="swing", shirt=suk.WOOD_D,
                 hair_color="#d9d0c5", mustache=True, glasses=True,
                 look=(1.2, 0.3), extra=beard)
    g += suk.L(hx, hy + 6, x + 96, 441, suk.WOOD, 14)      # 拐杖：从手心到地面
    g += suk.C(hx, hy, 9, suk.WOOD_D)                      # 杖柄（握在手圆里）
    g += suk.E(x + 96, 442, 12, 6, suk.WOOD_D)             # 杖脚落地
    return g


def _ge():
    """哥：哥哥（高、戴帽）踢球，球悬在两人之间，弟弟（矮）张手接。"""
    bx, by, bs = 250, 448, 0.95
    sho = by - 168 * bs
    hcy = sho - 8 * bs - 62 * bs             # 头心
    cap = (suk.P(f"M {bx - 52} {hcy - 36} Q {bx - 58} {hcy - 92} {bx} {hcy - 96} "
                 f"Q {bx + 58} {hcy - 92} {bx + 52} {hcy - 36} "
                 f"Q {bx} {hcy - 60} {bx - 52} {hcy - 36} Z", suk.RED)
           + suk.E(bx, hcy - 38, 62, 10, suk.RED_D)
           + suk.C(bx, hcy - 97, 8, suk.RED_D))
    dash = (f' stroke-linecap="round" stroke-dasharray="2 16" fill="none"')
    g = suk.ground()
    g += suk.kid(bx, by, s=bs, pose="stride", arms="swing", face="smile",
                 look=(1.5, 0.4), shirt=suk.WBLUE, extra=cap)
    g += f'<path d="M 300 424 Q 336 398 362 362" stroke="{suk.TEAL}" stroke-width="6"{dash}/>'
    g += f'<path d="M 418 300 Q 444 288 460 285" stroke="{suk.TEAL}" stroke-width="6"{dash}/>'
    g += suk.ball(390, 330, 32, suk.RED, suk.RED_D, suk.PINK)   # 球在两人之间
    g += suk.kid(530, 448, s=0.75, arms="up", face="open", look=(-1.5, -0.8), shirt=suk.GREEN)
    return g


ARTS["别"] = _bie()
ARTS["洗"] = _xi()
ARTS["爷"] = _ye()
ARTS["哥"] = _ge()

if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    assert set(ARTS) == {"别", "洗", "爷", "哥"}
    for k, v in ARTS.items():
        ET.fromstring(f'<g xmlns="http://www.w3.org/2000/svg">{v}</g>')
    print("OK", sorted(ARTS))
