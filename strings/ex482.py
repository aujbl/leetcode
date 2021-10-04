# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/4 8:53
"""
from typing import List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_upper = ''
        for ss in s:
            if ss == '-':
                pass
            elif ss.islower():
                s_upper += ss.upper()
            else:
                s_upper += ss
        head = len(s_upper) % k
        if head > 0:
            return '-'.join([s_upper[:head]] + [s_upper[i:i+k] for i in range(head, len(s_upper), k)])
        else:
            return '-'.join([s_upper[i:i+k] for i in range(0, len(s_upper), k)])


if __name__ == '__main__':
    solution = Solution()
    S = "5F3Z-2e-9-w"
    K = 3
    S = "2-5g-3-J"
    K = 1
    print(solution.licenseKeyFormatting(S, K))
