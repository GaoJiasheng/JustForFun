#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 16/12/19 10:26 PM

import pandas as pd

"""
1 - 开始了解你的数据
探索Chipotle快餐数据
-- 将数据集存入一个名为chipo的数据框内
-- 查看前10行内容
-- 数据集中有多少个列(columns)？
-- 打印出全部的列名称
-- 数据集的索引是怎样的？
-- 被下单数最多商品(item)是什么?
-- 在item_name这一列中，一共有多少种商品被下单？
-- 在choice_description中，下单次数最多的商品是什么？
-- 一共有多少商品被下单？
-- 将item_price转换为浮点数
-- 在该数据集对应的时期内，收入(revenue)是多少？
-- 在该数据集对应的时期内，一共有多少订单？
-- 每一单(order)对应的平均总价是多少？
"""

def understand_data():
    chipo = pd.read_csv('./data/chipotle.tsv', sep='\t')
    print(1, chipo.head(10))
    print(2, chipo.shape[1])
    print(3, chipo.columns)
    print(4, chipo.index)
    # 下单数最多的商品是什么
    print(5, chipo[['item_name', 'quantity']].groupby(by=['item_name']).sum().sort_values(by=['quantity'], ascending=False))
    # Dataframe拿一列
    print(5, chipo.item_name)
    # 在item_name这一列中，有多少种商品被下单
    print(6, len(chipo[['item_name']].groupby(by=['item_name'])))
    print(6, chipo.item_name.nunique()) #去重
    print(6, chipo.item_name.count()) #不去重
    # 下单次数最多的商品
    print(7, chipo[['choice_description', 'quantity']].groupby(by=['choice_description']).count().sort_values(by='quantity', ascending=False).head())
    print(7, chipo['choice_description'].value_counts().head())
    # 一共有多少商品被下单
    print(8, chipo['quantity'].sum())
    print(8, chipo.quantity.sum()) #出来的是series
    print(8, chipo[['quantity']].sum().head()) #出来的是dataframe
    # 将item_price转换为浮点数
    chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
    print(9, chipo)
    # 总收入是多少
    print(10, (chipo['item_price']*chipo['quantity']).sum())
    # 一共有多少订单
    print(11, chipo.order_id.nunique())
    # 每一单order对应的平均总价是多少
    chipo['item_price_sum'] = chipo['item_price'] * chipo['quantity']
    print(12, chipo[['order_id', 'item_price_sum']].groupby(by='order_id').mean())

"""
-- 将数据集命名为euro12
-- 只选取 Goals 这一列
-- 有多少球队参与了2012欧洲杯？
-- 该数据集中一共有多少列(columns)?
-- 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
-- 对数据框discipline按照先Red Cards再Yellow Cards进行排序
-- 计算每个球队拿到的黄牌数的平均值
-- 找到进球数Goals超过6的球队数据
-- 选取以字母G开头的球队数据
-- 选取前7列
-- 选取除了最后3列之外的全部列
-- 找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
"""
def data_filter_and_sort():
    euro12 = pd.read_csv('./data/Euro2012.csv', sep=',')
    print(1, euro12['Goals'])
    print(1, euro12.Goals)
    # 共多少只球队
    print(2, euro12[['Team']].nunique())
    print(2, euro12.Team.nunique())
    # 共多少列
    print(3, len(euro12.columns))
    print(3, euro12.shape[1])
    # 将Team， Yellow Cards， Red Cards存为一个discipline的数据框
    discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
    print(4, discipline)
    # 将discipline按照Red Cards和Yellow Cards排序
    discipline = discipline.sort_values(by=['Yellow Cards', 'Red Cards'], ascending=False)
    print(5, discipline)
    # 计算每个队拿到的黄牌数的平均值
    print(6, discipline['Yellow Cards'].mean())
    #找到进球数Goals超过6的球队数据
    print(7, euro12[euro12.Goals>6])
    #选取以字母G开头的球队数据
    print(8, euro12[euro12.Team.str.startswith('G')])
    #选取前7列
    print(9, euro12.iloc[:, 0:7])
    #取除了最后3列之外的全部列
    print(10, euro12.iloc[:, 0:-3])
    #找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
    print(11, euro12.loc[euro12['Team'].isin(['England','Italy','Russia']), ['Team','Shooting Accuracy']])
    # loc：通过行列标签索引数据
    # iloc：通过行列号索引行数据
    # ix：通过行标签或行号索引数据（基于loc和iloc的混合）

