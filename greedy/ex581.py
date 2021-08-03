from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        len_n = len(nums)
        max_n, r = float('-inf'), -1
        min_n, l = float('inf'), -1
# 从右往左找到左侧升序停止的位置，从左往右找到右侧降序停止的位置
        for i in range(len_n):
            if max_n > nums[i]:
                r = i
            else:
                max_n = nums[i]
            if min_n < nums[len_n - 1 - i]:
                l = len_n - 1 - i
            else:
                min_n = nums[len_n - 1 - i]

        return 0 if r == -1 else r - l + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 2, 3, 4]
    print(solution.findUnsortedSubarray(nums))