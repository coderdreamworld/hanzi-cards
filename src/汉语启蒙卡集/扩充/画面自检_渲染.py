#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""逐卡渲染三套启蒙卡的**真实卡面**，供画面自检逐张看图。

产出：
    /tmp/vis_qa/<deck>_<idx>_<name>.png   每张卡一张手机卡面截图（会意卡自动点「变！」揭示）
    /tmp/vis_qa/sheet_<deck>_<n>.png      每 6 张一张对照长图（带编号与卡片名）
    /tmp/vis_qa/manifest.json             编号 → 卡片信息的对照表

用法：python3 扩充/画面自检_渲染.py [发布目录]
"""
import base64
import functools
import http.server
import json
import pathlib
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PARENT = ROOT.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = Path("/tmp/vis_qa")

DECKS = [
    ("huiyi.html", "huiyi", 24),
    ("bushou.html", "bushou", 19),
    ("yunyu.html", "yunyu", 24),
]


def render(publish_dir):
    import websocket

    server = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(http.server.SimpleHTTPRequestHandler,
                                            directory=str(publish_dir)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    manifest = {}
    with tempfile.TemporaryDirectory() as profile:
        browser = subprocess.Popen(
            [CHROME, "--headless=new", "--no-first-run", "--disable-gpu",
             "--remote-debugging-port=0", "--remote-allow-origins=*",
             f"--user-data-dir={profile}", "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            pf = pathlib.Path(profile) / "DevToolsActivePort"
            for _ in range(100):
                if pf.exists():
                    break
                time.sleep(.05)
            port = int(pf.read_text().splitlines()[0])
            pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
            page = next(p for p in pages if p["type"] == "page")
            ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=20)
            serial = [0]

            def cmd(method, params=None):
                serial[0] += 1
                ws.send(json.dumps({"id": serial[0], "method": method, "params": params or {}}))
                while True:
                    r = json.loads(ws.recv())
                    if r.get("id") == serial[0]:
                        if "error" in r:
                            raise RuntimeError(r["error"])
                        return r.get("result", {})

            def ev(expr):
                res = cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True,
                                               "awaitPromise": True})
                if "exceptionDetails" in res:
                    raise RuntimeError(json.dumps(res["exceptionDetails"])[:300])
                return res.get("result", {}).get("value")

            cmd("Page.enable")
            cmd("Runtime.enable")
            base = f"http://127.0.0.1:{server.server_port}/"

            def shot(name):
                r = cmd("Page.captureScreenshot", {"format": "png"})
                (OUT / f"{name}.png").write_bytes(base64.b64decode(r["data"]))

            for fname, deck, n in DECKS:
                cmd("Emulation.setDeviceMetricsOverride",
                    {"width": 390, "height": 844, "deviceScaleFactor": 2, "mobile": True})
                cmd("Page.navigate", {"url": base + fname + "?from=hub"})
                for _ in range(200):
                    try:
                        if ev("document.readyState === 'complete'"):
                            break
                    except RuntimeError:
                        pass
                    time.sleep(.05)
                time.sleep(.4)
                for i in range(n):
                    ev(f"state.i={i}; state.revealed=false; render()")
                    time.sleep(.12)
                    if ev("CARDS[state.i].type === 'magic'"):
                        ev("if(!state.revealed){document.getElementById('primaryBtn').click()}")
                        time.sleep(.15)
                    name = ev("CARDS[state.i].result || CARDS[state.i].radical || CARDS[state.i].title")
                    shot(f"{deck}_{i:02d}_{name}")
                    manifest[f"{deck}_{i:02d}"] = {
                        "deck": deck, "index": i, "name": name,
                        "type": ev("CARDS[state.i].type"),
                        "story": ev("CARDS[state.i].story || ''"),
                        "meaning": ev("CARDS[state.i].meaning || ''"),
                        "lines": ev("JSON.stringify(CARDS[state.i].lines||[])"),
                        "members": ev("JSON.stringify(CARDS[state.i].members||[])"),
                        "tips": ev("JSON.stringify(CARDS[state.i].tips||[])"),
                    }
                # 网格视图（整套缩略，检查配色撞车与裁切）
                cmd("Emulation.setDeviceMetricsOverride",
                    {"width": 1440, "height": 2600, "deviceScaleFactor": 1, "mobile": False})
                cmd("Page.navigate", {"url": base + fname + "?mode=grid"})
                time.sleep(.7)
                shot(f"{deck}_grid")
            ws.close()
        finally:
            browser.terminate()
            browser.wait(timeout=5)
            server.shutdown()
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
    print(f"渲染 {len(manifest)} 张卡 → {OUT}")


def sheets():
    """每 6 张拼一张对照图（2 行 × 3 列），带编号与卡片名，便于逐张核对。"""
    from PIL import Image, ImageDraw
    manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
    keys = sorted(manifest)
    per = 6
    cols, tw = 3, 420
    for deck in ("huiyi", "bushou", "yunyu"):
        dk = [k for k in keys if manifest[k]["deck"] == deck]
        for s in range(0, len(dk), per):
            chunk = dk[s:s + per]
            ims = []
            for k in chunk:
                im = Image.open(OUT / f"{k}_{manifest[k]['name']}.png").convert("RGB")
                # 只取卡片区域（去掉顶部标题与底部工具条），按高度裁到卡片框
                w, h = im.size
                im = im.crop((0, int(h * 0.08), w, int(h * 0.86)))
                r = tw / im.width
                ims.append((k, manifest[k]["name"], im.resize((tw, int(im.height * r)))))
            rh = max(i.height for _, _, i in ims)
            rows = (len(ims) + cols - 1) // cols
            sheet = Image.new("RGB", (cols * (tw + 10) + 10, rows * (rh + 34) + 10), (246, 241, 229))
            d = ImageDraw.Draw(sheet)
            for j, (k, nm, im) in enumerate(ims):
                x = 10 + (j % cols) * (tw + 10)
                y = 10 + (j // cols) * (rh + 34)
                d.text((x + 2, y + 2), f"{k}  {nm}", fill=(20, 20, 20))
                sheet.paste(im, (x, y + 22))
            sheet.save(OUT / f"sheet_{deck}_{s // per + 1}.png")
    print("对照图已生成")


def main():
    OUT.mkdir(exist_ok=True)
    for f in OUT.glob("*.png"):
        f.unlink()
    publish = Path(sys.argv[1]) if len(sys.argv) > 1 else PARENT / "微信传播方案" / "发布" / "github-pages"
    render(publish.resolve())
    sheets()
    print("\n".join(sorted(p.name for p in OUT.glob("sheet_*.png"))))


if __name__ == "__main__":
    main()
