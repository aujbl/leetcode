from typing import List


# 求权重最小的路径，不符合要求
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         dst_dict = {}
#         for i in range(n):
#             dst_dict[i] = []
#         for s, d, f in flights:
#             dst_dict[s].append((d, f))
#         fare = [-1] * n
#         fare[src] = 0
#         cnt = 0
#         pos = [(src, 0)]
#         while cnt <= k:
#             next_pos = []
#             for s, c in pos:
#                 dsts = dst_dict[s]
#                 for d, f in dsts:
#                     if c+1 < k:
#                         next_pos.append((d, c+1))
#                     if fare[d] == -1:
#                         fare[d] = fare[s] + f
#                     else:
#                         fare[d] = min(fare[d], fare[s]+f)
#             pos = next_pos
#             cnt += 1
#         return fare[dst]
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float('inf')] * n for _ in range(k+2)]
        f[0][src] = 0
        for t in range(1, k+2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t-1][j] + cost)
        ans = min(f[t][dst] for t in range(1, k+2))
        return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    solution = Solution()
    n = 4
    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1
    print(solution.findCheapestPrice(n, edges, src, dst, k))
