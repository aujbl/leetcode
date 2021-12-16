# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/6 16:57
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def if_reverse(node: ListNode) -> bool:
            i = 0
            while i < k and node:
                node = node.next
                i += 1
            return i == k

        new_head = ListNode(None)
        node = new_head
        while if_reverse(head):
            r_node = head
            prev = head
            # prev.next = None
            i = 1
            while i < k:
                r_node = r_node.next
                tmp = r_node
                tmp.next = prev
                prev = tmp
                i += 1

            node.next = prev
            node = head
            node.next = None
            head = r_node.next
        if head:
            node.next = head
        return new_head.next


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for i in range(2, 6):
        node.next = ListNode(i)
        node = node.next

    solution = Solution()
    print(solution.reverseKGroup(head, 2))

