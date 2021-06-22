# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:26:11 2021

@author: lee
"""

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         b = 0
#         bb = b*b
#         while bb <= c:
#             temp = (c - bb) ** 0.5
#             if temp == int(temp):
#                 return True
#             b += 1
#             bb = b*b
#         return False
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** 0.5)
        while l <= r:
            power = l**2 + r**2
            if power < c:
                l += 1
            elif power > c:
                r -= 1
            else:
                return True
        return False




if __name__ == '__main__':
    solution = Solution()
    c = 0
    print(solution.judgeSquareSum(c))
