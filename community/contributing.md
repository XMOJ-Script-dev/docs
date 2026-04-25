# 贡献指南

欢迎为 XMOJ-Script 贡献代码！在开始之前，请仔细阅读本页内容。我们是一个小团队，非常欢迎来自社区的高质量 PR。

## 分支说明

| 分支 | 用途 | PR 目标 |
|------|------|---------|
| `master` | 稳定发布版 | ❌ 不接受外部 PR |
| `dev` | 日常开发 | ❌ 不接受外部 PR |
| `extern-contrib` | **外部贡献专用** | ✅ 外部开发者请提交到此分支 |

::: warning 外部贡献者注意
请务必将 Pull Request 提交到 **`extern-contrib`** 分支，直接向 `master` 或 `dev` 提交的 PR 将被关闭。
:::

## 贡献流程

```text
1. Fork XMOJ-Script-dev/XMOJ-Script
2. 从 extern-contrib 分支新建功能分支
   git checkout -b feature/your-feature extern-contrib
3. 编写代码并在本地测试
4. 将最新的 extern-contrib 合并到你的分支，解决冲突
   git fetch origin && git merge origin/extern-contrib
5. 提交 Pull Request → extern-contrib 分支
```

## 代码规范

### 命名约定

| 类型 | 风格 | 示例 |
|------|------|------|
| 变量 | `camelCase` | `userId`, `submitCount` |
| 函数 | `PascalCase` | `GetUserRating`, `SubmitCode` |
| 类 | `TitleCase` | `RatingSystem`, `ImageUploader` |

> 旧代码中可能存在不符合规范的命名，但**新代码必须严格遵循**上述约定。

### 其他规范

- ❌ **不要**运行代码格式化工具（Prettier / clang-format 等），避免引入大量格式噪声
- ❌ **不要**在未经核心开发者同意的情况下引入新的外部依赖库
- ✅ 使用 **Bootstrap 5** 样式类，尽量避免编写自定义 CSS
- ✅ 使用 **Unix 换行符**（LF，`\n`），不要使用 Windows CRLF
- ✅ 提交 PR 前务必先将 `extern-contrib` 合并到你的分支并解决所有冲突

## 新功能开发

在动手写代码前，请先 [开一个 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose) 描述你的想法，等待核心开发者讨论并认可后再开始实现。

**核心原则：稳定 > 功能。** 新功能不能引入回归，不能降低脚本在主流浏览器上的兼容性。

## 行为准则

- 请**尊重**每一位开发者和社区成员
- 请**耐心**等待 PR 审核，我们是业余项目，响应时间不固定
- 请**理解**我们的决定，PR 被拒绝并不代表贡献不被珍视
- 请遵守 [Code of Conduct](https://github.com/XMOJ-Script-dev/XMOJ-Script/blob/master/CODE_OF_CONDUCT.md)

## 提交 Bug 或建议

发现 Bug 或有功能建议，欢迎在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 中反馈。

提交 Bug 时请提供：

- [ ] 问题的详细描述（实际行为 vs 预期行为）
- [ ] 可复现的最小步骤
- [ ] 浏览器名称与版本（如 Chrome 124）
- [ ] Tampermonkey 版本
- [ ] XMOJ-Script 版本（控制面板中可查看）
- [ ] 浏览器开发者工具 Console 截图（如有报错）

