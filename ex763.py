# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:54:07 2021

@author: lee
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        dic = {x: S.count(x) for x in set(S)}
        count_dic = {}
        result = []
        last_sum = 0
        
        for s in S:
            try:
                count_dic[s] += 1
            except:
                count_dic[s] = 1
            keys = count_dic.keys()
            difference = [dic[key] - count_dic[key] for key in keys]
            if sum(difference) == 0:
                result.append(sum(count_dic.values()) - last_sum)
                last_sum = sum(count_dic.values())
        return result
                
                
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {x: S.count(x) for x in set(S)}      
        result = []
        last_sum = sum(dic.values())
        keys = set()
        for s in S:
            keys.add(s)
            dic[s] -= 1
            if dic[s] == 0:
                difference = [dic[key] for key in keys]
                if sum(difference) == 0:
                    result.append(last_sum - sum(dic.values()))
                    last_sum = sum(dic.values())
                    [dic.pop(idx) for idx in keys]
                    keys = set()
        return result