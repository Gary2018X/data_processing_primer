# -*- coding: utf-8 -*-
# author:Gary
from pandas import DataFrame

# ********使用pandas复习******#
data1 = {"ID": [100, 101, 102, 103, 104, 106, 108, 110, 111, 113],
         "city": ['beijing', 'shanghai', 'wuhan', 'xian', 'beijing', 'beijing', 'shanghai', 'wuhan', 'xian', 'beijing'],
         "birty_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
         "name": ['zhang3', 'li4', 'wang5', 'zhao6', 'qian7', 'liu8', 'gao9', 'sun10', 'wu11', 'chen12']
         }
data1_frame1 = DataFrame(data1)

data2 = {"ID": [107, 109],
         "city": ['changsha', 'tianjin'],
         "birty_year": [1994, 1988],
         "name": ['tan13', 'gong14']
         }
data2_frame2 = DataFrame(data2)

# 合并数据,排序,重置行号

data1_frame1 = data1_frame1.append(data2_frame2).sort_values(by='ID', ascending=True).reset_index(drop=True)
print(data1_frame1)
