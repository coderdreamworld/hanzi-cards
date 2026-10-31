#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汉语启蒙卡集构建器。

- 复用上级目录的插画素材库与各组模块（只读，不改动正式识字卡项目）；
- 复用插画写 art_src："组id:字"（识字卡片_素材_<组id>.py 的 arts()）或 "seed:字"（识字卡片_图片/*.svg）；
- 大字字形用 fontTools 从 Songti.ttc 提取矢量轮廓（复用 识字卡片_构建.extract_glyphs）；
- 唯一正式构建入口：python3 汉语启蒙_构建.py
"""
import importlib.util
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # 汉语启蒙卡集/
PARENT = ROOT.parent                            # 孩子/
SEED_DIR = PARENT / "识字卡片_图片"

sys.path.insert(0, str(PARENT))
import 识字卡片_构建 as base  # noqa: E402  只借用 extract_glyphs，不会触发正式构建


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_seed_art(char):
    path = SEED_DIR / f"{char}.svg"
    text = path.read_text(encoding="utf-8")
    inner = re.search(r"<svg[^>]*>(.*)</svg>", text, re.S).group(1)
    inner = inner.replace('id="art"', "").replace('id="monster"', 'id="m-seed"')
    inner = inner.replace('id="hand"', 'id="hand-seed"').replace('href="#hand"', 'href="#hand-seed"')
    return inner.strip(), path


def blend(accent_hex, bg="#fdf8ec", alpha=0.16):
    r = int(accent_hex[1:3], 16)
    g = int(accent_hex[3:5], 16)
    b = int(accent_hex[5:7], 16)
    br, bg_, bb = (int(bg[i:i + 2], 16) for i in (1, 3, 5))
    mix = lambda f, t: round(t * (1 - alpha) + f * alpha)  # noqa: E731
    return f"#{mix(r, br):02x}{mix(g, bg_):02x}{mix(b, bb):02x}"


def check_art(key, svg, from_seed):
    try:
        ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{svg}</g></svg>')
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"插画 {key} 无法解析: {exc}") from exc
    if from_seed:
        return
    for bad in ("<text", "<use", "<defs", "<image", "href"):
        if bad in svg:
            raise ValueError(f"插画 {key} 含禁止标记 {bad}")


def build_set(sucai, template, set_def):
    problems = []
    kind = set_def["kind"]
    # 1) 解析插画
    group_mods = {}
    art_map, seen_keys = {}, set()
    all_cards = []
    for gi, g in enumerate(set_def["groups"]):
        for c in g["cards"]:
            c = dict(c)
            c["g"] = gi
            if c["key"] in seen_keys:
                problems.append(f"{set_def['file']}: 重复卡 key {c['key']}")
            seen_keys.add(c["key"])
            src = c.get("art_src") or c.get("badge", "")
            if src in sucai.NEW_ARTS:
                art_map[c["key"]] = sucai.NEW_ARTS[src]
                check_art(c["key"], art_map[c["key"]], from_seed=False)
            elif ":" in src:
                gid, key = src.split(":", 1)
                if gid == "seed":
                    art, path = load_seed_art(key)
                    art_map[c["key"]] = art
                    check_art(c["key"], art, from_seed=True)
                else:
                    if gid not in group_mods:
                        group_mods[gid] = load_module(PARENT / f"识字卡片_素材_{gid}.py", f"qs_{gid}").arts()
                    if key not in group_mods[gid]:
                        problems.append(f"{set_def['file']}: {c['key']} 引用 {src}，但组内无此插画")
                    else:
                        art_map[c["key"]] = group_mods[gid][key]
                        check_art(c["key"], art_map[c["key"]], from_seed=False)
            else:
                problems.append(f"{set_def['file']}: {c['key']} 没有可用插画 (art_src={src!r})")
            # 内容校验
            if c["type"] == "pic" and len(c.get("story", "")) > 24:
                problems.append(f"{c['key']} story 过长")
            if c["type"] == "verse":
                if len(c["lines"]) > 4:
                    problems.append(f"{c['key']} 超过 4 行")
                if any(len(ln) > 12 for ln in c["lines"]):
                    problems.append(f"{c['key']} 有超过 12 字的句子: {c['lines']}")
            if c["type"] == "magic" and len(c["parts"]) > 3:
                problems.append(f"{c['key']} 部件超过 3 个")
            all_cards.append(c)

    # 2) 字形
    need = set()
    for c in all_cards:
        if c["type"] == "pic":
            need.add(c["char"])
        elif c["type"] == "magic":
            need.update([p[0] for p in c["parts"]] + [c["result"]])
        elif c["type"] == "family":
            need.add(c["radical"])
            need.update(m[0] for m in c["members"])
    glyphs = base.extract_glyphs(sorted(need))

    # 3) 渲染
    html = (template
            .replace("__KIND__", kind)
            .replace("__TITLE__", set_def["title"])
            .replace("__SUB__", set_def["sub"])
            .replace("__ACCENT__", set_def["accent"])
            .replace("__TINT__", blend(set_def["accent"]))
            .replace("__CARDS__", repr_json(all_cards))
            .replace("__GROUPS__", repr_json([{"id": g["id"], "name": g["name"]} for g in set_def["groups"]]))
            .replace("__GLYPHS__", repr_json(glyphs))
            .replace("__ART__", repr_json(art_map)))
    leftover = re.sub(r"__(?:KIND|TITLE|SUB|ACCENT|TINT|CARDS|GROUPS|GLYPHS|ART)__", "", html)
    if "__" in leftover:
        left = [ln.strip()[:80] for ln in leftover.splitlines() if "__" in ln][:3]
        problems.append(f"模板占位符可能有遗漏: {left}")
    if problems:
        raise ValueError("\n".join(problems))
    out = ROOT / set_def["file"]
    out.write_text(html, encoding="utf-8")
    print(f"OK {out.name}  {out.stat().st_size / 1024:.1f} KB  |  {len(all_cards)} 卡  {len(glyphs)} 个字形")
    return out


def repr_json(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def main():
    sucai = load_module(ROOT / "汉语启蒙_素材.py", "qisucai")
    template = (ROOT / "汉语启蒙_模板.html").read_text(encoding="utf-8")
    outs = []
    try:
        for set_def in sucai.SETS:
            outs.append(build_set(sucai, template, set_def))
    except ValueError as exc:
        print("构建失败：")
        for line in str(exc).splitlines():
            print("  " + line)
        sys.exit(1)
    print(f"完成：{len(outs)} 个文件")


if __name__ == "__main__":
    main()
