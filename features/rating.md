# 用户评分

开启「添加用户评分和用户名颜色」后，用户名会按评分显示颜色，个人主页上也会显示具体分数。

## 怎么算

$$\text{评分} = \frac{\text{AC 的提交数}}{\text{全部提交数}} \times 1000$$

全部提交数包括 WA、TLE、CE 等所有结果。所以评分看的是命中率，不是做了多少题。

| 用户 | 全部提交 | AC | 评分 |
|------|---------|----|------|
| A | 100 | 80 | <span class="rating red">800</span> |
| B | 200 | 90 | <span class="rating yellow">450</span> |
| C | 150 | 50 | <span class="rating green">333</span> |
| D | 100 | 20 | <span class="rating blue">200</span> |

评分在浏览器里缓存一天，所以今天的提交通常明天才会反映出来。

## 颜色

| 颜色 | 评分 |
|------|------|
| <span class="rating red">红</span> | 高于 500 |
| <span class="rating yellow">黄</span> | 400–500 |
| <span class="rating green">绿</span> | 300–399 |
| <span class="rating blue">蓝</span> | 低于 300 |

## 在哪里显示

- 讨论区的帖子和回复
- 短消息
- 比赛排名
- 个人主页（显示具体分数）

## 想提高评分？

少交没把握的代码。提交前先在本地测好；没过的时候，用[获取测试点数据](./get-data)找到原因再改，别反复试。
