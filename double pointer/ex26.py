# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:41:34 2021

@author: lee
"""

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         len_n = len(nums)
#         i = 0
#         while i < len_n-1:
#             if nums[i] == nums[i+1]:
#                 nums.pop(i+1)
#                 len_n -= 1
#             else:
#                 i += 1
#         return len_n
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n < 2:
            return len_n
        slow, fast = 1, 1
        while fast < len_n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums))