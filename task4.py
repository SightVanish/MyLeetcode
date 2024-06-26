"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

from typing import List
# brute force: create a new list and sort->O(log(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        return nums1[len(nums1)//2] if len(nums1) % 2 == 1 else nums1[len(nums1)//2-1]/2+nums1[len(nums1)//2]/2

# two pointers -- O(log(min(m, n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1 # make sure length of nums1 <= length of nums2
        m, n = len(nums1), len(nums2)
        i, j = 0, m # let j be m -- meaning all elements can be in the left partition
        while i <= j:
            pivot1 = (i + j) // 2 # mid of nums1
            pivot2 = (m + n + 1) // 2 - pivot1 # to ensure the total left half
            nums1_left = nums1[pivot1 - 1] if pivot1 > 0 else -float('inf')
            nums1_right = nums1[pivot1] if pivot1 < m else float('inf')
            nums2_left = nums2[pivot2 - 1] if pivot2 > 0 else -float('inf')
            nums2_right = nums2[pivot2] if pivot2 < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1: return max(nums1_left, nums2_left) # the left partition contains one element more than the right part
                else: return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right: j = pivot1 - 1
            else: i = pivot1 + 1

s = Solution()
print(s.findMedianSortedArrays(nums1 = [0,0], nums2 = [0,0]))