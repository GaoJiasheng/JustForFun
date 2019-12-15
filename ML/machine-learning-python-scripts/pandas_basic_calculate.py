#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 15/12/19 6:36 PM

"""
姓名  语文  英语  数学
0  张飞  66  65  30
1  关羽  95  85  98
2  赵云  93  92  96
3  黄忠  90  88  77
4  典韦  80  90  90

假设一个团队里有 5 名学员，成绩如下表所示。
你可以用 NumPy 统计下这些人在语文、 英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩 排序，得出名次进行成绩输出。
"""

import pandas

def make_data():
    return pandas.DataFrame({
        "姓名":["张飞", "关羽", "赵云", "黄忠", "典韦"],
        "语文":[66, 95, 93, 90, 80],
        "英语":[65, 85, 92, 88, 90],
        "数学":[30, 98, 96, 77, 90]
    }, index=range(5))

if __name__ == "__main__":
    scores = make_data()
    temp = scores[["语文", "英语","数学"]]
    # basic calculation
    scores["平均"] = temp.mean(axis=1)
    scores["总成绩"] = temp.sum(axis=1)
    scores["最小成绩"] = temp.min(axis=1)
    scores["最大成绩"] = temp.max(axis=1)
    scores["方差"] = temp.var(axis=1)
    scores["标准差"] = temp.std(axis=1)
    # sort by total score
    scores = scores.sort_values(by='总成绩', ascending=False)
    # Extra: calculate the all guys total
    course_avg_scores = temp.mean(axis=0)
    course_avg_scores["姓名"]="各科平均分"
    scores = scores.append(course_avg_scores, ignore_index=True)

    print(scores)
