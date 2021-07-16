# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:50:54 2021

@author: lee
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        len_n = 1
        node = head.next
        while node.next:
            len_n += 1
            node = node.next
        len_n += 1
        node.next = head
        k = k % len_n
        node = head
        cnt = 1
        while cnt < len_n - k:
            node = node.next
            cnt += 1
        cur = node.next
        node.next = None
        return cur
            
            
            
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
node.val
node1.val    
        
        
        
        
        
        
        
        
        
        
        
        
        
head = ListNode(1)
node.val = 1
node.next = ListNode(5)
node = node.next

def display(node):
    print(node.val)
    while node.next is not None:
        node = node.next
        print(node.val)