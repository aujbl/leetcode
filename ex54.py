# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:23:14 2021

@author: lee
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        row = list(range(m))
        col = list(range(n))
        res = []
        while row and col:
            r = row[0]
            for c in col:
                res.append(matrix[r][c])
            c = col[-1]
            for r in row[1::]:
                res.append(matrix[r][c])
            row.pop(0)
            col.pop()
            row.reverse()
            col.reverse()
        return res
            