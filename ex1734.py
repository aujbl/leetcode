# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:13:00 2021

@author: 95348
"""
from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        total, odd = 1, encoded[1]
        for i in range(2, len(encoded)+2):
            total ^= i
            if i < len(encoded) and i % 2 == 1:
                odd ^= encoded[i]
        perm = [total ^ odd]
        for en in encoded:
            perm.append(perm[-1] ^ en)
        return perm