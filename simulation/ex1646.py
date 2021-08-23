from typing import List


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n+1)
        nums[1] = 1
        ans = 0
        for i in range(2, n+1):
            nums[i] = nums[i // 2] + (nums[i // 2 + 1]) * (i % 2)
            ans = max(ans, nums[i])
        return ans


if __name__ == '__main__':
    solution = Solution()
    # print(solution.getMaximumGenerated(3))
    for j in range(101):
        print('j: ', j, solution.getMaximumGenerated(j))
