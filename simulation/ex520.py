# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/11/13 9:20
"""
from typing import List

 
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        n = len(word)
        if word[0].isupper():
            if word[1].isupper():
                for w in word[2:]:
                    if w.isupper():
                        pass
                    else:
                        return False
            else:
                for w in word[2:]:
                    if w.islower():
                        pass
                    else:
                        return False
        else:
            for w in word[1:]:
                if w.islower():
                    pass
                else:
                    return False
        return True



if __name__ == '__main__':
    solution = Solution()
    print(solution)

