# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:51:23 2021

@author: lee
"""
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        len_w = len(wall)
        res = {}
        for bricks in wall:
            line = 0
            for brick in bricks[:-1]:
                line += brick
                if line not in res.keys():
                    res[line] = 1
                else:
                    res[line] += 1
        if not res.values():
            gap = 0
        else:
            gap = max(res.values())
        return len_w - gap