from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        deadends = set(deadends)
        minus = ['9', '0', '1', '2', '3', '4', '5', '6', '7', '8']
        adds = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        def gen_new_key(key):
            keys = []
            for i in range(4):
                num = int(key[i])
                new = key[:i] + minus[num] + key[i+1:]
                keys.append(new)
                new = key[:i] + adds[num] + key[i+1:]
                keys.append(new)
            return keys

        last_dict = {'0000': 0}
        cnt = 0
        while cnt < 10:
            for key in last_dict.keys():
                cnt = last_dict[key]
                new_keys = gen_new_key(key)
                new_dict = {}
                for new_key in new_keys:
                    if new_key == target:
                        return cnt + 1
                    if new_key not in deadends and new_key not in new_dict:
                        new_dict[new_key] = cnt + 1
            last_dict = new_dict


        return -1


if __name__ == '__main__':
    solution = Solution()
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(solution.openLock(deadends, target))
