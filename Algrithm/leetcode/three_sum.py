#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author : GaoJiasheng
#Date : 2019/4/15 5:44 PM

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 这个问题要看多少级哈希表，循环多少级,根据数据的量级酌情考虑
        idx = {}
        for i, vi in enumerate(nums):
            for j, vj in enumerate(nums):
                if i < j:
                    sum = vi + vj
                    if sum not in idx:
                        idx[sum] = []
                    idx[sum].append([i, j])

        target = 0
        res = []
        for k, vk in enumerate(nums):
            swp = target - vk
            if swp in idx:
                for combi in idx[swp]:
                    if k not in combi and k < combi[0] and k < combi[1]:
                        res.append(sorted([nums[k], nums[combi[0]], nums[combi[1]]]))
        result = []
        res.sort()
        for li in res:
            if result == []:
                result.append(li)
            if li != result[-1]:
                result.append(li)

        return result



if __name__ == "__main__":
    print Solution().threeSum([1,0,-1,2,-1,-4])
