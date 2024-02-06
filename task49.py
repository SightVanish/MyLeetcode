"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        s = []
        for i in strs: s.append(''.join(sorted(list(i))))
        for i in range(len(s)):
            if s[i] not in res: res[s[i]] = [strs[i]]
            else: res[s[i]].append(strs[i])
        return list(res.values())
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
