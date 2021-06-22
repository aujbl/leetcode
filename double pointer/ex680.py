class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(ss):
            ll, rr = 0, len(ss)-1
            while ll < rr:
                if ss[ll] == ss[rr]:
                    ll += 1
                    rr -= 1
                else:
                    return False
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return palindrome(s[l+1:r+1]) or palindrome(s[l:r])
        return True




if __name__ == '__main__':
    solution = Solution()
    # s = "abcb"
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(solution.validPalindrome(s))
