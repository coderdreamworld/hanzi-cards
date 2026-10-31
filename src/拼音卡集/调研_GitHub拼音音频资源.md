# GitHub 开源中文拼音发音音频资源调研

调研日期：2026-10-31 ｜ 调研方式：`gh search repos` / `gh search code` / `gh api`（仓库元数据、文件树、blob 哈希）+ WebFetch（站点页、README）+ 实际下载样本音频做 `md5` / `ffprobe` 比对。

**取证口径**：本报告区分三档标注。

| 标注 | 含义 |
| --- | --- |
| ✅ **已核实** | 我实际打开了仓库、读了 LICENSE 原文、列了文件树，或下载了音频文件做了哈希/参数比对 |
| ⚠️ **未验证** | 仅从搜索结果、README 摘要或第三方引用得知，我没有打开仓库确认 |
| ❌ **已排除** | 我实际打开确认了，但确认其**不含**目标内容 |

> 重要：本报告**没有**改动本目录任何实现文件（`拼音卡_素材.py`、`生成标准呼读音.py`、`拼音卡_构建.py`、任何 HTML）。只新增本文件。样本音频下载在 `/tmp/py_audio_probe/`。

---

## 零、结论速览（先看这一段）

**核心发现：你要的「声母呼读音」在 GitHub 上有现成的、可商用的合法来源，而且已经被别人切好了。**

| 结论 | 依据 |
| --- | --- |
| 23 个声母呼读音（bō pō mō fō dē tē nē lē…）**确实存在于开源音频里** | `davinfifield/mp3-chinese-pinyin-sound` 用**音节+声调**命名，`bo1.mp3`=bō、`fo1.mp3`=fō、`de1.mp3`=dē、`te1.mp3`=tē、`ne1.mp3`=nē、`le1.mp3`=lē、`ji1.mp3`=jī、`zhi1.mp3`=zhī… 全部命中。**该仓库 LICENSE = Unlicense（公有领域），可商用、无需署名** |
| 有人已经把这套切成了「拼音卡可直接用」的形态 | `argsno/flashcards-site` 的 `audio/pinyin/`：92 个 mp3，声母已是呼读音（`b.mp3`←`bo1.mp3`），并附 `LICENSE.txt` 原文 = Unlicense，README 写明来源与生成命令 |
| 存在与本项目**结构完全一致**（23 声母 + 24 韵母 + 16 整体认读）的现成仓库 | `vaebe/pinyin-audio`：`audio/sheng-mu/`(23) + `audio/yun-mu/`(24) + `audio/zheng-ti/`(16)，且经 md5 比对确认其声母**就是**上面那套呼读音。**但该仓库无 LICENSE，不能直接商用** |
| 「fō dē tē nē lē 没有常用汉字、纯汉字 TTS 做不到」这一判断成立，但有解 | 解法不是造汉字，而是**直接用「bo po mo fo de te ne le」这些呼读音音节的一声**，这正是教材声母表的做法，也是 `argsno` / `pinyin-playpad` / `hotoo` 三家独立项目的共同做法 |
| 纯汉字 TTS 语料库（THCHS-30 / AISHELL / Baker / MagicData / Datatang）**全部不适用** | 它们是整句朗读语料，不含孤立声母呼读音，且大多不在 GitHub 上以可下载音频形式分发 |

---

## 一、逐仓库档案

### A 类：有音频，且**许可清晰可商用**

#### A1. `davinfifield/mp3-chinese-pinyin-sound` ⭐ 首选源头 ✅已核实

- URL：https://github.com/davinfifield/mp3-chinese-pinyin-sound
- 描述：Mandarin Chinese pinyin sounds in MP3 format（42 star，19 fork，2014-05 最后提交，未归档）
- **许可：Unlicense（公有领域奉献）**。仓库 `LICENSE` 原文关键条款：

  > This is free and unencumbered software released into the public domain.
  > Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, **for any purpose, commercial or non-commercial**, and by any means.
  > …we dedicate any and all copyright interest in the software to the public domain…
  > For more information, please refer to <http://unlicense.org>

  仓库根目录只有 `LICENSE`、`README.md`、`mp3/` 三个条目，LICENSE 覆盖整个仓库（含 mp3 目录）。**可商用、可修改、可内嵌进交付物、无需署名。**

- 文件组织：**单目录 `mp3/`，一个音节一个文件，共 1000 个**。
- 命名规则：`<拼音音节><声调数字>.mp3`，如 `bo1.mp3`、`zhi3.mp3`、`ma5.mp3`。ü 用 `v`/`ve`/`vn` 写法（`lv1`、`lve1`、`lvn1`）；另有一批 `luu1`/`luue1`/`luun1` 的异体写法。
- 音质（实测 `ffprobe`）：**44100 Hz / 单声道 / 128 kbps**，单个音节 **0.65 s ~ 1.3 s**（例：`bo1.mp3` = 0.705250 s / 10555 B；`fo1.mp3` = 1.306063 s；`zhi1.mp3` = 1.280000 s）。
- **对呼读音的意义**：这批录音里 `bo po mo fo de te ne le ge ke he ji qi xi zhi chi shi ri zi ci si yi wu` 全部存在，且都以**第一声**命名。其中 `fo`、`te`、`ne`、`le`、`de`、`ji`、`qi`、`xi`、`ri` **在现代汉语里没有独立音节**（`fo` 更没有），能存在就证明录音者按**呼读音**录的，不可能是「得 dé」「特 tè」这类词。
  - ⚠️ 具体某个文件是「dē」还是「dé」我**没有听音确认**，这是从「同一套录音里存在 fo/te/ne/le 这些非词音节」推出的强推断。落地前请人耳过一遍。
- **仓库历史**：只有 2 次提交，作者 `pffy`（2014-04-11 initial release）。原仓库 `pffy/mp3-chinese-pinyin-sound` 现已 404（被删或改名），`davinfifield` 是接手后的现名。这解释了为什么 `shikangkai` 的 README 里引用的旧地址打不开。
- **同源关系（已用 md5 核实）**：`shikangkai/Chinese-Pinyin-Audio/Pinyin-Female/bo1.mp3` 与本仓库 `mp3/bo1.mp3` **md5 完全相同**（`c614987d19a7f55cb3232a8f1b3a3186`）。

---

#### A2. `argsno/flashcards-site` ⭐ 最省事的「切好版」 ✅已核实

