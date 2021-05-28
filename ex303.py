# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:03:49 2021

@author: lee
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        len_n = len(self.nums)
        sumrange = 0
        self.res = [0]
        for i in range(len_n):
            sumrange += self.nums[i]
            self.res.append(sumrange)

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1] - self.res[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)