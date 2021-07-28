from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        ans = []

        def findparent(node: TreeNode):
            nonlocal parents
            if node.left:
                parents[node.left.val] = node
                findparent(node.left)
            if node.right:
                parents[node.right.val] = node
                findparent(node.right)

        def findans(node: TreeNode, src: TreeNode, depth: int):
            nonlocal parents
            nonlocal ans
            if not node:
                return
            if depth == k:
                ans.append(node.val)
                return
            if node.left != src:
                findans(node.left, node, depth+1)
            if node.right != src:
                findans(node.right, node, depth+1)
            if node.val in parents and parents[node.val] != src:
                findans(parents[node.val], node, depth+1)

        findparent(root)
        findans(target, None, 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    target = 5
    K = 2
    print(solution.distanceK(root, target, K))

# root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))