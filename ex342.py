class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        bin_n = bin(n)[2:].zfill(31)
        cnt = 0
        for i, s in enumerate(bin_n):
            if s == '0':
                pass
            elif s == '1':
                cnt += 1
                if i % 2 == 0:
                    pass
                else:
                    return False
                if cnt > 1:
                    return False
            else:
                return False
        return True

if __name__ == '__main__':
    n = 16
    solution = Solution()
    print(solution.isPowerOfFour(n))

