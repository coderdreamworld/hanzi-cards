#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画——会意字组（10 字）：明尘从众双林森条休尖。

部件就是规律本身，严格按字库 note 设计：
明=日+月并排；尘=小土堆+小手扇起灰尘；从=两个小人一前一后；
众=三个小人品字形；双=两只并排的手；林=两棵一样的树；
森=三棵树（下二上一）；条=树枝垂叶成一条；休=小人靠树闭眼；
尖=削尖的铅笔立在大三角上（上小下大）。
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


lib = _load("scys_lib_huiyi", os.path.join(_HERE, "识字卡片_素材库.py"))


# ---------- 小组件 ----------
def sun_face(cx, cy, r):
    """带笑脸、八向光芒的太阳（明卡的「日」部件）。"""
    g = ""
    for i in range(8):
        a = math.radians(i * 45)
        x1, y1 = cx + (r + 15) * math.cos(a), cy + (r + 15) * math.sin(a)
        x2, y2 = cx + (r + 42) * math.cos(a), cy + (r + 42) * math.sin(a)
        g += lib.L(x1, y1, x2, y2, lib.YEL_D, 8)
    g += lib.C(cx + r * 0.05, cy + r * 0.06, r, "#e2952a")
    g += lib.C(cx - r * 0.04, cy - r * 0.04, r * 0.94, lib.SUN)
    g += lib.C(cx - r * 0.3, cy - r * 0.3, r * 0.18, lib.SUN_L, 0.9)
    g += lib.C(cx - 24, cy - 10, 7, lib.INK)
    g += lib.C(cx + 24, cy - 10, 7, lib.INK)
    g += lib.P(f"M {cx-24} {cy+14} Q {cx} {cy+32} {cx+24} {cy+14}", stroke=lib.INK, w=6)
    return g


def crescent(cx, cy, r, fill=lib.YEL):
    """弯月：鼓包朝左、月口朝右（明卡/晚卡的「月」部件画法）。"""
    d = (f"M {cx} {cy - r} "
         f"C {cx - r * 1.18} {cy - r * 0.52} {cx - r * 1.18} {cy + r * 0.52} {cx} {cy + r} "
         f"C {cx - r * 0.42} {cy + r * 0.48} {cx - r * 0.42} {cy - r * 0.48} {cx} {cy - r} Z")
    return lib.P(d, fill)


def closed_eyes(x, y, s, skin=lib.SKIN):
    """盖住 kid() 默认的睁眼并画闭眼弧线（须与 kid 同一旋转组内使用）。"""
    ey = y - 246 * s
    g = lib.E(x - 22 * s, ey, 12.5 * s, 15.5 * s, skin)
    g += lib.E(x + 22 * s, ey, 12.5 * s, 15.5 * s, skin)
    g += lib.P(f"M {x - 30 * s} {ey} Q {x - 22 * s} {ey + 8 * s} {x - 14 * s} {ey}",
               stroke=lib.INK, w=6 * s)
    g += lib.P(f"M {x + 14 * s} {ey} Q {x + 22 * s} {ey + 8 * s} {x + 30 * s} {ey}",
               stroke=lib.INK, w=6 * s)
    return g


def hanging_leaf(cx, top, ln, w, fill):
    """从枝头垂下的细长叶子。"""
    d = (f"M {cx} {top} "
         f"C {cx - w} {top + ln * 0.35} {cx - w} {top + ln * 0.72} {cx} {top + ln} "
         f"C {cx + w} {top + ln * 0.72} {cx + w} {top + ln * 0.35} {cx} {top} Z")
    return lib.P(d, fill)


# ---------- 各卡场景 ----------
def card_ming():
    # 日 + 月 并排挂天空，拼成明
    g = lib.ground()
    g += sun_face(282, 248, 76)
    g += crescent(502, 248, 100)
    g += lib.P("M 468 266 Q 486 282 504 266", stroke=lib.INK, w=6)
    return g


