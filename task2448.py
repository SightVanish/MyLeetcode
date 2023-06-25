"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
You can do the following operation any number of times:
Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].
Return the minimum total cost such that all the elements of the array nums become equal.
Example 1:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
"""


from typing import List
# Time Complexity: O(nlgn); Space Complexity: O(n)
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        nums, cost = zip(*sorted(zip(nums, cost)))
        # left2right[i]: cost of increasing all nums[:i] to nums[i]
        # right2left[i]: cost of decreasing all nums[i+1:] to nums[i]
        left2right, right2left = [0] * n, [0] * n
        left_cost, right_cost = cost[0], cost[-1]
        for i in range(1, n):
            left2right[i] = left2right[i-1] + (nums[i] - nums[i-1]) * left_cost
            left_cost += cost[i]
            right2left[n-i-1] = right2left[n-i] + (nums[n-i] - nums[n-i-1]) * right_cost
            right_cost += cost[n-i-1]
        res = [left2right[i] + right2left[i] for i in range(n)]
        return min(res)

s = Solution()
print(s.minCost(nums = [1,3,5,2], cost = [2,3,1,14]))
            
"""
proof: the final equal value v could be in nums
1. min(nums) <= v <= max(nums)
2. sort nums
3. assume nums[i] < v < nums[i+1]
4. if move v to nums[i+1], 
   change of cost = sum(cost[:i])*(nums[i+1]-v) - sum(cost[i+1:])*(nums[i+1]-v)
                  = sum(cost[:i] - sum(cost[i+1:]))*(nums[i+1]-v)
5. if move v to nums[i],
   change of cost = sum(sum(cost[i+1:]) - sum(cost[:i]))*(nums[i+1]-v)
6. if sum(cost[i+1:]) == sum(cost[:i]): move either way
   else: we can always find a way to decrease total cost
"""
