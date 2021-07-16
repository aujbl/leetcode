# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:30:23 2021

@author: lee
"""

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         len_n = len(nums)
#         i = 0
#         while i < len_n:
#             if nums[i] == val:
#                 nums.pop(i)
#                 len_n -= 1
#             else:
#                 i += 1
#         return len_n

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(solution.removeElement(nums, val))



