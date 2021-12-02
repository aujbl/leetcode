# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/2 9:17
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = score.copy()
        s.sort(reverse=True)
        idx_score = [(b, a) for a, b in enumerate(s)]
        idx_score.sort(key=lambda x: -x[0])
        d = dict(idx_score)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = []
        for s in score:
            if d[s] < 3:
                res.append(medal[d[s]])
            else:
                res.append(str(d[s] + 1))
        return res


if __name__ == '__main__':
    solution = Solution()
    score = [2, 1]
    print(solution.findRelativeRanks(score))

