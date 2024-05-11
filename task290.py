class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            if pattern.find(pattern[i]) != s.index(s[i]): return False
        return True
    

s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))