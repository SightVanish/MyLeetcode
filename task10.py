"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 or len(p) == 0: return False
        dp = [[0 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = 1
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i-1] == 1:
                # consider 'a*' as ''
                dp[0][i+1] = 1
        for i in range(0, len(s)):
            for j in range(0, len(p)):
                if s[i] == p[j] or p[j] == '.': dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if s[i] != p[j-1] and p[j-1] != '.': dp[i+1][j+1] = dp[i+1][j-1] # consider 'a*' as ''
                    # 'a*'='aa' or 'a*'='a' or 'a*'=''
                    else: dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1]
        return dp[-1][-1]

        
s = Solution()
print(s.isMatch('aa', 'a'))

exit()

        



# there are only 4 different situations in regular expression: 
# a, ., a*, .*
# one bundary: aaaaab, a*aab -> true
# how to decide? -> ignore and count the number of a and decide whether it is smaller then the given array
# so we should start from the regular expresssion instead of the given array
#--- too complicated and fail
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if len(p) >= 2 and p[1] == "*":
            if s and (p[0] == s[0] or p[0] == "."):
                return self.isMatch(s,p[2:]) or self.isMatch(s[1:],p)
            else:
                return self.isMatch(s,p[2:])
        if s and (p[0] == "." or p[0] == s[0]):
            return self.isMatch(s[1:],p[1:])
        return False

# Dynamic programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)] # dp[i][j] means whether the first i entries in s are matched with the j entries in p
        dp[0][0] = True # if s, p are null then always true
        for j in range(2, lp + 1): # init the first row 
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, ls + 1):
            for j in range(1, lp + 1): # step through dp[][]
                m, n = i - 1, j - 1
                if p[n] == '*':
                    if s[m] == p[n - 1] or p[n - 1] == '.': # which means that the entry before '*' is matched--either match or '.'
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else: dp[i][j] = dp[i][j - 2]
                elif s[m] == p[n] or p[n] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

# backtracking
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s # clever, if p is null the if s is null return true else return false
        if len(p) > 1 and p[1] == '*': # need to check the second value is * or not first
            if s and (p[0] == '.' or s[0] == p[0]): # if the value before * is matched, and we also need to make sure s is not null
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p) # two possibilities--if * just select nothing(no matter . or alpha) then we need to skip two entries in p; else we just move on 1 entris in s to see what will happen
            return self.isMatch(s, p[2:]) # if the entry before * is not matched, there can only be true if * select nothing
        if s and (p[0] == '.' or s[0] == p[0]): # we can make sure there is no * to disturb
            return self.isMatch(s[1:], p[1:]) #simply go on 
        return False #if somehing falls here, it must goes wrong


# s = Solution()
# a = "aaa"
# b = "ab*a*c*a"
# print(s.isMatch(a,b))
dp = [[10 for a in range(3 + 1)] for a in range(5 + 1)]
print(dp)


