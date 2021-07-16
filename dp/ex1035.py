# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:05:57 2021

@author: 95348
"""
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n+1)
        for i in range(1, m+1):
            last_dp = dp
            dp = [0]* (n+1)
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = last_dp[j-1] + 1
                else:
                    dp[j] = max(last_dp[j], dp[j-1])
        return dp[-1]
                    
                    