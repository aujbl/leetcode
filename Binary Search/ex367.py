# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/4 15:30
"""
from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-7:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num

# binary search

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         l, r = 1, num
#         while l <= r:
#             mid = l + ((r - l) >> 1)
#             if mid * mid == num:
#                 return True
#             elif mid * mid > num:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return False

if __name__ == '__main__':
    solution = Solution()
    print(solution)
