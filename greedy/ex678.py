# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/12 9:15
"""
from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        min_c = max_c = 0
        for ss in s:
            if ss == '(':
                min_c += 1
                max_c += 1
            elif ss == ')':
                min_c = max(min_c-1, 0)
                max_c -= 1
                if max_c < 0:
                    return False
            else:
                min_c = max(min_c-1, 0)
                max_c += 1
        return min_c == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution)
