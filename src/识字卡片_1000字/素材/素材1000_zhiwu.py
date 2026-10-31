#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""植物组新增 25 卡插画与文案（1000 字批次 B6）。

字表：藤菌蘑菇茎稻麦棉枣菊桂兰笋李栗桑枝根芦苇蒲玫瑰桐柏
（前 23 字 花草木叶树果瓜苗竹豆莲杏桃荷松梅柳枫 + 迁移 子禾皮苹芽
 在 legacy ../识字卡片_素材_zhiwu.py，本文件不重复）。

与 legacy 错造型：legacy 是 橙花五瓣/草丛/发芽小树/大叶/圆冠树/苹果树/
条纹瓜/土里芽/竹竿/豆荚/池塘莲蓬/黄杏枝/粉桃/单支荷花/三层松塔/
梅枝粉花/垂柳/红枫（+迁移卡），本批全部换主体：
棚架紫藤/木头上的橙菌/红伞白点大蘑菇/草丛褐菇/粗茎特写/金黄垂稻穗/
直立麦芒穗/白棉桃开裂/深红长枣/金菊绒球/桂花小簇/盆栽兰草/破土笋尖/
紫李/刺球栗/紫桑果/木枝绿叶/土中根系/单株大芦花/水边苇丛/蒲棒香蒲/
单朵红玫瑰/玫瑰丛+花苞/大圆叶桐树/塔形柏树。

