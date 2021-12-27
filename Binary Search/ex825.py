from typing import List
import bisect


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        # n = len(ages)
        for age in ages:
            min_age = 0.5 * age + 7
            l = bisect.bisect_right(ages, min_age)
            r = bisect.bisect_right(ages, age)
            if r > l:
                res += (r - l - 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    # ages = [108,115,5,24,82]
    # ages = [16, 16]
    # ages = [16, 17, 18]
    ages = [20, 30, 100, 110, 120]
    print(solution.numFriendRequests(ages))
