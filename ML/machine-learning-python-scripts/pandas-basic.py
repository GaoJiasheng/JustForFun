#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 4/12/19 11:00 PM

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def series_creation():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    print(s[2])

def creation():
    # 用带有日期时间索引的数组来创建DataFrame
    dates = pd.date_range('20130101', periods=6) #先创建一个时间的序列(一维的)
    df = pd.DataFrame(1, index=dates, columns=list('ABCD'))
    # print df

    # 传递可以转化为类似Series的diczt对象来创建DataFrame
    # 可以理解为穿了多个列进去，每个列都是一个list，可以支持多种格式的list
    df2 = pd.DataFrame({
        'A':1.,     # 如果是一个值，则默认用这个值构建一个同样value的list
        'B':pd.Timestamp('20130102'),       # 这是pandas里的时间, 默认传进去，也会构建一个序列
        'C':pd.Series(1, index=list(range(4)), dtype='float32'),    # 这是pandas里边的序列类型
        'D':np.array([1,2,2,4], dtype='int32'), # 这是numpy里的序列类型
        'E':pd.Categorical(["test", "train", "test", "hahaah"]),  # 这也是pandas里的一种序列类型
        'F':'foo'     # 这是一个值，跟上面的单值一样
    })
    return df2

def assignment():
    df2 = pd.DataFrame({
        "A":[2,4,6,8],
        "B":[9,10,11,12]
    })
    # 我们先创建一个Series,别忘了，这是一个线性的数据结构
    # 内容是1，2，3，4，5，6，索引用的是一个日期2019年11月的几天
    s1 = pd.Series([1,2,3,4], index=pd.date_range('20191102', periods=4))
    print("----------print Series s1-------------")
    print(s1)
    # 把s1这个序列，赋值给df2的一个列
    print("----------print DataForm after added by s1-------------")
    df2.loc[:, "S"] = s1.to_numpy()
    print(df2)
    # 通过位置赋值，修改第3行第3列的数据为10000
    print("----------print Series s1 after by edit value-------------")
    df2.iat[2,2] = 10000
    print(df2)
    # 如果df2中元素大于0，则将符号改成负的
    print("----------print Series s1 after value calculate-------------")
    df2[df2>0] = -df2
    print(df2)

def usage():
    # 每个dataframe的列，都可以有自己的类型
    df2 = creation()
    for k in df2:
        print("----------")
        print("key:", k) # k就是ABCD，就是列名
        print(df2[k])   # 可以仔细看看，这里边有个dtype，就是我们定义时设定的数据类型

    # 好了，现在已经有了一个dataframe的元素了，我们开始看看里边的东西
    print("---------dataframe head--------")
    print(df2.head(3)) #查看头三行
    print("---------d ataframe tail--------")
    print(df2.tail(3))  #查看尾三行
    print("---------dataframe index(行号)--------")
    print(df2.index)
    print("---------dataframe columns(列名)--------")
    print(df2.columns)
    print("---------dataframe convert to numpy(给出一个底层的numpy对象来针对numpy进行计算)--------")
    print(df2.to_numpy()) #可以看到打出来的，也是一个二维数组，只是更加底层，用的是python原生的list类型
    print("---------dataframe describe(快速统计摘要)--------")
    print(df2.describe()) #可以快速给出每一列的摘要，算一下count、avg、mean之类的
    print("---------dataframe print describe(行列转置)--------")
    print(df2.T)
    print("---------dataframe print sort by column(列排序)--------")
    print(df2.sort_index(axis=1, ascending=False)) # 按列名儿，降序排序
    print("---------dataframe print sort by value(值排序)--------")
    print(df2.sort_values(by="E")) # 按第E列的值，排序

def selection():
    # 我们还用那个ABCD的二维表格
    df2 = creation()
    # 使用下标的方式来获取列
    # 获取df2这个dataframe的第A列
    print("---------dataframe print Column A--------")
    print(df2['A'])
    # 当获取行的时候，要使用切片的方式来获取行
    # 获取df2这个dataframe的第一行
    print("---------dataframe print line 1--------")
    print(df2[0:1])
    # 获取df2这个dataframe的第2,3,4行
    print("---------dataframe print line 2,3,4--------")
    print(df2[2:5])
    # 获取df2这个dataframe的所有行
    print("---------dataframe print all line--------")
    print(df2[:])
    # 获取df2这个datafram的A, B两列的第2，3行
    print("---------dataframe print line 2,3 of Column A,B--------")
    print(df2.loc[2:4, ['A', 'B']])
    # 按行列的位置来选择数据
    print("---------dataframe print line 3--------")
    print(df2.iloc[3])
    print("---------dataframe print line(1~2) column(2~4)--------")
    print(df2.iloc[1:3, 2:5])
    print("---------dataframe print line(1~2) of all column--------")
    print(df2.iloc[1:3, :])
    print("---------dataframe print all lines of column(2~4)--------")
    print(df2.iloc[:, 2:5])
    print("---------dataframe print a point value: second line, second column--------")
    print(df2.iloc[1, 1])
    # 按照值的条件来进行筛选 # 打印D这列>=3的所有行
    print("---------dataframe print lines whose column D >=3 --------")
    print(df2[df2.D >= 3])
    # 打印D这列在某个集合内的所有行
    print("---------dataframe print selection by value--------")
    # 增加一列K
    df2['K'] = ['one', 'two', 'three', 'four']
    # 打印K这一列，值为two和four的行
    print(df2[df2['K'].isin(['two', 'four'])])

