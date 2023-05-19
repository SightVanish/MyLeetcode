"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        return nums1[len(nums1)//2] if len(nums1) % 2 == 1 else nums1[len(nums1)//2-1]/2+nums1[len(nums1)//2]/2
        

s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))


        