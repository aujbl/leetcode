# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/18 9:15
"""
from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << (len(bin(num)) - 2)) - 1 - num


if __name__ == '__main__':
    solution = Solution()
    print(solution.findComplement(2**32-1))
