# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:00:14 2021

@author: lee
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_numbers = len(numbers)
        left, right = 0, len_numbers-1
        result = numbers[left] + numbers[right]
        while result != target:
            if result < target:
                left += 1
            else:
                right -= 1
            result = numbers[left] + numbers[right]
        return [left+1, right+1]
        