def card_chen():
    # 尘：扫把扫过，灰尘飞扬起来（小小的土粒=尘）
    g = lib.ground()
    g += lib.E(320, 436, 150, 16, "#d9d0c2")                      # 地上的一摊灰尘
    # 扫把（柄朝右上，帚毛贴地扫向左）
    g += lib.L(452, 166, 316, 372, "#a9743f", 20)                 # 长柄
    g += lib.R(438, 152, 36, 24, 10, "#8a5a33")                   # 柄端
    g += lib.P("M 316 372 L 452 166", stroke="#c9a55c", w=8)      # 柄高光
    for bx, by in ((318, 382), (296, 396), (276, 406), (258, 412)):
        g += lib.L(322, 372, bx, by, "#d9b98a", 10)               # 帚毛扇形
    g += lib.R(306, 360, 44, 18, 8, "#b98a4a")                    # 帚扎带
    # 灰尘飞扬（小点点从帚头扬起）
    for dx, dy, dr in ((300, 336, 8), (272, 310, 6), (246, 286, 7), (224, 260, 5), (208, 236, 4)):
        g += lib.C(dx, dy, dr, "#b0a898")
    for dx, dy, dr in ((286, 344, 4), (260, 318, 4), (236, 296, 4), (214, 272, 3)):
        g += lib.C(dx, dy, dr, "#c9c2b8")
    return g


def card_cong():
    # 两个一样的小人一前一后走
    g = lib.ground()
    g += lib.kid(300, 424, s=0.78, pose="walk", face="smile")  # 后面那个
    g += lib.kid(468, 456, s=0.78, pose="walk", face="smile")  # 前面那个
    return g


def card_zhong_char():
    # 三个小人品字形站开：后面一个居中，前面两个并排
    g = lib.ground()
    # 后排孩子站得更远：脚下补一小块地面 + 接触阴影，避免悬空漂浮
    g += lib.E(380, 377, 90, 15, "#b9dcc9")
    g += lib.E(380, 379, 58, 8, lib.INK, 0.10)
    g += lib.kid(380, 376, s=0.58, face="smile")
    g += lib.kid(282, 448, s=0.66, face="smile")
    g += lib.kid(478, 448, s=0.66, face="smile")
    return g


def card_shuang():
    """双：一双红色小运动鞋摆成一对（鞋头朝外，鞋口鞋带清晰，与「脚」卡同款鞋）。"""
    def shoe():
        # 鞋头朝右的红色小运动鞋：深色鞋口、白色鞋带、白鞋底（鞋口方向清晰）
        return lib.wrap(
            lib.P("M 0 0 L 0 -30 Q 3 -60 38 -63 Q 74 -66 94 -36 Q 101 -25 103 -8 L 104 0 Z", lib.RED),
            lib.R(-8, 0, 122, 24, 12, "#fdfdfa"),
            lib.E(16, -46, 17, 11, lib.RED_D),
            lib.L(30, -38, 70, -32, "#fdfdfa", 7),
            lib.L(34, -26, 74, -20, "#fdfdfa", 7))
    g = lib.ground(380, 448, 235, 22)
    g += lib.E(233, 432, 88, 9, lib.INK, 0.08)
    g += lib.E(527, 432, 88, 9, lib.INK, 0.08)
    g += f'<g transform="translate(302,398) scale(-1.3,1.3)">{shoe()}</g>'
    g += f'<g transform="translate(458,398) scale(1.3)">{shoe()}</g>'
    return g


def card_lin():
    # 两棵一样的树并排
    g = lib.ground()
    g += lib.tree_round(275, 450, s=0.85)
    g += lib.tree_round(485, 450, s=0.85)
    return g


def card_sen():
    # 三棵树：下面两棵并排，上面一棵居中靠后
    g = lib.ground()
    g += lib.tree_round(380, 386, s=0.62)
    g += lib.tree_round(272, 452, s=0.7)
    g += lib.tree_round(488, 452, s=0.7)
    return g


