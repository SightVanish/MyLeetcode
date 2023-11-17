"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
"""

from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = [nums[i] + nums[len(nums)-i-1] for i in range(len(nums))]
        return max(nums)

s = Solution()
print(s.minPairSum([3,5,4,2,4,6]))
# for input: [3,5,4,2,4,6]
# sorted: [2, 3, 4, 4, 5, 6]
# we can get: 4 + 4 is the answer
# proof: if there exist a combination such that all pairsum < 4 + 4 (not even equal)
#        take 3 as pivot: 3 cannot combine with 5 -- as we already make sure 3 + 5 <= 4 + 4
#        in order to make sure all pairsum < 4 + 4: 5 must combine with the left part of 3, which is [2]
#        keep doing so and we will found there is no element left for 6 (the biggest element) to combine -- contradiction