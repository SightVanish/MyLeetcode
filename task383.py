from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words = defaultdict(int)
        for w in magazine: words[w] += 1
        for w in ransomNote: words[w] -= 1
        for n in words.values():
            if n < 0: return False
        return True

s = Solution()
print(s.canConstruct('a', 'b'))