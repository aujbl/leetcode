import bisect
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target_dict = {}

        for i, t in enumerate(target):
            target_dict[t] = i
        d = []
        for a in arr:
            if a in target_dict:
                idx = target_dict[a]
                site = bisect.bisect_left(d, idx)
                if site < len(d):
                    d[site] = idx
                else:
                    d.append(idx)
        return len(target) - len(d)


if __name__ == '__main__':
    solution = Solution()
    target = [5, 1, 3]
    arr = [9, 4, 2, 3, 4]
    target = [6, 4, 8, 1, 3, 2]
    arr = [4, 7, 6, 2, 3, 8, 6, 1]
    print(solution.minOperations(target, arr))