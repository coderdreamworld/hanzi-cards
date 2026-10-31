#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成拼音卡课堂呼读音；全部离线预生成，不依赖浏览器 TTS。"""
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio"
SWIFT_HELPER = ROOT / "生成标准呼读音.swift"

# 文本只是给语音引擎定位字词；真正的读音由 IPA 指定。这样 f、d、t、r 等不会
# 被“飞、东、天、日”的词义读音带偏，而是统一读成一声的课堂呼读音。
READINGS = {
    "a": "阿", "o": "喔", "e": "鹅", "i": "衣", "u": "乌", "v": "迂",
    "b": "玻", "p": "坡", "m": "摸", "f": "佛", "d": "得", "t": "特",
    "n": "讷", "l": "勒", "g": "哥", "k": "科", "h": "喝", "j": "基",
    "q": "欺", "x": "希", "zh": "知", "ch": "蚩", "sh": "诗", "r": "日",
    "z": "资", "c": "雌", "s": "思", "y": "衣", "w": "乌",
    "ai": "哀", "ei": "诶", "ui": "威", "ao": "凹", "ou": "欧", "iu": "优",
    "ie": "耶", "ve": "约", "er": "儿", "an": "安", "en": "恩", "in": "因",
    "un": "温", "vn": "晕", "ang": "肮", "eng": "灯", "ing": "英", "ong": "翁",
    "zhi": "知", "chi": "吃", "shi": "诗", "ri": "日", "zi": "资", "ci": "雌",
    "si": "丝", "yi": "衣", "wu": "乌", "yu": "迂", "ye": "耶", "yue": "约",
    "yuan": "冤", "yin": "因", "yun": "晕", "ying": "英",
}

# 采用常见普通话宽式 IPA；˥ 表示一声的高平调。声母卡播放的是课堂呼读音，
# 不是英文字母名，也不是任意找一个同声母的汉字。
IPA_READINGS = {
    "a": "a˥", "o": "o˥", "e": "ɤ˥", "i": "i˥", "u": "u˥", "v": "y˥",
    "b": "pu̯o˥", "p": "pʰu̯o˥", "m": "mu̯o˥", "f": "fu̯o˥",
    "d": "tɤ˥", "t": "tʰɤ˥", "n": "nɤ˥", "l": "lɤ˥",
    "g": "kɤ˥", "k": "kʰɤ˥", "h": "xɤ˥",
    "j": "tɕi˥", "q": "tɕʰi˥", "x": "ɕi˥",
    "zh": "ʈʂɨ˥", "ch": "ʈʂʰɨ˥", "sh": "ʂɨ˥", "r": "ʐi˥",
    "z": "tsɨ˥", "c": "tsʰɨ˥", "s": "sɨ˥",
    "y": "i˥", "w": "u˥",
    "ai": "aɪ˥", "ei": "eɪ˥", "ui": "u̯eɪ˥", "ao": "ɑʊ˥", "ou": "oʊ˥",
    "iu": "i̯oʊ˥", "ie": "i̯ɛ˥", "ve": "ɥɛ˥", "er": "ɤɻ˥",
    "an": "an˥", "en": "ən˥", "in": "in˥", "un": "uən˥", "vn": "yn˥",
    "ang": "ɑŋ˥", "eng": "ɤŋ˥", "ing": "iŋ˥", "ong": "uŋ˥",
    "zhi": "ʈʂɨ˥", "chi": "ʈʂʰɨ˥", "shi": "ʂɨ˥", "ri": "ʐi˥",
    "zi": "tsɨ˥", "ci": "tsʰɨ˥", "si": "sɨ˥",
    "yi": "i˥", "wu": "u˥", "yu": "y˥", "ye": "jɛ˥", "yue": "ɥɛ˥",
    "yuan": "ɥɛn˥", "yin": "in˥", "yun": "yn˥", "ying": "iŋ˥",
}

TONE_NARRATIONS = {
    "TONE_1": "第一声，高高平平。妈，衣，乌。",
    "TONE_2": "第二声，从低到高。鹅，鱼，羊。",
    "TONE_3": "第三声，先降再升。马，五，雨。",
    "TONE_4": "第四声，从高到低。爸，兔，树。",
    "TONE_0": "轻声，读得轻而短。妈妈，爸爸，孩子。",
}

CONTRAST_NARRATIONS = {
    "C_bdpq": (["b", "d", "p", "q"], "看清竖和半圆的位置。"),
    "C_ft": (["f", "t"], "看清长竖和短竖。"),
    "C_mn": (["m", "n"], "两个门洞和一个门洞。"),
    "C_zzh": (["z", "zh"], "前一个是平舌音，后一个是翘舌音。"),
    "C_cch": (["c", "ch"], "前一个是平舌音，后一个是翘舌音。"),
    "C_ssh": (["s", "sh"], "前一个是平舌音，后一个是翘舌音。"),
    "C_uv": (["u", "v"], "看清两点，听清口形。"),
}


