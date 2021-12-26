# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/26 10:04
"""
from typing import List

 
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        triangle = [1]
        for i in range(0, len(a)-1):
            triangle.append(triangle[-1] * a[i])

        res, tmp = [], 1
        for j in range(len(a)-1, 0, -1):
            res.append(tmp * triangle[j-1])
            tmp *= a[j]
        return res

# class Solution:
#     def constructArr(self, a: List[int]) -> List[int]:
#         U, D = [1], [1]
#         for i in range(0, len(a)-1):
#             U.append(U[-1] * a[i])
#             D.append(D[-1] * a[len(a) - i - 1])
#         res = []
#         D.reverse()
#         for x, y in zip(U, D):
#             res.append(x * y)
#         return res


if __name__ == '__main__':
    solution = Solution()
    a = [1, 2, 3, 4]
    print(solution.constructArr(a))

