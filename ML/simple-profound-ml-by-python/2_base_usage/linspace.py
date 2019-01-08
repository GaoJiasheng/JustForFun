#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/2 下午12:54

import numpy
import matplotlib.pyplot as pyplot

N = 8
y = numpy.zeros(N)
x1 = numpy.linspace(0, 10, N, endpoint=True)
x2 = numpy.linspace(0, 10, N, endpoint=False)

pyplot.plot(x1, y, 'o')
pyplot.plot(x2, y+0.5, 'o')
pyplot.ylim([-0.5, 1])
pyplot.show()

if __name__ == "__main__":
    pass