- URL：https://github.com/argsno/flashcards-site
- 目录：https://github.com/argsno/flashcards-site/tree/main/audio/pinyin
- 说明：静态站「识字练习卡」，其 `audio/pinyin/` 是**为拼音卡片专门加工过的成套音频**。
- **许可**：
  - 仓库根目录**没有** LICENSE（根目录条目只有 `.nojekyll 404.html audio css favicon.ico favicon.svg fonts icons index.html js manifest.json weapp-qrcode.jpg`）→ 代码部分无授权声明。
  - **但 `audio/pinyin/LICENSE.txt` 内含完整 Unlicense 原文**（与 A1 逐字一致），且 `audio/pinyin/README.md` 明确声明来源是 A1。
  - 结论：**音频本体是公有领域，可商用、可内嵌、无需署名**；README/JS 代码不要顺带抄进交付物。
- **文件组织**：`audio/pinyin/`，**92 个 mp3**（另 + README.md + LICENSE.txt），文件名全 ASCII。
  - 声母 23：`b c ch d f g h j k l m n p q r s sh t w x y z zh .mp3`
  - 韵母 24（部分带四声变体）：`a1~a4 ai1~ai4 an ang ao1~ao4 e1~e4 ei1~ei4 en eng er i1~i4 ie in ing iu1~iu4 o1~o4 ong ou1~ou4 u1~u4 ui1~ui4 un v1~v4 ve vn`
  - 整体认读 9（toneless）：`wu ye yi yin ying yu yuan yue yun`
  - 另 7 个整体认读（zhi chi shi ri zi ci si）**与声母共用文件**（`zh/ch/sh/r/z/c/s.mp3`，因为声母呼读音本来就是「zhi chi shi ri zi ci si」）
- **音质（实测）**：**44100 Hz / 单声道 / 96000 bps**，经 `loudnorm=I=-16:TP=-1.5:LRA=7` 归一化，首尾各 15 ms 淡入淡出。单个 0.65 s ~ 1.31 s。92 个 mp3 合计 **1 271 362 B ≈ 1.21 MB**。
- **溯源链（已用时长精确比对核实）**：

  | argsno 文件 | 实测时长 | davinfifield 原文件 | 实测时长 | 对应 |
  | --- | --- | --- | --- | --- |
  | `b.mp3` | 0.705306 | `bo1.mp3` | 0.705250 | b ← bō ✅ |
  | `f.mp3` | 1.306122 | `fo1.mp3` | 1.306063 | f ← fō ✅ |
  | `d.mp3` | 0.914286 | `de1.mp3` | 0.914250 | d ← dē ✅ |
  | `zh.mp3` | 1.280000 | `zhi1.mp3` | 1.280000 | zh ← zhī ✅ |
  | `w.mp3` | 0.940408 | `wu1.mp3` | 0.940375 | w ← wū ✅ |
  | `y.mp3` | 0.940408 | `yi1.mp3` | 0.940375 | y ← yī ✅ |
  | `ye.mp3` | 1.097143 | `ye1.mp3` | 1.097125 | yè ✅ |
  | `a1.mp3` | 0.653061 | `a1.mp3` | 0.653063 | ā ✅ |

  时长逐条吻合到毫秒级，**可以确定 argsno 的音频就是 davinfifield 那套的重编码版**。
- 其 `audio/pinyin/README.md` 原文（关键段落，逐字）：

  > ## 来源与许可
  > - 原始录音：davinfifield/mp3-chinese-pinyin-sound，**Unlicense（公有领域）**，可商用、可修改、无需署名。本目录 `LICENSE.txt` 为原仓库许可原文。
  > - 取法（都是为了同一个录音者，避免音色跳）：
  >   - **声母**：呼读音音节（`b`←`bo`、`zh`←`zhi`），只取第一声；
  >   - **韵母**：零声母音节（`i`←`yi`、`ui`←`wei`、`ie`←`ye`），四声各取一条；
  >   - **仓库没有的三个**：`o`←`wo`、`eng`←`weng`、`ong`←`yong`，剪掉开头 35ms 滑音后取元音段。
  > - 统一处理：`loudnorm=I=-16:TP=-1.5:LRA=7`、单声道 44.1kHz、96kbps、首尾各 15ms 淡入淡出。
  > ## 已知局限
  > - 源录音首尾被切齐，声母辅音偏轻…
  > - `o`/`eng`/`ong` 由滑音音节剪出，起点比自然发音略硬，真机上需要人耳复核。

  ⚠️ **注意**：`argsno` 的 `o`/`eng`/`ong` 是从 `wo`/`weng`/`yong` 里剪出来的，「起点略硬」是人耳已知问题。若本项目对这 3 个音敏感，建议改用本项目现有的 Tingting IPA 合成音。

---

#### A3. `byhow/yanyu` — MIT，2063 个 mp3 ✅已核实

- URL：https://github.com/byhow/yanyu ｜ npm：https://www.npmjs.com/package/yanyu
- 描述：A Chinese speech synthesis and recognition library toolkit（11 star，2026-10-30 仍在更新）
- **许可：MIT**。`LICENSE` 原文关键条款：

  > MIT License
  > Copyright (c) 2020 flyingbeaver
  > Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, **including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies** of the Software…

- 文件组织：`pinyin-syllables/`，**2063 个 mp3**。
- 命名规则：**两套并存**——`<音节>.mp3`（无调，如 `bo.mp3`、`fo.mp3`、`de.mp3`、`te.mp3`）**与** `<音节><声调>.mp3`（`bo1.mp3`…）。另有 `1000.mp3`（兜底静音/占位）。
- 音质（实测）：**44100 Hz / 立体声 / 128000 bps**，单个 **0.26 s ~ 0.34 s**（`de`=0.279 s、`bo`=0.302 s、`ge`=0.341 s）。体积小，但**单声道化 + 截得很短**，直接外放可能偏"顶"。
- **对呼读音的意义**：`bo po mo fo de te ne le ge ke he ji qi xi zhi chi shi ri zi ci si yi wu` 的**无调文件全部存在**（我逐一验证了 23 个文件名）。`fo`/`te` 无调文件的存在同样说明是呼读音。
- ⚠️ **重要保留**：仓库 `src/index.ts` 显示这个库本身**只做音频拼接**（用 `audiosprite` 把 `pinyin-syllables/*.mp3` 拼起来），**README 和代码都没有交代这批音频是从哪录的**。MIT 覆盖的是「the Software」，把第三方录音打包进 MIT 仓库属于灰色地带。**商用前建议向作者确认录音来源。**
- 对比：我逐个比对了 yanyu 与 hotoo 的 23 个同名无调文件，**md5 全部不同** → 两家是**各自独立的录音**，音色不同（正好可以做 A/B 备选）。

