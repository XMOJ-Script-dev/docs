# 贡献代码

欢迎提 PR。我们人少、时间也少，下面这些规矩能帮我们更快地合并你的代码。

## 先开 Issue

做新功能之前，先[开一个 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose) 说说你的想法，等我们回复了再动手。修 bug 可以直接提 PR。

我们的原则是**稳定比功能重要**：新功能不能让原来能用的东西坏掉。

## 往哪个分支提

| 分支 | 用途 |
|------|------|
| `master` | 正式版，不接受 PR |
| `dev` | 开发分支，只接受项目成员的 PR |
| `extern-contrib` | **外部贡献者请提到这里** |

```bash
git checkout -b my-fix origin/extern-contrib
# 改代码、在浏览器里测试……
git fetch origin && git merge origin/extern-contrib   # 提 PR 前先合并最新代码
```

提到 `master` 或 `dev` 的外部 PR 会被关掉。

## 代码风格

| 类型 | 写法 | 例子 |
|------|------|------|
| 变量 | camelCase | `submitCount` |
| 函数 | PascalCase | `GetUserRating` |
| 类 | TitleCase | `NavbarStyler` |

- **不要**跑格式化工具（Prettier 之类），会产生一大堆无关改动。老代码风格不统一，也请保持原样。
- 用 Bootstrap 的类，少写自定义 CSS。
- 换行符用 LF。
- 加新的外部库之前先问我们。
- 版本号由 CI 自动更新，不要手动改。

## 报 bug

到 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 反馈，写清楚：

- 发生了什么，你本来想要什么
- 怎么复现
- 浏览器和版本，比如 Chrome 140
- 脚本管理器和版本
- XMOJ-Script 版本（在 Tampermonkey 控制面板里能看到）
- 按 <kbd>F12</kbd> 打开控制台，有报错的话截图

GitHub Issues 是公开的，不要贴密码、Cookie 或 `PHPSESSID`。

## 行为准则

互相尊重，耐心等 review。我们是业余项目，回复可能慢。PR 没被合并不代表你的贡献不重要。详见 [Code of Conduct](https://github.com/XMOJ-Script-dev/XMOJ-Script/blob/master/CODE_OF_CONDUCT.md)。
