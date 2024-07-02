"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, d, m, n = [], {}, len(s), len(p)
        if n > m : return []
        for i in p:
            if i in d: d[i] += 1
            else: d[i] = 1
        for i in range(n):
            if s[i] in d: 
                d[s[i]] -= 1
        if all(v == 0 for v in d.values()): res.append(0)
        for i in range(1, m - n + 1):
            if s[i-1] in p: d[s[i-1]] += 1
            if s[i+n-1] in p: d[s[i+n-1]] -= 1
            if all(v == 0 for v in d.values()): res.append(i)
        return res
    

s = Solution()
print(s.findAnagrams("abab", "ab"))
