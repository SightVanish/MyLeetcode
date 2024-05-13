from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starting = [] # the starting number of the consecutive list
        res = 0
        for n in nums:
            if n-1 not in nums: starting.append(n)
        for n in starting:
            temp = 0
            while n in nums:
                temp += 1
                n += 1
            res = max(res, temp)
        return res


        
s = Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))