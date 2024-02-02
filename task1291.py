"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(1, 11-i):
                c = int(''.join([str(j+m) for m in range(i)]))
                if low <= c <= high: res.append(c)
        return res


# since sequential integer is limited, one possible solution is to generate all possible seqential integer --> O(1) time complexity
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            c = i
            for j in range(i+1, 10):
                c = c * 10 + j
                if low <= c <= high: res.append(c)
        res.sort() # since length of res is limited, sorting takes O(1).
        return res