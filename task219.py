from typing import List
# sliding window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        history = {}
        for i in range(len(nums)):
            if nums[i] in history and i - history[nums[i]] <= k: return True
            history[nums[i]] = i
        return False

s = Solution()
print(s.containsNearbyDuplicate([99,99], 2))