from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        d = [float('inf') for _ in range(n)]
        d[0] = 0
        for i in range(n):
            for j in range(i):
                if nums[j] >= i-j: d[i] = min(d[i], d[j]+1)
        return d[-1]

# a better solution: farthers is the farthest position we can reach; steps is the steps to reach the farthest positoin
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        farthest, steps, end = 0, 0, 0
        for i in range(len(nums)):
            farthest = max(farthest, i+nums[i])
            print(farthest, steps)
            if farthest >= len(nums)-1: return steps + 1
            # reach the fartherest place within this step (explore all node in this layer)
            if i == end:
                end = farthest
                steps += 1 

s = Solution()
print(s.jump([2,3,1,1,4]))