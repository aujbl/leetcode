from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = ['0', '1']
        for i in range(1, n):
            new_res = []
            for num in res:
                new_res.append('0' + num)
            res.reverse()
            for num in res:
                new_res.append('1' + num)

            res = new_res
        res = [int(n, 2) for n in res]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(10))

