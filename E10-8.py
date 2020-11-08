# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********使用pandas匹配******#
data1 = {"ID": [100, 101, 102, 103, 104, 106, 108, 110, 111, 113],
         "city": ['beijing', 'shanghai', 'wuhan', 'xian', 'beijing', 'beijing', 'shanghai', 'wuhan', 'xian', 'beijing'],
         "birty_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
         "name": ['zhang3', 'li4', 'wang5', 'zhao6', 'qian7', 'liu8', 'gao9', 'sun10', 'wu11', 'chen12']
         }
data1_frame1 = pd.DataFrame(data1)
NS_map = {'beijing': 'north', 'shanghai': 'south', 'xian': 'north', 'wuhan': 'south'}
data1_frame1['NS'] = data1_frame1['city'].map(NS_map)
print(data1_frame1)
