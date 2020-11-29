#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : Gao Jiasheng
# Date : 2020/11/28 22:59

import pandas

df = pandas.read_excel("11.data_cleansing_data.xlsx")
df = df.rename(columns={0:"no", 1:"name", 2:"age", 3:"weight", 4:"man_chest", 5:"man_hipline", 6:"man_waistline", 7:"man_chest", 8:"man_hipline", 9:"man_waistline"})

# integrality
df = df.dropna(how="all")

age_maxf = df['age'].value_counts().index[0]
df['age'] = df['age'].fillna(age_maxf)

# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)

# 将 lbs转换为 kgs, 2.2lbs=1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
    # 截取从头开始到倒数第三个字符之前，即去掉lbs。
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i,'weight'] = '{}kgs'.format(weight)

# 切分名字，删除源数据列
df[['first_name','last_name']] = df['name'].str.split(expand=True)
df.drop('name', axis=1, inplace=True)

# 删除非 ASCII 字符
df['first_name'] = df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True)
df['last_name'] = df['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True)


# 删除重复数据行
df.drop_duplicates(['first_name','last_name'],inplace=True)
print(df)


if __name__ == "__main__":
    pass
