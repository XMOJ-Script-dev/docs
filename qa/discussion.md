# 常见问题

## 脚本安装问题

安装相关问题请优先查阅[安装指南 → 常见问题](../guide/installation#常见问题)章节，涵盖了安装后无效果、开发者模式等最常见情况。

---

## 讨论区 / 短消息问题

### JSON 解析错误

**错误提示：**
```
JSON解析错误：SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

**原因：** VPN / 代理将请求重定向到了代理服务器的错误页面，返回了 HTML 而非 JSON。

**解决方法：**
- 更换 VPN 节点或链路后重试
- 或暂时关闭代理访问讨论区

---

### D1 Error（数据库错误）

**错误提示：**
```
D1 Error
```

**原因：** 后端数据库（Cloudflare D1）发生了临时异常，通常为偶发性问题。

**解决方法：** 刷新页面后重试，一般可自行恢复。

---

### Cloudflare Challenge / 访问被拦截

**症状：** 讨论区一直转圈、显示 Cloudflare 验证页面或报 403 错误。

**解决方法：**

1. 新开标签页直接访问 [https://api.xmoj-bbs.me](https://api.xmoj-bbs.me)
2. 在该页面完成 Cloudflare 的人机验证（通常会自动通过，或点击验证按钮）
3. 验证通过后返回讨论区，重新访问即可

若上述方法无效，请联系管理员 @zhuchenrui2 手动将您的 IP 加入白名单。

---

### 短消息在线看登录失败

**症状：** 会话登录时提示「登录失败」或「用户名或 Session 无效」。

**可能原因：**
- `PHPSESSID` 已过期（退出登录、长时间未使用会导致 Session 失效）
- 用户名输入错误（注意大小写）
- 复制 `PHPSESSID` 时前后带有多余空格

**解决方法：** 重新登录 [www.xmoj.tech](https://www.xmoj.tech) 获取最新的 `PHPSESSID`，参照[短消息在线看](../apps/messages#方式二会话登录通用支持移动端)的步骤操作。

---

## 脚本运行时错误

如遇脚本运行报错，请按以下步骤收集信息后再反馈：

1. 按 <kbd>F12</kbd> 打开浏览器开发者工具，切换到「**Console**」选项卡
2. 复制完整的错误信息（包括错误类型、文件名和行号）
3. 在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 中搜索是否有相同问题
4. 如无已有 Issue，[新建 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose) 并提供：
   - 错误信息完整截图
   - 浏览器名称与版本
   - Tampermonkey 版本
   - XMOJ-Script 版本
   - 触发错误的操作步骤

---

## 功能请求

有想要的新功能？请在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new/choose) 提交 Feature Request，描述你的使用场景和期望行为。

> 在提交前请先搜索一下，避免重复。

---

## 其他问题

如遇文档中未提及的问题，欢迎在以下渠道寻求帮助：

- 💬 [讨论区](https://www.xmoj-bbs.me) — 适合日常使用问题和经验交流
- 🐛 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) — 适合 Bug 报告和功能建议

