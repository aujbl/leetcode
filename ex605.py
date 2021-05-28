# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:38:01 2021

@author: lee
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        len_f = len(flowerbed)
        if len_f == 1:
            if flowerbed[0] == 0:
                n -= 1
                if n == 0:
                    return True
            return False
        else:
            for i in range(len_f):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1 
                        n -= 1
                elif i == len_f-1:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1
                if n == 0:
                    return True
            return False
        


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        flowerbed = [0] + flowerbed +[0]
        len_f = len(flowerbed)
        i = 1
        while i < len_f-1:
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        i += 2
                        n -= 1
                    else:
                        i += 3
                else:
                    i += 1
            else:
                i += 2
            if n == 0:
                return True
        return False

                
        