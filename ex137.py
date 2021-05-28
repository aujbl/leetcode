# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:41:47 2021

@author: 95348
"""
from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1]
        return ans[0]
    