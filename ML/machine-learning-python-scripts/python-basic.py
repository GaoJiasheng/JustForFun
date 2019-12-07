#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng For Yuchao
#Date : 3/12/19 7:23 PM

# 基础的几种数据类型,简单打印打印看看,知道怎么用就行
def types_of_py():
    num_int = 100
    num_float = 100.0
    name = "Yuchao Zhao"

    # 先看看基础类型
    print num_int, type(num_int)
    print num_float, type(num_float)
    print name, type(name)

# 其实Python很简单的，很多的东西都是所见即所得
# List类型，其实就是个列表, 同样元素的聚合，一般的形式是 [1,2,3,4]
# 因为是一个列表，所以会有序号:第一个元素，序号是0；最后一个元素，序号是len(array)-1
def list_type():
    # a是一个列表
    a = [1,2,3,4,5]

    # 我想拿a的一些元素的方法
    print "Print the first and the last value of List:"
    print a[0], a[len(a)-1] # 拿列表的第一个元素和最后一个元素

    # 遍历列表
    print "Print the List by loop:"
    for i in a:
        print i,

    # 拿列表中的一段
    print "\nPrint the 2nd~3th element of List:"
    # 索引1代表第二个，索引3代表第四个元素，因此写[1:3]其实是一个前闭后开的结构
    print a[1:3] # [1:3]其实拿的是a[1],a[2]两个元素

    # Python骚操作(面试可以加分)
    # 打印list中每个元素的(2x^2+8x-16)
    print "Print the 2x^2+8x-16 of every element of List:"
    for j in [2*i*i+8*i-16 for i in a]:
        print j,

# dict是字典类型，其实也很简单，就是一种k-v的对应方式，比如{"name":"Yuchao", "sex":"female"}
# name: yuchao
# sex: female
# 你看，一个对应一个，这种k-v的形式，在Python中叫dict类型
def dict_type():
    person = {"name":"Yuchao", "sex":"female"}
    # 此时我想要拿到你的name
    print "Print the name of Yuchao:"
    print person["name"]

    # 拿到dict的所有的key
    print "Print the all keys of dict:"
    print person.keys()

    # 遍历dict
    print "Print the dict by loop:"
    for k in person:
        print "\t", k, " -- ",person[k]
    print

    # dict的骚操作与list类似
    print "Print the every value add &&:"
    # for i in 的后面其实就是一个slice
    # [k for k in [1,2,3]]这个表达式，你仔细看看，其实就是一个for循环的变体
    for i in [k+":"+"&"+person[k]+"&" for k in person]:
        print i

if __name__ == "__main__":
    """有点类似C语言的main函数
    """
    #types_of_py()
    #list_type()
    dict_type()
