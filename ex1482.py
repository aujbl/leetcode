# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:45:00 2021

@author: lee
"""
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        
        def ifdays(days: int) -> bool:
            m1 = k1 = 0
            for i, bloom in enumerate(bloomDay):
                if bloom <= days:
                    k1 += 1
                    if k1 == k:
                        m1 += 1
                        if m1 == m:
                            return True
                        k1 = 0
                else:
                    k1 = 0
            return False
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            days = low + (high-low) // 2
            if ifdays(days):
                high = days
            else:
                low = days + 1
        return low
            

            
        