# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/7 8:50
"""
from typing import List


# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         l = r = 0
#         cnt = 0
#         for ss in s:
#             if ss == 'R':
#                 r += 1
#             else:
#                 l += 1
#             if l == r:
#                 cnt += 1
#                 l = r = 0
#         return cnt


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        cnt = 0
        for ss in s:
            if ss == 'R':
                r += 1
            else:
                r -= 1
            if r == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution)
