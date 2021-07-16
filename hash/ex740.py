# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:05:27 2021

@author: lee
"""
from typing import List

# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         maxVal = max(nums)
#         total = [0] * (maxVal + 1)
#         for val in nums:
#             total[val] += val
        
#         def rob(nums: List[int]) -> int:
#             size = len(nums)
#             first, second = nums[0], max(nums[0], nums[1])
#             for i in range(2, size):
#                 first, second = second, max(first + nums[i], second)
#             return second
        
#         return rob(total)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/delete-and-earn/solution/shan-chu-bing-huo-de-dian-shu-by-leetcod-x1pu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = {}
        for num in nums:
            if num not in total:
                total[num] = 0
            total[num] += num
            
        first = [0 if 1 not in total else total[1]][0]
        second = max(first, [0 if 2 not in total else total[2]][0])
        for i in range(3, max(nums)+1):
            num = [0 if i not in total else total[i]][0]
            first, second = second, max(first+num, second)
        return second