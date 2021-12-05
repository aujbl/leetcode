# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/5 9:42
"""
from typing import List

 
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def power(a, x):
            p = 1
            while x > 0:
                p *= a
                x -= 1
            return p
        p = power(a, b[0]) % MOD
        for x in b[1:]:
            p = power(p, 10) * power(a, x) % MOD
        return p


if __name__ == '__main__':
    solution = Solution()
    print(solution)

