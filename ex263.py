# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:33:13 2021

@author: lee
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 5 == 0:
            n = n / 5
        while n % 3 == 0:
            n = n / 3
        while n % 2 == 0:
            n = n / 2
        if n == 1:
            return True 
        else:
            return False
        
        
        
# for i in range(20):
#     print(solution.isUgly(i))