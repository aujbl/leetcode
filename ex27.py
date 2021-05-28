# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:30:23 2021

@author: lee
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_n = len(nums)
        i = 0
        while i < len_n:
            if nums[i] == val:
                nums.pop(i)
                len_n -= 1
            else:
                i += 1
        return len_n