#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片插画——形容组（5 字）：好 新 快 美 响。

全部是「看得出的状态」：
好=竖起大拇指的大手（自画，同 lib.hand 配色）+ 两颗小金星；
新=拆开的新礼物盒，蝴蝶结完整、盒口内衬发亮 + 亮晶晶闪光（全新未旧）；
快=小朋友奔跑 + 身后三道速度线 + 脚下小风；
美=戴花环的小女孩（花冠+裙子+丸子头）+ 一朵小花 + 蝴蝶；
响=摇晃的小金铃铛 + 两侧弧形声波线。
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lib = _load("scys_lib_xingrong", os.path.join(_HERE, "识字卡片_素材库.py"))


# ---------- 本组新组件 ----------
def sparkle(cx, cy, r, fill=lib.SUN):
    """四角亮晶晶闪光（十字薄菱形）。"""
    return (lib.PG([(cx, cy - r), (cx + r * 0.26, cy), (cx, cy + r), (cx - r * 0.26, cy)], fill)
            + lib.PG([(cx - r, cy), (cx, cy - r * 0.26), (cx + r, cy), (cx, cy + r * 0.26)], fill))


def thumb_hand(cx, cy, s=1.0):
    """竖起大拇指的大手：拇指 + 握拳 + 三道折指缝 + 芥末袖口（同 lib.hand 配色）。"""
    g = ""
    # 拇指（先画，根部被拳头压住）
    g += (f'<g transform="rotate(-14 -10 -20)">'
          + lib.R(-32, -182, 46, 150, 23, lib.SKIN_D)
          + lib.R(-38, -188, 46, 150, 23, "#f7c49c") + "</g>")
    # 拳头（深一号底 + 主体）
    g += lib.R(-6, -82, 152, 148, 36, lib.SKIN_D)
    g += lib.R(-16, -92, 152, 148, 36, "#f7c49c")
    # 折指缝
    for yy in (-46, -10, 26):
        g += lib.P(f"M 0 {yy} Q 62 {yy + 9} 124 {yy}", stroke=lib.SKIN_D, w=5)
    # 袖口
    g += lib.R(-30, 56, 172, 58, 24, "#f2b03c")
    g += lib.R(-30, 56, 172, 18, 9, "#e8a13c")
    return f'<g transform="translate({cx},{cy}) scale({s})">{g}</g>'


def butterfly(cx, cy, s=1.0):
    """小蝴蝶：四片圆翅 + 身体 + 触角。"""
    g = lib.C(cx - 16 * s, cy - 10 * s, 13 * s, "#f0876f")
    g += lib.C(cx + 16 * s, cy - 10 * s, 13 * s, "#f0876f")
    g += lib.C(cx - 12 * s, cy + 8 * s, 9 * s, lib.YEL)
    g += lib.C(cx + 12 * s, cy + 8 * s, 9 * s, lib.YEL)
    g += lib.E(cx, cy, 4.5 * s, 14 * s, lib.INK)
    g += lib.L(cx - 2 * s, cy - 13 * s, cx - 8 * s, cy - 22 * s, lib.INK, 2.5 * s)
    g += lib.L(cx + 2 * s, cy - 13 * s, cx + 8 * s, cy - 22 * s, lib.INK, 2.5 * s)
    return g


def bell(cx, cy, s=1.0, rot=0):
    """小金铃铛：挂环 + 钟身 + 铃口 + 铃舌。"""
    g = f'<circle cx="0" cy="-78" r="16" fill="none" stroke="{lib.WOOD_D}" stroke-width="10"/>'
    dome = "M -67 39 L 67 39 Q 71 -9 43 -41 Q 21 -63 0 -65 Q -21 -63 -43 -41 Q -71 -9 -67 39 Z"
    g += f'<g transform="translate(4,3)">{lib.P(dome, lib.YEL_D)}</g>'
    g += lib.P(dome, lib.YEL)
    g += lib.C(-24, -20, 12, "#f9c95e", 0.9)
    g += lib.R(-78, 34, 156, 24, 12, lib.YEL_D)
    g += lib.C(0, 74, 17, lib.YEL_D)
    return f'<g transform="translate({cx},{cy}) rotate({rot}) scale({s})">{g}</g>'


# ---------- 各卡场景 ----------
def card_hao():
    # 好：小女孩和小男孩手拉手——女+子=好，好朋友一起玩
    s = 0.9
    y = 444
    sho = y - 168 * s
    girl = lib.kid(300, y, s=s, bun=True, skirt=True, shirt=lib.PINK, look=(1, 0))
    boy = lib.kid(460, y, s=s, look=(-1, 0))
    clasp = (lib.L(300 + 44 * s, sho + 6 * s, 372, 342, lib.SKIN, 26)
             + lib.L(460 - 44 * s, sho + 6 * s, 388, 342, lib.SKIN, 26)
             + lib.C(372, 344, 12.5, lib.SKIN) + lib.C(388, 344, 12.5, lib.SKIN))
    hearts = (lib.heart(380, 130, 17, lib.RED)
              + lib.heart(348, 158, 10, lib.PINK)
              + lib.heart(412, 158, 10, lib.PINK))
    return lib.wrap(lib.ground(), girl, boy, clasp, hearts)


