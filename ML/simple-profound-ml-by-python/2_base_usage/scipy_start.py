#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2018/10/1 上午10:23

import numpy as np
from scipy import sparse

# 用numpy的eye函数生成一个6行6列的对角矩阵
# 矩阵中对角线上的元素数值是1，其余都是0
matrix = np.eye(6)

# 把np数组转化为CSR格式的Scipy稀疏矩阵(sparse matrix)
# sparse函数只存储非0元素
# sparse 计算空置矩阵的东东
# csr_matrix: Compressed Sparse Row Matrix
sparse_matrix = sparse.csr_matrix(matrix)

print("对角矩阵：\n{}".format(matrix))
print("\nsparse存储的矩阵：\n{}".format(sparse_matrix))

if __name__ == "__main__":
    pass
