# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         while head and head.val == val:
#             head = head.next
#         former = head
#         while former:
#             latter = former.next
#             while latter and latter.val == val:
#                 latter = latter.next
#             former.next = latter
#             former = former.next
#         return head

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            head = head.next
        return head