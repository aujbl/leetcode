# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/24 9:37
"""
from typing import List


class Solution:
    def originalDigits(self, s: str) -> str:
        nums = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
        s_dict = defaultdict(int)
        for k in s:
            s_dict[k] += 1

        def del_s(s_num, del_num):
            for ss in s_num:
                s_dict[ss] -= del_num

        res = [0] * 10
        for i, k in enumerate('zwuxg'):
            num = 2 * i
            res[num] = s_dict[k]
            del_s(nums[num], res[num])

        for i, k in enumerate('hfv'):
            num = (i + 1) * 2 + 1
            res[num] = s_dict[k]
            del_s(nums[num], res[num])

        res[1] = s_dict['o']
        del_s(nums[1], res[1])
        res[9] = s_dict['n']

        res = [i for i in range(10) if res[i] > 0]

        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution)

