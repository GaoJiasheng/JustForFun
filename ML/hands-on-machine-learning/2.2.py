#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 16/4/21 12:49 上午

import os
import tarfile
import urllib
import pandas
import numpy

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
    #print(housing.info())
    #print(housing["ocean_proximity"].value_counts())
    #print(housing["longitude"].describe())
    return pandas.read_csv(csv_path)

# view_describe_by_plot(housing, "longitude")
def view_describe_by_plot(df, column):
    import matplotlib.pyplot as plt
    if column == "":
        df.hist()
    else:
        df[column].hist()
    plt.show()

# there is also a function train_test_split in sklearn.model_selection
def split_train_test(data, test_ratio):
    import numpy as np
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def income_cat():
    import matplotlib.pyplot as plt
    housing['income_cat'] = pandas.cut(housing['median_income'],
                                   bins=[0., 1.5, 3.0, 4.5, 6., numpy.inf],
                                       labels=[1, 2, 3, 4, 5])
    housing['income_cat'].hist()
    #housing['median_income'].hist()
    plt.show()

if __name__ == "__main__":
    fetch_housing_data()
    housing = load_housing_data()
    income_cat()

