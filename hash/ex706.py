# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:06:07 2021

@author: lee
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = []
        self.value = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.key:
            self.key.append(key)
            self.value.append(value)
        else:
            self.value[self.key.index(key)] = value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.key:
            return -1
        else:
            return self.value[self.key.index(key)]
        


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key not in self.key:
            pass
        else:
            self.value.pop(self.key.index(key))
            self.key.pop(self.key.index(key))



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)