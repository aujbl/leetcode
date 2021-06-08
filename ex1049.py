from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        result = {0}
        for stone in stones:
            new_res = set()
            for res in result:
                new_res.add(res+stone)
                new_res.add(res-stone)
            result = new_res
        res = min([res for res in result if res >= 0])
        return res

if __name__ == '__main__':
    # stones = [2, 7, 4, 1, 8, 1]
    # stones = [31, 26, 33, 21, 40]
    stones = [1, 2]
    solution = Solution()
    print(solution.lastStoneWeightII(stones))