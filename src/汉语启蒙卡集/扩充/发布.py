#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把扩充后的三套启蒙卡发布为 github-pages 副本（huiyi/bushou/yunyu.html）。

发布副本 = 新构建 + 发布层增强（与现行线上页一致）：
  1. PWA 头：favicon / apple 系列 meta / touch-icon / manifest（照抄现行线上页）
  2. 首页按钮的 :active / :hover / ≤380px 补充样式（线上页有、源模板没有）
  3. GA4：analytics.js（幂等注入，源模板不含）
另：更新首页 index.html 上三个子集的数量文案。幂等，重复运行安全。
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent          # 汉语启蒙卡集/
PUBLISH = HERE.parent / "微信传播方案" / "发布" / "github-pages"

FILES = {
    "汉语启蒙_会意字卡.html": "huiyi.html",
    "汉语启蒙_部首家族卡.html": "bushou.html",
    "汉语启蒙_韵语与声音卡.html": "yunyu.html",
}

# 发布层注入块（取自现行线上页，勿改内容）
PWA_LINES = """  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="识字卡">
  <link rel="apple-touch-icon" sizes="180x180" href="touch-icon-v3.png">
  <link rel="manifest" href="./manifest.json">"""

HOME_CSS = """
    .home-btn:active{transform:scale(.94);background:#e8f4ee}
    @media(hover:hover){.home-btn:hover{background:#f6efe2}}
    @media(max-width:380px){.home-btn{padding:4px 8px}}"""


def favicon_line():
    """从现行线上 huiyi.html 抄彩虹 favicon（含渐变绘制，保持全站一致）。"""
    src = (PUBLISH / "huiyi.html").read_text(encoding="utf-8")
    m = re.search(r'^\s*(<link rel="icon" href="data:image/svg\+xml[^>]*>)\s*$', src, re.M)
    if m:
        return m.group(1)
    raise SystemExit("现行线上页找不到 favicon，拒绝发布（避免图标回退）")


def enhance(html, fav):
    if 'rel="icon"' not in html:
        pwa = "\n  ".join([fav] + [l.strip() for l in PWA_LINES.splitlines()])
        html = html.replace('<meta name="theme-color"',
                            pwa + "\n  <meta name=\"theme-color\"", 1)
    if "analytics.js" not in html:
        i = html.rfind("</head>")
        html = html[:i] + '  <script defer src="./analytics.js"></script>\n' + html[i:]
    if ".home-btn:active" not in html:
        html = html.replace("</style>", HOME_CSS + "\n  </style>", 1)
    return html


def publish():
    fav = favicon_line()
    for src_name, out_name in FILES.items():
        html = (HERE / src_name).read_text(encoding="utf-8")
        html = enhance(html, fav)
        out = PUBLISH / out_name
        backup = out.with_suffix(".html.bak")
        if out.exists() and not backup.exists():
            backup.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
        out.write_text(html, encoding="utf-8")
        print(f"已发布 {out_name}: {out.stat().st_size/1024:.0f}KB（备份 {backup.name}）")


def hub():
    hub_path = PUBLISH / "index.html"
    t = hub_path.read_text(encoding="utf-8")
    t2 = t.replace("<b>部首家族 · 找朋友</b>10 个部首家族",
                   "<b>部首家族 · 找朋友</b>19 个部首家族")
    t2 = t2.replace("<b>韵语与声音游戏</b>8 韵语 + 6 声音游戏，拼音耳朵准备",
                    "<b>韵语与声音游戏</b>14 韵语 + 10 声音游戏，拼音耳朵准备")
    if t2 != t:
        hub_path.write_text(t2, encoding="utf-8")
        print("首页数量文案已更新")
    else:
        print("首页文案已是最新")


if __name__ == "__main__":
    publish()
    hub()
