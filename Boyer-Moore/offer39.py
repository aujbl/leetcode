# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/26 9:24
"""
from typing import List

 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, cnt = nums[0], 0
        for n in nums:
            # 每一对不相同的数字做一次消除，剩下的一定是数量最多的元素
            if cnt == 0:
                candidate = n
            if n == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate


if __name__ == '__main__':
    solution = Solution()
    print(solution)

