"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        m, n = nums[0], nums[0] - 1
        res = []
        for i in range(len(nums)):
            if nums[i] == n + 1:
                n = nums[i]
            else:
                if m < n:
                    res.append('{0}->{1}'.format(m, n))
                else:
                    res.append(str(m))
                m, n = nums[i], nums[i]
        if m < n:
            res.append('{0}->{1}'.format(m, n))
        else:
            res.append(str(m))
        return res


s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))


