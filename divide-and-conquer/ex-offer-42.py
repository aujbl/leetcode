from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = 0
        res = nums[0]
        for num in nums:
            pre_sum = max(pre_sum+num, num)
            res = max(res, pre_sum)
        return res



if __name__ == '__main__':
    solution = Solution()
    nums = [-10000]
    print(solution.maxSubArray(nums))