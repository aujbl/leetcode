from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        tri_dict = [0, 1, 1]
        if n < 3:
            return tri_dict[n]
        for i in range(3, n+1):
            tri_dict.append(sum(tri_dict))
            tri_dict.pop(0)
        return tri_dict[-1]


if __name__ == '__main__':
    solution = Solution()
    for i in range(38):
        print('i: ', solution.tribonacci(i))
