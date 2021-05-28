# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 08:31:24 2021

@author: lee
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n < 3:
            return max(nums)
        
        def rob1(start, end):
            dp = [nums[start], max(nums[start:start+2])]
            for i in range(start+2, end):
                dp.append(max(dp[1], nums[i]+dp[0]))
                # dp.pop(0)
                dp = dp[1:]
            return dp[-1]
        
        return max(rob1(0, len_n-1), rob1(1, len_n))


        # dp = [nums[0], max(nums[:2])]
        # for i in range(2, len_n-1):
        #     dp.append(max((nums[i]+dp[0]), dp[1]))
        #     dp.pop(0)
        # first = dp[-1]
        
        # dp = [nums[1], max(nums[1:3])]
        # for i in range(3, len_n):
        #     dp.append(max((nums[i]+dp[0]), dp[1]))
        #     dp.pop(0)
        # second = dp[-1]
        # return max(first, second)