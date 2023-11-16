"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
"""
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # convert to integer
        nums = [int(i, 2) for i in nums]
        for i in range(2**len(nums)):
            if i not in nums: 
                b = bin(i)[2:]
                return '0'*(len(nums) - len(b)) + b

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        # make sure res if different at least one bit with each string
        for i in range(len(nums)): res += '0' if nums[i][i] == '1' else '1'
        return res

s = Solution()
print(s.findDifferentBinaryString(["01","10"]))




        