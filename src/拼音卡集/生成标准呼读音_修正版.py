#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成修正版拼音呼读音。

路线（2026-10-31 定稿）
----
1. **能用汉字就不用 IPA** —— 58 个音用 macOS `say -v Tingting` 直读标准第一声汉字。
2. 汉语里没有第一声常用字的少数音（o/ün/yun）走 Tingting IPA（实测能完整渲染的简单写法）。
3. **d/t/n/l/f/r/ri 这 7 个文件走「Tingting IPA + PSOLA 拉平」**：Tingting 的 IPA 渲染带
   自然语调（d 稳态上扬 21%、t 先降后升 31%），且「日」的舌尖元音 [ɨ] 与平调在
   Tingting 的 IPA 通道里不可兼得。PSOLA 只改基频、保留音色与共振峰——
   d/t/n/l/f 用 `˥` 源拉平；r/ri 用 `ʐɨ`（自然四声、含 [ɨ] 元音）拉平成「日的平声」。
   （曾试过 espeak-ng，音色机械被用户否掉；本路线为最终方案。）

用法
----
    python3 生成标准呼读音_修正版.py                    # 输出到 audio_修正版/
    python3 生成标准呼读音_修正版.py --out audio         # 覆盖线上 audio/（确认后再用）
    python3 生成标准呼读音_修正版.py --out audio_修正版 --only L_ai L_q L_er
