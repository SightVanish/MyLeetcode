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
        steps = {}
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        # def climb(i: int):
        #     if i in steps: return steps[i]
        #     climb(i-1)
        #     climb(i-2)
        #     steps[i] = steps[i-1] + steps[i-2]
        # climb(n)
        # return steps[n]
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]

s = Solution()
print(s.climbStairs(3))



