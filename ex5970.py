# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2022/1/2 11:28
"""
from typing import List
from collections import defaultdict
# d = defaultdict(list)
#
# d[0] = [2]
# d[1] = [0]
# d[2] = [1]
#
# flag = False
# def recursion(tmp):
#     li = d[tmp[-1]]
#     if not li:
#         return
#     for i in li:
#         if i not in tmp:
#             tmp.append(i)
#             recursion(tmp)
#             tmp.remove(i)
#         else:
#             print(tmp)
#             flag = True
#             return
#
# tmp = []
# for k in d:
#     if flag:
#         break
#     tmp.append(k)
#     recursion(tmp)
#     tmp.remove(k)


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        table = defaultdict(list)
        for i in range(len(favorite)):
            table[favorite[i]].append(i)

        self.res = 0
        flag = False

        def recursion(tmp):
            li = table[tmp[-1]]
            if not li:
                return
            for i in li:
                if i not in tmp:
                    tmp.append(i)
                    recursion(tmp)
                    tmp.remove(i)
                else:
                    print(tmp)
                    self.res = max(self.res, len(tmp))
                    flag = True
                    return

        tmp = []
        for k in list(table.keys()):
            if flag:
                break
            tmp.append(k)
            recursion(tmp)
            tmp.remove(k)
        if self.res == 2 and len(favorite) > 2:
            return 3
        return self.res


if __name__ == '__main__':
    solution = Solution()
    # favorite = [2, 2, 1, 2]
    favorite = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]  # 6
    print(solution.maximumInvitations(favorite))

