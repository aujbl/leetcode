from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count('1')
            for i in range(n):
                if mask & (1 << i) and (num % (i+1) == 0 or (i+1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]
        return f[(1 << n)-1]


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 16):
        print(solution.countArrangement(i))
