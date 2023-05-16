"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

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



# class Solution:
#     def checkRepeating(self, s: str) -> bool:
#         if len(set(s)) < len(s):
#             return False
#         else:
#             return True

#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         i = 0
#         j = 1
#         minLength = j - i
#         while j <= len(s):
#             while self.checkRepeating(s[i:j]) and j <= len(s):
#                 minLength = max(minLength, j - i)
#                 print(minLength)
#                 j += 1
#             while not self.checkRepeating(s[i:j]) and i < j:
#                 i += 1
#         return minLength
            
            
s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))