# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headB or not headA:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next
            pb = pb.next
            if not pa:
                if pb:
                    pa = headB
            if not pb:
                if pa:
                    pb = headA
        return pa