def card_tiao():
    """条：晾衣绳上挂着一条条——柳条、面条、彩带、毛线，都是一条。"""
    g = lib.ground(380, 462, 240, 20)
    # 晾衣绳（微微下垂）
    g += lib.P("M 70 172 Q 380 232 690 172", stroke="#a9743f", w=9)
    # 1 柳条（绿叶长条，随风微弯）
    g += lib.C(160, 196, 6, "#8a5a33")
    g += lib.P("M 160 202 Q 146 268 164 340 Q 170 366 158 392", stroke=lib.GREEN, w=13)
    g += lib.E(154, 396, 10, 17, lib.GREEN, 0.9)
    # 2 面条（奶油色，弯弯垂下）
    g += lib.C(288, 194, 6, "#8a5a33")
    g += lib.P("M 288 200 Q 276 268 296 330 Q 302 358 290 396", stroke="#f5deb3", w=12)
    # 3 彩带（红色，带燕尾缺口）
    g += lib.C(414, 192, 6, "#8a5a33")
    g += lib.P("M 414 198 Q 400 264 420 336 Q 426 362 416 384", stroke=lib.RED, w=15)
    g += lib.PG([(416, 384), (404, 408), (416, 398), (428, 408)], lib.RED)
    # 4 毛线（黄色，末端一个小线球）
    g += lib.C(542, 194, 6, "#8a5a33")
    g += lib.P("M 542 200 Q 530 266 548 332 Q 554 360 544 388", stroke="#f2c14e", w=12)
    g += lib.C(546, 394, 15, "#e8a13c")
    return g


def card_xiu():
    # 累了坐在大树下歇一歇：树冠高高在上，小人坐地上靠着树干闭眼休息
    g = lib.ground()
    g += f'<g opacity="0.1">{lib.E(486, 444, 215, 13, lib.INK)}</g>'  # 树荫
    trunk = (lib.PG([(497, 452), (559, 452), (549, 196), (507, 196)], lib.WOOD_D)
             + lib.PG([(479, 452), (509, 452), (503, 426)], lib.WOOD_D)
             + lib.PG([(547, 452), (577, 452), (553, 426)], lib.WOOD_D))
    crown = (lib.C(520, 148, 104, lib.GREEN)
             + lib.C(392, 176, 66, lib.GREEN)
             + lib.C(648, 172, 68, lib.GREEN)
             + lib.C(566, 100, 56, lib.GREEN_L, 0.9))
    g += trunk + crown
    body = lib.kid(422, 452, s=0.75, pose="sit", face="smile", shirt=lib.TEAL)
    # 补一条水平大腿（向前伸），让 kid 的竖直小腿读成坐姿而不是站姿
    s = 0.75
    thigh = lib.R(422 - 86 * s, 452 - 90 * s, 116 * s, 24 * s, 12 * s, lib.BLUE_D)
    g += f'<g transform="rotate(10 422 452)">{body}{thigh}{closed_eyes(422, 452, 0.75)}</g>'
    return g


def card_jian():
    # 上小下大：削尖的铅笔立在大三角形上
    g = lib.ground()
    g += lib.PG([(230, 436), (530, 436), (380, 306)], lib.TEAL_L)
    g += lib.R(230, 424, 300, 16, 8, lib.TEAL_D)
    g += lib.R(368, 186, 24, 96, 4, lib.YEL)            # 笔杆
    g += lib.R(368, 282, 24, 10, 2, "#c9cdd1")          # 金属箍
    g += lib.R(370, 292, 20, 16, 7, lib.PINK)           # 橡皮（底端）
    g += lib.PG([(368, 188), (392, 188), (380, 130)], lib.WOOD_L)  # 笔尖木削（上端削尖）
    g += lib.PG([(376, 148), (384, 148), (380, 130)], lib.INK)     # 铅芯
    return g


