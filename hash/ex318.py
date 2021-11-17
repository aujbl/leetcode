# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/17 8:52
"""
from typing import List

 
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def w2num(w):
            num = ['0'] * 26
            for s in w:
                num[ord(s) - ord('a')] = '1'
            return int(''.join(num), 2)
        nums = {}
        for w in words:
            key = w2num(w)
            if key not in nums:
                nums[key] = len(w)
            else:
                nums[key] = max(nums[key], len(w))
        res = 0
        keys = list(nums.keys())
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                if keys[i] & keys[j] == 0:
                    res = max(res, nums[keys[i]] * nums[keys[j]])

        return res


if __name__ == '__main__':
    solution = Solution()
    words = ["a","aa","aaa","aaaa"]
    print(solution.maxProduct(words))