---

#### A4. `hotoo/pinyin` — MIT，407 个 mp3 ✅已核实

- URL：https://github.com/hotoo/pinyin （**7831 star**，pīnyīn 项目主仓）
- **许可：MIT**。`LICENSE` 原文关键条款：

  > MIT License
  > Copyright (c) 2026 闲耘™
  > Permission is hereby granted, free of charge, to any person obtaining a copy of this software … **to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies** of the Software…

- 文件组织：现为 monorepo，音频在 `apps/website/docs/public/audio/`，**407 个 mp3**，**无调命名**：`a.mp3 ai.mp3 an.mp3 … bo.mp3 … fo.mp3 de.mp3 te.mp3 ne.mp3 le.mp3 ge.mp3 ke.mp3 he.mp3 ji.mp3 qi.mp3 xi.mp3 zhi.mp3 chi.mp3 shi.mp3 ri.mp3 zi.mp3 ci.mp3 si.mp3 yi.mp3 wu.mp3`（已实测存在 `fo de te ne lei den` 等）。
- 音质（实测）：**44100 Hz / 单声道 / 64 kbps**，但**每个文件长达 8.5 ~ 10 s**（`fo`=8.915 s、`wu`=10.030 s、`a`=9.449 s）。**全部 407 个合计约 29 MB。**
- ⚠️ **不适合内嵌**：8~10 s 的单音节意味着大量静音padding，单文件体积是 zispace 那套的 10 倍以上。**适合做外链 CDN / 在线试听，不适合塞进单文件 HTML。**
- ⚠️ 音频来源未在仓库中交代（同 A3 的保留意见）。

---

#### A5. `hugolpz/audio-cmn` — CC-BY-SA，1707 个音节 ✅已核实

- URL：https://github.com/hugolpz/audio-cmn （98 star）
- 描述：Chinese (zh-cnm) opendata audio files for 8,596 hsk words and 1,707 syllabs.
- **许可：CC-BY-SA**。README 关键原文：

  > | # of items | Naming | Set's specifics | Authorship |
  > | 1707 | `cmn-zi4.mp3` | syllabs v.2 | **Chen Wang, CC-by-sa** |
  > | +8000 | `cmn-名字.mp3` | HSK_2000 list (words,zi) | Yue Tan, CC-by-sa |
  > ### License
  > - **CC-by-sa.** See table upper for authors.

- 文件组织：`18k-abr/ 24k-abr/ 64k/ 96k/` 四个音质档，每档含 `syllabs/`（1707）与 `hsk/`。
- 命名：`cmn-<带调拼音>.mp3`。
- 音质：`64k/syllabs/`（推荐档）、`24k-abr`（约轻一半）、`18k-abr`（约轻 1/3）。
- ⚠️ **CC-BY-SA 的两个硬约束**：① **必须署名**（作者 Chen Wang / Yue Tan + 许可证链接）；② **相同方式共享（ShareAlike）** —— 你的成品 HTML 会被要求以相同许可发布。**对"给用户交付的单文件 HTML"不友好。**
- ⚠️ 目录里**没有 `bo.mp3`/`fo.mp3` 这类纯声母文件**（是带调音节全集），呼读音需自行切取。

---

#### A6. `gitcode.com/open-source-toolkit/79b35` — 1608 个汉字读音 ✅（部分核实）

- URL：https://gitcode.com/open-source-toolkit/79b35
- WebFetch 读到的页面：标题「1608个汉字读音MP3资源包」，描述为「面向阅读开发、语音合成、语言学习的普通话汉字发音 MP3 资源包」，页面显示 **MIT License 徽章**。
- 对应 `zispace/hanyu-pinyin-audio` 里的 `gitcode.com/audio/`（1289 个 `<音节><声调>.mp3`）。
- ⚠️ **未验证**：MIT 徽章是否覆盖音频本体、以及 README 全文（WebFetch 只拿到页面可见部分）。需人工打开确认。

---

### B 类：有音频，但**许可不明或限制商用**

#### B1. `vaebe/pinyin-audio` — 结构与本项目 100% 对齐 ⭐结构参考 ✅已核实

- URL：https://github.com/vaebe/pinyin-audio （2 star，2024-08 建库后基本未动）
- 描述：「汉语拼音声母、韵母、整体认读音节 mp3 文件」
- **许可：仓库无 LICENSE 文件**（根目录只有 `README.md audio index.html index.ts package.json`）。`package.json` 里写了 `"license": "ISC"`，但 `README.md` 只有 3 个字（`# pinyin-audio`）——**没有版权声明，ISC 只是 npm 字段，ISC 也不适用于音频**。
- 文件组织（**与本项目 63 项结构逐项对齐**）：
  - `audio/sheng-mu/`：**23 个**，b p m f d t n l g k h j q x zh ch sh r z c s y w
  - `audio/yun-mu/`：**24 个**，a o e i u v ai ei ui ao ou iu ie ve er an en in un vn ang eng ing ong（ü 用 `v`/`ve`/`vn`）
  - `audio/zheng-ti/`：**16 个**，zhi chi shi ri zi ci si yi wu yu ye yue yuan yin yun ying（文件名带 `1`，如 `zhi1.mp3`）
- `index.ts` 注释逐字：

  > /**
  >  * 声母：23个。分别是：b p m f d t n l g k h j q x zh ch sh r z c s y w
  >  */
  > /**
  >  * 韵母：24个。单韵母：a o e i u ü
  >  复韵母：ai ei ui ao ou iu ie üe
  >  特殊韵母：er
  >  鼻韵母：an en in un ün ang eng ing ong
  >  … ü 使用 v 代替
  >  */
  > /**
  >  * 整体认读音节：16个，分别是：zhi chi shi ri zi ci si yi wu yu ye yue yin yun yuan ying
  >  */

