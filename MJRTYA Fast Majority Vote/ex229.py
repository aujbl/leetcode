# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/22 9:45
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            if vote1 > 0 and num == element1:
                vote1 += 1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            elif vote1 == 0:
                element1 = num
                vote1 = 1
            elif vote2 == 0:
                element2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1

        if vote1 > 0 and cnt1 > len(nums) / 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            ans.append(element2)

        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,3,3,2,2,2]
    print(solution.majorityElement(nums))
