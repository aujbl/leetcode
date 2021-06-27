from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, flag = len(board), False
        process = []
        for i in range(n, 0, -1):
            temp = board[i-1]
            if flag:
                temp.reverse()
                flag = False
            else:
                flag = True
            process += temp
        next, cnt = [0], 0
        while next:
            next_next = []
            for pos0 in next:
                for plus in range(1, 7):
                    pos = pos0 + plus
                    if pos+1 == n*n:
                        return cnt+1
                    if process[pos] == -1:
                        next_next.append(pos)
                        process[pos] = 0
                    elif process[pos] > 0:
                        if process[pos] == n*n:
                            return cnt+1
                        next_next.append(process[pos]-1)
                        process[pos] = 0
            cnt += 1
            next = next_next
        return -1




if __name__ == '__main__':
    solution = Solution()
    # board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    print(solution.snakesAndLadders(board))