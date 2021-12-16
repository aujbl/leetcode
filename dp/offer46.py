# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/13 10:20
"""
from typing import List

 
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [0, 1]
        for i in range(len(num)):
            if i > 0 and 9 < int(num[i-1:i+1]) < 26:
                r = dp[0] + dp[1]
            else:
                r = dp[1]
            dp = dp[1:] + [r]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.translateNum(12258))

