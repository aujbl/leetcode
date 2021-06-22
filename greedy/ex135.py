# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:15:57 2021

@author: lee
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:      
        
        n = len(ratings)
        result = [1] * n
        for i in range(n-1):
            if ratings[i] < ratings[i+1] and result[i] >= result[i+1]:
                result[i+1] = result[i] + 1
                
        for j in range(n-1, 0, -1):
            if ratings[j-1] > ratings[j] and result[j-1] <= result[j]:
                result[j-1] = result[j] + 1
                
        return sum(result)