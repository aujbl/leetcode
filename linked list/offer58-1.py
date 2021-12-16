# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/16 9:27
"""
from typing import List

 
class Solution:
    def reverseWords(self, s: str) -> str:
        j = len(s) - 1
        res = []
        while j >= 0:
            while j >= 0 and s[j] == ' ':
                j -= 1
            i = j
            while i >= 0 and s[i] != ' ':
                i -= 1
            if i < j:
                res.append(s[i+1:j+1])
            j = i
        return ' '.join(res)


if __name__ == '__main__':
    solution = Solution()
    s = "  hello world!  "
    print(solution.reverseWords(s))

