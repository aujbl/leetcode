# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/26 10:45
"""
from typing import List

 
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def walk(ss: str):
            x0, y0 = startPos
            i = cnt = 0
            while i < len(ss):
                if ss[i] == 'U':
                    x0 -= 1
                elif ss[i] == 'D':
                    x0 += 1
                elif ss[i] == 'L':
                    y0 -= 1
                else:
                    y0 += 1
                if 0 <= x0 < n and 0 <= y0 < n:
                    cnt += 1
                    i += 1
                else:
                    break
            return cnt
        res = []
        for i in range(len(s)):
            res.append(walk(s[i:]))
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"
    print(solution.executeInstructions(n, startPos, s))

