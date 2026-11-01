#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把新插画导成一张对照图（HTML → Chrome headless 截图），用于逐张目检。

用法：python3 扩充/新插画对照.py
输出：/tmp/artsheet.html 与 /tmp/artsheet.png
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # 汉语启蒙卡集/
OUT_HTML = Path("/tmp/artsheet.html")
OUT_PNG = Path("/tmp/artsheet.png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DECKS = [
    ("汉语启蒙_会意字卡.html", "会意字", ["好", "双", "品", "掰", "灶", "岩", "晶", "朋", "出", "男"]),
    ("汉语启蒙_部首家族卡.html", "部首徽章",
     ["族虫", "族讠", "族忄", "族犭", "族月", "族火", "族辶", "族米", "族钅"]),
    ("汉语启蒙_韵语与声音卡.html", "韵语与游戏",
     ["小白兔白又白", "晚上星星亮晶晶", "雨过天晴出彩虹", "小火车开进城",
      "小书本有儿歌", "小母鸡下蛋蛋",
      "听音找东西", "词语接一接", "轻声轻轻读", "舌头打卷"]),
]


def extract(html, var):
    m = re.search(rf"const {var} = (\[.*?\]|\{{.*?\}});\n", html, re.S)
    if not m:
        raise SystemExit(f"找不到 const {var}")
    return json.loads(m.group(1))


def main():
    cells = []
    for fname, deck, keys in DECKS:
        html = (ROOT / fname).read_text(encoding="utf-8")
        art = extract(html, "ART")
        cards = {c["key"]: c for c in extract(html, "CARDS")}
        for k in keys:
            if k not in art:
                print(f"⚠ {deck}/{k} 没有插画")
                continue
            label = k
            c = cards.get(k, {})
            if c.get("result"):
                label = f"{k}（{c.get('story','')}）"
            elif c.get("radical"):
                label = f"{c['radical']} 部 · {c.get('meaning','')}"
            elif c.get("title"):
                label = c["title"]
            cells.append((f"{deck}·{label}",
                          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480">'
                          + art[k] + "</svg>"))
    body = []
    for i, (label, svg) in enumerate(cells):
        body.append(f'<figure><div class="box">{svg}</div><figcaption>{i+1}. {label}</figcaption></figure>')
    doc = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;padding:14px;background:#f4efe3;font:13px/1.5 "PingFang SC",sans-serif}}
h1{{font-size:16px;margin:0 0 12px}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
figure{{margin:0;background:#fff;border:1px solid #d8cfbb;border-radius:8px;padding:8px}}
.box{{aspect-ratio:760/480;background:#fdf8ec;border-radius:6px;overflow:hidden}}
.box svg{{width:100%;height:100%;display:block}}
figcaption{{margin-top:6px;color:#333;font-size:12px}}
</style><h1>新插画对照表（{len(cells)} 张）</h1><div class="g">{''.join(body)}</div>"""
    OUT_HTML.write_text(doc, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--no-first-run", "--disable-gpu",
                    "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--screenshot={OUT_PNG}", "--window-size=1500,2400",
                    f"file://{OUT_HTML}"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{len(cells)} 张 → {OUT_PNG}")


if __name__ == "__main__":
    main()