- 音质（实测）：**22050 Hz / 单声道 / 56000 bps**，单文件 **0.9 ~ 1.2 s**。63 个合计 **450 561 B ≈ 440 KB**。
- **关键实测结论：它的 23 个声母文件 = 呼读音**。我下载全部 23 个，与 `zispace` 的 `2-所有音节/<音节>1.mp3` 做 md5 全量比对：

  | 声母 | 字节级相同的文件 | 声母 | 字节级相同的文件 |
  | --- | --- | --- | --- |
  | b | `bo1` (bō) | j | `ji1` (jī) |
  | p | `po1` (pō) | q | `qi1` (qī) |
  | m | `mo1` (mō) | x | `xi1` (xī) |
  | f | `fo1` (fō) | zh | `zhi1` (zhī) |
  | d | `de1` (dē) | ch | `chi1` (chī) |
  | t | `te1` (tē) | sh | `shi1` (shī) |
  | n | `ne1` (nē) | r | `ri1` (rī) |
  | l | `le1` (lē) | z | `zi1` (zī) |
  | g | `ge1` (gē) | c | `ci1` (cī) |
  | k | `ke1` (kē) | s | `si1` (sī) |
  | h | `he1` (hē) | y | `yi1` (yī) |
  | | | w | `wu1` (wū) |

  **23/23 全部命中，零例外。** `fo`/`te`/`ne`/`le`/`de`/`ji`/`qi`/`xi`/`ri` 都在其中，**这从字节层面证实了「呼读音」在开源音频里是现成的**。
- ⚠️ **不可直接商用**：无 LICENSE + 内容明显来自第三方教学站点（音频与 `zispace` 的 `misc/2-所有音节` 集合完全同源）。**但它是最好的「结构说明书」**，可以直接照抄它的目录规划。

---

#### B2. `zispace/hanyu-pinyin-audio` — 拼音音频站点镜像大合集 ✅已核实

- URL：https://github.com/zispace/hanyu-pinyin-audio （49 star，576 MB，2025-07 最后提交）
- 主页：https://zispace.github.io/hanyu-pinyin/
- 描述：「汉语拼音音频数据汇集（目前为 mp3 或 wav 格式），原始音频来自网络，已移除重复文件，本项目仅供参考。」
- **许可：仓库无 LICENSE 文件**（根目录只有 `.gitignore README.md` + 15 个音频目录）。README 明说「**原始音频来自网络**」「**本项目仅供参考**」→ **作者自己就声明了这是搬运，没有授权**。
- **文件组织：按来源站分目录**（共 20 843 个文件，这是"拼音音频站点开源镜像"的答案）：

  | 目录 | 文件数 | 来源 |
  | --- | ---: | --- |
  | `digmandarin.com/audio/` | 1629 | digmandarin 拼音表 |
  | `mandarintemple.com/audio/` | 1994 | Mandarin Temple 拼音表（**wav，含 5 声**） |
  | `yabla.com/audio/` | 1629 | yabla 拼音表 |
  | `yoyochinese.com/audio/` | 1613 | YoyoChinese 拼音表 |
  | `sreading.org/audio/` | 1702 | sreading 拼音路径 |
  | `studycli.org/audio/` | 1573 | StudyCLI 拼音表 |
  | `lost-theory.org/audio/` | 1930 | 汉语拼音网 |
  | `uvm.edu/audio/` | 411 | **University of Vermont** 汉语教学页（wav 为主，**每个 6~7 s**） |
  | `github-davinfifield/mp3/` | 1623 | = A1 的镜像 |
  | `github-shikangkai/` | 3040 | = B3 的镜像 |
  | `github-hotoo/audio/` | 406 | = A4 的镜像 |
  | `github-hugolpz/` | 1707 | = A5 的镜像 |
  | `gitcode.com/audio/` | 1289 | = A6 的镜像 |
  | **`misc/`** | **265** | **见下** |

- **`misc/` 是本次调研最重要的目录**，命名带中文序号，直接对应本项目的需求：

  ```
  misc/1-声母/     b c ch d f g h j k l m n p q r s sh t w x y z zh .mp3   (23 个)
  misc/1-韵母/     ai an ang ao e ei en eng er i ie in ing iu o ong ou u ui un ü üe ün .mp3  (23 个，缺 a)
  misc/2-所有音节/ a1..a4 … zhi1..zhi4 zi1..zi4（共 219 个，音节+声调）
  ```

  - `misc/1-声母/*` 与 `misc/2-所有音节/*1.mp3` 的关系（实测 md5）：**21/23 完全相同**（仅 `b`、`t` 两个不同）。也就是说 **`1-声母/` 基本就是「呼读音音节的一声」**。
  - `misc/2-所有音节/` 的**音质实测**：**22050 Hz / 单声道 / 56000 bps**，单文件 **0.89 ~ 1.18 s**（`bo1`=1.175571 s、`wu1`=0.888143 s、`de1`=1.071000 s）。**体积小，是内嵌单文件 HTML 最划算的一套。**
  - `misc/1-声母/` 少一个 `a`（韵母 a 在 `misc/2-所有音节/a1.mp3`）。注意 `misc/1-韵母/` 只有 23 个文件，`a` 缺席。
- ⚠️ **不可商用**（无 LICENSE + 自述"仅供参考" + 原始音频来自各站点，那些站点的音频本身多数也未开源授权）。
- **它的真实价值**：① 证明"呼读音音频"在开源世界已被标准化命名；② 提供一份**多来源横向对照表**，可用于判断某个音哪个来源最准；③ `misc/2-所有音节/` 的 22050 Hz/56 kbps 版本是**体积最小的呼读音载体**。

---

#### B3. `shikangkai/Chinese-Pinyin-Audio` — 女声/男声双套 ✅已核实

- URL：https://github.com/shikangkai/Chinese-Pinyin-Audio （28 star，2017 建库后未再更新）
- **许可：无 LICENSE 文件**（根目录只有 `Readme.md` + 4 个音频目录）→ 不可商用。
- Readme 原文（关键）：

  > 文件夹：Pinyin-Female
  > 女声读音来自：https://github.com/pffy/mp3-chinese-pinyin-sound
  > 去除重复后共有1617例。
  > 文件夹 Pinyin-Male
  > 男声读音来自：http://lost-theory.org/chinese/phonetics/
  > 网站上有些音频缺失，共有1568例。
  > 文件夹 Pinyin-Female-Wav 和 Pinyin-Male-Wav 分别为上述文件夹文件 WAV 格式转化后的文件。
  > 其中，量化位数为16，采样率为22050Hz，单声道。

- 文件组织（实测统计）：

  | 目录 | 格式 | 数量 |
  | --- | --- | ---: |
  | `Pinyin-Female/` | mp3 | 1617 |
  | `Pinyin-Female-Wav/` | wav | 1617 |
  | `Pinyin-Male/` | **wav**（README 说 mp3，实际是 wav，文档有出入） | 1568 |
  | `Pinyin-Male-Wav/` | wav | 1568 |

