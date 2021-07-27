from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res, root_val = -1, root.val

        def dfs(node: TreeNode) -> None:
            nonlocal res
            if not node:
                return
            if -1 < res <= node.val:
                return
            if node.val > root_val:
                res = node.val

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res



if __name__ == '__main__':
    solution = Solution()

    print(solution)