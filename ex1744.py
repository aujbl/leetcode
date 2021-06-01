from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre = [0]
        for candies in candiesCount:
            pre.append(pre[-1] + candies)
        res = []
        for ty, day, cap in queries:
            have = [pre[ty] + 1, pre[ty+1]]
            need = [day + 1, (day+1) * cap]
            if need[1] < have[0] or need[0] > have[1]:
                res.append(False)
            else:
                res.append(True)
        return res


if __name__ == '__main__':
    # candiesCount = [7, 4, 5, 3, 8]
    # queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
    candiesCount = [5, 2, 6, 4, 1]
    queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]

    solution = Solution()
    print(solution.canEat(candiesCount, queries))
