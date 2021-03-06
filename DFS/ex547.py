from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def findConnected(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    findConnected(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0
        for i in range(provinces):
            if i not in visited:
                findConnected(i)
                circles += 1
        return circles
