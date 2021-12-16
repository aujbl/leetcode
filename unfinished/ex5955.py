# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/12 11:49
"""
from typing import List

 
from collections import defaultdict
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l = r = 0
        fruits_dict = defaultdict(int)
        for p, a in fruits:
            if startPos - k <= p <= startPos + k:
                fruits_dict[p] = a
                if startPos - k <= p <= startPos:
                    l += a
                if startPos <= p <= startPos + k:
                    r += a
        res = max(l, r)
        # for i in range(1, k // 2):
        #     # if  startPos - k + i // 2 + 1 >= startPos:
        #     #     break
        #     l += fruits_dict[startPos + i]
        #     l -= fruits_dict[startPos - k + i // 2]
        #     l -= fruits_dict[startPos - k + i // 2 + 1]
        #     res = max(res, l)
        l -= fruits_dict[startPos - k]
        for i in range(1, k+1):
            l -= fruits_dict[startPos - k + i]
            if i % 2 == 0:
                l += fruits_dict[startPos + (i + 1) // 2]
            res = max(res, l)

        return res


if __name__ == '__main__':
    solution = Solution()
    f = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
    s = 5
    k = 4
    print(solution.maxTotalFruits(f, s, k))

