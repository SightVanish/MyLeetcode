"""
Alice plays the following game, loosely based on the card game "21".
Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
Alice stops drawing numbers when she gets k or more points.
Return the probability that Alice has n or fewer points.
Answers within 10-5 of the actual answer are considered accepted.
Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
"""

# Dynamic programming + sliding window
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >=  k+ maxPts: return 1 # definitely Alice will win

        p = [0 for _ in range(n+1)] # possibilities of getting points form 0 to n
        p[0] = 1 # the possibility of getting 0 points is 1
        sumWidowns, res = 1.0, 0 # sum: sum of possibilities in the sliding window; res: sum of possibilities of getting <= n points
        
        for i in range(1, n+1):
            p[i] = sumWidowns/maxPts # possibility of getting i points: P[i] = sum(P[k] * draw(i-k)) = sum(P[k])/draw a certain point
            
            if i < k:
                # keep drawing, it is not time to stop
                sumWidowns += p[i]
            if i >= k:
                # stop drawing, it is the possible to win the game
                res += p[i]
            
            if i >= maxPts:
                # only maintain a sliding window of lenth maxPts
                # we only stand a chance to get point i from the window
                sumWidowns -= p[i - maxPts]
        return res

s = Solution()
print(s.new21Game(0, 0, 1))