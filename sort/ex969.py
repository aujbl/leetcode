from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n-1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]         # 将最大值翻转到第一位
            for i in range(n // 2):
                arr[i], arr[n-1-i] = arr[n-1-i], arr[i]         # 翻转全部元素
            ans.append(index + 1)
            ans.append(n)

        return ans


if __name__ == '__main__':
    solution = Solution()
    arr = [3, 2, 4, 1]
    print(solution.pancakeSort(arr))
