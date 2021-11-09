# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/8 9:23
"""
from typing import List
from collections import defaultdict

 
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         s_dict = defaultdict(int)
#         g_dict = defaultdict(int)
#         same = 0
#         res = []
#         for s, g in zip(secret, guess):
#             if s == g:
#                 same += 1
#             s_dict[s] += 1
#             g_dict[g] += 1
#         res.append(str(same))
#         res.append('A')
#         total_same = 0
#         for s in s_dict.keys():
#             total_same += min(s_dict[s], g_dict[s])
#         total_same = total_same - same
#         res.append(str(total_same))
#         res.append('B')
#         return ''.join(res)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt_s, cnt_g = [0] * 10, [0] * 10
        same = 0
        for s, g in zip(secret, guess):
            if s == g:
                same += 1
            cnt_s[int(s)] += 1
            cnt_g[int(g)] += 1
        total_same = 0
        for x, y in zip(cnt_s, cnt_g):
            total_same += min(x, y)
        return str(same) + 'A' + str(total_same - same) + 'B'


if __name__ == '__main__':
    solution = Solution()
    secret = "1807"
    guess = "7810"
    print(solution.getHint(secret, guess))

