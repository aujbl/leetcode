from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1            # !!!
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]
# 还可以反转s，求最长公共子序列


if __name__ == '__main__':
    solution = Solution()
    s = "bbbab"
    # s = "cbbd"
    print(solution.longestPalindromeSubseq(s))



