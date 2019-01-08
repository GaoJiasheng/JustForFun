#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 下午10:003

import numpy
import matplotlib.pyplot as pyplot
# 导入数据集生成器
from sklearn.datasets import make_regression

# 生成特征数量为1，噪音为50的数据集
X, y = make_regression(n_features=1, n_informative=1, noise=50, random_state=8)

# 导入用于回归分析的KNN模型
from sklearn.neighbors import KNeighborsRegressor
reg = KNeighborsRegressor(n_neighbors=2)

# 用KNN模型拟合数据
reg.fit(X, y)

print '\n\n\n'
print '代码运行结果：'
print '====================='
print '模型评分：{:.2f}'.format(reg.score(X, y))
print '====================='

# 把预测结果用图像进行可视化
z = numpy.linspace(-3,3,200).reshape(-1, 1)
pyplot.scatter(X, y,c='yellow', edgecolor='k')
pyplot.plot(z, reg.predict(z), c='red', linewidth=3)

# 给图像添加标题
pyplot.title('KNN Regressor')
pyplot.show()

if __name__ == "__main__":
    pass