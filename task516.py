"""
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        if s[0] == s[-1]: return 2 + self.longestPalindromeSubseq(s[1:-1])
        else: return max(self.longestPalindromeSubseq(s[1:]), self.longestPalindromeSubseq(s[:-1]))

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1): # i: len(s)-1 -> 0
            dp[i][i] = 1
            for j in range(i+1, len(s)): # j: i+1 -> len(s)-1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # dp[i+1][j], dp[i][j-1] are computed before
        return dp[0][-1]
            
















s = Solution()
print(s.longestPalindromeSubseq('bbbab'))


