from typing import List

# 二分法
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         l, r = 0, x
#         while l <= r:
#             mid = l + (r-l)//2
#             if mid ** 2 > x:
#                 r = mid - 1
#             elif mid ** 2 < x:
#                 l = mid + 1
#             else:
#                 return mid
#         return l-1


# 牛顿法
# f(x) is bow shape, f'(x) -> 0, f"(x) = 0
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        n = x
        while n ** 2 > x:
            print('n: ', n)
            n = int(n/2 + x/2/n)

        return n


if __name__ == '__main__':
    solution = Solution()
    # for i in range(100):
    #     print('i: %d ' % i, solution.mySqrt(i))
    print(solution.mySqrt(100))

