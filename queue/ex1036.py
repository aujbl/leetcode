from typing import List
from collections import deque


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
        BOUNDARY = 10 ** 6

        rows = sorted(set(pos[0] for pos in blocked) | {source[0], target[0]})
        columns = sorted(set(pos[1] for pos in blocked) | {source[1], target[1]})
        r_mapping, c_mapping = dict(), dict()

        r_id = (0 if rows[0] == 0 else 1)
        r_mapping[rows[0]] = r_id
        for i in range(1, len(rows)):
            r_id += (1 if rows[i] == rows[i-1] + 1 else 2)
            r_mapping[rows[i]] = r_id
        if rows[-1] != BOUNDARY - 1:
            r_id += 1

        c_id = (0 if columns[0] == 0 else 1)
        c_mapping[columns[0]] = c_id
        for i in range(1, len(columns)):
            c_id += (1 if columns[i] == columns[i-1] + 1 else 2)
            c_mapping[columns[i]] = c_id
        if columns[-1] != BOUNDARY - 1:
            c_id += 1

        grid = [[0] * (c_id+1) for _ in range(r_id+1)]
        for x, y in blocked:
            grid[r_mapping[x]][c_mapping[y]] = 1

        sx, sy = r_mapping[source[0]], c_mapping[source[1]]
        tx, ty = r_mapping[target[0]], c_mapping[target[1]]

        q = deque([(sx, sy)])
        grid[sx][sy] = 1
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx <= r_id and 0 <= ny <= c_id and grid[nx][ny] != 1:
                    if (nx, ny) == (tx, ty):
                        return True
                    q.append((nx, ny))
                    grid[nx][ny] = 1
        return False


# class Solution:
#     def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
#         BLOCKED, VALID, FOUND = -1, 0, 1
#         BOUNDARY = 10 ** 6
#
#         if len(blocked) < 2:
#             return True
#
#         hash_blocked = set(tuple(pos) for pos in blocked)
#
#         def check(start: List[int], finish: List[int]) -> int:
#             sx, sy = start
#             fx, fy = finish
#             countdown = len(blocked) * (len(blocked) - 1) // 2
#
#             q = deque([(sx, sy)])
#             visited = set([(sx, sy)])
#
#             while q and countdown > 0:
#                 x, y = q.popleft()
#                 for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
#                     if 0 <= nx < BOUNDARY and 0 <= y < BOUNDARY and (nx, ny) not in hash_blocked and (nx, ny) not in visited:
#                         if (nx, ny) == (fx, fy):
#                             return FOUND
#                         countdown -= 1
#                         q.append((nx, ny))
#                         visited.add((nx, ny))
#             if countdown > 0:
#                 return BLOCKED
#             return VALID
#
#         if (result := check(source, target)) == FOUND:
#             return True
#         elif result == BLOCKED:
#             return False
#         else:
#             result = check(target, source)
#             if result == BLOCKED:
#                 return False
#             return True


if __name__ == '__main__':
    solution = Solution()
    blocked = [[0, 1], [1, 0]]
    source = [0, 0]
    target = [0, 2]
    print(solution.isEscapePossible(blocked, source, target))
