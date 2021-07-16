# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 08:14:13 2021

@author: lee
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        pass

    def next(self) -> int:
        return 0

    def hasNext(self) -> bool:
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()