# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/29 9:49
"""
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum_m = sum(machines)
        n = len(machines)
        if sum_m % n != 0:
            return -1
        avg = sum_m // n
        ls, rs = 0, sum_m
        ans = 0
        for i in range(n):
            rs -= machines[i]
            a = max(i * avg - ls, 0)
            b = max((n - i - 1) * avg - rs, 0)
            ans = max(ans, a+b)
            ls += machines[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    machine = [100000,0,100000,0,100000,0,100000,0,100000,0,100000,0]
    print(solution.findMinMoves(machine))