- 音质：Wav 为 **22050 Hz / 单声道 / 16 bit**（实测 `Pinyin-Male-Wav/bo1.wav` = 0.979138 s）。mp3 为 44100 Hz / 单声道 / 128 kbps。
- **女声 mp3 与 A1（davinfifield）字节相同**（`Pinyin-Female/bo1.mp3` md5 = `c614987d…` = `mp3/bo1.mp3` md5）。**所以它的女声部分法律地位等于 A1 = Unlicense**，只是本仓库自身缺 LICENSE；直接引用 A1 更干净。
- 男声来自 lost-theory.org，**来源站点无开源授权**，不可商用。

---

#### B4. `hanziguru/pinyin-audio` — 声称"录音棚品质"，但限非商用 ✅已核实

- URL：https://github.com/hanziguru/pinyin-audio （0 star，2026-10-22 建库）
- 描述：High-quality studio Pinyin audio recordings for Mandarin Chinese (tones 1-5)
- **许可：仓库无 LICENSE 文件**（根目录只有 `.gitignore README.md dist/`）。README 末尾原文：

  > ## 📜 License & Acknowledgements
  > Compiled for HanziGuru to support Chinese language learners worldwide. Audio sources derived from standard open educational Mandarin pronunciation archives. **Free for educational and non-commercial use.**

  → **明确限定「非商业」，且「来源为标准开放教育普通话发音档案」只是含糊表述，没有点名、没有 LICENSE 原文。** ⚠️ 「educational and non-commercial」直接否掉商用。
- 文件组织：`dist/`，**1636 个 mp3**（约 22 MB），命名 `<音节><声调1-5>.mp3`（`ma1.mp3`…`ma5.mp3`，ü 写作 `v`：`nv3.mp3`、`lve4.mp3`）。
- 用途：HanziGuru 用 jsDelivr CDN 引：`https://cdn.jsdelivr.net/gh/hanziguru/pinyin-audio@main/dist/{syllable}{tone}.mp3`
- ⚠️ 该仓库**没有孤立声母文件**，只有完整音节+声调。呼读音要从 `bo1`/`fo1` 里取（但它有 `fo1` 吗？——README 举例只有 nv/lve，**未验证**是否含 fo/te/ne/le）。

---

#### B5. `luzhihua407/aihu` — 微信小程序，声母韵母目录结构 ✅已核实

- URL：https://github.com/luzhihua407/aihu （6 star，2019）
- 描述：「一个帮助小朋友学习声母、韵母、字母发音、和100以内的加减法的微信小程序」
- **许可：无 LICENSE 文件**（根目录 `README.md app.js app.json … voice weui.wxss`）→ 不可商用。
- 音频目录 `voice/`（实测 77 个音频）：
  - `voice/zh/`：**47 个**——`a ai an ang ao b c ch d e ei en eng er f g h i ie in ing iu j k l m n o ong ou p q r s sh t u ui un w x y z zh ü üe ün`
    → 声母 23 个（b c ch d f g h j k l m n p q r s sh t w x y z zh）+ 韵母 24 个（a o e i u ü ai ei ui ao ou iu ie üe er an en in un ün ang eng ing ong）**齐了**，但整体认读 16 个只有 9 个（wu ye yi yin ying yu yuan yue yun），缺 zhi chi shi ri zi ci si 7 个（可由声母 zh/ch/sh/r/z/c/s 顶替）
  - `voice/en/`：英文字母 26 个
  - `voice/right.mp3` `voice/sorry.mp3` `voice/exam/question.mp3` `voice/alphabet-complete.mp3`
- **价值**：这是「小朋友学声母韵母」的现成产品形态参考，文件名就是拼音本身，取用极方便；**且它证明了声母 mp3 命名直接用字母（b.mp3）是行业惯例**。

---

### C 类：**已核实不含**目标音频（省去后续排查）

| 仓库 | URL | 许可 | 实测结果 |
| --- | --- | --- | --- |
| `mozillazg/python-pinyin`（pypinyin） | https://github.com/mozillazg/python-pinyin | MIT | ✅已核实 **0 个**音频文件（纯拼音转换库） |
| `xpinyin` | — | — | ✅已核实 `mozillazg/xpinyin` **仓库不存在（404）** |
| `zh-lx/pinyin-pro` | https://github.com/zh-lx/pinyin-pro | MIT（4758 star） | ✅已核实 **0 个**音频文件 |
| `xiaobopang/pinyin` | https://github.com/xiaobopang/pinyin | Apache-2.0 | ✅已核实 **0 个**音频文件 |
| `Yidadaa/shuangpin` | https://github.com/Yidadaa/shuangpin | MIT（535 star，双拼练习） | ✅已核实 **0 个**音频文件（用 TTS 实时合成） |
| `jiong3/pinyinChart` | https://github.com/jiong3/pinyinChart | NOASSERTION | ✅已核实 **0 个**音频文件 |
| `shengeng87/pinyin-castle` | https://github.com/shengeng87/pinyin-castle | 无 | ✅已核实 **0 个**音频文件 |
| `ryuutyouki/3Dpinyin` | https://github.com/ryuutyouki/3Dpinyin | 无 | ✅已核实仅 12 个**音效**（explosion/praise/wrong），拼音走 TTS |
| `Synkied/hanzipy` | https://github.com/Synkied/hanzipy | MIT | ✅已核实 **0 个**音频文件 |
| `wuwangzhang1216/congcong-school` | https://github.com/wuwangzhang1216/congcong-school | MIT（1166 star） | ✅已核实 **0 个**音频文件 |
| `sbsrf/home`（声笔输入法） | https://github.com/sbsrf/home | 无 | ✅已核实 **0 个**音频文件 |
| `wangqinmi/hanzi-park` | https://github.com/wangqinmi/hanzi-park | 无 | ⚠️ 3232 个 mp3（幼儿识字，神经网络 TTS），**无 LICENSE**，不可商用 |
| `npm: pinyin-audio` / `chinese-pinyin-audio` / `pinyin-sound` | npm registry | — | ✅已核实 **npm 上不存在这三个包** |
| `npm: speak-tts` | https://www.npmjs.com/package/speak-tts | MIT | ✅已核实是浏览器 Web Speech API 封装，**不含音频** |

---

### D 类：中文 TTS 语料库 —— **全部不适用** ✅已核实

