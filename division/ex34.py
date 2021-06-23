from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        def division(op):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] == target:
                    if op == 0:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    l = mid + 1
            if op == 0:
                return l if nums[l] == target else -1
            else:
                return r
        left = division(0)
        return [-1, -1] if left == -1 else [left, division(1)]


if __name__ == '__main__':
    solution = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    target = 6
    nums = []
    print(solution.searchRange(nums, target))
