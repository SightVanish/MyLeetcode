"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(':')', '[':']', '{': '}'}
        l = []
        for i in s: 
            if i in bracket:
                l.append(bracket[i])
            else:
                if l:
                    t = l.pop()
                    if t != i:
                        return False
                else:
                    return False

        if l:
            return False
        else: 
            return True

class Solution:
    def isValid(self, s: str) -> bool:
        p = {']': '[', ')': '(', '}': '{'}
        stack = []
        for i in s:
            if i in ['[', '(', '{']: stack.append(i)
            else:
                if len(stack) == 0 or p[i] != stack[-1]: return False
                stack.pop()
        return len(stack) == 0
        
s = Solution()
print(s.isValid("()[]{}"))

