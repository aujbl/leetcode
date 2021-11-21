# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/21 9:33
"""
from typing import List

 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        h = 0
        for ch in root.children:
            h = max(self.maxDepth(ch), h)
        return h + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution)

