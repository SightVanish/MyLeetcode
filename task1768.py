"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ''
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        res += word1[i:] + word2[j:]
        return res
    
    def mergeAlternately(self, w1, w2):
        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue='')) # consider zip_longest

s = Solution()
print(s.mergeAlternately("abc", "pqr"))
