#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""天文组插画与文案（「日」为种子卡，由构建脚本提供，不在本模块）。

9 字：月 星 云 电 风 雨 雪 虹 冰
- 夜景卡（月/星）共用深蓝夜空面板 NIGHT（BLUE 同族深色），靠剪影区分：月牙 vs 五角星。
- 云/雪用浅蓝天空面板，雪的面板更深一号，白色雪花更跳。
- 电用淡紫灰底 LAV 显夜雨感；风/雨/虹按语义铺底，冰放在冰凉浅色地面上。
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from 识字卡片_素材库 import (C, E, GREEN, GREEN_L, INK, L, P, PG, PINK, R, SUN, SUN_L,
                          WHITE, WBLUE, WOOD_D, YEL, YEL_D, cloud_p, drop, flower5,
                          ground, star5, wrap)

NIGHT = "#2e4d74"      # 深蓝夜空（BLUE 同族深色）
SKY_L = "#dceefa"      # 白天浅蓝天空（云卡）
SKY_L2 = "#c9e3f5"     # 更深一号的浅蓝（雪卡，衬白雪花）
LAV = "#c3b8d6"        # 淡紫灰（电卡夜雨底色）
GREEN_DK = "#5f8f52"   # 深一号绿（柳条/草，GREEN 同族）
RAIN_L = "#a5d9f0"     # 雨水浅蓝（WBLUE 同族）


GROUP_CARDS = [
    {"char": "月", "pinyin": "yuè", "tone": "第四声",
     "sentence": "月亮弯弯挂夜空。",
     "say": "弯弯的是月亮，晚上挂在天上。",
     "chat": "“月亮什么时候出来？”",
     "life": "晚上带他找一找月亮，看看缺了哪一块。"},
    {"char": "星", "pinyin": "xīng", "tone": "第一声",
     "sentence": "天上有颗大星星。",
     "say": "一闪一闪的是星星，晚上数一数。",
     "chat": "“你看到几颗星星？”",
     "life": "晴朗的晚上到楼下抬头找星星。"},
    {"char": "云", "pinyin": "yún", "tone": "第二声",
     "sentence": "白云朵朵天上飘。",
     "say": "天上白白的叫云，慢慢飘。",
     "chat": "“那朵云像什么？”",
     "life": "抬头看云，说说自己看到的形状。"},
    {"char": "电", "pinyin": "diàn", "tone": "第四声",
     "sentence": "闪电咔嚓一闪。",
     "say": "闪电是天上一闪一闪的亮光。",
     "chat": "“打雷闪电时要躲在哪里？”",
     "life": "下雨打闪时一起看窗外，数一数闪了几次。"},
    {"char": "风", "pinyin": "fēng", "tone": "第一声",
     "sentence": "风吹叶子沙沙响。",
     "say": "风看不见，叶子动就是风来了。",
     "chat": "“今天的风大不大，你怎么知道？”",
     "life": "跑一跑感受风，或拿张纸片看它飘。"},
    {"char": "雨", "pinyin": "yǔ", "tone": "第三声",
     "sentence": "下雨啦，滴滴答答。",
     "say": "天上掉下来的小水点就是雨。",
     "chat": "“雨点打在伞上是什么声音？”",
     "life": "下次下雨听一听雨声，踩踩小水花。"},
    {"char": "雪", "pinyin": "xuě", "tone": "第三声",
     "sentence": "雪花飘飘落下来。",
     "say": "白白软软的是雪，冬天才有。",
     "chat": "“雪花是什么颜色的？”",
     "life": "下雪时接一片雪花看一看，堆个小雪球。"},
    {"char": "虹", "pinyin": "hóng", "tone": "第二声",
     "sentence": "雨后天上出彩虹。",
     "say": "雨停后天上弯弯的七色带叫彩虹。",
     "chat": "“彩虹有哪几种颜色？”",
     "life": "雨后出门找一找彩虹，看不到就看图片。"},
    {"char": "冰", "pinyin": "bīng", "tone": "第一声",
     "sentence": "冰块凉凉又硬硬。",
     "say": "水冻起来就变成冰，又冷又硬。",
     "chat": "“冰摸起来是什么感觉？”",
     "life": "冻一格冰块让他摸一摸，看它化成水。"},
]


def _leaf(x, y, rot, rx=17, ry=8, fill=GREEN):
    """小叶片（斜椭圆），配合风卡的倾斜动势。"""
    return f'<g transform="rotate({rot} {x} {y})">{E(x, y, rx, ry, fill)}</g>'


