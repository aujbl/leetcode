# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/5 8:53
"""
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for a in arr:
            k = a - difference
            if k not in dp:
                dp[a] = 1
            else:
                dp[a] = dp[k] + 1
        return max(dp.values())


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 3, 4]
    arr = [1, 3, 5, 7]
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference = -2
    print(solution.longestSubsequence(arr, difference))
