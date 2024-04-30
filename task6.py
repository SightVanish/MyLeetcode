class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        row = 0
        up = 0
        d = {i:[] for i in range(numRows)}
        for i in s:
            d[row].append(i)
            if up: row -= 1
            else: row += 1
            if row == 0: up = 0
            if row == numRows - 1: up = 1
        return ''.join([''.join(d[i]) for i in range(numRows)])

s = Solution()
print(s.convert(s = 'AB', numRows = 1))
