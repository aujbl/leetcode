# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         costs.sort()
#         cnt = 0
#         for cost in costs:
#             if coins >= cost:
#                 coins -= cost
#                 cnt += 1
#             else:
#                 return cnt
#         return cnt


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost_dict = {}
        for cost in costs:
            if cost not in cost_dict:
                cost_dict[cost] = 0
            cost_dict[cost] += 1
        cnt = 0
        for cost in sorted(cost_dict.keys()):
            num = cost_dict[cost]
            if coins >= cost * num:
                coins -= cost * num
                cnt += num
            else:
                while coins >= cost:
                    coins -= cost
                    cnt += 1
                return cnt
        return cnt







