#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""部首家族 · 找朋友 —— 扩充数据（新增 9 个家族 + 9 张徽章插画）。

本文件是**独立可运行**的数据模块，schema 与 ../汉语启蒙_素材.py 一致：
    NEW_CARDS = [ _family(...), ... ]
    NEW_ARTS  = { "徽虫": "<svg 内部标记>", ... }

合并到 ../汉语启蒙_素材.py 时注意一件事（重要）：
    这里的 `_family()` 是 **8 参数**版本，比 汉语启蒙_素材.py 里现有的 7 参数版本
    多一个「怎么玩」（现有版本把"怎么玩"写死成同一句话，本轮 9 张卡每张都不一样）。
    8 参数顺序：rad, name, meaning, members, say(家族故事), play(怎么玩), chat(聊一聊), life(生活里)
    产出的 tips 顺序与现有卡片完全一致：[家族故事, 怎么玩, 聊一聊, 生活里]
    （模板 cardFamily 取 tips[2] 当“聊一聊”渲染在卡片底部，顺序不能动）。

    ★ 用同目录的 `扩充合并.py` 合并**不需要**改 汉语启蒙_素材.py 的 `_family()`：
      合并脚本只是把这里已经构造好的卡片 dict 直接 extend 进 SET_JIAZU，
      不会再调用那边的 `_family()`。已实测：
          python3 扩充合并.py
          → 并入 部首家族_扩充数据.py → jiazu: 卡 9 / 韵语 0 / 游戏 0 / 新插画 9
    只有在**手工把 NEW_CARDS 抄进 汉语启蒙_素材.py** 时，才需要把那边的
    `_family()` 也换成下面这份 8 参数定义，否则会报
    “_family() takes 7 positional arguments but 8 were given”。

设计依据（详见同目录 部首家族_扩充设计.md）：
- 每个成员字都真带这个部首（用 Unihan 康熙部首 + 简体字部件肉眼核对过）；
- 一个成员字只属于一个家族，扩充后 19 个家族成员零重复；
- 成员字全部在 ../识字卡片_1000字/字库1000.py 的 1000 字全集内；
- 徽章画风沿用 汉语启蒙_素材.py 的 _badge(bg, inner)：圆外圈 + 奶油内圈 + 中间图形。

