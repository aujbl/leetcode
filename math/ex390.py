# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2022/1/2 10:09
"""
from typing import List

 
class Solution:
    def lastRemaining(self, n: int) -> int:
        a1, an = 1, n
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k == 0:
                k = 1
                a1 += step
                if cnt % 2:
                    an -= step
            else:
                k = 0
                if cnt % 2:
                    a1 += step
                an -= step
            cnt >>= 1
            step <<= 1
        return a1


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemaining(1000000000))

