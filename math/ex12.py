# -*- coding: utf-8 -*-
"""
Created on Fri May 14 08:34:57 2021

@author: 95348
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        str_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 
                    100:'C', 90:'XC', 50:'L', 40:'XL',
                    10:'X', 9:'IX',5:'V', 4:'IV', 1:'I'
                    }
                    
        res = ''
        for den in str_dict.keys():
            div = num // den
            if div > 0:
                res += str_dict[den] * div
            num %= den 
        return res
            