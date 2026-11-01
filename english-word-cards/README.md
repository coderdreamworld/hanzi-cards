# 英语单词卡 demo

`index.html` 是可直接打开的单文件交互页面，也是 GitHub Pages 发布文件。当前包含 57 张卡：第 1 层核心 46 词 + 旧 demo 保留的 11 张选学卡，分为 6 个主题岛。插画、样式、交互和文本都内嵌在该文件中，无需构建、安装依赖或加载外部字体。发音使用浏览器 `speechSynthesis`，实际可用声音取决于设备与浏览器。

## 起步词汇规划

### 先说结论

一年级不需要按“几百个单词”设计。更稳妥的判断是：

- 国家课标把 1～2 年级设为英语“预备级”，重点是视、听、说和初步积累听说词汇，没有规定一年级词量。
- 小学 5～6 年级对应的二级才要求初步运用 500 个左右单词，并可在主题下补充 100～300 个词。
- 人教旧版“新起点/一年级起点”官方教材附录中，一年级全年约 98 个词条；第三方把 `a/an` 拆开统计时是 100 个。
- 人教 2024 新版 PEP 一年级预备级教材的第三方同步词表样本约 46 个词。官方未在该介绍页公开逐单元词表，实际使用时以学校课本附录为准。

因此，本项目的默认目标不是“几百词”，而是：**46 个校内跟读核心词，优先做熟；再扩展到 100 个起步词；孩子适应后才考虑 150 词选学池。**

### 学习顺序和验收方式

| 阶段 | 词量 | 学习目标 | 验收方式 |
| --- | ---: | --- | --- |
| 第 1 层 | 46 | 跟着音频听懂、看图说出、会回应课堂指令 | 听音指图、看图说词、做动作 |
| 第 2 层 | 100 | 覆盖一年级常见生活场景，能放进短句和问答 | 用 `I have...`、`This is...`、`Where is...?` 玩卡片 |
| 第 3 层 | 150 | 选学池，供学有余力或一年级起点较早的孩子使用 | 只做听说认读，不默认拼写和默写 |

一年级不把拼写作为主目标。卡片交互可以保留拼写练习，但应放在最后的“挑战”入口，不阻塞听说认读。

### 第 1 层：新版 PEP 一年级参考核心 46 词

> 词表来自第三方同步资源中标注为人民教育出版社的人教 PEP 一年级上下册；正式使用前请用孩子学校课本附录校对。这个表是本 demo 后续扩卡的第一优先级。

| 分类 | 词数 | 单词与中文 |
| --- | ---: | --- |
| 问好 | 3 | hello 你好；hi 嗨；bye 再见 |
| 课堂学习 | 8 | pencil 铅笔；book 书；show 展示；open 打开；look 看；listen 听；read 读；say 说 |
| 上学物品 | 4 | bottle 瓶子；pencil case 笔袋；bag 书包；cap 帽子 |
| 身边的人 | 6 | brother 哥哥/弟弟；dad 爸爸；mum 妈妈；sister 姐姐/妹妹；classmate 同班同学；teacher 老师 |
| 礼貌称呼 | 4 | thank 谢谢；Mr 先生；sorry 抱歉；Miss 女士/小姐 |
| 清洁和身体 | 5 | wash 洗；hand 手；face 脸；brush 刷；tooth 牙齿 |
| 食物 | 6 | noodle 面条；tomato 西红柿；rice 米饭；carrot 胡萝卜；apple 苹果；banana 香蕉 |
| 宠物 | 5 | dog 狗；bird 鸟；fish 鱼；rabbit 兔子；cat 猫 |
| 特征和动作 | 5 | big 大的；swim 游泳；fly 飞；small 小的；run 跑 |

### 第 2 层：从 46 词补到 100 个起步词

下面 54 个词主要从人教旧版“新起点/一年级起点”一年级词表中挑选，用来补齐功能词、颜色、数字、身体、教室、饮食。与上面 46 词合并后正好 100 个，且无重复。

| 分类 | 词数 | 单词与中文 |
| --- | ---: | --- |
| 高频功能词 | 24 | I 我；a 一个；an 一个；the 这/那；is 是；are 是；this 这；it 它；my 我的；you 你/你们；what 什么；no 不；yes 是；and 和；have 有；do 做；like 喜欢；in 在里面；on 在上面；under 在下面；where 哪里；can 能/会；how 怎么；many 许多 |
| 颜色 | 6 | red 红色；yellow 黄色；green 绿色；blue 蓝色；black 黑色；pink 粉色 |
| 数字 | 7 | one 一；four 四；five 五；six 六；seven 七；eight 八；nine 九 |
| 身体 | 4 | ear 耳朵；eye 眼睛；nose 鼻子；mouth 嘴 |
| 教室和房间 | 8 | desk 书桌；chair 椅子；schoolbag 书包；ruler 尺子；blackboard 黑板；door 门；box 盒子；bed 床 |
| 饮食 | 5 | water 水；tea 茶；milk 牛奶；juice 果汁；egg 鸡蛋 |

### 第 3 层：150 词选学池

在第 100 词之后，优先补下面 50 个。它们是选学内容，不建议当作一年级达标要求。

