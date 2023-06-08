"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binary_a, binary_b, binary_c = bin(a)[2:].rjust(32, '0'), bin(b)[2:].rjust(32, '0'), bin(c)[2:].rjust(32, '0')
        # print(binary_a, binary_b, binary_c)
        res = 0
        for i in range(32):
            if (int(binary_a[i]) or int(binary_b[i])) != int(binary_c[i]):
                if binary_c[i] == '1': res += 1
                else:
                    if (int(binary_a[i]) and int(binary_b[i])) == 1: res += 2
                    else: res += 1
        return res
    

s = Solution()
print(s.minFlips(6,783,863))
