# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:27:45 2021

@author: lee
"""
#暴力解法
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        res = 0
        for i in range(len(A)):
            res = int(''.join([str(x) for x in A[0:i+1]]), 2) % 5
            if res > 0:
                result.append(False)
            else:
                result.append(True)
        return result
    



class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        res = 0
        for i in range(len(A)):
            res = (res*2 + int(str(A[i]), 2)) % 5
            print(res)
            if res > 0:
                result.append(False)
            else:
                result.append(True)
        return result