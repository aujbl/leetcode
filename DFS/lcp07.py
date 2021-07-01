from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        end_dict = {}
        for i in range(n):
            end_dict[i] = []
        for trans in relation:
            end_dict[trans[0]].append(trans[1])

        def dfs(start, cnt, res=0):
            if cnt == k and start == n-1:
                res += 1
            elif cnt < k:
                end = end_dict[start]
                for start in end:
                    res = dfs(start, cnt+1, res)
            return res
        res = dfs(0, 0)
        return res

# class Solution:
#     def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
#         def recursion(start, cnt, res=0):
#             if cnt == k and start == n-1:
#                 res += 1
#             elif cnt < k:
#                 end = []
#                 for trans in relation:
#                     if trans[0] == start:
#                         res = recursion(trans[1], cnt+1, res)
#             return res
#         res = recursion(0, 0)
#         return res

# class Solution:
#     def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
#         def recursion(start, cnt, res=0):
#             if cnt == k and start == n-1:
#                 res += 1
#             elif cnt < k:
#                 end = []
#                 for trans in relation:
#                     if trans[0] == start:
#                         end.append(trans[1])
#                 for start in end:
#                     res = recursion(start, cnt+1, res)
#             return res
#         res = recursion(0, 0)
#         return res




if __name__ == '__main__':
    solution = Solution()
    # n, k = 5, 3
    # relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    n, k = 3, 2
    relation = [[0, 2], [2, 1]]
    print(solution.numWays(n, relation, k))
