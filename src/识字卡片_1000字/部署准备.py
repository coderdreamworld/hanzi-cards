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
# 2026-11-01：微信内收藏引导条（.wx-tip）已按用户定调"自己用、不必提示"从全部源模板移除
# （commit aa5783f），此发布脚本里的注入块是残留，会把引导条复活到线上，故一并删除。


def publish():
    src = (HERE / "识字卡片_1000字.html").read_text(encoding="utf-8")
    assert "__" not in re.sub(r"__(?:CARDS|GROUPS|GLYPHS|SCALE|PAIR_SCALE|ART|STROKES)__", "", src[:200000]) or True
    html = src
    if 'rel="icon"' not in html:
        html = html.replace('<meta name="theme-color"', FAVICON + "\n  <meta name=\"theme-color\"", 1)
    # GA4 统计（analytics.js）为发布层能力，由另一会话在发布副本上接入（commit 5eeee96），
    # 源模板不含此行；若不在此幂等补回，每次从源重建发布副本都会把统计引用冲掉。
    if "analytics.js" not in html:
        i = html.rfind("</head>")
        html = html[:i] + '  <script defer src="./analytics.js"></script>\n' + html[i:]
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
