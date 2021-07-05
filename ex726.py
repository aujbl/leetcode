from typing import List


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        len_f = len(formula)

        def atoms(sub_formula: str, num: int, sort: bool):
            cnt_dict = {}
            i, len_s = 0, len(sub_formula)
            while i < len_s:
                digit, atom = 0, sub_formula[i]
                while i+1 < len_s and not sub_formula[i+1].isupper():
                    i += 1
                    if sub_formula[i].islower():
                        atom += sub_formula[i]
                    elif sub_formula[i].isdigit():
                        digit = digit*10 + int(sub_formula[i])
                if digit == 0:
                    digit = 1
                if atom in cnt_dict:
                    digit = digit + cnt_dict[atom]
                cnt_dict[atom] = digit
                i += 1
            if num > 1:
                for key, value in cnt_dict.items():
                    cnt_dict[key] = value*num
            if sort:
                cnt_dict = sorted(cnt_dict.items(), key=lambda x: x)
                res = ''
                for key, value in cnt_dict:
                    res += key
                    res += str(value)
            else:
                res = ''
                for key, value in cnt_dict.items():
                    res += key
                    res += str(value)
            return res

        sub_formula, j = '', 0
        while j < len_f:





        return res


if __name__ == '__main__':
    solution = Solution()
    formula = "H2OHC3"
    print(solution.countOfAtoms(formula))
