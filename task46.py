"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def order(prefix, remainder):
            if len(remainder) == 0:
                res.append(prefix)
            else:
                for i in range(len(remainder)): order(prefix + [remainder[i]], remainder[:i]+remainder[i+1:])
        order([], nums)        
        return res

s = Solution()
print(s.permute([1,2,3]))
