# 安装指南

本页面将引导您完成 XMOJ-Script 的完整安装流程。

::: tip 快速安装
1. 安装 [Tampermonkey](https://www.tampermonkey.net/) 浏览器扩展
2. 在浏览器扩展管理页面开启**开发者模式** <span style="color: red;">*</span>
3. 在 Tampermonkey 扩展管理页面开启**允许运行用户脚本** <span style="color: red;">*</span>
4. 点击 [安装 XMOJ-Script](https://xmoj-bbs.me/XMOJ.user.js) → 在弹出框中点击「安装」

> <span style="color: red;">*</span> 表示对于 Chrome / Edge 138+ 的用户需要进行的操作
>
> 由于 Google Chrome Manifest V3 政策，Tampermonkey 必须在**开发者模式**下或启用**允许用户脚本**扩展开关才能完整运行用户脚本。**跳过此步骤会导致脚本无法工作。**
>
> 详见 [Tampermonkey 官方说明 → Q209](https://www.tampermonkey.net/faq.php#Q209)
:::

## 1 安装 Tampermonkey

XMOJ-Script 是一个 **用户脚本（Userscript）**，需要借助 Tampermonkey 等用户脚本管理器来运行。

请根据您使用的浏览器，点击对应链接安装 Tampermonkey：

| 浏览器 | 安装链接 | 备注 |
|--------|---------|------|
| Google Chrome | [Chrome 应用商店](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)（[国内镜像](https://chrome.zzzmh.cn/info/dhdgffkkebhmkfjojejmpbldmpobfkfo)） | 推荐 |
| Microsoft Edge | [Edge 加载项商店](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd) | 推荐 |
| Mozilla Firefox | [Firefox 附加组件](https://addons.mozilla.org/firefox/addon/tampermonkey/) | 无需开发者模式 |
| Safari | [App Store](https://apps.apple.com/app/tampermonkey/id1482490089) | 需额外配置 |
| Opera | [Opera 插件商店](https://addons.opera.com/extensions/details/tampermonkey-beta/) | — |

## 2 开启浏览器开发者模式 <span style="color: red;">*</span>

::: warning <center>Chrome / Edge 138+ 必须完成此步骤</center>
:::

### Google Chrome

1. 地址栏输入 `chrome://extensions` 并按 <kbd>Enter</kbd>
2. 找到页面**右上角**的「**开发者模式**」（Developer mode）开关将其**打开**

   ![Chrome 开发者模式](/developer_mode.jpg)

3. 刷新页面后生效

### Microsoft Edge

1. 地址栏输入 `edge://extensions` 并按 <kbd>Enter</kbd>
2. 找到页面**左下角**的「**开发人员模式**」开关将其**打开**

   ![Edge 开发者模式](/developer_mode_edge.jpg)

### Mozilla Firefox

Firefox **无需**开启开发者模式，安装 Tampermonkey 后即可直接跳到第三步。

### Safari（macOS）

1. 打开 Safari →「偏好设置」→「高级」选项卡
2. 勾选「**在菜单栏中显示"开发"菜单**」
3. 菜单栏出现「开发」菜单后，点击「**允许未签名的扩展**」
4. 在 Safari 扩展列表中**启用** Tampermonkey

## 3 允许扩展运行用户脚本 <span style="color: red;">*</span>

::: warning <center>Chrome / Edge 138+ 必须完成此步骤</center>
:::

### Google Chrome

1. 地址栏输入 `chrome://extensions` 并按 <kbd>Enter</kbd>
2. 进入 Tempermonkey 扩展「**详情**」页面

   ![Chrome 扩展详情](/extension_detail.jpg)

3. 勾选「**允许运行用户脚本**」

   ![Chrome 允许运行用户脚本](/allow_userscript.jpg)

### Microsoft Edge

1. 地址栏输入 `edge://extensions` 并按 <kbd>Enter</kbd>
2. 进入 Tempermonkey 扩展「**详细信息**」页面

   ![Edge 扩展详细信息](/extension_detail_edge.jpg)

3. 勾选「**允许用户脚本**」

   ![Edge 允许用户脚本](/allow_userscript_edge.jpg)

::: details 如何确认配置是否生效？
点击浏览器右上角扩展 → Tampermonkey 图标。若弹出页面正常打开且不显示「请启用开发者模式以允许用户脚本注入。点击这里了解如何操作。」等警告内容，说明至此配置已生效。
:::

## 4 安装 XMOJ-Script

<a href="https://xmoj-bbs.me/XMOJ.user.js" style="display:inline-flex;align-items:center;gap:8px;padding:8px 20px;background:#1a7f37;color:#fff;border-radius:6px;text-decoration:none;font-weight:600;font-size:0.95rem;border:1px solid rgba(31,35,40,0.15);">最新稳定版（推荐）</a>
<a href="https://ghpages.xmoj-bbs.me/XMOJ.user.js" style="display:inline-flex;align-items:center;gap:8px;padding:8px 20px;background:#3092ad;color:#fff;border-radius:6px;text-decoration:none;font-weight:600;font-size:0.95rem;border:1px solid rgba(31,35,40,0.15);margin-left:12px;">预览版</a>

点击上方其中一个按钮后，Tampermonkey 将弹出脚本安装确认页面，确认信息无误后点击「**安装**」即可。

::: info 备用最新版安装渠道
- [ScriptCat 镜像站](https://scriptcat.org/zh-CN/script-show-page/1500/)：国内访问更快
- [GitHub Releases](https://github.com/XMOJ-Script-dev/XMOJ-Script/releases/latest)：手动下载 `XMOJ.user.js` 后拖入 Tampermonkey 控制面板
:::

## 5 验证安装

1. 打开 [www.xmoj.tech](https://www.xmoj.tech)
2. 若页面样式明显变化（导航栏更新、Bootstrap 风格按钮），说明脚本已运行
3. 登录后点击右上角用户名，若菜单中出现「**插件设置**」，则安装完成 ✅

## 更新脚本

XMOJ-Script 支持**自动更新**。Tampermonkey 会定期检查最新版并静默更新。

手动更新步骤：

1. 点击 Tampermonkey 图标 →「**控制面板**」
2. 找到 XMOJ-Script 条目，点击右侧「**更新**」按钮（或「检查更新」）

## 常见问题

### 安装后访问 xmoj.tech 没有变化？

按以下顺序逐项排查：

| 检查项 | 说明 |
|--------|------|
| Tampermonkey 是否已启用 | 扩展图标不应显示灰色或带叉 |
| XMOJ-Script 脚本是否已启用 | 控制面板中脚本开关应为打开状态 |
| 开发者模式是否已开启 | Chrome / Edge 必须，见第二步 |
| 是否访问了正确的域名 | 确认是 `xmoj.tech` 而非其他域名 |
| 尝试硬刷新 | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>（macOS：<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>）|

### 提示「此扩展程序未经 Chrome 网上应用店验证」？

这是 Chrome 在启用开发者模式后对所有通过非商店途径安装的扩展显示的**标准安全提示**，属于正常现象。Tampermonkey 本身已通过 Chrome 商店审核，`.user.js` 是用户脚本的标准格式，不影响安全性。

### 安装页面显示乱码或加载失败？

可能是网络问题导致 GitHub 资源访问缓慢。请：
- 尝试通过 [ScriptCat 镜像](https://scriptcat.org/zh-CN/script-show-page/1500/) 安装
- 或稍后重试主安装链接

### 如何完全卸载脚本？

1. 打开 Tampermonkey 控制面板
2. 找到 XMOJ-Script 条目
3. 点击右侧删除（垃圾桶）图标
4. 确认删除即可，不影响浏览器本身

