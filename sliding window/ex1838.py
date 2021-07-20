from typing import List

# 超时
# class Solution:
    # def maxFrequency(self, nums: List[int], k: int) -> int:
    #     nums_dict = {}
    #     for num in nums:
    #         if num not in nums_dict:
    #             nums_dict[num] = 1
    #         else:
    #             nums_dict[num] += 1
    #     keys = sorted(nums_dict, key=lambda x: x, reverse=True)
    #     print('keys...')
    #     res = 0
    #     print('res... start...')
    #     for i, num in enumerate(keys):
    #         print('i%d, num%d' % (i, num))
    #         cnt, k1 = nums_dict[num], k
    #         while k1 > 0 and i < len(keys)-1:
    #             diff = num - keys[i+1]
    #             quo = k1 // diff
    #             if quo >= nums_dict[keys[i+1]]:
    #                 k1 -= diff*nums_dict[keys[i+1]]
    #                 cnt += nums_dict[keys[i+1]]
    #             else:
    #                 cnt += quo
    #                 k1 = -1
    #             i += 1
    #         res = max(res, cnt)
    #     return res
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        len_n = len(nums)
        l = total = 0
        res = 1
        for r in range(1, len_n):
            # total为差值和
            # 若最后一个值比前一个大b，计算差值和时每个差值都增加b
            total += (nums[r] - nums[r-1]) * (r-l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res, r-l+1)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 9, 6]
    k = 2
    nums = [1, 4, 8, 13]
    k = 5
    print(solution.maxFrequency(nums, k))