# 组卡片文案数据（不含种子字）
GROUP_CARDS = [
    {"char": "明", "pinyin": "míng", "tone": "第二声",
     "sentence": "明天我们一起去公园。",
     "say": "太阳和月亮并排挂天上，加起来就是明。",
     "chat": "什么东西亮亮的，能照亮屋子？",
     "life": "明天早起，和太阳公公问个早。"},
    {"char": "尘", "pinyin": "chén", "tone": "第二声",
     "sentence": "扫把扫过，灰尘飞起来。",
     "say": "扫把扫过，小小的土粒飞起来，就是灰尘的尘。",
     "chat": "“扫把扫过的地方，灰尘去哪儿了？”",
     "life": "帮爸爸妈妈扫扫地，看看扬起的灰尘。"},
    {"char": "从", "pinyin": "cóng", "tone": "第二声",
     "sentence": "他从家走到学校。",
     "say": "一个跟着一个走，就是跟从的从。",
     "chat": "玩开火车时你跟在谁后面？",
     "life": "排队时你跟着前面小朋友走一走。"},
    {"char": "众", "pinyin": "zhòng", "tone": "第四声",
     "sentence": "观众都为小猫鼓掌。",
     "say": "三个人排成品字，人多就是众。",
     "chat": "好多人在一起，可以叫什么？",
     "life": "数数游乐场里有几个小朋友。"},
    {"char": "双", "pinyin": "shuāng", "tone": "第一声",
     "sentence": "一双小鞋子，真好看。",
     "say": "两只鞋合在一起，就是一双。",
     "chat": "“哪只是左脚，哪只是右脚？”",
     "life": "把自己的鞋子摆成一双。"},
    {"char": "林", "pinyin": "lín", "tone": "第二声",
     "sentence": "树林里真凉快。",
     "say": "两棵树肩并肩站着，就是树林的林。",
     "chat": "小区里哪里能看到好多树？",
     "life": "去公园找两棵并排的大树。"},
    {"char": "森", "pinyin": "sēn", "tone": "第一声",
     "sentence": "森林里住着大熊。",
     "say": "树更多更大，就变成森林的森。",
     "chat": "森林里可能住着哪些动物？",
     "life": "用积木搭三棵树，变成小森林。"},
    {"char": "条", "pinyin": "tiáo", "tone": "第二声",
     "sentence": "柳条、面条，一条条。",
     "say": "长长的挂着的，一条一条，都叫条。",
     "chat": "“你还见过哪些东西是一条一条的？”",
     "life": "用积木摆一条长长的小路。"},
    {"char": "休", "pinyin": "xiū", "tone": "第一声",
     "sentence": "累了坐在树下休息。",
     "say": "小人靠着大树闭眼歇一歇，就是休。",
     "chat": "你跑累了喜欢在哪里休息？",
     "life": "靠着大树或沙发歇一小会儿。"},
    {"char": "尖", "pinyin": "jiān", "tone": "第一声",
     "sentence": "铅笔削得尖尖的。",
     "say": "上头小小的，底下大大的，就是尖。",
     "chat": "家里还有什么东西尖尖的？",
     "life": "用手指搭个尖尖的小塔顶。"},
]


