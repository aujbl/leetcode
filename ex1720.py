# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:15:32 2021

@author: 95348
"""
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        encoded = [first] + encoded
        i = 1
        while i < len(encoded):
            encoded[i] = encoded[i-1] ^ encoded[i]
            i += 1
        return encoded
            


# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         res = [first]
#         for num in encoded:
#             res.append(num ^ res[-1])
#         return res