# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/26 9:30
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dict = {}
        stack = []
        for n in nums2:
            while stack != [] and n > stack[-1]:
                nums2_dict[stack[-1]] = n
                stack.pop()
            stack.append(n)
            nums2_dict[n] = -1
        ans = []
        for n in nums1:
            ans.append(nums2_dict[n])

        return ans


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(solution.nextGreaterElement(nums1, nums2))
