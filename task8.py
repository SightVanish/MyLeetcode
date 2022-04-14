
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:
# Input: "42"
# Output: 42

# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

import re # import the library of regular expression
# code with regular expression--really fast and simpl
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

# more explaining
class Solution_ex:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip(' ')   # remove the ' ' in the head of string
        num_re = re.compile(r'^[\+\-]?\d+') # set the rules for regular expression
        # 
        num = num_re.findall(str)
        num = int(*num)
        return max(min(num,INT_MAX),INT_MIN)    # since python won't crash for the size of int we need to check it manually

# regular solution
class Solution_re:
    def myAtoi(self, str: str) -> int:
        numdic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        i = 0
        # 跳过前面的空白
        while i < len(str) and str[i] == ' ':
            i += 1
        # 判断异常转换情况
        if i >= len(str) or (str[i] not in numdic and str[i] not in ('+','-')):
            return 0
        # 判断正负性
        sign = 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        # 提取数
        num = 0
        boundry = (1<<31)-1 if sign > 0 else 1<<31
        # 注意先判断索引，以防越界
        while i < len(str) and str[i] in numdic:
            num = num *10 + numdic[str[i]]
            i += 1
            if num > boundry:
                return sign * boundry
        return sign * num



t = Solution_ex()
string = input()
print(string)
t.myAtoi(string)
