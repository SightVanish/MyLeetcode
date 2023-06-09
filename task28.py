"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = hash(needle)
        for i in range(len(haystack)-len(needle) + 1):
            if hash(haystack[i: i+len(needle)]) == h:
                return i
        return -1
    
s = Solution()
print(s.strStr(haystack = "a", needle = "a"))
