import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        s = list(s)
        s.sort()
        # heapq.heapify(s)
        res = [s.pop()]
        k = 1
        drop = []
        while s:
            if res[-1] == s[-1]:
                while s and s[-1] == res[-1] and k < repeatLimit:
                    res.append(s.pop())
                    k += 1

                drop = []
                while s and s[-1] == res[-1]:
                    drop.append(s.pop())
            else:
                res.append(s.pop())
                k = 1
                if drop:
                    s = s + drop
                    drop = []
                # for ch in drop:
                #     heapq.heappush(s, ch)
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    # s = 'cczazcc'
    # s = 'aababab'
    s = 'bbbbbbbbbbaaaaaaaaaaaaaaaa'
    print(solution.repeatLimitedString(s, 1))
