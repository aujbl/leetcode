from typing import List
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         len_p = len(piles)
#         dp = [[0] * len_p for _ in range(len_p)]
#         for i in range(len_p):
#             dp[i][i] = piles[i]
#         i= len_p-2
#         while i >= 0:
#             j = i+1
#             while j < len_p:
#                 dp[i][j] = max(dp[i][i]-dp[i+1][j], dp[j][j]-dp[i][j-1])
#                 j += 1
#             i -= 1
#         return dp[0][len_p-1] > 0
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        len_p = len(piles)
        last_dp = [0]*(len_p-1) + [piles[-1]]
        i = len_p-2
        while i >= 0:
            dp = [0] * len_p
            j, dp[i] = i+1, piles[i]
            while j < len_p:
                dp[j] = max(piles[i]-last_dp[j], piles[j]-dp[j-1])
                j += 1
            last_dp = dp
            i -= 1
        return last_dp[-1] > 0

if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    solution = Solution()
    print(solution.stoneGame(piles))