def ipa_segment(sound: str) -> dict:
    return {"text": READINGS[sound], "ipa": IPA_READINGS[sound]}


def build_manifest() -> list[dict]:
    items = [
        {"name": f"L_{sound}", "segments": [ipa_segment(sound)]}
        for sound in READINGS
    ]
    items.extend(
        {"name": name, "segments": [{"text": text}]}
        for name, text in TONE_NARRATIONS.items()
    )
    items.extend(
        {"name": f"{name}_tip", "segments": [{"text": explanation}]}
        for name, (_, explanation) in CONTRAST_NARRATIONS.items()
    )
    return items


def duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True,
        capture_output=True,
        text=True,
        timeout=20,
    )
    value = result.stdout.strip()
    if not value or value == "N/A":
        raise RuntimeError(f"音频没有有效音轨：{path.name}")
    return float(value)


def concat_audio(inputs: list[Path], output: Path) -> None:
    command = ["ffmpeg", "-loglevel", "error", "-y"]
    for source in inputs:
        command.extend(["-i", str(source)])
    streams = "".join(f"[{index}:a]" for index in range(len(inputs)))
    command.extend([
        "-filter_complex", f"{streams}concat=n={len(inputs)}:v=0:a=1[out]",
        "-map", "[out]", "-c:a", "aac", "-b:a", "96k", str(output),
    ])
    subprocess.run(command, check=True, timeout=30)


def main() -> None:
    AUDIO.mkdir(exist_ok=True)
    items = build_manifest()
    with tempfile.TemporaryDirectory(prefix="pinyin-audio-") as tmp_name:
        tmp = Path(tmp_name)
        manifest = tmp / "manifest.json"
        pcm_dir = tmp / "pcm"
        encoded_dir = tmp / "m4a"
        encoded_dir.mkdir()
        ipa_items = [item for item in items if any(segment.get("ipa") for segment in item["segments"])]
        plain_items = [item for item in items if item not in ipa_items]
        manifest.write_text(json.dumps(ipa_items, ensure_ascii=False), encoding="utf-8")
        subprocess.run(
            ["swift", str(SWIFT_HELPER), str(manifest), str(pcm_dir)],
            check=True,
            timeout=240,
        )
        for item in plain_items:
            source = pcm_dir / f"{item['name']}.caf"
            text = "".join(segment["text"] for segment in item["segments"])
            subprocess.run(
                ["say", "-v", "Tingting", "-r", "165", "-o", str(source), text],
                check=True,
                timeout=30,
            )
            print(f"✓ {source.name}", flush=True)
        for item in items:
            source = pcm_dir / f"{item['name']}.caf"
            output = encoded_dir / f"{item['name']}.m4a"
            if not source.exists() or source.stat().st_size <= 4096:
                raise RuntimeError(f"系统语音没有生成有效内容：{item['name']}")
            subprocess.run(
                ["ffmpeg", "-loglevel", "error", "-y", "-i", str(source),
                 "-c:a", "aac", "-b:a", "96k", str(output)],
                check=True,
                timeout=20,
            )
            audio_duration = duration(output)
            if output.stat().st_size <= 2048 or audio_duration < 0.12:
                raise RuntimeError(f"音频过短或为空：{item['name']}（{audio_duration:.3f}s）")
            print(f"✓ {output.name}  {audio_duration:.2f}s", flush=True)
        for name, (sounds, _) in CONTRAST_NARRATIONS.items():
            contrast_output = encoded_dir / f"{name}.m4a"
            concat_audio(
                [*(encoded_dir / f"L_{sound}.m4a" for sound in sounds),
                 encoded_dir / f"{name}_tip.m4a"],
                contrast_output,
            )
            if contrast_output.stat().st_size <= 4096 or duration(contrast_output) < 0.6:
                raise RuntimeError(f"易混对照音频无效：{name}")
            print(f"✓ {contrast_output.name}  {duration(contrast_output):.2f}s", flush=True)
        public_names = [f"L_{sound}" for sound in READINGS]
        public_names.extend(TONE_NARRATIONS)
        public_names.extend(CONTRAST_NARRATIONS)
        for name in public_names:
            source = encoded_dir / f"{name}.m4a"
            destination = AUDIO / source.name
            pending = AUDIO / f".{source.name}.tmp"
            shutil.copy2(source, pending)
            pending.replace(destination)
    print(f"已生成 {len(READINGS)} 个标准呼读音 + {len(TONE_NARRATIONS)} 个声调音频"
          f" + {len(CONTRAST_NARRATIONS)} 个易混对照音频")


if __name__ == "__main__":
    main()