- 衣服和描述：short 短的；your 你的；T-shirt T 恤；sock 袜子；skirt 短裙；shorts 短裤；shirt 衬衫；dress 连衣裙
- 吃喝和感受：thirsty 渴的；thanks 谢谢；duck 鸭子；want 想要；vegetable 蔬菜；hungry 饿的；chicken 鸡肉
- 玩具和出行：ship 轮船；train 火车；plane 飞机；doll 洋娃娃；car 小汽车；bear 熊；ball 球
- 家居和方位：near 在附近；light 灯；behind 在后面
- 水果：watermelon 西瓜；grape 葡萄；pear 梨；orange 橙子
- 综合扩展：colour 颜色；dolphin 海豚；tiger 老虎；monkey 猴子；sure 当然；jump 跳；eat 吃；sleep 睡觉；sun 太阳
- 通用补充：white 白色；two 二；three 三；ten 十；play 玩；draw 画；drink 喝；sing 唱；dance 跳舞；moon 月亮；star 星星；rain 雨

### 当前 57 卡版本的构成

核心 46 词已按 5 个主题岛完整并入 `index.html`：

1. 问好课堂岛：10 词。
2. 上学伙伴岛：10 词。
3. 礼貌清洁岛：9 词。
4. 食物岛：6 词。
5. 动物动作岛：11 词。

旧 demo 中不在核心 46 词内的 jump、eat、sleep、can、do、in、on、under、sun、car、ball 被保留为第 6 个“选学岛”。这样旧功能不丢失，但主线仍以核心 46 词为先。

后续扩到 100 词时，优先补第 2 层表格中尚未出现的功能词、颜色、数字、身体、教室和饮食；每批仍保持 8～10 词，并同步补齐 `sentence / say / chat / life / act / how / art` 七类内容。

### 来源和口径

- 教育部《义务教育英语课程标准（2022 年版）》：一级对应 3～4 年级，二级对应 5～6 年级；1～2 年级设预备级，以视听说为主。二级词汇要求为“初步运用 500 个左右单词”。见[官方 PDF](http://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582349487953.pdf)。
- 人民教育出版社《义务教育英语（PEP）》新教材简介：三至六年级为国家课程主体，一二年级预备级教材供地方课程规划选用。见[人教社介绍页](https://www.pep.com.cn/xw/zt/hd/12/xjcjs/xx/202409/t20240920_1995564.html)。
- 人教旧版一年级起点官方电子教材入口：[一年级上册](https://book.pep.com.cn/1212001101123/mobile/index.html)、[一年级下册](https://book.pep.com.cn/1212001102123/mobile/index.html)。附录按单元呈现，全年约 98 个词条。
- 新版 PEP 一年级上下册词表参考：[一年级上册](https://yyld.51jiaoxi.com/yishang/rjbp_danci.html)、[一年级下册](https://yyld.51jiaoxi.com/yixia/rjbp_danci.html)。这是第三方同步资源，不是官方公开词表。

## 文件

- `index.html`：唯一需要同步的程序文件。
- `previews/`：桌面、手机、手机拼写状态与 57 张插画总览的审查图；不参与页面运行。
- `designs/`：46 个起步核心词的 baoyu-design 分批设计稿。第 1～5 批分别对应问好与课堂、上学物品与身边人、礼貌清洁身体、食物、宠物特征动作；每批含 HTML、截图与 `_d_meta.json`。

### 当前版本交互

- 主题岛切换、数字点选、左右箭头、键盘方向键和移动端左右滑动均可换卡。
- 点图或点单词朗读单词；底部圆形按钮朗读当前英文例句。
- 普通读 `rate=1.05`，慢慢读 `rate=0.55`，均固定 `lang="en-US"` 并优先选择可用美式声音。
- 每张卡有英文例句、跟读提示、追问、生活迁移、身体动作和画面线索；这些内容在“更多玩法与卡片说明”中分层展示。
- “拼一拼”只取字母，不把 `pencil case` 的空格做成空位；“藏起字”用于先听音再看答案。

### 完整性检查口径

修改 `index.html` 后至少运行：

1. 静态检查：卡片数、唯一单词数、每个字段非空、HTML 标签闭合、JS 语法可解析。
2. 桌面检查：1440×900 与 1280×720 均不能出现页面级横向或纵向滚动。
3. 手机检查：390×844 不能出现页面级横向溢出；主题岛和数字条只允许内部滚动。
4. 内容检查：逐张切换 57 卡，确认 SVG、单词、例句和提示均渲染。
5. 交互检查：读一遍、慢慢读、读句子、拼一拼、藏字/揭晓、键盘和主题切换。
6. 控制台检查：无运行时异常；favicon 404 也视为发布前问题。

## 发布与维护

本目录是本地权威副本。GitHub 仓库 `coderdreamworld/hanzi-cards` 中的 `english-word-cards/` 是同一 demo 的独立发布目录。修改本地 `index.html` 或 `README.md` 后，把对应文件复制到仓库的 `english-word-cards/`，核对两份文件一致，再提交并推送。在线直达地址是 <https://coderdreamworld.github.io/hanzi-cards/english-word-cards/>。

新增单词时，在 `index.html` 的卡片数据中增加一项，补齐 `sentence / say / chat / life / act / how / art`，并按“完整性检查口径”回归。`previews/` 随设计变化更新即可。
