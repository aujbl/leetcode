# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/8/31 10:40
"""
from typing import List


# 区间修改
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for i, j, book in bookings:
            diff[i-1] += book
            if j < n:
                diff[j] -= book
        for k in range(1, n):
            diff[k] += diff[k-1]
        return diff


if __name__ == '__main__':
    solution = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(solution.corpFlightBookings(bookings, n))
