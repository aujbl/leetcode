# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/25 9:36
"""
from typing import List
import math
 
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets) / math.log(minutesToTest // minutesToDie + 1))


if __name__ == '__main__':
    solution = Solution()
    print(solution.poorPigs(1000, 15, 60))

