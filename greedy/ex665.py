class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        len_n = len(nums)
        i = cnt = 0
        while i < len_n-1:
            if nums[i] <= nums[i+1]:
                i += 1
            else:
                if i < len_n-2 and nums[i+2] > nums[i]:
                    nums[i+1] = nums[i]
                    cnt += 1
                elif i < len_n-2 and nums[i+2] <= nums[i]:
                    nums[i] = nums[i+1]
                    cnt += 1
                if 0 < i:
                    i -= 1
                while i < len_n-1:
                    if nums[i] <= nums[i+1]:
                        i += 1
                    else:
                        cnt += 1
                        i += 1
        return cnt <= 1

# 面向bug编程。。。。
# 注意：[3, 4, 2, 3], [5, 7, 1, 8], [1, 2, 4, 5, 3]
