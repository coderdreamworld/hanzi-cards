#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""识字卡片 · 1000 字全集 构建器。

数据来源：
- 字库1000.py           → 1000 字 31 组（前 402 条目与 422 版一致）
- ../识字卡片_素材_*.py  → legacy 402 卡内容与插画（只读复用，不修改）
- ../识字卡片_图片/*.svg → legacy 种子卡插画（只读复用）
- 素材/素材1000_<gid>*.py → 新 562 卡内容与插画（子代理生产）
- 笔画数据1000.py        → 1000 字笔顺
- 卡片模板.html          → 页面框架（含宽屏三栏版，960px 断点）

用法：
  python3 构建.py              # 正式构建（要求 1000 卡全齐）
  python3 构建.py --partial    # 预览构建（缺卡留空框，输出 /tmp/preview_1000.html）
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
OUT = HERE / "识字卡片_1000字.html"
TEMPLATE = HERE / "卡片模板.html"
sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(HERE))
import 识字卡片_构建 as base  # noqa: E402  借用 extract_glyphs / SEED_CARDS / load_art

SCALE, PAIR_SCALE = base.SCALE, base.PAIR_SCALE


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def legacy_group_modules():
    """{gid: [module,...]} 来自上级目录的 识字卡片_素材_*.py（只读）。"""
    mods = {}
    for f in sorted(PARENT.glob("识字卡片_素材_*.py")):
        if f.name == "识字卡片_素材库.py":
            continue
        baseid = f.stem.replace("识字卡片_素材_", "")
        gid = re.sub(r"_[^_]*$", "", baseid) if "_" in baseid else baseid
        mods.setdefault(gid, []).append(load_module(f, f"lg_{baseid}"))
    return mods


def new_group_modules():
    """{gid: [module,...]} 来自本目录 素材/素材1000_<gid>*.py。"""
    mods = {}
    for f in sorted((HERE / "素材").glob("素材1000_*.py")):
        baseid = f.stem.replace("素材1000_", "")
        gid = re.sub(r"_[^_]*$", "", baseid) if "_" in baseid else baseid
        mods.setdefault(gid, []).append(load_module(f, f"nw_{baseid}"))
    return mods


def norm_key(card):
    if card.get("pair"):
        return tuple(card["pair"])
    return card["char"] if "char" in card else card["key"]


def resolve_deck(partial=False):
    """返回 (groups_out, art_map, missing)。missing=[(gid, 字/对, 原因)]"""
    lg = legacy_group_modules()
    nw = new_group_modules()
    sys.path.insert(0, str(HERE))
    spec = importlib.util.spec_from_file_location("ziku1000", HERE / "字库1000.py")
    ziku = importlib.util.module_from_spec(spec); spec.loader.exec_module(ziku)

    # 字库顺序索引
    zidx = {}
    for g in ziku.GROUPS:
        m = {}
        for i, item in enumerate(g["chars"]):
            key = item["char"] if isinstance(item, dict) else item
            key = tuple(key) if isinstance(key, (list, tuple)) else key
            m[key] = i
        zidx[g["id"]] = m

    groups_out, art_map, missing, seen = [], {}, [], set()
    for g in ziku.GROUPS:
        gid = g["id"]
        cards, mod_arts = [], {}
        for mod in lg.get(gid, []):
            cards += [dict(c) for c in mod.GROUP_CARDS]
        for c in base.SEED_CARDS.get(gid, []):
            cards.append(dict(c))
        for mod in nw.get(gid, []):
            cards += [dict(c) for c in mod.GROUP_CARDS]
        # 先规整 key，再按 legacy 同规则解析插画（种子文件优先，其次模块 arts）
        for c in cards:
            k = norm_key(c)
            if "key" not in c:
                c["key"] = "".join(k) if isinstance(k, tuple) else k
            if not c.get("pair") and "char" not in c:
                c["char"] = c["key"]
            c["pair"] = list(k) if isinstance(k, tuple) else None
            if c["key"] in base.SEED_ART_FILES:
                art_map[c["key"]] = base.load_art(base.SEED_ART_FILES[c["key"]])
        for mod in lg.get(gid, []):
            for k, v in mod.arts().items():
                mod_arts[k] = v
        for mod in nw.get(gid, []):
            for k, v in mod.arts().items():
                mod_arts[k] = v
        for k, v in mod_arts.items():
            if k not in art_map:
                art_map[k] = v
        # 校验
        for c in cards:
            label = c["key"]
            k = norm_key(c)
            if k in seen:
                missing.append((gid, label, "重复卡"))
            seen.add(k)
            if label not in art_map:
                missing.append((gid, label, "缺插画"))
                art_map[label] = ""
            for fld in ("pinyin", "tone", "sentence", "say", "chat", "life"):
                if not c.get(fld):
                    missing.append((gid, label, f"缺{fld}"))
        have = {norm_key(c) for c in cards}
        for k in zidx[gid]:
            if k not in have:
                label = "".join(k) if isinstance(k, tuple) else k
                missing.append((gid, label, "缺卡"))
        extra = [norm_key(c) for c in cards if norm_key(c) not in zidx[gid]]
        for k in extra:
            label = "".join(k) if isinstance(k, tuple) else k
            missing.append((gid, label, "多余卡（不在字库）"))
        cards.sort(key=lambda c: zidx[gid][norm_key(c)])
        groups_out.append({"id": gid, "name": g["name"], "desc": g.get("desc", ""), "cards": cards})

    total = sum(len(c["pair"]) if c["pair"] else 1 for g in groups_out for c in g["cards"])
    if not partial:
        hard = [m for m in missing if m[2] not in ("缺卡",)]
        if missing:
            raise ValueError(f"共 {len(missing)} 个问题（卡 {sum(len(g['cards']) for g in groups_out)}，字 {total}）:\n" +
                             "\n".join(f"  [{gid}] {label}: {why}" for gid, label, why in missing[:80]))
        assert total == 1000, f"总字数 {total} != 1000"
    return groups_out, art_map, missing


def render_document(groups_out, art_map):
    all_keys = [c["key"] for g in groups_out for c in g["cards"]]
    glyphs = base.extract_glyphs(sorted({ch for c in all_keys for ch in c}))
    flat_cards = []
    for gi, g in enumerate(groups_out):
        for c in g["cards"]:
            flat_cards.append({**c, "g": gi})
    template = TEMPLATE.read_text(encoding="utf-8")
    strokes_mod = load_module(HERE / "笔画数据1000.py", "strokes1000")
    return (template
            .replace("__CARDS__", json.dumps(flat_cards, ensure_ascii=False))
            .replace("__GROUPS__", json.dumps([{"id": g["id"], "name": g["name"]} for g in groups_out], ensure_ascii=False))
            .replace("__GLYPHS__", json.dumps(glyphs, ensure_ascii=False))
            .replace("__SCALE__", str(SCALE))
            .replace("__PAIR_SCALE__", str(PAIR_SCALE))
            .replace("__ART__", json.dumps(art_map, ensure_ascii=False))
            .replace("__STROKES__", strokes_mod.STROKES_JSON))


def build(partial=False):
    groups_out, art_map, missing = resolve_deck(partial=partial)
    html = render_document(groups_out, art_map)
    if partial:
        import os
        out = Path(f"/tmp/preview_1000_{os.getpid()}.html")
    else:
        out = OUT
        if not missing:
            pass
    tmp = out.with_suffix(out.suffix + ".tmp")
    tmp.write_text(html, encoding="utf-8")
    tmp.replace(out)
    n_cards = sum(len(g["cards"]) for g in groups_out)
    n_chars = sum(len(c["pair"]) if c["pair"] else 1 for g in groups_out for c in g["cards"])
    print(f"{'预览' if partial else 'OK'} {out}  {out.stat().st_size/1024:.1f} KB | {len(groups_out)} 组 {n_cards} 卡 {n_chars} 字 | 缺口 {len(missing)}")


if __name__ == "__main__":
    build(partial="--partial" in sys.argv)
