# 常见问题

## 装了脚本没反应

最常见的原因：Chrome 或 Edge 没有打开「允许用户脚本」。看[安装 → 装了没反应？](../guide/installation#装了没反应)。

## 讨论区和短消息

### 提示「JSON解析错误」

```
JSON解析错误：SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

一般是 VPN 或代理把请求拦了，返回了一个网页。换个节点，或者暂时关掉代理再试。

### 提示「D1 Error」

服务器的数据库临时出错，通常刷新一下就好了。

### 一直转圈，或者提示 403

可能被 Cloudflare 的人机验证拦住了。

1. 新开一个标签页，打开 [api.xmoj-script.uk](https://api.xmoj-script.uk)。
2. 如果出现验证，完成它。
3. 回到小明的OJ刷新。

还是不行，在讨论区找管理员 @zhuchenrui2。

### 短消息在线看登录失败

- `PHPSESSID` 过期了：在小明的OJ退出登录、或者很久没用都会让它失效。重新登录小明的OJ，再复制一次。
- 用户名打错了。
- 复制的时候多带了空格。

步骤见[短消息在线看](../apps/messages#登录)。

## 脚本报错

1. 按 <kbd>F12</kbd> 打开开发者工具，切到「控制台」（Console）。
2. 把红色的报错截图。
3. 先在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 里搜一下有没有人报过。
4. 没有的话，[新建一个 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose)，附上截图、浏览器和版本、XMOJ-Script 版本，以及你做了什么操作。

GitHub Issues 是公开的，截图前确认里面没有 `PHPSESSID`、密码或其他个人信息。

## 想要新功能

到 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose) 提，说清楚你想在什么场景下做什么。先搜一下有没有人提过。

## 其他问题

- 日常使用问题：在小明的OJ的讨论区里问。
- bug 和建议：[GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues)。
- 隐私和数据删除：见[隐私说明](https://www.xmoj-script.uk/privacy.html)。
