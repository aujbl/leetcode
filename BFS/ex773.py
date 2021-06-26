from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        str_b = ''
        for b in board:
            for s in b:
                str_b += str(s)
        if str_b == '123450':
            return 0
        seen = set()
        seen.add(str_b)
        exchange_list = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def exchange(str_board):
            chang_list = exchange_list[str_board.index('0')]
            new_strings = []
            for idx in chang_list:
                temp = str_board[idx]
                new_str = str_board.replace('0', '6')
                new_str = new_str.replace(temp, '0')
                new_str = new_str.replace('6', temp)
                new_strings.append(new_str)
            return new_strings

        cnt_strings = [str_b]
        cnt = 0
        while cnt_strings:
            new_cnt_strings = []
            for s in cnt_strings:
                new_strings = exchange(s)
                for new_string in new_strings:
                    if new_string == '123450':
                        return cnt+1
                    if new_string not in seen:
                        new_cnt_strings.append(new_string)
                        seen.add(new_string)
            cnt_strings = new_cnt_strings
            cnt += 1
        return -1





if __name__ == '__main__':
    solution = Solution()
    # board = [[1, 2, 3], [4, 0, 5]]
    # board = [[1, 2, 3], [5, 4, 0]]
    # board = [[4, 1, 2], [5, 0, 3]]
    board = [[3, 2, 4], [1, 5, 0]]
    print(solution.slidingPuzzle(board))

