#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/2 下午6:06

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

'''
X, y = make_regression(
    n_samples=100,
    n_features=3,
    n_informative=2,
    random_state=38
)
'''
from sklearn.datasets import load_diabetes
X, y = load_diabetes().data, load_diabetes().target


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
lr = LinearRegression().fit(X_train, y_train)

print 'lr.coef_ : ', lr.coef_[:]
print 'lr.intercept_ : ', lr.intercept_

print '训练数据集得分：', lr.score(X_train, y_train)
print '测试数据集得分：', lr.score(X_test, y_test)

if __name__ == "__main__":
    pass