from typing import List


class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(':')
        if '?' in h:
            if h == '??':
                h = '23'
            elif h[0] == '?':
                h = '2' + h[1] if int(h[1]) <= 3 else '1' + h[1]
            else:
                h = h[0] + '9' if int(h[0]) <= 1 else h[0] + '3'
        if m[0] == '?':
            m = '5' + m[1]
        if m[1] == '?':
            m = m[0] + '9'
        return h + ':' + m


if __name__ == '__main__':
    solution = Solution()
    time = "2?:?0"
    time = "0?:3?"
    time = "1?:22"
    print(solution.maximumTime(time))