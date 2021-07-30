from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power, ans = len(columnTitle) - 1, 0
        for c in columnTitle:
            ans += ((26**power) * (ord(c) - 64))
            power -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('ZY'))