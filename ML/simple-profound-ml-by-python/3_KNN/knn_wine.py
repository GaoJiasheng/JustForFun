#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 下午10:45

from sklearn.datasets import load_wine

wine_dataset = load_wine()

'''print 看看
print 'data : \n', wine_dataset['data']
print '\ntarget : \n', wine_dataset['target']
print '\ntarget names: \n', wine_dataset['target_names']
print '\nfeature names: \n', wine_dataset['feature_names']
print '\nDESCR: \n', wine_dataset['DESCR']
'''

# 导入数据集拆分工具
from sklearn.model_selection import train_test_split

# 将数据集拆分为训练数据集和测试数据集
X_train, X_test, y_train, y_test = train_test_split(
    wine_dataset['data'], wine_dataset['target'], random_state=0)

# 导入KNN分类模型
from sklearn.neighbors import KNeighborsClassifier

# 指定模型的n_neighbors参数值为1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# 看一下 分类器准确率
print 'classifier score : %.2f' % (knn.score(X_test, y_test),)

# 分类预测
import numpy
X_new = numpy.array([[13.2,2.77,2.51,18.5,96.6,1.04,2.55,0.57,1.47,6.2,1.05,3.33,820]])

# 使用predict预测
prediction = knn.predict(X_new)
print '\n\n\n代码运行结果：\n预测新红酒分类为：', wine_dataset['target_names'][prediction]

if __name__ == "__main__":
    pass
