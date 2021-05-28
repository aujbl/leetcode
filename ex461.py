class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # binx, biny = bin(x)[2:], bin(y)[2:]
        # len_x, len_y = len(binx), len(biny)
        # if len_x < len_y:
        #     binx = '0' * (len_y-len_x) + binx
        # else:
        #     biny = '0' * (len_x-len_y) + biny
        # res = 0
        # for b1, b2 in zip(binx, biny):
        #     if b1 != b2:
        #         res += 1
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    x, y = 3, 1
    solution = Solution()
    print(solution.hammingDistance(x, y))