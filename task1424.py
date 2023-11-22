"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
"""

from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = [[]] # consider using a dict{} instead to improve performance
        res = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j < len(d): d[i+j].append(nums[i][j])
                else: d.append([nums[i][j]])
        for i in d: res += i[::-1]
        return res


s = Solution()
print(s.findDiagonalOrder([[1,2,3,4,5,6]]))     
