from typing import List
# 3 sum closest is difficult -> convert to 2 sum cloeset -> can be solve with 2 pointer
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # handle corner cases
        if len(nums) <= 3: return sum(nums)
        if sum(nums[:3]) > target: return sum(nums[:3])
        if sum(nums[-3:]) < target: return sum(nums[-3:])
        res = sum(nums[:3])
        # convert to 2 sum problem
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target): res = s
                if s < target: l += 1
                else: r -= 1
        return res
            
s = Solution()
print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))