"""
-- 将数据框命名为drinks
-- 哪个大陆(continent)平均消耗的啤酒(beer)更多？
-- 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
-- 打印出每个大陆每种酒类别的消耗平均值
-- 打印出每个大陆每种酒类别的消耗中位数
-- 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
"""
def grouping():
    #将数据框命名为drinks
    drinks = pd.read_csv('./data/drinks.csv')
    print(1, drinks)
    # 哪个大陆(continent)平均消耗的啤酒(beer)更多？
    print(2, drinks[['continent', 'beer_servings']].groupby(by='continent').sum().sort_values(by='beer_servings', ascending=False))
    # 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
    print(3, drinks[['continent', 'wine_servings']].groupby(by='continent').describe())
    # 打印出每个大陆每种酒类别的消耗平均值
    print(4, drinks[['continent', 'wine_servings', 'beer_servings', 'spirit_servings']].groupby(by='continent').mean())
    # 打印出每个大陆每种酒类别的消耗中位数
    print(5, drinks.groupby(by='continent').median())
    # 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
    print(6, drinks[['continent', 'spirit_servings']].groupby(by='continent').describe())

"""
-- 将数据框命名为crime
-- 每一列(column)的数据类型是什么样的？
-- 将Year的数据类型转换为 datetime64
-- 将列Year设置为数据框的索引
-- 删除名为Total的列
-- 按照Year（每十年）对数据框进行分组并求和
-- 何时是美国历史上生存最危险的年代？
"""
def apply():
    # 将数据框命名为crime
    crime = pd.read_csv('./data/US_Crime_Rates_1960_2014.csv')
    print(1, crime)
    # 每一列(column) 的数据类型是什么样的？
    print(2, crime.info())
    # 将Year的数据类型转换为 datetime64
    crime.Year = pd.to_datetime(crime.Year, format='%Y')
    print(3, crime.Year)

    # 将列Year设置为数据框的索引
    crime = crime.set_index('Year', drop=True)
    print(4, crime)
    # 删除名为Total的列
    del crime['Total']
    print(5, crime)
    # 按照Year（每十年）对数据框进行分组并求和
    crimes = crime.resample('10AS').sum()
    print(6, crimes)
    # 何时是美国历史上生存最危险的年代？
    print(7, crime.idxmax())

"""
-- 创建DataFrame
-- 将上述的DataFrame分别命名为data1, data2, data3
-- 将data1和data2两个数据框按照行的维度进行合并，命名为all_data
-- 将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
-- 打印data3
-- 按照subject_id的值对all_data和data3作合并
-- 对data1和data2按照subject_id作连接
-- 找到 data1 和 data2 合并之后的所有匹配结果
"""
def merge():
    # 创建DataFrame
    raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

    raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

    raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
    # 将上述的DataFrame分别命名为data1, data2, data3
    data1 = pd.DataFrame(raw_data_1)
    data2 = pd.DataFrame(raw_data_2)
    data3 = pd.DataFrame(raw_data_3)
    # 将data1和data2两个数据框按照行的维度进行合并，命名为all_data
    all_data = pd.concat([data1, data2], axis=1)
    print(1, all_data)
    # 将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
    all_data_col = pd.concat([data1, data2], axis=0)
    print(2, all_data_col)
    # 打印data3
    print(3, data3)
    # 按照subject_id的值对all_data和data3作合并
    print(4, pd.merge(all_data_col, data3, on='subject_id'))
    # 对data1和data2按照subject_id作连接
    print(5, pd.merge(data1, data2, on='subject_id', how='left'))
    # 找到data1和data2合并之后的所有匹配结果
    print(6, pd.merge(data1, data2, on='subject_id', how='outer'))

    ## concat是用来拼接的
    ## merge是用来做连表的

"""
-- 将数据作存储并且设置前三列为合适的索引
-- 2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
-- 将日期设为索引，注意数据类型，应该是datetime64[ns]
-- 对应每一个location，一共有多少数据值缺失
-- 对应每一个location，一共有多少完整的数据值
-- 对于全体数据，计算风速的平均值
-- 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
-- 创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差
-- 对于每一个location，计算一月份的平均风速
-- 对于数据记录按照年为频率取样
-- 对于数据记录按照月为频率取样
"""

