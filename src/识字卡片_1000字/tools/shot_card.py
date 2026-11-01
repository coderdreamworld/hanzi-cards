#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""单卡截图（改卡后自检用）。
用法: python3 tools/shot_card.py <字> [<字>...]   → /tmp/shot_<组>_<字>.png（整卡 900x1180）
只写 /tmp，不碰项目文件。"""
import io, json, os, random, shutil, subprocess, sys, contextlib
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from 构建 import build, resolve_deck

groups, _, _ = resolve_deck(partial=True)
flat = [(g["id"], c["key"]) for g in groups for c in g["cards"]]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    build(partial=True)
preview = buf.getvalue().split()[1]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
prof = f"/tmp/sc_{os.getpid()}_{random.randint(1000,9999)}"
for ch in sys.argv[1:]:
    hits = [(g, k) for (g, k) in flat if k == ch]
    assert len(hits) == 1, f"{ch} 命中 {len(hits)} 张: {hits}"
    g, k = hits[0]
    n = flat.index((g, k)) + 1
    out = f"/tmp/shot_{g}_{k}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=6000",
                    f"--user-data-dir={prof}", "--window-size=900,1180",
                    f"--screenshot={out}", f"file://{preview}?n={n}"], capture_output=True)
    print(out)
try:
    shutil.rmtree(prof)
except Exception:
    pass
