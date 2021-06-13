from typing import List
# 超出时间限制
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        result = [(0, 0)]
        for g, p in zip(group, profit):
            new_result = []
            for peo, pro in result:
                new_result.append((peo, pro))
                if peo + g <= n:
                    new_result.append((peo+g, pro+p))
            result = new_result
        cnt = 0
        for res in result:
            if res[1] >= minProfit:
                cnt += 1
        return cnt % (10**9+7)

if __name__ == '__main__':
    # n = 5
    # minProfit = 3
    # group = [2, 2]
    # profit = [2, 3]
    n = 10; minProfit = 5; group = [2, 3, 5]; profit = [6, 7, 8]
    solution = Solution()
    print(solution.profitableSchemes(n, minProfit, group, profit))


