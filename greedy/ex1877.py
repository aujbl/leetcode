from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        len_n = len(nums)
        nums.sort()
        res = 0
        for i in range(len_n//2):
            res = max(res, nums[i]+nums[len_n-1-i])
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 5, 2, 3]
    nums = [3, 5, 4, 2, 4, 6]
    nums = [1, 1]
    print(solution.minPairSum(nums))

