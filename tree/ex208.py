# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 07:37:20 2021

@author: lee
"""

# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = set()


#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         if word not in self.data:
#             self.data.add(word)


#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         return word in self.data


#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         len_p = len(prefix)
#         for word in self.data:
#             if len(word) < len_p:
#                 pass
#             else:
#                 if word[:len_p] == prefix:
#                     return True
#         return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for alp in prefix:
            alp = ord(alp) - ord('a')
            if not node.children[alp]:
                return None
            node = node.children[alp]
        return node
        
    def insert(self, word: str) -> None:
        node = self
        for alp in word:
            alp = ord(alp) - ord('a')
            if not node.children[alp]:
                node.children[alp] = Trie()
            node = node.children[alp]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None











