def _blade(x, y, s=1.0):
    """被风吹弯的小草（向左倒）。"""
    return P(f"M {x} {y} Q {x - 14 * s} {y - 10 * s} {x - 26 * s} {y - 28 * s}",
             stroke=GREEN_DK, w=6)


# ---------- 插画 ----------
def art_月():
    """深蓝夜空大面积 + 金黄弯月（闭眼睡眠感），无星（星是另一张卡）。"""
    return wrap(
        ground(),
        R(70, 48, 620, 372, 36, NIGHT),
        P("M 380 128 A 122 122 0 1 1 380 372 A 175 175 0 0 0 380 128 Z", YEL),
        P("M 443 238 Q 455 248 467 238", stroke=INK, w=6),      # 闭眼：睡着
        P("M 444 288 Q 456 298 468 288", stroke=INK, w=6),      # 微笑
        C(476, 262, 9, PINK, 0.75),
    )


def art_星():
    """同一夜空底，主角换成一颗带笑脸的大五角星 + 两颗小星。"""
    return wrap(
        ground(),
        R(70, 48, 620, 372, 36, NIGHT),
        star5(230, 152, 26, SUN_L),
        star5(534, 346, 18, SUN_L),
        f'<g transform="translate(6,8)">{star5(380, 258, 118, YEL_D)}</g>',
        star5(380, 258, 118, YEL),
        C(354, 252, 8, INK), C(406, 252, 8, INK),
        C(357, 249, 2.6, WHITE), C(409, 249, 2.6, WHITE),
        P("M 364 276 Q 380 290 396 276", stroke=INK, w=6),
        C(336, 268, 9, PINK, 0.75), C(424, 268, 9, PINK, 0.75),
    )


def art_云():
    """浅蓝天空 + 占满画面的大白云（带浅蓝底衬与笑脸）。"""
    shade = f'<g transform="translate(0,12)">{cloud_p(380, 258, 2.6, "#cfe4f4")}</g>'
    return wrap(
        ground(),
        R(70, 48, 620, 372, 36, SKY_L),
        shade,
        cloud_p(380, 258, 2.6, WHITE),
        C(344, 246, 9, INK), C(416, 246, 9, INK),
        C(347, 243, 3, WHITE), C(419, 243, 3, WHITE),
        P("M 356 274 Q 380 292 404 274", stroke=INK, w=7),
        C(320, 264, 12, PINK, 0.8), C(440, 264, 12, PINK, 0.8),
    )


def art_电():
    """淡紫灰夜雨底 + 金黄粗闪电（圆头折线，深一号色偏移做体积）。"""
    d = "M 442 96 L 350 240 L 416 240 L 324 392"
    shadow = P(d, stroke=YEL_D, w=54)
    return wrap(
        ground(),
        R(70, 48, 620, 372, 36, LAV),
        f'<g transform="translate(9,10)">{shadow}</g>',
        P(d, stroke=YEL, w=54),
    )


def _cubic_tangents(p0, p1, p2, p3, n):
    """三次贝塞尔曲线上 n 个采样点的 (x, y, 切线角)。"""
    pts = []
    for i in range(1, n + 1):
        t = i / n
        mt = 1 - t
        x = mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t ** 3 * p3[0]
        y = mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t ** 3 * p3[1]
        dx = 3 * mt * mt * (p1[0] - p0[0]) + 6 * mt * t * (p2[0] - p1[0]) + 3 * t * t * (p3[0] - p2[0])
        dy = 3 * mt * mt * (p1[1] - p0[1]) + 6 * mt * t * (p2[1] - p1[1]) + 3 * t * t * (p3[1] - p2[1])
        pts.append((x, y, math.degrees(math.atan2(dy, dx))))
    return pts


def _frond(p0, p1, p2, p3):
    """一条柳条：曲线茎 + 沿途叶片（叶向随风同侧倾斜）。"""
    g = P(f"M {p0[0]} {p0[1]} C {p1[0]} {p1[1]} {p2[0]} {p2[1]} {p3[0]} {p3[1]}",
          stroke=GREEN_DK, w=7)
    for i, (x, y, ang) in enumerate(_cubic_tangents(p0, p1, p2, p3, 9)):
        g += _leaf(x, y + 5, ang + 8, rx=17, ry=7, fill=GREEN if i % 2 else GREEN_L)
        if i % 2 == 0:
            g += _leaf(x + 8, y - 6, ang - 6, rx=13, ry=5.5, fill=GREEN_L)
    return g


