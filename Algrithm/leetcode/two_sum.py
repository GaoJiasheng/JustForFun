#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2019/4/15 5:23 PM

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {}
        for i,val  in enumerate(nums):
            if val not in idx:
                idx[val] = []
            idx[val].append(i)
        for i, val in enumerate(nums):
            if target-val in idx and target-val != val:
                return i, idx[target-val][0]
            if target-val == val and len(idx[val]) > 1:
                return i, idx[val][1]
        return -1, -1


if __name__ == "__main__":
    print Solution().twoSum([3, 3], 6)
