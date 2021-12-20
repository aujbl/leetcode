import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for house in houses:
            r = bisect.bisect_right(heaters, house)
            if r == 0:
                closest = heaters[0] - house
            elif r == len(heaters):
                closest = house - heaters[-1]
            else:
                closest = min(heaters[r] - house, house - heaters[r-1])
            res = max(res, closest)
        return res


if __name__ == '__main__':
    solution = Solution()
    houses = [1, 5]
    heaters = [2]
    print(solution.findRadius(houses, heaters))