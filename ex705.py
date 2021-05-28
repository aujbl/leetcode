# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 09:59:01 2021

@author: lee
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []


    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)


    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.pop(self.data.index(key))


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)