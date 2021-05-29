from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum( nums: List[int], k: int) -> int:
            cnt_dict = {0: 1}
            pre = cnt = 0
            for num in nums:
                pre += num
                if pre - k in cnt_dict:
                    cnt += cnt_dict[pre - k]
                if pre in cnt_dict:
                    cnt_dict[pre] += 1
                else:
                    cnt_dict[pre] = 1
            return cnt
        res, len_n = 0, len(matrix[0])
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)+1):
                if j - i == 1:
                    nums = matrix[i]
                else:
                    for k in range(len_n):
                        nums[k] += matrix[j-1][k]
                # nums = [0] * len(matrix[0])
                # for k in range(len(matrix[0])):
                #     for rows in matrix[i:j]:
                #         nums[k] += rows[k]
                res += subarraySum(nums, target)
        return res


if __name__ == '__main__':
    # matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    matrix = [[1, -1], [-1, 1]]
    target = 0
    # matrix = [[904]]
    solution = Solution()
    print((solution.numSubmatrixSumTarget(matrix, target)))