import datetime
def statistics():
    # 将数据作存储并且设置前三列为合适的索引
    df = pd.read_csv('./data/wind.csv', sep='\s+', parse_dates=[[0, 1, 2]])
    print(1, df)
    # 2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
    df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(lambda x: datetime.date(x.year-100 if x.year > 1999 else x.year, x.month, x.day))
    print(2, df)
    # 将日期设为索引，注意数据类型，应该是datetime64[ns]
    df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'])
    df = df.set_index('Yr_Mo_Dy')
    print(3, df)
    # 对应每一个location，一共有多少数据值缺失
    print(4, df.isnull().sum())
    # 对应每一个location，一共有多少完整的数据值
    print(5, df.shape[1]-df.isnull().sum())
    # 对于全体数据，计算风速的平均值
    print(6, df.mean().mean())
    # 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
    loc_stats = df.describe().T[['min','max','mean','std']]
    print(7, loc_stats)
    loc_stats = pd.DataFrame()
    loc_stats['min'] = df.min()
    loc_stats['max'] = df.max()
    loc_stats['std'] = df.std()
    loc_stats['mean'] = df.mean()
    print(7, loc_stats)
    # 创建一个名为day_stats的数据框去计算并存储所有location所有天的风速最小值，最大值，平均值和标准差
    day_stats = pd.DataFrame()
    day_stats['min'] = df.min(axis=1)
    day_stats['max'] = df.max(axis=1)
    day_stats['mean'] = df.mean(axis=1)
    day_stats['std'] = df.min(axis=1)
    print(8, day_stats)

    # 对于每一个location，计算一月份的平均风速
    df['date'] = df.index
    df['year'] = df['date'].apply(lambda df: df.year)
    df['month'] = df['date'].apply(lambda df: df.month)
    df['day'] = df['date'].apply(lambda df: df.day)
    january_winds = df.query('month == 1')  # 等同于df[df.month==1]
    print(9, january_winds.loc[:, 'RPT':'MAL'].mean())
    # 对于数据记录按照年为频率取样
    print(10, df.query('month == 1 and day == 1'))
    # 对于数据记录按照月为频率取样
    print(11, df.query('day == 1'))

# visualisation
"""
-- 将数据框命名为titanic
-- 将PassengerId设置为索引
-- 绘制一个展示男女乘客比例的扇形图
-- 绘制一个展示船票Fare, 与乘客年龄和性别的散点图
-- 有多少人生还？
-- 绘制一个展示船票价格的直方图
"""
def visualisation():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    # 将数据框命名为titanic
    titanic = pd.read_csv('./data/train.csv')
    # 将PassengerId设置为索引
    titanic = titanic.set_index('PassengerId')
    print(1, titanic)
    # 绘制一个展示男女乘客比例的扇形图
    #Male = titanic[['Sex']].query('Sex == "male"').count()
    #Female = titanic[['Sex']].query('Sex == "female"').count()
    Male = (titanic.Sex == 'male').sum()
    Female = (titanic.Sex == 'female').sum()
    proportions = [Male, Female]
    plt.pie(proportions, labels=['Male', 'Female'], shadow=True, autopct='%1.1f%%', startangle=90,explode=(0.15, 0))
    plt.axis('equal')
    plt.title('Sex Proportion')
    plt.tight_layout()

    # 绘制一个展示船票Fare, 与乘客年龄和性别的散点图
    lm = sns.lmplot(x='Age', y='Fare', data=titanic, hue='Sex', fit_reg=False)
    lm.set(title='Fare x Age')
    axes = lm.axes # 坐标取值范围
    axes[0,0].set_ylim(-5, )
    axes[0,0].set_xlim(-5, 85)
    plt.show()

    # 有多少人生还？
    print(titanic.Survived.sum())

    # 绘制一个展示船票价格的直方图
    df = titanic.Fare.sort_values(ascending=False)
    plt.hist(df, bins=(np.arange(0, 600, 10)))
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.title('Fare Payed Histrogram')

    plt.show()


if __name__ == "__main__":
    visualisation()
