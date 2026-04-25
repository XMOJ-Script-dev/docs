# ELXMOJ — 桌面客户端

**ELXMOJ** 是基于 [Electron](https://www.electronjs.org/) 构建的小明的OJ桌面客户端。它在原生应用窗口中打开 `www.xmoj.tech`，并**自动注入 XMOJ-Script 用户脚本**，让您无需安装浏览器扩展即可享受脚本的全部增强功能。

- 官网：[https://elxmoj.xmoj-bbs.me](https://elxmoj.xmoj-bbs.me)
- GitHub：[XMOJ-Script-dev/ELXMOJ](https://github.com/XMOJ-Script-dev/ELXMOJ)

## 主要功能

| 功能 | 说明 |
|------|------|
| 🖥️ 原生桌面体验 | 独立窗口，无需打开浏览器 |
| 💉 自动注入脚本 | 启动时自动注入 `XMOJ.user.js`，无需 Tampermonkey |
| 🔄 脚本更新检测 | 每次启动可自动检查脚本是否有新版本 |
| ⚙️ 设置持久化 | 更新通道、启动行为等设置持久保存 |
| 🔍 启动自检 | 内置自检功能，快速排查运行问题 |
| 🌐 多平台支持 | 支持 Windows、macOS、Linux |

## 下载安装

当前版本：**v1.1.0**

前往 [GitHub Releases](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/latest) 下载最新版本，或直接点击下方对应平台的链接：

### Windows

| 安装包类型 | 下载链接 |
|-----------|---------|
| 安装程序（推荐） | [ELXMOJ-1.1.0-win-x64.exe](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/download/v1.1.0/ELXMOJ-1.1.0-win-x64.exe) |

下载后双击 `.exe` 文件，按照安装向导完成安装（支持自定义安装目录）。

::: tip Windows 安全提示
首次运行时，Windows SmartScreen 可能弹出警告"Windows 已保护你的电脑"。点击"**更多信息**" → "**仍要运行**"即可继续安装。这是因为应用尚未进行微软代码签名，不影响安全性。
:::

### macOS

| 安装包类型 | 下载链接 | 适用架构 |
|-----------|---------|---------|
| DMG 镜像 | [ELXMOJ-1.1.0-mac-arm64.dmg](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/download/v1.1.0/ELXMOJ-1.1.0-mac-arm64.dmg) | Apple Silicon (M1/M2/M3) |
| ZIP 压缩包 | [ELXMOJ-1.1.0-mac-arm64.zip](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/download/v1.1.0/ELXMOJ-1.1.0-mac-arm64.zip) | Apple Silicon (M1/M2/M3) |

打开 `.dmg` 文件，将 `ELXMOJ.app` 拖入"应用程序"文件夹。

::: tip macOS 安全提示
首次打开时，macOS Gatekeeper 可能提示"无法验证开发者"。请前往**系统设置 → 隐私与安全性**，点击"**仍要打开**"授权运行。
:::

### Linux

| 安装包类型 | 下载链接 |
|-----------|---------|
| AppImage（推荐） | [ELXMOJ-1.1.0-linux-x86_64.AppImage](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/download/v1.1.0/ELXMOJ-1.1.0-linux-x86_64.AppImage) |
| tar.gz 压缩包 | [ELXMOJ-1.1.0-linux-x64.tar.gz](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/download/v1.1.0/ELXMOJ-1.1.0-linux-x64.tar.gz) |

使用 AppImage 时，需先赋予执行权限：

```bash
chmod +x ELXMOJ-1.1.0-linux-x86_64.AppImage
./ELXMOJ-1.1.0-linux-x86_64.AppImage
```

## 应用设置

打开设置窗口：菜单栏 **ELXMOJ → 设置**

### 更新通道

| 通道 | 脚本来源 | 适用场景 |
|------|---------|---------|
| **正式版**（默认） | `https://xmoj-bbs.me/XMOJ.user.js` | 日常使用，稳定版本 |
| **预览版** | `https://dev.xmoj-bbs.me/XMOJ.user.js` | 体验新功能，可能不稳定 |

### 启动行为

- **启动时检查脚本更新**：每次启动 ELXMOJ 时自动联网检查脚本是否有新版本，发现新版本时弹窗提示
- **自动注入 userscript**：启动后自动将 `XMOJ.user.js` 注入到页面，关闭此选项则以普通浏览器模式打开 XMOJ

### 工具

| 操作 | 说明 |
|------|------|
| 立即检查更新 | 手动触发脚本版本检查 |
| 执行自检 | 检查应用运行环境，输出诊断信息 |
| 下载最新 App | 获取 ELXMOJ 应用本身的最新版下载链接 |

## 菜单栏功能

ELXMOJ 在系统菜单栏中提供以下入口（位于 **ELXMOJ** 菜单）：

- **设置** — 打开设置窗口
- **执行自检** — 运行启动自检
- **检查脚本更新** — 手动检查脚本是否有新版本

## 常见问题

**Q：ELXMOJ 和直接在浏览器中使用脚本有什么区别？**

ELXMOJ 是独立应用，无需安装 Tampermonkey，启动即用，适合不想在浏览器里安装扩展的用户。同时，ELXMOJ 作为专属客户端，未来可支持更多桌面端专属功能（如系统通知等）。

**Q：ELXMOJ 中的脚本版本和 Tampermonkey 中的版本一致吗？**

是的，两者使用相同的 `XMOJ.user.js` 脚本文件，功能完全相同。ELXMOJ 从官网或预览版服务器获取更新。

**Q：启动后白屏或无法加载页面怎么办？**

1. 检查网络连接是否正常，确认可以访问 `www.xmoj.tech`
2. 打开**设置 → 执行自检**，查看诊断输出
3. 如问题持续，可在 [GitHub Issues](https://github.com/XMOJ-Script-dev/ELXMOJ/issues) 中反馈
