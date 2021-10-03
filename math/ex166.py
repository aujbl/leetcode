# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/3 9:57
"""
from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        flag = False
        if (numerator < 0) ^ (denominator < 0):
            flag = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        re_dict = {}
        int_part = numerator // denominator
        float_part = numerator % denominator
        res = str(int_part) + '.' if float_part > 0 else str(int_part)
        i = len(res)
        while float_part > 0 and float_part not in re_dict:
            re_dict[float_part] = i
            int_part = (float_part * 10) // denominator
            float_part = (float_part * 10) % denominator
            res += str(int_part)
            i += 1
        if float_part in re_dict:
            res = res[:re_dict[float_part]] + '(' + res[re_dict[float_part]:] + ')'
        if flag:
            res = '-' + res
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fractionToDecimal(-1, -2147483648))
