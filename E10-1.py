# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********使用pandas生成csv******#
data = {"os": ['Machintosh', 'Windows', 'Linux'],
        "release": [1984, 1985, 1991],
        "country": ['US', 'US', '']}
df = pd.DataFrame(data)
df.to_csv('OSlist.csv')
