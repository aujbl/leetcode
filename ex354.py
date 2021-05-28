# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:04:59 2021

@author: lee
"""
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        len_e = len(envelopes)
        envelopes.sort()
        envelope = envelopes[-1]
        cnt = 1

        return cnt
            
    
