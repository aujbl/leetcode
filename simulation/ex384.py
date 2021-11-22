# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/22 9:05
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.shuffle_data = nums.copy()

    def reset(self) -> List[int]:
        self.shuffle_data = self.data.copy()
        return self.shuffle_data

    def shuffle(self) -> List[int]:
        for i in range(len(self.data)):
            j = random.randrange(i, len(self.shuffle_data))
            self.shuffle_data[i], self.shuffle_data[j] = self.shuffle_data[j], self.shuffle_data[i]
        return self.shuffle_data


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == '__main__':
    solution = Solution()
    print(solution)

