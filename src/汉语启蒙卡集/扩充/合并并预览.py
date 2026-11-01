#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并三个子集的扩充数据 → 解析插画 → 渲染 PNG 对照图（不覆盖正式产物）。

用法：
    python3 扩充/合并并预览.py                 # 合并 + 渲染全部四套
    python3 扩充/合并并预览.py --only huiyi    # 只渲染某一套
    python3 扩充/合并并预览.py --no-merge      # 只渲染现有正式数据

扩充数据来自本目录下的：
    会意字_扩充数据.py    → NEW_CARDS / NEW_ARTS
    部首家族_扩充数据.py  → NEW_CARDS / NEW_ARTS
    韵语声音_扩充数据.py  → NEW_VERSES / NEW_GAMES / NEW_ARTS
"""
import argparse
import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent      # 汉语启蒙卡集/
PARENT = ROOT.parent                                # 孩子/
HERE = ROOT / "扩充"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(ROOT))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def resolve_art(cards, new_arts):
    """镜像 汉语启蒙_构建.build_set 的插画解析口径。返回 (art_map, problems)。"""
    art_map, problems = {}, []
    legacy_cache, new_cache = {}, {}

    def legacy_arts(gid):
        if gid not in legacy_cache:
            p = PARENT / f"识字卡片_素材_{gid}.py"
            if not p.exists():
                legacy_cache[gid] = None
            else:
                legacy_cache[gid] = load(p, f"pv_{gid}").arts()
        return legacy_cache[gid]

    def new1000_arts(gid):
        if gid not in new_cache:
            merged = {}
            for f in sorted((PARENT / "识字卡片_1000字" / "素材").glob(f"素材1000_{gid}*.py")):
                merged.update(load(f, f"pv1000_{f.stem}").arts())
            new_cache[gid] = merged
        return new_cache[gid]

    def seed_art(ch):
        p = PARENT / "识字卡片_图片" / f"{ch}.svg"
        text = p.read_text(encoding="utf-8")
        inner = re.search(r"<svg[^>]*>(.*)</svg>", text, re.S).group(1)
        inner = inner.replace('id="art"', "").replace('id="monster"', 'id="m-seed"')
        inner = inner.replace('id="hand"', 'id="hand-seed"').replace('href="#hand"', 'href="#hand-seed"')
        return inner.strip()

    for c in cards:
        src = c.get("art_src") or c.get("badge") or ""
        if src in new_arts:
            art_map[c["key"]] = new_arts[src]
        elif ":" in src:
            head, rest = src.split(":", 1)
            if head == "seed":
                try:
                    art_map[c["key"]] = seed_art(rest)
                except Exception as exc:
                    problems.append(f"{c['key']}: seed 读取失败 {exc}")
            elif head == "1000":
                gid, key = rest.split(":", 1)
                arts = new1000_arts(gid)
                if key not in arts:
                    problems.append(f"{c['key']}: 1000:{gid} 里没有「{key}」")
                else:
                    art_map[c["key"]] = arts[key]
            else:
                arts = legacy_arts(head)
                if arts is None:
                    problems.append(f"{c['key']}: 找不到模块 识字卡片_素材_{head}.py")
                elif rest not in arts:
                    problems.append(f"{c['key']}: 组 {head} 里没有「{rest}」")
                else:
                    art_map[c["key"]] = arts[rest]
        else:
            problems.append(f"{c['key']}: art_src 无法解析 {src!r}")
    return art_map, problems


def merge(sucai):
    """把三个扩充数据文件并进 SETS（内存态，不落盘）。"""
    added = {}
    for fname, attr in (("会意字_扩充数据.py", "huiyi"),
                        ("部首家族_扩充数据.py", "jiazu"),
                        ("韵语声音_扩充数据.py", "shengyin")):
        path = HERE / fname
        if not path.exists():
            print(f"（跳过 {fname}：尚未生成）")
            continue
        mod = load(path, f"ext_{attr}")
        arts = dict(getattr(mod, "NEW_ARTS", {}) or {})
        sucai.ARTS.update(arts)
        sucai.NEW_ARTS.update(arts)
        cards = list(getattr(mod, "NEW_CARDS", []) or [])
        if attr == "huiyi":
            sucai.SET_HUIYI["groups"][0]["cards"] += cards
        elif attr == "jiazu":
            sucai.SET_JIAZU["groups"][0]["cards"] += cards
        else:
            verses = list(getattr(mod, "NEW_VERSES", []) or [])
            games = list(getattr(mod, "NEW_GAMES", []) or [])
            sucai.SET_SHENGYIN["groups"][0]["cards"] += verses
            sucai.SET_SHENGYIN["groups"][1]["cards"] += games
        added[attr] = (len(cards), len(verses) if attr == "shengyin" else 0,
                       len(games) if attr == "shengyin" else 0, len(arts))
    return added


def render(name, cards, art_map, label):
    boxes = []
    for card in cards:
        key = card["key"]
        art = art_map.get(key)
        if art is None:
            art = '<text x="380" y="240" font-size="40" fill="#c00">缺插画</text>'
        cap = key
        if card.get("type") == "magic":
            cap = card.get("result", key)
        elif card.get("type") == "family":
            cap = card.get("radical", key) + " " + card.get("name", "")
        boxes.append(
            '<div style="display:inline-block;margin:10px;border:3px solid #e8d9a0;'
            'border-radius:18px;overflow:hidden;vertical-align:top">'
            '<div style="text-align:center;font-size:36px;padding:10px 0;'
            'background:#fdf3c9;color:#4a3226">' + html.escape(cap) + "</div>"
            '<svg viewBox="0 0 760 480" style="width:520px;background:#fdf8ec;display:block">'
            + art + "</svg></div>"
        )
    doc = ('<!doctype html><meta charset="utf-8">'
           '<body style="margin:0;background:#fff;font-family:sans-serif">'
           + "".join(boxes) + "</body>")
    out = Path(f"/tmp/qh_{name}.html")
    out.write_text(doc, encoding="utf-8")
    rows = max(1, -(-len(cards) // 3))
    height = rows * 400 + 30
    png = Path(f"/tmp/qh_{name}.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size=1650,{height}", f"--screenshot={png}",
                    f"file://{out}"], check=True, stderr=subprocess.DEVNULL)
    print(f"  {name}: {len(cards)} 张 → {png}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--no-merge", action="store_true")
    args = ap.parse_args()

    sucai = load(ROOT / "汉语启蒙_素材.py", "qisucai")
    if not args.no_merge:
        added = merge(sucai)
        for k, v in added.items():
            print(f"合并 {k}: 卡 {v[0]} / 韵语 {v[1]} / 游戏 {v[2]} / 新插画 {v[3]}")

    plan = [("huiyi", sucai.SET_HUIYI, "会意字"), ("jiazu", sucai.SET_JIAZU, "部首家族"),
            ("shengyin", sucai.SET_SHENGYIN, "韵语声音")]
    all_problems = []
    for name, sd, label in plan:
        if args.only and args.only != name:
            continue
        cards = [c for g in sd["groups"] for c in g["cards"]]
        art_map, problems = resolve_art(cards, sucai.NEW_ARTS)
        all_problems += problems
        print(f"[{label}] {len(cards)} 张，插画缺失 {len(problems)}")
        for p in problems:
            print("   !", p)
        render(name, cards, art_map, label)
    if all_problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
