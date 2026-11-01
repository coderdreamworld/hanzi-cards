# 奇妙小脑袋 · 逻辑桌游

本目录单独保存逻辑桌游，和识字卡、拼音卡等项目分开维护。

- `index.html`：可离线运行的单文件 Demo。对应本机原稿 `孩子/逻辑桌游_Demo.html`。
- `设计方案.md`：玩法、难度与设计依据。对应本机原稿 `孩子/逻辑桌游_设计方案.md`。
- `../../logic-board-game/index.html`：GitHub Pages 发布副本，访问路径为 `/hanzi-cards/logic-board-game/`。

本机原稿改动后，从仓库根目录同步并检查两份 HTML 一致：

```sh
cp ../../../逻辑桌游_Demo.html src/logic-board-game/index.html
cp ../../../逻辑桌游_设计方案.md src/logic-board-game/设计方案.md
cp src/logic-board-game/index.html logic-board-game/index.html
cmp src/logic-board-game/index.html logic-board-game/index.html
```

单独克隆此仓库开发时，直接修改本目录，再复制 `index.html` 到发布目录。这个 Demo 没有构建步骤或外部依赖。
