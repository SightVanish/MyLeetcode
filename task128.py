from typing import List
# worst case: O(n^2)
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
# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_interval = {}
        res = 0
        for i in nums:
            l, r = i, i 
            # check max interval
            if i - 1 in num_interval: l = num_interval[i - 1][0]
            if i + 1 in num_interval: r = num_interval[i + 1][1]
            # update the boundary
            if l in num_interval: num_interval[l] = [min(num_interval[l][0], l), max(num_interval[l][1], r)]
            else: num_interval[l] = [l, r]
            if r in num_interval: num_interval[r] = [min(num_interval[r][0], l), max(num_interval[r][1], r)]
            else: num_interval[r] = [l, r]
            res = max(res, r - l + 1)
        return res


        
s = Solution()
print(s.longestConsecutive(nums = [4,2,2,-4,0,-2,4,-3,-4,-4,-5,1,4,-9,5,0,6,-8,-1,-3,6,5,-8,-1,-5,-1,2,-9,1]))