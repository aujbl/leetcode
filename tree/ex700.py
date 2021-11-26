# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/26 9:06
"""
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            root = root.left if root.val > val else root.right
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution)

