# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:22:52 2021

@author: lee
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        if m != 0:
            n = len(matrix[0])
        else:
                n = 0
        matrix = [[0] * n] + matrix
        self.matrix = []
        for row in matrix:
            self.matrix.append([0]+row)
        i = j = 1
        while i < m+1:
            j = 1
            while j < n+1:
                self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1] + self.matrix[i][j]
                j += 1
            i += 1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] + self.matrix[row1][col1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1]




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
