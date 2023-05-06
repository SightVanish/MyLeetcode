"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        i, j = 0,  k - 1
        for l in s[:k]:
            if l in vowel:
                curr += 1
        res = curr
        while j < len(s) - 1:
            if s[i] in vowel: 
                curr -= 1
            if s[j + 1] in vowel:
                curr += 1
            res = max(res, curr)
            i += 1
            j += 1
        return res

