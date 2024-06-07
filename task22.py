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

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate(s, l, r): # s: current string, l: number of left parenthesis, r: number of right parenthesis
            if len(s) == 2 * n: output.append(s)
            else:
                if l < n: generate(s + '(', l + 1, r)
                if r < l: generate(s + ')', l, r + 1)
        generate('', 0, 0)
        return output
    
s = Solution()
print(s.generateParenthesis(1))





