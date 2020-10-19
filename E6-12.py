# -*- coding: utf-8 -*-
# author:Gary
import datetime as dt

# ********可视化前提知识：时间序列数据计算,timedelta和datetime********#
# 生成表示“2019年10月1日”的datetime对象，将其赋予给变量x
x = dt.datetime(2019, 10, 1)
# 生成表示假期时长为七天的timedelta对象，将其赋予给变量z
z = dt.timedelta(days=7)

# 生成表示x之后z天（要上班的日子）的datetime对象，并赋予y
y = x + z
print(y)
d = z * 2  # 假期翻倍
print(d)
d = d + dt.timedelta(days=1)  # 在此翻倍基础上再加一天
print(d)
# 输出时间翻了多少倍
print(d/z)

