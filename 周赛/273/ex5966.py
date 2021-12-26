# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/26 11:41
"""
from typing import List

 
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        mean = sum(nums) // len(nums)
        a, b = [], []
        for n in nums:
            if n < mean:
                a.append(n)
            else:
                b.append(n)
        a.sort()
        b.sort()
        res = []
        for x, y in zip(a, b):
            res.append((x + y) // 2)
        while len(res) < len(nums)//2:
            res.append(mean)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]
    # [2,3,7,8,8,9,9,10]
    print(solution.recoverArray(nums))

