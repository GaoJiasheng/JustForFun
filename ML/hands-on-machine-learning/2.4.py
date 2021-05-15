#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 16/4/21 5:21 下午

import os
import tarfile
import urllib
import pandas
import numpy
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + ("datasets/housing/housing.tgz")

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pandas.read_csv(csv_path)

if __name__ == "__main__":
    fetch_housing_data()
    housing = load_housing_data()
    housing['income_cat'] = pandas.cut(housing['median_income'],
                                   bins=[0., 1.5, 3.0, 4.5, 6., numpy.inf],
                                   labels=[1, 2, 3, 4, 5])

    from sklearn.model_selection import StratifiedShuffleSplit
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    housing = strat_train_set.copy()

    # show longitude & latitude
    # 经纬度 + 人口分布热力图
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1,
                 s=housing['population']/100, label="population", figsize=(10, 7),
                 c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
    # 收入中位数和房屋价格中位数的相关性
    housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
    plt.show()


    # 寻找相关性 - corr
    corr_matrix = housing.corr()
    #print(corr_matrix['median_house_value'].sort_values(ascending=False))

    # 寻找相关性 - pandas.plotting.scatter_matrix
    from pandas.plotting import scatter_matrix
    attributes=['median_house_value', "median_income", "total_rooms", "housing_median_age"]
    a = scatter_matrix(housing[attributes], figsize=(12,8))

    # 数据清理
    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set['median_house_value'].copy()

    housing.dropna(subset=["total_bedrooms"])
    housing.drop("total_bedrooms", axis=1)
    median=housing["total_bedrooms"].median()
    housing["total_bedrooms"].fillna(median, inplace=True)

    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    housing_tr = pandas.DataFrame(X, columns=housing_num.columns,
                              index=housing_num.index)

    # 处理文本和分类属性
    housing_cat = housing[["ocean_proximity"]]
    housing_cat.head(10)

    # 从文本转到数字
    from sklearn.preprocessing import OrdinalEncoder
    ordinal_encoder = OrdinalEncoder()
    housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
    housing_cat_encoded[:10]

    from sklearn.preprocessing import OneHotEncoder
    cat_encoder = OneHotEncoder()
    housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
    print(housing_cat_1hot)








