"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letters = {'2':['a', 'b', 'c'],
                   '3':['d', 'e', 'f'],
                   '4':['g', 'h', 'i'],
                   '5':['j', 'k', 'l'],
                   '6':['m', 'n', 'o'],
                   '7':['p', 'q', 'r', 's'],
                   '8':['t', 'u', 'v'],
                   '9':['w', 'x', 'y', 'z']}
        res = []
        def combinations(prefix='', digits=''):
            if digits == '': return
            if len(digits) == 1:
                for l in letters[digits[0]]:
                    res.append(prefix + l)
            else:
                for l in letters[digits[0]]:
                    combinations(prefix+l, digits[1:])
        combinations(prefix='', digits=digits)
        return res

s = Solution()
print(s.letterCombinations("23"))