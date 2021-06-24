from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if (m+1)%2 == 0:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m-1]:
                    r = m - 1
                else:
                    l = m + 1
        return nums[l-1]



if __name__ == '__main__':
    solution = Solution()
    nums = [3, 3, 5]
    print(solution.singleNonDuplicate(nums))
