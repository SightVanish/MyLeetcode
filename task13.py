"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == 'I' and s[i+1] in 'VX': res -= 1
            elif i < len(s) - 1 and s[i] == 'X' and s[i+1] in 'LC': res -= 10
            elif i < len(s) - 1 and s[i] == 'C' and s[i+1] in 'DM': res -= 100
            else: res += symbols[s[i]]
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        for i in range(0,len(s)):
            result += dic[s[i]]
            if i < len(s)-1 and s[i] == "I":
                if s[i+1] == "X" or s[i+1] == "V":
                    result -= 2*dic[s[i]]
            if i < len(s)-1 and s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    result -= 2*dic[s[i]]
            if i < len(s)-1 and s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    result -= 2*dic[s[i]]
        return result

s = Solution()
i = "LVIII"
print(s.romanToInt(i))