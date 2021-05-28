# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:13:06 2021

@author: lee
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        
        def bfs(node: TreeNode) -> int:
            if not node.left and not node.right:
                return node.val
            if not node.left:
                return bfs