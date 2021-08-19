from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s
        l, r = 0, len(s)-1
        vowel = 'aeiouAEIOU'
        ans_l, ans_r = '', ''
        while l <= r:
            if s[l] in vowel and s[r] in vowel:
                ans_l = ans_l + s[r]
                if l < r:
                    ans_r = s[l] + ans_r
                l += 1
                r -= 1
            else:
                if s[l] not in vowel and l <= r:
                    ans_l = ans_l + s[l]
                    l += 1
                if s[r] not in vowel and l <= r:
                    ans_r = s[r] + ans_r
                    r -= 1
        return ans_l + ans_r


if __name__ == '__main__':
    solution = Solution()
    s = "..."
    # s = "leeticode"
    # s = ' '
    print(solution.reverseVowels(s))



