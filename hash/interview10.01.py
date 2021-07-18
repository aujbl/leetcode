from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            idx = ''.join(sorted(s, key=lambda x: x))
            if idx not in res:
                res[idx] = [s]
            else:
                res[idx].append(s)
        return list(res.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
