# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/10 15:11
"""
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        i = total = 0
        while i < n and total + chalk[i] <= k:
            total += chalk[i]
            i += 1
        if i >= n:
            k %= total
            i = total = 0
            while i < n and total + chalk[i] <= k:
                total += chalk[i]
                i += 1
        return i

# 还可以计算前缀和，优化第二遍的查找

if __name__ == '__main__':
    solution = Solution()
    chalk = [5, 1, 5]
    k = 22
    chalk = [3, 4, 1, 2]
    k = 25
    print(solution.chalkReplacer(chalk, k))
