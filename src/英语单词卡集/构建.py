#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡构建：锁定词库、逐卡插画和离线音频三者一致才交付。

python3 构建.py             正式构建 500 词条
python3 构建.py --partial   只预览已经落盘的卡，输出本目录预览_en.html
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "english-words.html"
TEMPLATE = HERE / "卡片模板_en.html"
VER = "20261104b"


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_ciku():
    return load_module(HERE / "词库500.py", "ciku500")


def group_modules():
    mods = {}
    for f in sorted((HERE / "素材").glob("素材_en_*.py")):
        gid = re.sub(r"_\d+$", "", f.stem.removeprefix("素材_en_"))
        mods.setdefault(gid, []).append(load_module(f, "en_" + f.stem))
    return mods


def audio_slug(word):
    return word.lower().replace(" ", "-")


def validate_art(art):
    if not isinstance(art, str) or not art.strip():
        return ["缺插画"]
    try:
        root = ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg">' + art + '</svg>')
    except ET.ParseError as exc:
        return [f"插画 XML 解析失败: {exc}"]
    allowed = {"svg", "g", "path", "rect", "ellipse", "circle", "line", "polygon", "polyline"}
    problems = []
    for el in root.iter():
        tag = el.tag.rsplit("}", 1)[-1]
        if tag not in allowed or (el is not root and tag == "svg"):
            problems.append(f"插画含禁止标签 {tag}")
        for attr, value in el.attrib.items():
            if attr.lower().startswith("on") or "url(" in value or attr in {"href", "style", "filter"}:
                problems.append(f"插画含禁止属性 {attr}")
    # 几何边界在实际渲染层检查。局部坐标含 translate/rotate/scale，不能直接作画布坐标。
    return problems


def resolve_deck(partial=False):
    ciku, mods = load_ciku(), group_modules()
    manifest_path = HERE / "audio" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    groups_out, art_map, aud, problems = [], {}, {}, []
    words = [w["w"] for g in ciku.GROUPS for w in g["words"]]
    if len(words) != 500 or len(set(w.casefold() for w in words)) != 500:
        problems.append(("词库", "", "词库须恰好500个不重复词条"))
    known = {g["id"] for g in ciku.GROUPS}
    for gid in set(mods) - known:
        problems.append((gid, "", "未知组素材"))
    for g in ciku.GROUPS:
        gid = g["id"]
        wanted = {w["w"]: w for w in g["words"]}
        cards, arts = [], {}
        for mod in mods.get(gid, []):
            entries, drawings = list(mod.GROUP_CARDS), mod.arts()
            keys = [c["w"] for c in entries]
            if set(keys) != set(drawings):
                problems.append((gid, "", "模块词条与插画键不一致"))
            cards.extend(dict(c) for c in entries)
            for key, svg in drawings.items():
                if key in arts:
                    problems.append((gid, key, "重复插画"))
                arts[key] = svg
        counts = collections.Counter(c["w"] for c in cards)
        for w, count in counts.items():
            if count != 1:
                problems.append((gid, w, "重复词条"))
        for w in set(arts) - set(wanted):
            problems.append((gid, w, "多余插画"))
        card_map = {c["w"]: c for c in cards}
        for w in card_map.keys() - wanted.keys():
            problems.append((gid, w, "多余词条"))
        ordered = []
        for w, item in wanted.items():
            if w not in card_map:
                problems.append((gid, w, "缺词条"))
            elif card_map[w].get("cn") != item["cn"]:
                problems.append((gid, w, "中文释义与锁定词库不一致"))
            svg = arts.get(w, "")
            for problem in validate_art(svg):
                problems.append((gid, w, problem))
            if w in card_map and svg:
                ordered.append({"w": w, "cn": item["cn"]})
                art_map[w] = svg
                aud[w] = manifest.get(w, {})
                for kind in ("w", "s"):
                    path = HERE / "audio" / f"en_{audio_slug(w)}_{kind}.m4a"
                    meta = aud[w].get(kind, {})
                    if not path.is_file() or path.stat().st_size < 512 or meta.get("dur", 0) <= 0:
                        problems.append((gid, w, f"缺{kind}音频或时长信息"))
        if ordered or not partial:
            groups_out.append({"id": gid, "name": g["name"], "en": g.get("en", ""), "cards": ordered})
    hard = [p for p in problems if p[2] not in {"缺词条", "缺插画"}]
    if hard or (problems and not partial):
        failures = hard if partial else problems
        raise ValueError("构建失败:\n" + "\n".join(f"[{g}] {w}: {why}" for g, w, why in failures[:80]))
    return groups_out, art_map, aud, problems


def js_json(value):
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def build(partial=False):
    groups, art, aud, problems = resolve_deck(partial=partial)
    cards = [{**c, "g": gi, "key": c["w"]} for gi, g in enumerate(groups) for c in g["cards"]]
    html = TEMPLATE.read_text(encoding="utf-8")
    values = {
        "__CARDS__": js_json(cards),
        "__GROUPS__": js_json([{k: v for k, v in g.items() if k != "cards"} for g in groups]),
        "__ART__": js_json(art),
        "__AUD__": js_json(aud),
        "__VER__": VER,
    }
    for placeholder, value in values.items():
        html = html.replace(placeholder, value)
    out = HERE / "预览_en.html" if partial else OUT
    temporary = out.with_suffix(".html.tmp")
    temporary.write_text(html, encoding="utf-8")
    temporary.replace(out)
    print(f"{'预览' if partial else 'OK'} {out} | {len(groups)}组 {len(cards)}词条 | 待补{len(problems)}项")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--partial", action="store_true")
    build(partial=parser.parse_args().partial)
