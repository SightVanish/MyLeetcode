from typing import List
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1 for _ in range(len(s))]
        wordDict = set(wordDict)
        n = max([len(i) for i in wordDict])
        def segment(i):
            if s[:i + 1] in wordDict: dp[i] = True
            elif dp[i] == -1:
                for j in range(n):
                    if s[i - j: i + 1] in wordDict and segment(i - j - 1):
                        dp[i] = True
                        break
            # print(i, dp)
            return dp[i] if dp[i] != -1 else False
        segment(len(s) - 1)
        return False if dp[-1] == -1 else dp[-1]
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True 
        wordDict = set(wordDict)
        n = max([len(i) for i in wordDict])
        for i in range(len(s)):
            for j in range(min(i + 1, n)):
                if dp[i - j] and s[i - j: i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[-1]

s = Solution()
print(s.wordBreak("a", ["aa","aaa","aaaa","aaaaa","aaaaaa"]))