def art_风():
    """一棵完整的柳树被风吹得柳条向左扬起，叶、落叶、小花全朝左，树干完整在画面内。"""
    tree = wrap(
        f'<g transform="rotate(5 620 440)">{R(600, 200, 40, 244, 18, WOOD_D)}</g>',
        C(620, 168, 58, GREEN_DK),
        C(580, 196, 44, GREEN, 0.95),
        C(664, 190, 46, GREEN_L, 0.9),
    )
    willow = wrap(
        _frond((576, 150), (452, 170), (336, 180), (168, 208)),
        _frond((568, 178), (452, 214), (340, 228), (176, 274)),
        _frond((560, 204), (452, 248), (348, 268), (208, 322)),
    )
    flying = wrap(
        _leaf(140, 352, -34, fill=GREEN_L), _leaf(238, 384, 18, fill=YEL), _leaf(104, 396, -14),
    )
    flower = wrap(
        P("M 138 344 Q 148 362 168 372", stroke=GREEN_DK, w=5),
        flower5(136, 328, 16, PINK, SUN),
        _leaf(206, 300, -28, rx=13, ry=6, fill=PINK),
    )
    swoosh = wrap(
        P("M 70 116 C 180 92 300 116 420 84", stroke="#bcd7e8", w=6),
        P("M 88 208 C 204 184 322 208 440 172", stroke="#bcd7e8", w=6),
    )
    grass = wrap(_blade(300, 436), _blade(330, 442, 0.8), _blade(468, 440),
                 _blade(500, 434, 0.9), _blade(590, 442, 0.8))
    return wrap(ground(), swoosh, tree, willow, flying, flower, grass)


def art_雨():
    """乌云 + 斜雨丝（线段为主、两颗雨滴）+ 地上一滩小水花。"""
    cloud = wrap(
        cloud_p(380, 168, 1.9, "#7a828d"),
        cloud_p(380, 152, 1.9, "#9098a3"),
    )
    rain = wrap(
        L(296, 218, 268, 330, WBLUE, 7),
        L(344, 224, 318, 344, WBLUE, 7),
        L(392, 218, 364, 330, WBLUE, 7),
        L(440, 224, 414, 344, WBLUE, 7),
        L(486, 218, 458, 330, WBLUE, 7),
        drop(300, 368, 11), drop(452, 374, 11),
    )
    splash = wrap(
        E(380, 424, 118, 20, RAIN_L),
        E(380, 420, 92, 14, "#bfe4f6"),
        P("M 300 412 Q 318 394 336 410", stroke="#9fd3ee", w=6),
        P("M 428 410 Q 446 392 464 408", stroke="#9fd3ee", w=6),
        C(268, 396, 6, "#9fd3ee"), C(490, 400, 7, "#9fd3ee"), C(352, 384, 5, "#9fd3ee"),
    )
    return wrap(ground(), splash, rain, cloud)


def art_雪():
    """浅蓝天底 + 六瓣雪花（六向手臂带分叉）+ 底下小雪堆。"""
    cx, cy, arm = 380, 232, 102
    flake = ""
    for i in range(6):
        a = math.radians(i * 60)
        dx, dy = math.cos(a), math.sin(a)
        flake += L(cx, cy, cx + arm * dx, cy + arm * dy, WHITE, 12)
        for t in (0.42, 0.68):
            bx, by = cx + arm * t * dx, cy + arm * t * dy
            bl = 24 if t > 0.5 else 19
            for s in (-1, 1):
                ba = a + s * math.radians(42)
                flake += L(bx, by, bx + bl * math.cos(ba), by + bl * math.sin(ba), WHITE, 8)
    flake += C(cx, cy, 15, WHITE)
    return wrap(
        ground(fill="#e8f3fa"),
        R(70, 48, 620, 372, 36, SKY_L2),
        C(250, 130, 7, WHITE), C(540, 170, 6, WHITE), C(470, 110, 5, WHITE), C(210, 200, 5, WHITE),
        flake,
        E(282, 420, 132, 34, WHITE),
        E(474, 426, 146, 32, "#f2f8fd"),
        E(474, 420, 138, 28, WHITE),
    )


BOW = ["#f2a3a0", "#f6bd7d", "#f8dc8e", "#a9d190", "#8fd0c2", "#93b5e0", "#c5a8de"]


def art_虹():
    """雨后拱形七色带（柔和粉彩），一端藏进小云里。"""
    bands = ""
    for i, col in enumerate(BOW):
        r = 272 - i * 18
        bands += P(f"M {380 - r} 428 A {r} {r} 0 0 1 {380 + r} 428", stroke=col, w=18)
    return wrap(ground(), bands, cloud_p(140, 404, 1.05, "#e8f1f8"))


