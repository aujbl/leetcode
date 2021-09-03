# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/3 10:02
"""
from typing import List
import heapq


# class Solution:
#     def smallestK(self, arr: List[int], k: int) -> List[int]:
#         heap = []
#         for a in arr:
#             heapq.heappush(heap, a)
#         ans = []
#         for i in range(k):
#             ans.append(heapq.heappop(heap))
#         return ans


# 快速排序
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         def quick_sort(arr, l, r):
#             if l >= r:
#                 return
#             i, j = l, r
#             while i < j:
#                 while i < j and arr[j] >= arr[l]:
#                     j -= 1
#                 while i < j and arr[i] <= arr[l]:
#                     i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#             arr[l], arr[i] = arr[i], arr[l]
#             quick_sort(arr, l, i-1)
#             quick_sort(arr, i + 1, r)
#         quick_sort(arr, 0, len(arr)-1)
#         return arr[:k]

# 快速排序修改
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr
        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i-1)
            if k > i:
                return quick_sort(i+1, r)
            return arr[:k]
        return quick_sort(0, len(arr)-1)


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4
    print(solution.getLeastNumbers(arr, k))