"""
from __future__ import annotations

import argparse
import json

import numpy as np
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SWIFT_HELPER = ROOT / "生成标准呼读音.swift"

# ---------------------------------------------------------------------------
# 修正后的 64 个音形项目。
#   汉字项：直接用 macOS `say -v Tingting` 读标准第一声汉字（不带 IPA）。
#   IPA 项：汉语里没有对应第一声常用汉字，只能走 IPA；写法必须是 macOS 能完整
#           渲染的「单层简单」形式。
# ---------------------------------------------------------------------------

# 声母 21 + y/w 2
CHAR_READINGS = {
    # 声母呼读音（全部第一声）
    "b": "玻", "p": "坡", "m": "摸",
    "g": "哥", "k": "科", "h": "喝",
    "j": "基", "q": "欺", "x": "希",
    "zh": "知", "ch": "吃", "sh": "诗",
    "z": "资", "c": "疵", "s": "思",
    "y": "衣", "w": "乌",
    # 单韵母 6
    "a": "阿", "e": "婀", "i": "衣", "u": "乌", "v": "迂",
    # 复韵母 8 + 特殊韵母 1
    "ai": "哀", "ei": "诶", "ui": "威", "ao": "凹",
    "ou": "欧", "iu": "优", "ie": "耶", "ve": "约", "er": "耳",
    # 前鼻韵母 4 + 后鼻韵母 4
    "an": "安", "en": "恩", "in": "因", "un": "温",
    "ang": "肮", "eng": "灯", "ing": "英",
    # 整体认读音节 16
    "zhi": "知", "chi": "吃", "shi": "诗",
    "zi": "资", "ci": "疵", "si": "思",
    "yi": "衣", "wu": "乌", "yu": "迂", "ye": "耶", "yue": "约",
    "yuan": "冤", "yin": "音", "ying": "英",
}

# 必须走 IPA 的音：文本只用来给引擎定位，真实读音由 IPA 指定。
IPA_READINGS = {
    "vn": ("啊", "yn˥"),   # ün —— 晕是四声、云是二声，都不是第一声
    "yun": ("啊", "yn˥"),
    # o 用「喔」——它是教材注音的标准后半高圆唇后元音；但「喔」单念是四声，
    # 所以挂 IPA 强制第一声。实测结果与「噢」直读完全一致（0.37 s / 平调）。
    "o": ("喔", "o˥"),
    # ong：汉语里**没有**零声母的 ong 音节，「翁」是 wēng（字面就带 w 音），
    # 「轰 hōng」又带 h 声母，所以只能用 IPA。macOS 不支持 ʊ（会被整段丢掉，
    # 只剩 0.09 s 鼻音），故用 oŋ —— 圆唇后元音 + 鼻韵尾，**不带 w/u 滑音**。
    "ong": ("啊", "oŋ˥"),
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

# 卡片用 ü 命名，文件名统一用 v
# 走「Tingting IPA + PSOLA 拉平」的音（2026-10-31 定稿）：d/t/n/l/f/r/ri。
# (文本, IPA, 目标基频 None=自动取浊音中位数并夹到 [200,265])
PSOLA_READINGS = {
    "d": ("啊", "tɤ˥", None),
    "t": ("啊", "tʰɤ˥", None),
    "n": ("啊", "nɤ˥", None),
    "l": ("啊", "lɤ˥", None),
    "f": ("啊", "fo˥", None),
    "r": ("日", "ʐɨ", None),   # 自然「日」含舌尖元音 [ɨ]，拉平即「日的平声」
    "ri": ("日", "ʐɨ", None),  # r 与 ri 普通话同音
}

SR = 22050


def _f0_track(x, sr, fmin=70.0, fmax=400.0):
    W = int(0.040 * sr); H = int(0.005 * sr)
    lo, hi = int(sr / fmax), int(sr / fmin)
    times, f0s = [], []
    for i in range(0, max(1, len(x) - W), H):
        seg = x[i:i + W] * np.hanning(W)
        if float(np.sqrt(np.mean(seg ** 2))) < 0.006:
            times.append(i / sr); f0s.append(np.nan); continue
        s = seg - seg.mean()
        c = np.correlate(s, s, "full")[W - 1:]
        if c[0] <= 0:
            times.append(i / sr); f0s.append(np.nan); continue
        pk = int(np.argmax(c[lo:hi])) + lo
        times.append(i / sr)
        f0s.append(sr / pk if c[pk] / c[0] > 0.35 else np.nan)
    return np.array(times), np.array(f0s)


def psola_flatten(x, sr, target=None, clamp=(200.0, 265.0)):
    """TD-PSOLA + 颗粒重采样：浊音段基频拉平（严格恒定），清音头尾原样保留。"""
    times, f0s = _f0_track(x, sr)
    ok = ~np.isnan(f0s)
    if ok.sum() < 8:
        return x, None
    med = float(np.median(f0s[ok]))
    tgt = float(np.clip(med, clamp[0], clamp[1])) if target is None else float(target)
    vi = np.where(ok)[0]
    i0 = max(0, int(times[vi[0]] * sr) - int(0.004 * sr))
    i1 = min(len(x) - 1, int((times[vi[-1]] + 0.008) * sr))
    span = i1 - i0
    if span < int(0.05 * sr):
        return x, tgt

    def f0_at(pos):
        f = float(np.interp(pos / sr, times, np.where(np.isnan(f0s), med, f0s)))
        return f if f >= 50 else tgt

    marks = []
    pos = i0; guard = 0
    while pos < i1 and guard < 20000:
        marks.append(pos); pos += int(sr / f0_at(pos)); guard += 1
    if len(marks) < 6:
        return x, tgt
    T = sr / tgt
    grain_out = int(2 * T)
    need = int(np.ceil(span / T)) + 2
    synth = np.zeros(span + int(0.03 * sr) + grain_out)
    reservoir = max(4, len(marks) // 4)
    outp = 0
    for j in range(need):
        if j < len(marks):
            m = marks[j]
        else:  # 段长不足：循环尾部颗粒补足（时间微扩展）
            m = marks[len(marks) - reservoir + ((j - len(marks)) % reservoir)]
        p = sr / f0_at(m)
        gin = int(2 * p)
        a = m - gin // 2; b = a + gin
        if a < 0 or b > len(x):
            continue
        g = x[a:b] * np.hanning(gin)
        if gin != grain_out:
            g = np.interp(np.linspace(0, gin - 1, grain_out), np.arange(gin), g)
        synth[outp:outp + grain_out] += g
        outp += int(T)
    synth = synth[:min(outp + grain_out, len(synth))]
    fade = int(0.010 * sr)
    head = x[:i0]
    nf = min(fade, len(synth), max(1, len(x) - i0))
    synth[:nf] = synth[:nf] * np.linspace(0, 1, nf) + x[i0:i0 + nf] * np.linspace(1, 0, nf)
    tail = x[i1:]
    nt = min(fade, len(synth), len(tail))
    if nt > 0:
        synth[-nt:] = synth[-nt:] * np.linspace(1, 0, nt) + tail[:nt] * np.linspace(0, 1, nt)
    return np.concatenate([head, synth, tail[nt:]]), tgt


def encode_pcm(y, dst):
    peak = float(np.max(np.abs(y)))
    y = y * 10 ** ((-2.6 - 20 * np.log10(max(1e-9, peak))) / 20)
    n_in = int(0.012 * SR); y[:n_in] *= np.linspace(0, 1, n_in)
    n_out = int(0.050 * SR); y[-n_out:] *= np.linspace(1, 0, n_out)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR),
                    "-ac", "1", "-i", "-", "-c:a", "aac", "-b:a", "96k", str(dst)],
                   input=y.astype("<f4").tobytes(), check=True, timeout=60)


def audio_name(sound: str) -> str:
    return f"L_{sound.replace('ü', 'v')}"


def build_manifest() -> list[dict]:
    items: list[dict] = []
    for sound, char in CHAR_READINGS.items():
        if char is None:
            continue
        items.append({"name": audio_name(sound), "segments": [{"text": char}]})
    for sound, (text, ipa) in IPA_READINGS.items():
        items.append({"name": audio_name(sound),
                      "segments": [{"text": text, "ipa": ipa}]})
    items.extend({"name": name, "segments": [{"text": text}]}
                 for name, text in TONE_NARRATIONS.items())
    items.extend({"name": f"{name}_tip", "segments": [{"text": explanation}]}
                 for name, (_, explanation) in CONTRAST_NARRATIONS.items())
    return items


def run(cmd: list[str], timeout: int = 240) -> None:
    subprocess.run(cmd, check=True, timeout=timeout, capture_output=True)


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True, capture_output=True, text=True, timeout=20).stdout.strip()
    if not out or out == "N/A":
        raise RuntimeError(f"音频没有有效音轨：{path.name}")
    return float(out)


def to_pcm(src: Path, dst: Path) -> None:
    """解成 48 kHz 单声道 PCM，供无缝隙拼接。"""
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src),
         "-ac", "1", "-ar", "48000", "-f", "s16le", str(dst)], timeout=30)


def concat_pcm(sources: list[Path], dst: Path) -> None:
    """先解 PCM 再拼接，消除 AAC 编码延迟造成的拼接缝。"""
    tmp = dst.parent / (dst.stem + "_parts")
    tmp.mkdir(exist_ok=True)
    try:
        for index, source in enumerate(sources):
            to_pcm(source, tmp / f"{index:03d}.pcm")
        with open(dst, "wb") as out:
            for index in range(len(sources)):
                out.write((tmp / f"{index:03d}.pcm").read_bytes())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def encode(src: Path, dst: Path, bitrate: str = "96k", raw: bool = False) -> None:
    cmd = ["ffmpeg", "-loglevel", "error", "-y"]
    if raw:
        cmd += ["-f", "s16le", "-ar", "48000", "-ac", "1"]
    cmd += ["-i", str(src), "-c:a", "aac", "-b:a", bitrate, str(dst)]
    run(cmd, timeout=30)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="audio_修正版",
                        help="输出目录；传 audio 则覆盖线上音频")
    parser.add_argument("--only", nargs="*", default=None,
                        help="只重生成这些音（留空为全部）")
    args = parser.parse_args()

    out_dir = (ROOT / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    items = build_manifest()
    if args.only:
        wanted = {audio_name(s) for s in args.only}
        items = [i for i in items if i["name"] in wanted]

    with tempfile.TemporaryDirectory(prefix="pinyin-fix-") as tmp_name:
        tmp = Path(tmp_name)
        pcm_dir = tmp / "pcm"
        pcm_dir.mkdir()
        psola_names = {audio_name(k) for k in PSOLA_READINGS}
        ipa_items = [i for i in items
                     if any(s.get("ipa") for s in i["segments"])
                     and i["name"] not in psola_names]
        plain_items = [i for i in items if i not in ipa_items]

        (tmp / "m.json").write_text(
            json.dumps(ipa_items, ensure_ascii=False), encoding="utf-8")
        if ipa_items:
            run(["swift", str(SWIFT_HELPER), str(tmp / "m.json"), str(pcm_dir)])
        psola_names = {audio_name(k) for k in PSOLA_READINGS}
        plain_items = [i for i in plain_items if i["name"] not in psola_names]
        for item in plain_items:
            text = "".join(s["text"] for s in item["segments"])
            run(["say", "-v", "Tingting", "-r", "165",
                 "-o", str(pcm_dir / f"{item['name']}.caf"), text], timeout=30)

        for item in items:
            source = pcm_dir / f"{item['name']}.caf"
            if not source.exists() or source.stat().st_size <= 4096:
                raise RuntimeError(f"系统语音没有生成有效内容：{item['name']}")
            encode(source, pcm_dir / f"{item['name']}.m4a")
            if item["name"].endswith("_tip"):
                continue                      # 中间产物，不进输出目录
            target = out_dir / f"{item['name']}.m4a"
            shutil.copy2(pcm_dir / f"{item['name']}.m4a", target)
            print(f"✓ {target.name}  {probe_duration(target):.2f}s", flush=True)

        # PSOLA 路线（d/t/n/l/f/r/ri）：Tingting IPA 源 → 拉平 → 归一化
        psola_keys = {audio_name(k): k for k in PSOLA_READINGS}
        psola_src = {k: v for k, v in psola_keys.items()}
        if psola_src:
            manifest = [{"name": k, "segments": [{"text": PSOLA_READINGS[v][0],
                                                  "ipa": PSOLA_READINGS[v][1]}]}
                        for k, v in psola_src.items()]
            (tmp / "p.json").write_text(json.dumps(manifest, ensure_ascii=False),
                                        encoding="utf-8")
            subprocess.run(["swift", str(SWIFT_HELPER), str(tmp / "p.json"), str(pcm_dir)],
                           check=True, timeout=240, capture_output=True)
            for key in psola_src:
                tgt = PSOLA_READINGS[psola_src[key]][2]
                x = np.frombuffer(subprocess.run(
                    ["ffmpeg", "-v", "error", "-i", str(pcm_dir / f"{key}.caf"),
                     "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                    check=True, capture_output=True).stdout, dtype="<f4").astype(np.float64)
                flat, _ = psola_flatten(x, SR, tgt)
                encode_pcm(flat, pcm_dir / f"{key}.m4a")
                shutil.copy2(pcm_dir / f"{key}.m4a", out_dir / f"{key}.m4a")
                print(f"✓ {key}.m4a（PSOLA 拉平）  {probe_duration(out_dir / f'{key}.m4a'):.2f}s",
                      flush=True)

        for name, (sounds, _) in CONTRAST_NARRATIONS.items():
            parts = [pcm_dir / f"{audio_name(sound)}.m4a" for sound in sounds]
            parts.append(pcm_dir / f"{name}_tip.m4a")
            if not all(part.exists() for part in parts):
                print(f"· 跳过 {name}.m4a（--only 未覆盖其组成部分）", flush=True)
                continue
            merged = pcm_dir / f"{name}.pcm"
            concat_pcm(parts, merged)
            encode(merged, pcm_dir / f"{name}.m4a", raw=True)
            target = out_dir / f"{name}.m4a"
            shutil.copy2(pcm_dir / f"{name}.m4a", target)
            print(f"✓ {target.name}  {probe_duration(target):.2f}s", flush=True)

    print(f"已写入 {out_dir}")


if __name__ == "__main__":
    main()
