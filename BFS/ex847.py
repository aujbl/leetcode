from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}

        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                return dist
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist+1))
                    seen.add((v, mask_v))


if __name__ == '__main__':
    solution = Solution()
    graph = [[1, 2, 3], [0], [0], [0]]
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    print(solution.shortestPathLength(graph))