#!/usr/bin/env python3
"""生成26个字母名音频，拼读时逐个播放，画面高亮跟随实际音频结束。"""
import json
import string
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO = HERE / "audio"

for letter in string.ascii_lowercase:
    target = AUDIO / f"en_letter_{letter}.m4a"
    if target.exists():
        continue
    source = AUDIO / f"en_letter_{letter}.aiff"
    subprocess.run(["say", "-v", "Samantha", "-r", "120", "-o", str(source), letter.upper() + "."], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(source), "-c:a", "aac", "-b:a", "96k", "-ar", "22050", "-ac", "1", str(target)], check=True)
    source.unlink()
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(target)], capture_output=True, text=True, check=True)
    duration = float(json.loads(result.stdout)["format"]["duration"])
    assert 0.15 < duration < 3, (letter, duration)
print("OK 26字母音频；拼读高亮随每段实际播放结束切换")
