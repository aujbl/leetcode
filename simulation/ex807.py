# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/13 8:56
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        m_max, n_max = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                m_max[i] = max(m_max[i], grid[i][j])
                n_max[j] = max(n_max[j], grid[i][j])

        res = 0
        for i in range(m):
            for j in range(n):
                res += (min(m_max[i], n_max[j]) - grid[i][j])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution)

