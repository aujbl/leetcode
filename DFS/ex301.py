# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/27 9:31
"""
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = set([s])
        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    # pruning 连续相同的符号，不可能存在有效的结果
                    if i > 0 and ss[i] == s[i-1]:
                        continue
                    # 记录去掉任何一个符号的所有结果
                    if ss[i] == '(' or ss[i] == ')':
                        nextSet.add(ss[:i] + ss[i+1:])
            currSet = nextSet

        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "()())()"
    s = "(a)())()"
    print(solution.removeInvalidParentheses(s))
