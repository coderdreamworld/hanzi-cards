#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扩充卡内容审校（2026-11-01）：用权威数据核对“卡片讲的对不对”。

核对项：
  ① 部首归属：新家族每个成员字的 IDS 里必须真的带这个部首，且位置符合
     （竖心旁要左��� ⿰忄X；走之旁 ⿺辶X；虫/讠/犭/火/月/米/钅按家族要求）。
  ② 会意拆解：每张新会意卡的“部件”必须等于该字 IDS 的真实构形。
  ③ 韵语：行末字韵脚一致、6 首互不撞车；且「找韵脚」提示里列的字
     必须就是每行行末的那个字（现网自检漏了这一条）。
  ④ 用字覆盖：韵语正文与提示、游戏步骤与提示用字都在 1000 字全集内。

依赖：
  /tmp/ids.txt  —— CHISE 汉字构形数据库（Unicode IDS）
                  下载：curl -sSL https://raw.githubusercontent.com/cjkvi/cjkvi-ids/master/ids.txt -o /tmp/ids.txt
  拼音表1000.json（项目内，拼音与声调的权威来源）

用法：python3 扩充/审校_内容核对.py
"""
import json
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent          # 汉语启蒙卡集/
_PARENT = _ROOT.parent        # 孩子/
sys.path.insert(0, str(_PARENT))
sys.path.insert(0, str(_ROOT))

IDS_PATH = Path("/tmp/ids.txt")
IDS_TSV = _HERE / "部首构形表.tsv"      # 仓库内的构形快照（离线可跑）
PINYIN_JSON = _PARENT / "识字卡片_1000字" / "拼音表1000.json"


def load_module(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def norm_ids(s):
    """IDS 变体字归一：吅＝并排两口、昍＝并排两日、龵＝左手旁、灬＝火的四点底。"""
    return (s.replace("吅", "⿰口口").replace("昍", "⿰日日")
             .replace("龵", "手").replace("灬", "火"))


def comps(ids):
    """从 IDS 里取出构件（去掉结构符），用于和卡片上的部件逐字比对。"""
    return "".join(sorted(re.sub(r"[⿰-⿿]", "", norm_ids(ids))))


def load_ids():
    """优先用仓库内的构形快照，其次用 /tmp/ids.txt（CHISE 汉字构形数据库）。"""
    ids = {}
    if IDS_TSV.exists():
        for line in IDS_TSV.read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                ids[parts[0]] = parts[1]
    if ids:
        return ids
    if not IDS_PATH.exists():
        return ids
    for line in IDS_PATH.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        cp = parts[0][2:]
        try:
            ch = chr(int(cp, 16))
        except ValueError:
            continue
        ids[ch] = parts[2].split("[")[0].strip()
    return ids


# ---- 部首 → (IDS 里必须出现的构件, 允许的结构前缀) ----
RAD_REQ = {
    "虫": ("虫", ("⿰", "⿱", "⿲")),
    "讠": ("讠", ("⿰",)),
    "忄": ("忄", ("⿰",)),          # 必须左���（竖心旁）
    "犭": ("犭", ("⿰",)),
    "月": ("月", ("⿰", "⿱", "⿸", "⿹")),
    "火": ("火", ("⿰", "⿱", "⿲")),
    "辶": ("辶", ("⿺",)),
    "米": ("米", ("⿰", "⿱", "⿲")),
    "钅": ("钅", ("⿰",)),
}

# ---- 会意卡声称的部件 → 期望 IDS（用 IDS 描述真实构形）----
HUIYI_EXPECT = {
    "好": "⿰女子", "双": "⿰又又", "品": "⿱口⿰口口", "掰": "⿲手分手",
    "灶": "⿰火土", "岩": "⿱山石", "晶": "⿱日⿰日日", "朋": "⿰月月",
    "出": "⿱屮凵", "男": "⿱田力",
}
# 「出」是民间字理（两座山叠起来），字形学上的真实构形是 屮+凵；
# 卡面教的是通行启蒙说法，这里按约定放行但必须显式记录。
HUIYI_FOLK = {"出": ("山", "山")}

TM = {"ā": "a", "á": "a", "ǎ": "a", "à": "a", "ē": "e", "é": "e", "ě": "e", "è": "e",
      "ī": "i", "í": "i", "ǐ": "i", "ì": "i", "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
      "ū": "u", "ú": "u", "ǔ": "u", "ù": "u", "ǖ": "ü", "ǘ": "ü", "ǚ": "ü", "ǜ": "ü", "ü": "ü"}
INIT = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h",
        "j", "q", "x", "r", "z", "c", "s"]


def final_of(p):
    s = "".join(TM.get(c, c) for c in p.lower() if c.isalpha())
    if not s:
        return "?"
    if s[0] in "yw":
        f = s[1:] if len(s) > 1 else ""
        if s[0] == "y" and f.startswith("u"):
            f = "ü" + f[1:]
    else:
        f = s
        for i in INIT:
            if s.startswith(i) and len(s) > len(i):
                f = s[len(i):]
                break
    f = f.replace("ü", "v")
    for a, b in (("iu", "iou"), ("ui", "uei"), ("un", "uen")):
        f = f.replace(a, b)
    f = {"iou": "iu", "uei": "ui", "uen": "un"}.get(f, f)
    return f.replace("v", "ü")


def rhyme_family(p):
    """十三辙并韵：去介音 i/u/ü；ao/iao、a/ua、ang/iang/uang 同辙。"""
    f = final_of(p)
    while f and f[0] in "iuü" and len(f) > 1:
        f = f[1:]
    return f


def line_tail(line):
    m = re.match(r"^(.*)([一-鿿])([，。；！？]?)$", line)
    return m.group(2) if m else None


def main():
    problems, notes = [], []
    ids = load_ids()
    if not ids:
        print("⚠ 没有 /tmp/ids.txt，跳过构形核对（部首/拆解结论会缺证据）")
    py = json.loads(PINYIN_JSON.read_text(encoding="utf-8"))
    ziku = load_module(_PARENT / "识字卡片_1000字" / "字库1000.py", "zk")
    S = set()
    for g in ziku.GROUPS:
        for it in g["chars"]:
            S.update(list(it) if isinstance(it, tuple)
                     else [it.get("char", it) if isinstance(it, dict) else it])

    huiyi = load_module(_HERE / "会意字_扩充数据.py", "ext_huiyi")
    jiazu = load_module(_HERE / "部首家族_扩充数据.py", "ext_jiazu")
    yunyu = load_module(_HERE / "韵语声音_扩充数据.py", "ext_yunyu")

    # ① 部首归属
    print("① 新家族成员部首归属（IDS 构形证据）")
    for c in jiazu.NEW_CARDS:
        rad = c["radical"]
        comp, prefixes = RAD_REQ[rad]
        for ch, _ in c["members"]:
            d = ids.get(ch, "")
            dn = norm_ids(d)
            ok = (ch == rad) or (dn.startswith(prefixes) and comp in dn)
            mark = "✓" if ok else "✗"
            if not ok:
                problems.append(f"[部首] {c['name']} 成员「{ch}」IDS={d or '无'} 不含 {comp}（应为 {'/'.join(prefixes)} 构形）")
            print(f"   {mark} {rad}·{ch}  IDS={d or '（无 IDS）'}")

    # ② 会意拆解
    print("\n② 会意卡拆解与 IDS 是否一致")
    for c in huiyi.NEW_CARDS:
        r = c["result"]
        parts = "".join(p[0] for p in c["parts"])
        d = ids.get(r, "")
        exp = HUIYI_EXPECT.get(r, "")
        got = comps(d) if d else ""
        want = "".join(sorted(parts))
        folk = HUIYI_FOLK.get(r)
        ok = bool(d) and (got == want or (folk is not None and tuple(sorted(parts)) == folk))
        print(f"   {'✓' if ok else '✗'} {r}  卡片部件={parts}  构形构件={got or '—'}  IDS={d or '（无）'}"
              + ("  ← 民间字理，已记录" if folk and tuple(sorted(parts)) == folk else ""))
        if exp and d and norm_ids(d) != exp:
            problems.append(f"[拆解] {r} 构形 {d} 与预期 {exp} 不一致（IDS 数据变了？）")
        if not ok:
            problems.append(f"[拆解] {r} 卡片部件「{parts}」与真实构件「{got}」不一致")

    # ③ 韵语：韵脚 + 提示一致性
    print("\n③ 韵语行末字 / 韵辙 / 「找韵脚」提示一致性")
    for v in yunyu.NEW_VERSES:
        tails = [line_tail(ln) for ln in v["lines"]]
        fams = [rhyme_family(py[t]["pinyin"]) for t in tails if t in py]
        tip = v["tips"][2][1]
        listed = re.findall(r"[一-鿿]", tip.split("——")[0])
        tail_list = [t for t in tails]
        ok = listed == tail_list
        print(f"   {'✓' if ok else '✗'} {v['title']}  行末={''.join(tail_list)}  韵辙={set(fams)}")
        print(f"      提示列字={''.join(listed)}")
        if not ok:
            problems.append(f"[韵脚提示] {v['title']} 提示列的字 {''.join(listed)} ≠ 实际行末字 {''.join(tail_list)}")
        if len(set(fams)) != 1:
            problems.append(f"[韵脚] {v['title']} 韵辙不齐 {fams}")

    # ④ 用字覆盖
    print("\n④ 韵语/游戏用字是否都在 1000 字全集")
    for v in yunyu.NEW_VERSES:
        for ln in v["lines"] + [v["tips"][2][1]]:
            miss = [c for c in ln if "一" <= c <= "鿿" and c not in S]
            if miss:
                problems.append(f"[用字] {v['title']} 「{''.join(miss)}」不在 1000 字全集")
    for g in yunyu.NEW_GAMES:
        for s in g["steps"] + [t for _, t in g["tips"]]:
            miss = [c for c in s if "一" <= c <= "鿿" and c not in S]
            if miss:
                problems.append(f"[用字] 游戏「{g['title']}」 「{''.join(miss)}」不在 1000 字全集")

    print()
    if problems:
        print(f"发现 {len(problems)} 个问题：")
        for p in problems:
            print("  ✗ " + p)
        sys.exit(1)
    print("内容核对全部通过 ✓")


if __name__ == "__main__":
    main()
