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
        i = j = 0
        while i < m+j and j < n:
            if nums1[i] >= nums2[j]:
                nums1[i+1:m+1+j] = nums1[i:m+j]
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1
        nums1[m+j:] = nums2[j:]

            