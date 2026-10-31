#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 hanzi-writer-data 生成 1000 字笔顺数据（与 legacy 编码完全一致：round(v/8) 量化+差分）。"""
import json, re, ast, importlib.util, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("ziku", HERE / "字库1000.py")
ziku = importlib.util.module_from_spec(spec); spec.loader.exec_module(ziku)

chars = []
for g in ziku.GROUPS:
    for it in g["chars"]:
        chars += list(it) if isinstance(it, tuple) else [it["char"] if isinstance(it, dict) else it]
chars = sorted(set(chars))
print("目标字数:", len(chars))

def quant(meds):
    out = []
    for st in meds:
        pts = [(round(x/8), round(y/8)) for x, y in st]
        arr = [pts[0][0], pts[0][1]]
        px, py = pts[0]
        for x, y in pts[1:]:
            arr += [x - px, y - py]; px, py = x, y
        out.append(arr)
    return out

# 1) 生成并验证 legacy 422 字全量对拍
t = open("/Users/ping/C 行动_与人交流/孩子/识字卡片_笔画数据.py", encoding="utf-8").read()
m = re.search(r'STROKES_JSON = \((.*)\)\s*$', t, re.S)
legacy = json.loads(ast.literal_eval("(" + m.group(1) + ")"))
bad = []
for ch, exp in legacy.items():
    try:
        hw = json.load(open(f"tools/node_modules/hanzi-writer-data/{ch}.json"))
        got = quant(hw["medians"])
        if got != exp: bad.append(ch)
    except FileNotFoundError:
        bad.append(ch)
print(f"legacy 对拍: {len(legacy)-len(bad)}/{len(legacy)} 一致", ("不一致: " + "、".join(bad)) if bad else "✓")
assert not bad, "公式与 legacy 不一致，禁止继续"

# 2) 生成全部 1000 字
data, missing = {}, []
for ch in chars:
    try:
        hw = json.load(open(f"tools/node_modules/hanzi-writer-data/{ch}.json"))
        data[ch] = quant(hw["medians"])
    except FileNotFoundError:
        missing.append(ch)
if missing:
    print("hanzi-writer-data 缺字:", "、".join(missing)); sys.exit(1)
print(f"✓ 1000 字笔顺数据齐 ({len(data)})")

# 3) 包络统计（含半笔宽 41.5）→ STROKE_FIT
PAD = 41.5
x0 = y0 = 1e9; x1 = y1 = -1e9
for ch, strokes in data.items():
    for st in strokes:
        x, y = st[0]*8, st[1]*8; xs, ys = [x], [y]
        for k in range(2, len(st), 2):
            x += st[k]*8; y += st[k+1]*8; xs.append(x); ys.append(y)
        x0 = min(x0, min(xs)); x1 = max(x1, max(xs))
        y0 = min(y0, min(ys)); y1 = max(y1, max(ys))
ex0, ex1, ey0, ey1 = x0-PAD, x1+PAD, y0-PAD, y1+PAD
w, h = ex1-ex0, ey1-ey0
s = round(0.97/max(w, h), 8)
cx, cy = round((ex0+ex1)/2, 1), round((ey0+ey1)/2, 1)
print(f"包络: x {x0:.0f}..{x1:.0f}  y {y0:.0f}..{y1:.0f}")
print(f"含笔宽: x {ex0:.1f}..{ex1:.1f} ({w:.1f})  y {ey0:.1f}..{ey1:.1f} ({h:.1f})")
print(f"STROKE_FIT = {{ s: {s}, cx: {cx}, cy: {cy} }}")

# 4) 写文件（与 legacy 相同格式）
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
with open(HERE / "笔画数据1000.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
    f.write('"""识字卡 1000 字笔画数据——标准笔顺（来源 hanzi-writer-data，GPL-3.0 数据许可）。\n')
    f.write('编码与 422 版完全一致：每字每笔 [x0,y0,dx1,dy1,...]，1024 坐标 1/8 量化值，解码累加 ×8 还原。"""\n\n')
    f.write("STROKES_JSON = (\n")
    f.write('"%s"\n' % payload)
    f.write(")\n")
print("笔画数据1000.py 已写出", (HERE / "笔画数据1000.py").stat().st_size, "B")
