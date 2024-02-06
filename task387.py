"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m, n = [], []
        for i in s:
            if i in m: n.append(i)
            else: m.append(i)
        for i in m:
            if i not in n: return s.find(i)
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))