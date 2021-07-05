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
                    if value > 1:
                        res += str(value)
            else:
                res = ''
                for key, value in cnt_dict.items():
                    res += key
                    res += str(value)
            return res

        left, result, j = [], '', 0
        while j < len_f:
            if formula[j] == '(':
                result += formula[j]
                left.append(len(result)-1)
            elif formula[j] == ')':
                num = 0
                while j+1 < len_f and formula[j+1].isdigit():
                    j += 1
                    num = num*10 + int(formula[j])
                if num == 0:
                    num = 1
                start = left.pop()+1
                process = atoms(result[start:], num, False)
                result = result[:start-1] + process
            else:
                result += formula[j]
            j += 1

        result = atoms(result, 1, True)
        return result


if __name__ == '__main__':
    solution = Solution()
    formula = "H2O"
    formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
    # formula = "K4(ON(SO3)2)2"
    print(solution.countOfAtoms(formula))
