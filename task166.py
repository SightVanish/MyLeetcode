"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0: return ''
        if numerator == 0: return '0'
        res = ''
        if numerator * denominator < 0: res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        # integer part
        res += str(numerator // denominator)
        remainder = numerator % denominator
        # fraction part
        if remainder:
            res += '.'
            remainder_dict = {} # record all remainder
            while remainder and remainder not in remainder_dict:
                # long division
                remainder_dict[remainder] = len(res)
                remainder *= 10
                res += str(remainder // denominator)
                remainder = remainder % denominator
            if remainder in remainder_dict: 
                res = res[:remainder_dict[remainder]] + '(' + res[remainder_dict[remainder]:] + ')'
        return res
    
s = Solution()
print(s.fractionToDecimal(numerator = 4, denominator = 333))