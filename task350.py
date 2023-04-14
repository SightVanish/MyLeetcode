"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d = {}
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in nums2:
            if i in d and d[i] > 0:
                d[i] -= 1
                res.append(i)
        return res