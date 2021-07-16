from typing import List

# ((val >> i) & 1)可以用来取出第i位, 10**9的二进制表示为30位
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        len_n, res = len(nums), 0
        for i in range(30):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            res += cnt * (len_n - cnt)
        return res


# class Solution:
#     def totalHammingDistance(self, nums: List[int]) -> int:
#         cnt_bin = dict()
#         for i in range(30):
#             cnt_bin[i] = 0
#         for num in nums:
#             bin_num = bin(num)[2:].zfill(30)
#             for i, s in enumerate(bin_num):
#                 if s == '1':
#                     cnt_bin[i] += 1
#         res = 0
#         for cnt in cnt_bin.values():
#             res += (cnt * (len(nums) - cnt))
#         return res

# 暴力超时解法
# class Solution:
#     def totalHammingDistance(self, nums: List[int]) -> int:
#         def hammingDistance(x: int, y: int) -> int:
#             return bin(x ^ y).count('1')
#         res = 0
#         for i, num1 in enumerate(nums):
#             for num2 in nums[i+1:]:
#                res += hammingDistance(num1, num2)
#         return res

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # nums = [4, 14, 2]
    solution = Solution()
    res = solution.totalHammingDistance(nums)
    print(res)