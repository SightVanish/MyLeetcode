from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = [1], [1], []
        temp = 1
        for i in range(0, len(nums)-1):
            temp *= nums[i]
            prefix.append(temp)
        temp = 1
        for i in range(len(nums)-1, 0, -1):
            temp *= nums[i]
            suffix.append(temp)
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[-i-1])
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))