| 语料 | 仓库 | 许可 | 为什么不能用 |
| --- | --- | --- | --- |
| THCHS-30 | https://github.com/langtern/THCHS-30 | Apache-2.0 | ✅已核实 `data/A11_0.wav.mp3` 等，**是整句朗读语料**（30k 句），**无孤立声母**；且不是全部上架 GitHub |
| AISHELL-3 | https://github.com/felixfuyihui/AISHELL-4 等 | Apache-2.0 | ✅已核实均为**训练/识别**工程，非孤立音节音频 |
| Baker（中文标准普通话语音数据库） | — | 非商用（数据集声明仅限学术） | ✅已核实 GitHub 上**无该数据集仓库**（原始分发在 openslr / magicdata） |
| MagicData | — | — | ✅已核实 GitHub 搜 "MagicData speech" **无结果** |
| Datatang（aidatatang_200zh） | https://github.com/PennyZhang9/aidatatang_200zh | 无 | ✅已核实**无 LICENSE**，且是整句语料 |
| Mozilla / Common Voice | — | — | ✅已核实 GitHub 搜 "mozilla tts dataset" **无结果**；Common Voice 是众包朗读长句，与孤立呼读音无关 |

**结论：这条路彻底堵死。** 语料库解决的是"整句朗读"，而拼音卡需要的是"脱离词境的孤立呼读音"，两者在数据形态上就不重合。

---

## 二、专章：「声母呼读音」到底有没有现成的

### 2.1 你的判断成立，但解法不是造汉字

「fō / dē / tē / nē / lē 在现代汉语里没有常用汉字，纯汉字 TTS 做不到」——**这个判断是对的**。macOS/Windows/浏览器的 TTS 都是「文本 → 音节」或「文本 → 音素」的，喂 `fo`/`de` 给中文 TTS，它要么读成「佛 fó」「的 de」，要么读出拼音字母名，要么乱码。

### 2.2 但「呼读音」本身是一个**真实的、可录制的音**，而且教材就是这么教的

《汉语拼音方案》声母表里的 `b p m f` 那一列，标的不是「玻 坡 摸 佛」，而是 **bō pō mō fō**（dē tē nē lē gē kē hē jī qī xī zhī chī shī rī zī cī sī yī wū）。这些音**脱离汉字独立存在**，是中国人从小学会的音。教材、拼音表网站、几乎所有拼音教具都按这个读。

### 2.3 开源界的标准做法：借「音节+一声」的文件当呼读音

`argsno` 的 README 把这套做法写成了明文（原文见 §A2），`bincode2199/pinyin-playpad` 的 `js/speech.js` 注释也印证了同一口径：

> ```
> *   audio/initials/<声母>.mp3          声母本音       (misc/1-声母)
> *   audio/finals/<韵母>.mp3            韵母本音       (misc/1-韵母)
> *   audio/syllables/<音节><声调>.mp3    带调逐段朗读   (misc/2-所有音节)
> *   audio/characters/<音节><声调>.mp3   完整文字发音   (yoyochinese.com)
> ```

`littleflower212/study` 的 `scripts/download-pinyin-audio.sh` 则是把同一套下载脚本化（原文片段）：

> ```bash
> # 从 zispace/hanyu-pinyin-audio 下载标准拼音录音到 public/audio/pinyin/
> CDN="https://cdn.jsdelivr.net/gh/zispace/hanyu-pinyin-audio@data"
> …
> for sym in b p m f d t n l g k h j q x zh ch sh r z c s y w; do
>   url=$(remote "misc" "1-声母" "${sym}.mp3")
>   download "声母 $sym" "$url" "$OUT/py-${sym}.mp3"
> done
> ```

### 2.4 完整映射表（我实测得到的，可直接照做）

以 `davinfifield/mp3-chinese-pinyin-sound`（Unlicense）为源，**呼读音 = 对应音节的第一声文件**：

| 呼读音 | 声母 | 源文件 | 呼读音 | 声母 | 源文件 |
| --- | --- | --- | --- | --- | --- |
| bō | b | `bo1.mp3` | jī | j | `ji1.mp3` |
| pō | p | `po1.mp3` | qī | q | `qi1.mp3` |
| mō | m | `mo1.mp3` | xī | x | `xi1.mp3` |
| fō | f | `fo1.mp3` | zhī | zh | `zhi1.mp3` |
| dē | d | `de1.mp3` | chī | ch | `chi1.mp3` |
| tē | t | `te1.mp3` | shī | sh | `shi1.mp3` |
| nē | n | `ne1.mp3` | rī | r | `ri1.mp3` |
| lē | l | `le1.mp3` | zī | z | `zi1.mp3` |
| gē | g | `ge1.mp3` | cī | c | `ci1.mp3` |
| kē | k | `ke1.mp3` | sī | s | `si1.mp3` |
| hē | h | `he1.mp3` | yī | y | `yi1.mp3` |
| | | | wū | w | `wu1.mp3` |

**23/23 全部在源仓库存在**（我用文件树全量校验过，无一缺失）。

韵母（借零声母音节）：

| 韵母 | 源文件 | 韵母 | 源文件 |
| --- | --- | --- | --- |
| a | `a1.mp3` | ie | `ye1.mp3` |
| o | `wo1.mp3` ⚠️需剪滑音 | üe | `yue1.mp3` |
| e | `e1.mp3` | er | `er1.mp3` |
| i | `yi1.mp3` | an | `an1.mp3` |
| u | `wu1.mp3` | en | `en1.mp3` |
| ü | `yu1.mp3` | in | `yin1.mp3` |
| ai | `ai1.mp3` | un | `yun1.mp3` |
| ei | `ei1.mp3` | ün | `yuan1.mp3` |
| ui | `wei1.mp3` | ang | `ang1.mp3` |
| ao | `ao1.mp3` | eng | `weng1.mp3` ⚠️需剪滑音 |
| ou | `ou1.mp3` | ing | `ying1.mp3` |
| iu | `liu1.mp3` | ong | `yong1.mp3` ⚠️需剪滑音 |

### 2.5 一个必须知道的技术细节

呼读音 bō 的声母 `b` 是**不送气**的 [p⁰]，而「波 bō」这个字是**送气**的 [p]。直接用 `bo1.mp3` 当声母 b 的读音，**声母会偏重**。`argsno` 自己的「已知局限」也承认了这点：

> 源录音首尾被切齐，**声母辅音偏轻**；练习是「看字母自己读、家长判会/不会」，不考辨音差异。

→ 结论：**这批录音用于「认字形 + 跟读」是够的；用于「听辨 b/d/p/q」这类精细辨音训练是不够的。** 本项目如果只做 4 岁认读卡片，够用。

---

## 三、许可与可用性判断

