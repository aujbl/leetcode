# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 08:07:29 2021

@author: lee
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        i = 0
        while i < len(haystack):
            j = 0
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i-j
            elif needle[0] in haystack[i-j+1:i+1]:
                i = i-j+1
                while haystack[i] != needle[0]:
                    i += 1
            else:
                i += 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    haystack = ""
    needle = ""
    print(solution.strStr(haystack, needle))