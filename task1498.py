"""
You are given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
"""












from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort() # we can sort input list because we only care which elements are selected and we do not care the sequence
        res = 0
        mod = 10**9 + 7
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[j] > target - nums[i]: 
                j -= 1
            else: 
                res += pow(2, j - i, mod)
                i += 1
        return res % mod

nums = [2,9,4,3,6,9,1,1]
target = 6







s = Solution()
print(s.numSubseq(nums, target))












