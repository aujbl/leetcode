from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n-1, -1
            while l <= r:
                mid = l + (r-l)//2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos+1, i))
        power.sort()
        ans = []
        for i in range(k):
            ans.append(power[i][1])
        # heapq.heapify(power)
        # ans = []
        # for i in range(k):
        #     ans.append(heapq.heappop(power)[1])
        return ans


if __name__ == '__main__':
    solution = Solution()
    mat =[[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
    k = 3
    print(solution.kWeakestRows(mat, k))