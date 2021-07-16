# -*- coding: utf-8 -*-
"""
Created on Fri May  7 08:43:36 2021

@author: 95348
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i, res = 1, start
        while i < n:
            start += 2
            res = res ^ start
            i += 1
        return res
    