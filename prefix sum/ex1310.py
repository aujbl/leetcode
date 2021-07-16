# -*- coding: utf-8 -*-
"""
Created on Wed May 12 08:12:55 2021

@author: 95348
"""
from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preprocess = [arr[0]]
        for a in arr[1:]:
            preprocess.append(preprocess[-1] ^ a)
        res = []
        for query in queries:
            if query[0] == query[1]:
                res.append(arr[query[0]])
            elif query[0] == 0:
                res.append(preprocess[query[1]])
            else:
                res.append(preprocess[query[0]-1] ^ preprocess[query[1]])
        return res