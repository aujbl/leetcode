# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:42:42 2021

@author: lee
"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        len_p = len(pairs)
        visited = [False] * len_p
        Union = []
        
        def findUnion():
            i, union = 0, set()
            while i < len_p and not visited[i]:
                if not union:
                    union = set(pairs[i])
                else:
                    pass
                    
                    
            
            