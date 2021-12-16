# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/13 10:48
"""
from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_dict = defaultdict(lambda: -1)
        tmp = res = 0
        for i in range(len(s)):
            last = ch_dict[s[i]]
            ch_dict[s[i]] = i
            tmp = tmp + 1 if tmp < i - last else i - last
            res = max(res, tmp)
        return res
  

if __name__ == '__main__':
    solution = Solution()
    s = "aabcb"
    print(solution.lengthOfLongestSubstring(s))

