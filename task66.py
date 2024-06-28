from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry: digits[i] += 1
            if digits[i] > 9: digits[i] = 0
            else: 
                carry = 0
                break
        return [[1]] + digits if carry else digits
