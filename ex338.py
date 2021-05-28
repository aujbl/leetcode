# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:03:26 2021

@author: lee
"""
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        B = []
        while num > 0:
            B.append(num%2)
            num = num//2
        res = []
        len_B = len(B)
        l = 0
        count = sum(B)
        res.append(count)
        while l < len_B:
            if B[l] == 0:
                B[l] = 1
                l += 1
            else:
                B[l] = 0
                count = count + l - 1
                res.append(count)
                l = 0
        res.reverse()
        return res
                
        