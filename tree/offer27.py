from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        mirror_root = TreeNode(root.val)
        mirror_q = [mirror_root]
        q = [root]
        while q:
            new_q = []
            for n in q:
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            new_q.reverse()

            if not new_q:
                break

            new_mirror_q = []
            for i in range(0, len(new_q)):
                if i % 2 == 0:
                    mirror_q[i//2].left = TreeNode(new_q[i].val)
                    new_mirror_q.append(mirror_q[i//2].left)
                else:
                    mirror_q[i//2].right = TreeNode(new_q[i].val)
                    new_mirror_q.append(mirror_q[i//2].right)

            mirror_q = new_mirror_q
            new_q.reverse()
            q = new_q
        return mirror_root


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(solution.mirrorTree(root))
