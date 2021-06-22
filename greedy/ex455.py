class Solution:
    def findContentChildren(self, children: List[int], cookies: list[int]) -> int:
        children.sort()
        cookies.sort()
        len_children, len_cookies = len(children), len(cookies)

        i = j = count = 0
        while i < len_children and j < len_cookies:
            while j < len_cookies and children[i] > cookies[j]:
                j += 1
            if j < len_cookies:
                count += 1
            i += 1
            j += 1

        return count