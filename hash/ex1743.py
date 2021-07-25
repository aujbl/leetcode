from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        nums_dict = {}
        for x, y in adjacentPairs:
            if x not in nums_dict:
                nums_dict[x] = [y]
            else:
                nums_dict[x].append(y)
            if y not in nums_dict:
                nums_dict[y] = [x]
            else:
                nums_dict[y].append(x)
        for key, value in nums_dict.items():
            if len(value) == 1:
                res = [key] + value
                break
        while len(nums_dict[res[-1]]) > 1:
            if nums_dict[res[-1]][0] == res[-2]:
                res.append(nums_dict[res[-1]][1])
            else:
                res.append(nums_dict[res[-1]][0])
        return res


if __name__ == '__main__':
    solution = Solution()
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    adjacentPairs = [[100000, -100000]]
    print(solution.restoreArray(adjacentPairs))
