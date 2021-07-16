# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:04:40 2021

@author: lee
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        len_s = len(S)
        if len_s < 2:
            return S
        res = []
        i = 0
        while i < len_s:
            if not res or res[-1] != S[i]:
                res.append(S[i])
            else:
                res.pop()
            i += 1
        return ''.join(res)
        