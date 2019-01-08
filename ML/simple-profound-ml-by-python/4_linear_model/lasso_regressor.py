#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/6 下午6:41

from sklearn.linear_model import Lasso
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import numpy

X, y = load_diabetes().data, load_diabetes().target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

lasso = Lasso().fit(X_train, y_train)
print '\n\n代码运行结果：\n'
print '套索回归在训练数据集的得分:%.2f' % (lasso.score(X_train, y_train))
print '套索回归在训练数据集的得分:%.2f' % (lasso.score(X_test, y_test))
print '套索回归使用的特征数:%.2f' % (numpy.sum(lasso.coef_ != 0))

if __name__ == "__main__":
    pass
