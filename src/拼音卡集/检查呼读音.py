#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""客观检查拼音呼读音：声调（基频走势）、韵母音值（共振峰）、音节是否被读成两段。

只依赖 ffmpeg + numpy，不联网、不改任何音频文件。
用法：
    python3 检查呼读音.py                # 扫描 audio/ 下全部 L_/TONE_/C_
    python3 检查呼读音.py --file a.m4a b.m4a
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
SR = 16000
FRAME = 640          # 40 ms
HOP = 160            # 10 ms
F0_MIN, F0_MAX = 70.0, 450.0


def decode(path: Path) -> np.ndarray:
    """解成 16 kHz 单声道 float32。"""
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le",
         "-ac", "1", "-ar", str(SR), "-"],
        check=True, capture_output=True, timeout=60,
    ).stdout
    return np.frombuffer(raw, dtype="<f4").astype(np.float64)


def f0_track(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """自相关基频跟踪。返回 (时间秒, 基频 Hz, 浊音标志)。"""
    win = np.hanning(FRAME)
    times, freqs, voiced = [], [], []
    lo, hi = int(SR // F0_MAX), int(SR // F0_MIN)
    for start in range(0, len(x) - FRAME, HOP):
        seg = x[start:start + FRAME] * win
        rms = float(np.sqrt(np.mean(seg ** 2)))
        times.append(start / SR)
        if rms < 0.004:
            freqs.append(np.nan)
            voiced.append(False)
            continue
        frame = seg - seg.mean()
        corr = np.correlate(frame, frame, mode="full")[FRAME - 1:]
        if corr[0] <= 0:
            freqs.append(np.nan)
            voiced.append(False)
            continue
        window = corr[lo:hi]
        if window.size == 0:
            freqs.append(np.nan)
            voiced.append(False)
            continue
        peak = int(np.argmax(window)) + lo
        # 归一化自相关置信度，过低判为清音
        if corr[peak] / corr[0] < 0.32:
            freqs.append(np.nan)
            voiced.append(False)
            continue
        freqs.append(SR / peak)
        voiced.append(True)
    return np.array(times), np.array(freqs), np.array(voiced)


def voiced_span(times: np.ndarray, freqs: np.ndarray, voiced: np.ndarray):
    """返回 (起始秒, 结束秒, 浊音段内基频序列)。"""
    idx = np.where(voiced)[0]
    if idx.size == 0:
        return None, None, np.array([])
    t0, t1 = times[idx[0]], times[idx[-1]]
    return t0, t1, freqs[idx]


def tone_shape(times: np.ndarray, freqs: np.ndarray, voiced: np.ndarray) -> dict:
    """按基频曲线判声调。"""
    t0, t1, seg = voiced_span(times, freqs, voiced)
    if seg.size < 4:
        return {"tone": "?", "f0_start": None, "f0_end": None, "f0_median": None}
    seg = seg[~np.isnan(seg)]
    if seg.size < 4:
        return {"tone": "?", "f0_start": None, "f0_end": None, "f0_median": None}
    n = seg.size
    head = float(np.median(seg[: max(1, n // 4)]))
    mid = float(np.median(seg[n // 3: 2 * n // 3 + 1]))
    tail = float(np.median(seg[-max(1, n // 4):]))
    lo, hi = float(seg.min()), float(seg.max())
    # 用相对中位数的归一化，避免男女声基频差异影响判定
    base = float(np.median(seg))
    head_r = (head - base) / base
    tail_r = (tail - base) / base
    dip_r = (mid - base) / base
    if abs(tail_r - head_r) < 0.06 and lo > base * 0.85:
        tone = "1 平" if base > 0 else "?"
        tone = "1 平"
    elif tail_r > 0.10 and tail_r - head_r > 0.12:
        tone = "2 升"
    elif tail_r < -0.10 and head_r - tail_r > 0.12:
        tone = "4 降"
    elif dip_r < -0.10:
        tone = "3 降升"
    else:
        tone = "1 平"
    return {
        "tone": tone,
        "f0_start": round(head, 1),
        "f0_end": round(tail, 1),
        "f0_median": round(base, 1),
        "f0_range": round(hi - lo, 1),
    }


def formants(x: np.ndarray, t0: float, t1: float) -> tuple[float | None, float | None]:
    """在韵母段（浊音段后 60%）估计 F1/F2。"""
    if t0 is None or t1 is None or t1 - t0 < 0.12:
        return None, None
    s = int((t0 + (t1 - t0) * 0.45) * SR)
    e = int(t1 * SR)
    seg = x[s:e]
    if seg.size < FRAME:
        return None, None
    seg = seg * np.hanning(seg.size)
    spec = np.abs(np.fft.rfft(seg, n=16384))
    freqs = np.fft.rfftfreq(16384, 1 / SR)
    # 谱平滑，压掉谐波细峰
    kernel = np.ones(9) / 9
    spec = np.convolve(spec, kernel, mode="same")
    # 取能量最大的那一帧，避免读到辅音或尾音
    win = 512
    best, best_spec = None, None
    for i in range(0, max(1, len(seg) - win), win):
        chunk = seg[i:i + win]
        if chunk.size < win // 2:
            break
        cs = np.abs(np.fft.rfft(chunk * np.hanning(chunk.size), n=16384))
        cs = np.convolve(cs, kernel, mode="same")
        energy = float(np.sum(cs))
        if best is None or energy > best:
            best, best_spec = energy, cs
    spec = best_spec if best_spec is not None else spec

    def peak(lo_hz: float, hi_hz: float, above: float = 0) -> float | None:
        mask = (freqs >= lo_hz) & (freqs <= hi_hz) & (freqs > above)
        if not mask.any():
            return None
        idx = int(np.argmax(np.where(mask, spec, 0)))
        return float(freqs[idx])

    f1 = peak(150, 1000)
    f2 = peak(700, 3200, above=(f1 or 0) + 120)
    return f1, f2


def internal_gaps(x: np.ndarray, thresh: float = 0.006) -> list[float]:
    """找内部静音段（可能表示被拼成两段音）。"""
    win = int(SR * 0.01)
    n = len(x) // win
    if n < 3:
        return []
    rms = np.array([np.sqrt(np.mean(x[i * win:(i + 1) * win] ** 2)) for i in range(n)])
    silent = rms < thresh
    gaps, run = [], 0
    for i in range(1, len(silent) - 1):   # 首尾静音不算
        if silent[i]:
            run += 1
        else:
            if run >= 4:                   # >= 40 ms
                gaps.append(round(run * 0.01, 3))
            run = 0
    return gaps


def analyze(path: Path) -> dict:
    x = decode(path)
    times, freqs, voiced = f0_track(x)
    t0, t1, _ = voiced_span(times, freqs, voiced)
    tone = tone_shape(times, freqs, voiced)
    f1, f2 = formants(x, t0, t1)
    dur = len(x) / SR
    voiced_ratio = float(voiced.sum() / max(1, len(voiced)))
    return {
        "file": path.name,
        "duration": round(dur, 3),
        "voiced": round(voiced_ratio, 2),
        "tone": tone["tone"],
        "f0_start": tone["f0_start"],
        "f0_end": tone["f0_end"],
        "f0_median": tone["f0_median"],
        "f1": round(f1) if f1 else None,
        "f2": round(f2) if f2 else None,
        "gaps": internal_gaps(x),
        "peak_dbfs": round(20 * np.log10(max(1e-6, float(np.max(np.abs(x))))), 1),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", nargs="*", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.file:
        paths = [Path(p) for p in args.file]
    else:
        paths = sorted((ROOT / "audio").glob("*.m4a"))
        paths = [p for p in paths if re.match(r"^(L_|TONE_|C_)", p.name)]

    rows = [analyze(p) for p in paths]
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    head = f"{'文件':<20}{'时长':>6}{'浊音':>6}{'声调':>9}{'F0起':>7}{'F0止':>7}{'F1':>6}{'F2':>6}{'内静音':>8}"
    print(head)
    print("-" * len(head))
    for r in rows:
        print(f"{r['file']:<20}{r['duration']:>6.2f}{r['voiced']:>6.2f}{r['tone']:>9}"
              f"{str(r['f0_start']):>7}{str(r['f0_end']):>7}{str(r['f1']):>6}{str(r['f2']):>6}"
              f"{str(r['gaps']):>8}")


if __name__ == "__main__":
    sys.exit(main())
