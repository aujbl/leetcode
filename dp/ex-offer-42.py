from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         pre_sum = 0
#         res = nums[0]
#         for num in nums:
#             pre_sum = max(pre_sum+num, num)
#             res = max(res, pre_sum)
#         return res


# 分治法
class Solution:
    class Status:
        def __init__(self, lSum=0, rSum=0, mSum=0, iSum=0):
            self.lSum = lSum
            self.rSum = rSum
            self.mSum = mSum
            self.iSum = iSum







if __name__ == '__main__':
    solution = Solution()
    nums = [-10000]
    print(solution.maxSubArray(nums))