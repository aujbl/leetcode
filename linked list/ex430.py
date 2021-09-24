# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/24 9:25
"""
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            cur = node
            last = None
            while cur:
                nxt = cur.next
                if cur.child:
                    child_last = dfs(cur.child)

                    cur.next = cur.child
                    cur.child.prev = cur

                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last
        dfs(head)
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution)
