"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
"""
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        for i in range(len(arr)-n):
            if arr[i] == arr[i+n]: return arr[i]

s = Solution()
print(s.findSpecialInteger([1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))