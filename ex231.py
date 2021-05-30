# 位运算: (1)   n & (n - 1) == 0
#        (2)   n & -n == n
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n & (n-1) == 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 注意
        if n < 1:
            return False
        return n & (n-1) == 0
# 循环
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n < 1:
#             return False
#         bin_n = bin(n)[2:]
#         cnt = 0
#         for s in bin_n:
#             if s == '1':
#                 cnt += 1
#             if cnt > 1:
#                 return False
#         return True

if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.isPowerOfTwo(n))

