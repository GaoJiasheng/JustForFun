#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/5 上午9:47
print("...")

from sklearn.linear_model import Ridge
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pyplot

X, y = load_diabetes().data, load_diabetes().target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# alpha参数的最佳设置取决于我们使用的特定数据集，增加alpha值会降低特征变量的系数,使其趋于零
# 个人理解：其实就是给各个变量加入了权重的概念。(不一定对)
ridge = Ridge(alpha=1).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
lr = LinearRegression().fit(X_train, y_train)


print('\n代码运行结果：')
print('岭回归训练数据集得分：%.2f' % (ridge.score(X_train, y_train)))
print('岭测试训练数据集得分：%.2f' % (ridge.score(X_test, y_test)))
print('\n')

# alpha = 10 的系数大多在0附近
# alpha = 1 时系数普遍增大了, alpha=0.1时就更大了
# alpha=0.1大部分与线性回归的点重合了
pyplot.plot(ridge01.coef_, 's', label='Ridge alpha=0.1')
pyplot.plot(ridge.coef_, '^', label='Ridge alpha=1')
pyplot.plot(ridge10.coef_, 'v', label='Ridge alpha=10')
pyplot.plot(lr.coef_, 'o', label='Linear regression')
pyplot.xlabel("coefficient index")
pyplot.ylabel("coefficient magnitude")
pyplot.hlines(0, 0, len(lr.coef_))
pyplot.legend()
pyplot.show()

if __name__ == "__main__":
    pass
