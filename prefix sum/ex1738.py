# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:06:00 2021

@author: lee
"""
from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        #注意m， n位置
        coordinate = [[0] * n for _ in range(m)]
        coordinate[0][0] = matrix[0][0]
        for j in range(1, n):
            coordinate[0][j] = coordinate[0][j-1] ^ matrix[0][j]
        for i in range(1, m):
            coordinate[i][0] = coordinate[i-1][0] ^ matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                coordinate[i][j] = coordinate[i-1][j-1] ^ coordinate[i-1][j] ^ \
                                    coordinate[i][j-1] ^ matrix[i][j]
        res = []
        while coordinate:
            res += coordinate.pop()
        res.sort(reverse=True)
        return res[k-1]


