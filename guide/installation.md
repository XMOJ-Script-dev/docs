# 安装

一共三步：装一个脚本管理器，允许它运行用户脚本，再装 XMOJ-Script。

::: warning Chrome 和 Edge 用户注意
第二步不能跳过。新版 Chrome 和 Edge 默认不让扩展运行用户脚本，不打开这个开关，脚本装好了也不会生效。这是最常见的「装了没反应」的原因。
:::

## 1. 装脚本管理器

推荐 Tampermonkey。脚本猫（ScriptCat）也可以。

| 浏览器 | 下载 |
|--------|------|
| Chrome | [Chrome 应用商店](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) |
| Edge | [Edge 加载项](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd) |
| Firefox | [Firefox 附加组件](https://addons.mozilla.org/firefox/addon/tampermonkey/) |
| Safari | [App Store](https://apps.apple.com/app/tampermonkey/id1482490089) |

打不开 Chrome 应用商店的话，可以从 [Tampermonkey 官网](https://www.tampermonkey.net/) 找其他下载方式。

## 2. 允许运行用户脚本

先在地址栏打开 `chrome://version` 或 `edge://version`，看看版本号。

### Chrome 138 及以上

1. 地址栏打开 `chrome://extensions`，在 Tampermonkey 下面点「详情」。

   ![Chrome 扩展详情](/extension_detail.jpg)

2. 打开「允许运行用户脚本」开关。

   ![允许运行用户脚本](/allow_userscript.jpg)

### Edge 138 及以上

1. 地址栏打开 `edge://extensions`，在 Tampermonkey 下面点「详细信息」。

   ![Edge 扩展详细信息](/extension_detail_edge.jpg)

2. 打开「允许用户脚本」开关。

   ![允许用户脚本](/allow_userscript_edge.jpg)

### Chrome / Edge 137 及以下

1. 地址栏打开 `chrome://extensions`（Edge 是 `edge://extensions`）。
2. 打开「开发者模式」（Edge 叫「开发人员模式」）。Chrome 在右上角，Edge 在左侧。

   ![Chrome 开发者模式](/developer_mode.jpg)

### Firefox 和 Safari

不需要额外设置，直接下一步。Safari 要在「设置 → 扩展」里启用 Tampermonkey。

::: details 怎么确认设置好了？
点工具栏上的 Tampermonkey 图标。弹出的窗口里没有「请启用开发者模式」之类的提示，就说明设置好了。官方说明见 [Tampermonkey FAQ Q209](https://www.tampermonkey.net/faq.php#Q209)。
:::

## 3. 安装 XMOJ-Script

点下面的按钮，管理器会打开安装页，点「安装」。

<a class="mono-btn" href="https://www.xmoj-script.uk/XMOJ.user.js">安装正式版</a>
<a class="mono-btn alt" href="https://dev.xmoj-script.uk/XMOJ.user.js">安装预览版</a>

预览版会先用上新功能，但可能有 bug。不确定就装正式版。

装不上的话，也可以从 [脚本猫](https://scriptcat.org/zh-CN/script-show-page/1500/) 安装，或者在 [GitHub Releases](https://github.com/XMOJ-Script-dev/XMOJ-Script/releases/latest) 下载 `XMOJ.user.js`，拖进管理器的控制面板。

## 4. 检查一下

打开 [www.xmoj.tech](https://www.xmoj.tech) 并刷新。页面样式变了，就说明脚本在运行。

登录后，右上角的用户菜单里会多出「插件设置」，所有功能都在这里开关。

## 更新

脚本会自己检查更新。有新版本时，页面上会弹出提示，点一下就能更新。也可以在 Tampermonkey 控制面板里手动点「检查更新」。

## 装了没反应？

按顺序检查：

1. 第 2 步的开关打开了吗？Chrome 和 Edge 十有八九是这个问题。
2. Tampermonkey 和 XMOJ-Script 在控制面板里都是启用状态吗？
3. 打开的是 `www.xmoj.tech` 吗？
4. 强制刷新试试：<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>，macOS 上是 <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>。

还是不行，看[常见问题](../qa/discussion)，或者到 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 反馈。

### 浏览器提示「此扩展程序未经验证」？

开启开发者模式后，Chrome 会对扩展显示这个提示。这是正常现象，不影响使用。

## 卸载

在 Tampermonkey 控制面板里找到 XMOJ-Script，点删除图标。
