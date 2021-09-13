# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/13 15:04
"""
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x0, y0 in points:
            dis_dict = {}
            for x1, y1 in points:
                dis = (x1-x0)**2 + (y1-y0)**2
                if dis not in dis_dict:
                    dis_dict[dis] = 1
                else:
                    dis_dict[dis] += 1
            for cnt in dis_dict.values():
                ans += cnt*(cnt-1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution)
