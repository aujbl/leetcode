# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/14 10:08
"""
from typing import List

 
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        q = []
        heapq.heapify(q)
        spend_time = 0
        for d, l in courses:
            if spend_time + d <= l:
                spend_time += d
                heapq.heappush(q, -d)
            elif q and -q[0] > d:
                # 条件成立时，总花费时间可能更少，剩余可用时间可能更多
                spend_time += heapq.heappop(q) + d
                heapq.heappush(q, -d)
        return len(q)


if __name__ == '__main__':
    solution = Solution()
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(solution.scheduleCourse(courses))

