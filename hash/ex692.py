# -*- coding: utf-8 -*-
"""
Created on Thu May 20 08:15:23 2021

@author: 95348
"""
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            if word not in count:
                count[word] = 0
            count[word] += 1
        return sorted(count.keys(), key = lambda key: (-count[key], key))[:k]


# for key in count.keys():
#     print('-count[key]: ', -count[key], 'key: ', key)