"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""
class Solution:
    def maxScore(self, s: str) -> int:
        l, r = 0, s.count('1')
        res = 0
        for i in range(0, len(s)-1):
            if s[i] == '0': l += 1
            else: r -= 1
            res = max(res, l + r)
        return res

s = Solution()
print(s.maxScore("1111"))
