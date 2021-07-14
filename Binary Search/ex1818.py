import bisect
from typing import List

# wrong
# class Solution:
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         max_diff = res = 0
#         max_diff_dict = {}
#         for num1, num2 in zip(nums1, nums2):
#             diff = abs(num1-num2)
#             res += diff
#             if diff >= max_diff:
#                 max_diff = diff
#                 if max_diff not in max_diff_dict:
#                     max_diff_dict[max_diff] = [num2]
#                 else:
#                     max_diff_dict[max_diff] += [num2]
#
#         min_diff = res
#         for num in max_diff_dict[max_diff]:
#             for num1 in nums1:
#                 min_diff = min(min_diff, abs(num-num1))
#
#         return (res-max_diff+min_diff) % (10**9+7)
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        rec = nums1.copy()
        rec.sort()
        res = max_reduce = 0
        for num1, num2 in zip(nums1, nums2):
            diff = abs(num1-num2)
            res += diff
            idx = bisect.bisect_left(rec, num2)
            if idx == 0:
                min_diff = abs(num2-rec[idx])
            elif idx == len(rec):
                min_diff = abs(num2-rec[idx-1])
            else:
                min_diff = min(abs(num2-rec[idx-1]), abs(num2-rec[idx]))
            max_reduce = max(max_reduce, abs(diff-min_diff))
        return (res - max_reduce) % (10**9+7)




if __name__ == '__main__':
    solution = Solution()
    # nums1 = [1, 7, 5]
    # nums2 = [2, 3, 5]
    # nums1 = [2, 4, 6, 8, 10]
    # nums2 = [2, 4, 6, 8, 10]
    # nums1 = [1, 10, 4, 4, 2, 7]
    # nums2 = [9, 3, 5, 1, 7, 4]
    # nums1 = [1, 28, 21]
    # nums2 = [9, 21, 20]
    nums1 = [56, 51, 39, 1, 12, 14, 58, 82, 18, 41, 70, 64, 18, 7, 44, 90, 55, 23, 11, 79, 59, 76, 67, 92, 60, 80, 57, 11, 66,
     32, 76, 73, 35, 65, 55, 37, 38, 26, 4, 7, 64, 84, 98, 61, 78, 1, 80, 33, 5, 66, 32, 30, 52, 29, 41, 2, 21, 83, 30,
     35, 21, 30, 13, 26, 36, 93, 81, 41, 98, 23, 20, 19, 45, 52, 25, 51, 52, 24, 2, 45, 21, 97, 11, 92, 28, 37, 58, 29,
     5, 18, 98, 94, 86, 65, 88, 8, 75, 12, 9, 66]

    nums2 = [64, 32, 98, 65, 67, 40, 71, 93, 74, 24, 49, 80, 98, 35, 86, 52, 99, 65, 15, 92, 83, 84, 80, 71, 46, 11, 26, 70, 80,
     2, 81, 57, 97, 12, 68, 10, 49, 80, 24, 18, 45, 72, 33, 94, 60, 5, 94, 99, 14, 41, 25, 83, 77, 67, 49, 70, 94, 83,
     55, 17, 61, 44, 50, 62, 3, 36, 67, 10, 2, 39, 53, 62, 44, 72, 66, 7, 3, 6, 80, 38, 43, 100, 17, 25, 24, 78, 8, 4,
     36, 86, 9, 68, 99, 64, 65, 15, 42, 59, 79, 66]
    print(solution.minAbsoluteSumDiff(nums1, nums2))

