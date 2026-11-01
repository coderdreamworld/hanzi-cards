#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 扩充/ 目录下的扩充数据并进汉语启蒙卡集的数据模块。

扩充数据文件（可选，缺失时静默跳过）：
    会意字_扩充数据.py    NEW_CARDS / NEW_ARTS
    部首家族_扩充数据.py  NEW_CARDS / NEW_ARTS
    韵语声音_扩充数据.py  NEW_VERSES / NEW_GAMES / NEW_ARTS

用法：
    import 扩充合并
    扩充合并.apply(sucai)      # sucai = 汉语启蒙_素材 模块
"""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_PARENT = _HERE.parent

# 文件名 → (套 id, 套定义在模块里的名字)
FILE_TARGET = {
    "会意字_扩充数据.py": "huiyi",
    "部首家族_扩充数据.py": "jiazu",
    "韵语声音_扩充数据.py": "shengyin",
}


def load_expansion(path):
    spec = importlib.util.spec_from_file_location(f"ext_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def apply(sucai, verbose=False):
    """把扩充数据并进 sucai（汉语启蒙_素材 模块）并返回并入摘要列表。"""
    summary = []
    for path in sorted(_HERE.glob("*_扩充数据.py")):
        mod = load_expansion(path)
        target = getattr(mod, "TARGET", None) or FILE_TARGET.get(path.name)
        if target is None:
            raise ValueError(f"{path.name} 不知道该并进哪一套，请设 TARGET 属性")
        set_def = {"huiyi": sucai.SET_HUIYI, "jiazu": sucai.SET_JIAZU,
                   "shengyin": sucai.SET_SHENGYIN}[target]

        arts = dict(getattr(mod, "NEW_ARTS", {}) or {})
        for k, v in arts.items():
            sucai.ARTS[k] = v
            sucai.NEW_ARTS[k] = v

        cards = list(getattr(mod, "NEW_CARDS", []) or [])
        verses = list(getattr(mod, "NEW_VERSES", []) or [])
        games = list(getattr(mod, "NEW_GAMES", []) or [])
        if target == "shengyin":
            set_def["groups"][0]["cards"].extend(verses)
            set_def["groups"][1]["cards"].extend(games)
        elif cards:
            set_def["groups"][0]["cards"].extend(cards)
        summary.append((path.name, target, len(cards), len(verses), len(games), len(arts)))
        if verbose:
            print(f"  并入 {path.name} → {target}: 卡 {len(cards)} / 韵语 {len(verses)} "
                  f"/ 游戏 {len(games)} / 新插画 {len(arts)}")
    return summary


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(_PARENT))
    spec = importlib.util.spec_from_file_location("qisucai", _PARENT / "汉语启蒙_素材.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for row in apply(m, verbose=True):
        print(row)
