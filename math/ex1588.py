from typing import List

# O(n^2)
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         if n < 3:
#             return sum(arr)
#         for i in range(1, n):
#             arr[i] += arr[i-1]
#         arr.insert(0, 0)
#         ans = arr[-1]
#         for i in range(3, n+1, 2):
#             for j in range(i, n+1):
#                 ans += (arr[j] - arr[j-i])
#         return ans

# O(n)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            l_e, l_o = i // 2 + 1, (i + 1) // 2
            r_e, r_o = (n - 1 - i) // 2 + 1, (n - i) // 2
            ans += (l_e * r_e + l_o * r_o) * arr[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 4, 2, 5, 3]
    # arr = [1, 2]
    # arr = [10, 11, 12]
    print(solution.sumOddLengthSubarrays(arr))


