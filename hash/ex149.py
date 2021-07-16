from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        len_p = len(points)
        if len_p < 2:
            return len_p
        # 辗转相除法求最大公约数
        def gcd(m, n):
            return m if not n else gcd(n, m % n)

        def getslope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if not dx:
                return 0, 1
            if not dy:
                return 1, 0
            d = gcd(dx, dy)
            return dx/d, dy/d

        res = 0
        for i in range(len_p):
            if res > len_p/2 or res > len_p-i:
                return res
            p1 = points[i]
            lines_dict = {}
            res1 = 0
            for j in range(i+1, len_p):
                p2 = points[j]
                slope = (getslope(p1, p2))
                lines_dict[slope] = (lines_dict[slope]+1) if slope in lines_dict else 2
                res1 = max(res1, lines_dict[slope])
            res = max(res, res1)

        return res




if __name__ == '__main__':
    solution = Solution()
    # points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points = [[1, 1], [2, 2], [8, 8]]
    print(solution.maxPoints(points))

