"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
"""















class Solution:
    def addDigits(self, num: int) -> int:

        num = str(num)
        while len(num) > 1:
            num = str(sum(map(lambda x: int(x), num)))
        return int(num)
s = Solution()
print(s.addDigits(0))


