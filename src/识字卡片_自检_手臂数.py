#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""肤色肢体结构诊断。

这不是“看懂人体”的替代品：折臂会由多段 path/line 构成，纯计数只能筛出候选。
脚本负责三件可可靠自动化的事：扫描最终 402 卡、验证 SVG 可解析、守住已修卡
的头数/肤色肢体段数回归；候选清单必须配合目标卡预览人工复核。
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import 识字卡片_构建 as builder


ROOT = Path(__file__).resolve().parent
SKIN = {"#f8cba4", "#eeb28a", "#f7c49c"}
EXPECTED_TOTAL = 402

# 这些卡曾出现多臂、长臂或器具误读；固定最终结构签名，防止同类问题回归。
REGRESSIONS = {
    "爸": (2, 4),
    "医": (1, 2),
    "飞": (1, 2),
    "不": (1, 2),
    "的": (1, 2),
    "来": (2, 4),
    "放": (1, 2),
    "举": (1, 2),
    "孩": (0, 0),
}


def color(tag, attribute):
    match = re.search(rf'{attribute}="(#[0-9a-fA-F]{{6}})"', tag)
    return match.group(1).lower() if match else None


def scan(svg):
    """返回（肤色大头圆数，肤色线/路径段数）。"""
    heads = 0
    for tag in re.findall(r"<circle\b[^>]*>", svg):
        radius = re.search(r'r="([\d.]+)"', tag)
        if color(tag, "fill") in SKIN and radius and float(radius.group(1)) >= 30:
            heads += 1
    segments = 0
    for tag in re.findall(r"<(?:line|path)\b[^>]*>", svg):
        if color(tag, "stroke") in SKIN:
            segments += 1
    return heads, segments


def main():
    groups, art_map = builder.resolve_deck()
    ordered = [(group["name"], card["key"]) for group in groups for card in group["cards"]]
    failures = []
    if len(ordered) != EXPECTED_TOTAL:
        failures.append(f"应扫描 {EXPECTED_TOTAL} 卡，实际 {len(ordered)} 卡")

    rows = []
    candidates = []
    for group_name, key in ordered:
        svg = art_map[key]
        try:
            ET.fromstring(f'<g xmlns="http://www.w3.org/2000/svg">{svg}</g>')
        except ET.ParseError as exc:
            failures.append(f"[{group_name}] {key} SVG 无法解析：{exc}")
            continue
        heads, segments = scan(svg)
        rows.append((group_name, key, heads, segments))
        if heads and segments > 2 * heads:
            candidates.append((group_name, key, heads, segments))

    by_key = {key: (heads, segments) for _group, key, heads, segments in rows}
    for key, expected in REGRESSIONS.items():
        actual = by_key.get(key)
        if actual != expected:
            failures.append(f"回归卡 {key}：预期 {expected[0]} 头/{expected[1]} 段，实际 {actual}")

    report = ROOT / "识字卡片_修复待确认" / "手臂数扫描.txt"
    with report.open("w", encoding="utf-8") as handle:
        handle.write("组\t卡片\t肤色大头圆\t肤色线/路径段\n")
        for row in rows:
            handle.write("\t".join(map(str, row)) + "\n")

    print(f"扫描 {len(rows)} 卡；SVG 全部可解析" if not failures else f"扫描 {len(rows)} 卡")
    if candidates:
        print(f"结构候选 {len(candidates)} 张（分段手臂也会入选，需看预览复核）：")
        for group_name, key, heads, segments in candidates:
            print(f"  [{group_name}] {key}：{heads} 头 / {segments} 肤色段")
    else:
        print("没有肤色段数超出 2×头数的候选")
    print(f"明细：{report.name}")

    if failures:
        print(f"硬性失败 {len(failures)} 项：", file=sys.stderr)
        for failure in failures:
            print("  " + failure, file=sys.stderr)
        raise SystemExit(1)
    print(f"{len(REGRESSIONS)} 张高风险卡结构回归通过 ✓")


if __name__ == "__main__":
    main()
