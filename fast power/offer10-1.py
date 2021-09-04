# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/4 9:20
"""
from typing import List

# O(n), O(n)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         fibs = [0, 1]
#         for i in range(2, n+1):
#             fibs.append((fibs[-1] + fibs[-2]) % (10**9+7))
#         return fibs[-1]


# dp:O(n),O(1)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         fibs = [0, 1]
#         for i in range(2, n+1):
#             fibs.append((fibs[1] + fibs[0]) % (10**9+7))
#             fibs = fibs[1:]
#         return fibs[-1]

class Solution:
    def fib(self, n: int) -> int:
        MOD = 10**9 + 7
        if n < 2:
            return n

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n-1)
        return res[0][0]


if __name__ == '__main__':
    solution = Solution()

    print(solution)
