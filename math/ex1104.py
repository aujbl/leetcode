from numpy import log2
from typing import List

'''        // 2
        是找父节点，（）就是求label在这一行里的对称节点，label和它的对称节点sym_label之和为(2 ** row - 1 + 2 ** (row - 1))
        妙就妙在每个之字形label的父节点，就是label的sym_label在非之字形树里的父节点'''


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        row = int(log2(label))+1
        ans = [0]*row
        while row:
            ans[row-1] = label
            label = (2**row-1-label+2**(row-1))//2
            row -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    label = 12
    print(solution.pathInZigZagTree(label))