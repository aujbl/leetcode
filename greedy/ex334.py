from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first, second = nums[0], float('inf')
        for num in nums[1:]:
            if num > second:
                return True
            elif first < num < second:
                second = num
            elif num < first:
                first = num
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [5,1,5,5,2,5,4]
    nums = [1,2,3,4,5]
    nums = [5, 4, 3, 2, 1]
    nums = [2, 1, 5, 0, 4, 6]
    nums = [1, 2 ,4]
    print(solution.increasingTriplet(nums))
