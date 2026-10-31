#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用卡片级哈希锁定一次修改的允许范围。

推荐流程：
  python3 识字卡片_修改范围.py begin 爸 医 飞
  # 只修改上述卡片
  python3 识字卡片_修改范围.py check
  python3 识字卡片_构建.py
  python3 识字卡片_修改范围.py finish

默认要求“实际变更集合 == 点名集合”：既拦截误改，也拦截漏改。
"""

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

import 识字卡片_构建 as builder


ROOT = Path(__file__).resolve().parent
STATE = ROOT / ".识字卡片_修改范围.json"
VALID_FIELDS = ("art", "content", "group", "position")
PROTECTED_FILES = (
    "识字卡片_模板.html",
    "识字卡片_构建.py",
    "识字卡片_字库.py",
    "识字卡片_素材库.py",
    "识字卡片_修改范围.py",
)


def digest(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def protected_hashes():
    return {
        name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        for name in PROTECTED_FILES
    }


def snapshot(groups=None, art_map=None):
    """返回最终解析后的逐卡哈希；共享组件扩散也会反映到受影响卡片。"""
    if groups is None or art_map is None:
        groups, art_map = builder.resolve_deck()
    cards = {}
    for group_position, group in enumerate(groups):
        for card_position, card in enumerate(group["cards"]):
            key = card["key"]
            content_hash = digest(card)
            art_hash = digest(art_map[key])
            cards[key] = {
                "group": group["id"],
                "position": f"{group_position}:{card_position}",
                "content": content_hash,
                "art": art_hash,
                "payload": digest({
                    "group": group["id"],
                    "position": f"{group_position}:{card_position}",
                    "content": content_hash,
                    "art": art_hash,
                }),
            }
    return cards


def read_state():
    if not STATE.exists():
        raise SystemExit("没有进行中的修改范围。请先运行 begin 并列出用户点名的卡片。")
    return json.loads(STATE.read_text(encoding="utf-8"))


def differences(before, after):
    details = {}
    for key in sorted(set(before) | set(after)):
        if key not in before:
            details[key] = ["新增卡片"]
            continue
        if key not in after:
            details[key] = ["删除卡片"]
            continue
        fields = [
            name for name in ("group", "position", "content", "art")
            if name in before[key] and name in after[key] and before[key][name] != after[key][name]
        ]
        if fields:
            details[key] = fields
    return details


def assess(before, after, allowed, allowed_fields_by_card=None, allow_unchanged=False):
    details = differences(before, after)
    changed = set(details)
    allowed = set(allowed)
    allowed_fields_by_card = allowed_fields_by_card or {key: ["art"] for key in allowed}
    unexpected = sorted(changed - allowed)
    missing = [] if allow_unchanged else sorted(allowed - changed)
    field_violations = {
        key: sorted(set(fields) - set(allowed_fields_by_card.get(key, ())))
        for key, fields in details.items()
        if key in allowed and set(fields) - set(allowed_fields_by_card.get(key, ()))
    }
    return details, unexpected, missing, field_violations


def fields_by_card(state):
    """兼容本轮开始时生成的旧版统一字段状态。"""
    if "allowed_fields_by_card" in state:
        return state["allowed_fields_by_card"]
    fields = state.get("allowed_fields", ["art"])
    return {key: fields for key in state["allowed"]}


def print_result(state, allow_unchanged=False, current=None):
    current = current or snapshot()
    allowed_fields = fields_by_card(state)
    details, unexpected, missing, field_violations = assess(
        state["baseline"], current, state["allowed"], allowed_fields,
        allow_unchanged=allow_unchanged,
    )
    changed_text = "、".join(f"{key}({'+'.join(fields)})" for key, fields in details.items()) or "无"
    print("点名卡片：" + "、".join(state["allowed"]))
    print("逐卡允许字段：" + "、".join(
        f"{key}({'+'.join(allowed_fields[key])})" for key in state["allowed"]
    ))
    print("实际变更：" + changed_text)
    if unexpected:
        print("[失败] 越界修改：" + "、".join(unexpected))
    if missing:
        print("[失败] 点名但未修改：" + "、".join(missing))
    if field_violations:
        text = "、".join(f"{key}({'+'.join(fields)})" for key, fields in field_violations.items())
        print("[失败] 点名卡片改了未授权字段：" + text)
    protected_changes = []
    if "protected" in state:
        current_protected = protected_hashes()
        protected_changes = [
            name for name, old_hash in state["protected"].items()
            if current_protected.get(name) != old_hash
        ]
        if protected_changes:
            print("[失败] 卡片任务中修改了全局保护文件：" + "、".join(protected_changes))
    if unexpected or missing or field_violations or protected_changes:
        return False
    print("范围校验通过：实际变更集合与点名集合一致 ✓")
    return True


def command_begin(args):
    if STATE.exists():
        raise SystemExit(f"已有进行中的修改范围：{STATE.name}。请先 check/finish。")

    groups, arts = builder.resolve_deck()
    compiled = builder.render_document(groups, arts)
    if not builder.OUT.exists() or builder.OUT.read_text(encoding="utf-8") != compiled:
        raise SystemExit(
            "当前源码与正式 HTML 已有未登记差异，不能在变化发生后补开范围。"
            "请先查明并恢复一致状态。"
        )

    baseline = snapshot(groups, arts)
    allowed_fields = {}
    for spec in args.cards:
        key, separator, raw_fields = spec.partition(":")
        fields = raw_fields.split(",") if separator else ["art"]
        if not key or not all(fields) or any(field not in VALID_FIELDS for field in fields):
            raise SystemExit(
                f"无效范围：{spec}。格式示例：爸 或 的:art,content；"
                f"可用字段：{','.join(VALID_FIELDS)}"
            )
        if key in allowed_fields:
            raise SystemExit(f"卡片重复点名：{key}")
        allowed_fields[key] = fields
    requested = list(allowed_fields)
    unknown = [key for key in requested if key not in baseline]
    if unknown:
        raise SystemExit("不存在的卡片：" + "、".join(unknown))
    state = {
        "version": 1,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "allowed": requested,
        "allowed_fields_by_card": allowed_fields,
        "protected": protected_hashes(),
        "baseline": baseline,
    }
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"已锁定 {len(requested)} 张：" + "、".join(requested))
    print("完成修改后运行 check；交付前运行 finish。")


def command_check(args):
    groups, arts = builder.resolve_deck()
    if args.expected_deck and builder.deck_digest(groups, arts) != args.expected_deck:
        raise SystemExit("范围检查解析结果与构建器待写结果不一致，已拒绝构建。")
    if not print_result(read_state(), current=snapshot(groups, arts)):
        raise SystemExit(1)


def command_finish(_args):
    state = read_state()
    groups, arts = builder.resolve_deck()
    if not print_result(state, current=snapshot(groups, arts)):
        raise SystemExit(1)
    compiled = builder.render_document(groups, arts)
    if not builder.OUT.exists() or builder.OUT.read_text(encoding="utf-8") != compiled:
        raise SystemExit("正式 HTML 与已校验源码不一致，请先构建并完成浏览器核验。")
    STATE.unlink()
    print("修改范围已结案。")


def command_status(_args):
    state = read_state()
    print(f"开始时间：{state['created_at']}")
    print("点名卡片：" + "、".join(state["allowed"]))
    print_result(state, allow_unchanged=True)


def command_self_test(_args):
    base = {
        "甲": {"group": "g", "position": "0:0", "content": "c1", "art": "a1", "payload": "p1"},
        "乙": {"group": "g", "position": "0:1", "content": "c2", "art": "a2", "payload": "p2"},
    }
    only_a = {key: dict(value) for key, value in base.items()}
    only_a["甲"]["art"] = "changed"
    details, unexpected, missing, violations = assess(base, only_a, ["甲"], {"甲": ["art"]})
    assert set(details) == {"甲"} and not unexpected and not missing and not violations
    _, unexpected, missing, _ = assess(
        base, only_a, ["甲", "乙"], {"甲": ["art"], "乙": ["art"]}
    )
    assert not unexpected and missing == ["乙"]
    _, unexpected, missing, _ = assess(base, only_a, ["乙"], {"乙": ["art"]})
    assert unexpected == ["甲"] and missing == ["乙"]
    content_change = {key: dict(value) for key, value in base.items()}
    content_change["甲"]["content"] = "changed"
    _, _, _, violations = assess(base, content_change, ["甲"], {"甲": ["art"]})
    assert violations == {"甲": ["content"]}
    reordered = {key: dict(value) for key, value in base.items()}
    reordered["甲"]["position"] = "0:1"
    _, _, _, violations = assess(base, reordered, ["甲"], {"甲": ["art"]})
    assert violations == {"甲": ["position"]}
    print("范围校验器自测通过 ✓")


def make_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    begin = sub.add_parser("begin", help="修改前锁定用户点名卡片")
    begin.add_argument(
        "cards", nargs="+",
        help="卡片 key；默认仅 art。逐卡放宽示例：的:art,content 条:content",
    )
    begin.set_defaults(func=command_begin)
    for name, func, help_text in (
        ("check", command_check, "检查是否误改或漏改"),
        ("finish", command_finish, "校验通过后结束本轮范围"),
    ):
        cmd = sub.add_parser(name, help=help_text)
        if name == "check":
            cmd.add_argument(
                "--expected-deck",
                help="由构建器传入的解析结果摘要，用来防止检查与写入对象不一致",
            )
        cmd.set_defaults(func=func)
    status = sub.add_parser("status", help="查看当前范围和变更")
    status.set_defaults(func=command_status)
    self_test = sub.add_parser("self-test", help="运行隔离逻辑回归测试")
    self_test.set_defaults(func=command_self_test)
    return parser


if __name__ == "__main__":
    arguments = make_parser().parse_args()
    arguments.func(arguments)
