#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 字库1000.py：422 全含 + 578 新字 = 1000。主题池 + 有序补充池，程序校验。"""
import importlib.util
from pathlib import Path
PARENT = Path("/Users/ping/C 行动_与人交流/孩子")
spec = importlib.util.spec_from_file_location("ziku", PARENT / "识字卡片_字库.py")
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)

legacy_entries = {g["id"]: list(g["chars"]) for g in old.GROUPS}
LEGACY = set()
for g in old.GROUPS:
    for it in g["chars"]:
        if isinstance(it, tuple): LEGACY.update(it)
        else: LEGACY.add(it["char"] if isinstance(it, dict) else it)

# ── 主题扩充池（逐字对照 422 清单去重过；值为字符串=单字卡，列表=对比卡） ──
ADD = {
 "shuzi":    "千万亿元角第倍号加减乘除等点",
 "liangci":  "支棵朵辆匹束滴份张枚座栋间次排",
 "duibi":    [("粗","细"),("厚","薄"),("深","浅"),("干","湿"),("软","硬"),("饱","饿"),("沉","浮"),("浓","淡"),
              ("宽","窄"),("阴","晴"),("卷","展"),("睁","闭"),("吞","吐"),("输","赢"),("挖","填"),("香","臭")],
 "tianwen":  "雾霜雷阳露霞雹光",
 "ziran":    "岸波浪坡谷岛穴岭峰池泉崖原野沟湖溪湾",
 "zhiwu":    "藤菌蘑菇茎稻麦棉茶枣菊桂兰笋李栗桑枝根芦苇蒲玫瑰桐柏",
 "dongwu":   "驴骆驼鹰鲸鲨雀燕鸥鹤豹猩雕鹭鹊鸵豚",
 "dongwu2":  "蚂蚁蜘蛛蜗蚊蝇蚕蝉蟋蟀蜻蜓萤猬鹦鹉蝴蚯蚓蝌蚪蛾螳螂蚱蜢蜈蚣蝎蚌螺鲤鲫蝠蜥蜴獭窝",
 "renti":    "骨汗血脑唇腿肩肘膝脖睫泪额胸掌腕腰甲拇腮颊",
 "rencheng": "婶伯朋友客姥农工兵警护司员姑舅婆娘父母伙伴孙咱您",
 "shiwu":    "糕粽馒汤汁盐醋油橙橘蕉茄萝蒜葱姜肉辣咸柿柚荔薯藕椒蜜粥菠芒莓柠檬酱鲜",
 "wupin":    "凳篮筐盘勺毛巾肥皂刷枕毯垫表缸罐铁盆锅叉碟筷照筒珠瓢",
 "changsuo": "城市乡村街园场店馆邮局厅亭巷庄堡",
 "xuexi":    "题奖室板考试名班教答页铅橡胶墨音记认识",
 "yanse":    "银紫棕",
 "shijian":  "秒季岁晨寒暑",
 "huiyi":    "品晶灶灭掰岩歪看",
 "dongzuo3": "躺趴蹲踩踏跨蹦攀登钻跃滑泳骑翻滚散奔冲梦澡望扭",
 "dongzuo4": "拎扛掀按压捏摸撕拖卷叠折系解换捉抓捧捡投抛传拧扔接递贴修扶握排追逃赶转摇摆收泼洒挑拔托切炒煮蒸尝咬嚼吞喊叫挤挥揉挠闻铺盖藏卖选抬理倒种堆补吸舔捆端竖抖逗靠搓",
 "xingrong": "静吵闹整齐乱旧累困乖勇健暖凉净丑密温烫扁紧慢熟敢矮坏假",
 "changyong": "着呢吧哦啦向往跟越让些么或刚各爱应该行能已懂嗯",
 "fushi":    "裤鞋帽袜裙扣袋脱晒衫布线绳袖领套围晾链靴带",
 "jiaotong": "车轮船帆路桥道停送站票座轨辆舵锚舱翼汽飞划港机桨",
 "gongju":   "剪锤钉锁钥匙锯斧铲蜡秤针网帚锄镰烛柴",
 "fangwu":   "房屋楼梯窗墙瓦砖床柜架层厨帘席棚被厕玻璃塔",
 "wenti":    "舞琴鼓号笛运动赛队铃涂弹吹筝积曲锣牌琵琶",
 "shehui":   "邻居礼貌请谢错借忙安话助卫夸赞",
 "qingxu":   "喜怒怕惊气欢慌羞急烦忘悲",
}
# ── 有序补充池（主题池不足时按序取用；均为低幼常用、可画） ──
EXTRAS = ["蚂","蚁","蝴","蚯","蚓","蝌","蚪","蛾","萤","蜗","蜻","蜓","蟹","虾","贝","螺","蚌","鲤","鲫","鲨","鲸",
 "豚","鹰","雕","鹭","鹊","鸵","鹤","鸥","豹","猩","雀","燕","蚕","蝉","蟋","蟀","猬","蝎","蜈","蚣","螳","螂","蚱","蜢","蝠","蜥","蜴","窝",
 "湖","溪","湾","沟","崖","原","野","泉","池","穴","岭","峰","坡","谷","岛","岸","波","浪",
 "芦","苇","蒲","玫","瑰","藤","菌","蘑","菇","茎","稻","麦","棉","茶","枣","菊","桂","兰","笋","李","栗","桑","枝","根",
 "额","胸","掌","腕","腰","甲","拇","睫","脖","肘","膝","唇","汗","血","脑","骨","泪","腿","肩",
 "父","母","伙","伴","孙","咱","您","姑","舅","婆","娘","姥","婶","伯","朋","友","客","农","工","兵","警","护","司","员",
 "筷","盆","锅","叉","碟","缸","罐","铁","照","筒","珠","毛","巾","肥","皂","刷","枕","毯","垫","表","篮","筐","盘","勺","凳",
 "烛","柴","锄","镰","锯","斧","铲","蜡","秤","针","网","帚","剪","锤","钉","锁","钥","匙",
 "塔","厕","玻","璃","厨","帘","席","棚","被","瓦","砖","柜","架","层","梯","窗","墙","床","房","屋","楼",
 "厅","亭","巷","邮","局","店","馆","场","园","街","乡","村","城","市",
 "港","机","桨","帆","舵","锚","舱","翼","汽","轨","辆","站","票","座","停","送","划","道","桥","路","船","车","轮","飞",
 "页","铅","橡","胶","墨","音","记","认","识","答","教","班","名","考","试","板","室","奖","题",
 "紫","棕","银","秒","季","岁","晨","品","晶","灶","灭","掰","岩","歪","看",
 "躺","趴","蹲","踩","踏","跨","蹦","攀","登","钻","跃","滑","泳","骑","翻","滚","散","奔","冲","梦","澡","望",
 "拎","扛","掀","按","压","捏","摸","撕","拖","卷","叠","折","系","解","换","捉","抓","捧","捡","投","抛","传","拧","扔","接","递","贴","修","扶","握","排","追","逃","赶","转","摇","摆","收","泼","洒","挑","拔","托","切","炒","煮","蒸","尝","咬","嚼","吞","喊","叫","挤","挥","揉","挠","闻","铺","盖","藏","卖","选","抬","理","倒","种","堆","补","吸","舔","捆","端","竖","抖","逗","靠",
 "静","吵","闹","整","齐","乱","旧","累","困","乖","勇","健","暖","凉","净","丑","密","温","烫","扁","紧","慢","熟","敢","矮","坏","假",
 "着","呢","吧","哦","啦","向","往","跟","越","让","些","么","或","刚","各","爱","应","该","行","能","已","懂",
 "裤","鞋","帽","袜","裙","扣","袋","脱","晒","衫","布","线","绳","袖","领","套","围","晾","链","靴","带",
 "舞","琴","鼓","号","笛","运","动","赛","队","铃","涂","弹","吹","筝","积","曲","锣","牌",
 "邻","居","礼","貌","请","谢","错","借","忙","安","话","助","卫","夸","赞",
 "喜","怒","怕","惊","气","欢","慌","羞","急","烦","忘",
 "千","万","亿","元","角","第","倍","号","加","减","乘","除","等","点","支","棵","朵","辆","匹","束","滴","份","张","枚","座","栋","间","次","排",
 "雾","霜","雷","阳","露","霞","雹","光",
 "粗","细","厚","薄","深","浅","干","湿","软","硬","饱","饿","沉","浮","浓","淡","宽","窄","阴","晴","展","睁","闭","吐","输","赢","挖","填","香","臭",
]

