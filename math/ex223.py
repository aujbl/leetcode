# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/30 15:21
"""
from typing import List


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total_area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if bx2 <= ax1 or ax2 <= bx1:
            cross_x = 0
        else:
            x = [ax1, ax2, bx1, bx2]
            x.sort()
            cross_x = x[2] - x[1]
        if by2 <= ay1 or ay2 <= by1:
            cross_y = 0
        else:
            y = [ay1, ay2, by1, by2]
            y.sort()
            cross_y = y[2] - y[1]
        return total_area - cross_x * cross_y


if __name__ == '__main__':
    solution = Solution()
    ax1 = -2; ay1 = -2; ax2 = 2; ay2 = 2; bx1 = -2; by1 = -2; bx2 = 2; by2 = 2
    print(solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