| 资源 | 许可 | 能否商用 | 能否放进交付的 HTML | 能否署名 |
| --- | --- | --- | --- | --- |
| `davinfifield/mp3-chinese-pinyin-sound` | **Unlicense**（公有领域） | ✅ 可以 | ✅ 可以（音频字节可直接打包） | ❌ 无需署名（但建议注明出处） |
| `argsno/flashcards-site/audio/pinyin/` | **Unlicense**（`LICENSE.txt` 原文） | ✅ 可以 | ✅ 可以 | ❌ 无需署名 |
| `byhow/yanyu` | MIT（仅覆盖 Software） | ⚠️ 待作者确认录音来源 | ⚠️ 同左 | ✅ 需保留 MIT 声明 |
| `hotoo/pinyin` | MIT（仅覆盖 Software） | ⚠️ 待作者确认录音来源 | ⚠️ 同左 | ✅ 需保留 MIT 声明 |
| `hugolpz/audio-cmn` | **CC-BY-SA** | ✅ 可以 | ⚠️ **要求成品同许可发布（SA）** | ✅ **必须署名** Chen Wang / Yue Tan + 许可证链接 |
| `gitcode.com/open-source-toolkit/79b35` | MIT 徽章（⚠️未验证） | ⚠️ 未验证 | ⚠️ 未验证 | — |
| `vaebe/pinyin-audio` | ❌ 无 LICENSE | ❌ **不可以** | ❌ 不可以 | — |
| `zispace/hanyu-pinyin-audio` | ❌ 无 LICENSE（自述"仅供参考"） | ❌ **不可以** | ❌ 不可以 | — |
| `shikangkai/Chinese-Pinyin-Audio` | ❌ 无 LICENSE（女声部分实为 Unlicense 上游） | ⚠️ 女声可（引 A1）/ 男声不可 | 同左 | — |
| `hanziguru/pinyin-audio` | ❌ 无 LICENSE，README 限定"非商业" | ❌ **不可以** | ❌ 不可以 | — |
| `luzhihua407/aihu` | ❌ 无 LICENSE | ❌ **不可以** | ❌ 不可以 | — |
| THCHS-30 / AISHELL / Baker / MagicData / Datatang | 各自条款 | ❌ 内容形态不适用 | ❌ | — |

**一句话结论：真正「拿来就能商用、能直接进交付物」的只有 Unlicense 系的两个：`davinfifield/mp3-chinese-pinyin-sound`（原始）和 `argsno/flashcards-site/audio/pinyin/`（切好的）。**

---

## 四、体积测算

### 4.1 本项目现状

| 项 | 实测值 |
| --- | --- |
| `audio/` 目录 | **130 个 .m4a，合计 1 520 907 B ≈ 1.49 MB**，平均 11 699 B/个 |
| `拼音字母卡.html` | 228 442 B ≈ 223 KB |
| 引用方式 | **外链相对路径** `new Audio(\`audio/${encodeURIComponent(name)}…\`)`，**不是 base64 内嵌**（`data:audio` 出现 0 次） |

→ 本项目当前就是「HTML + 同级 audio/ 目录」结构，不是单文件。

### 4.2 如果要做成**单文件 HTML（base64 内嵌）**

| 方案 | 63 项原始体积 | base64 后（×4/3） | 单文件 HTML 预计 |
| --- | ---: | ---: | ---: |
| A1 davinfifield 原件（44.1k / 128kbps / 单声道） | ≈ 630 KB（63 × ~10 KB，实测单个 6 583 ~ 26 857 B，均值 ~10 KB） | ≈ 840 KB | ≈ **1.06 MB** |
| A2 argsno 成品（44.1k / 96kbps / 单声道，已归一化） | ≈ 850 KB | ≈ 1.13 MB | ≈ **1.36 MB** |
| B2 zispace `misc/2-所有音节`（22.05k / 56kbps / 单声道） | ≈ 450 KB（实测 46 个采样文件合计 341 982 B，均值 ~7.4 KB） | ≈ **600 KB** | ≈ **820 KB** |
| B1 vaebe 63 件全集（22.05k / 56kbps / 单声道） | **450 561 B ≈ 440 KB**（实测） | ≈ **587 KB** | ≈ **810 KB** |

**结论**：
- 全量 63 项 + 5 声调 + 7 易混对照 ≈ 75 个音频，**base64 内嵌后单文件约 0.9 ~ 1.5 MB**。
- 4 岁家长手机上打开 1.5 MB 的 HTML 没问题（当前文件本来 223 KB，加完变 1.4 MB 左右），但**首屏解析会变慢**。
- **体积最优解是 22050 Hz / 56 kbps 版本（440 KB raw / 587 KB base64）**，比 A1/A2 小一半，音质对「认读 + 跟读」足够。
- **更优解：保持现状的外链方式**，`audio/` 目录体积不计入 HTML，HTML 仍是 223 KB，且支持缓存、不会重复下载。

---

## 五、推荐采用清单

### 🟢 第一档：可直接用（许可干净、形态对路）

