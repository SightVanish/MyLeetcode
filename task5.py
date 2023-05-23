"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

class Solution:
    def getPalindrome(self, s, i, j):
        # expand palindromic string from i<-center->j
        while i >=0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-1 # you can not return i, j here
    def longestPalindrome(self, s: str) -> str:
        i, j = 0, 0
        for center in range(len(s)):
            # there are two situation for Palindrome
            l1, r1 = self.getPalindrome(s, center, center) # odd palindromic string
            l2, r2 = self.getPalindrome(s, center, center+1) # even palindromic string
            # keep track of the longest palindromic string
            if r1-l1 > j-i:
                i, j = l1, r1
            if r2-l2 > j-i:
                i, j = l2, r2
        return s[i:j+1] # note: j+1 here


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1
        l, r = 0, 0
        for pivot in range(len(s) - 1):
            l1, r1 = expand(pivot, pivot)
            l2, r2 = expand(pivot, pivot + 1)
            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2
        return s[l: r+1]

