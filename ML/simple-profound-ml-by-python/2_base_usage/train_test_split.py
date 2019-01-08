#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/2 上午9:21

import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(10).reshape((5,2))
print X
y = range(5)

print '\norigin data : '
print X, y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print '\ntrain data : '
print X_train, y_train
print '\ntest data : '
print X_test, y_test

if __name__== "__main__":
    pass