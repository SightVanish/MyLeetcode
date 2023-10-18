"""
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.
nums is considered continuous if both of the following conditions are fulfilled:
- All elements in nums are unique.
- The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums) # lenth of input
        nums=sorted(set(nums))
        res = n
        for i, start in enumerate(nums):
            # try each element as the starting element
            expected_end = start + n - 1
            l, r = i, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2 
                if nums[mid] == expected_end:
                    l = mid + 1
                    break
                if nums[mid] <= expected_end: l = mid + 1
                else: r = mid - 1
            res = min(res, n - (l - i))
        return res


s = Solution()
print(s.minOperations([1,2,3,5,6]))
        