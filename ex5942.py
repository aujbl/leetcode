# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/5 10:58
"""
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnts = [0] * 10
        for d in digits:
            if cnts[d] < 3:
                cnts[d] += 1
        digits = []
        for i in range(10):
            digits += [i] * cnts[i]

        res = set()
        for i in range(len(digits)):
            d1 = digits[i]
            for j in range(len(digits)):
                d2 = digits[j]
                if j == i:
                    continue
                for k in range(len(digits)):
                    if k == j or k == i:
                        continue
                    d3 = digits[k]
                    num = d1 * 100 + d2 * 10 + d3
                    if 99 < num < 999 and num % 2 == 0:
                        res.add(num)
        res = list(res)
        res.sort()
        return res


if __name__ == '__main__':
    solution = Solution()

    digits = [0, 0, 0]
    print(solution.findEvenNumbers(digits))

