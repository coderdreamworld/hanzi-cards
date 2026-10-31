# 识字卡片插画：GitHub 同类技术方案调研

- 调研日期：2026-10-25
- 调研问题：有没有和我们同样"用代码画插画"（SVG/HTML 标记拼接）但画面质量明显更好的 skill 或工具箱？能否解决现在 402 卡里"手很长、脸没腿、形象奇怪、画风不贴切"的问题？
- 硬约束前提：单文件 HTML 飞书预览 ≤12MB；同页 400+ 卡禁 `<defs>/<use>/<text>/<image>`；插画必须极小体积——这正是坚持矢量代码画的理由。

## 一句话结论

**没有一个现成的 skill 能直接"把儿童识字卡的 SVG 小人画好"。** 但 GitHub 上同类"代码画图"的高质量项目沉淀出了同一套方法论共识：**质量不靠模型自由发挥，靠"固定视觉系统 + 硬性几何约束 + 校验脚本 + 人类插画师设计的部件库"**。这套东西都可以移植进我们现有的 `素材库.py` / `设计规范.md` 契约；如果想要"细腻、真实"的画质跃迁，则要走"图像模型生成 → vtracer 矢量化回 SVG"的混合管线，体积上依然守得住 12MB（见 §5 测算）。

## 现状基线

- 成品 `识字卡片_422字.html` = **1.5MB**，402 卡平均约 **3.7KB/卡**；12MB 上限下每卡预算约 24KB（留余量后按 15–20KB 规划），即还有 **约 8 倍体积余量**可以换更精细的插画。
- 现有 `kid()` 是一个单体函数（stand/sit/walk/run/sleep × arms × face），四肢长度在函数内部写死；"手长/没腿"类崩坏来自设计 Agent 绕开组件自己拼形状时没有比例约束，也没有任何脚本去量几何。

## 1 同一技术路线（代码画图）且质量更好的标杆

### 1.1 op7418/guizang-social-card-skill（归藏，7.7k star，AGPL-3.0）——方法论最值得抄

小红书图文卡 skill：单文件 HTML 排版 → Playwright 截图出 PNG。它和我们是同一件事（代码拼画面），质量靠四层锁：

- **固定视觉系统**：只给 Editorial / Swiss 两套画风 × 28 个版式骨架 × 10 套主题预设，**禁止自定义 hex 颜色**——防止 Agent 随手发明配色。
- **DOM 实测校验脚本** `validate-social-deck.mjs`：9 条规则基于 Playwright 真实测量（溢出、footer 碰撞、字号下限、密度带），不是"目测好看"。
- 7 步结构化工作流（Intake→主题→版式→取图→渲染→交付→迭代），文字压图有主体避让 / quiet-zone 规则。
- 注意 license 是 **AGPL-3.0**：**借鉴方法论没问题，不要直接复制它的代码/文本进我们仓库**。

### 1.2 sai-tv/academic-figures（MIT）——和我们素材库契约最同构的范本

学术 SVG 插图 skill，纯代码生成可编辑矢量图。它证明了几何硬约束写进 SKILL.md 的做法：

- 内置规范文件（期刊栏宽/字号/边距，如 Nature 单栏 89mm）；Wong 2011 色盲安全调色板，自定义色必须过对比度检查；
- **硬性几何约束**：箭头最短 10mm、标签距箭头线 3.5mm、面板标签距内容 2.5mm……全部是"数字"而不是形容词；
- 每个交付变体都换布局与风格，交稿前过 QA 清单。

→ 对我们的启示：`设计规范.md` 里"友好圆润、重心居中"这类形容词，应升级为**比例常数表**（见 §5 建议 1）。

### 1.3 anthropics/skills 的 canvas-design（官方，Apache 2.0）——代码画"艺术"的官方上限

官方"用代码做博物馆级视觉"的 skill：纯代码绘制（重复图案、精确几何、分层图案），输出 PNG/PDF。方法论两步：先写一篇"设计哲学宣言"（美学运动命名 + 4–6 段空间/色彩/比例/层级的阐述），再据此作画；最后有**强制精修环节**——"不加新图形，回头打磨既有构图"。它的"哲学先行 + 精修收尾"两步值得并入我们的设计 Agent 流程。

### 1.4 其他同类

