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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = {}
        for character in t:
            dict_t[character] = dict_t.get(character, 0) + 1
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# test upload
s = Solution()
print(s.minWindow('A', 'AA'))
