#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 下午2:32

from matplotlib import pyplot
import numpy

# 从-20到20，元素数为10的等差数列
x = numpy.linspace(-20, 20, 10)

y = x**3+2*x**2+6*x+5

pyplot.plot(x,y,marker="o")
pyplot.show()

if __name__ == "__main__":
    pass