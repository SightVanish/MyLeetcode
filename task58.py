class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b, e = 0, 0
        for i in range(len(s)):
            if s[i] != ' ':
                if i == 0 or s[i-1] == ' ': b = i
                if i == len(s)-1 or s[i+1] == ' ': e = i
        return e - b + 1
        
