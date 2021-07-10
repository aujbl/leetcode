from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        small = min(nums1[0], nums2[0])
        idx, i = (m+n) // 2, 0
        while i < idx:
            if




if __name__ == '__main__':
    solution = Solution()
    print()
