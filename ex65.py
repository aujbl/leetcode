class Solution:
    def isNumber(self, s: str) -> bool:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        e, flag = ['e', 'E'], ['-', '+']
        cnt_e = 0
        if s[0] in flag:
            s = s[1:]
        if s[0] in e or s == '.':
            return False
        s = s.replace('E', 'e')
        s = s.replace('e-', 'e')
        s = s.replace('e+', 'e')
        i = 0
        while i < len(s):
            if s[i] in nums:
                pass
            elif s[i] == '.':
                if cnt_e > 0:
                    return False
                i += 1
                while i < len(s):
                    if s[i] in nums:
                        pass
                    elif s[i] in e:
                        if i == len(s)-1:
                            return False
                        else:
                            if s[i-1] not in nums and s[i-1] != '.':
                                return False
                            if s[i+1] not in nums:
                                return False
                        cnt_e += 1
                    else:
                        return False
                    if cnt_e > 1:
                        return False
                    i += 1
                return True
            elif s[i] in e:
                if i == len(s) - 1:
                    return False
                else:
                    if s[i-1] not in nums and s[i-1] != '.':
                        return False
                    if s[i+1] not in nums:
                        return False
                cnt_e += 1
            else:
                return False
            if cnt_e > 1:
                return False
            i += 1
        return True


if __name__ == '__main__':
    is_num = ["46.e3", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    # is_num = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    solution = Solution()
    for num in is_num:
        print(solution.isNumber(num))
