#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/23 11:18

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import base

import pandas as pd
from pandas import Series, DataFrame

# Series
base.chapter("pandas series")
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# x3 = x2
d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print("x1:\n", x1)
print("x2:\n", x2)
print("x3:\n", x3)

# DataFrame
base.chapter("pandas datafram")
data = {
    "chinese": [66, 95, 93, 90, 80],
    "english": [65, 85, 92, 88, 90],
    "math": [30, 98, 96, 77, 90],
}

df1 = DataFrame(data)
df2 = DataFrame(data, index=['Zhangfei', 'Guanyu', 'Zhaoyun', 'HuangZhong', 'Dianwei'])
print("df1:\n", df1)
print("df2:\n", df2)

# pandas data import & export
# base.chapter('Data import and export')
# score = DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data.xlsx')

# data drop by column or index
base.chapter('data drop by column & index')
df3 = df2.drop(columns=['chinese'])
df4 = df3.drop(index=['Zhangfei'])
print("df3:\n", df3)
print("df4:\n", df4)

# rename columns
base.chapter('rename columns')
# same as df2.rename(columns={'chinese':'Yuwen', 'english':'Yingyu'}, inplace=True)
df3 = df2.rename(columns={'chinese':'Yuwen', 'english':'Yingyu'}, inplace=False)
print("df2:\n", df3)

# drop duplicates
base.chapter('drop duplicate')
df1 = df1.drop_duplicates()

# space character strip
base.chapter('space character strip')
# strip & lstrip & rstrip
#df2['chinese'] = df2['chinese'].map(str.strip)

# upper & lower & title
df2.columns = df2.columns.str.upper()
df2.columns = df2.columns.str.lower()

# find null
data = {
    "chinese": [66, 95, 93, 90, 80],
    "english": [65, None, 92, 88, 90],
    "math": [30, 98, 96, None, 90],
}

df5 = DataFrame(data, index=['Zhangfei', 'Guanyu', 'Zhaoyun', 'HuangZhong', 'Dianwei'])
print(df5.isnull())
print(df5.isnull().any())

# apply by column
# df2['name'] = df2['name'].apply(str.upper)

def double_df(x):
    return x*2

df2['chinese'] = df2['chinese'].apply(double_df)


# apply by datafram
def plus(df, n, m):
    df['new1'] = (df['chinese']+df['english']) * m
    df['new2'] = (df['chinese']+df['english']) * n
    return df

df2 = df2.apply(plus, axis=1, args=(2, 3, ))

# common statistics function
base.chapter("pandas common statistics function")
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
print("\ndf1:\n", df1)
print("\ndf1.describe:\n", df1.describe())
print("\ndf1.argmin():\n", type(df1['data1']), df1['data1'].argmin())
print("\ndf1.argmax():\n", df1['data1'].argmax())

# merge dataframe
base.chapter("dataframe merge")
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
print("\ndf1:", df1)
print("\ndf2:", df2)

df3 = pd.merge(df1, df2, on='name')
print("\ndf3:", df3)
df4 = pd.merge(df1, df2, on='name', how='inner')
print("\ndf4:", df4)
df5 = pd.merge(df1, df2, on='name', how='left')
print("\ndf5:", df5)
df6 = pd.merge(df1, df2, on='name', how='right')
print("\ndf6:", df6)
df7 = pd.merge(df1, df2, on='name', how='outer')
print("\ndf7:", df7)


# operate Dataframe by SQL language
base.chapter("operate dataframe by SQL language")
from pandasql import sqldf, load_meat, load_births
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))








