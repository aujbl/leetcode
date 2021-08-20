from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n, i = len(s), 0
        s = list(s)
        ans = []

        def revers_s(sub_s: List):
            sub_s.reverse()
            return sub_s
        while i < n:
            ans += revers_s(s[i:min(i+k, n)])
            i += k
            ans += s[i:min(i+k, n)]
            i += k
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    s = "abcdefg"
    # s = "abcd"
    k = 2
    print(solution.reverseStr(s, k))
