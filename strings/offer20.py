# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/12/29 10:01
"""
from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        while s and s[0] == ' ':
            s = s[1:]
        while s and s[-1] == ' ':
            s = s[:-1]
        if not s:
            return False

        if len(s.split(' ')) > 1:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]
            if s and (s[0] == '+' or s[0] == '-'):
                return False

        s = s.lower()
        for ch in s:
            if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', 'e', '.']:
                return False
        cnt = 0
        for ch in s:
            if ch == '.' or ch == 'e':
                cnt += 1
            if cnt > 1:
                return False

        # if s[0] == '.':
        #     if not s[1:].isnumeric():
        #         return False
        parts = s.split('.')
        if len(parts) == 2:
            p0, p1 = parts
            if not p0:
                if not p1:
                    return False
            for p in parts:
                if p == '':
                    continue
                if not p.isnumeric():
                    return False
            # if not p0.isnumeric() or not p1.isnumeric():
            #     return False

        parts = s.split('e')
        if len(parts) == 2:
            # if not parts[1] and parts[0] == '0':
            #     return False
            # if parts[0] == '':
            #     return False
            for p in parts:
                if p == '':
                    return False
                if p[0] == '+' or p[0] == '-':
                    p = p[1:]
                if not p.isnumeric():
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()
    for s in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]:
        print(solution.isNumber(s))
    s = '.-4'
    print(solution.isNumber(s))