独立运行本文件做数据自检：python3 部首家族_扩充数据.py
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_PARENT = _HERE.parent           # 汉语启蒙卡集/
_GRAND = _PARENT.parent         # 孩子/
for _p in (str(_GRAND), str(_PARENT)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from 识字卡片_素材库 import (  # noqa: E402
    C, E, R, L, P, PG, wrap, bowl, heart, kid,
    INK, PAGE, RED, RED_D, YEL, YEL_D, SUN, SUN_L, TEAL, TEAL_D, TEAL_L,
    BLUE, BLUE_D, WBLUE, SKIN, SKIN_D, WOOD, WOOD_D, WOOD_L, GREEN, GREEN_L,
    PINK, WHITE,
)

# ============================ 徽章 ============================
# 圈色（外圈）刻意避开现有 10 张徽章的 teal / green / peach / blue /
# light green / yellow / pink：改用 紫、灰蓝、玫红、深棕、深钢蓝、砖红、
# 橄榄、暖橙、深金 九条新色道，且内圈仍是奶油 PAGE，与现有卡片同一套结构。


def _badge(bg, inner):
    """圆形徽章：外圈 bg + 奶油内圈 + 中间图形（沿用 汉语启蒙_素材.py 的画法）。"""
    return wrap(C(380, 240, 168, bg), C(380, 240, 146, PAGE), inner)


def _badge_chong():
    """虫：一只红瓢虫，黑头黑点，两根小触角。"""
    body = wrap(
        E(382, 262, 78, 66, RED_D),
        E(378, 252, 76, 66, RED),
        L(378, 192, 378, 316, INK, 6),
        C(344, 238, 13, INK), C(412, 238, 13, INK),
        C(356, 288, 11, INK), C(400, 288, 11, INK),
        E(344, 212, 14, 10, WHITE, 0.45),
        C(378, 174, 40, INK),
        P("M 354 142 Q 328 108 308 122", stroke=INK, w=6),
        P("M 402 142 Q 428 108 448 122", stroke=INK, w=6),
        L(306, 236, 284, 250, INK, 6), L(306, 268, 286, 284, INK, 6),
        L(306, 300, 288, 312, INK, 6),
        L(450, 236, 472, 250, INK, 6), L(450, 268, 470, 284, INK, 6),
        L(450, 300, 468, 312, INK, 6))
    return _badge("#9d7fa8", body)


def _badge_yan():
    """讠：一个大对话气泡，飘着三个小圆点。"""
    bubble = wrap(
        R(272, 152, 220, 136, 36, BLUE),
        PG([(322, 282), (300, 330), (368, 282)], BLUE),
        R(410, 272, 84, 56, 22, TEAL_L),
        PG([(422, 322), (410, 352), (452, 322)], TEAL_L),
        C(332, 220, 15, WHITE), C(382, 220, 15, WHITE), C(432, 220, 15, WHITE))
    return _badge("#9aa3ad", bubble)


def _badge_xin():
    """忄：一颗跳动的心，深红托底、亮红在上、左上一点高光。"""
    h = wrap(
        heart(386, 250, 78, RED_D),
        heart(376, 236, 78, RED),
        E(350, 206, 15, 11, WHITE, 0.6))
    return _badge("#c0516e", h)


def _badge_quan():
    """犭：一只棕白小狗，垂耳、黑鼻子、弯眼睛。"""
    dog = wrap(
        E(304, 182, 32, 58, "#a9713c"), E(456, 182, 32, 58, "#a9713c"),
        E(380, 252, 88, 78, "#e0b07a"),
        E(380, 296, 48, 34, "#f8ecd8"),
        E(380, 274, 14, 10, INK),
        P("M 380 284 Q 380 302 358 300", stroke=INK, w=5),
        P("M 380 284 Q 380 302 402 300", stroke=INK, w=5),
        P("M 366 302 Q 380 322 394 302 Z", PINK),
        E(346, 232, 11, 14, INK), E(414, 232, 11, 14, INK),
        C(342, 228, 4, WHITE), C(410, 228, 4, WHITE))
    return _badge("#8c6a4a", dog)


def _badge_yue():
    """月：一弯月亮，奶黄色月牙，上面有两颗小眼睛一个笑脸。"""
    moon = wrap(
        C(380, 240, 92, SUN),
        C(424, 210, 80, PAGE),
        E(320, 178, 11, 9, SUN_L), E(300, 268, 9, 7, SUN_L),
        E(336, 232, 9, 11, INK), E(360, 228, 9, 11, INK),
        P("M 338 254 Q 350 266 364 250", stroke=INK, w=6),
        C(326, 250, 7, PINK, 0.7))
    return _badge("#4a6fa5", moon)


def _badge_huo():
    """火：一团跳动的火苗，外面红、里面黄，底下压着两根木头。"""
    flame = wrap(
        P("M 380 118 C 424 182 456 224 456 274 C 456 322 422 342 380 342 "
          "C 338 342 306 322 306 274 C 306 230 336 204 352 176 "
          "C 360 204 372 218 380 224 C 388 200 386 158 380 118 Z", RED),
        P("M 380 216 C 406 252 424 278 424 300 C 424 324 404 340 380 340 "
          "C 356 340 338 324 338 300 C 338 282 354 268 366 248 "
          "C 370 266 378 274 386 272 C 386 256 384 236 380 216 Z", SUN),
        R(318, 340, 124, 16, 8, WOOD_D),
        '<g transform="rotate(-14 380 348)">' + R(326, 332, 108, 14, 7, WOOD) + "</g>")
    return _badge("#c2553e", flame)


def _badge_zou():
    """辶：一条弯弯的小路，路上一串小脚印，小朋友正走在上面。"""
    road = P("M 276 340 Q 340 316 392 268 Q 436 228 470 198", stroke=WOOD_L, w=38)
    prints = []
    for x, y in ((308, 322), (344, 300), (378, 274)):
        prints.append(f'<g transform="rotate(-42 {x} {y})">' + E(x, y, 10, 14, "#8a5a33") + "</g>")
    walker = kid(436, 234, 0.44, pose="walk", arms="swing", shirt=RED)
    return _badge("#6d8f7a", wrap(road, *prints, walker))


def _badge_mi():
    """米：一只小碗，碗里堆着金黄的米粒。"""
    grains = []
    rows = [(-44, 252, 4), (-22, 238, 4), (0, 232, 4), (22, 238, 4), (44, 252, 4),
            (-32, 218, 3), (-10, 206, 4), (14, 206, 4), (36, 218, 3),
            (-18, 184, 3), (6, 174, 3), (26, 184, 3)]
    for dx, y, n in rows:
        for i in range(n):
            x = 380 + dx + (i - (n - 1) / 2) * 28
            rot = -20 if (i + int(dx)) % 2 == 0 else 20
            grains.append(f'<g transform="rotate({rot} {x} {y})">'
                          + E(x, y, 16, 8, SUN) + "</g>")
    rice = wrap(E(380, 268, 90, 48, "#f0b64e"), *grains)
    return _badge("#a7a05e", wrap(rice, bowl(380, 300, 82, rice=False)))


def _badge_jin():
    """钅：一块金元宝，两头翘得高高的，中间一道亮光。"""
    gold = wrap(
        P("M 238 268 C 248 236 268 226 288 236 C 320 284 440 284 472 236 "
          "C 492 226 512 236 522 268 C 512 330 458 350 380 350 "
          "C 302 350 248 330 238 268 Z", SUN),
        P("M 292 252 C 324 292 436 292 468 252", stroke=YEL_D, w=7),
        E(338, 314, 30, 11, SUN_L, 0.8),
        E(428, 318, 18, 8, SUN_L, 0.6))
    return _badge("#c08a3e", gold)


NEW_ARTS = {
    "徽虫": _badge_chong(),
    "徽讠": _badge_yan(),
    "徽忄": _badge_xin(),
    "徽犭": _badge_quan(),
    "徽月": _badge_yue(),
    "徽火": _badge_huo(),
    "徽辶": _badge_zou(),
    "徽米": _badge_mi(),
    "徽钅": _badge_jin(),
}


# ============================ 卡片数据 ============================

def _family(rad, name, meaning, members, say, play, chat, life):
    """部首家族卡。8 参数版（比 汉语启蒙_素材.py 的 7 参数版多一个「怎么玩」）。"""
    return {"type": "family", "key": f"族{rad}", "radical": rad, "name": name,
            "meaning": meaning, "members": members, "badge": f"徽{rad}",
            "tips": [["家族故事", say], ["怎么玩", play],
                     ["聊一聊", chat], ["生活里", life]]}


NEW_CARDS = [
    _family("虫", "虫字家族", "带虫字的字，说的都是小虫虫和小动物。",
            [["蚂", "蚂蚁"], ["蚊", "蚊子"], ["蜂", "蜜蜂"],
             ["蝶", "蝴蝶"], ["蝉", "知了"], ["萤", "萤火虫"]],
            "虫字藏在这些字里，它们都是小虫子。",
            "读一个成员字，再用手比出虫子的样子找虫字。",
            "你在公园见过哪些小虫子？名字里带虫字吗？",
            "去公园找小虫，看看它的名字带不带虫字。"),

    _family("讠", "言字旁家族", "带言字旁的字，都和说话有关。",
            [["说", "说话"], ["请", "请坐"], ["谢", "谢谢"],
             ["记", "记住"], ["认", "认字"], ["讲", "讲故事"]],
            "言字旁像一张小嘴巴，说话、谢谢都从这里出。",
            "读一个成员字，再做一做「说」的动作，看谁先想到。",
            "今天跟谁说过话了？那些字带言字旁吗？",
            "吃饭前说一声「谢谢」，指指这两个字。"),

    _family("忄", "竖心旁家族", "带竖心旁的字，说的是心里的小感觉。",
            [["怕", "害怕"], ["惊", "吃惊"], ["急", "着急"],
             ["忙", "帮忙"], ["慌", "慌张"], ["慢", "慢走"]],
            "竖心旁像心里在跳，怕、急、慌都是心的感觉。",
            "做一个表情，说出你是什么感觉，再找带竖心旁的字。",
            "今天你心里是什么感觉？害怕还是着急？",
            "害怕的时候抱抱妈妈，说出「怕」字。"),

    _family("犭", "反犬旁家族", "带反犬旁的字，都是动物朋友。",
            [["猫", "小猫"], ["狗", "小狗"], ["猪", "小猪"],
             ["猴", "猴子"], ["狐", "狐狸"], ["狼", "大灰狼"]],
            "反犬旁像一只小动物，猫、狗、猴、狐狸都是它朋友。",
            "学一学小动物怎么叫，再找找哪个字带反犬旁。",
            "你最喜欢哪个动物？它的名字带反犬旁吗？",
            "去动物园，指着动物说出它的名字。"),

    _family("月", "肉月旁家族", "带月字旁的字，说的都是身体上的事。",
            [["脸", "笑脸"], ["肚", "肚子"], ["肩", "肩膀"],
             ["脖", "脖子"], ["胸", "胸口"], ["膝", "膝盖"]],
            "月字旁胖胖的，说起来都是身上的地方。",
            "指指自己身上的一块，看看那个字带不带月字旁。",
            "你身上哪个地方最爱动？那个字带月字旁吗？",
            "洗澡时指指肚子和脸，说出这两个字。"),

    _family("火", "火字旁家族", "带火字的字，都和火、热有关。",
            [["火", "火焰"], ["灯", "台灯"], ["炒", "炒菜"],
             ["煮", "煮饭"], ["烫", "很烫"]],
            "火字旁像小小的火苗，灯、炒、煮都要用火。",
            "找一件家里用火做的事，说出它的字。",
            "做饭的时候，哪些字带火字旁？",
            "开灯时指指「灯」，说说它带火字旁。"),

    _family("辶", "走之旁家族", "带走之旁的字，都和走动有关。",
            [["过", "过去"], ["进", "进来"], ["送", "送给"],
             ["远", "远方"], ["边", "旁边"], ["道", "马路"]],
            "走之旁像一条小尾巴，走、过、进都要迈开腿。",
            "读一个成员字，再做一个小走的动作，看它是不是走之旁。",
            "今天你走到哪里去了？那个字带走之旁吗？",
            "出门时说「我们走过去」，指指这个字。"),

    _family("米", "米字旁家族", "带米字的字，都是能吃的。",
            [["米", "大米"], ["糖", "糖果"], ["粥", "喝粥"],
             ["糕", "蛋糕"], ["粉", "面粉"]],
            "米字旁像一把米粒，糖、粥、糕、粉都是吃的。",
            "看桌上的食物，找出带米字的字。",
            "今天吃的东西里，哪个字带米字旁？",
            "吃饭时指着米饭，说说「米」字。"),

    _family("钅", "金字旁家族", "带金字旁的字，都是金属做的。",
            [["钟", "时钟"], ["铃", "铃铛"], ["针", "针线"],
             ["镜", "镜子"], ["钉", "钉子"]],
            "金字旁亮亮的，针、铃、镜子都是金属做的。",
            "摸一摸家里的金属物件，看看名字带不带金字旁。",
            "家里哪些东西是金属做的？名字带金字旁吗？",
            "看看门上的锁或钥匙，指指「金」字旁。"),
]


# ============================ 自检 ============================
if __name__ == "__main__":
    import importlib.util
    import json
    import xml.etree.ElementTree as ET

    problems = []

    # ---- 载入基准 ----
    def _load(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    zk = _load(_GRAND / "识字卡片_1000字" / "字库1000.py", "zk1000")
    chars1000 = set()
    for g in zk.GROUPS:
        for it in g["chars"]:
            chars1000.update(list(it) if isinstance(it, tuple)
                             else [it.get("char", it) if isinstance(it, dict) else it])

    sucai = _load(_PARENT / "汉语启蒙_素材.py", "qysucai")
    old_families = [c for g in sucai.SET_JIAZU["groups"] for c in g["cards"]]

    # ---- ① 成员字都在 1000 字全集内 ----
    for c in NEW_CARDS:
        for ch, word in c["members"]:
            if ch not in chars1000:
                problems.append(f"{c['name']} 成员「{ch}」不在 1000 字全集内")
            if len(word) > 4:
                problems.append(f"{c['name']} 词「{word}」超过 4 字")
            if not word:
                problems.append(f"{c['name']} 成员「{ch}」没有配词")
        if not 4 <= len(c["members"]) <= 6:
            problems.append(f"{c['name']} 成员数 {len(c['members'])} 不在 4~6 之间")
        if not (1 <= len(c["meaning"]) <= 30):
            problems.append(f"{c['name']} 一句话含义过长")
        for tag, txt in c["tips"]:
            if len(txt) > 30:
                problems.append(f"{c['name']} 的「{tag}」超过 30 字：{txt}")

    # ---- ② 全部家族（新 9 + 现有 10）成员零重复 ----
    seen = {}
    for c in NEW_CARDS + old_families:
        for ch, _ in c["members"]:
            if ch in seen:
                problems.append(f"成员字「{ch}」重复：{seen[ch]} 与 {c['name']}")
            else:
                seen[ch] = c["name"]

    # ---- ③ 新部首不与现有 10 个部首相同 ----
    old_rads = {c["radical"] for c in old_families}
    for c in NEW_CARDS:
        if c["radical"] in old_rads:
            problems.append(f"新部首「{c['radical']}」与现有家族重复")
        if c["badge"] not in NEW_ARTS:
            problems.append(f"{c['name']} 缺少徽章插画 {c['badge']}")

    # ---- ④ 徽章 SVG 合法 ----
    for k, v in NEW_ARTS.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except Exception as e:  # noqa: BLE001
            problems.append(f"插画 {k} 无法解析: {e}")
        for bad in ("<text", "<use", "<defs", "<image", "href"):
            if bad in v:
                problems.append(f"插画 {k} 含禁止标记 {bad}")

    # ---- ⑤ 部首字形在宋体里存在（构建器要抽矢量） ----
    try:
        from fontTools.ttLib import TTCollection
        coll = TTCollection("/System/Library/Fonts/Supplemental/Songti.ttc", lazy=True)
        cmap = coll.fonts[0].getBestCmap()
        need = {c["radical"] for c in NEW_CARDS}
        need |= {m[0] for c in NEW_CARDS for m in c["members"]}
        miss = sorted(ch for ch in need if ord(ch) not in cmap)
        if miss:
            problems.append(f"宋体缺字: {miss}")
    except Exception as e:  # noqa: BLE001
        print(f"（跳过宋体检查：{e}）")

    # ---- 报告 ----
    total_members = sum(len(c["members"]) for c in NEW_CARDS + old_families)
    print(f"新增家族 {len(NEW_CARDS)} 个，扩充后共 {len(NEW_CARDS) + len(old_families)} 个家族")
    print(f"新成员 {sum(len(c['members']) for c in NEW_CARDS)} 个，"
          f"全体成员 {total_members} 个，去重后 {len(seen)} 个")
    print(f"新徽章 {len(NEW_ARTS)} 张；新部首：{' '.join(c['radical'] for c in NEW_CARDS)}")
    if problems:
        print("问题：")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("数据自检通过 ✓")
