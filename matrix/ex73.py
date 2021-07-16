# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:28:03 2021

@author: lee
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_flag = 0 in matrix[0]
        col_flag = 0 in [matrix[i][0] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i][1::] = [0] * (n-1)
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row_flag:
            matrix[0] = [0] * n
        if col_flag:
            for i in range(m):
                matrix[i][0] = 0