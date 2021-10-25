# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/25 9:04
"""
from typing import List


# binary search
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#
#         def rowSearch(row):
#             n = len(row)
#             l, r = 0, n-1
#             while l <= r:
#                 mid = l + ((r - l) >> 1)
#                 if row[mid] == target:
#                     return True
#                 elif row[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             return False
#
#         for row in matrix:
#             if row[0] > target:
#                 break
#             elif row[-1] < target:
#                 continue
#             else:
#                 if rowSearch(row):
#                     return True
#
#         return False

# z search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(solution.searchMatrix(matrix, target))
