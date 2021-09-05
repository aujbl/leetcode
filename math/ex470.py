# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/5 9:20
"""
from typing import List


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r1, r2 = rand7(), rand7()
        sum_r = (r1 - 1) * 7 + r2
        if sum_r > 40:
            return self.rand10()
        elif sum_r % 10 == 0:
            return 10
        else:
            return sum_r % 10


if __name__ == '__main__':
    solution = Solution()
    print(solution)
