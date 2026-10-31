#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性迁移脚本：按 识字卡片_重分类方案.md 把 122 张课标卡并入 21 组新结构。

做法：
1. 加载当前全部组模块，收集每张卡的最终版插画（SVG 串）与文案（GROUP_CARDS 条目）；
2. 按目标分组表（逐字）校验 402 卡 / 422 字全覆盖无重复；
3. 重写 识字卡片_字库.py 的 GROUPS（21 组）；
4. 接收组模块：文案例表与插画以「重分类迁移覆盖块」追加到文件末尾
   （已有覆盖块的文件直接在其块内插键，不做链式包裹）；
5. 新组（量词/场所/学习文教/动作·拓展）生成全新模块文件；
6. 删除 kebiao_a~d（内容已全部迁出）。
"""
import importlib.util
import pathlib
import re

ROOT = pathlib.Path("/Users/ping/C 行动_与人交流/孩子")

# ---------- 目标分组（逐字，按各新组内展示顺序） ----------
TARGET = {
    "liangci":  list("只个几片串"),
    "duibi":    [("男", "女"), ("正", "反")],
    "fangwei":  list("东南西北向边旁那"),
    "tianwen":  ["闪"],
    "ziran":    ["江", "气", "影", "贝"],
    "zhiwu":    ["子", "禾", "皮", "苹", "芽"],
    "dongwu":   ["乌", "鸦", "尾", "巴"],
    "rencheng": ["它", "们", "儿", "自", "己", "孩", "谁"],
    "wupin":    ["金", "衣", "服"],
    "changsuo": ["家", "路", "台", "公", "处", "住", "工", "厂", "院"],
    "xuexi":    list("文数学音乐棋字词语句纸课业校歌国升作声诗"),
    "yanse":    ["色", "青", "彩"],
    "shijian":  ["候"],
    "huiyi":    ["力", "无", "步", "对", "同", "办", "法"],
    "dongzuo2": list("打起立成着为参加会见采问到觉穿玩回变生点看过"),
    "xingrong": ["丽", "真", "老", "久", "全", "最", "活"],
    "changyong": ["么", "以", "又", "可", "当", "要", "什", "得", "更", "许", "比", "呀"],
}

NEW_GROUP_META = {
    "liangci":  ("量词", "一只、一个、几个、一串——量词就在嘴边"),
    "changsuo": ("场所", "家、路、院子——走到哪认到哪"),
    "xuexi":    ("学习文教", "课本、文具、唱歌升旗——上学的词"),
    "dongzuo2": ("动作·拓展", "课标补充的更多动作"),
}

# ---------- 加载现状 ----------
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

ART, CARD = {}, {}
for f in sorted(ROOT.glob("识字卡片_素材_*.py")):
    if f.name == "识字卡片_素材库.py":
        continue
    m = load(f, "mig_" + f.stem)
    for k, v in m.arts().items():
        assert k not in ART, f"插画键重复：{k}"
        ART[k] = v
    for c in m.GROUP_CARDS:
        key = "".join(c["pair"]) if c.get("pair") else (c.get("char") or c.get("key"))
        assert key not in CARD, f"文案键重复：{key}"
        CARD[key] = c

# ---------- 校验目标覆盖 ----------
need = []
for gid, keys in TARGET.items():
    for k in keys:
        kk = "".join(k) if isinstance(k, tuple) else k
        need.append(kk)
missing = [k for k in need if k not in ART or k not in CARD]
assert not missing, f"目标键缺素材/文案：{missing}"
assert len(need) == len(set(need)), "目标键有重复"
# 全库覆盖检查：所有模块卡片键 ∈ 目标 ∪ 基础17组原卡
base_keys = set()
for g in load(ROOT / "识字卡片_字库.py", "zk_chk").GROUPS:
    if g["id"] == "kebiao":
        continue
    for item in g["chars"]:
        k = item["char"] if isinstance(item, dict) else item
        base_keys.add("".join(k) if isinstance(k, tuple) else k)
leftover = [k for k in CARD if k not in need and k not in base_keys]
assert not leftover, f"有卡未归组：{leftover}"
print(f"校验通过：目标 {len(need)} 卡，基础存量 {len(base_keys)} 组键，未归组 {len(leftover)}")

# ---------- 重写字库 GROUPS ----------
zk_spec = importlib.util.spec_from_file_location("zk_mig", str(ROOT / "识字卡片_字库.py"))
zk = load(ROOT / "识字卡片_字库.py", "zk_mig")

def emit_chars(keys):
    """keys: str 或 tuple 列表 → 字库 chars 源码片段"""
    parts = []
    for k in keys:
        if isinstance(k, tuple):
            parts.append(f'("{k[0]}", "{k[1]}")')
        else:
            parts.append(f'"{k}"')
    return parts

new_groups = []
for g in zk.GROUPS:
    if g["id"] == "kebiao":
        continue
    add = TARGET.get(g["id"], [])
    chars = list(g["chars"]) + [k for k in add if not isinstance(k, tuple)] + [k for k in add if isinstance(k, tuple)]
    desc = g["desc"] + "；本组含课标补充字"
    new_groups.append({"id": g["id"], "name": g["name"], "desc": desc, "kind": g["kind"], "chars": chars})

ORDER = ["shuzi", "liangci", "duibi", "fangwei", "tianwen", "ziran", "zhiwu", "dongwu",
         "renti", "rencheng", "shiwu", "wupin", "changsuo", "xuexi", "yanse", "shijian",
         "huiyi", "dongzuo", "dongzuo2", "xingrong", "changyong"]
byid = {g["id"]: g for g in new_groups}
for gid, (name, desc) in NEW_GROUP_META.items():
    keys = TARGET[gid]
    new_groups.append({"id": gid, "name": name, "desc": desc, "kind": "mix", "chars": list(keys)})
new_groups.sort(key=lambda g: ORDER.index(g["id"]))

def ser(obj, indent=0):
    pad = " " * indent
    if isinstance(obj, dict):
        items = []
        for k, v in obj.items():
            items.append(f'"{k}": {ser(v, indent)}')
        return "{ " + ", ".join(items) + " }"
    if isinstance(obj, tuple):
        return "(" + ", ".join(ser(x, indent) for x in obj) + (",)" if len(obj) == 1 else ")")
    if isinstance(obj, list):
        return "[" + ", ".join(ser(x, indent) for x in obj) + "]"
    if isinstance(obj, str):
        return '"' + obj + '"'
    return repr(obj)

groups_lines = []
for g in new_groups:
    lines = [f'    {{ "id": "{g["id"]}", "name": "{g["name"]}", "desc": "{g["desc"]}", "kind": "mix", "chars": [']
    chunks = []
    for c in g["chars"]:
        if isinstance(c, tuple):
            chunks.append(f'("{c[0]}", "{c[1]}")')
        elif isinstance(c, dict):
            chunks.append(ser(c))
        else:
            chunks.append(f'"{c}"')
    # 每行 6 个
    for i in range(0, len(chunks), 6):
        lines.append("        " + ", ".join(chunks[i:i+6]) + ",")
    lines.append("    ]},")
    groups_lines.append("\n".join(lines))

zk_src = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""幼儿识字 422 字字库与分组（2026-10-26 重分类版，21 组）。

来源：统编版语文一年级上册识字表 300 字为主干 + 补充高频字，凑齐 422 字。
2026-10-26 重分类：原"课标补充"大组解散，122 字按主题并入各认知组，
新增 量词 / 场所 / 学习文教 三组；动作组拆为 动作 / 动作·拓展。
分组按识字规律排列，display_order 即卡片连续展示顺序。

结构：
  GROUPS = [ {{"id","name","desc","kind":"mix","chars":[...]}} ]
    - chars 元素：单字字符串 / ("上","下") 对比卡 / {{"char","note"}} 带设计备注
运行本文件会自检：总数 == 422、无重复字。
"""

