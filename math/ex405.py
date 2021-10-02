class Solution:
    def toHex(self, num: int) -> str:
        bit_dict = {
            '0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
            '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'
        }
        if num < 0:
            num += 2 ** 31
            s = bin(num)[2:]
            s = s.zfill(31)
            s = '1' + s
        else:
            s = bin(num)[2:]
            bits = len(s) // 4
            bits = bits if len(s) % 4 == 0 else bits + 1
            s = s.zfill(4 * bits)
        res = ''
        for i in range(0, len(s), 4):
            bit = s[i:i+4]
            res += bit_dict[bit]
        return res

if __name__ == '__main__':
    solution = Solution()
    num = -1
    print(solution.toHex(num))