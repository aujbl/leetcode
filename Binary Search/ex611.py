from typing import List
import bisect

# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         len_n = len(nums)
#         nums.sort()
#         ans = 0
#         for i in range(len_n-1):
#             for j in range(i+1, len_n):
#                 ans += bisect.bisect_left(nums[j+1:], nums[i]+nums[j])
#         return ans


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        len_n = len(nums)
        nums.sort()
        ans = 0
        for i in range(len_n-1):
            k = i
            for j in range(i+1, len_n):
                while k+1 < len_n and nums[k+1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k-j, 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 3, 4]
    # nums = [0, 0, 0]
    print(solution.triangleNumber(nums))