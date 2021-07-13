from typing import List
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        ps = []

        for l, r, h in buildings:
            ps.append((l, -h))
            ps.append((r, h))
        ps.sort()

        prev = 0
        q = SortedList([prev])

        for pos, h in ps:
            q.add(-h) if h < 0 else q.remove(h)
            # cur保持为当前q中最高的位置
            cur = q[-1]
            if cur != prev:
                res.append([pos, cur])
                prev = cur

        return res



if __name__ == '__main__':
    solution = Solution()
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    buildings = [[0, 2, 3], [2, 5, 3]]
    print(solution.getSkyline(buildings))

