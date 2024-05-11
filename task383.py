class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words = {}
        for w in ransomNote:
            if w in words: words[w] += 1
            else: words[w] = 1
        for w in magazine:
            if w in words: words[w] -= 1
        for w in words:
            if words[w] > 0: return False
        return True