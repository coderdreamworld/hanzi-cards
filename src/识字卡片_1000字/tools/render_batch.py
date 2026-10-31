#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染指定组的卡片网格预览图（供生产/审卡代理看图）。
用法: python3 tools/render_batch.py <gid> [<gid>...]   → /tmp/batch_<gid>.png（每片≤4行）"""
import math, subprocess, sys, os, random
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def count_cards(gid):
    import importlib.util
    sys.path.insert(0, str(HERE))
    from 构建 import resolve_deck
    groups, _, _ = resolve_deck(partial=True)
    for g in groups:
        if g["id"] == gid:
            return len(g["cards"])
    return 0

def ensure_preview():
    import os
    from 构建 import build
    build(partial=True)
    return f"/tmp/preview_1000_{os.getpid()}.html"

def render(gid):
    n = count_cards(gid)
    if n == 0:
        print(f"[{gid}] 没有可渲染的卡（该组新卡尚未生产）"); return
    rows = math.ceil(n / 3)
    preview = ensure_preview()
    url = f"file://{preview}?grid&group={gid}"
    prof = f"/tmp/rb_{random.randint(1000,9999)}"
    out = f"/tmp/batch_{gid}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=8000",
                    f"--user-data-dir={prof}", f"--window-size=1240,{min(rows*470+140, 14000)}",
                    f"--screenshot={out}", url], capture_output=True)
    try: os.system(f"rm -rf {prof}")
    except Exception: pass
    print(f"[{gid}] {n} 卡 → {out}")

if __name__ == "__main__":
    for gid in sys.argv[1:]:
        render(gid)
