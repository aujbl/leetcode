# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/26 11:11
"""
from typing import List
from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pos_dict = defaultdict(list)
        for i in range(n):
            pos_dict[arr[i]].append(i)
        total_dict = {}
        for k in pos_dict.keys():
            total_dict[k] = (sum(pos_dict[k]), len(pos_dict[k]))
        res = []
        for i in range(n):
            res.append(abs(total_dict[arr[i]][0] - total_dict[arr[i]][1] * i))
        return res
  

if __name__ == '__main__':
    solution = Solution()
    arr = [2, 1, 3, 1, 2, 3, 3]
    print(solution.getDistances(arr))

