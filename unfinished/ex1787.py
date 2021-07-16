# -*- coding: utf-8 -*-
"""
Created on Tue May 25 08:28:03 2021

@author: 95348
"""

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        dict_k = [dict() for _ in range(k)]
        for i in range(k):
            for num in nums[i::k]:
                if num not in dict_k[i]:
                    dict_k[i][num] = 1
                else:
                    dict_k[i][num] += 1
        res = len_n 
        for i in range(0, len_n, k):
            numk = nums[i:i+k]
            print('numk: ', numk)
        