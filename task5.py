class Solution:
    def getPalindrome(self, s, i, j):
        while i >=0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-1 # you can not return i, j here
    def longestPalindrome(self, s: str) -> str:
        i, j = 0, 0
        for center in range(len(s)):
            # there are two situation for Palindrome
            l1, r1 = self.getPalindrome(s, center, center)
            l2, r2 = self.getPalindrome(s, center, center+1)
            if r1-l1 > j-i:
                i, j = l1, r1
            if r2-l2 > j-i:
                i, j = l2, r2
        return s[i:j+1] # note: j+1 here

