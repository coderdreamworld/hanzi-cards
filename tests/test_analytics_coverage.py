"""Check that every published page loads the shared analytics code."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    "index.html", "pinyin-zimu.html", "shizi-422.html", "shizi-1000.html",
    "xiangxing.html", "huiyi.html", "bushou.html", "yunyu.html", "emotion.html",
)
TAG = '<script defer src="./analytics.js"></script>'


def main():
    assert (ROOT / "analytics.js").is_file()
    assert not (ROOT / "pinyin-pindu.html").exists()
    for name in PAGES:
        html = (ROOT / name).read_text(encoding="utf-8")
        assert html.count(TAG) == 1, name
        assert html.index(TAG) < html.index("</head>"), name
    print(f"已检查 {len(PAGES)} 个发布页面的统计入口")


if __name__ == "__main__":
    main()
