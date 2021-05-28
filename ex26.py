# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:41:34 2021

@author: lee
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_n = len(nums)
        i = 0
        while i < len_n-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                len_n -= 1
            else:
                i += 1
        return len_n
            