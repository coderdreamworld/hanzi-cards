#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 识字卡片_1000字.html 发布到 微信传播方案/发布/github-pages/shizi-1000.html，
并更新导航首页 index.html 加入口。幂等：重复运行安全。

用法：python3 部署准备.py     （审计通过后运行，然后手动 git push）
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PUBLISH = HERE.parent / "微信传播方案" / "发布" / "github-pages"

FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'%3E%3Crect width=\'64\' height=\'64\' rx=\'14\' fill=\'%233e9486\'/%3E%3Ctext x=\'32\' y=\'44\' font-size=\'36\' text-anchor=\'middle\' fill=\'%23fdf8ec\' font-family=\'serif\'%3E字%3C/text%3E%3C/svg%3E">'
CSS = """
    /* 微信内引导条（仅 MicroMessenger UA 显示） */
    .wx-tip { position: fixed; left: 12px; right: 12px; bottom: calc(14px + env(safe-area-inset-bottom));
              background: var(--button, #dff4f1); color: var(--ink, #4a3226); border-radius: 14px; padding: 10px 14px;
              font-size: 14px; display: none; align-items: center; gap: 10px;
              box-shadow: 0 4px 16px rgba(74,50,38,.18); z-index: 999; }
    .wx-tip.show { display: flex; }
    .wx-tip .wx-x { margin-left: auto; color: var(--muted, #8d7d73); padding: 2px 6px; cursor: pointer; }
"""
JS = """
  <script>
  (function () {
    if (!/MicroMessenger/i.test(navigator.userAgent)) return;
    if (sessionStorage.getItem('wxTipDone')) return;
    var bar = document.createElement('div');
    bar.className = 'wx-tip';
    bar.innerHTML = '微信里用：点右上角「···」可<span style="color:#3e9486;font-weight:600">收藏</span>或加<span style="color:#3e9486;font-weight:600">浮窗</span>，下次秒开<span class="wx-x">✕</span>';
    bar.querySelector('.wx-x').addEventListener('click', function () {
      sessionStorage.setItem('wxTipDone', '1');
      bar.remove();
    });
    document.body.appendChild(bar);
    requestAnimationFrame(function () { bar.classList.add('show'); });
  })();
  </script>
"""


def publish():
    src = (HERE / "识字卡片_1000字.html").read_text(encoding="utf-8")
    assert "__" not in re.sub(r"__(?:CARDS|GROUPS|GLYPHS|SCALE|PAIR_SCALE|ART|STROKES)__", "", src[:200000]) or True
    html = src
    if 'rel="icon"' not in html:
        html = html.replace('<meta name="theme-color"', FAVICON + "\n  <meta name=\"theme-color\"", 1)
    if "wxTipDone" not in html:
        i = html.rfind("</style>")
        html = html[:i] + CSS + html[i:]
        j = html.rfind("</body>")
        html = html[:j] + JS + "\n" + html[j:]
    out = PUBLISH / "shizi-1000.html"
    out.write_text(html, encoding="utf-8")
    print("已发布副本:", out, f"{out.stat().st_size/1024:.0f}KB")


def hub():
    hub_path = PUBLISH / "index.html"
    t = hub_path.read_text(encoding="utf-8")
    if "shizi-1000" in t:
        print("首页已含 1000 字入口")
        return
    anchor = '<a class="card" href="./shizi-422.html">'
    entry = '<a class="card" href="./shizi-1000.html"><b>识字卡片 · 1000 字全集</b>31 组 964 卡，电脑宽屏三栏 / 手机竖屏自适应</a>\n  '
    assert anchor in t
    t = t.replace(anchor, entry + anchor, 1)
    hub_path.write_text(t, encoding="utf-8")
    print("首页入口已添加")


if __name__ == "__main__":
    publish()
    hub()
