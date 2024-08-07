from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0: return 
        for i in range(len(nums)//2):
            nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range(k, (len(nums)+k)//2):
            nums[i], nums[len(nums)+k-i-1] = nums[len(nums)+k-i-1], nums[i]

# a simple way using python would be: nums[:] = nums[-k:]+nums[:len(nums)-k]            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0: return 
        nums[:] = nums[-k:]+nums[:len(nums) - k]


s = Solution()
print(s.rotate([1,2], 2))