一眼可辨约定（主控硬规则）：稻=金黄稻穗下垂、麦=麦芒穗直立、棉=白棉桃开裂、
笋=破土笋尖、菌蘑菇=伞盖（菌=木头+橙菇、蘑=红伞白点单朵、菇=褐菇一丛）、
芦苇=芦花穗（芦=单株特写、苇=水边一丛）、玫瑰=红花刺茎（玫=单朵特写、
瑰=丛+花苞）、藤=缠绕棚架、桐柏=大树整株（桐=大圆叶、柏=塔形鳞叶，
与 legacy 松的三角针叶塔区分）。同组邻居卡轮廓+主色错开。
"""
import importlib.util
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, "/Users/ping/C 行动_与人交流/孩子")
from 识字卡片_素材库 import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent          # .../识字卡片_1000字/素材
ROOT = HERE.parent                              # .../识字卡片_1000字

# ---------- 本组同族补充色 ----------
LEAF_D, LEAF_DD, LEAF_V = "#5e8f52", "#4a7a3e", "#d4e8b0"
FRESH = "#8fca6f"
TONG_L = "#a2d684"                       # 桐叶亮面
STEM_G, STEM_HI, NODE = "#9cc98a", "#c8e0a8", "#5e8f52"
SOIL, SOIL_D, SOIL_L = "#8a5a38", "#6b4322", "#a9744a"
RICE, RICE_D, RICE_L = "#d9a53c", "#b9852a", "#eec95e"
STRAW = "#b5a642"                        # 稻秆黄绿
WHEAT_C, WHEAT_D, AWN = "#e8c84e", "#c9a032", "#d9b458"
JUJUBE, JUJUBE_D, JUJUBE_L = "#a83226", "#8a281e", "#c05246"
PLUMF, PLUMF_D = "#9a5ab8", "#7a449a"
BUR, BUR_D, NUT, NUT_D = "#6a9a5c", "#557f4a", "#a9743f", "#8a5a33"
MUL, MUL_L, MUL_D = "#b04a8a", "#c86aa2", "#93386f"
SHROOM_R = "#d4552f"                     # 蘑：红伞白点
SHROOM_O, SHROOM_O_D = "#f0913c", "#d97b28"   # 菌：橙菇
SHROOM_T, SHROOM_T_D = "#c9a06a", "#b0885a"   # 菇：褐菇
LOG, LOG_L, LOG_RING = "#8a5a33", "#a9743f", "#c99a68"
WIST, WIST_D = "#b48fd0", "#9a74b8"
ORCH, ORCH_D = "#c79ad6", "#a276c0"
OSM, OSM_D = "#f0913c", "#d97b28"
CYP_D, CYP, CYP_L = "#35705a", "#3f8468", "#4d9877"   # 柏：偏蓝绿，别于 legacy 松
PLUME, PLUME_D = "#e8dcc0", "#cdbb96"    # 芦花
CIGAR, CIGAR_D = "#7a4a28", "#63381c"    # 蒲棒
ROSE_C, ROSE_D2, ROSE_L2 = "#d84a52", "#b23444", "#e8767e"
ROOTC, ROOTC_D = "#e9c08a", "#d3a86e"
BRANCH_B = "#8a5a33"                     # 果枝棕
BARK = "#6b4a33"                         # 深棕（梅枝同族更深）


GROUP_CARDS = [
    {"char": "藤", "pinyin": "téng", "tone": "第二声",
     "sentence": "藤蔓爬满了架子。",
     "say": "藤是会缠绕的蔓，顺着架子一圈圈往上爬。",
     "chat": "“藤为什么要绕着架子长呀？”",
     "life": "指指小区爬满墙的藤，看它绕了几圈。"},
    {"char": "菌", "pinyin": "jūn", "tone": "第一声",
     "sentence": "蘑菇就是一种菌。",
     "say": "菌像撑开的小伞，蘑菇就是菌的一种。",
     "chat": "“雨后木头上会不会冒出小菌？”",
     "life": "雨后找找木头上冒出的小菌，只能看不能吃。"},
    {"char": "蘑", "pinyin": "mó", "tone": "第二声",
     "sentence": "大蘑菇像把小伞。",
     "say": "红伞伞白杆杆，伞盖上还有白点点。",
     "chat": "“蘑菇的伞盖下面藏着什么？”",
     "life": "用积木搭一个蘑菇给你看。"},
    {"char": "菇", "pinyin": "gū", "tone": "第一声",
     "sentence": "一丛小菇靠在一起。",
     "say": "一朵朵小菇挤在一起，像一排小伞。",
     "chat": "“数一数，图上有几朵菇？”",
     "life": "跟大人去超市认认白白的口蘑。"},
    {"char": "茎", "pinyin": "jīng", "tone": "第一声",
     "sentence": "直直的茎顶着花苞。",
     "say": "粗粗的茎像吸管，把水送上叶片和花朵。",
     "chat": "“茎帮植物做什么呀？”",
     "life": "掰一根芹菜茎，看看里面的细管子。"},
    {"char": "稻", "pinyin": "dào", "tone": "第四声",
     "sentence": "金黄的稻穗弯了腰。",
     "say": "稻子熟了，一串串谷穗压得弯下腰。",
     "chat": "“香香的米饭是稻子变来的吗？”",
     "life": "吃饭时看看碗里白白的米。"},
    {"char": "麦", "pinyin": "mài", "tone": "第四声",
     "sentence": "麦穗长着细细的芒。",
     "say": "直直的麦秆顶着麦穗，还翘着细细的芒。",
     "chat": "“麦芒像不像细细的针？”",
     "life": "吃馒头时说：这是麦子磨的面做的。"},
    {"char": "棉", "pinyin": "mián", "tone": "第二声",
     "sentence": "棉桃裂开吐出白棉。",
     "say": "棉桃熟了裂开口，露出白白软软的棉花。",
     "chat": "“你的小棉袄里装着什么呀？”",
     "life": "摸摸棉被，感受软软的棉。"},
    {"char": "枣", "pinyin": "zǎo", "tone": "第三声",
     "sentence": "树上的枣红了。",
     "say": "枣子红红小小的，挂在枝头一串串。",
     "chat": "“枣是圆圆的还是长长的？”",
     "life": "吃两颗红枣，把核种进花盆。"},
    {"char": "菊", "pinyin": "jú", "tone": "第二声",
     "sentence": "秋天菊花开满园。",
     "say": "菊花的花瓣又细又多，像卷卷的绒球。",
     "chat": "“菊花是什么季节开的？”",
     "life": "秋游看菊花，数数花瓣有多少。"},
    {"char": "桂", "pinyin": "guì", "tone": "第四声",
     "sentence": "桂花香香飘满院。",
     "say": "桂花小小的、黄黄的，藏在绿叶里，特别香。",
     "chat": "“闻一闻，桂花是什么香味？”",
     "life": "秋天闻闻小区里的桂花香。"},
    {"char": "兰", "pinyin": "lán", "tone": "第二声",
     "sentence": "兰花开在花盆里。",
     "say": "兰花的叶子细细长长，花朵清清秀秀的。",
     "chat": "“兰花的叶子和别的花哪里不一样？”",
     "life": "去花店找一盆兰花闻一闻。"},
    {"char": "笋", "pinyin": "sǔn", "tone": "第三声",
     "sentence": "春雨后笋芽钻出土。",
     "say": "笋尖尖的，穿着一层层外衣，从土里钻出来。",
     "chat": "“笋长大以后会变成什么？”",
     "life": "摸摸菜市场的笋，说说它的外衣。"},
    {"char": "李", "pinyin": "lǐ", "tone": "第三声",
     "sentence": "树上的李子熟了。",
     "say": "李子圆圆的、紫紫的，挂满了枝头。",
     "chat": "“李子和苹果颜色哪里不一样？”",
     "life": "洗一颗李子尝尝酸甜。"},
    {"char": "栗", "pinyin": "lì", "tone": "第四声",
     "sentence": "栗子穿着刺外壳。",
     "say": "栗子外面是刺球壳，里面藏着光溜溜的果子。",
     "chat": "“猜猜刺壳里住着谁？”",
     "life": "剥一颗糖炒栗子尝一尝。"},
    {"char": "桑", "pinyin": "sāng", "tone": "第一声",
     "sentence": "桑叶喂给蚕宝宝。",
     "say": "桑树结出紫红的桑果，叶子是蚕宝宝的饭。",
     "chat": "“蚕宝宝最爱吃什么叶子？”",
     "life": "找一片桑叶，看看它的边边。"},
    {"char": "枝", "pinyin": "zhī", "tone": "第一声",
     "sentence": "树枝上长着绿叶。",
     "say": "枝是从树干上分出来的杈，能挂住叶子和果子。",
     "chat": "“大树的手臂像不像枝条？”",
     "life": "捡一根掉落的树枝，摆个造型。"},
    {"char": "根", "pinyin": "gēn", "tone": "第一声",
     "sentence": "大树把根扎进土里。",
     "say": "根藏在土里，像手掌一样抓住泥土喝水。",
     "chat": "“植物的根有什么用呀？”",
     "life": "拔一根小草，看看它的根。"},
    {"char": "芦", "pinyin": "lú", "tone": "第二声",
     "sentence": "芦花白白的像羽毛。",
     "say": "芦苇顶上开着一穗白白软软的芦花。",
     "chat": "“风吹过来，芦花会怎么样？”",
     "life": "用棉花粘一穗白白的芦花。"},
    {"char": "苇", "pinyin": "wěi", "tone": "第三声",
     "sentence": "水边的苇丛沙沙响。",
     "say": "一丛丛细高的苇，长在池塘和河边。",
     "chat": "“苇丛里可能藏着谁的家？”",
     "life": "经过水边，找找高高的苇丛。"},
    {"char": "蒲", "pinyin": "pú", "tone": "第二声",
     "sentence": "蒲棒像根小腊肠。",
     "say": "香蒲顶着一根根棕色的小蒲棒，像小香肠。",
     "chat": "“蒲棒摸起来是硬还是软？”",
     "life": "逛公园水池边找找蒲棒。"},
    {"char": "玫", "pinyin": "méi", "tone": "第二声",
     "sentence": "红玫瑰开得真艳。",
     "say": "这朵红红的花叫玫瑰，茎上还有小刺。",
     "chat": "“玫瑰的茎上藏着什么？”",
     "life": "母亲节送妈妈一支玫瑰。"},
    {"char": "瑰", "pinyin": "guī", "tone": "第一声",
     "sentence": "玫瑰园里花苞多。",
     "say": "玫瑰有开好的，也有没打开的小花苞。",
     "chat": "“花苞打开后会变成什么？”",
     "life": "数数小区的玫瑰开了几朵。"},
    {"char": "桐", "pinyin": "tóng", "tone": "第二声",
     "sentence": "桐树长着大圆叶。",
     "say": "桐树的叶子又大又圆，像一把把小扇子。",
     "chat": "“桐叶和你的手掌谁大？”",
     "life": "捡一片大桐叶当扇子扇一扇。"},
    {"char": "柏", "pinyin": "bǎi", "tone": "第三声",
     "sentence": "柏树一年四季绿。",
     "say": "柏树长得又高又直，像一座绿宝塔。",
     "chat": "“柏树冬天落叶吗？”",
     "life": "找找小区里的柏树，抱一抱树干。"},
]


# ---------- 本地组件 ----------
def place(inner, x, y, rot=0, s=1.0):
    """把以原点为基准的图形平移/旋转/缩放到 (x,y)。"""
    t = f"translate({x},{y})"
    if rot:
        t += f" rotate({rot})"
    if s != 1.0:
        t += f" scale({s})"
    return f'<g transform="{t}">{inner}</g>'


def leaf(ln, wd, fill):
    """尖头椭圆叶：原点在叶柄，叶尖指向 +x 方向。"""
    return P(f"M 0 0 Q {ln * 0.42} {-wd} {ln} 0 Q {ln * 0.42} {wd} 0 0 Z", fill)


def leaf_veined(ln, wd, fill, vein=LEAF_V):
    """带主脉的叶子。"""
    return leaf(ln, wd, fill) + L(10, 0, ln - 12, 0, vein, 3.5)


def petal_up(ln, wd, fill):
    """尖头花瓣：原点在花蒂，花瓣指向 -y（向上）。"""
    return P(f"M 0 0 Q {-wd} {-ln * 0.45} 0 {-ln} Q {wd} {-ln * 0.45} 0 0 Z", fill)


# ---------- 各卡插画 ----------
def art_teng():
    """藤：木棚架 + 左右缠绕的绿蔓 + 垂挂的紫藤花串。"""
    g = ground()
    for px in (246, 514):
        g += R(px - 10, 160, 20, 286, 8, WOOD_D)
    for sy in (196, 268, 340, 412):
        g += R(226, sy, 308, 13, 6, WOOD)
    vine_l = P("M 322 446 Q 284 412 322 380 Q 360 348 322 316 Q 284 284 322 252 "
               "Q 360 220 322 188 Q 300 166 314 148", stroke=LEAF_D, w=9)
    vine_r = P("M 438 446 Q 476 412 438 380 Q 400 348 438 316 Q 476 284 438 252 "
               "Q 400 220 438 188 Q 458 168 448 152", stroke=LEAF_D, w=9)
    g += vine_l + vine_r
    for tx, ty in [(352, 296), (306, 224), (444, 350), (412, 232)]:
        g += P(f"M {tx} {ty} q 16 -4 14 -18 q -3 -10 -14 -6", stroke=LEAF_D, w=4)
    for lx, ly, rot in [(330, 356, -150), (346, 262, -30), (438, 300, 208),
                        (424, 212, -20), (360, 180, -60)]:
        g += place(leaf_veined(72, 26, GREEN), lx, ly, rot)
    for cx, cy in [(322, 200), (438, 172)]:
        g += (E(cx + 4, cy + 4, 17, 21, WIST_D) + E(cx, cy, 17, 21, WIST)
              + E(cx, cy + 34, 14, 17, WIST) + E(cx + 1, cy + 62, 11, 13, WIST)
              + E(cx - 1, cy + 84, 8, 10, WIST_D))
    g += E(560, 442, 60, 12, LEAF_V, 0.7) + E(200, 444, 50, 10, LEAF_V, 0.6)
    return g


def art_jun():
    """菌：横放的老木头，顶上冒出三朵橙伞小菌。"""
    g = ground()
    g += R(150, 316, 460, 92, 42, LOG)
    g += R(150, 316, 460, 30, 15, LOG_L)
    for bx in (220, 300, 440, 520):
        g += L(bx, 360, bx - 8, 396, SOIL_D, 5)
    g += C(230, 342, 14, GREEN_L, 0.9) + C(486, 336, 11, GREEN, 0.85) + C(210, 348, 8, GREEN, 0.8)
    g += E(596, 362, 22, 46, LOG_L) + E(596, 362, 13, 28, LOG_RING) + C(596, 362, 5, SOIL_D)
    for sx, sc in [(286, 0.62), (387, 1.0), (498, 0.72)]:
        cap_w, cap_h = 134 * sc, 58 * sc
        stem_w, stem_h = 30 * sc, 52 * sc
        base_y = 322
        g += R(sx - stem_w / 2, base_y - stem_h, stem_w, stem_h, stem_w * 0.4, WHITE)
        g += P(f"M {sx - cap_w / 2} {base_y - stem_h + 4} "
               f"Q {sx - cap_w / 2 + 5} {base_y - stem_h - cap_h} {sx} {base_y - stem_h - cap_h} "
               f"Q {sx + cap_w / 2 - 5} {base_y - stem_h - cap_h} {sx + cap_w / 2} {base_y - stem_h + 4} "
               f"Q {sx} {base_y - stem_h + 18} {sx - cap_w / 2} {base_y - stem_h + 4} Z", SHROOM_O)
        g += E(sx, base_y - stem_h + 5, cap_w / 2 - 2, 10 * sc, SHROOM_O_D)
        g += C(sx - cap_w * 0.22, base_y - stem_h - cap_h * 0.5, 9 * sc, WHITE, 0.65)
    g += place(leaf(58, 13, GREEN_L), 620, 438, -40)
    return g


def art_mo():
    """蘑：单朵大蘑菇特写——红伞盖白斑点，白胖伞柄。"""
    g = ground()
    g += R(348, 258, 64, 182, 28, WHITE)
    g += R(386, 266, 20, 168, 10, "#e0dad0")
    g += E(380, 436, 46, 12, "#e0dad0")
    g += E(380, 270, 150, 26, "#b8403a")
    g += P("M 232 270 Q 238 148 380 148 Q 522 148 528 270 Q 380 302 232 270 Z", SHROOM_R)
    for sx, sy, sr in [(320, 212, 20), (432, 196, 14), (472, 240, 12),
                       (270, 248, 11), (380, 176, 9), (356, 250, 7)]:
        g += C(sx, sy, sr, WHITE)
    g += P("M 268 196 Q 320 158 380 152", stroke="#ef8073", w=9)
    for gx, gy in [(300, 438), (462, 440), (288, 444)]:
        g += place(leaf(58, 12, GREEN_L), gx, gy, -35)
    g += place(leaf(58, 12, GREEN), 452, 446, 210)
    return g


def art_gu():
    """菇：草丛里一丛褐伞小菇（一大两小），与红蘑/橙菌区分。"""
    g = ground()
    g += E(380, 428, 160, 30, GREEN_L)
    # 大菇
    g += R(312, 302, 36, 122, 15, WHITE)
    g += R(334, 310, 12, 110, 6, "#e0dad0")
    g += E(330, 306, 66, 12, SHROOM_T_D)
    g += P("M 266 302 Q 270 244 330 244 Q 390 244 394 302 Q 330 316 266 302 Z", SHROOM_T)
    g += P("M 296 262 Q 316 248 336 250", stroke="#dab98a", w=7)
    # 小菇右
    g += R(428, 330, 26, 88, 11, WHITE)
    g += E(440, 332, 48, 9, SHROOM_T_D)
    g += P("M 394 328 Q 398 288 441 288 Q 484 288 488 328 Q 441 338 394 328 Z", SHROOM_T)
    # 小菇左
    g += R(242, 352, 22, 72, 10, WHITE)
    g += E(252, 354, 40, 8, SHROOM_T_D)
    g += P("M 214 350 Q 218 318 252 318 Q 286 318 290 350 Q 252 358 214 350 Z", SHROOM_T)
    for bx, by, rot in [(420, 432, -35), (350, 436, 208), (282, 430, -60),
                        (486, 438, -30), (216, 436, 200)]:
        g += place(leaf(60, 12, GREEN), bx, by, rot)
    return g


def art_jing():
    """茎：粗壮的绿茎特写——茎上两片大叶、顶上饱满的花苞。"""
    g = ground()
    g += E(380, 436, 120, 24, SOIL) + E(380, 430, 112, 20, SOIL_L)
    g += R(356, 148, 48, 286, 20, STEM_G)
    g += R(366, 158, 14, 268, 7, STEM_HI)
    for ny in (298, 392):
        g += R(352, ny, 56, 11, 5, NODE)
    g += place(leaf_veined(122, 42, GREEN), 358, 304, 206)
    g += place(leaf_veined(122, 42, GREEN_L), 402, 398, -26)
    g += P("M 380 148 Q 344 112 380 64 Q 416 112 380 148 Z", FRESH)
    g += P("M 380 148 Q 366 120 380 88", stroke=LEAF_D, w=5)
    g += P("M 380 148 Q 362 142 350 128", stroke=NODE, w=7)
    g += P("M 380 148 Q 398 142 410 128", stroke=NODE, w=7)
    return g


def rice_ear(s=1.0):
    """下垂的稻穗（本地坐标：穗轴向下垂，谷粒左右交错）。"""
    g = L(0, 0, 2, 122 * s, "#c9a84a", 5 * s)
    for i in range(9):
        y = (18 + 116 * i / 8) * s
        side = 1 if i % 2 else -1
        a = 36 + 20 * i / 8
        g += f'<g transform="translate({side * 15 * s:.0f},{y:.0f}) rotate({side * a:.0f})">' \
             + E(0, 0, 10 * s, 16 * s, RICE) + E(1.5 * s, 2 * s, 9 * s, 14.5 * s, RICE_L) + "</g>"
    g += E(0, 152 * s, 9 * s, 15 * s, RICE)
    return g


def art_dao():
    """稻：三株金黄稻秆，穗头沉甸甸向下垂。"""
    g = ground()
    g += P("M 372 446 Q 366 380 300 320 Q 282 302 276 286", stroke=STRAW, w=10)
    g += P("M 386 446 Q 384 350 384 260 Q 384 230 386 206", stroke=STRAW, w=11)
    g += P("M 400 446 Q 410 372 462 316 Q 478 300 486 288", stroke=STRAW, w=10)
    g += place(leaf_veined(150, 20, "#a8b86a", LEAF_V), 378, 400, 158)
    g += place(leaf_veined(140, 18, "#b5c274", LEAF_V), 390, 380, 18)
    g += place(leaf_veined(130, 18, "#a8b86a", LEAF_V), 302, 356, 206)
    g += place(leaf_veined(126, 16, "#b5c274", LEAF_V), 458, 366, -16)
    g += place(rice_ear(1.05), 276, 286, -38)
    g += place(rice_ear(1.2), 386, 206, -4)
    g += place(rice_ear(1.05), 486, 288, 38)
    return g


def wheat_ear(x, top, s=1.0):
    """直立麦穗：左右交错的麦粒 + 顶上四根长麦芒。"""
    g = ""
    for i in range(7):
        y = top + i * 15 * s
        g += place(leaf(36 * s, 12 * s, WHEAT_C), x, y, 202)
        g += place(leaf(36 * s, 12 * s, WHEAT_D), x, y, 338)
    g += place(leaf(32 * s, 11 * s, WHEAT_C), x, top - 4 * s, 270)
    for dx in (-16, -6, 6, 16):
        g += L(x + dx * s, top + 20 * s, x + dx * 2.4 * s, top - 70 * s, AWN, 3.5)
    return g


def art_mai():
    """麦：四株直立的麦秆，穗尖翘着细细长芒。"""
    g = ground()
    for i, (sx, sh) in enumerate([(286, 0.9), (350, 1.05), (416, 1.0), (478, 0.88)]):
        g += L(sx, 444, sx, 444 - 170 * sh, "#c9a032", 7)
        g += place(leaf(120 * sh, 15, "#c9b458"), sx, 444 - 52 * sh, 196 + i * 4)
        g += place(leaf(110 * sh, 14, "#d6c468"), sx, 444 - 78 * sh, -14 - i * 3)
        g += wheat_ear(sx, 444 - 170 * sh, sh)
    return g


def art_mian():
    """棉：棉枝上三朵裂开的棉桃，雪白棉絮又大又醒目。"""
    g = ground()
    g += P("M 380 446 Q 374 350 380 216", stroke=LEAF_D, w=13)
    g += P("M 378 336 Q 330 316 300 296", stroke=LEAF_D, w=9)
    g += P("M 380 306 Q 430 294 462 316", stroke=LEAF_D, w=9)
    g += P("M 379 250 Q 380 232 380 216", stroke=LEAF_D, w=8)
    g += place(leaf_veined(104, 34, GREEN), 374, 380, 212)
    g += place(leaf_veined(104, 34, GREEN_L), 388, 350, -26)
    g += place(leaf_veined(84, 28, "#6a9a5c"), 330, 318, 200)
    g += place(leaf_veined(84, 28, "#6a9a5c"), 436, 336, -18)

    def boll(cx, cy, s=1.0):
        return (C(cx - 19 * s, cy + 5 * s, 21 * s, "#e6e0d0")
                + C(cx - 14 * s, cy, 20 * s, WHITE) + C(cx + 13 * s, cy + 2 * s, 20 * s, WHITE)
                + C(cx, cy - 12 * s, 22 * s, WHITE) + C(cx + 2 * s, cy + 8 * s, 17 * s, "#f4f0e6")
                + PG([(cx - 36 * s, cy + 18 * s), (cx - 12 * s, cy + 12 * s), (cx - 20 * s, cy + 38 * s)], "#8a5a33")
                + PG([(cx + 36 * s, cy + 18 * s), (cx + 12 * s, cy + 12 * s), (cx + 20 * s, cy + 38 * s)], "#8a5a33")
                + PG([(cx - 8 * s, cy + 20 * s), (cx + 8 * s, cy + 20 * s), (cx, cy + 44 * s)], "#8a5a33"))

    g += boll(300, 282, 0.95)
    g += boll(462, 302, 0.9)
    g += boll(380, 178, 1.1)
    g += C(380, 148, 6, "#8a5a33")
    return g


def art_zao():
    """枣：斜伸的枝条挂深红长枣，配小碎叶。"""
    g = ground()
    g += P("M 110 402 Q 250 340 410 306 Q 540 278 648 262", stroke=BRANCH_B, w=20)
    g += P("M 300 330 Q 320 366 316 402", stroke=BRANCH_B, w=11)
    g += P("M 470 292 Q 500 320 504 356", stroke=BRANCH_B, w=10)
    for lx, ly, rot in [(210, 344, -30), (350, 316, -18), (520, 282, -14),
                        (600, 268, -10), (180, 366, 16), (430, 300, -22)]:
        g += place(leaf_veined(66, 20, GREEN), lx, ly, rot)
    for fx, fy in [(252, 388), (318, 372), (398, 352), (508, 380), (576, 312)]:
        g += L(fx, fy - 26, fx + 2, fy - 44, "#8a5a33", 5)
        g += (E(fx + 3, fy + 3, 19, 28, JUJUBE_D) + E(fx, fy, 19, 28, JUJUBE)
              + E(fx - 6, fy - 10, 6, 10, JUJUBE_L, 0.8))
    return g


def chrys_bloom(cx, cy, s=1.0):
    """金菊绒球：外 16 瓣 + 内 12 细瓣 + 小花心。"""
    g = ""
    for i in range(16):
        g += f'<g transform="translate({cx},{cy}) rotate({i * 22.5:.0f})">{petal_up(112 * s, 15 * s, "#e8b53c")}</g>'
    for i in range(12):
        g += f'<g transform="translate({cx},{cy}) rotate({i * 30 + 15:.0f})">{petal_up(74 * s, 13 * s, "#f2c95e")}</g>'
    return g + C(cx, cy, 26 * s, "#d99a2b") + C(cx - 8 * s, cy - 8 * s, 8 * s, "#f5d878", 0.9)


def art_ju():
    """菊：一朵金色绒球大菊，花瓣又细又密。"""
    g = ground()
    g += P("M 380 380 Q 386 414 380 446", stroke=LEAF_D, w=13)
    g += place(leaf_veined(96, 30, GREEN), 376, 408, 205)
    g += place(leaf_veined(96, 30, GREEN_L), 386, 424, -25)
    g += chrys_bloom(380, 258, 1.0)
    return g


def osm_flower(cx, cy, r=9, col=None):
    """一朵小小的四瓣桂花。"""
    col = col or OSM
    g = ""
    for a in range(4):
        ang = math.radians(a * 90 + 45)
        g += C(cx + r * math.cos(ang), cy + r * math.sin(ang), r * 0.6, col)
    return g + C(cx, cy, r * 0.42, OSM_D)


def art_gui():
    """桂：深绿枝叶间一簇簇金黄小花，几粒花瓣正飘落。"""
    g = ground()
    g += P("M 120 200 Q 300 226 470 210 Q 580 200 656 176", stroke=BARK, w=22)
    g += P("M 330 222 Q 356 268 350 318", stroke=BARK, w=12)
    g += P("M 470 210 Q 452 260 466 306", stroke=BARK, w=12)
    for lx, ly, rot, col in [(210, 232, 24, LEAF_DD), (270, 258, -18, LEAF_DD),
                             (400, 268, 18, LEAF_DD), (520, 236, -22, LEAF_DD),
                             (560, 196, 26, LEAF_DD), (330, 296, -30, "#5e8f52"),
                             (452, 290, 26, "#5e8f52"), (620, 176, -20, LEAF_DD),
                             (180, 262, 30, "#5e8f52"), (588, 260, -26, "#5e8f52")]:
        g += place(leaf_veined(84, 26, col, "#3e6a34"), lx, ly, rot)
    for i, (fx, fy) in enumerate([(250, 268), (296, 296), (382, 300), (412, 322),
                                  (478, 282), (508, 306), (560, 246), (288, 326),
                                  (352, 342), (452, 348)]):
        for j, (dx, dy) in enumerate([(-16, 8), (14, 4), (-2, 22), (20, 24), (2, -14)]):
            col = "#f6ad4e" if (i + j) % 3 == 0 else OSM
            g += osm_flower(fx + dx, fy + dy, 10, col)
    # 飘落的桂花瓣
    for px, py, pr in [(322, 386, 5), (418, 404, 4), (270, 366, 4),
                       (506, 384, 5), (376, 424, 4), (452, 428, 3.5)]:
        g += C(px, py, pr, OSM, 0.85)
    return g


def orchid_flower(cx, cy, s=1.0):
    """一朵兰花：五枚细长瓣 + 小唇瓣。"""
    g = ""
    for a in (-90, -38, 38, 142, 218):
        g += f'<g transform="translate({cx},{cy}) rotate({a})">{petal_up(54 * s, 13 * s, ORCH)}</g>'
    return g + E(cx, cy + 16 * s, 13 * s, 9 * s, ORCH_D) + C(cx, cy, 6 * s, "#f2d06a")


def art_lan():
    """兰：盆栽兰草——细长弯叶 + 花茎挑着三朵兰花。"""
    g = ground()
    g += place(leaf_veined(190, 26, GREEN), 370, 352, 206)
    g += place(leaf_veined(200, 28, LEAF_DD), 380, 356, 230)
    g += place(leaf_veined(196, 27, GREEN_L), 392, 354, -26)
    g += place(leaf_veined(180, 24, "#6a9a5c"), 388, 350, -54)
    g += P("M 378 352 Q 388 292 376 238 Q 368 196 396 152", stroke=NODE, w=8)
    g += orchid_flower(370, 240, 1.1)
    g += orchid_flower(398, 150, 1.3)
    g += orchid_flower(356, 292, 0.95)
    g += P("M 300 356 L 460 356 L 442 442 L 318 442 Z", "#c89058")
    g += P("M 300 356 L 460 356 L 452 384 L 308 384 Z", "#b57b44")
    g += R(292, 344, 176, 16, 8, WOOD_D)
    return g


def art_sun():
    """笋：矮胖圆肩的笋特写——黄褐身体、Λ 形鞘棱、两侧翘起的鞘尖。"""
    g = ground()
    g += E(380, 442, 215, 34, SOIL)
    # 右后方半露的小笋
    g += P("M 542 306 L 506 438 Q 530 448 554 438 Z", "#b09a5e")
    # 主笋：矮胖身体、圆肩
    g += P("M 380 158 Q 344 176 316 240 Q 282 320 268 436 Q 380 462 492 436 "
           "Q 478 320 444 240 Q 416 176 380 158 Z", "#c9b078")
    # Λ 形鞘棱
    for yb, bw in ((267, 72), (319, 95), (371, 106), (410, 111)):
        g += P(f"M {380 - bw} {yb} L 380 {yb - 38} L {380 + bw} {yb}", stroke="#8a6f42", w=9)
    # 两侧翘起的鞘尖
    g += PG([(296, 306), (252, 272), (316, 290)], "#b89c60")
    g += PG([(478, 366), (522, 330), (462, 348)], "#b89c60")
    # 小尖头 + 高光
    g += PG([(368, 172), (380, 148), (393, 172)], "#6b4a26")
    g += L(320, 300, 296, 420, WHITE, 6)
    # 前景土盖住笋根 + 裂纹
    g += E(380, 448, 196, 22, SOIL_L)
    g += P("M 208 440 q 12 10 30 12", stroke=SOIL_D, w=6)
    g += P("M 556 436 q -12 12 -30 13", stroke=SOIL_D, w=6)
    return g


def art_li():
    """李：枝头三颗圆紫李，配光滑绿叶。"""
    g = ground()
    g += P("M 110 196 Q 280 240 460 232 Q 570 228 650 248", stroke=BRANCH_B, w=18)
    g += P("M 300 238 Q 288 268 296 296", stroke=BRANCH_B, w=10)
    g += P("M 452 234 Q 470 258 462 282", stroke=BRANCH_B, w=10)
    for lx, ly, rot in [(190, 226, 22), (370, 226, -16), (540, 234, 16),
                        (620, 244, -12), (250, 244, 10)]:
        g += place(leaf_veined(78, 26, LEAF_DD, "#3e6a34"), lx, ly, rot)
    for fx, fy, fr in [(296, 342, 54), (462, 336, 50), (580, 306, 46)]:
        g += L(fx, fy - fr - 2, fx + 2, fy - fr - 22, "#8a5a33", 6)
        g += C(fx + 4, fy + 5, fr, PLUMF_D) + C(fx, fy, fr, PLUMF)
        g += P(f"M {fx} {fy - fr + 6} Q {fx + 8} {fy} {fx + 2} {fy + fr - 8}",
               stroke=PLUMF_D, w=4, opacity=0.7)
        g += C(fx - fr * 0.32, fy - fr * 0.34, fr * 0.2, WHITE, 0.7)
    return g


def art_li4():
    """栗：刺球总苞裂开，露出亮棕色栗子。"""
    g = ground()
    cx, cy, r = 380, 296, 122
    for i in range(26):
        a = math.radians(i * 360 / 26)
        tip = (cx + (r + 30) * math.cos(a), cy + (r + 30) * math.sin(a))
        b1 = (cx + r * math.cos(a - 0.09), cy + r * math.sin(a - 0.09))
        b2 = (cx + r * math.cos(a + 0.09), cy + r * math.sin(a + 0.09))
        g += PG([b1, tip, b2], BUR_D if i % 2 else BUR)
    g += C(cx, cy, r, BUR)
    g += P(f"M {cx - 26} {cy - r + 10} Q {cx + 10} {cy - 44} {cx + 96} {cy - 52} "
           f"Q {cx + 40} {cy - 8} {cx + 30} {cy + 40} Q {cx - 8} {cy - 10} {cx - 26} {cy - r + 10} Z", "#4c3a22")
    g += C(cx + 52, cy - 34, 58, NUT) + C(cx + 52, cy - 34, 58, NUT)
    g += C(cx + 58, cy - 40, 50, "#a9743f")
    g += C(cx + 40, cy - 52, 12, WHITE, 0.6)
    g += P(f"M {cx + 22} {cy - 76} Q {cx + 52} {cy - 92} {cx + 84} {cy - 74}", stroke=NUT_D, w=5)
    g += P(f"M {cx - 30} {cy - r + 8} Q {cx - 60} {cy - 30} {cx - 30} {cy + 30} "
           f"Q {cx - 4} {cy - 8} {cx - 30} {cy - r + 8} Z", BUR_D)
    for sx, sy, sr in [(196, 408, 34), (560, 414, 28)]:
        for i in range(14):
            a = math.radians(i * 360 / 14)
            g += PG([(sx + sr * math.cos(a - 0.12), sy + sr * math.sin(a - 0.12)),
                     (sx + (sr + 16) * math.cos(a), sy + (sr + 16) * math.sin(a)),
                     (sx + sr * math.cos(a + 0.12), sy + sr * math.sin(a + 0.12))], BUR_D)
        g += C(sx, sy, sr, BUR)
    return g


def mulberry_leaf(ln, fill):
    """桑叶：主叶 + 上下两个侧裂，边缘有波浪感。"""
    g = leaf(ln, ln * 0.36, fill)
    g += E(ln * 0.34, -ln * 0.16, ln * 0.2, ln * 0.13, fill)
    g += E(ln * 0.34, ln * 0.16, ln * 0.2, ln * 0.13, fill)
    g += L(8, 0, ln * 0.8, 0, "#3e6a34", 3)
    return g


def art_sang():
    """桑：枝上垂着紫红桑果（疙疙瘩瘩）+ 裂叶。"""
    g = ground()
    g += P("M 110 226 Q 290 200 470 222 Q 580 236 646 222", stroke="#8a6242", w=17)
    g += P("M 300 210 Q 292 178 306 150", stroke="#8a6242", w=10)
    g += P("M 480 226 Q 500 196 492 168", stroke="#8a6242", w=10)
    for lx, ly, rot, col in [(190, 208, -22, LEAF_DD), (350, 176, -80, LEAF_DD),
                             (540, 200, -14, LEAF_DD), (250, 236, 14, "#5e8f52"),
                             (420, 244, -8, "#5e8f52"), (600, 216, 20, LEAF_DD)]:
        g += place(mulberry_leaf(96, col), lx, ly, rot)
    for fx, fy, rot in [(292, 330, 10), (452, 322, -8), (576, 300, 14)]:
        body = (E(4, 4, 20, 42, MUL_D) + E(0, 0, 20, 42, MUL))
        for r_i in range(5):
            yy = -32 + r_i * 16
            body += C(-11, yy, 7, MUL_L) + C(9, yy + 8, 7, MUL_L)
        g += L(fx, fy - 40, fx, fy - 58, "#8a6242", 5)
        g += f'<g transform="translate({fx},{fy}) rotate({rot})">{body}</g>'
    return g


def art_zhi():
    """枝：一段带木纹的粗枝，分杈挂叶和芽。"""
    g = ground()
    g += P("M 130 424 Q 280 356 420 296 Q 520 252 632 196", stroke=BRANCH_B, w=26)
    g += P("M 596 214 Q 632 196 664 168", stroke=BRANCH_B, w=12)
    g += P("M 330 348 Q 300 310 310 270", stroke=BRANCH_B, w=13)
    g += P("M 470 276 Q 510 268 546 240", stroke=BRANCH_B, w=11)
    for bx in (220, 330, 450, 560):
        g += L(bx, 398 - bx * 0.22, bx + 26, 390 - bx * 0.22, BARK, 5)
    g += E(384, 320, 9, 6, BARK) + E(500, 262, 8, 5, BARK)
    for lx, ly, rot in [(306, 264, -95), (330, 268, -60), (550, 236, -30),
                        (664, 164, -50), (648, 172, -14), (300, 268, -135)]:
        g += place(leaf_veined(84, 27, GREEN), lx, ly, rot)
    g += E(664, 160, 12, 18, FRESH)
    g += P("M 656 152 q 8 -8 16 -2", stroke=LEAF_D, w=4)
    return g


def art_gen():
    """根：剖开土层看根——地上一株小苗，土里白根四伸。"""
    g = ground()
    g += P("M 380 330 Q 374 288 380 244", stroke=NODE, w=12)
    g += place(leaf_veined(86, 28, GREEN), 378, 250, 205)
    g += place(leaf_veined(86, 28, GREEN_L), 384, 246, -28)
    g += R(116, 330, 528, 112, 16, "#8a6242")
    g += R(116, 330, 528, 18, 9, "#7a5236")
    for dx, dy, dr in [(180, 386, 6), (300, 414, 5), (470, 396, 6), (580, 418, 5),
                       (250, 424, 4), (520, 372, 4), (380, 396, 5)]:
        g += C(dx, dy, dr, "#6b4a33")
    g += P("M 380 332 Q 376 380 382 434", stroke=ROOTC, w=16)
    g += P("M 378 344 Q 320 356 268 372 Q 216 386 172 380", stroke=ROOTC, w=12)
    g += P("M 382 344 Q 438 354 492 372 Q 544 388 590 382", stroke=ROOTC, w=12)
    g += P("M 380 372 Q 348 396 314 408", stroke=ROOT, w=9)
    g += P("M 382 372 Q 420 398 456 410", stroke=ROOT, w=9)
    for rx, ry, rrot in [(272, 376, -12), (486, 376, 10), (316, 410, -8),
                         (452, 412, 8), (382, 430, 90)]:
        g += place(L(0, 0, 34, 0, ROOTC_D, 4) + L(30, 0, 44, 10, ROOTC_D, 3), rx, ry, rrot)
    g += P("M 340 436 q 12 8 28 6", stroke="#6b4a33", w=4)
    return g


def art_lu():
    """芦：单株特写——顶上一穗毛茸茸的大芦花。"""
    g = ground()
    g += P("M 380 444 Q 390 340 384 244", stroke="#7a9a5a", w=11)
    g += place(leaf(170, 17, "#7fae70"), 382, 330, 46)
    g += place(leaf(160, 16, GREEN), 380, 300, 138)
    g += place(leaf(140, 15, "#8fbc80"), 386, 268, -30)
    g += L(380, 250, 378, 96, "#b8a87e", 6)
    g += E(380, 158, 54, 92, PLUME)
    for i in range(14):
        t = i / 13
        py = 96 + 130 * t
        sway = 44 * math.sin(t * math.pi)
        side = 1 if i % 2 else -1
        col = PLUME_D if i % 3 else PLUME
        g += f'<g transform="translate({380 + side * sway:.0f},{py:.0f}) rotate({side * 28:.0f})">' \
             + E(0, 0, 6, 17, col) + "</g>"
    g += E(378, 106, 20, 26, PLUME)
    return g


def art_wei():
    """苇：水边一丛细苇，穗子高矮错落。"""
    g = ground()
    g += E(380, 428, 310, 36, WBLUE) + E(380, 424, 280, 28, "#a5d9f0", 0.85)
    for sx, top, s in [(300, 200, 0.9), (356, 156, 1.0), (420, 176, 0.95), (478, 220, 0.85)]:
        g += P(f"M {sx} 440 Q {sx + 6} {(top + 440) / 2:.0f} {sx} {top}", stroke="#7a9a5a", w=8)
        g += place(leaf(130 * s, 14, GREEN), sx, top + 96, 210)
        g += place(leaf(120 * s, 13, "#8fbc80"), sx, top + 130, -26)
        g += L(sx, top + 44, sx - 4, top + 2, "#b8a87e", 5)
        g += f'<g transform="rotate(-8 {sx} {top + 20})">' + E(sx - 2, top + 20, 20, 46, PLUME) + "</g>"
        g += E(sx - 3, top - 12, 9, 12, PLUME_D)
    g += P("M 150 434 Q 190 440 230 434", stroke=WHITE, w=5, opacity=0.7)
    g += P("M 540 438 Q 580 444 620 438", stroke=WHITE, w=5, opacity=0.7)
    return g


def art_pu():
    """蒲：香蒲——棕色蒲棒像小腊肠，剑叶细长。"""
    g = ground()
    for sx, top in [(316, 188), (392, 150), (462, 206)]:
        g += L(sx, 444, sx, top + 84, NODE, 9)
        g += R(sx - 13, top, 26, 86, 13, CIGAR)
        g += R(sx + 3, top + 4, 10, 78, 5, CIGAR_D)
        g += L(sx, top, sx - 2, top - 34, "#8a9a5a", 5)
    g += place(leaf(200, 19, LEAF_DD), 352, 440, 216)
    g += place(leaf(210, 20, GREEN), 400, 442, -32)
    g += place(leaf(180, 17, "#6a9a5c"), 448, 438, -8)
    g += place(leaf(160, 15, GREEN_L), 330, 440, 242)
    return g


def rose_bloom(cx, cy, s=1.0):
    """玫瑰花朵：外 8 圆瓣 + 内 6 瓣 + 旋心。"""
    g = ""
    for i in range(8):
        a = i * 45
        pet = P(f"M 0 0 Q {-56} {-38} {-30} {-96} Q 0 {-118} {30} {-96} Q {56} {-38} 0 0 Z", ROSE_C)
        g += f'<g transform="translate({cx},{cy}) rotate({a}) scale({s})">{pet}</g>'
    for i in range(6):
        a = i * 60 + 30
        pet2 = P(f"M 0 0 Q {-34} {-26} {-18} {-62} Q 0 {-76} {18} {-62} Q {34} {-26} 0 0 Z", ROSE_L2)
        g += f'<g transform="translate({cx},{cy}) rotate({a}) scale({s})">{pet2}</g>'
    g += f'<g transform="translate({cx},{cy}) scale({s})">' \
         + P("M -46 0 A 46 46 0 1 1 0 46 A 34 34 0 1 1 34 0 A 22 22 0 1 1 0 22 A 12 12 0 1 1 -12 0",
             stroke=ROSE_D2, w=7) + "</g>"
    return g


def art_mei():
    """玫：单朵红玫瑰特写——刺茎、两片叶、大花头。"""
    g = ground()
    g += P("M 380 440 Q 388 380 380 316", stroke=LEAF_D, w=15)
    for tx, ty in [(392, 402), (368, 366), (390, 336)]:
        g += PG([(tx, ty), (tx + 18, ty - 7), (tx + 3, ty - 16)], LEAF_DD)
    g += place(leaf_veined(88, 30, LEAF_DD), 376, 366, 208)
    g += place(leaf_veined(88, 30, GREEN), 386, 330, -26)
    g += rose_bloom(380, 216, 1.05)
    return g


def art_gui4():
    """瑰：玫瑰丛——两朵开的 + 一个花苞，枝叶带刺。"""
    g = ground()
    for sx in (300, 380, 462):
        g += P(f"M {sx} 442 Q {sx + 6} 380 {sx + (0 if sx == 380 else 14)} 320",
               stroke=LEAF_D, w=11)
    for tx, ty in [(436, 400), (286, 392), (408, 356)]:
        g += PG([(tx, ty), (tx + 16, ty - 6), (tx + 2, ty - 14)], LEAF_DD)
    for lx, ly, rot in [(292, 372, 205), (356, 396, -30), (452, 372, -24),
                        (322, 336, -14), (436, 330, 18), (384, 420, 202)]:
        g += place(leaf_veined(76, 25, LEAF_DD), lx, ly, rot)
    g += rose_bloom(298, 268, 0.78)
    g += rose_bloom(462, 300, 0.72)
    # 两个没打开的小花苞
    g += P("M 392 322 Q 388 288 396 262", stroke=LEAF_D, w=8)
    g += P("M 396 262 Q 378 232 396 204 Q 414 232 396 262 Z", ROSE_C)
    g += P("M 396 262 Q 382 268 376 284", stroke=LEAF_DD, w=5)
    g += P("M 396 262 Q 410 268 416 284", stroke=LEAF_DD, w=5)
    g += P("M 528 442 Q 538 412 546 384", stroke=LEAF_D, w=7)
    g += P("M 546 384 Q 534 366 546 348 Q 558 366 546 384 Z", ROSE_C)
    g += P("M 546 384 Q 536 390 532 402", stroke=LEAF_DD, w=4)
    g += P("M 546 384 Q 556 390 560 402", stroke=LEAF_DD, w=4)
    return g


def art_tong():
    """桐：整株桐树，冠是一张张看得清的大圆叶。"""
    g = ground()
    g += E(380, 448, 150, 15, "#aed4c2")
    g += P("M 356 444 L 362 330 L 398 330 L 404 444 Z", WOOD)
    g += P("M 372 334 Q 318 306 288 278", stroke=WOOD_D, w=13)
    g += P("M 388 334 Q 444 308 474 282", stroke=WOOD_D, w=13)
    g += P("M 380 330 Q 378 288 380 258", stroke=WOOD_D, w=13)
    for lx, ly, lr, col in [(278, 244, 64, FRESH), (478, 250, 62, GREEN),
                            (380, 186, 70, TONG_L), (296, 318, 54, GREEN),
                            (462, 322, 52, FRESH), (380, 300, 46, TONG_L)]:
        g += L(lx, ly + lr * 0.86, lx, ly + lr * 1.18, LEAF_DD, 6)
        g += C(lx, ly, lr, col)
        g += PG([(lx, ly + lr * 0.32), (lx - 13, ly + lr + 1), (lx + 13, ly + lr + 1)], "#fdf8ec")
        for a in (-70, -35, 0, 35, 70):
            ar = math.radians(a)
            g += L(lx, ly + lr * 0.5, lx + lr * 0.86 * math.sin(ar), ly + lr * 0.5 - lr * 0.8 * math.cos(ar),
                   LEAF_V, 3.5)
    return g


def art_bai():
    """柏：塔形柏树，一层层圆鳞叶叠上去。"""
    g = ground()
    g += E(380, 448, 120, 13, "#aed4c2")
    g += R(368, 348, 24, 96, 9, WOOD_D)
    tiers = [(380, 352, 106, 40, CYP_D), (380, 296, 88, 38, CYP),
             (380, 244, 70, 34, CYP_D), (380, 196, 54, 30, CYP), (380, 152, 38, 26, CYP_L)]
    for tx, ty, tw, th, col in tiers:
        g += E(tx, ty, tw, th, col)
        for row in range(2):
            ry = ty - 10 + row * 16
            span = tw * (0.62 if row == 0 else 0.4)
            n = max(3, int(span / 16))
            for i in range(n):
                dx = -span + i * (2 * span / (n - 1)) if n > 1 else 0
                g += C(tx + dx, ry, 6.5, CYP_L, 0.9)
    g += C(380, 118, 16, CYP_L) + C(380, 104, 9, CYP)
    return g


def arts():
    return {
        "藤": art_teng(), "菌": art_jun(), "蘑": art_mo(), "菇": art_gu(),
        "茎": art_jing(), "稻": art_dao(), "麦": art_mai(), "棉": art_mian(),
        "枣": art_zao(), "菊": art_ju(), "桂": art_gui(), "兰": art_lan(),
        "笋": art_sun(), "李": art_li(), "栗": art_li4(), "桑": art_sang(),
        "枝": art_zhi(), "根": art_gen(), "芦": art_lu(), "苇": art_wei(),
        "蒲": art_pu(), "玫": art_mei(), "瑰": art_gui4(), "桐": art_tong(),
        "柏": art_bai(),
    }


if __name__ == "__main__":
    LEGACY23 = {"花", "草", "木", "叶", "树", "果", "瓜", "苗", "竹", "豆",
                "莲", "杏", "桃", "荷", "松", "梅", "柳", "枫",
                "子", "禾", "皮", "苹", "芽"}
    spec = importlib.util.spec_from_file_location("ziku1000", str(ROOT / "字库1000.py"))
    ziku = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ziku)
    full = []
    for grp in ziku.GROUPS:
        if grp["id"] == "zhiwu":
            full = [it["char"] if isinstance(it, dict) else it for it in grp["chars"]]
    expect = [c for c in full if c not in LEGACY23]
    got = [c["char"] for c in GROUP_CARDS]
    a = arts()
    print(f"植物组新增：卡数 {len(GROUP_CARDS)}（字数 {len(got)}）")
    print(f"arts 数：{len(a)}")
    print(f"与字库比对：{'一致 ✓' if got == expect else '不一致 ✗ 期望 ' + str(expect) + ' 实际 ' + str(got)}")
    print(f"插画覆盖：{'齐全 ✓' if set(a) == set(got) else '缺失 ' + str(set(got) - set(a))}")
    py = json.loads((ROOT / "拼音表1000.json").read_text(encoding="utf-8"))
    bad_py = [c["char"] for c in GROUP_CARDS
              if py.get(c["char"], {}).get("pinyin") != c["pinyin"]
              or py.get(c["char"], {}).get("tone") != c["tone"]]
    print(f"拼音/声调：{'与拼音表逐一一致 ✓' if not bad_py else '不一致 ' + str(bad_py)}")
    lens = [(c["char"], f) for c in GROUP_CARDS for f in ("say", "chat", "life") if len(c[f]) > 30]
    sl = [(c["char"], len(c["sentence"])) for c in GROUP_CARDS
          if not (4 <= len(c["sentence"]) - 1 <= 10)]
    miss = [c["char"] for c in GROUP_CARDS if c["char"] not in c["sentence"]]
    print(f"三段长度：{'全部 ≤30 ✓' if not lens else str(lens)}")
    print(f"句长 4–10：{'全部达标 ✓' if not sl else str(sl)}")
    print(f"句含目标字：{'全部 ✓' if not miss else str(miss)}")
    bad = []
    for k, v in a.items():
        try:
            ET.fromstring(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480"><g>{v}</g></svg>')
        except ET.ParseError as e:
            bad.append((k, str(e)))
        for t in ("<text", "<use", "<defs", "<image", "href"):
            if t in v:
                bad.append((k, t))
    print("SVG 校验：全部合法 ✓" if not bad else f"SVG 问题：{bad}")
    assert got == expect and set(a) == set(got) and not bad_py and not lens and not sl and not miss and not bad, "自检未通过"
    print("自检通过 ✓")
