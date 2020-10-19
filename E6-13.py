# -*- coding: utf-8 -*-
# author:Gary
import datetime as dt

# ********可视化前提知识：时间序列数据,字符串转datetime********#
s = '2019-10-1'
# s指定字符串，后面的参数指定提前方法
x = dt.datetime.strptime(s, '%Y-%m-%d')
print(x)
