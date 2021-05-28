# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:57:09 2021

@author: lee
"""
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        compare = lambda x, y: 1 if x+y > y+x else -1
        nums.sort(key=(cmp_to_key(compare)), reverse=True)
        return '0' if nums[0]=='0' else ''.join(nums)
                  






# class Solution(object):
#     def largestNumber(self, nums):
#         nums_str = list(map(str, nums))
#         compare = lambda x, y: 1 if x + y < y + x else -1
#         nums_str.sort(key=cmp_to_key(compare))
#         res = "".join(nums_str)
#         if res[0] == "0":
#             res = "0"
#         return res

