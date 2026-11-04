#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语单词卡 · 批量音频生成（say → ffmpeg → 校验 → manifest）。

与拼音卡同一条离线预生成路线（见 发音方案.md 实测）：
  单词: say -v Samantha -r 140 "Cat."       → en_<slug>_w.m4a
  拼读: say -v Samantha -r 120 "C, A, T. Cat." → en_<slug>_s.m4a
输出 AAC 96k 22050Hz 单声道，audio/manifest.json 记每条时长（拼读逐字母高亮用）。

用法：
  python3 生成音频.py --group dongwu-a        # 只生成该组
  python3 生成音频.py --group all             # 全部 500 词
  python3 生成音频.py --group dongwu-a --force  # 已存在的也重生成
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO = HERE / "audio"
VOICE = "Samantha"
RATE_W, RATE_S = "140", "120"

spec = importlib.util.spec_from_file_location("cik", HERE / "词库500.py")
cik = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cik)

def slug(w):
    return w.lower().replace(" ", "-")

def spell_text(w):
    letters = [ch for ch in w if ch.isalpha()]
    return ", ".join(letters) + ". " + w + "."

def word_text(w):
    return w + "."

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])}… 失败: {r.stderr[:300]}")
    return r

def gen_one(w, kind, text, rate, force):
    path = AUDIO / f"en_{slug(w)}_{kind}.m4a"
    if path.exists() and not force:
        return None
    with tempfile.TemporaryDirectory() as td:
        aiff = Path(td) / "a.aiff"
        run(["say", "-v", VOICE, "-r", rate, "-o", str(aiff), text])
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff),
             "-c:a", "aac", "-b:a", "96k", "-ar", "22050", "-ac", "1", str(path)])
    # 校验：时长合理 + 非静音
    p = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(path)])
    dur = float(p.stdout.strip())
    v = run(["ffmpeg", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"])
    mean = [l for l in v.stderr.splitlines() if "mean_volume" in l]
    mv = float(mean[0].split(":")[1].replace("dB", "").strip()) if mean else -99
    assert 0.3 < dur < 12, f"{w}/{kind} 时长异常 {dur:.2f}s"
    assert mv > -45, f"{w}/{kind} 疑似静音 mean={mv}dB"
    return {"dur": round(dur, 2), "mean_db": mv}

def main():
    args = sys.argv[1:]
    force = "--force" in args
    gi = args.index("--group")
    gid = args[gi + 1]
    groups = cik.GROUPS if gid == "all" else [g for g in cik.GROUPS if g["id"] == gid]
    assert groups, f"找不到组 {gid}"
    AUDIO.mkdir(exist_ok=True)

    manifest = {}
    mf = AUDIO / "manifest.json"
    if mf.exists():
        manifest = json.loads(mf.read_text(encoding="utf-8"))

    ok = skip = 0
    for g in groups:
        for item in g["words"]:
            w = item["w"]
            entry = manifest.get(w, {})
            r1 = gen_one(w, "w", word_text(w), RATE_W, force)
            if r1: entry["w"] = r1; ok += 1
            else: entry.setdefault("w", {}); skip += 1
            r2 = gen_one(w, "s", spell_text(w), RATE_S, force)
            if r2: entry["s"] = r2; ok += 1
            else: entry.setdefault("s", {})
            manifest[w] = entry
    mf.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK 生成 {ok} 条，跳过 {skip} 条 → {mf}")

if __name__ == "__main__":
    main()
