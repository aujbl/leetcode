# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/30 9:08
"""
from typing import List

 
class Solution:
    def findNthDigit(self, n: int) -> int:
        nums = [0, 9, 189, 2889, 38889, 488889, 5888889,
                68888889, 788888889]
        i = 0
        while i < 9 and n > nums[i]:
            i += 1
        # i为n所指向的数字的位数
        # num是n最后所指向的数字
        # remain是num中n所指向的位，remain=0时，指向上一个数字的最后一位
        num = (n - nums[i - 1]) // i + 10 ** (i - 1)
        remain = (n - nums[i-1]) % i
        if remain == 0:
            return int(str(num - 1)[-1])
        else:
            return int(str(num)[remain-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(1654980001))

