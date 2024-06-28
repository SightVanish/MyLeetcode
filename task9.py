# mine
class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = x #i is used for iteration
        r = 0 #r is used for result
        if x < 0: return False
        while i > 0:
            r = r*10 + i%10
            i = (int)(i/10) # note that there is no variable type in python, so you need to pay attention to it
        if x == r: return True
        else: return False

s = Solution()
f = s.isPalindrome(-12321)
print(f)