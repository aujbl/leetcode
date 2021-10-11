# -*- coding: utf-8 -*-

"""
@author: jbl
@time: 2021/10/11 8:58
"""
from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        en_dict = {
            0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
            16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
            20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
            60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
            100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'
        }

        def partWords(n: int):
            res = []
            while n > 0:
                if n >= 100:
                    res.append(en_dict[n // 100])
                    res.append(en_dict[100])
                    n %= 100
                elif n > 19:
                    res.append(en_dict[n//10*10])
                    n %= 10
                else:
                    res.append(en_dict[n])
                    n = 0
            return res

        res = []
        if num < 21:
            res.append(en_dict[num])
        else:
            while num > 0:
                if num >= 1000000000:
                    res.append(en_dict[num // 1000000000])
                    res.append(en_dict[1000000000])
                    num %= 1000000000
                elif num >= 1000000:
                    res = res + partWords(num // 1000000)
                    res.append(en_dict[1000000])
                    num %= 1000000
                elif num >= 1000:
                    res = res + partWords(num // 1000)
                    res.append(en_dict[1000])
                    num %= 1000
                else:
                    res = res + partWords(num)
                    num = 0
        return ' '.join(res)


if __name__ == '__main__':
    solution = Solution()
    num = 1000000000
    print(solution.numberToWords(num))



