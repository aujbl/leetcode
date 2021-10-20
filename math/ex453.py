# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/20 9:36
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_n = min(nums)
        res = 0
        for n in nums:
            res += (n - min_n)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(solution.minMoves(nums))
