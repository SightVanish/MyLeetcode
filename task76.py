"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""
import time
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(m, n):
            for i in m: 
                if m[i] > n[i]: return False
            return True 
        d= {}
        for i in t: d[i] = d[i]+1 if d.get(i) else 1
        r = {i:0 for i in d}
        i, j, p, q = 0, 0, -1, len(s)

        while i <= j and j < len(s):
            while not valid(d, r) and j < len(s):
                j += 1
                if s[j-1] in r: r[s[j-1]] += 1
            while valid(d, r) and i <= j:
                if q - p > j - i: p, q = i, j
                if s[i] in r: r[s[i]] -= 1
                i+= 1
        if p == -1: return "" 
        return s[p: q]





s = Solution()
print(s.minWindow('A', 'AA'))
