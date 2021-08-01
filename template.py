from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)

        dfs(root, 0, 0)
        nodes.sort()
        ans, lastcol = list(), float('-inf')
        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append([])
            ans[-1].append(value)
        return ans


if __name__ == '__main__':
    solution = Solution()

    print(solution)



