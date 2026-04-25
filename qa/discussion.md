# 常见问题

## 讨论区无法访问

### 问题一：JSON 解析错误

**错误信息：**
```
JSON解析错误：SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

**原因：** 您开启了 VPN 或代理，导致请求被重定向到代理服务器的错误页面。

**解决方案：**
- 更换 VPN 节点（链路）
- 或直接关闭代理后再访问

---

### 问题二：D1 Error

**错误信息：**
```
D1 Error
```

**原因：** 数据库临时错误，通常为偶发性问题。

**解决方案：**
- 刷新页面重试

---

### 问题三：Cloudflare Challenge / 访问被拦截

**症状：** 讨论区显示 Cloudflare 验证页面或一直加载。

**解决方案：**

1. 手动访问 [https://api.xmoj-bbs.me](https://api.xmoj-bbs.me)，完成 Cloudflare Challenge 验证
2. 验证通过后返回讨论区，问题通常会自动解决
3. 若仍有问题，可联系 @zhuchenrui2 手动将您的 IP 加入白名单

---

## 脚本相关问题

### 安装后无效果

请参考[安装指南](../guide/installation)中的"常见安装问题"部分。

### 脚本报错

如遇脚本运行时报错，请：

1. 打开浏览器开发者工具（按 <kbd>F12</kbd>），查看 Console 中的错误信息
2. 在 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 中搜索是否有相同问题
3. 如无已有 Issue，请[新建 Issue](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues/new) 并附上：
   - 错误信息截图
   - 浏览器名称和版本
   - Tampermonkey 版本
   - 脚本版本

---

## 反馈与建议

如果您遇到文档中未提及的问题，欢迎通过以下渠道反馈：

- 📋 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) — Bug 反馈与功能建议
- 💬 [讨论区反馈版](https://www.xmoj-bbs.me) — 日常使用问题咨询
