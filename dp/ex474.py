from typing import List
#
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
#         for i in range(1, len(strs)+1):
#             nums_0 = strs[i-1].count('0')
#             nums_1 = len(strs[i-1]) - nums_0
#             for j in range(m+1):
#                 for k in range(n+1):
#                     dp[i][j][k] = dp[i-1][j][k]
#                     if j >= nums_0 and k >= nums_1:
#                         dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-nums_0][k-nums_1]+1)
#         return dp[len(strs)][m][n]

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        last_dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(len(strs)):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            nums_0 = strs[i].count('0')
            nums_1 = len(strs[i]) - nums_0
            for j in range(m+1):
                for k in range(n+1):
                    dp[j][k] = last_dp[j][k]
                    if j >= nums_0 and k >= nums_1:
                        dp[j][k] = max(dp[j][k], last_dp[j-nums_0][k-nums_1]+1)
            last_dp = dp
        return dp[m][n]



if __name__ == '__main__':
    # strs = ["111", "1000", "1000", "1000"]
    strs = ["10", "0001", "111001", "1", "0"]
    m, n = 5, 3
    # strs = ["10", "0", "1"]
    # m = 1
    # n = 1
    solution = Solution()
    print(solution.findMaxForm(strs, m, n))
