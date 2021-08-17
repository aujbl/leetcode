from typing import List


class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        n_a = n_l = i = 0
        s0 = ''
        for s1 in s:
            if s1 != s0:
                n_l = 0
            if s1 == 'A':
                n_a += 1
                if n_a >= 2:
                    return False
            elif s1 == 'L':
                n_l += 1
                if n_l >= 3:
                    return False
            s0 = s1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "PPALLP"
    s = "PPALLL"
    s = ''
    print(solution.checkRecord(s))

