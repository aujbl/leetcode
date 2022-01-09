# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2022/1/9 12:04
"""
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def wordtonum(word):
            num = ['0'] * 26
            for w in word:
                num[ord(w) - ord('a')] = '1'
            num = ''.join(num)
            return int(num, 2)

        start_nums = [wordtonum(w) for w in startWords]
        # start_nums = set(start_nums)
        target_nums = [wordtonum(w) for w in targetWords]

        res = 0
        for i in range(len(target_nums)):
            num = target_nums[i]
            if num in start_nums:
                # res += 1
                continue
            else:
                for j in range(len(start_nums)):
                    mod = start_nums[j]
                    if num & mod == mod and len(targetWords[i]) == len(startWords[j])+1:
                        # w = startWords[j]
                        # if w == targetWords[i][:len(w)]:
                        res += 1
                        break
        return res


if __name__ == '__main__':
    solution = Solution()
    startWords = ["ant", "act", "tack"]
    targetWords = ["tack", "act", "acti"]
    print(solution.wordCount(startWords, targetWords))

