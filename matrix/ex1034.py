from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        if grid[row][col] == color:
            return grid

        m, n = len(grid), len(grid[0])
        directions = [-1, 0, 1, 0, -1]
        q = [[row, col]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        find_color = grid[row][col]
        union = set()
        union.add((row, col))
        while q:
            r, c = q.pop()
            for i in range(4):
                r1 = r + directions[i]
                c1 = c + directions[i+1]
                if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] == find_color and not visited[r1][c1]:
                    q.append([r1, c1])
                    union.add((r1, c1))
            visited[r][c] = True

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = grid[i][j]

        for r, c in union:
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                res[r][c] = color
                continue
            for i in range(4):
                r1, c1 = r + directions[i], c + directions[i+1]
                if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] != find_color:
                    res[r][c] = color
                    break

        return res


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    row = 1
    col = 1
    color = 2
    print(solution.colorBorder(grid, row, col, color))
