"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
"""


from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]: return letters[0]

        i, j = 0, len(letters) - 1
        while i < j:
            mid = (i + j) // 2
            if target >= letters[mid]: i = mid + 1
            else: j = mid # since we want to find the first element > target, mid may be the one, we cannot skip mid
        return letters[i]
s = Solution()
letters = ["x","x","y","y"]; target = "z"
print(s.nextGreatestLetter(letters, target))

        