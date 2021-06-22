# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# slow, fast pointer
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next and head.next.next:
            slow = head.next
            fast = slow.next
        else:
            return None
        while fast:
            if fast == slow:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            else:
                slow = slow.next
                if fast.next and fast.next.next:
                    fast = fast.next.next
                else:
                    return None
        return None


'''hash map'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         ptrs = {head}
#         next = head.next
#         while next:
#             if next in ptrs:
#                 return next
#             ptrs.add(next)
#             next = next.next
#         return None
