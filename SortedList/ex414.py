# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/6 9:57
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        for n in nums:
            if n > c:
                a, b, c = b, c, n
            elif b < n < c:
                a, b = b, n
            elif a < n < b:
                a = n
            else:
                pass
        if a == float('-inf'):
            return c
        else:
            return a


# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums = set(nums)
#         if len(nums) < 3:
#             return max(nums)
#         heap = []
#         for n in nums:
#             heapq.heappush(heap, -n)
#         heapq.heappop(heap)
#         heapq.heappop(heap)
#         return -heapq.heappop(heap)


if __name__ == '__main__':
    solution = Solution()
    print(solution)
