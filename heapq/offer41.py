import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []

    def addNum(self, num: int) -> None:
        if len(self.big_heap) != len(self.small_heap):
            heapq.heappush(self.big_heap, -heapq.heappushpop(self.small_heap, num))
        else:
            heapq.heappush(self.small_heap, -heapq.heappushpop(self.big_heap, -num))

    def findMedian(self) -> float:
        return self.small_heap[0] if len(self.big_heap) != len(self.small_heap) else (-self.big_heap[0] + self.small_heap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()