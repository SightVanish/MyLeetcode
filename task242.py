class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for i in s:
            if i in m: m[i] += 1
            else: m[i] = 1
        for i in t:
            if i in m: m[i] -= 1
            else: return False
        for i in m:
            if m[i] != 0: return False
        return True