# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/29 9:06
"""
from typing import List

 
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = c = 0
        res = 0
        for a in range(n - 3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [28, 8, 49, 85, 37, 90, 20, 8]
    print(solution.countQuadruplets(nums))

