# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/23 8:45
"""
from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in {1, 3, 9, 27, 81, 243, 729, 2187, 6561,
                     19683, 59049, 177147, 531441, 1594323,
                     4782969, 14348907, 43046721, 129140163, 387420489, 1162261467}


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(45))