def card_xin():
    # 新：拆开的新礼物盒（盒口内衬发亮）+ 完整蝴蝶结盒盖 + 亮晶晶
    g = lib.ground()
    g += lib.R(274, 310, 224, 126, 16, lib.RED_D)
    g += lib.R(266, 302, 224, 126, 16, lib.RED)
    g += lib.R(354, 302, 50, 126, 8, lib.YEL)          # 盒身丝带
    g += lib.E(378, 302, 112, 18, lib.SUN_L)           # 盒口内衬发亮
    g += lib.E(378, 302, 86, 12, lib.WHITE, 0.55)
    lid = (lib.R(-108, -22, 224, 52, 14, lib.RED_D)
           + lib.R(-116, -30, 224, 52, 14, lib.RED)
           + lib.R(-24, -30, 48, 52, 6, lib.YEL))
    bow = (lib.C(-30, -46, 17, lib.YEL) + lib.C(30, -46, 17, lib.YEL)
           + lib.C(0, -32, 13, lib.YEL_D)
           + lib.P("M -6 -20 Q -28 12 -16 34", stroke=lib.YEL, w=10)
           + lib.P("M 6 -20 Q 28 12 16 34", stroke=lib.YEL, w=10))
    g += f'<g transform="translate(512,236) rotate(-12)">{lid + bow}</g>'
    g += sparkle(236, 214, 18) + sparkle(600, 306, 14) + sparkle(300, 152, 11)
    g += lib.C(560, 182, 5, lib.SUN_L, 0.9) + lib.C(212, 260, 4.5, lib.SUN_L, 0.9)
    return g


def card_kuai():
    # 快：奔跑的小朋友 + 身后三道速度线 + 脚下小风
    g = lib.ground()
    g += lib.L(148, 296, 300, 296, lib.BLUE, 14)
    g += lib.L(112, 348, 292, 348, lib.TEAL_L, 14)
    g += lib.L(156, 400, 300, 400, lib.BLUE, 14)
    runner = lib.kid(452, 432, s=0.85, pose="run", arms="clap", face="smile", look=(2, -1))
    g += f'<g transform="rotate(13 452 432)">{runner}</g>'   # 前倾冲刺姿
    g += lib.P("M 386 444 Q 330 452 306 436 Q 290 424 312 416", stroke=lib.TEAL_L, w=8)
    g += lib.P("M 396 414 Q 352 420 338 406", stroke=lib.TEAL_L, w=7)
    return g


def card_mei3():
    # 美：戴花环的小女孩 + 一朵小花 + 蝴蝶
    g = lib.ground()
    g += lib.kid(380, 436, s=0.9, bun=True, skirt=True, face="smile")
    for fx, fy, pc in ((326, 191, "#f0876f"), (351, 168, lib.PINK), (380, 160, "#f0876f"),
                       (409, 168, lib.PINK), (434, 191, "#f0876f")):
        g += lib.flower5(fx, fy, 12, petal=pc)          # 花环
    g += lib.L(186, 446, 186, 402, lib.GREEN, 8)
    g += lib.flower5(186, 386, 26)
    g += butterfly(568, 244, 1.15)
    return g


def card_xiang3():
    # 响：摇晃的小铃铛 + 两侧弧形声波线
    g = lib.ground()
    g += lib.P("M 252 262 A 92 92 0 0 0 252 386", stroke=lib.TEAL, w=11)
    g += lib.P("M 192 242 A 150 150 0 0 0 192 406", stroke=lib.TEAL_L, w=11)
    g += lib.P("M 508 262 A 92 92 0 0 1 508 386", stroke=lib.TEAL, w=11)
    g += lib.P("M 568 242 A 150 150 0 0 1 568 406", stroke=lib.TEAL_L, w=11)
    g += lib.P("M 486 206 Q 504 220 502 242", stroke=lib.INK, w=7)   # 摇晃弧
    g += lib.P("M 274 206 Q 256 220 258 242", stroke=lib.INK, w=7)
    g += bell(380, 330, 1.02, rot=10)
    return g


