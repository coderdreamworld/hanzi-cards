"""Browser regression check for every card deck linked from the hub."""

import functools
import http.server
import json
import pathlib
import subprocess
import tempfile
import threading
import time
import urllib.request

import websocket


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DECKS = (
    "pinyin-zimu", "shizi-422", "shizi-1000",
    "xiangxing", "huiyi", "bushou", "yunyu", "emotion",
)
HUB_DECKS = set(DECKS) - {"xiangxing"}


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    server = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(ROOT))
    )
    threading.Thread(target=server.serve_forever, daemon=True).start()
    failures = []
    with tempfile.TemporaryDirectory() as profile:
        browser = subprocess.Popen(
            [CHROME, "--headless=new", "--no-first-run", "--disable-gpu",
             "--remote-debugging-port=0", "--remote-allow-origins=*",
             f"--user-data-dir={profile}", "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        try:
            portfile = pathlib.Path(profile) / "DevToolsActivePort"
            for _ in range(100):
                if portfile.exists():
                    break
                time.sleep(.05)
            port = int(portfile.read_text().splitlines()[0])
            pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
            page = next(p for p in pages if p["type"] == "page")
            ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=10)
            serial = 0

            def cmd(method, params=None):
                nonlocal serial
                serial += 1
                ws.send(json.dumps({"id": serial, "method": method, "params": params or {}}))
                while True:
                    response = json.loads(ws.recv())
                    if response.get("id") == serial:
                        if "error" in response:
                            raise RuntimeError(response["error"])
                        return response.get("result", {})

            def evaluate(expression):
                result = cmd("Runtime.evaluate", {"expression": expression,
                                                  "returnByValue": True, "awaitPromise": True})
                if "exceptionDetails" in result:
                    raise RuntimeError(result["exceptionDetails"].get("text"))
                return result.get("result", {}).get("value")

            base = f"http://127.0.0.1:{server.server_port}/"

            def visit(path):
                cmd("Page.navigate", {"url": base + path})
                for _ in range(120):
                    if evaluate("document.readyState === 'complete' && location.pathname.endsWith(" +
                                json.dumps("/" + path.split("?")[0]) + ")"):
                        time.sleep(.12)
                        return
                    time.sleep(.05)
                raise RuntimeError(f"Page did not load: {path}")

            cmd("Page.enable")
            cmd("Runtime.enable")
            cmd("Emulation.setDeviceMetricsOverride", {
                "width": 390, "height": 844, "deviceScaleFactor": 3, "mobile": True,
            })
            visit("index.html")
            links = evaluate("Array.from(document.querySelectorAll('a.card')).map(a => a.getAttribute('href'))")
            layout_expr = ("(() => { const card=document.querySelector('.gallery .stage .card-svg, .gallery .stage .card');"
                           "const nav=document.querySelector('.gallery .bar, .gallery .controls');"
                           "const home=document.querySelector('.gallery .home-btn, .topbar .home-btn');"
                           "return {overflow:document.documentElement.scrollWidth>innerWidth+1,"
                           "overlap:!!card&&!!nav&&card.getBoundingClientRect().bottom>nav.getBoundingClientRect().top+1,"
                           "homeTop:home?home.getBoundingClientRect().top:null};})()")
            for deck in ("xiangxing", "pinyin-pindu"):
                if any(href and href.startswith("./" + deck + ".html") for href in links):
                    failures.append(f"{deck}: intentionally hidden deck appears in hub")
            for deck in DECKS:
                if deck in HUB_DECKS and not any(href and href.startswith("./" + deck + ".html") for href in links):
                    failures.append(f"{deck}: missing hub entry")
                if not (ROOT / (deck + ".html")).exists():
                    failures.append(f"{deck}: missing published HTML")
                    continue
                evaluate("localStorage.clear()")
                visit(deck + ".html?from=hub")
                home = evaluate("Array.from(document.querySelectorAll('a.home-btn')).some(a => {"
                                "const r=a.getBoundingClientRect(),s=getComputedStyle(a);"
                                "return s.display!=='none' && r.width>0 && r.height>0 && r.top>=44 && "
                                "a.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2));})")
                if not home:
                    detail = evaluate("Array.from(document.querySelectorAll('a.home-btn')).map(a=>{"
                                      "const r=a.getBoundingClientRect(),h=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);"
                                      "return {top:r.top,left:r.left,width:r.width,height:r.height,hit:h?.className,display:getComputedStyle(a).display};})")
                    failures.append(f"{deck}: no reachable mobile home button {detail}")
                layout = evaluate(layout_expr)
                if layout["overflow"] or layout["overlap"]:
                    failures.append(f"{deck}: phone layout {layout}")
                time.sleep(.12)
                first = evaluate("JSON.parse(localStorage.getItem('hz.last') || 'null')")
                if not first or first.get("id") != deck:
                    failures.append(f"{deck}: first card not saved")
                step = "render(index + 1)" if deck == "emotion" else (
                    "move(1)" if deck.startswith("pinyin-") else "go(1)")
                evaluate(step)
                time.sleep(.12)
                latest = evaluate("JSON.parse(localStorage.getItem('hz.last') || 'null')")
                saved = evaluate("JSON.parse(localStorage.getItem('hz.deck." + deck + "') || 'null')")
                if not latest or latest.get("id") != deck or latest == first:
                    failures.append(f"{deck}: next card not reflected in hub progress")
                if not saved or saved.get("i") != 1:
                    failures.append(f"{deck}: card 2 not saved for resume")
                visit("index.html")
                resume = evaluate("document.querySelector('a.card.continue')?.getAttribute('href')")
                if resume != "./" + deck + ".html?from=hub":
                    failures.append(f"{deck}: hub has no matching resume link")
                badges = evaluate("document.querySelectorAll('.lastbadge').length")
                if badges != (1 if deck in HUB_DECKS else 0):
                    failures.append(f"{deck}: hub has {badges} last-viewed badges")
                visit(deck + ".html?from=hub")
                restored = evaluate("index" if deck == "emotion" else "state.i")
                if restored != 1:
                    failures.append(f"{deck}: did not restore card 2 (got {restored})")
                cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 320, "height": 568, "deviceScaleFactor": 3, "mobile": True,
                })
                visit(deck + ".html?from=hub")
                layout = evaluate(layout_expr)
                if layout["overflow"] or layout["overlap"] or layout["homeTop"] is None or layout["homeTop"] < 44:
                    failures.append(f"{deck}: narrow phone layout {layout}")
                cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 390, "height": 844, "deviceScaleFactor": 3, "mobile": True,
                })
                evaluate("localStorage.clear()")
                visit(deck + ".html")
                first_direct = evaluate("JSON.parse(localStorage.getItem('hz.deck." + deck + "') || 'null')")
                if not first_direct or first_direct.get("i") != 0:
                    failures.append(f"{deck}: direct first card not saved")
                evaluate(step)
                direct_next = evaluate("JSON.parse(localStorage.getItem('hz.deck." + deck + "') || 'null')")
                if not direct_next or direct_next.get("i") != 1:
                    failures.append(f"{deck}: first direct navigation not saved")
                cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False,
                })
                visit(deck + ".html?from=hub")
                desktop_home = evaluate("Array.from(document.querySelectorAll('.desk-top .home-btn, .topbar .home-btn')).some(a=>{"
                                        "const r=a.getBoundingClientRect();"
                                        "return r.width>0&&r.height>0&&a.getAttribute('href')==='index.html'&&"
                                        "a.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2));})")
                if not desktop_home:
                    failures.append(f"{deck}: desktop home button unavailable")
                cmd("Emulation.setDeviceMetricsOverride", {
                    "width": 390, "height": 844, "deviceScaleFactor": 3, "mobile": True,
                })
            print("\n".join(failures) if failures else f"PASS: {len(DECKS)} decks, home + save + resume")
            ws.close()
        finally:
            browser.terminate()
            browser.wait(timeout=5)
            server.shutdown()
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
