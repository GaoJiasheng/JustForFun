#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/29 11:10

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import base
from sklearn import preprocessing
import numpy as np

x = np.array([
    [0., -3., 1.],
    [3., 1., 2.],
    [0., 1., -1.]
])

# Min-max
base.chapter("min-max")
min_max_scaler = preprocessing.MinMaxScaler()
min_max_x = min_max_scaler.fit_transform(x)
print(min_max_x)

# Z-score
base.chapter("Z-score")
scaled_x = preprocessing.scale(x)
print(scaled_x)

# 小数定标
base.chapter("小数定标")
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

if __name__ == "__main__":
    pass