# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:46:19 2021

@author: lee
"""
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        row = list(range(n))
        col = list(range(n))
        res = [[0 for i in range(n)] for j in range(n)]
        cnt = 1
        while cnt < n*n+1:
            r = row[0]
            for c in col:
                if res[r][c] == 0:
                    res[r][c] = cnt
                    cnt += 1
            c = col[-1]
            for r in row:
                if res[r][c] == 0:
                    res[r][c] = cnt
                    cnt += 1
            row.pop(0)
            col.pop()
            row.reverse()
            col.reverse()
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         m = len(matrix)
#         n = len(matrix[0])
#         if m == 1:
#             return matrix[0]
#         row = list(range(m))
#         col = list(range(n))
#         res = []
#         while row and col:
#             r = row[0]
#             for c in col:
#                 res.append(matrix[r][c])
#             c = col[-1]
#             for r in row[1::]:
#                 res.append(matrix[r][c])
#             row.pop(0)
#             col.pop()
#             row.reverse()
#             col.reverse()
#         return res