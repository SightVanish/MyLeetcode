"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
     
        steps = {-1: 0, 0: 0}
        def climb(n):
            if n in steps: return steps[n]
            steps[n] = min(climb(n-1)+cost[n], climb(n-2)+cost[n-1])
            return steps[n]
        climb(len(cost)-1)
        return steps[len(cost)-1]

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))