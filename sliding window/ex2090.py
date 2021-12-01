# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/1 9:32
"""
from typing import List

 
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        if len(nums) < 2*k+1:
            return res
        avg_sum = sum(nums[:2*k+1])
        res[k] = avg_sum // (2 * k + 1)
        for i in range(k+1, len(nums)-k):
            avg_sum -= nums[i - k - 1]
            avg_sum += nums[i + k]
            res[i] = avg_sum // (2 * k + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    print(solution.getAverages(nums, k))

