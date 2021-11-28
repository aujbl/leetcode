# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/28 9:43
"""
from typing import List

 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = [0] * 26
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []

        for ch in p:
            p_cnt[ord(ch) - ord('a')] += 1

        s_cnt = [0] * 26
        for ch in s[:len_p]:
            s_cnt[ord(ch) - ord('a')] += 1

        res = [0] if p_cnt == s_cnt else []

        for i in range(len(p), len(s)):
            s_cnt[ord(s[i-len_p]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1
            if s_cnt == p_cnt:
                res.append(i-len_p+1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution)

