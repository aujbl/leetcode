from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_dict = {0: 1}
        for num in nums:
            new_dict = {}
            for key in sum_dict.keys():
                if (key+num) in new_dict:
                    new_dict[key+num] += sum_dict[key]
                else:
                    new_dict[key+num] = sum_dict[key]
                if (key-num) in new_dict:
                    new_dict[key-num] += sum_dict[key]
                else:
                    new_dict[key-num] = sum_dict[key]
            sum_dict = new_dict
        if target not in sum_dict:
            return 0
        return sum_dict[target]

if __name__ == '__main__':
    nums = [1]
    target = 2
    solution = Solution()
    print(solution.findTargetSumWays(nums, target))