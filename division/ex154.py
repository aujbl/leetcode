# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:10:23 2021

@author: lee
"""
from typing import List

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         low, high = 0, len(nums) - 1
#         while low < high:
#             pivot = low + (high - low) // 2
#             if nums[pivot] < nums[high]:
#                 high = pivot
#             elif nums[pivot] > nums[high]:
#                 low = pivot + 1
#             else:
#                 high -= 1
#         return nums[low]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui--16/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]



if __name__ == '__main__':
    solution = Solution()
    # nums = [2, 3, 3, 5, 1, 2]
    nums = [2, 2, 2, 0, 1]
    # nums = [10, 1, 10, 10, 10]
    print(solution.findMin(nums))
















