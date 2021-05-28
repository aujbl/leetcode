# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:59:54 2021

@author: lee
"""
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            sum_w, d = 0, 1
            for weight in weights:
                sum_w += weight
                if sum_w > mid:
                    sum_w = weight
                    d += 1
            if d > D:
                left = mid + 1
            else:
                right = mid
        return left
            
                