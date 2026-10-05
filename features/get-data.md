# 获取测试点数据

提交没过的时候，可以拿到出错那个测试点的输入数据，在本地复现问题。

::: warning 不一定每次都成功
这个功能偶尔会拿不到数据，尤其是在部分比赛里。遇到了请到 [GitHub Issues](https://github.com/XMOJ-Script-dev/XMOJ-Script/issues) 反馈。
:::

## 怎么用

1. 在「插件设置」里确认「获取数据功能」是开着的（默认开启）。
2. 打开没通过的那次提交的详情页。
3. 点「获取数据」。
4. 等一会儿，输入数据会显示在页面上。复制到本地文件里调试。

数据比较大时会慢一些，耐心等。

## 拿到数据之后

```bash
# 把数据存成 input.txt，然后：
g++ -O2 -o solution solution.cpp
./solution < input.txt
```

本地跑出来和预期不一样，就能对着这组数据找 bug 了。
