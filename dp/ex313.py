from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        len_p = len(primes)
        p = [1] * len_p
        for i in range(2, n+1):
            candidates = [p[i] * primes[i] for i in range(len_p)]
            min_can, min_idx = candidates[0], 0
            # for j in range(len_p):
            #     if candidates[j] <

if __name__ == '__main__':
    solution = Solution()
    print(solution)
