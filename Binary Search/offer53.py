class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1] or target < nums[0]:
            return 0

        def left(flag=True):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if flag:
                    if nums[mid] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return l
        return left(False) - left()