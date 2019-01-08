#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 下午2:15

import pandas

data = {
    "Name" : ["小于", "小涵", "小渝", "小涵"],
    "City" : ["北京", "上海", "广州", "深圳"],
    "Age":["18", "20", "22", "24"],
    "Height":["162", "161", "164", "166"]
}

data_frame = pandas.DataFrame(data=data)
print(data_frame)

if __name__ == "__main__":
    pass