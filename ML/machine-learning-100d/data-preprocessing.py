#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : GaoJiasheng
# Date : 2018/9/23 上午9:48

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/gavin/work/machine-learning-100D'])

# Importing the libraries
import numpy as np
import pandas as pd

# Importing dataset
dataset = pd.read_csv('./datasets/Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Handling the missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])

# creating a dummy variable
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

# splitting the datasets into traning sets and Test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_tran, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

if __name__ == "__main__":
    print X_train
    print X_test
