from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        sum_w = sum(w)
        self.weight = [w[0]/sum_w]
        for w0 in w[1:]:
            self.weight.append(self.weight[-1] + w0/sum_w)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.weight, random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

