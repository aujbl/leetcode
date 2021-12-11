# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/11 9:40
"""
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        self.top = self.persons[0]
        self.top_persons = [self.top]
        cnt_tickits = defaultdict(int)
        cnt_tickits[self.top] = 1
        for p in self.persons[1:]:
            cnt_tickits[p] += 1
            if cnt_tickits[p] >= cnt_tickits[self.top]:
                self.top = p
            self.top_persons.append(self.top)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)
        return self.top_persons[idx - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


if __name__ == '__main__':
    solution = Solution()
    print(solution)