# 组卡片文案数据（不含种子字）
GROUP_CARDS = [
    {"char": "好", "pinyin": "hǎo", "tone": "第三声",
     "sentence": "好朋友一起玩。",
     "say": "女孩和男孩手拉手，女加子就是好。",
     "chat": "“你的好朋友是谁呀？”",
     "life": "见到好朋友，拉拉手问个好。"},
    {"char": "新", "pinyin": "xīn", "tone": "第一声",
     "sentence": "打开新礼物。",
     "say": "礼物刚拆开，亮晶晶的全是新。",
     "chat": "“新鞋子和旧鞋子有啥不一样？”",
     "life": "穿新衣服时说说新在哪里。"},
    {"char": "快", "pinyin": "kuài", "tone": "第四声",
     "sentence": "小哥哥跑得真快。",
     "say": "跑得呼呼生风，就是快。",
     "chat": "“你和爸爸赛跑谁快？”",
     "life": "走一走，再快跑几步比一比。"},
    {"char": "美", "pinyin": "měi", "tone": "第三声",
     "sentence": "戴花环的女孩真美。",
     "say": "戴上花环，就是最美的小姑娘。",
     "chat": "“你觉得什么最美呀？”",
     "life": "把捡到的花瓣摆成一个花环。"},
    {"char": "响", "pinyin": "xiǎng", "tone": "第三声",
     "sentence": "铃铛响叮当。",
     "say": "铃铛摇一摇，叮叮当当真响。",
     "chat": "“家里什么声音最响？”",
     "life": "摇摇小铃铛，听听声音多大。"},
]


def arts():
    return {
        "好": card_hao(),
        "新": card_xin(),
        "快": card_kuai(),
        "美": card_mei3(),
        "响": card_xiang3(),
    }


if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    ziku = _load("scys_ziku_xingrong", os.path.join(_HERE, "识字卡片_字库.py"))
    grp = next(g for g in ziku.GROUPS if g["id"] == "xingrong")
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
    print(f"形容组：卡数 {len(GROUP_CARDS)}，arts {len(cards)}，与字库比对一致 ✓")


# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----
GROUP_CARDS += [
    {'char': '丽', 'pinyin': 'lì', 'tone': '第四声', 'sentence': '花儿真美丽。', 'say': '又美又好看，就说真美丽。', 'chat': '你觉得什么最美丽？', 'life': '把他的画贴墙上，夸真美丽。'},
    {'char': '久', 'pinyin': 'jiǔ', 'tone': '第三声', 'sentence': '老树活了很久。', 'say': '老树年纪大，树干上有一圈圈年轮。', 'chat': '这棵老树见过小时候的爸爸吗？', 'life': '翻老照片，讲很久以前的事。'},
    {'char': '全', 'pinyin': 'quán', 'tone': '第二声', 'sentence': '积木全拼好了。', 'say': '每块积木都有小勾，全部拼好了。', 'chat': '积木全拼好了吗？还差几块？', 'life': '收玩具时说：全部收回箱子啦！'},
    {'char': '最', 'pinyin': 'zuì', 'tone': '第四声', 'sentence': '站得最高的是我。', 'say': '最高领奖台上站着的，就是第一名。', 'chat': '家里谁的个子最高？', 'life': '全家比一比，说谁跑得最快。'},
    {'char': '活', 'pinyin': 'huó', 'tone': '第二声', 'sentence': '活蹦乱跳的小鱼。', 'say': '小鱼摆着尾巴游来游去，活蹦乱跳。', 'chat': '“家里谁最活泼好动呀？”', 'life': '学小鱼摆摆尾巴游一游。'},
    {'char': '真', 'pinyin': 'zhēn', 'tone': '第一声', 'sentence': '真心送给你。', 'say': '亮晶晶的红心，就是真心。', 'chat': '“真心喜欢一件事是什么样？”', 'life': '抱抱妈妈，说一句真心话。'},
    {'char': '老', 'pinyin': 'lǎo', 'tone': '第三声', 'sentence': '老爷爷拄拐杖。', 'say': '头发胡子白白的，年纪就老了。', 'chat': '“家里谁年纪最大呀？”', 'life': '见到老人主动说声爷爷好。'},
]
_arts_mig = {
    '丽': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="332.4" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="363.68" y="346.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="344.36" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="375.64" cy="438.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 308.48 289.44 Q 306.64 361.2 323.2 363.04 L 396.8 363.04 Q 413.36 361.2 411.52 289.44 Q 360 274.71999999999997 308.48 289.44 Z" fill="#f5a58c"/><path d="M 312.15999999999997 333.6 L 407.84000000000003 333.6 L 420.72 396.16 L 299.28 396.16 Z" fill="#e8663c"/><line x1="319.52" y1="294.96" x2="301.12" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="301.12" cy="361.2" r="11.96" fill="#f8cba4"/><line x1="400.48" y1="294.96" x2="418.88" y2="361.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="418.88" cy="361.2" r="11.96" fill="#f8cba4"/><circle cx="306.64" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="413.36" cy="234.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="360" cy="225.04" r="57.04" fill="#f8cba4"/><path d="M 304.1008 205.076 Q 308.664 157.7328 360 161.1552 Q 411.336 157.7328 415.8992 205.076 Q 391.372 195.3792 360 201.0832 Q 328.628 195.3792 304.1008 205.076 Z" fill="#5a3d2b"/><circle cx="360" cy="153.28" r="18.400000000000002" fill="#5a3d2b"/><ellipse cx="339.76" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="339.76" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="380.24" cy="217.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="380.24" cy="213.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 326.88 195.3792 Q 339.76 189.6752 352.64 194.23839999999998" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 367.36 194.23839999999998 Q 380.24 189.6752 393.12 195.3792" fill="none" stroke="#5a3d2b" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 341.6 248.95999999999998 Q 360 263.68 378.4 248.95999999999998" fill="none" stroke="#4a3226" stroke-width="6.44" stroke-linecap="round" stroke-linejoin="round"/><circle cx="319.52" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="400.48" cy="237.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="360.0" cy="149.0" r="6.82" fill="#f0876f"/><circle cx="370.46162167924666" cy="156.60081306187558" r="6.82" fill="#f0876f"/><circle cx="366.4656377752172" cy="168.89918693812442" r="6.82" fill="#f0876f"/><circle cx="353.5343622247828" cy="168.89918693812442" r="6.82" fill="#f0876f"/><circle cx="349.5383783207533" cy="156.60081306187558" r="6.82" fill="#f0876f"/><circle cx="360" cy="160" r="5.5" fill="#f2b53c"/><circle cx="324.0" cy="161.0" r="6.82" fill="#f0876f"/><circle cx="334.46162167924666" cy="168.60081306187558" r="6.82" fill="#f0876f"/><circle cx="330.4656377752172" cy="180.89918693812442" r="6.82" fill="#f0876f"/><circle cx="317.5343622247828" cy="180.89918693812442" r="6.82" fill="#f0876f"/><circle cx="313.5383783207533" cy="168.60081306187558" r="6.82" fill="#f0876f"/><circle cx="324" cy="172" r="5.5" fill="#f2b53c"/><circle cx="396.0" cy="161.0" r="6.82" fill="#f0876f"/><circle cx="406.46162167924666" cy="168.60081306187558" r="6.82" fill="#f0876f"/><circle cx="402.4656377752172" cy="180.89918693812442" r="6.82" fill="#f0876f"/><circle cx="389.5343622247828" cy="180.89918693812442" r="6.82" fill="#f0876f"/><circle cx="385.5383783207533" cy="168.60081306187558" r="6.82" fill="#f0876f"/><circle cx="396" cy="172" r="5.5" fill="#f2b53c"/><circle cx="298.0" cy="185.0" r="6.82" fill="#f0876f"/><circle cx="308.46162167924666" cy="192.60081306187558" r="6.82" fill="#f0876f"/><circle cx="304.4656377752172" cy="204.89918693812442" r="6.82" fill="#f0876f"/><circle cx="291.5343622247828" cy="204.89918693812442" r="6.82" fill="#f0876f"/><circle cx="287.5383783207533" cy="192.60081306187558" r="6.82" fill="#f0876f"/><circle cx="298" cy="196" r="5.5" fill="#f2b53c"/><circle cx="422.0" cy="185.0" r="6.82" fill="#f0876f"/><circle cx="432.46162167924666" cy="192.60081306187558" r="6.82" fill="#f0876f"/><circle cx="428.4656377752172" cy="204.89918693812442" r="6.82" fill="#f0876f"/><circle cx="415.5343622247828" cy="204.89918693812442" r="6.82" fill="#f0876f"/><circle cx="411.5383783207533" cy="192.60081306187558" r="6.82" fill="#f0876f"/><circle cx="422" cy="196" r="5.5" fill="#f2b53c"/><line x1="419" y1="361" x2="430" y2="326" stroke="#7fae70" stroke-width="6" stroke-linecap="round"/><ellipse cx="406" cy="346" rx="11" ry="5.5" fill="#7fae70" opacity="0.85"/><circle cx="432.0" cy="290.0" r="12.4" fill="#f0876f"/><circle cx="451.0211303259031" cy="303.819660112501" r="12.4" fill="#f0876f"/><circle cx="443.7557050458495" cy="326.180339887499" r="12.4" fill="#f0876f"/><circle cx="420.2442949541505" cy="326.180339887499" r="12.4" fill="#f0876f"/><circle cx="412.9788696740969" cy="303.8196601125011" r="12.4" fill="#f0876f"/><circle cx="432" cy="310" r="10.0" fill="#f2b53c"/>',
    '久': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><polygon points="298,438 324,266 384,266 410,438" fill="#b57b44"/><path d="M 312 402 Q 354 390 396 402" fill="none" stroke="#e9b97e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M 308 366 Q 354 353 400 366" fill="none" stroke="#e9b97e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M 314 330 Q 354 318 394 330" fill="none" stroke="#e9b97e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M 326 298 Q 354 289 382 298" fill="none" stroke="#e9b97e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="354" cy="192" r="100" fill="#7fae70"/><circle cx="258" cy="244" r="66" fill="#9cc98a"/><circle cx="450" cy="244" r="66" fill="#9cc98a"/><circle cx="354" cy="122" r="62" fill="#9cc98a" opacity="0.92"/><path d="M 396 112 Q 398 142 428 142 Q 458 142 460 112 Z" fill="#b57b44"/><ellipse cx="417" cy="112" rx="9" ry="11" fill="#f9c95e"/><ellipse cx="439" cy="112" rx="9" ry="11" fill="#f9c95e"/><rect x="548" y="402" width="13" height="44" rx="6" fill="#b57b44"/><circle cx="554" cy="382" r="30" fill="#9cc98a"/>',
    '全': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="270" y="364" width="220" height="60" rx="10" fill="#e8663c"/><path d="M 365.75 394.95 L 377.15 405.4 L 395.2 383.55" fill="none" stroke="#fdfdfa" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><rect x="285" y="302" width="190" height="60" rx="10" fill="#f2b53c"/><path d="M 365.75 332.95 L 377.15 343.4 L 395.2 321.55" fill="none" stroke="#3e9486" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><rect x="300" y="240" width="160" height="60" rx="10" fill="#4fae9f"/><path d="M 365.75 270.95 L 377.15 281.4 L 395.2 259.55" fill="none" stroke="#fdfdfa" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><rect x="330" y="178" width="100" height="60" rx="10" fill="#5fa8d8"/><path d="M 365.75 208.95 L 377.15 219.4 L 395.2 197.55" fill="none" stroke="#fdfdfa" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
    '最': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="166" y="352" width="132" height="84" rx="10" fill="#f2b53c"/><rect x="166" y="414" width="132" height="22" rx="10" fill="#d99a2b"/><rect x="306" y="300" width="148" height="136" rx="10" fill="#e8663c"/><rect x="306" y="412" width="148" height="24" rx="10" fill="#d4552f"/><rect x="462" y="372" width="132" height="64" rx="10" fill="#5fa8d8"/><rect x="462" y="414" width="132" height="22" rx="10" fill="#4a97c9"/><rect x="362.6" y="240.51999999999998" width="15.079999999999998" height="48.72" rx="6.959999999999999" fill="#4a97c9"/><rect x="382.32" y="240.51999999999998" width="15.079999999999998" height="48.72" rx="6.959999999999999" fill="#4a97c9"/><ellipse cx="370.14" cy="298.52" rx="12.18" ry="5.8" fill="#4a3226" opacity="0.85"/><ellipse cx="389.86" cy="298.52" rx="12.18" ry="5.8" fill="#4a3226" opacity="0.85"/><path d="M 347.52 204.56 Q 346.36 249.79999999999998 356.8 250.95999999999998 L 403.2 250.95999999999998 Q 413.64 249.79999999999998 412.48 204.56 Q 380 195.28 347.52 204.56 Z" fill="#5fa8d8"/><line x1="354.48" y1="208.04" x2="331.28" y2="167.44" stroke="#f8cba4" stroke-width="17.4" stroke-linecap="round"/><circle cx="331.28" cy="167.44" r="7.539999999999999" fill="#f8cba4"/><line x1="405.52" y1="208.04" x2="428.72" y2="167.44" stroke="#f8cba4" stroke-width="17.4" stroke-linecap="round"/><circle cx="428.72" cy="167.44" r="7.539999999999999" fill="#f8cba4"/><circle cx="346.36" cy="169.76000000000002" r="6.38" fill="#f8cba4"/><circle cx="413.64" cy="169.76000000000002" r="6.38" fill="#f8cba4"/><circle cx="380" cy="163.96" r="35.96" fill="#f8cba4"/><path d="M 344.7592 151.374 Q 347.63599999999997 121.5272 380 123.6848 Q 412.36400000000003 121.5272 415.2408 151.374 Q 399.778 145.26080000000002 380 148.85680000000002 Q 360.222 145.26080000000002 344.7592 151.374 Z" fill="#5a3d2b"/><ellipse cx="367.24" cy="159.32000000000002" rx="5.8" ry="7.539999999999999" fill="#4a3226"/><circle cx="367.24" cy="156.42000000000002" r="1.9719999999999998" fill="#fdfdfa"/><ellipse cx="392.76" cy="159.32000000000002" rx="5.8" ry="7.539999999999999" fill="#4a3226"/><circle cx="392.76" cy="156.42000000000002" r="1.9719999999999998" fill="#fdfdfa"/><path d="M 359.12 145.26080000000002 Q 367.24 141.6648 375.36 144.54160000000002" fill="none" stroke="#5a3d2b" stroke-width="3.4799999999999995" stroke-linecap="round" stroke-linejoin="round"/><path d="M 384.64 144.54160000000002 Q 392.76 141.6648 400.88 145.26080000000002" fill="none" stroke="#5a3d2b" stroke-width="3.4799999999999995" stroke-linecap="round" stroke-linejoin="round"/><path d="M 364.92 179.04000000000002 Q 380 173.24 395.08 179.04000000000002 Q 393.92 194.12 380 196.44000000000003 Q 366.08 194.12 364.92 179.04000000000002 Z" fill="#6b3325"/><path d="M 371.88 188.32000000000002 Q 380 183.68 388.12 188.32000000000002 Q 385.22 194.70000000000002 380 195.28000000000003 Q 374.78 194.70000000000002 371.88 188.32000000000002 Z" fill="#f0876f"/><circle cx="354.48" cy="172.08" r="6.38" fill="#f5a58c" opacity="0.8"/><circle cx="405.52" cy="172.08" r="6.38" fill="#f5a58c" opacity="0.8"/><polygon points="380.0,58.0 387.9351009059484,77.0782705759382 408.5316954888546,78.72949016875158 392.8392629699846,92.1717294240618 397.6335575687742,112.27050983124843 380.0,101.5 362.36644243122583,112.27050983124843 367.1607370300154,92.1717294240618 351.4683045111454,78.72949016875158 372.0648990940516,77.0782705759382" fill="#f7ae35"/>',
    '活': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><path d="M 110 298 Q 160 274 210 298 T 310 298 T 410 298 T 510 298 T 610 298 L 648 302 L 648 452 Q 380 472 110 452 Z" fill="#79c2e6"/><g transform="rotate(-6 390 368)"><polygon points="336,368 296,340 304,396" fill="#e8663c"/><ellipse cx="390" cy="368" rx="62" ry="40" fill="#f2916c"/><ellipse cx="398" cy="384" rx="44" ry="20" fill="#f7c5ae"/><polygon points="370,330 396,312 408,334" fill="#e8663c"/><ellipse cx="394" cy="398" rx="16" ry="9" fill="#e8663c" opacity="0.85"/><path d="M 414 344 Q 424 368 414 390" fill="none" stroke="#e8663c" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="428" cy="358" r="6" fill="#4a3226"/><circle cx="430" cy="356" r="1.8" fill="#fdfdfa"/></g><circle cx="462" cy="320" r="7" fill="#fdfdfa" opacity="0.65"/><circle cx="478" cy="294" r="5" fill="#fdfdfa" opacity="0.6"/><circle cx="490" cy="274" r="3.5" fill="#fdfdfa" opacity="0.55"/><path d="M 244 253 Q 251.65 264.25 244 271 Q 236.35 264.25 244 253 Z" fill="#79c2e6"/><path d="M 540 248 Q 546.8 258.0 540 264 Q 533.2 258.0 540 248 Z" fill="#79c2e6"/><path d="M 216 288 Q 244 272 272 288" fill="none" stroke="#a5d9f0" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 496 282 Q 524 266 552 282" fill="none" stroke="#a5d9f0" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    '真': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><rect x="246.5" y="355.9" width="22.099999999999998" height="71.39999999999999" rx="10.2" fill="#4a97c9"/><rect x="275.4" y="355.9" width="22.099999999999998" height="71.39999999999999" rx="10.2" fill="#4a97c9"/><ellipse cx="257.55" cy="440.9" rx="17.849999999999998" ry="8.5" fill="#4a3226" opacity="0.85"/><ellipse cx="286.45" cy="440.9" rx="17.849999999999998" ry="8.5" fill="#4a3226" opacity="0.85"/><path d="M 224.4 303.20000000000005 Q 222.7 369.5 238.0 371.2 L 306.0 371.2 Q 321.3 369.5 319.6 303.20000000000005 Q 272 289.6 224.4 303.20000000000005 Z" fill="#5fa8d8"/><line x1="234.6" y1="308.30000000000007" x2="263.5" y2="332.1" stroke="#f8cba4" stroke-width="25.5" stroke-linecap="round"/><circle cx="263.5" cy="332.1" r="11.049999999999999" fill="#f8cba4"/><line x1="309.4" y1="308.30000000000007" x2="282.2" y2="332.1" stroke="#f8cba4" stroke-width="25.5" stroke-linecap="round"/><circle cx="282.2" cy="332.1" r="11.049999999999999" fill="#f8cba4"/><circle cx="260.1" cy="328.70000000000005" r="11.049999999999999" fill="#f8cba4"/><circle cx="283.9" cy="328.70000000000005" r="11.049999999999999" fill="#f8cba4"/><circle cx="222.7" cy="252.20000000000005" r="9.35" fill="#f8cba4"/><circle cx="321.3" cy="252.20000000000005" r="9.35" fill="#f8cba4"/><circle cx="272" cy="243.70000000000005" r="52.699999999999996" fill="#f8cba4"/><path d="M 220.354 225.25500000000005 Q 224.57 181.51400000000007 272 184.67600000000004 Q 319.43 181.51400000000007 323.646 225.25500000000005 Q 300.985 216.29600000000005 272 221.56600000000006 Q 243.015 216.29600000000005 220.354 225.25500000000005 Z" fill="#5a3d2b"/><ellipse cx="253.3" cy="236.90000000000003" rx="8.5" ry="11.049999999999999" fill="#4a3226"/><circle cx="254.15" cy="231.80000000000004" r="2.8899999999999997" fill="#fdfdfa"/><ellipse cx="290.7" cy="236.90000000000003" rx="8.5" ry="11.049999999999999" fill="#4a3226"/><circle cx="291.55" cy="231.80000000000004" r="2.8899999999999997" fill="#fdfdfa"/><path d="M 241.4 216.29600000000005 Q 253.3 211.02600000000004 265.2 215.24200000000005" fill="none" stroke="#5a3d2b" stroke-width="5.1" stroke-linecap="round" stroke-linejoin="round"/><path d="M 278.8 215.24200000000005 Q 290.7 211.02600000000004 302.6 216.29600000000005" fill="none" stroke="#5a3d2b" stroke-width="5.1" stroke-linecap="round" stroke-linejoin="round"/><path d="M 255.0 265.80000000000007 Q 272 279.4000000000001 289.0 265.80000000000007" fill="none" stroke="#4a3226" stroke-width="5.95" stroke-linecap="round" stroke-linejoin="round"/><circle cx="234.6" cy="255.60000000000005" r="9.35" fill="#f5a58c" opacity="0.8"/><circle cx="309.4" cy="255.60000000000005" r="9.35" fill="#f5a58c" opacity="0.8"/><path d="M 288 394.8 C 225.6 348 251.6 301.2 288 332.4 C 324.4 301.2 350.4 348 288 394.8 Z" fill="#d4552f"/><path d="M 284 390.8 C 221.6 344 247.6 297.2 284 328.4 C 320.4 297.2 346.4 344 284 390.8 Z" fill="#e8663c"/><circle cx="262" cy="322" r="8" fill="#fdfdfa" opacity="0.75"/><line x1="256" y1="314" x2="260" y2="326" stroke="#f8cba4" stroke-width="17" stroke-linecap="round"/><line x1="288" y1="314" x2="284" y2="326" stroke="#f8cba4" stroke-width="17" stroke-linecap="round"/><circle cx="260" cy="330" r="11.5" fill="#f8cba4"/><circle cx="284" cy="330" r="11.5" fill="#f8cba4"/><rect x="534.5" y="355.9" width="22.099999999999998" height="71.39999999999999" rx="10.2" fill="#4a97c9"/><rect x="563.4" y="355.9" width="22.099999999999998" height="71.39999999999999" rx="10.2" fill="#4a97c9"/><ellipse cx="545.55" cy="440.9" rx="17.849999999999998" ry="8.5" fill="#4a3226" opacity="0.85"/><ellipse cx="574.45" cy="440.9" rx="17.849999999999998" ry="8.5" fill="#4a3226" opacity="0.85"/><path d="M 512.4 303.20000000000005 Q 510.7 369.5 526.0 371.2 L 594.0 371.2 Q 609.3 369.5 607.6 303.20000000000005 Q 560 289.6 512.4 303.20000000000005 Z" fill="#4fae9f"/><line x1="522.6" y1="308.30000000000007" x2="488.6" y2="248.80000000000004" stroke="#f8cba4" stroke-width="25.5" stroke-linecap="round"/><circle cx="488.6" cy="248.80000000000004" r="11.049999999999999" fill="#f8cba4"/><line x1="597.4" y1="308.30000000000007" x2="631.4" y2="248.80000000000004" stroke="#f8cba4" stroke-width="25.5" stroke-linecap="round"/><circle cx="631.4" cy="248.80000000000004" r="11.049999999999999" fill="#f8cba4"/><circle cx="510.7" cy="252.20000000000005" r="9.35" fill="#f8cba4"/><circle cx="609.3" cy="252.20000000000005" r="9.35" fill="#f8cba4"/><circle cx="560" cy="243.70000000000005" r="52.699999999999996" fill="#f8cba4"/><path d="M 508.354 225.25500000000005 Q 512.57 181.51400000000007 560 184.67600000000004 Q 607.43 181.51400000000007 611.646 225.25500000000005 Q 588.985 216.29600000000005 560 221.56600000000006 Q 531.015 216.29600000000005 508.354 225.25500000000005 Z" fill="#5a3d2b"/><ellipse cx="541.3" cy="236.90000000000003" rx="8.5" ry="11.049999999999999" fill="#4a3226"/><circle cx="540.4499999999999" cy="231.80000000000004" r="2.8899999999999997" fill="#fdfdfa"/><ellipse cx="578.7" cy="236.90000000000003" rx="8.5" ry="11.049999999999999" fill="#4a3226"/><circle cx="577.85" cy="231.80000000000004" r="2.8899999999999997" fill="#fdfdfa"/><path d="M 529.4 216.29600000000005 Q 541.3 211.02600000000004 553.2 215.24200000000005" fill="none" stroke="#5a3d2b" stroke-width="5.1" stroke-linecap="round" stroke-linejoin="round"/><path d="M 566.8 215.24200000000005 Q 578.7 211.02600000000004 590.6 216.29600000000005" fill="none" stroke="#5a3d2b" stroke-width="5.1" stroke-linecap="round" stroke-linejoin="round"/><path d="M 537.9 265.80000000000007 Q 560 257.30000000000007 582.1 265.80000000000007 Q 580.4 287.9000000000001 560 291.30000000000007 Q 539.6 287.9000000000001 537.9 265.80000000000007 Z" fill="#6b3325"/><path d="M 548.1 279.4000000000001 Q 560 272.6000000000001 571.9 279.4000000000001 Q 567.65 288.75000000000006 560 289.6000000000001 Q 552.35 288.75000000000006 548.1 279.4000000000001 Z" fill="#f0876f"/><circle cx="522.6" cy="255.60000000000005" r="9.35" fill="#f5a58c" opacity="0.8"/><circle cx="597.4" cy="255.60000000000005" r="9.35" fill="#f5a58c" opacity="0.8"/>',
    '老': '<ellipse cx="380" cy="446" rx="240" ry="24" fill="#c8e6d8"/><g transform="rotate(7 370 436)"><rect x="342.4" y="338.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><rect x="373.68" y="338.48" width="23.92" height="77.28" rx="11.040000000000001" fill="#4a97c9"/><ellipse cx="354.36" cy="430.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><ellipse cx="385.64" cy="430.48" rx="19.32" ry="9.200000000000001" fill="#4a3226" opacity="0.85"/><path d="M 318.48 281.44 Q 316.64 353.2 333.2 355.04 L 406.8 355.04 Q 423.36 353.2 421.52 281.44 Q 370 266.71999999999997 318.48 281.44 Z" fill="#5fa8d8"/><line x1="329.52" y1="286.96" x2="311.12" y2="353.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="311.12" cy="353.2" r="11.96" fill="#f8cba4"/><line x1="410.48" y1="286.96" x2="428.88" y2="353.2" stroke="#f8cba4" stroke-width="27.6" stroke-linecap="round"/><circle cx="428.88" cy="353.2" r="11.96" fill="#f8cba4"/><circle cx="316.64" cy="226.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="423.36" cy="226.23999999999998" r="10.120000000000001" fill="#f8cba4"/><circle cx="370" cy="217.04" r="57.04" fill="#f8cba4"/><path d="M 314.1008 197.076 Q 318.664 149.7328 370 153.1552 Q 421.336 149.7328 425.8992 197.076 Q 401.372 187.3792 370 193.0832 Q 338.628 187.3792 314.1008 197.076 Z" fill="#e7e2d6"/><ellipse cx="349.76" cy="209.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="350.68" cy="205.07999999999998" r="3.128" fill="#fdfdfa"/><ellipse cx="390.24" cy="209.67999999999998" rx="9.200000000000001" ry="11.96" fill="#4a3226"/><circle cx="391.16" cy="205.07999999999998" r="3.128" fill="#fdfdfa"/><path d="M 336.88 187.3792 Q 349.76 181.6752 362.64 186.23839999999998" fill="none" stroke="#e7e2d6" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 377.36 186.23839999999998 Q 390.24 181.6752 403.12 187.3792" fill="none" stroke="#e7e2d6" stroke-width="5.5200000000000005" stroke-linecap="round" stroke-linejoin="round"/><path d="M 351.6 240.95999999999998 Q 370 255.67999999999998 388.4 240.95999999999998" fill="none" stroke="#4a3226" stroke-width="6.44" stroke-linecap="round" stroke-linejoin="round"/><circle cx="329.52" cy="229.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><circle cx="410.48" cy="229.92" r="10.120000000000001" fill="#f5a58c" opacity="0.8"/><path d="M 351.6 235.43999999999997 Q 370 228.07999999999998 388.4 235.43999999999997 Q 370 239.11999999999998 351.6 235.43999999999997 Z" fill="#d9d0c5"/><g fill="none" stroke="#4a3226" stroke-width="4.6000000000000005"><circle cx="349.76" cy="209.67999999999998" r="14.72"/><circle cx="390.24" cy="209.67999999999998" r="14.72"/><line x1="364.48" y1="209.67999999999998" x2="375.52" y2="209.67999999999998" stroke="#4a3226" stroke-width="4.6000000000000005" stroke-linecap="round"/></g><path d="M 348 240 Q 370 302 392 240 Q 370 256 348 240 Z" fill="#e7e2d6"/></g><line x1="438.5" y1="356" x2="438.5" y2="441" stroke="#b57b44" stroke-width="13" stroke-linecap="round"/><circle cx="438.5" cy="350" r="13" fill="#b57b44"/><circle cx="438.5" cy="361" r="12" fill="#f8cba4"/>',
}
_arts_prev = arts
def arts():
    a = dict(_arts_prev())
    a.update(_arts_mig)
    return a
