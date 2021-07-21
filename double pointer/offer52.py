from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa, pb = pa.next, pb.next
            if not pa and pb:
                pa = headB
            if not pb and pa:
                pb = headA
        return pa



if __name__ == '__main__':
    solution = Solution()

    print(solution)
