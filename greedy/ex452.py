# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:35:15 2021

@author: lee
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0       
        
        def findArrow(start):
            arrow = points[start][1]
            while start < len_p and  arrow >= points[start][0]:
                arrow = min(arrow, points[start][1])
                start += 1
            return arrow, start
                 
        len_p = len(points)
        points.sort()
        i = count = 0     
        arrow = findArrow(i)
        while i < len_p:
            if points[i][0] <= arrow <= points[i][1]:
                count += 1
                while i < len_p and points[i][0] <= arrow <= points[i][1]:
                    i += 1
            else:
                arrow, i = findArrow(i)
                
        return count
    
        
                
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0       
        len_p = len(points)
        points.sort()
        count = 1
        i = 0
        arrow = points[i][1]
        while i < len_p:
            if arrow >= points[i][0]:
                arrow = min(arrow, points[i][1])
                i += 1
            else:
                count += 1
                arrow = points[i][1]
        
        len_p = len(points)
        points.sort()
        count = 1
        i = 0
        arrow = points[i][1]        
        for i in range(len_p):
            if arrow >= points[i][0]:
                arrow = min(arrow, points[i][1])
            else:
                count += 1
                arrow = points[i][1]
        
        
        return count
      
     

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1
        
        return ans




































