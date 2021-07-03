from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_sum = sum(set(nums))
        nums_sum = sum(nums)
        n_sum = (1+len(nums))*len(nums)//2
        return [nums_sum-set_sum, n_sum-set_sum]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 3, 5, 6, 7]
    print(solution.findErrorNums(nums))
