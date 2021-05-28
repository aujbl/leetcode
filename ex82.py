# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:28:33 2021

@author: lee
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        #节点是非为空，不直接判断节点值
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next                
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
node.val
node1.val    
        
        
        
        
        
        
        
        
        
        
        
        
        
head = ListNode()
node.val = 1
node.next = ListNode()
node = node.next

def display(node):
    print(node.val)
    while node.next is not None:
        node = node.next
        print(node.val)