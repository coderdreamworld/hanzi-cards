#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""拼音字母卡的结构、顺序、插图和音频回归检查。"""
import subprocess
from pathlib import Path

import 拼音卡_构建 as builder
import 拼音卡_素材 as material

ROOT = Path(__file__).resolve().parent

EXPECTED_INITIALS = "b p m f d t n l g k h j q x zh ch sh r z c s".split()
EXPECTED_YW = ["y", "w"]
EXPECTED_FINALS = "a o e i u ü ai ei ui ao ou iu ie üe er an en in un ün ang eng ing ong".split()
EXPECTED_WHOLE = "zhi chi shi ri zi ci si yi wu yu ye yue yuan yin yun ying".split()


def labels(cards: list[dict]) -> list[str]:
    return [card.get("letter") or card.get("sound") or card.get("label") for card in cards]


def audio_duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return float(result.stdout.strip())


def main() -> None:
    deck = material.SETS[0]
    groups = {group["id"]: group for group in deck["groups"]}

    assert labels(groups["initial"]["cards"]) == EXPECTED_INITIALS
    assert labels(groups["spelling"]["cards"]) == EXPECTED_YW
    assert labels(groups["final"]["cards"]) == EXPECTED_FINALS
    assert labels(groups["whole"]["cards"]) == EXPECTED_WHOLE

    expected_full = EXPECTED_INITIALS + EXPECTED_YW + EXPECTED_FINALS + EXPECTED_WHOLE
    assert labels(groups["full"]["cards"]) == expected_full
    assert len(expected_full) == 63
    assert len(groups["tone"]["cards"]) == 5
    assert [card["tone"] for card in groups["tone"]["cards"]] == [1, 2, 3, 4, 0]
    assert all(len(card["words"]) == 3 for card in groups["tone"]["cards"])
    assert len(groups["contrast"]["cards"]) == 7
    assert sum(len(group["cards"]) for group in deck["groups"]) == 138

    _, art_map = builder.base.resolve_deck()
    for group_id in ("initial", "spelling", "final", "whole"):
        for card in groups[group_id]["cards"]:
            label = labels([card])[0]
            if card.get("scene"):
                assert card["scene"] in material.NEW_ARTS, f"缺少插图：{group_id}/{label}"
            elif card.get("ref"):
                assert card["ref"] in art_map, f"缺少引用插图：{group_id}/{label}"
            else:
                raise AssertionError(f"卡片没有插图来源：{group_id}/{label}")

    required_audio = {
        card["audio"]
        for group_id in ("initial", "spelling", "final", "whole", "tone", "contrast")
        for card in groups[group_id]["cards"]
    }
    assert len(required_audio) == 75
    for name in sorted(required_audio):
        path = ROOT / "audio" / f"{name}.m4a"
        assert path.exists(), f"缺少音频：{path.name}"
        assert path.stat().st_size > 2048, f"音频为空或过小：{path.name}"
        assert audio_duration(path) >= 0.12, f"音频过短：{path.name}"

    html = (ROOT / "拼音字母卡.html").read_text(encoding="utf-8")
    assert "__CARDS__" not in html and "__GROUPS__" not in html
    assert "翻到新卡会自动发声" in html
    assert "完整拼音表 63" in html
    assert "声调五类" in html

    # —— 成品 HTML 自身的体检 ——
    # 只查素材不够：曾出现过「正则替换切坏 JSON、n 卡被整张删掉、卡数从 138 掉到 136」
    # 而素材侧完全正常的情况。这里直接从成品 HTML 里解析 CARDS，逐项核对。
    import json
    import re as _re

    raw = html[html.index("const CARDS = ") + len("const CARDS = "):]
    raw = raw.split(";\n", 1)[0]
    page_cards = json.loads(raw)
    assert len(page_cards) == 138, f"成品 HTML 卡数应为 138，实为 {len(page_cards)}"

    def page_label(card):
        return card.get("letter") or card.get("sound") or card.get("label") or card.get("key")

    by_group = {}
    for card in page_cards:
        by_group.setdefault(card.get("g"), []).append(page_label(card))
    assert by_group[0] == EXPECTED_INITIALS, f"成品 HTML 声母顺序不对：{by_group[0]}"
    assert by_group[1] == EXPECTED_YW
    assert by_group[2] == EXPECTED_FINALS
    assert by_group[3] == EXPECTED_WHOLE
    assert len(by_group[4]) == 63
    assert len(by_group[5]) == 5
    assert len(by_group[6]) == 7

    # 每张卡都要有插画，且正文里不能出现 undefined
    for index, card in enumerate(page_cards):
        assert "undefined" not in json.dumps(card, ensure_ascii=False), \
            f"第 {index} 张卡含 undefined"
        if card.get("type") in ("letter", "match", "sound"):
            assert card.get("art"), f"第 {index} 张卡缺插画"
        if card.get("type") == "tone":
            for word in card.get("words", []):
                assert word.get("art"), f"第 {index} 张声调卡例词缺插画"

    # 成品里引用的音频键必须都存在
    page_audio = set()
    for card in page_cards:
        if card.get("audio"):
            page_audio.add(card["audio"])
        elif card.get("letter"):
            page_audio.add("L_" + card["letter"].replace("ü", "v"))
    on_disk = {p.stem for p in (ROOT / "audio").glob("*.m4a")}
    assert not (page_audio - on_disk), f"成品引用的音频不存在：{sorted(page_audio - on_disk)}"

    print("通过：63 张完整表、5 张声调、7 张易混、75 个音频、138 个展示卡位、成品 HTML 数据完整")



if __name__ == "__main__":
    main()
