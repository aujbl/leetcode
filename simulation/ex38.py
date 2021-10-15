# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/15 9:04
"""
from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):
            len_n = len(res)
            new_res = ''
            j = 0
            while j < len_n:
                cur = res[j]
                cnt = 0
                while j < len_n and res[j] == cur:
                    j += 1
                    cnt += 1
                new_res += str(cnt)
                new_res += str(cur)
            res = new_res
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(30))
