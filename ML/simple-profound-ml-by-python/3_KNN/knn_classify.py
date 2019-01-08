#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 下午6:29

# ------------------START-------------------------------
# 导入数据集生成器
from sklearn.datasets import make_blobs

# 导入KNN分类器
from sklearn.neighbors import KNeighborsClassifier

# 导入画图工具
import matplotlib.pyplot as pyplot

# 导入数据集拆分工具
from sklearn.model_selection import train_test_split

# 生成样本数为200，分类为2的数据集
data = make_blobs(n_samples=500, centers=5, random_state=8)
X, y = data

# 将生成的数据进行可视化
#plt.scatter(X[:,0], X[:,1], c = y, cmap=plt.cm.spring, edgecolor='k')
#plt.show()

# ------------------CLASSIFIER-------------------------------
import numpy as np
clf = KNeighborsClassifier()
clf.fit(X, y)

# 下面代码用于画图
x_min, x_max = X[:, 0].min() -1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() -1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
print Z

TEST_POINTS = [
    [7.5,1.5],
    [3.0,3.0],
    [4.0,4.0],
    [6.0,6.0],
    [0,0]
]

print('\n\n\n')
print('代码运行结果')
print('==============================')
print '新数据点的分类是：', clf.predict(TEST_POINTS)
print('==============================')
print('模型正确率: {:.2f}'.format(clf.score(X, y)))
print('==============================')

pyplot.pcolormesh(xx, yy, Z, cmap=pyplot.cm.Pastel1)
pyplot.scatter(X[:, 0], X[:, 1], c=y, cmap=pyplot.cm.spring, edgecolor='k')
pyplot.xlim(xx.min(), xx.max())
pyplot.ylim(yy.min(), yy.max())
pyplot.title("Classifier:KNN")

for point in TEST_POINTS:
    if len(point) >= 2:
        pyplot.scatter(point[0], point[1], marker='*', c='red', s=200)

pyplot.show()

if __name__ == "__main__":
    pass
