"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, i, j = 0, 0, 0
        while j < len(s):
            if s[j] in s[i:j]: 
                i += 1
            else: 
                res = max(res, j - i + 1)
                j += 1
        return res

# keep tracking history
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = set()
        res = 0
        i, j  = 0, 0
        while j < len(s):
            while j < len(s) and s[j] not in history:
                res = max(res, j - i + 1)
                history.add(s[j])
                j += 1
            if j < len(s) and s[j] in history:
                while s[i] != s[j]: 
                    history.remove(s[i])
                    i += 1
                i += 1
                j += 1
        return res

# keep tracking history -- only track the index of the element
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in history or history[s[j]] < i:
                history[s[j]] = j
                res = max(res, j - i + 1)
            else: i = history[s[j]] + 1
            history[s[j]] = j
        return res


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))