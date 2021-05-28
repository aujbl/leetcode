# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:24:29 2021

@author: lee
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            j = i
            while j < len(nums)-1 and nums[j+1]-nums[j] == 1:
                j += 1
            if i != j:
                result.append(str(start) + '->' + str(nums[j]))
            else:
                result.append(str(start))
            i = j + 1
        return result
        
    
    
