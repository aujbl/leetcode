class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ss in s:
            if ss == ')':
                s1 = [stack.pop()]
                while s1[-1] != '(':
                    s1 += stack.pop()
                stack += s1[:-1]
            else:
                stack.append(ss)
        return ''.join(stack)

if __name__ == '__main__':
    s = "a(bcdefghijkl(mno)p)q"
    solution = Solution()
    print(solution.reverseParentheses(s))