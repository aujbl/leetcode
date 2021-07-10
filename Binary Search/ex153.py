class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]
        len_n = len(nums)
        l, r = 0, len_n-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] - nums[l] > 0:
                l = mid
            else:
                r = mid
        return nums[l+1]