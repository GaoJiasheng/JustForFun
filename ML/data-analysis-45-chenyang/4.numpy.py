#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/21 19:13

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import base
import numpy as np

# ndarry object
base.chapter("ndarry object")
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

# structure object
base.chapter("structure object")
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})
peoples = np.array([
    ("ZhangFei", 32, 75, 100, 90),
    ("GuanYu", 24, 85, 96, 88.5),
    ("ZhaoYun", 28, 85, 92, 96.5),
    ("HuangZhong", 29, 65, 85, 100)
], dtype=persontype)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']

print(ages, np.mean(ages))
print(chineses, np.mean(chineses))
print(maths, np.mean(maths))
print(englishs, np.mean(englishs))

# universal function
base.chapter("universal function")
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))

# maximum & minimum
base.chapter("max&min function")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))
print(np.amax(a))
print(np.amin(a, 0))
print(np.amin(a, 1))

# percentile
base.chapter("percentile")
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

# median
base.chapter("median")
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

# median
base.chapter("mean")
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# ptp
base.chapter("ptp")
print(np.ptp(a))
print(np.ptp(a, axis=0))
print(np.ptp(a, axis=1))

# average
base.chapter("average")
a = np.array([1, 2, 3, 4])
wts = np.array([4, 3, 2, 1])
print(np.average(a))
print(np.average(a, weights=wts))

# std & variance
base.chapter("std & var")
a = np.array([1, 2, 3, 4])
print(np.std(a), a.std())
print(np.var(a), a.var())

# sort
base.chapter("sort")
a = np.array([[3,4,2], [2, 4, 1]])
print(np.sort(a))
print(np.sort(a, axis=None, kind='quicksort', order=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))


if __name__ == "__main__":
    pass