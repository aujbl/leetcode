from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict, need_cnt = {}, 0
        for tt in t:
            need_dict[tt] = (need_dict[tt]+1) if tt in need_dict else 1
        l = r = 0
        while l < len(s):
            if



if __name__ == '__main__':
    solution = Solution()

    print()
