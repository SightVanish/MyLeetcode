class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = [i for i in s.lower() if i in alphabet]
        return list(reversed(s)) == s

# two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not s[l].isalnum(): l += 1
            while r > -1 and not s[r].isalnum(): r -= 1
            if l < r and s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True


s = Solution()
print(s.isPalindrome(s = ".,"))

        