def to_items(s):
    return list(s)
def dedupe_add(add):
    seen = set(LEGACY); out = {}
    for gid, val in add.items():
        keep = []
        if isinstance(val, str):
            for c in val:
                if c not in seen: keep.append(c); seen.add(c)
        else:
            for p in val:
                if not any(c in seen for c in p): keep.append(tuple(p)); seen.update(p)
        out[gid] = keep
    return out

ADD = dedupe_add(ADD)
flat = [(gid, it) for gid, items in ADD.items() for it in items]
n_new = sum(len(it) if isinstance(it, tuple) else 1 for _, it in flat)
need = 1000 - len(LEGACY)
print(f"422旧字: {len(LEGACY)} | 主题池: {n_new} | 需补: {need}")
if n_new < need:
    used = set(LEGACY)
    for _, it in flat: used.update(it if isinstance(it, tuple) else [it])
    taken = []
    for c in EXTRAS:
        if n_new + len(taken) >= need: break
        if c not in used: taken.append(c); used.add(c)
    print("补充池取用:", len(taken), taken[:20], "...")
    ADD["changyong"] = ADD.get("changyong", []) + taken
    n_new = sum(len(it) if isinstance(it, tuple) else 1 for gid, items in ADD.items() for it in items)
print(f"最终新字: {n_new}")
assert n_new == need

