from typing import List
import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.data = []


    def addNum(self, num: int) -> None:
        bisect.insort(self.data, num)
        self.len += 1


    def findMedian(self) -> float:
        if self.len % 2 == 1:
            return self.data[self.len//2]
        return (self.data[self.len//2] + self.data[self.len//2-1]) / 2

# 可以用SortedList
# 进阶：可以使用计数排序来统计0-100内数据的数量

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    solution = Solution()
    print(solution)