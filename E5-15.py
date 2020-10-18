# -*- coding: utf-8 -*-
# author:Gary
import pandas as pd

# ********pandas 不同列标签结合的基本使用********#
order_df = pd.DataFrame([[1000, 2546, 103], [1001, 4352, 101], [1002, 342, 101]],
                        columns=['id', 'item_id', 'customer_id'])

customer_df = pd.DataFrame([[101, 'zhang'], [102, 'li'], [103, 'wang']], columns=['id', 'name'])

# 使用customer_df的"id"和order_df的"customer_id"，将customer_df结合到order_df中;
order_df = pd.merge(order_df, customer_df, left_on='customer_id', right_on='id', how='inner')
print(order_df)