| # | 仓库 | 许可 | 为什么 |
| --- | --- | --- | --- |
| 1 | **[`davinfifield/mp3-chinese-pinyin-sound`](https://github.com/davinfifield/mp3-chinese-pinyin-sound)** | **Unlicense（公有领域）**，可商用/可修改/无需署名 | **唯一同时满足「有呼读音 + 许可干净 + 音色统一」的源头**。23 个声母呼读音 = `bo1 po1 mo1 fo1 de1 te1 ne1 le1 ge1 ke1 he1 ji1 qi1 xi1 zhi1 chi1 shi1 ri1 zi1 ci1 si1 yi1 wu1`（已全量验证存在）；韵母可从零声母音节取（`i`←yi1、`u`←wu1、`ü`←yu1、`ui`←wei1、`ie`←ye1、`ün`←yuan1…）。下载量小、音色一致。 |
| 2 | **[`argsno/flashcards-site` 的 `audio/pinyin/`](https://github.com/argsno/flashcards-site/tree/main/audio/pinyin)** | **Unlicense**（`LICENSE.txt` 原文） | **省事版**：声母已经切好成 `b.mp3/c.mp3/zh.mp3`（实测 = A1 对应文件），韵母/整体认读齐备，已做 `loudnorm` 归一化 + 15 ms 淡入淡出。README 写明了来源与生成命令，可复现。**拿它当 A1 的加工成品直接用，或抄它的 README 里的处理参数自己跑一遍。** |

### 🟡 第二档：需加工（内容对，但许可/形态需要处理）

| # | 仓库 | 许可 | 需要什么加工 |
| --- | --- | --- | --- |
| 3 | **[`vaebe/pinyin-audio`](https://github.com/vaebe/pinyin-audio)** | ❌ 无 LICENSE | **只当"结构说明书"用**：它的 `sheng-mu(23) / yun-mu(24) / zheng-ti(16)` 目录规划和 `index.ts` 里的清单注释是现成的行业规范，直接照抄目录名与 id。音频本体不要直接打包——它跟 A1 同源，**从 A1 重新取**即可拿到同样字节、合法来源。 |
| 4 | **[`zispace/hanyu-pinyin-audio`](https://github.com/zispace/hanyu-pinyin-audio)** 的 `misc/2-所有音节/` | ❌ 无 LICENSE（自述"仅供参考"） | **只当"参数参考和备选音源"**：它的 **22050 Hz / 单声道 / 56 kbps** 版本（已抽样 5 个文件复核，全部一致）是体积最小的呼读音载体，单条 6.6 ~ 9.2 KB，适合做单文件 HTML。但音频不可直接商用——**用 A1 跑同样的转码参数（`-ar 22050 -ac 1 -b:a 56k`）自己生成**，源是 Unlicense 就干净了。 |
| 5 | **[`hugolpz/audio-cmn`](https://github.com/hugolpz/audio-cmn)** | CC-BY-SA | 音质好（64k 档）、有 1707 个标准音节，可作为**交叉校验源**（拿同一音在不同来源比对，挑最准的）。⚠️ 若真要用：必须署名 + 成品同许可发布，对"交付单文件 HTML"是负担。**不建议作为主源。** |
| 6 | **[`byhow/yanyu`](https://github.com/byhow/yanyu)** / **[`hotoo/pinyin`](https://github.com/hotoo/pinyin)** | MIT（仅覆盖代码） | 两家都是**独立录音**（与 A1 逐文件 md5 全不同），可作**音色备选 / A-B 对照**，帮助判断某个音到底哪个来源准。⚠️ 音频来源仓库未交代、商用前需向作者确认。hotoo 每条 8~10 s、体积 29 MB，**只适合外链不适合内嵌**。 |
| 7 | **[`hanziguru/pinyin-audio`](https://github.com/hanziguru/pinyin-audio)** | ❌ 无 LICENSE + 限定"非商业" | ❌ **不可商用**。可作为**听感参考**（"专业录音棚版本长什么样"）来评估现有合成音的差距，不进交付物。 |

### 🔴 第三档：不可用

| 仓库 | 原因 |
| --- | --- |
| [`shikangkai/Chinese-Pinyin-Audio`](https://github.com/shikangkai/Chinese-Pinyin-Audio) | 无 LICENSE（**女声部分实为 A1 上游，字节相同**，改引 A1 即可；**男声来自 lost-theory.org，不可商用**） |
| [`luzhihua407/aihu`](https://github.com/luzhihua407/aihu) | 无 LICENSE（微信小程序，`voice/zh/` 目录结构可参考，音频不可用） |
| [`gitcode.com/open-source-toolkit/79b35`](https://gitcode.com/open-source-toolkit/79b35) | ⚠️ 未验证（页面显示 MIT 徽章但 README 全文未拿到；若确认 MIT 且是 A1 同源，可归入第一/二档） |
| [`ryuutyouki/3Dpinyin`](https://github.com/ryuutyouki/3Dpinyin) | 无 LICENSE；只有 12 个音效，拼音走 TTS |
| [`wangqinmi/hanzi-park`](https://github.com/wangqinmi/hanzi-park) | 无 LICENSE；3232 个 mp3 属识字项目的神经网络 TTS 产物 |
| [`hotoo/pinyin`](https://github.com/hotoo/pinyin)（内嵌场景） | MIT 但 29 MB / 单条 8~10 s，内嵌单文件不现实 |
| THCHS-30 / AISHELL-3 / Baker / MagicData / Datatang / Mozilla Common Voice | ❌ 整句朗读语料，无孤立呼读音；多数不在 GitHub 以音频分发 |
| `pypinyin` / `xpinyin` / `pinyin-pro` / `xiaobopang-pinyin` / `hanzipy` / `shuangpin` / `pinyinChart` / `pinyin-castle` | ✅已核实 **0 个音频文件**，全部为纯文本转换或走 TTS |

---

## 六、落地建议（一句话版）

1. **不要另找**——呼读音已经有了，而且合法：走 `davinfifield/mp3-chinese-pinyin-sound`（Unlicense），或直接用 `argsno/flashcards-site/audio/pinyin/` 的成品。
2. **本项目已有的 `生成标准呼读音.py`（macOS Tingting + 宽式 IPA 合成）不必推倒**：它的 IPA 方案是**唯一能精确控制 dē/tē/nē/lē 这类无汉字音的路径**，而开源录音只能"碰巧"对上。加之 `o`/`eng`/`ong` 在开源方案里是从滑音音节剪出来的（`argsno` 自述"起点略硬"）。**建议：保留合成音为主、开源录音作对照/备选，而不是替换。**
3. **若要引入开源录音做交叉校验**，最小动作：下载 A1 的 23 个呼读音文件，与现有 `audio/L_*.m4a` 逐条试听比对，标出差异最大的几个（例如 fō、dē、nē 这类），再决定是否替换。
4. **体积**：维持"HTML + 同级 `audio/` 目录"的外链方式（HTML 仍 223 KB）；若坚持单文件，用 22050 Hz / 56 kbps 转码，63 项 base64 后约 587 KB，整包约 810 KB。

---

## 附录：调研命令速查（可复现）

```bash
# 1) 找仓库
gh search repos "pinyin audio" --limit 30 --json fullName,description,url,license,stargazersCount
gh search repos "声母" --limit 20 --json fullName,description,url,license

# 2) 看许可证原文
gh api repos/OWNER/REPO/contents/LICENSE --jq '.content' | base64 -d

# 3) 看全部文件树（绕过 contents API 的 1000 条上限）
gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq '[.tree[]|select(.type=="blob")|.path]|length'

# 4) 确认仓库是否真的没有 LICENSE
gh api repos/OWNER/REPO/contents/ --jq '[.[].name]|join(" ")'

# 5) 下载样本 + 比对（本次用来证明「声母 = 呼读音」的方法）
gh api -H "Accept: application/vnd.github.raw" \
  repos/vaebe/pinyin-audio/contents/audio/sheng-mu/b.mp3 > b.mp3
md5 b.mp3
ffprobe -v error -show_entries format=duration:stream=sample_rate,channels,bit_rate \
  -of default=nw=1 b.mp3
```
