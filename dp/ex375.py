# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/12 9:02
"""
from typing import List

 
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        '''二分，只能取中间作为分界点，但这不一定是最优的'''
        '''
        l, r = 1, n
        res = 0
        while l <= r:
            mid = l + ((r - l) >> 1)
            res += mid
            l = mid + 1
        return res - n
        '''
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k-1], f[k+1][j]) for k in range(i, j))
        return f[1][n]


if __name__ == '__main__':
    solution = Solution()
    n = 10
    print(solution.getMoneyAmount(n))

