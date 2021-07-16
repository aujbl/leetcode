# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:51:13 2021

@author: 95348
"""
from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preprocess = [arr[0]]
        for num in arr[1:]:
            preprocess.append(preprocess[-1] ^ num)
        
        res = 0
        for i, num1 in enumerate(preprocess):
            if num1 == 0:
                res += i
            for j, num2 in enumerate(preprocess[i+1:]):
                if num1 == num2:
                    res += j
        return res
            