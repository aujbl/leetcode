from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [-1, 0, 1, 0, -1]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    island = [(i, j)]
                    area = 1
                    grid[i][j] = 0
                    while island:
                        r0, c0 = island.pop()
                        for k in range(4):
                            r, c= r0 + directions[k], c0+directions[k+1]
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                                island.append((r, c))
                                area += 1
                                grid[r][c] = 0
                    res = max(res, area)
                    if res >= m*n//2:
                        return res
        return res


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # grid = [[0, 0, 0, 0, 1, 0, 0]]
    print(solution.maxAreaOfIsland(grid))
