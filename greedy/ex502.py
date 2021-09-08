# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/8 11:38
"""
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w > max(capital):
            return sum(heapq.nlargest(k, profits)) + w

        n = len(profits)
        curr = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])

        pq = []
        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heapq.heappush(pq, -arr[curr][1])  # heapq默认小根堆，-号取得最大值
                curr += 1

            if pq:
                w -= heapq.heappop(pq)  # -- = +最大值
            else:
                break
        return w


if __name__ == '__main__':
    solution = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(solution.findMaximizedCapital(k, w, profits, capital))
