from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for i, p in enumerate(people):
            if i > p[1]:
                res.insert(p[1], p)
            else:
                res.append(p)
        return res



if __name__ == '__main__':
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(solution.reconstructQueue(people))
