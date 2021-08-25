from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        stk = [0]

        def dfs(x: int):
            if x == n - 1:
                # ans.append(stk)    传入引用，导致错误
                ans.append(stk[:])
                return
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        dfs(0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    graph = [[1, 2], [3], [3], []]
    # graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(solution.allPathsSourceTarget(graph))
