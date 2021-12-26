# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/19 10:59
"""
from typing import List

 
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        res = []
        for i in range(len(spaces)):
            if i == 0:
                res.append(s[:spaces[0]])
            elif i == len(spaces) - 1:
                res.append(s[spaces[-1]::])
            else:
                res.append(s[spaces[i-1]:spaces[i]])
        return ' '.join(res)


if __name__ == '__main__':
    solution = Solution()
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]
    print(solution.addSpaces(s, spaces))

