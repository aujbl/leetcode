from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        flag = False
        for l, r in ranges:
            if flag:
                if l-1 <= left <= r:
                    left = r
            else:
                if l <= left <= r:
                    left = r
                    flag = True
            if flag and left >= right:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    ranges = [[1, 2], [3, 4], [5, 6]]
    left, right = 2, 5
    ranges = [[1, 10], [10, 20]]
    left, right = 21, 21
    print(solution.isCovered(ranges, left, right))