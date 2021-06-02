from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_dict = {0:-1}
        pre = 0
        for i, num in enumerate(nums):
            pre += num
            key = pre % k
            if key in pre_dict:
                if i - pre_dict[key] > 1:
                    return True
            else:
                pre_dict[key] = i
        return False

if __name__ == '__main__':
    # nums = [23, 2, 4, 6, 7]
    k = 13
    nums = [23, 2, 6, 4, 7]
    solution = Solution()
    print(solution.checkSubarraySum(nums, k))