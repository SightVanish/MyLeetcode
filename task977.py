from typing import List
# O(n) space, O(nlgn) time
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [abs(i) ** 2 for i in nums]

# O(n) space, O(n) time
# two pointer
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums) and nums[i] < 0: i += 1
        j = i - 1
        while i < len(nums) and j > -1:
            if nums[i] < -nums[j]: 
                res.append(nums[i] ** 2)
                i += 1
            else: 
                res.append(nums[j] ** 2)
                j -= 1
        while i < len(nums):
            res.append(nums[i] ** 2)
            i += 1
        while j > -1:
            res.append(nums[j] ** 2)
            j -= 1
        return res