NEW_META = {
 "dongwu2":  ("动物·虫与水", "小虫和水中伙伴，轮廓差异大，孩子最爱"),
 "fushi":    ("服饰穿戴", "身上穿的、头上戴的，天天见"),
 "gongju":   ("工具", "做活修东西的小工具"),
 "fangwu":   ("房屋建筑", "家的结构和盖房子的东西"),
 "jiaotong": ("交通出行", "车船路桥，出门就见"),
 "wenti":    ("文体游戏", "唱歌画画运动，玩里认字"),
 "shehui":   ("社会礼貌", "请谢借还，做人做事的话"),
 "qingxu":   ("情绪", "看得出的心情，配表情脸"),
 "dongzuo3": ("动作·身体", "全身做出来的动作"),
 "dongzuo4": ("动作·手部", "手做出来的细动作，一卡一动作"),
}
ORDER = ["shuzi","liangci","duibi","fangwei","tianwen","ziran","zhiwu","dongwu","dongwu2","renti","rencheng",
         "fushi","shiwu","wenti","wupin","gongju","fangwu","changsuo","jiaotong","xuexi","yanse","shijian",
         "qingxu","shehui","huiyi","dongzuo","dongzuo2","dongzuo3","dongzuo4","xingrong","changyong"]
old_meta = {g["id"]: g for g in old.GROUPS}
GROUPS = []
for gid in ORDER:
    if gid in old_meta:
        g = dict(old_meta[gid]); g["chars"] = list(legacy_entries[gid]) + ADD.get(gid, [])
    else:
        name, desc = NEW_META[gid]
        g = {"id": gid, "name": name, "desc": desc, "kind": "mix", "chars": ADD.get(gid, [])}
    GROUPS.append(g)

allc = []
for g in GROUPS:
    for it in g["chars"]:
        allc += list(it) if isinstance(it, tuple) else [it["char"] if isinstance(it, dict) else it]
assert len(allc) == len(set(allc)) == 1000, f"{len(allc)}/{len(set(allc))}"
assert LEGACY <= set(allc)
cards = sum(1 for g in GROUPS for it in g["chars"])
print(f"✓ 1000字校验通过 | {len(GROUPS)}组 | {cards}卡 (422版为402卡)")
for g in GROUPS:
    n = sum(len(it) if isinstance(it, tuple) else 1 for it in g["chars"])
    print(f"  {g['id']:10s} {g['name']:8s} {n}")

with open("字库1000.py", "w", encoding="utf-8") as f:
    f.write('#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n')
    f.write('"""幼儿识字 1000 字字库与分组（2026-10-31，31 组）。\n\n')
    f.write('前 402 条目与 422 字版完全一致（顺序与备注不变）；新字按主题并入原组或入新组。\n')
    f.write('运行自检：总数 == 1000、无重复、包含全部 422 字。\n"""\n\nGROUPS = [\n')
    for g in GROUPS:
        f.write(f'    {{ "id": "{g["id"]}", "name": "{g["name"]}", "desc": "{g.get("desc","")}", "kind": "mix", "chars": [\n')
        line = "        "
        for it in g["chars"]:
            tok = f'("{it[0]}", "{it[1]}"), ' if isinstance(it, tuple) else (
                  '{ "char": "%s", "note": "%s" }, ' % (it["char"], it.get("note","")) if isinstance(it, dict) else f'"{it}", ')
            if len(line) + len(tok) > 96: f.write(line.rstrip() + "\n"); line = "        "
            line += tok
        if line.strip(): f.write(line.rstrip() + "\n")
        f.write("    ]},\n")
    f.write("]\n\n")
    f.write('if __name__ == "__main__":\n')
    f.write('    cs = [c for g in GROUPS for it in g["chars"] for c in (list(it) if isinstance(it, tuple) else [it.get("char", it) if isinstance(it, dict) else it])]\n')
    f.write('    assert len(cs) == len(set(cs)) == 1000, f"{len(cs)}/{len(set(cs))}"\n')
    f.write('    print("字库1000 自检通过：1000 字无重复，", len(GROUPS), "组")\n')
print("字库1000.py 已写出")
