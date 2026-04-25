# 安装指南

本页面将引导您完成 XMOJ-Script 的完整安装流程，包括安装用户脚本管理器、开启浏览器开发者模式，以及安装脚本本身。

## 第一步：安装 Tampermonkey

XMOJ-Script 是一个 **用户脚本（Userscript）**，需要借助 Tampermonkey 等用户脚本管理器来运行。

请根据您使用的浏览器，点击对应链接安装 Tampermonkey：

| 浏览器 | 下载链接 |
|--------|---------|
| Google Chrome | [Chrome 应用商店](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) |
| Microsoft Edge | [Edge 加载项商店](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd) |
| Mozilla Firefox | [Firefox 附加组件](https://addons.mozilla.org/firefox/addon/tampermonkey/) |
| Safari | [App Store](https://apps.apple.com/app/tampermonkey/id1482490089) |
| Opera | [Opera 插件商店](https://addons.opera.com/extensions/details/tampermonkey-beta/) |

::: tip 推荐
推荐使用 **Google Chrome** 或 **Microsoft Edge** 以获得最佳兼容性。
:::

## 第二步：开启浏览器开发者模式

::: warning 重要
由于 Google Chrome 的 **Manifest V3** 政策限制，Tampermonkey 必须在**开发者模式**下才能完整运行用户脚本。跳过此步骤可能导致脚本无法正常工作。

详见 [Tampermonkey 官方说明](https://www.tampermonkey.net/faq.php#Q209)。
:::

请根据您的浏览器，按照以下步骤开启开发者模式：

### Google Chrome

1. 在地址栏输入 `chrome://extensions` 并按 <kbd>Enter</kbd>
2. 在页面**右上角**找到"**开发者模式**"（Developer mode）开关
3. 点击将其**打开**（开关变为蓝色）

   ![Chrome 开发者模式示意](https://www.tampermonkey.net/images/faq/dev_mode_chrome.png)

4. 页面刷新后，Tampermonkey 将获得完整权限

### Microsoft Edge

1. 在地址栏输入 `edge://extensions` 并按 <kbd>Enter</kbd>
2. 在页面**左侧底部**找到"**开发人员模式**"开关
3. 点击将其**打开**

   ![Edge 开发者模式示意](https://www.tampermonkey.net/images/faq/dev_mode_edge.png)

4. 刷新浏览器后生效

### Mozilla Firefox

Firefox **无需**开启开发者模式，安装 Tampermonkey 后即可直接使用。

### Safari

Safari 用户需在 **Safari → 偏好设置（Preferences）→ 高级（Advanced）** 中勾选"**在菜单栏中显示开发菜单（Show Develop menu in menu bar）**"，随后在"开发（Develop）"菜单中允许来自未签名来源的扩展（Allow Unsigned Extensions）。

::: details 如何验证开发者模式已成功开启？
安装并启用 Tampermonkey 后，访问 Tampermonkey 的控制台（点击浏览器右上角 Tampermonkey 图标 → **控制台**），若可以正常打开且不显示警告横幅，即代表开发者模式配置正确。
:::

## 第三步：安装 XMOJ-Script

开发者模式开启后，点击下方按钮即可一键安装脚本：

<a href="https://github.com/XMOJ-Script-dev/XMOJ-Script/releases/latest/download/XMOJ.user.js" style="display:inline-block;padding:10px 20px;background:#4CAF50;color:#fff;border-radius:6px;text-decoration:none;font-weight:bold;">⬇️ 安装 XMOJ-Script（最新版）</a>

点击后，Tampermonkey 将弹出安装确认对话框，点击"**安装**"即可完成。

::: tip 备用安装方式
如果上方链接无法访问，可前往 [ScriptCat 镜像](https://scriptcat.org/zh-CN/script-show-page/1500/) 安装，或直接从 [GitHub Releases](https://github.com/XMOJ-Script-dev/XMOJ-Script/releases/latest) 下载 `XMOJ.user.js` 后手动拖入 Tampermonkey 控制台。
:::

## 第四步：验证安装

1. 访问 [xmoj.tech](https://xmoj.tech) 或 [www.xmoj.tech](https://www.xmoj.tech)
2. 若页面样式发生变化（如导航栏更新、按钮风格改变），说明脚本已成功运行
3. 点击右上角**用户名**，菜单中若出现"**插件设置**"选项，即代表安装成功

## 更新脚本

XMOJ-Script 支持**自动更新**。Tampermonkey 会定期检查脚本的最新版本并在后台自动更新。

您也可以手动检查更新：

1. 点击 Tampermonkey 图标 → **控制台**
2. 找到 XMOJ-Script 条目
3. 点击右侧"**更新**"按钮

当前最新版本：**3.4.0**

## 常见安装问题

**Q：安装后访问 xmoj.tech 看不到变化？**

请检查：
- Tampermonkey 扩展是否已启用（扩展图标不应显示为灰色）
- XMOJ-Script 脚本是否处于"已启用"状态
- 是否已正确开启开发者模式（Chrome/Edge）
- 尝试硬刷新页面（<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>）

**Q：提示"此扩展程序未经 Chrome 网上应用店验证"？**

这是正常的 Chrome 安全提示。Tampermonkey 本身是经过 Chrome 应用商店审核的正规扩展，用户脚本（`.user.js`）的执行依赖开发者模式，属于正常机制。

**Q：如何卸载脚本？**

进入 Tampermonkey 控制台，找到 XMOJ-Script，点击右侧垃圾桶图标即可卸载。
