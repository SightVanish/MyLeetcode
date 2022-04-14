# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# mine
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        i = x #i is used for iteration
        r = 0 #r is used for result
        if x < 0:   
            return False
        while i > 0:
            r = r*10 + i%10
            i = (int)(i/10) # note that there is no variable type in python, so you need to pay attention to it
        if x == r:
            return True
        else:
            return False

s = Solution()
f = s.isPalindrome(-12321)
print(f)