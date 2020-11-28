#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/28 11:05

from pandas import DataFrame

scores = DataFrame([
    {"chinese": 66, "english": 65, "math": None},
    {"chinese": 95, "english": 85, "math": 98},
    {"chinese": 95, "english": 92, "math": 96},
    {"chinese": 90, "english": 88, "math": 77},
    {"chinese": 80, "english": 90, "math": 90},
    {"chinese": 80, "english": 90, "math": 90}
], index=["Zhangfei", "Guanyu", "Zhaoyun", "Huangzhong", "Dianwei", "Dianwei"])

scores["total"] = scores.sum(axis=1)

print(scores)

if __name__ == "__main__":
    pass