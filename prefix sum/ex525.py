from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_dict = {0:-1}
        pre = res = 0
        for i, num in enumerate(nums):
            if num == 1:
                pre += 1
            else:
                pre -= 1
            if pre not in pre_dict:
                pre_dict[pre] = i
            else:
                res = max(res, i-pre_dict[pre])
        return res

if __name__ == '__main__':
    nums = [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    solution = Solution()
    print(solution.findMaxLength(nums))
