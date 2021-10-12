# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/12 8:47
"""
from typing import List


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            x_power = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_power
                x_power *= x_power
                N //= 2
            return ans
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    solution = Solution()
    x = 2
    n = 10
    print(solution.myPow(x, n))
