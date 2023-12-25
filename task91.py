"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0 for _ in s]
        if s[-1] == '0': dp[-2] = 1
        else: dp[-1] = 1
        dp.append(1)
        i = len(s) - 2
        while i >= 0:
            if s[i] == '0': dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if (s[i] == "1") or (s[i] == "2" and int(s[i + 1]) <= 6): dp[i] += dp[i+2]
            i -= 1
        return dp[0]


s = Solution()
print(s.numDecodings('27'))