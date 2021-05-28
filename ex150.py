# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 08:41:42 2021

@author: lee
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                right = nums.pop()
                left = nums.pop()
                nums.append(left+right)
            elif token == '-':
                right = nums.pop()
                left = nums.pop()
                nums.append(left-right)
            elif token == '*':
                right = nums.pop()
                left = nums.pop()
                nums.append(left*right)
            elif token == '/':
                right = nums.pop()
                left = nums.pop()
                nums.append(int(left/right))
            else:
                nums.append(int(token))
        return nums.pop()