from typing import List


# class Solution:
#     def reorderedPowerOf2(self, n: int) -> bool:
#         def isPowerOfTwo(n: int) -> bool:
#             return (n & (n-1)) == 0
#
#         nums = sorted(list(str(n)))
#         m = len(nums)
#         vis = [False] * m
#
#         def backtrack(idx: int, num: int) -> bool:
#             if idx == m:
#                 return isPowerOfTwo(num)
#             for i, ch in enumerate(nums):
#                 if (num == 0 and ch == '0') or vis[i] or (i > 0 and not vis[i-1] and ch == nums[i-1]):
#                     continue
#                 vis[i] = True
#                 if backtrack(idx+1, num*10 + ord(ch) - ord('0')):
#                     return True
#                 vis[i] = False
#             return False
#
#         return backtrack(0, 0)

def countDigits(n: int):
    cnt = [0] * 10
    while n:
        cnt[n % 10] += 1
        n //= 10
    return tuple(cnt)


powerOf2Digits = {countDigits(1 << i) for i in range(30)}


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return countDigits(n) in powerOf2Digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorderedPowerOf2(1))
