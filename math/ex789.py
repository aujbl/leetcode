from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            d = abs(x - target[0]) + abs(y - target[1])
            if d <= dis:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
    ghosts = [[1,9],[2,-5],[3,8],[9,8],[-1,3]]
    target = [8,-10]
    print(solution.escapeGhosts(ghosts, target))


