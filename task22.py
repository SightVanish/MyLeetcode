"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return ''
        res = []
        def generate(l, r, s):
            if l == 0:
                res.append(s.ljust(n*2, ')'))
                return
            if s[-1] == ')' and l == r:
                generate(l-1, r, s+'(')
            else:
                generate(l, r-1, s+')')
                generate(l-1, r, s+'(')
        generate(n-1, n, '(')
        return res
    
s = Solution()
print(s.generateParenthesis(1))





