# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/19 9:54
"""
from typing import List

# recursion
# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         def steps(n):
#             if n == 1:
#                 return 0
#             if n % 2 == 0:
#                 return 1 + steps(n // 2)
#             else:
#                 return min(steps((n + 1) // 2), steps((n - 1) // 2)) + 2
#         return steps(n)


class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            else:
                if n == 3:
                    n -= 1
                elif (n >> 1) & 1 == 1:
                    n += 1
                else:
                    n -= 1
            steps += 1
        return steps


if __name__ == '__main__':
    solution = Solution()
    print(solution)

