#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2020/12/23 2:16 下午

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import base
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base.chapter("scatter")
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
# scatter via matplotlib
plt.scatter(x, y, marker="x")
plt.show()
# scatter via seaborn
df = pd.DataFrame({'x':x, 'y':y})
sns.jointplot(x='x', y='y', data=df, kind='scatter')
plt.show()

base.chapter("line plot")
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
# line plot via Matplotlib
plt.plot(x, y)
plt.show()
# line plot via Seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x="x", y="y", data=df)
plt.show()

base.chapter("histogram")
a = np.random.randn(100)
s = pd.Series(a)
# histogram via matplotlib
plt.hist(s)
plt.show()
# histogram via seaborn
sns.distplot(s, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()

base.chapter("bar")
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]

# bar via Matplotlib
plt.bar(x, y)
plt.show()

# bar via Seaborn
sns.barplot(x, y)
plt.show()

base.chapter("boxplot")
data = np.random.normal(size=(10, 4))
label = ['A', 'B', 'C', 'D']
# boxplotlib via Matplotlib
plt.boxplot(data, labels=label)
plt.show()
# boxplotlib via Seaborn
df = pd.DataFrame(data, columns=label)
sns.boxplot(data=df)
plt.show()

base.chapter("pie")
nums = [25, 37, 33, 37, 6]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Other']
# pie via Matplotlib
plt.pie(x=nums, labels=labels)
plt.show()

base.chapter("heat map")
flights = sns.load_dataset("flights")
data=flights.pivot('year', 'month', 'passengers')
# heat map via seaborn
sns.heatmap(data)
plt.show()


base.chapter("二元分布")
tips = sns.load_dataset("tips")
print(tips.head(10))
# 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()


if __name__ == "__main__":
    pass
