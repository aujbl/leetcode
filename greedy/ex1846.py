from typing import List

# sort + greedy
# class Solution:
#     def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
#         arr.sort()
#         arr[0] = i = 1
#         while i < len(arr):
#             if arr[i] > arr[i-1]+1:
#                 arr[i] = arr[i-1]+1
#             i += 1
#         return arr[-1]
# count sort + greedy
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        len_a = len(arr)
        cnt = [0] * len_a
        for a in arr:
            cnt[min(a, len_a)-1] += 1
        miss = 0
        for count in cnt:
            if count == 0:
                miss += 1
            else:
                miss = miss - count + 1 if miss >= count else 0
        return len_a-miss


if __name__ == '__main__':
    solution = Solution()
    arr = [2, 2, 1, 2, 1]
    arr = [100, 1, 1000]
    arr = [1, 2, 3, 4, 5]
    arr = [100]
    arr = [1, 2, 2, 4]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr))


