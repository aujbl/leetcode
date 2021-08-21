from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = ans = 0
        while i < n:
            j = i
            last_c = chars[i]
            while j < n and chars[j] == last_c:
                j += 1
            if j - i == 1:
                chars[ans] = last_c
            else:
                chars[ans] = last_c
                char = list(str(j-i))
                chars[ans+1:ans+1+len(char)] = char
                ans += len(char)
            ans += 1
            i = j
        return ans


if __name__ == '__main__':
    solution = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    chars = ["a"]
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    chars = ["a", "a", "b", "b", "c", "c", "c", "&", "a", "z", "0"]
    print(solution.compress(chars))