from typing import List


# fast power
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            rows, cols, tmp = len(a), len(b[0]), len(b)
            c = [[0] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    for k in range(tmp):
                        c[i][j] += a[i][k] * b[k][j]
                        c[i][j] %= MOD
            return c

        def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if (n & 1) == 1:
                    ret = multiply(ret, mat)
                n >>= 1
                mat = multiply(mat, mat)
            return ret

        res = matrixPow(mat, n)
        return sum(res[0]) % MOD


# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MOD = 10**9+7
#         dp = [[0, 0, 0], [0, 0, 0]]
#         dp[0][0] = 1
#         for i in range(1, n+1):
#             dp_new = [[0, 0, 0], [0, 0, 0]]
#
#             # end with 'P'
#             for j in range(2):
#                 for k in range(3):
#                     dp_new[j][0] = (dp_new[j][0] + dp[j][k]) % MOD
#
#             # end with 'A'
#             for k in range(3):
#                 dp_new[1][0] = (dp_new[1][0] + dp[0][k]) % MOD
#
#             # end with 'L'
#             for j in range(2):
#                 for k in range(1, 3):   # !!!
#                     dp_new[j][k] = (dp_new[j][k] + dp[j][k-1]) % MOD
#             dp = dp_new
#
#         return (sum(dp[0]) + sum(dp[1])) % MOD


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord(10101))

