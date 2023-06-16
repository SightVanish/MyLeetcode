"""
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.
For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
Since the answer may be very large, return it modulo 109 + 7.
Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
"""

from typing import List
from math import factorial
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def combination(m, n):
            # select m items from items without order -> mix left tree and right tree without breaking internal order
            return factorial(n) // (factorial(n-m) * factorial(m))

        def permuation(nums):
            if len(nums) <= 2: return 1
            left_tree = [i for i in nums if i < nums[0]]
            right_tree = [i for i in nums if i > nums[0]]
            return combination(len(left_tree), len(left_tree) + len(right_tree)) * permuation(left_tree) * permuation(right_tree)

        return (permuation(nums) - 1) % (10**9 + 7)


s = Solution()
print(s.numOfWays([2,1,3]))
