from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        i, ans = 1, 0
        while i < n:
            diff = nums[i] - nums[i-1]
            j = i + 1
            while j < n and nums[j] - nums[j-1] == diff:
                j += 1
            ans += ((j-i) * (j-i-1) // 2)
            i = j
        return ans


if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 3, 5, 6, 7]
    # nums = [1, 2, 3, 4, 5, 6]
    nums = [1, 1]
    print(solution.numberOfArithmeticSlices(nums))