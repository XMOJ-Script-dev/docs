# 短消息在线看

不装脚本，也能在任何浏览器里收发小明的OJ的短消息，手机上也行。

打开：[www.xmoj-script.uk/messages.html](https://www.xmoj-script.uk/messages.html)

能做的事：看联系人和对话、回复、给任何人发新消息、粘贴图片、搜索联系人，支持暗色模式。

## 登录

它需要你在小明的OJ上的登录凭证 `PHPSESSID`。有两种方式拿到。

::: warning PHPSESSID 就相当于你的密码
拿到它的人可以用你的账号登录小明的OJ。不要发给任何人，也不要贴到讨论区或 GitHub 上。
:::

### 书签登录（电脑）

最省事的方法。

1. 打开短消息在线看，切到「书签登录」。
2. 把「登录到短消息在线看」按钮拖到书签栏。
3. 打开 [www.xmoj.tech](https://www.xmoj.tech)，确认已经登录。
4. 点一下刚才的书签，会自动跳回来并登录。

### 会话登录（手机和电脑都行）

手动复制 `PHPSESSID`，填到「会话登录」里，连同你的用户名一起提交。

**电脑上**：登录 [www.xmoj.tech](https://www.xmoj.tech)，按 <kbd>F12</kbd> 打开开发者工具。Chrome 和 Edge 切到「应用」（Application），Firefox 切到「存储」，在 Cookie → `www.xmoj.tech` 里找到 `PHPSESSID`，复制它的值。

**iPhone / iPad**：需要一台 Mac。在 iPhone 的 Safari 里登录小明的OJ，然后在 Mac 的 Safari 里选「开发」→ 你的设备 → xmoj.tech 页面，在网页检查器的「储存空间」里找到 `PHPSESSID`。

页面上也有每种浏览器的详细步骤。

## 用法

- **看对话**：点左边的联系人。
- **回复**：在底部输入，点「发送」。
- **发新消息**：点「发新消息」，填收件人和内容。
- **发图片**：在输入框里按 <kbd>Ctrl</kbd>+<kbd>V</kbd>。图片的注意事项见[粘贴发图](../features/image-hosting)。
- **换主题**：点右上角的主题按钮。

## 注意

- 登录信息保存在你的浏览器里。清除浏览器数据后要重新登录。
- 在小明的OJ上退出登录，`PHPSESSID` 就失效了，这里也要重新登录。
- 短消息存在 XMOJ-Script 的服务器上，加密保存。详见[隐私说明](https://www.xmoj-script.uk/privacy.html)。
