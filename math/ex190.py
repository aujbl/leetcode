# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:43:29 2021

@author: lee
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:].zfill(32)
        bin_n = ''.join(reversed(bin_n))
        return int(bin_n, 2)