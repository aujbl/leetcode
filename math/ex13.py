# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:27:09 2021

@author: lee
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        str_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100,
                    'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1
                    }
        res = i = 0
        while i < len(s):
            key = s[i]
            if i < len(s)-1 and key+s[i+1] in str_dict.keys():
                i += 1
                key += s[i]
            res += str_dict[key]
            i += 1
        return res
            
            
        