# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:08:26 2021

@author: 95348
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        #初始化大数组耗时长
        # dp = [[0] * arrLen for _ in range(steps+1)]
        dp = [0] * arrLen
        temp = [0] *arrLen
        dp[0] = 1
        for i in range(1, steps+1):
            #走太远是回不去的，所以其实min(arrLen,steps/2+1)就可以了！
            for j in range(min(arrLen,steps//2+1)):
                temp[j] = sum(dp[max(j-1, 0):min(j+2, arrLen)]) % (10**9+7)
            dp[:min(arrLen,steps//2+1)] = temp[:min(arrLen,steps//2+1)]
        return dp[0]



