# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/1 10:04
"""
from typing import List


# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1 = [int(x) for x in version1.split('.')]
#         v2 = [int(x) for x in version2.split('.')]
#         n = max(len(v1), len(v2))
#         v1 += [0] * (n - len(v1))
#         v2 += [0] * (n - len(v2))
#         for x, y in zip(v1, v2):
#             if x > y:
#                 return 1
#             elif x < y:
#                 return -1
#         return 0

# 还可以考虑双指针
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            v1 = v2 = 0
            while i < m and version1[i] != '.':
                v1 = 10 * v1 + int(version1[i])
                i += 1
            i += 1
            while j < n and version2[j] != '.':
                v2 = 10 * v2 + int(version2[j])
                j += 1
            j += 1
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


if __name__ == '__main__':
    solution = Solution()
    version1 = "1"
    version2 = "1.101"
    print(solution.compareVersion(version1, version2))
