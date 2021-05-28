# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:48:28 2021

@author: lee
"""
from typing import List

# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         len_n = len(nums)
#         if len_n == 1:
#             return [-1]
#         res = []
#         search = nums[1::]
#         for num in nums:
#             j = 0
#             while j < len_n-1 and num >= search[j]:
#                 j += 1
#             if j < len_n-1 and num < search[j]:
#                 res.append(search[j])
#             else:
#                 res.append(-1)
#             search.pop(0)
#             search.append(num)
#         return res
                
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res
