# 英语单词卡 demo

`index.html` 是可直接打开的单文件交互原型，也是 GitHub Pages 发布文件。19 个单词分在 8 个主题岛；插画、样式和交互都内嵌在该文件中，无需构建或安装依赖。发音使用浏览器 `speechSynthesis`，实际可用声音取决于设备与浏览器。

## 文件

- `index.html`：唯一需要同步的程序文件。
- `previews/`：桌面、手机、手机拼写状态与 19 张插画总览的审查图；不参与页面运行。

## 发布与维护

本目录是本地权威副本。GitHub 仓库 `coderdreamworld/hanzi-cards` 中的 `english-word-cards/` 是同一 demo 的独立发布目录。修改本地 `index.html` 后，复制到仓库的 `english-word-cards/index.html`，核对两份文件一致，再提交并推送。在线直达地址是 <https://coderdreamworld.github.io/hanzi-cards/english-word-cards/>。

新增单词时，在 `index.html` 的卡片数据中增加一项，并检查插画语义、发音、主题切换、桌面一屏显示和手机横向溢出。`previews/` 随设计变化更新即可。
