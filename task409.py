"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = []
        res = 0
        for i in s:
            if i in l:
                res += 2
                l.remove(i)
            else:
                l.append(i)
        if l:
            res += 1
        return res

