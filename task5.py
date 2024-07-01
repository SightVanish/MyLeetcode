# expand on each node
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
    
# 2-D Dynamic Programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] # dp[i][j] = True if s[i:j+1] is palindromic
        l, r = 0, 0
        for j in range(len(s)):
            dp[j][j] = True # s[j:j+1] must be palindromic
            for i in range(j): # s[i:j+1], i < j
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]): 
                    dp[i][j] = True
                    if j - i > r - l: l, r = i, j
        return s[l: r + 1] 