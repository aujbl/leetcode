from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candi, cnt = -1, 0
        for num in nums:
            if cnt == 0:
                candi = num
            if candi == num:
                cnt += 1
            else:
                cnt -= 1
        cnt = 0
        for num in nums:
            if num == candi:
                cnt += 1
        if 2 * cnt > len(nums):
            return candi
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,5,9,5,9,5,5,5]
    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement(nums))
