# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:50:03 2021

@author: lee
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        temp = nums1[0:m]
        idx = i = j = 0
        while idx < m+n:
            if i == m:
                nums1[idx:] = nums2[j::]
                idx = m+n
            elif j == n:
                nums1[idx:] = temp[i:]
                idx = m+n
            else:    
                if temp[i] <= nums2[j]:
                    nums1[idx] = temp[i]
                    i += 1
                else:
                    nums1[idx] = nums2[j]
                    j += 1
                idx += 1

            