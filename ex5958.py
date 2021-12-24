# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/19 11:09
"""
from typing import List

 
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        i = j = 0
        res = 0
        while i < n:
            j = i + 1
            while j < n and prices[j-1] - prices[j] == 1:
                j += 1
            res += (j - i) * (j - i + 1) // 2
            i = j
        return res


if __name__ == '__main__':
    solution = Solution()
    prices = [3, 2, 1, 4]
    print(solution.getDescentPeriods(prices))

