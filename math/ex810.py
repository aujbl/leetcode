# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:19:07 2021

@author: lee
"""
from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        xor = 0
        for num in nums:
            xor ^= num
        return xor == 0