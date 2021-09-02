# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/2 10:25
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
#         n = 1
#         node = head
#         while node.next:
#             node = node.next
#             n += 1
#         i = 1
#         node = head
#         while i < n + 1 - k:
#             node = node.next
#             i += 1
#         return node

# 快慢指针，fast先走k步，然后slow开始出发，当fast走到终点时，slow即为所求
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        i = 1
        while i < k:
            fast = fast.next
            i += 1
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution)
