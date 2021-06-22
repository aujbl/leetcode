from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sale = prices[0]
        res = 0
        for price in prices[1:]:
            if price >= sale:
                sale = price
            else:
                res += (sale - buy)
                buy = sale = price
        res += (sale - buy)
        return res


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    # prices = [1, 2, 3, 4, 5]
    print(solution.maxProfit(prices))
