# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:52:34 2021

@author: lee
"""
from typing import List

#暴力超时
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        res = []
        for xi, mi in queries:
            if nums[0] > mi:
                res.append(-1)
            else:
                j = result = 0
                while j < len(nums) and nums[j] <= mi:
                    result = max(result, xi ^ nums[j])
                    j += 1
                res.append(result)
        return res
                