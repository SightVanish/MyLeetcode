"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        steps = [1, 2]
        for i in range(2, n):
            steps.append(sum(steps))
            steps = steps[1:]
        return steps[-1]


s = Solution()
print(s.climbStairs(2))



