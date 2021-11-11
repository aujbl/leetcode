# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/11 9:50
"""
from typing import List


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
                g[j] %= mod
            f = g
        return f[k]


if __name__ == '__main__':
    solution = Solution()
    n = 5
    k = 5
    print(solution.kInversePairs(n, k))

