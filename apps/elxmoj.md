# ELXMOJ 桌面客户端

ELXMOJ 是一个桌面应用。它在自己的窗口里打开小明的OJ，并且已经内置了 XMOJ-Script，不用装浏览器扩展，也不用打开「允许用户脚本」。

- 官网：[elxmoj.xmoj-script.uk](https://elxmoj.xmoj-script.uk)
- 源代码：[XMOJ-Script-dev/ELXMOJ](https://github.com/XMOJ-Script-dev/ELXMOJ)

## 下载

到 [GitHub Releases](https://github.com/XMOJ-Script-dev/ELXMOJ/releases/latest) 下载对应系统的文件：

| 系统 | 文件 |
|------|------|
| Windows | `ELXMOJ-…-win-x64.exe` |
| macOS（Apple 芯片） | `ELXMOJ-…-mac-arm64.dmg` |
| Linux | `ELXMOJ-…-linux-x86_64.AppImage`，或 `.tar.gz` |

### Windows

双击 `.exe` 安装。如果弹出「Windows 已保护你的电脑」，点「更多信息」→「仍要运行」。应用没有买微软的代码签名，所以会有这个提示。

### macOS

打开 `.dmg`，把 ELXMOJ 拖进「应用程序」。第一次打开如果提示无法验证开发者，到「系统设置 → 隐私与安全性」里点「仍要打开」。

目前只有 Apple 芯片（M 系列）的版本。

### Linux

```bash
chmod +x ELXMOJ-*-linux-x86_64.AppImage
./ELXMOJ-*-linux-x86_64.AppImage
```

## 设置

菜单栏里选 **ELXMOJ → 设置**。

- **更新通道**：正式版，或者预览版（新功能先上，可能不稳定）。和浏览器里装的是同一个脚本。
- **启动时检查脚本更新**：有新版本时提示你。
- **自动注入脚本**：关掉的话，ELXMOJ 就是一个普通的浏览器窗口。

设置里还有「执行自检」，出问题时可以先跑一下看看诊断信息。

## 打不开或者白屏？

1. 确认网络能打开 `www.xmoj.tech`。
2. 在设置里点「执行自检」，看看输出。
3. 还是不行，到 [ELXMOJ 的 Issues](https://github.com/XMOJ-Script-dev/ELXMOJ/issues) 反馈。