- MrBongoC/ai-iso-skill：等距（isometric）插画单 HTML，同一思路在小众画风上的实现。
- GitHub topic [`claude-skills`](https://github.com/topics/claude-skills)、清单 [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)、[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)、[bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) 可继续淘，但目前没有比上述三个更对口的"代码画儿童插画"skill。

## 2 换引擎路线：图像模型 + 强风格锁定（画质上限更高）

这些不是代码画图，但在"怎么让 AI 画得贴切、不崩"上是最成熟的方案：

### 2.1 helloianneo/ian-xiaohei-illustrations（小黑插画，12.8k star，MIT）——风格圣经的最佳模板

中文正文配图 skill，12.8k star。每张图单独调图像模型生成 PNG（16:9）。它的高分不在模型，在**约束写法**：

- **角色圣经**：视觉 IP"小黑"（黑色实心、白点眼、细腿、空表情），描述精确到可复现；
- **先规划后生成**：读内容 → 提炼认知锚点 → 输出 shot list（每张的主题/结构类型/动作）→ 再逐张生成；
- **隐喻必须重新发明**，禁止复刻示例构图；"如果去掉主角画面仍成立，说明主角太装饰了"；
- **QA checklist 收尾**：白底、留白、动作清晰、无错字、非 PPT 感逐项过。

→ 这正是"角色圣经 + 跨工具提示词"那两份存档文档的成熟工程化版本，可直接借鉴它的 SKILL.md 组织方式。

### 2.2 儿童绘本流水线

- [ayushnagvanshi101098-ship-it/book-illustration-engine](https://github.com/ayushnagvanshi101098-ship-it/book-illustration-engine)：风格锁定 + 角色一致 + 印刷级儿童绘本插画流水线（Claude Code 插件 + fal.ai/Flux LoRA）。
- [picture-book-wizard](https://github.com/aiskillstore/marketplace/blob/main/skills/kart-io/picture-book-wizard/README.md)（aiskillstore 市场）：一致角色的双语儿童绘本，18 种视觉风格。
- GitHub topic：[`character-consistency`](https://github.com/topics/character-consistency)、[`consistent-characters`](https://github.com/topics/consistent-characters) ——"不训练 LoRA 也让角色跨图一致"的 skill 群。

**与 12MB 的冲突及解法**：图像模型出的是位图（单张几百 KB 起），402 张直接内嵌必然超限。桥接工具见 §4 的 vtracer——把扁平风位图矢量化回 SVG，通常能压到 10–80KB/张，按卡筛选使用仍可守住上限；或走 WebP 高压缩 + 分卷 HTML。

## 3 结构性根治"手长/没腿"：换用人类插画师设计的部件库

Agent 自己拼椭圆和矩形，人体崩坏是随机的；改用**人类画师预先设计好头/手/腿/姿势的部件库**，拼装结果天然不崩，且都是矢量 SVG、体积小、可换色：

| 库 | License | 是什么 | 对我们的用法 |
| --- | --- | --- | --- |
| [Open Peeps](https://github.com/openpeeps/open-peeps)（官方站 [openpeeps.com](https://www.openpeeps.com)） | CC0 | 手绘感人物：头/发型/脸/上身/下身/站坐姿**全拆分**，58 万+组合，SVG+PNG | `kid()` 的人体部分替换源首选；CC0 无需署名 |
| [Humaaans](https://www.humaaans.com)（GitHub 镜像 [Calinou/humaaans](https://github.com/Calinou/humaaans)） | CC0 | 混搭人物（Pablo Stanley），姿势/服装/发型/配色可换 | 同上备选，风格更现代 |
| [DiceBear](https://github.com/dicebear/dicebear) | 核心 MIT，**各风格单独 license**（见 [licenses 页](https://www.dicebear.com/licenses/)） | 63 种风格头像/人物，seed 确定性生成 SVG，有本地 JS 库与 HTTP API | 可本地批量产出人物 SVG 再内联；`croodles`/`doodle`/`big-smile`/`open-peeps` 等风格贴儿童 |
| [OpenMoji](https://github.com/hfg-gmuend/openmoji) | CC BY-SA 4.0 | 4,495 个 emoji 级 SVG（含大量动作/食物/动物/物品），HfG 设计学院出品，颜色和黑白两套 | 动词卡（跑/吃/找）与物品卡可直接取材；**需在 HTML 里加署名**，且衍生需同方式共享 |
| [flowbite-illustrations](https://github.com/themesberg/flowbite-illustrations) | MIT | 50+ 3D 风格 SVG 插画 | 场景卡点缀备选 |
| 清单 | — | [MrPeker/awesome-illustrations](https://github.com/MrPeker/awesome-illustrations)、[goabstract/Awesome-Design-Tools](https://github.com/goabstract/Awesome-Design-Tools)、[toools.design](https://www.toools.design/free-open-source-illustrations)、[unDraw](https://undraw.co)（开放 license，500+ 扁平场景） | 继续扩库用 |

注意：部件库配色需要映射到我们 PALETTE 统一色板（SVG 属性替换即可）；部件库人体与代码画的物件混排时，加地面椭圆和统一光源方向保持画风一致。

## 4 配套工具链（把两条路线焊起来）

- [visioncortex/vtracer](https://github.com/visioncortex/vtracer)（**MIT**）：彩色位图→SVG 矢量化（层级聚类 + 曲线拟合），有 Python CLI / npm / 网页版。图像模型产物 → vtracer → 矢量小图 → 内联 HTML，是"画质跃迁"与"12MB 红线"的桥。
- [SVGO](https://github.com/svg/svgo)：SVG 无损压缩（去 metadata、合并路径），vtracer 输出后再过一遍，通常再省 30–60%。
- Playwright 截图管线：归藏 skill 的 `render.mjs` 思路（HTML→PNG 交付或对照验收），本机可直接复用。

## 5 落地建议（按投入排序）

1. **零换栈、立即做：给现有契约补"硬约束 + 校验脚本"**（借鉴 §1 全部三家）
   - `设计规范.md` 增加比例常数表：头身比（现 kid() H=300/头 r=62 ≈ 2.4 头身）、臂展 ≤ 身高 × k、手长 ≤ 头半径 × k、四肢必须落地/落髋坐标区间……全部写成数字；
   - 新增校验脚本：用 ElementTree 解析 `arts()` 输出，量关键部件包围盒与比例、检查是否踩 `defs/use/text` 禁令、检查主体是否落在地面椭圆上，超限直接报错——等价于归藏的 DOM 实测校验 + academic-figures 的几何约束；
   - 流程加"精修环节"（canvas-design）：交稿前不允许再加新元素，只许修主体。
2. **中期：人物换部件库**（§3）——Open Peeps（CC0）或 DiceBear 儿童系风格做 `kid()` 的人体来源，物件/场景继续代码画；这是"手长/没腿"的**结构性根治**，且体积可控（单部件 SVG 数 KB）。
3. **画质跃迁（可选）：图像模型 + 小黑方法论 + vtracer**（§2 + §4）——用"角色圣经 + shot list + QA 清单"约束图像模型逐卡生成 → vtracer 矢量化 → SVGO → 内联；单卡按 ≤20KB 预算，402 卡总量约 4–8MB，仍在 12MB 内。角色一致性可参考 book-illustration-engine 的流水线设计。
4. **License 红线**：AGPL（归藏）只学方法不抄代码；CC BY-SA（OpenMoji）内联需在 HTML 加署名且衍生同方式共享；CC0（Open Peeps/Humaaans）与 MIT（DiceBear 核心、vtracer、academic-figures、flowbite）最省心。

## 来源

- https://github.com/op7418/guizang-social-card-skill
- https://github.com/sai-tv/academic-figures
- https://github.com/anthropics/skills （canvas-design：`skills/canvas-design/SKILL.md`）
- https://github.com/MrBongoC/ai-iso-skill
- https://github.com/helloianneo/ian-xiaohei-illustrations
- https://github.com/ayushnagvanshi101098-ship-it/book-illustration-engine
- https://github.com/aiskillstore/marketplace/blob/main/skills/kart-io/picture-book-wizard/README.md
- https://github.com/topics/character-consistency 、https://github.com/topics/consistent-characters
- https://github.com/openpeeps/open-peeps 、https://www.openpeeps.com
- https://www.humaaans.com 、https://github.com/Calinou/humaaans
- https://github.com/dicebear/dicebear 、https://www.dicebear.com/licenses/
- https://github.com/hfg-gmuend/openmoji
- https://github.com/themesberg/flowbite-illustrations
- https://github.com/MrPeker/awesome-illustrations 、https://github.com/goabstract/Awesome-Design-Tools 、https://www.toools.design/free-open-source-illustrations 、https://undraw.co
- https://github.com/visioncortex/vtracer 、https://github.com/svg/svgo
- https://github.com/ComposioHQ/awesome-claude-skills 、https://github.com/travisvn/awesome-claude-skills 、https://github.com/bergside/awesome-design-skills
