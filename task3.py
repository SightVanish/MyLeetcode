class Solution:
    def checkRepeating(self, s: str) -> bool:
        if len(set(s)) < len(s):
            return False
        else:
            return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 1
        minLength = j - i
        while j <= len(s):
            while self.checkRepeating(s[i:j]) and j <= len(s):
                minLength = max(minLength, j - i)
                print(minLength)
                j += 1
            while not self.checkRepeating(s[i:j]) and i < j:
                i += 1
        return minLength
            
            
s = Solution()
print(s.lengthOfLongestSubstring("au"))