#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/23 1:19

import numpy as np

scoretype = np.dtype({
    "names": ["name", 'chinese', 'english', 'math'],
    "formats": ["S32", 'i', 'i', 'i']
})
scores = np.array([
    ("zhangfei", 66, 65, 30),
    ("guanyu", 95, 85, 98),
    ("zhaoyun", 93, 92, 96),
    ("huangzhou", 90, 88, 77),
    ("dianwei", 80, 90, 90),
], dtype=scoretype)

# avg, max, min, variance, std
for subject in ["chinese", "english", "math"]:
    print("%s:"%(subject,))
    print("\tmax:%d" % (np.max(scores[:][subject], )))
    print("\tmin:%d" % (np.min(scores[:][subject], )))
    print("\tavg:%d" % (np.mean(scores[:][subject], )))
    print("\tvariance:%d" % (np.var(scores[:][subject], )))
    print("\tstd:%d" % (np.std(scores[:][subject], )))

print("\npaiming:")
for person in sorted(scores, key=lambda x:x[1]+x[2]+x[3], reverse=True):
    print(person["name"], person[1]+person[2]+person[3])