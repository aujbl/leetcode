from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            jump = 0
            j = i + nums[i]
            if j % n == i:
                continue
            if nums[i] > 0:
                while jump <= n and nums[j % n] > 0:
                    if j % n == i:
                        return True
                    j += nums[j % n]
                    jump += 1
            else:
                while jump <= n and nums[j % n] < 0:
                    if j % n == i:
                        return True
                    j += nums[j % n]
                    jump += 1
        return False

# 可以考虑快慢指针

if __name__ == '__main__':
    solution = Solution()
    # nums = [2, -1, 1, 2, 2]
    nums = [1, 2, 3, 4, 5]          # 特殊循环
    nums = [1, 1, 2]               # 注意循环起点位置
    nums = [-1, 2]
    print(solution.circularArrayLoop(nums))

