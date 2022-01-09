# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2022/1/9 11:14
"""
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        i, j = 0, n - 1
        while i < n and nums[i] != 1:
            i += 1

        if i == 0 and nums[-1] == 1:
            while j > i and nums[j] == 1:
                j -= 1

        while j > i and nums[j] != 1:
            j -= 1

        # return min(n - j - 1 + i, (j - i + 1) - nums[i:j + 1].count(1))
        return (j - i + 1) - nums[i:j + 1].count(1)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0]
    print(solution.minSwaps(nums))