def art_冰():
    """淡蓝冰块立方（顶面/侧面分色 + 高光）+ 底边垂下三根冰凌。"""
    return wrap(
        ground(fill="#e8f3fa"),
        E(380, 428, 185, 38, "#dceef9"),
        PG([(467, 212), (514, 166), (514, 322), (467, 368)], "#a9d3ec"),
        PG([(295, 212), (342, 166), (514, 166), (467, 212)], "#e3f3fd"),
        R(295, 212, 172, 156, 14, "#c6e6f8"),
        P("M 330 244 L 310 330", stroke=WHITE, w=11),
        P("M 366 244 L 352 302", stroke=WHITE, w=8),
        PG([(318, 198), (338, 179), (362, 179), (342, 198)], WHITE),
        PG([(310, 364), (348, 364), (325, 446)], "#bfe3f5"),
        PG([(362, 364), (404, 364), (378, 468)], "#bfe3f5"),
        PG([(418, 364), (452, 364), (438, 428)], "#bfe3f5"),
        L(322, 374, 318, 414, WHITE, 4),
        L(374, 374, 371, 432, WHITE, 4),
    )


def arts():
    return {"月": art_月(), "星": art_星(), "云": art_云(), "电": art_电(),
            "风": art_风(), "雨": art_雨(), "雪": art_雪(), "虹": art_虹(), "冰": art_冰()}


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import 识字卡片_字库 as ZIKU

    GID, SEEDS = "tianwen", {"日"}
    expect = []
    for g in ZIKU.GROUPS:
        if g["id"] == GID:
            for item in g["chars"]:
                k = item["char"] if isinstance(item, dict) else item
                if k not in SEEDS:
                    expect.append(k)
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"天文组：卡数 {len(GROUP_CARDS)}（字数 {len(got)}，种子字 {sorted(SEEDS)} 已跳过）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad, "自检未通过"
    print("自检通过 ✓")


# ---- 2026-10-26 重分类迁移 ----
GROUP_CARDS += [
    {'char': '闪', 'pinyin': 'shǎn', 'tone': '第三声', 'sentence': '星星一闪一闪。', 'say': '星星亮一下暗一下，就是闪。', 'chat': '“夜空里什么会一闪一闪呀？”', 'life': '晚上找找一闪一闪的小灯。'},
]
_arts_mig = {
    '闪': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="70" y="48" width="620" height="372" rx="36" fill="#3d5a86"/><polygon points="386.0,148.0 411.39232289903487,209.05046584300226 477.30142556433475,214.33436854000504 427.0856415039506,257.3495341569977 442.42738422007744,321.665631459995 386.0,287.2 329.57261577992256,321.665631459995 344.9143584960494,257.3495341569977 294.69857443566525,214.33436854000507 360.60767710096513,209.05046584300226" fill="#d99a2b"/><polygon points="380.0,146.0 403.80530271784517,203.23481172781464 465.5950864665638,208.18847050625473 418.5177889099537,248.51518827218536 432.90067270632255,308.8115294937453 380.0,276.5 327.09932729367745,308.8115294937453 341.4822110900463,248.51518827218538 294.4049135334362,208.18847050625476 356.19469728215483,203.23481172781464" fill="#f7ae35"/><line x1="262" y1="126" x2="232" y2="100" stroke="#fdfdfa" stroke-width="8" stroke-linecap="round"/><line x1="498" y1="126" x2="528" y2="100" stroke="#fdfdfa" stroke-width="8" stroke-linecap="round"/><line x1="506" y1="306" x2="546" y2="318" stroke="#fdfdfa" stroke-width="7" stroke-linecap="round"/><polygon points="180.0,118.0 183.70304708944258,126.90319293543783 193.31479122813215,127.67376207875074 185.99165605265947,133.94680706456217 188.22899353209462,143.32623792124926 180.0,138.3 171.77100646790538,143.32623792124926 174.00834394734053,133.94680706456217 166.68520877186785,127.67376207875074 176.29695291055742,126.90319293543783" fill="#f9c95e"/><polygon points="586.0,321.0 588.9095369988478,327.995365877844 596.4616216792467,328.60081306187556 590.707729755661,333.529634122156 592.4656377752173,340.89918693812444 586.0,336.95 579.5343622247829,340.89918693812444 581.292270244339,333.529634122156 575.5383783207533,328.60081306187556 583.0904630011522,327.995365877844" fill="#f9c95e"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
