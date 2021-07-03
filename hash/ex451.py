from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ss in s:
            if ss not in freq:
                freq[ss] = 1
            else:
                freq[ss] += 1
        sort = sorted(freq, key=lambda s0: freq[s0], reverse=True)
        res = ''
        for s in sort:
            res += freq[s]*s
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "Aabb"
    print(solution.frequencySort(s))
