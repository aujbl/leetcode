from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        ans = 0
        while i <= j:
            if i == j or people[j] + people[i] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    people = [1, 2]
    limit = 3
    people = [3,5,3,4]
    limit = 5
    print(solution.numRescueBoats(people, limit))