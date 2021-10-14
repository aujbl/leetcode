# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/14 8:50
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                l = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                r = mid - 1
            else:
                return mid


if __name__ == '__main__':
    solution = Solution()
    arr = [24,69,100,99,79,78,67,36,26,19]
    print(solution.peakIndexInMountainArray(arr))
