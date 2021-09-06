# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/6 9:01
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution)