GROUPS = [
{chr(10).join(groups_lines)}
]


def flatten():
    """返回 [(group_id, group_name, 卡片标识, 说明), ...]。"""
    out = []
    for g in GROUPS:
        for item in g["chars"]:
            key = item["char"] if isinstance(item, dict) else item
            out.append((g["id"], g["name"], key, g["kind"]))
    return out


def all_chars():
    seen = []
    for _, _, key, _ in flatten():
        chars = list(key) if isinstance(key, tuple) else [key]
        seen.extend(chars)
    return seen


if __name__ == "__main__":
    chars = all_chars()
    dups = sorted({{c for c in chars if chars.count(c) > 1}})
    print(f"卡片数：{{len(flatten())}}（单字卡按 1、对比卡按 1 计）")
    print(f"字数：{{len(chars)}}")
    print(f"重复字：{{dups if dups else '无'}}")
    assert len(chars) == 422, f"字数应为 422，实际 {{len(chars)}}"
    assert not dups, f"存在重复字：{{dups}}"
    print("字库校验通过 ✓")
'''
(ROOT / "识字卡片_字库.py").write_text(zk_src, encoding="utf-8")
print("字库已重写：21 组")

# ---------- 生成接收模块的迁移块 & 新组模块 ----------
new_groups = {}
for gid, keys in TARGET.items():
    gname, gdesc = NEW_GROUP_META.get(gid, (None, None))
    cards_src, arts_src = [], []
    for k in keys:
        kk = "".join(k) if isinstance(k, tuple) else k
        c = CARD[kk]
        fields = []
        if c.get("pair"):
            fields.append(f'"pair": {c["pair"]!r}')
        fields.append(f'"key": {kk!r}')
        if "char" in c and not c.get("pair"):
            fields.append(f'"char": {c["char"]!r}')
        for f in ("pinyin", "tone", "sentence", "say", "chat", "life"):
            if f in c:
                fields.append(f'"{f}": {c[f]!r}')
        cards_src.append("{ " + ", ".join(fields) + " }")
        arts_src.append(f'        "{kk}": (\'\'\'{ART[kk]}\'\'\'),')
    if gname:  # 新组 → 全新模块
        mod = (f'#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n'
               f'"""识字卡片插画——{gname}组（{len(keys)}卡）。2026-10-26 重分类迁移，'
               f'插画取自原课标模块的最终版。"""\n\n'
               f'GROUP_CARDS = [\n' + "\n".join("    " + c + "," for c in cards_src) + "\n]\n\n"
               f'def arts():\n    return {{\n' + "\n".join(arts_src) + "\n    }\n\n\n"
               f'if __name__ == "__main__":\n'
               f'    import xml.etree.ElementTree as ET\n'
               f'    assert set(arts()) == {set(k for k in keys)!r}\n'
               f'    for v in arts().values():\n'
               f'        ET.fromstring(f\'<g xmlns="http://www.w3.org/2000/svg">{{v}}</g>\')\n'
               f'    print("自检通过 ✓", len(arts()), "卡")\n')
        (ROOT / f"识字卡片_素材_{gid}.py").write_text(mod, encoding="utf-8")
        print(f"新模块：素材_{gid}.py（{len(keys)}卡）")
    else:  # 并入既有模块
        fp = ROOT / f"识字卡片_素材_{gid}.py"
        t = fp.read_text()
        cards_block = "GROUP_CARDS += [\n" + "\n".join("    " + c + "," for c in cards_src) + "\n]\n"
        keys_src = "\n".join(arts_src)
        marker = "修复合并（来源：识字卡片_修复待确认"
        if marker in t:  # 已有覆盖块：把新键插进该块 return a 之前
            mi = t.find(marker)
            ri = t.find("    return a\n", mi)
            t = t[:ri] + keys_src + "\n" + t[ri:]
            head = "# ---- 2026-10-26 重分类迁移（并入既有覆盖块）----\n"
            t = t[:ri] + head.replace("\n", "") + "\n" + t[ri:]
            print(f"{gid}: {len(keys_src.splitlines())} 键并入既有覆盖块")
        else:
            block = (f'\n\n# ---- 2026-10-26 重分类迁移（识字卡片_重分类方案.md，用户已确认）----\n'
                     f'{cards_block}\n'
                     f'_arts_prev = arts\n'
                     f'def arts():\n'
                     f'    a = dict(_arts_prev())\n{keys_src}\n'
                     f'    return a\n')
            t = t + block
            print(f"{gid}: 追加迁移块 {len(cards_src)} 键")
        fp.write_text(t)

# ---------- 删除 kebiao 四件套 ----------
for gid in ("a", "b", "c", "d"):
    fp = ROOT / f"识字卡片_素材_kebiao_{gid}.py"
    if fp.exists():
        fp.unlink()
        print("deleted", fp.name)
print("迁移完成")
