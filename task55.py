from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = [0 for _ in range(n)]
        r[0] = 1
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[j] >= i-j and r[j]:
                    r[i] = 1
                    break
        return r[-1]
    
# a better solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remaining_steps = 0
        for i in nums:
            if remaining_steps < 0: return False
            else: remaining_steps = max(remaining_steps, i)
            remaining_steps -= 1 # move forward
        return True


s = Solution()
print(s.canJump([2,3,1,1,4]))