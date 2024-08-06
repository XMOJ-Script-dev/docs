# 用户评分

计算方式：小明的OJ增强脚本的用户评分是基于使用者在小明的OJ (xmoj.tech) 上的正确率计算获得。详细的说，就是用户在小明的OJ上的提交正确率*100，即AC提交数 / 总提交数 * 100（包含等待、忽略等情况）。

用户评分和可以相对客观地评价用户在小明的OJ上做题吸收情况，有利于用户之间的横向促进和比较。

颜色特征：

1. 对于用户评分在500分以上的（正确率50%以上的），用户名将显示红色。
2. 对于用户评分在400分到500分的（包含400分、500分），用户名显示黄色。
3. 对于用户评分在300分到400分的（包含300分不包含400分），用户名将显示绿色。
4. 对于用户评分在300分以下的，用户名将显示蓝色。

与洛谷（luogu.com.cn）用户咕值的差别和相同点：

1. 小明的OJ增强脚本用户评分不考虑对于社区贡献和使用频次，相对既有长效客观性。
2. 小明的OJ增强脚本用户评分实时显示，不具有延迟性。

***

## Rating System

Like Luogu, XMOJ-Script has a rating system. The rating system is used to determine the color of your username.

## How is Rating Calculated?
> Please note that this may change in the future.

Currently, your rating equals your AC rate, i.e.,
The number of accepted submissions divided by the total number of submissions. The rating is then multiplied by 1000
to get the final rating value.
Ratings are cached on the client side for one day.


## Rating Colors

The color of a username in XMOJ-Script is determined by the user's rating. The rating system assigns different colors based on the rating value:

> Please note that this may change in the future.
- **Red**: Assigned if the rating is greater than 500.
- **Yellow**: Assigned if the rating is between 400 and 500 (inclusive).
- **Green**: Assigned if the rating is between 300 and 400 (inclusive).
- **Blue**: Assigned if the rating is less than 300.

This system helps visually distinguish users based on their ratings.