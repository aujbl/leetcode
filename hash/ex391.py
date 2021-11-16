# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/16 9:32
"""
from typing import List

 
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x0, y0, a0, b0 = rectangles[0]
        points = set()
        def add_point(p):
            if p not in points:
                points.add(p)
            else:
                points.remove(p)
        area = 0
        for rect in rectangles:
            x, y, a, b = rect
            x0 = min(x0, x)
            y0 = min(y0, y)
            a0 = max(a0, a)
            b0 = max(b0, b)
            area += ((b - y) * (a - x))
            for i in [x, a]:
                for j in [y, b]:
                    add_point((i, j))
        if len(points) != 4:
            return False
        else:
            for i in [x0, a0]:
                for j in [y0, b0]:
                    if (i, j) not in points:
                        return False
        return area == (b0 - y0) * (a0 - x0)


if __name__ == '__main__':
    solution = Solution()
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    # rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
    # rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
    print(solution.isRectangleCover(rectangles))

