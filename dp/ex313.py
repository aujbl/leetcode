from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        len_p = len(primes)
        p = [1] * len_p
        for i in range(2, n+1):
            candidates = [dp[p[k]] * primes[k] for k in range(len_p)]
            dp[i] = min(candidates)
            for j in range(len_p):
                if candidates[j] == dp[i]:
                    p[j] += 1
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    n = 12
    primes = [2, 7, 13, 19]
    n = 1
    primes = [2, 3, 5]
    print(solution.nthSuperUglyNumber(n, primes))
