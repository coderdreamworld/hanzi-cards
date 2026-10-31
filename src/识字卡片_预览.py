#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把最终解析后的插画渲染成带字标签的对照长图。

用法：
  python3 识字卡片_预览.py rencheng dongzuo
  python3 识字卡片_预览.py --keys 爸 医 飞 老 不

输出位于 /tmp；每行 3 张，内容与正式构建器使用同一解析入口。
"""

import argparse
import html
import subprocess
from pathlib import Path

import 识字卡片_构建 as builder


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render(name, cards, art_map):
    boxes = []
    for card in cards:
        key = card["key"]
        boxes.append(
            '<div style="display:inline-block;margin:12px;border:3px solid #e8d9a0;'
            'border-radius:18px;overflow:hidden;vertical-align:top">'
            '<div style="width:100%;text-align:center;font-size:46px;padding:16px 0;'
            'background:#fdf3c9;color:#4a3226">' + html.escape(key) + "</div>"
            '<svg viewBox="0 0 760 480" style="width:560px;background:#fdf8ec;display:block">'
            + art_map[key] + "</svg></div>"
        )
    document = (
        '<!doctype html><meta charset="utf-8">'
        '<body style="margin:0;background:#fff;font-family:sans-serif">'
        + "".join(boxes) + "</body>"
    )
    out = Path(f"/tmp/preview_{name}.html")
    out.write_text(document, encoding="utf-8")
    rows = -(-len(cards) // 3)
    height = rows * 465 + 30
    png = Path(f"/tmp/preview_{name}.png")
    subprocess.run(
        [
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--window-size=1830,{height}", f"--screenshot={png}", f"file://{out}",
        ],
        check=True,
    )
    print(f"{name}: {len(cards)} 张 → {png}（{rows} 行）")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("groups", nargs="*", help="字库中的组 id")
    parser.add_argument("--keys", nargs="+", help="只预览指定卡片 key，可用空格或逗号分隔")
    args = parser.parse_args()
    if not args.groups and not args.keys:
        parser.error("请提供至少一个组 id，或使用 --keys 指定卡片")

    groups, art_map = builder.resolve_deck()
    by_group = {group["id"]: group for group in groups}
    all_cards = {card["key"]: card for group in groups for card in group["cards"]}

    if args.keys:
        keys = [part for item in args.keys for part in item.split(",") if part]
        unknown = [key for key in keys if key not in all_cards]
        if unknown:
            raise SystemExit("不存在的卡片：" + "、".join(unknown))
        render("keys", [all_cards[key] for key in keys], art_map)

    unknown_groups = [gid for gid in args.groups if gid not in by_group]
    if unknown_groups:
        raise SystemExit("不存在的组：" + "、".join(unknown_groups))
    for gid in args.groups:
        render(gid, by_group[gid]["cards"], art_map)


if __name__ == "__main__":
    main()
