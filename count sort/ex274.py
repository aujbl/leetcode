from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        bigger, h = len(citations), 0
        for ci in citations:
            if bigger >= ci:
                h = ci
            else:
                h = max(h, bigger)
            if h >= bigger:
                return h
            bigger -= 1
        return h






if __name__ == '__main__':
    solution = Solution()
    citations = [1, 5, 100, 100, 100, 100]
    citations = [100]
    citations = [3,0,6,1,5]
    print(solution.hIndex(citations))