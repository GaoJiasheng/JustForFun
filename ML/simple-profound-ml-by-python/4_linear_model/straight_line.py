#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/2 下午12:04

import numpy as np
import matplotlib.pyplot as pyplot

# 令X为-5到5之间，元素数为100的等差数列
x = np.linspace(-5, 5, 100)

# 输入直线方程
y = 0.5*x + 3
pyplot.plot(x, y, c='orange')
pyplot.title('Straight Line')
pyplot.show()


if __name__ == "__main__":
    pass


