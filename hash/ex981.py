from typing import List


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [[0, timestamp], ['', value]]
        else:
            self.data[key][0].append(timestamp)
            self.data[key][1].append(value)

    def check(self, nums: List, target: int) -> int:
        l, r = 1, len(nums) - 1
        if target >= nums[r]:
            return r
        if target < nums[l]:
            return 0
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        idx = self.check(self.data[key][0], timestamp)
        return self.data[key][1][idx]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == '__main__':
    solution = Solution()
    inputs = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    inputs = [[], ["foo", "bar", 1], ["foo", 1],
                ["foo", 3], ["foo", "bar2", 4],
                ["foo", 4], ["foo", 5]]
    # ["TimeMap", "set", "set", "get", "set", "get", "get"]
    # [[], ["a", "bar", 1], ["x", "b", 3], ["b", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    print()
