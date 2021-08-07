from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            j = i + nums[i]
            if nums[i] > 0:
                while (j <= i + n) and nums[j % n] > 0:
                    if j % n == i:
                        return True
                    j += nums[j % n]
                return False
            else:
                while j >= i - n and nums[j % n] < 0:
                    if j % n == i:
                        return True
                    j += nums[j % n]
                return False


if __name__ == '__main__':
    solution = Solution()
    nums = [2, -1, 1, 2, 2]
    nums = [-1, 2]
    nums = [1, 2, 3, 4, 5]
    print(solution.circularArrayLoop(nums))



