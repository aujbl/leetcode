# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/29 9:58
"""
from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            # case 1
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # case 2
            if i == 4 and (distance[3] == distance[1] and distance[4] >= distance[2] - distance[0]):
                return True

            #case 3
            if i >= 5 and (distance[i-3] - distance[i-5] <= distance[i-1] <= distance[i-3]
                           and distance[i] >= distance[i-2] - distance[i-4]
                           and distance[i-2] > distance[i-4]):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    distance = [2, 1, 1, 2]
    print(solution.isSelfCrossing(distance))