def data_nan():
    # 这个主要讲NaN这个东西，这个东西其实是Not a Number的缩写，代表不是一个数字
    # pandas里的非数字，都用这个东西
    # 第四个元素，即s[3],是nan
    s = pd.Series([1,3,5,np.nan, 6,8])
    print('---------print series contains a nan----------')
    print(s)
    print('---------print DataFrame contains a nan----------')
    df = pd.DataFrame({
        'A':1.0,
        'B':s,
        'C':np.array([1,2,3,4,5,6])
    })
    print(df) #此时，第B列的第4行，值是NaN，打印出来可以看到
    print('---------print DataFrame filled nan----------')
    print(df.fillna(value=10000)) #注意，这些改变并不会真正操作df，而是生成一个新的DataFrame,真正的df并没有被改动
    print('---------print DataFrame drop nan----------')
    print(df.dropna(how='any')) # 这样就会把带有NaN的行，也就是第三行删掉
    print('---------print if DataFrame value is nan----------')
    print(pd.isna(df))

def calculate():
    s = pd.Series([1,3,5,np.nan, 6,8])
    df = pd.DataFrame({
        'A':1.0,
        'B':s,
        'C':np.array([1,2,3,4,5,6])
    })
    print('---------print basic dataframe----------')
    print(df)
    #求个平均
    print('---------print dataframe average by column----------')
    print(df.mean())
    print('---------print dataframe average by row----------')
    print(df.mean(1))
    print('---------print dataframe calc by apply function on column----------')
    print(df.apply(lambda x:x.max() - x.min()))
    # 字符串方法
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print('---------print series str func----------')
    print(s.str.lower())

def merge():
    # 创建一个随机的dataframe
    df = pd.DataFrame(np.random.randn(10, 4))
    # 按行分解和连接concat
    pieces = [df[:3], df[3:7], df[7:]] # 分解为多组
    #print(pd.concat(pieces)) #再给他接起来
    # 按列链接join
    left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
    print(left)
    print(right)
    print(pd.merge(left, right, on='key'))
    # 追加行append
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    s = df.iloc[3]
    print(df.append(s, ignore_index=True))

def grouping():
    # 分割、应用、组合
    df = creation()
    # 根据D列分组之后，求其他列的和
    print(df.groupby('D').sum())
    # 多列分组
    print(df.groupby(['D', 'E']).sum())

def stack():
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                        'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                        'one', 'two', 'one', 'two']]))

    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    # 把A和B两列，压成索引，最终展现一个线性的结构
    stacked=df.stack()
    print(stacked)
    # unstack
    print(stacked.unstack().unstack())

def pivot():
    df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                       'B': ['A', 'B', 'C'] * 4,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D': np.random.randn(12),
                       'E': np.random.randn(12)})
    print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

def time_series():
    rng = pd.date_range('1/1/2012', periods=1000, freq='S')
    ts = pd.Series(np.random.randint(0, 1000, len(rng)), index=rng)
    # resample
    print(ts.resample('5Min').sum())

    # timezone
    rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print(ts)
    ts_utc=ts.tz_localize('UTC')
    print(ts_utc)
    # convert to other time zone
    print(ts_utc.tz_convert('US/Eastern'))

    # timestamp <--> period
    rng = pd.date_range('1/1/2012', periods=5, freq='M')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    period =ts.to_period()
    print(period)
    print(period.to_timestamp())

def categoricals():
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                       "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    # set new grade column:w
    # convert the raw column to categoricals
    df['grade'] = df["raw_grade"].astype("category")
    print(df['grade'])
    # reset the value by meaning value
    df['grade'].cat.categories = ["very good", 'good', 'very bad']
    print(df['grade'].cat.categories)
    # empty will be one special key when use categoricals
    print(df.groupby("grade").count())

def visualisation():
    ts = pd.Series(np.random.randn(1000),
                   index = pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()


def read_excel(path="~/Desktop/students.xlsx"):
    df1 = pd.read_excel(path, sheet_name=0, header=0)
    print(df1)

def write_excel(path="~/Desktop/students.xlsx"):
    df1 = pd.read_excel(path, sheet_name=0, header=0, index_col=[0,1,2,])
    df1.to_excel(excel_writer=path, sheet_name='写入的sheet', encoding='utf-8')

def resample_learning():
    df = pd.read_csv("~/Desktop/apple.csv", parse_dates=["date"], index_col="date")
    print(df[:10])
    # parse_dates：boolean or list of ints or names or list of lists or dict, default False. 这个参数指定对CSV文件中日期序列的处理方式：
    # 默认为False，原样加载，不解析日期时间，
    # 可以为True，尝试解析日期索引，
    # 可以为数字或 names 的列表，解析指定的列为时间序列，
    # 可以为以列表为元素的列表，解析每个子列表中的字段组合为时间序列，
    # 可以为值为列表的字典，解析每个列表中的字段组合为时间序列，并命名为字典中对应的键值；
    # Printing the first 10 rows of dataframe

    # 要求按月统计苹果股票的close价格的平均值
    # 解决方法如下：
    monthly_resampled_data = df.close.resample('M').mean()
    #print(monthly_resampled_data)
    weekly_resampled_data = df.close.resample('W').mean()
    #print(weekly_resampled_data)
    Quarterly_resampled_data = df.open.resample('Q').mean()
    #print(Quarterly_resampled_data)
    ser = pd.Series([1, 10, 3, np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
    #print(ser)
    # 重新按照天来resample，并填充控制与Nan值，产生如下输出
    print('----------------------------')
    print(ser.resample('W').ffill())
    # 上一句没看懂，为何会输出那样的结果

if __name__ == "__main__":
    merge()


