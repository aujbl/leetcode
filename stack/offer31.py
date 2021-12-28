# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/28 10:18
"""
from typing import List

 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        stack = []
        for n in pushed:
            if n != popped[0]:
                stack.append(n)
            else:
                popped.pop(0)
                while stack and popped and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
        return True if not stack else False


if __name__ == '__main__':
    solution = Solution()
    pushed = [2, 1, 0]
    popped = [1, 2, 0]
    print(solution.validateStackSequences(pushed, popped))

