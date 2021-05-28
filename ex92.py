# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:16:04 2021

@author: lee
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        node = head
        i = 1
        while i < left:
            if i == left-1:
                re_head = node
            node = node.next
            i += 1     
        stack = []
        while i < right+1:
            stack.append(node)
            node = node.next
            i += 1  
        Next = stack[-1].next
        if left == 1:
            head = stack.pop()
            re_head = head
        while stack:
            node = stack.pop()
            re_head.next = node
            re_head = node
        re_head.next = Next
        return head
            
        
        
        
        
        
        
        
        Next = node.next
        if left == 1:
            head = node
        while stack:
            re_head.next = stack.pop()
        re_head.next = Next
        
        return head
        
        
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def display(node):
    print(node.val)
    while node.next is not None:
        node = node.next
        print(node.val)
        
    

    
    
                