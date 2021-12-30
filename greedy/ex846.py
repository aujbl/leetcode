from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        cnt_dict = Counter(hand)
        for x in hand:
            if cnt_dict[x] == 0:
                continue
            for i in range(x, x+groupSize):
                if cnt_dict[i] == 0:
                    return False
                cnt_dict[i] -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    hand = [1, 2, 3, 4, 5]
    groupSize = 4
    print(solution.isNStraightHand(hand, groupSize))
