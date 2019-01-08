#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/6 下午5:40

from sklearn.model_selection import learning_curve,KFold
import numpy
import matplotlib.pyplot as pyplot
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes().data, load_diabetes().target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 定制一个学习曲线的函数
def plot_learning_curve(est, X, y):
    # 将数据进行20次拆分来对模型进行评分
    training_set_size, train_scores, test_scores = learning_curve(
        est, X, y, train_sizes=numpy.linspace(.1, 1, 20),
        cv=KFold(20, shuffle=True,random_state=1))
    estimator_name = est.__class__.__name__
    line = pyplot.plot(training_set_size, test_scores.mean(axis=1),
                       '-', label='training '+estimator_name)
    pyplot.plot(training_set_size, test_scores.mean(axis=1), '*',
                label='test '+estimator_name, c=line[0].get_color())
    pyplot.xlabel('Training set size')
    pyplot.ylabel('Score')
    pyplot.ylim(0, 1.1)

plot_learning_curve(Ridge(alpha=1), X_train, y_train)
plot_learning_curve(LinearRegression(), X_train, y_train)
pyplot.legend(loc=(0, 1.05), ncol=2, fontsize=11)
pyplot.show()

if __name__ == "__main__":
    pass
