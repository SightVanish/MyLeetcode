# 2-D Dynamic Programming - time complexity/space complexity: O(mn)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)] # dp[i][j] = True if s3[:i+j] can be presented via s1[:i] and s2[:j]
        dp[0][0] = True
        for i in range(1, m + 1): # only with s1
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]: dp[i][0] = True
        for j in range(1, n + 1): # only with s2
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]: dp[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]): dp[i][j] = True
        return dp[-1][-1]

# 1-D Dynamic Programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) > len(s2): s1, s2 = s2, s1 # make sure length of s1 <= length of s2
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        for i in range(1, m + 1): # only with s1
            if dp[i - 1] and s1[i - 1] == s3[i - 1]: dp[i] = True 
        # currently dp[i] is the dp[i][0] in the 2-D version
        for j in range(1, n + 1):
            # currently dp[j] is the dp[i-1][j] in the 2-D version
            if dp[0] and s2[j - 1] == s3[j - 1]: dp[0] = True
            else: dp[0] = False
            for i in range(1, m + 1):
                if (dp[i - 1] and s1[i - 1] == s3[i + j - 1]) or (dp[i] and s2[j - 1] == s3[i + j - 1]): dp[i] = True
                else: dp[i] = False
        return dp[-1]
                


s = Solution()
print(s.isInterleave(s1 = "a", s2 = "", s3 = "a"))
