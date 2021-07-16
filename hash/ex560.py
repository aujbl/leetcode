from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt_dict = {0: 1}
        pre = cnt = 0
        for num in nums:
            pre += num
            if pre - k in cnt_dict:
                cnt += cnt_dict[pre-k]
            if pre in cnt_dict:
                cnt_dict[pre] += 1
            else:
                cnt_dict[pre] = 1
        return cnt


if __name__ == '__main__':
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    solution = Solution()
    print(solution.subarraySum(nums, k))