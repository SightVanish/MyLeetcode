"""
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same.
A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def countHomogenous(self, s: str) -> int:
        before = 0
        res = 0
        for i in range(1, len(s)):
            if s[i] != s[before]:
                res += (i - before) * (i - before + 1) // 2
                before = i
        return (res + (len(s) - before) * (len(s) - before + 1) // 2) % (10 ** 9 + 7)
    
s = Solution()
print(s.countHomogenous("abbcccaa"))