def arts():
    return {
        "明": card_ming(),
        "尘": card_chen(),
        "从": card_cong(),
        "众": card_zhong_char(),
        "双": card_shuang(),
        "林": card_lin(),
        "森": card_sen(),
        "条": card_tiao(),
        "休": card_xiu(),
        "尖": card_jian(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    ziku = _load("scys_ziku_huiyi", os.path.join(_HERE, "识字卡片_字库.py"))
    grp = next(g for g in ziku.GROUPS if g["id"] == "huiyi")
    expect = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    mine = [c["char"] for c in GROUP_CARDS]
    assert mine == expect, f"卡序与字库不一致：{mine} vs {expect}"

    cards = arts()
    assert set(cards) == set(mine), "arts 键与 GROUP_CARDS 不一致"
    punct = "，。！？、；：·—…"
    for c in GROUP_CARDS:
        ch = c["char"]
        core = [t for t in c["sentence"] if t not in punct]
        assert 4 <= len(core) <= 10, f"{ch} sentence 长度 {len(core)}"
        assert ch in c["sentence"], f"{ch} sentence 未含目标字"
        for k in ("say", "chat", "life"):
            assert len(c[k]) <= 30, f"{ch} {k} 超长：{len(c[k])}"
        v = cards[ch]
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            assert bad not in v, f"{ch} 含禁止标记 {bad}"
    print(f"会意字组：卡数 {len(GROUP_CARDS)}，arts {len(cards)}，与字库比对一致 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '力', 'pinyin': 'lì', 'tone': '第四声', 'sentence': '大象用鼻子举起大木头。', 'say': '长鼻子一使劲，大木头举起来，这就是力。', 'chat': '搬什么东西最费力呀？', 'life': '搬小椅子，比比谁力气大。'},
    {'char': '办', 'pinyin': 'bàn', 'tone': '第四声', 'sentence': '我想出好办法。', 'say': '头顶灯泡一亮：好办法想出来了！', 'chat': '东西够不着，你有什么好办法？', 'life': '拿不到杯子？搬个小凳子来想办法。'},
    {'char': '同', 'pinyin': 'tóng', 'tone': '第二声', 'sentence': '三个球完全相同。', 'say': '三个球一样大一样色，就是同。', 'chat': '“找找家里哪两样东西相同？”', 'life': '配袜子：挑出相同的两只。'},
    {'char': '对', 'pinyin': 'duì', 'tone': '第四声', 'sentence': '两块拼图对上了。', 'say': '两块拼图正好拼在一起，就是对上了。', 'chat': '“拼图的两块怎样才算对上呀？”', 'life': '玩拼图，拼对一块就喊：对啦！'},
    {'char': '无', 'pinyin': 'wú', 'tone': '第二声', 'sentence': '盒子里无玩具。', 'say': '盒盖大开，里面空空的，什么也无。', 'chat': '“盒子里无糖果了，怎么办呀？”', 'life': '吃完饼干说：盒里无饼干啦。'},
    {'char': '步', 'pinyin': 'bù', 'tone': '第四声', 'sentence': '一步一步向前走。', 'say': '脚印一双又一双，一步一步向前走。', 'chat': '“从房间到客厅，你走了几步？”', 'life': '牵着他一步一步上楼梯。'},
    {'char': '法', 'pinyin': 'fǎ', 'tone': '第三声', 'sentence': '这个法子真好。', 'say': '虚线小路从起点通到终点，这就是法子。', 'chat': '瓶盖拧不开，有什么法子？', 'life': '换个法子试试：两只手一起拧。'},
]
_arts_mig = {
    '力': lib.ground()+ '<rect x="238" y="376" width="44" height="70" rx="17" fill="#9db8c9"/><rect x="302" y="384" width="44" height="62" rx="17" fill="#9db8c9"/><rect x="366" y="384" width="44" height="62" rx="17" fill="#9db8c9"/><rect x="430" y="376" width="44" height="70" rx="17" fill="#9db8c9"/><ellipse cx="356" cy="330" rx="142" ry="92" fill="#9db8c9"/><path d="M 218 316 Q 190 336 202 368" stroke="#9db8c9" stroke-width="14" fill="none" stroke-linecap="round"/><ellipse cx="466" cy="288" rx="44" ry="56" fill="#84a2b5"/><circle cx="512" cy="298" r="64" fill="#9db8c9"/><circle cx="534" cy="284" r="11" fill="#fdfdfa"/><circle cx="537" cy="286" r="5.5" fill="#4a3226"/><circle cx="522" cy="318" r="10" fill="#f5a58c" opacity="0.7"/><path d="M 520 330 Q 532 340 544 328" stroke="#4a3226" stroke-width="6" fill="none" stroke-linecap="round"/><g transform="rotate(-6 540 176)"><rect x="460" y="158" width="160" height="34" rx="16" fill="#c98a4b"/><line x1="488" y1="166" x2="488" y2="184" stroke="#a9713a" stroke-width="6" stroke-linecap="round"/><line x1="520" y1="166" x2="520" y2="184" stroke="#a9713a" stroke-width="6" stroke-linecap="round"/><line x1="552" y1="166" x2="552" y2="184" stroke="#a9713a" stroke-width="6" stroke-linecap="round"/><line x1="584" y1="166" x2="584" y2="184" stroke="#a9713a" stroke-width="6" stroke-linecap="round"/></g><path d="M 550 330 Q 592 262 566 206" stroke="#9db8c9" stroke-width="27" fill="none" stroke-linecap="round"/><circle cx="563" cy="198" r="15" fill="#9db8c9"/><path d="M 636 148 Q 646 136 662 132" stroke="#f2b53c" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M 628 174 Q 642 164 658 160" stroke="#f2b53c" stroke-width="7" fill="none" stroke-linecap="round"/>',
    '办': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><line x1="459.9570600599758" y1="49.5" x2="446.10065359942473" y2="41.5" stroke="#d99a2b" stroke-width="7" stroke-linecap="round"/><line x1="476.3631243155941" y1="34.46661187964395" x2="469.60123212774295" y2="19.96568728705755" stroke="#d99a2b" stroke-width="7" stroke-linecap="round"/><line x1="492.0" y1="31.0" x2="492.0" y2="15.0" stroke="#d99a2b" stroke-width="7" stroke-linecap="round"/><line x1="507.6368756844059" y1="34.46661187964395" x2="514.398767872257" y2="19.965687287057555" stroke="#d99a2b" stroke-width="7" stroke-linecap="round"/><line x1="524.0429399400242" y1="49.5" x2="537.8993464005753" y2="41.5" stroke="#d99a2b" stroke-width="7" stroke-linecap="round"/><circle cx="492" cy="68" r="30" fill="#f7ae35"/><circle cx="483.0" cy="59.0" r="9.0" fill="#f9c95e" opacity="0.9"/><rect x="475.5" y="92.0" width="33.0" height="15.0" rx="6" fill="#c3c9d1"/><rect x="475.5" y="97.4" width="33.0" height="4.2" rx="4" fill="#aab1ba"/><rect x="333.0" y="340.6" width="23.400000000000002" height="75.60000000000001" rx="10.8" fill="#4a97c9"/><rect x="363.6" y="340.6" width="23.400000000000002" height="75.60000000000001" rx="10.8" fill="#4a97c9"/><ellipse cx="344.7" cy="430.6" rx="18.900000000000002" ry="9.0" fill="#4a3226" opacity="0.85"/><ellipse cx="375.3" cy="430.6" rx="18.900000000000002" ry="9.0" fill="#4a3226" opacity="0.85"/><path d="M 309.6 284.79999999999995 Q 307.8 355.0 324.0 356.8 L 396.0 356.8 Q 412.2 355.0 410.4 284.79999999999995 Q 360 270.4 309.6 284.79999999999995 Z" fill="#5fa8d8"/><g transform="rotate(-68 399.6 290.19999999999993)"><line x1="399.6" y1="290.19999999999993" x2="477.0" y2="290.19999999999993" stroke="#f8cba4" stroke-width="27.0" stroke-linecap="round"/><circle cx="478.8" cy="290.19999999999993" r="11.700000000000001" fill="#f8cba4"/></g><line x1="320.4" y1="290.19999999999993" x2="300.6" y2="353.19999999999993" stroke="#f8cba4" stroke-width="27.0" stroke-linecap="round"/><circle cx="300.6" cy="353.19999999999993" r="11.700000000000001" fill="#f8cba4"/><circle cx="307.8" cy="230.79999999999995" r="9.9" fill="#f8cba4"/><circle cx="412.2" cy="230.79999999999995" r="9.9" fill="#f8cba4"/><circle cx="360" cy="221.79999999999995" r="55.800000000000004" fill="#f8cba4"/><path d="M 305.316 202.26999999999995 Q 309.78 155.95599999999993 360 159.30399999999995 Q 410.22 155.95599999999993 414.684 202.26999999999995 Q 390.69 192.78399999999993 360 198.36399999999995 Q 329.31 192.78399999999993 305.316 202.26999999999995 Z" fill="#5a3d2b"/><ellipse cx="340.2" cy="214.59999999999997" rx="9.0" ry="11.700000000000001" fill="#4a3226"/><circle cx="342.0" cy="209.19999999999996" r="3.06" fill="#fdfdfa"/><ellipse cx="379.8" cy="214.59999999999997" rx="9.0" ry="11.700000000000001" fill="#4a3226"/><circle cx="381.6" cy="209.19999999999996" r="3.06" fill="#fdfdfa"/><path d="M 327.6 192.78399999999996 Q 340.2 187.20399999999995 352.8 191.66799999999995" fill="none" stroke="#5a3d2b" stroke-width="5.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M 367.2 191.66799999999995 Q 379.8 187.20399999999995 392.4 192.78399999999996" fill="none" stroke="#5a3d2b" stroke-width="5.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M 336.6 245.19999999999996 Q 360 236.19999999999996 383.4 245.19999999999996 Q 381.6 268.59999999999997 360 272.19999999999993 Q 338.4 268.59999999999997 336.6 245.19999999999996 Z" fill="#6b3325"/><path d="M 347.4 259.59999999999997 Q 360 252.39999999999995 372.6 259.59999999999997 Q 368.1 269.49999999999994 360 270.4 Q 351.9 269.49999999999994 347.4 259.59999999999997 Z" fill="#f0876f"/><circle cx="320.4" cy="234.39999999999995" r="9.9" fill="#f5a58c" opacity="0.8"/><circle cx="399.6" cy="234.39999999999995" r="9.9" fill="#f5a58c" opacity="0.8"/>',
    '同': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><circle cx="208.9" cy="368.64" r="58" fill="#d4552f"/><circle cx="204.26" cy="361.1" r="55.39" fill="#e8663c"/><circle cx="186.28" cy="345.44" r="13.92" fill="#f5a58c" opacity="0.9"/><circle cx="382.9" cy="368.64" r="58" fill="#d4552f"/><circle cx="378.26" cy="361.1" r="55.39" fill="#e8663c"/><circle cx="360.28" cy="345.44" r="13.92" fill="#f5a58c" opacity="0.9"/><circle cx="556.9" cy="368.64" r="58" fill="#d4552f"/><circle cx="552.26" cy="361.1" r="55.39" fill="#e8663c"/><circle cx="534.28" cy="345.44" r="13.92" fill="#f5a58c" opacity="0.9"/>',
    '对': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="150" y="208" width="214" height="220" rx="30" fill="#4fae9f"/><rect x="150" y="404" width="214" height="24" rx="12" fill="#3e9486"/><rect x="396" y="208" width="214" height="220" rx="30" fill="#f2b53c"/><rect x="396" y="404" width="214" height="24" rx="12" fill="#d99a2b"/><circle cx="210" cy="268" r="16" fill="#fdfdfa" opacity="0.4"/><circle cx="456" cy="268" r="16" fill="#fdfdfa" opacity="0.4"/><circle cx="380" cy="318" r="36" fill="#3e9486"/><circle cx="380" cy="318" r="26" fill="#4fae9f"/><line x1="380" y1="250" x2="380" y2="266" stroke="#3e9486" stroke-width="7" stroke-linecap="round"/><line x1="380" y1="370" x2="380" y2="386" stroke="#3e9486" stroke-width="7" stroke-linecap="round"/><path d="M 354.5 123.7 L 374.9 142.4 L 407.2 103.3" fill="none" stroke="#7fae70" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>',
    '无': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><g transform="translate(380,452) scale(1.45) translate(-380,-452)"><ellipse cx="380" cy="452" rx="190" ry="12" fill="#4a3226" opacity="0.08"/><rect x="272" y="302" width="216" height="56" rx="12" fill="#8a5a33"/><ellipse cx="380" cy="332" rx="96" ry="9" fill="#6f4526" opacity="0.6"/><g transform="rotate(-24 260 339)"><rect x="154" y="326" width="108" height="26" rx="9" fill="#e9b97e"/><rect x="154" y="344" width="108" height="8" rx="4" fill="#c89058"/></g><g transform="rotate(24 500 339)"><rect x="498" y="326" width="108" height="26" rx="9" fill="#e9b97e"/><rect x="498" y="344" width="108" height="8" rx="4" fill="#c89058"/></g><rect x="260" y="338" width="240" height="112" rx="16" fill="#c89058"/><rect x="282" y="360" width="196" height="68" rx="12" fill="#e9b97e"/></g>',
    '步': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><ellipse cx="122" cy="428" rx="26" ry="9" fill="#9cc98a"/><ellipse cx="96" cy="452" rx="20" ry="8" fill="#9cc98a"/><ellipse cx="620" cy="342" rx="22" ry="8" fill="#9cc98a"/><ellipse cx="648" cy="368" rx="18" ry="7" fill="#9cc98a"/><path d="M 172 438 L 545 285" fill="none" stroke="#f2dfa8" stroke-width="84" stroke-linecap="round" stroke-linejoin="round"/><g transform="rotate(55 273 440)"><ellipse cx="272.8" cy="431.6" rx="14" ry="20" fill="#a08256"/><ellipse cx="272.8" cy="455.6" rx="9" ry="7" fill="#a08256"/></g><g transform="rotate(79 310 383)"><ellipse cx="310.2" cy="375.4" rx="14" ry="20" fill="#a08256"/><ellipse cx="310.2" cy="399.4" rx="9" ry="7" fill="#a08256"/></g><g transform="rotate(55 375 389)"><ellipse cx="374.8" cy="380.6" rx="14" ry="20" fill="#a08256"/><ellipse cx="374.8" cy="404.6" rx="9" ry="7" fill="#a08256"/></g><g transform="rotate(79 412 332)"><ellipse cx="412.2" cy="324.4" rx="14" ry="20" fill="#a08256"/><ellipse cx="412.2" cy="348.4" rx="9" ry="7" fill="#a08256"/></g><g transform="rotate(55 477 338)"><ellipse cx="476.8" cy="329.6" rx="14" ry="20" fill="#a08256"/><ellipse cx="476.8" cy="353.6" rx="9" ry="7" fill="#a08256"/></g><g transform="rotate(4 545 242.48000000000002)"><rect x="523.92" y="235.04000000000002" width="16.12" height="52.08" rx="7.4399999999999995" fill="#4a97c9"/><rect x="549.96" y="235.04000000000002" width="16.12" height="48.36" rx="7.4399999999999995" fill="#4a97c9"/></g><ellipse cx="528.88" cy="298.28" rx="13.02" ry="6.2" fill="#4a3226" opacity="0.85"/><ellipse cx="559.88" cy="295.8" rx="13.02" ry="6.2" fill="#4a3226" opacity="0.85"/><path d="M 510.28 197.84 Q 509.04 246.20000000000002 520.2 247.44000000000003 L 569.8 247.44000000000003 Q 580.96 246.20000000000002 579.72 197.84 Q 545 187.92000000000002 510.28 197.84 Z" fill="#e8663c"/><line x1="517.72" y1="201.56" x2="500.36" y2="243.72" stroke="#f8cba4" stroke-width="18.6" stroke-linecap="round"/><circle cx="500.36" cy="243.72" r="8.06" fill="#f8cba4"/><line x1="572.28" y1="201.56" x2="594.6" y2="232.56" stroke="#f8cba4" stroke-width="18.6" stroke-linecap="round"/><circle cx="594.6" cy="232.56" r="8.06" fill="#f8cba4"/><circle cx="509.04" cy="160.64" r="6.82" fill="#f8cba4"/><circle cx="580.96" cy="160.64" r="6.82" fill="#f8cba4"/><circle cx="545" cy="154.44" r="38.44" fill="#f8cba4"/><path d="M 507.3288 140.986 Q 510.404 109.0808 545 111.3872 Q 579.596 109.0808 582.6712 140.986 Q 566.142 134.4512 545 138.2952 Q 523.858 134.4512 507.3288 140.986 Z" fill="#5a3d2b"/><ellipse cx="531.36" cy="149.48" rx="6.2" ry="8.06" fill="#4a3226"/><circle cx="532.6" cy="146.38" r="2.108" fill="#fdfdfa"/><ellipse cx="558.64" cy="149.48" rx="6.2" ry="8.06" fill="#4a3226"/><circle cx="559.88" cy="146.38" r="2.108" fill="#fdfdfa"/><path d="M 522.68 134.4512 Q 531.36 130.6072 540.04 133.6824" fill="none" stroke="#5a3d2b" stroke-width="3.7199999999999998" stroke-linecap="round" stroke-linejoin="round"/><path d="M 549.96 133.6824 Q 558.64 130.6072 567.32 134.4512" fill="none" stroke="#5a3d2b" stroke-width="3.7199999999999998" stroke-linecap="round" stroke-linejoin="round"/><path d="M 532.6 170.56 Q 545 180.48 557.4 170.56" fill="none" stroke="#4a3226" stroke-width="4.34" stroke-linecap="round" stroke-linejoin="round"/><circle cx="517.72" cy="163.12" r="6.82" fill="#f5a58c" opacity="0.8"/><circle cx="572.28" cy="163.12" r="6.82" fill="#f5a58c" opacity="0.8"/>',
    '法': lib.ground() + lib.kid(300, 446, s=1.0, arms="point", point_at=(452, 336)) + '<path d="M 764 232 Q 590 250 424 320" stroke="#9c6b3f" stroke-width="20" fill="none" stroke-linecap="round"/><ellipse cx="640" cy="246" rx="26" ry="12" fill="#7cc8bb" transform="rotate(-16 640 246)"/><ellipse cx="700" cy="238" rx="26" ry="12" fill="#7cc8bb" transform="rotate(-12 700 238)"/><line x1="540" y1="276" x2="542" y2="264" stroke="#8a6b2f" stroke-width="6" stroke-linecap="round"/><circle cx="540" cy="300" r="30" fill="#e8663c"/><circle cx="530" cy="290" r="8" fill="#fdfdfa" opacity="0.85"/><circle cx="423" cy="322" r="14" fill="#f8cba4"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
