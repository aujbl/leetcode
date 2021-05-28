# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:00:54 2021

@author: lee
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        
        it1, it2 = dfs(root1), dfs(root2)
        while True:
            try:
                num1 = next(it1)
                try:
                    num2 = next(it2)
                except StopIteration:
                    return False
            except StopIteration:
                try:
                    num2 = next(it2)
                    return False
                except StopIteration:
                    return True
            if num1 != num2:
                return False
                    



root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(3), TreeNode(2))