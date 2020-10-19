# -*- coding: utf-8 -*-
# author:Gary
import numpy as np

# ********可视化前提知识：二项分布随机********#
np.random.seed(0)
# 成功概率0.5，次数为100的二项分布试验中，求总试验次数为1w次时总成功数
nums = np.random.binomial(100, 0.5, size=10000)

# 成功的评价概率
print(nums.mean() / 100)
