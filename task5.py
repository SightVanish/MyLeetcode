"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1; j += 1
            return i+1, j-1
        for p in range(len(s)-1):
            i, j = expand(p, p)
            l, r = (i, j) if j - i > r - l else (l, r)
            i, j = expand(p, p+1)
            l, r = (i, j) if j - i > r - l else (l, r)
        return s[l:r+1]