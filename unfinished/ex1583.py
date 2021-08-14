from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j

        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x

        unhappyCount = 0
        for x in range(n):
            y = match[x]
            index = order[x][y]
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                if order[u][x] < order[u][v]:
                    unhappyCount += 1
                    break

        return unhappyCount


作者：LeetCode - Solution
链接：https: // leetcode - cn.com / problems / count - unhappy - friends / solution / tong - ji - bu - kai - xin - de - peng - you - by - leetcode - solutio /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# class Solution:
#     def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
#         importance = dict()
#         for i, pre in enumerate(preferences):
#             for j, p in enumerate(pre):
#                 importance[(i, p)] = n-j-1
#         len_p, ans = len(pairs), 0
#
#         def unhappy(x, y, u, v):
#             return importance[(x, u)] > importance[(x, y)] and importance[(u, x)] > importance[(u, v)]
#
#         for i in range(len_p):
#             x, y = pairs[i]
#             for j in range(len_p):
#                 if i == j:
#                     continue
#                 u, v = pairs[j]
#                 if unhappy(x, y, u, v):
#                     ans += 1
#                 if unhappy(x, y, v, u):
#                     ans += 1
#                 if unhappy(y, x, u, v):
#                     ans += 1
#                 if unhappy(y, x, v, u):
#                     ans += 1
#         return ans


if __name__ == '__main__':
    solution = Solution()
    n = 4
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]
    n = 2
    preferences = [[1], [0]]
    pairs = [[1, 0]]
    n = 4
    preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
    pairs = [[1, 3], [0, 2]]
    print(solution.unhappyFriends(n, preferences, pairs))
