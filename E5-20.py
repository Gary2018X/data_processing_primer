# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# 参考博客：https://blog.csdn.net/zyuPp/article/details/107229096
prefecture_df = pd.DataFrame([["广东", 19.97, 1134, "华南"],
                              ["广西", 23.76, 5659, "华南"],
                              ["湖北", 18.59, 6028, "华中"],
                              ["湖南", 21.18, 6700, "华中"],
                              ["陕西", 20.56, 3813, "西北"]],
                             columns=["Prefecture", "Area", "Population", "Region"])
print(prefecture_df)

# 将prefecture_df按大区（region）进行组化，结果赋予给变量grouped_df;
grouped_df = prefecture_df.groupby('Region')  # 按照Region列分组
print(grouped_df)

# 对prefecture_df中出现的各个大区，统计各大区的平均面积和平均人口;
# 方法一
df2 = grouped_df[['Area', 'Population']].mean()  # 求均值
print(df2)


# 方法二，利用apply方法
def f(df):
    data = {'A_mean': df['Area'].mean(), 'P_mean': df['Population'].mean()}
    return pd.Series(data)


print(grouped_df.apply(f))

# 方法三，老师的方法
grouped_region = prefecture_df.groupby('Region')
mean_df = grouped_region.mean()
print(mean_df)
