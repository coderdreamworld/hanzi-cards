#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 · QA 截图（只写 /tmp，不碰项目文件）。

用法：
  python3 tools_qa截图.py --grid              # 全部卡网格总览（/tmp/en_grid.png）
  python3 tools_qa截图.py --n 3               # 第 3 张整卡（/tmp/en_n3.png）
  python3 tools_qa截图.py --mobile 3          # 第 3 张手机 deck 视图
  python3 tools_qa截图.py --desk 3            # 第 3 张桌面三栏视图
  python3 tools_qa截图.py --word cat          # 按词截图
"""
import contextlib
import io
import os
import random
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from 构建 import build, resolve_deck  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def preview_path():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        build(partial=True)
    return buf.getvalue().split()[1]


def shot(url, out, w, h, budget=6000):
    prof = f"/tmp/enqa_{os.getpid()}_{random.randint(1000, 9999)}"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                    f"--virtual-time-budget={budget}", f"--user-data-dir={prof}",
                    f"--window-size={w},{h}", f"--screenshot={out}", url],
                   capture_output=True)
    shutil.rmtree(prof, ignore_errors=True)
    print(out)


def main():
    args = sys.argv[1:]
    preview = preview_path()
    flat = [(g["id"], c["w"]) for g in resolve_deck(partial=True)[0] for c in g["cards"]]
    if "--grid" in args:
        n = len(flat)
        h = min(16000, 520 * (n // 3 + 1) + 260)
        shot(f"file://{preview}?grid", "/tmp/en_grid.png", 1240, h, budget=9000)
    if "--gridgroup" in args:
        i = args.index("--gridgroup")
        gid = args[i + 1]
        gn = sum(1 for g, k in flat if g == gid)
        h = min(16000, 520 * (gn // 3 + 1) + 260)
        shot(f"file://{preview}?grid&group={gid}", f"/tmp/en_grid_{gid}.png", 1240, h, budget=9000)
    for flag, w, h, tag in (("--n", 900, 1180, "n"), ("--mobile", 390, 844, "m"), ("--desk", 1440, 900, "d")):
        if flag in args:
            i = args.index(flag)
            for nn in args[i + 1:i + 2] if len(args) > i + 1 else []:
                if not nn.isdigit():
                    continue
                url_param = f"n={nn}" if flag == "--n" else f"i={nn}"
                shot(f"file://{preview}?{url_param}", f"/tmp/en_{tag}{nn}.png", w, h)
    if "--word" in args:
        i = args.index("--word")
        w = args[i + 1]
        hits = [(g, k) for (g, k) in flat if k == w]
        assert len(hits) == 1, f"{w} 命中 {hits}"
        n = flat.index(hits[0]) + 1
        shot(f"file://{preview}?n={n}", f"/tmp/en_w_{w}.png", 900, 1180)


if __name__ == "__main__":
    main()
