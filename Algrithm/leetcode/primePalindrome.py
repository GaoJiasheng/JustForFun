#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : GaoJiasheng

def primePalindrome(N):
    """
    :type N: int
    :rtype: int
    """
    import string
    num = N
    if N == 1:
        return 2
    if N == 2 or N == 3:
        return N
    while True:
        print "test ", num
        num = num + 1
        # 所有素数一定在6的两侧
        if (num - 1) % 6 != 0 and (num + 1) % 6 != 0:
            continue
        # 所有双数位数的回文除11外,都可以被11整除
        num_str = str(num)
        if len(num_str) % 2 == 0:
            continue
        # 是否回文
        c = 0
        is_huiwen = True
        while c < len(num_str) / 2:
            if num_str[c] != num_str[-c - 1]:
                is_huiwen = False
                break
            c = c + 1
        if is_huiwen == False:
            continue
        # 是否素数
        c = 1
        is_sushu = True
        while c < num ** 0.5 and c+1 < num:
            c = c + 1
            if num % c == 0:
                is_sushu = False
                break
            else:
                continue
        if is_sushu:
            return num

if __name__ == "__main__":
    print primePalindrome(9989900)
