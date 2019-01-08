#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/2 下午12:28

import matplotlib.pyplot as pyplot
import numpy
import sklearn
# 导入线性回归模型
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

'''
# 输入两个点的横坐标
X = [[1], [4], [3]]
# 输入两个点的纵坐标
y = [3, 5, 3]
'''
X, y = make_regression(
    n_samples=50,
    n_features=1,
    n_informative=1,
    noise=50,
    random_state=1
)

# 用线性模型拟合这两个点
lr = LinearRegression().fit(X, y)

# 画出两个点和直线的图形
z = numpy.linspace(-3, 3, 200).reshape(-1, 1)

pyplot.scatter(X, y, s=80)
pyplot.plot(z, lr.predict(z), c='k')
pyplot.title('Straight Line')
pyplot.show()

# 直线方程
print '\n直线方程为：'
print 'y = %.3fx + %.3f\n' % (lr.coef_[0], lr.intercept_)


if __name__ == "__main__":
    pass
