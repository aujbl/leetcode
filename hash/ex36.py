# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/9/17 9:16
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(nums: List[str]) -> bool:
            flag = [False] * 9
            for n in nums:
                if n != '.':
                    if flag[int(n) - 1]:
                        return False
                    flag[int(n) - 1] = True
            return True

        for i in range(9):
            nums = board[i]
            if not is_valid(nums):
                return False

        for i in range(9):
            nums = []
            for b in board:
                nums.append(b[i])
            if not is_valid(nums):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for m in range(i, i + 3):
                    nums += board[m][j:j + 3]
                if not is_valid(nums):
                    return False

        return True

# 可以使用hash记录

if __name__ == '__main__':
    solution = Solution()
    print(solution)
