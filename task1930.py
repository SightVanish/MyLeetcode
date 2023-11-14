"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for i in range(len(s)-2):
            if s[i] not in s[0:i]:
                for j in range(len(s)-1, i+1, -1):
                    if s[j] == s[i]: 
                        res += len(set(s[i+1:j]))
                        break
        return res

# using fancy gramma
# the built-in function find() is run in C speed, which is much more faster than a python for loop
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        unique = set(s)
        for i in unique:
            l, r = s.find(i), s.rfind(i)
            if r > l: res += len(set(s[l+1: r]))
        return res

s = Solution()
print(s.countPalindromicSubsequence("bbcbaba"))