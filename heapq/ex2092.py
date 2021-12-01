# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/1 10:29
"""
from typing import List
from collections import deque, defaultdict
 
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        # 注意先排序
        meetings.sort(key=lambda x: x[2])
        m = len(meetings)

        res = [False] * n
        res[0] = res[firstPerson] = True

        i = 0
        while i < m:
            j = i
            while j + 1 < m and meetings[j + 1][2] == meetings[i][2]:
                j += 1

            vertices = set()
            edges = defaultdict(list)
            for k in range(i, j + 1):
                x, y = meetings[k][:2]
                vertices.update([x, y])
                edges[x].append(y)
                edges[y].append(x)

            q = deque([u for u in vertices if res[u]])
            while q:
                u = q.popleft()
                for v in edges[u]:
                    if not res[v]:
                        res[v] = True
                        q.append(v)

            i = j + 1

        return [i for i in range(n) if res[i]]


if __name__ == '__main__':
    solution = Solution()
    n = 4
    meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
    firstPerson = 3

    n = 12
    meetings = [[10, 8, 6], [9, 5, 11], [0, 5, 18], [4, 5, 13], [11, 6, 17], [0, 11, 10], [10, 11, 7], [5, 8, 3],
                [7, 6, 16], [3, 6, 10], [3, 11, 1], [8, 3, 2], [5, 0, 7], [3, 8, 20], [11, 0, 20], [8, 3, 4],
                [1, 9, 4], [10, 7, 11], [8, 10, 18]]
    firstPerson = 9
    print(solution.findAllPeople(n, meetings, firstPerson))

