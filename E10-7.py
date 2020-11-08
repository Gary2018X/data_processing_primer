# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********使用pandas去重******#
dupli_data = pd.DataFrame({'col1': [1, 1, 2, 3, 4, 4, 6, 6, 7, 7, 7, 8, 9, 9],
                           'col2': ['a', 'b', 'b', 'b', 'c', 'c', 'b', 'b', 'd', 'd', 'c', 'b', 'c', 'c']})
print(dupli_data)
print(dupli_data.drop_duplicates())
