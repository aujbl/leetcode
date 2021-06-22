from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def found(ss):
            if len(ss) > len(s):
                return False
            i = j = 0
            while i < len(s) and j < len(ss):
                if s[i] == ss[j]:
                    j += 1
                i += 1
            return j == len(ss)
        res = ''
        for dic in dictionary:
            if found(dic):
                if len(dic) > len(res):
                    res = dic
                elif len(dic) == len(res):
                    res = min(res, dic)
                else:
                    pass
        return res



if __name__ == '__main__':
    solution = Solution()
    # s = "abpcplea"
    # dictionary = ["ale", "apple", "monkey", "plea"]
    s = "abpcplea"
    dictionary = ["a", "b", "c"]
    # s = "abce"
    # dictionary = ["abe", "abc"]
    print(solution.findLongestWord(s, dictionary))
