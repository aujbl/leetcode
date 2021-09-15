# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/15 9:43
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        l, r, ans = 0, n - 1, -1
        while l <= r:
            mid = l + (r - l) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            elif get(mid) < get(mid + 1):
                l = mid + 1
            else:
                r = mid - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution)
