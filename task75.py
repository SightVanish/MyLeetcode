from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for i in nums: count[i] += 1
        for i in range(count[0]): nums[i] = 0
        for i in range(count[1]): nums[count[0] + i] = 1
        for i in range(count[2]): nums[count[0] + count[1] + i] = 2
