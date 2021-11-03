# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/3 9:23
"""
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap) <= 2:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i, j))

        res = 0
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            height, o_x, o_y = heapq.heappop(pq)
            for k in range(4):
                x = o_x + dirs[k]
                y = o_y + dirs[k+1]
                if (0 <= x < m) and (0 <= y < n) and visited[x][y] == 0:
                    if height > heightMap[x][y]:
                        res += height - heightMap[x][y]
                    visited[x][y] = 1
                    heapq.heappush(pq, (max(height, heightMap[x][y]), x, y))

        return res


if __name__ == '__main__':
    solution = Solution()
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    print(solution.trapRainWater(heightMap))
