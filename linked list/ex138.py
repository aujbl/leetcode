from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# hash, O(n), O(n)
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return None
#         node = head
#         n = 0
#         node_dict = {node: n}
#         new_head = Node(node.val)
#         new_node = new_head
#         new_node_dict = {n: new_node}
#         while node.next:
#             n += 1
#             node = node.next
#             node_dict[node] = n
#             new_node.next = Node(node.val)
#             new_node = new_node.next
#             new_node_dict[n] = new_node
#         node = head
#         new_node = new_head
#         while node:
#             if node.random:
#                 new_node.random = new_node_dict[node_dict[node.random]]
#             node = node.next
#             new_node = new_node.next
#         return new_head

# 迭代+节点拆分， O(n) + O(1）
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node = head
        while node:
            new_node = Node(node.val)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next
        node = head
        new_head = node.next
        new_node = new_head
        while node:
            if node.random:
                new_node.random = node.random.next.random
            node = node.next.next
            new_node = node.next
        return new_node


if __name__ == '__main__':
    solution = Solution()

    print(solution)