# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/16 9:07
"""
from typing import List

 
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            if i < j and nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.exchange([]))

