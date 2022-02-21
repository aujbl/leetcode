class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        n, i, left = len(s), 0, 'L'
        while i < n:
            j = i
            while j < n and s[j] == '.':
                j += 1
            right = s[j] if j < n else 'R'
            if left == right:
                while i < j:
                    s[i] = right
                    i += 1
            elif left == 'R' and right == 'L':
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1

        return ''.join(s)
