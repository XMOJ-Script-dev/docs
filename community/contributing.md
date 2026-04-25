# 贡献指南

欢迎为 XMOJ-Script 贡献代码！在开始之前，请仔细阅读本页内容。

## 贡献流程

::: warning 外部贡献者注意
外部开发者应基于 **`extern-contrib`** 分支进行修改，并将 Pull Request 提交至 **`extern-contrib`** 分支，**不要**直接向 `master` 或 `dev` 分支提交 PR。
:::

1. Fork [XMOJ-Script 仓库](https://github.com/XMOJ-Script-dev/XMOJ-Script)
2. 从 `extern-contrib` 分支创建您的功能分支
3. 完成代码修改，并在本地测试
4. 将 `extern-contrib` 分支合并到您的分支，解决所有冲突
5. 提交 Pull Request 至 `extern-contrib` 分支

## 代码规范

### 命名约定

| 类型 | 命名风格 | 示例 |
|------|---------|------|
| 变量 | camelCase | `userId`, `submitCount` |
| 函数 | PascalCase | `GetUserRating`, `SubmitCode` |
| 类 | TitleCase | `RatingSystem`, `ImageUploader` |

> 注意：旧代码中可能存在不符合规范的命名，但**新代码必须遵循**上述规范。

### 其他规范

- **不要**运行代码格式化工具（Code Formatter）
- **不要**在未经开发者同意的情况下引入新的外部库
- 使用 **Bootstrap** 样式类，尽量避免编写自定义 CSS
- 使用 **Unix 换行符**（`\n`，LF）
- 提交 PR 前，先将 `extern-contrib` 分支合并到您的分支并解决冲突

## 新功能开发

在开始开发新功能前，请先[开启一个 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new) 与团队讨论，获得认可后再动手编写代码。

我们的核心原则：**稳定性优先于功能**。在添加新功能前，我们会优先修复现有问题。

## 行为准则

- 请**尊重**开发者和其他用户
- 请**耐心**等待审核，我们是小团队，响应速度可能较慢
- 请**接受**我们的决定，即使您的 PR 被拒绝，也请保持良好心态
- 请遵守 [Code of Conduct](https://github.com/XMOJ-Script-dev/XMOJ-Script/blob/master/CODE_OF_CONDUCT.md)

## 提交 Bug 或建议

发现 Bug 或有功能建议？欢迎在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 中反馈。

提交时请尽量提供：
- 问题的详细描述
- 复现步骤
- 浏览器和 Tampermonkey 版本
- 相关截图（如有）
