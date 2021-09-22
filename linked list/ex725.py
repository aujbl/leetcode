# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        res = []
        num, plus = n // k, n % k
        node = head
        for i in range(k):
            cnt = num + 1 if i < plus else num
            if cnt > 0:
                new_head = node
                new_node = new_head
                while cnt > 1:
                    node = node.next
                    new_node.next = node
                    new_node = new_node.next
                    cnt -= 1
                node = node.next
                new_node.next = None
                res.append(new_head)
            else:
                res.append([])
        return res


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3)))
    print(solution.splitListToParts(head, 5))
