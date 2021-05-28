# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:59:52 2021

@author: lee
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        len_a = len(answers)
        i = res = cnt = 0
        while i < len_a:
            cnt = answers[i]
            res += (cnt + 1)
            if i+cnt+1 < len_a and answers[i+cnt+1] == cnt:
                i = i+cnt+1
            else:
                while i < len_a and answers[i] == cnt:
                    i += 1
        return res
            
            