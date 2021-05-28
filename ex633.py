# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:26:11 2021

@author: lee
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = 0
        bb = b*b
        while bb <= c:
            temp = (c - bb) ** 0.5
            if temp == int(temp):
                return True
            b += 1
            bb = b*b
        return False