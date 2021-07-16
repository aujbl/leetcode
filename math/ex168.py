from typing import List


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            res = chr(columnNumber % 26+65) + res
            columnNumber = columnNumber // 26
        return res


if __name__ == '__main__':
    solution = Solution()
    # for i in range(100):
    #     print('i: %d' % i, solution.convertToTitle(i))
    print(solution.convertToTitle(2147483647))