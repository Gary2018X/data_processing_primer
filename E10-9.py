# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********使用pandas数据离散化处理******#
data1 = {"ID": [100, 101, 102, 103, 104, 106, 108, 110, 111, 113],
         "city": ['beijing', 'shanghai', 'wuhan', 'xian', 'beijing', 'beijing', 'shanghai', 'wuhan', 'xian', 'beijing'],
         "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
         "name": ['zhang3', 'li4', 'wang5', 'zhao6', 'qian7', 'liu8', 'gao9', 'sun10', 'wu11', 'chen12']
         }
data1_frame1 = pd.DataFrame(data1)
birth_year_bins = [1980, 1985, 1990, 1995, 2000]
group_names = ['1980前', '85后', '1990前', '95后']
birth_year_cut_data = pd.cut(data1_frame1.birth_year, birth_year_bins, labels=group_names)
print(birth_year_cut_data)
