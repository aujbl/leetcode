# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/24 9:56
"""
from typing import List
import heapq

 
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        pq = []
        i = 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if apples[i]:
                heapq.heappush(pq, [i+days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)
                ans += 1
            i += 1

        while pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if len(pq) == 0:
                break
            p = heapq.heappop(pq)
            num = min(p[0] - i, p[1]) # 剩余天数和剩余水果数，取小即为可维持天数
            ans += num
            i += num
        return ans


if __name__ == '__main__':
    solution = Solution()
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    apples = [3, 0, 0, 0, 0, 2]
    days = [3, 0, 0, 0, 0, 2]
    print(solution.eatenApples(apples, days))

