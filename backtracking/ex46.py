from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        len_n = len(nums)
        res = []

        def backtrack(first=0):
            if first == len_n-1:
                res.append(nums[:])
            for i in range(first, len_n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(solution.permute(nums))
