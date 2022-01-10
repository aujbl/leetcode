from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        no_zero = True
        for r in range(m):
            row = [str(n) for n in grid[r]]
            row = ''.join(row)
            if no_zero and '0' in row:
                no_zero = False
            row = row.split('1')
            for s in row:
                if s and len(s) < stampWidth:
                    return False
                else:
                    continue
        for c in range(n):
            col = []
            for r in range(m):
                col.append(str(grid[r][c]))
            col = ''.join(col)
            if no_zero and '0' in col:
                no_zero = False
            col = col.split('1')
            for c in col:
                if c and len(c) < stampHeight:
                    return False
                else:
                    continue

        if not no_zero and (m < stampHeight or n < stampWidth):
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    # grid = [[1], [0], [0], [0]]
    stampHeight = 4
    stampWidth = 3
    print(solution.possibleToStamp(grid, stampHeight, stampWidth))