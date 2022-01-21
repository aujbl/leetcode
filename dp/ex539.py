from sqlite3 import Timestamp


from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def diff(time1: str, time2: str):
            h1, m1 = time1.split(':')
            h2, m2 = time2.split(':')
            h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)

            if m1 > m2:
                h2 -= 1
                m2 += 60
            return (h2 - h1) * 60 + (m2 - m1)


        res = 1440 - diff(timePoints[0], timePoints[-1])
        for i in range(1, len(timePoints)):
            res  = min(res, diff(timePoints[i-1], timePoints[i]))
        return res


if __name__ == '__main__':
    solution = Solution()
    # timePoints = ["23:59","00:00"]
    timePoints=["01:01","02:01","03:00"]
    print(solution.findMinDifference(timePoints))