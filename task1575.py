"""
You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.
At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.
Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).
Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.
Example 1:
Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
Output: 4
Explanation: The following are all possible routes, each uses 5 units of fuel:
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3
"""

from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[None for _ in range(fuel+1)] for _ in range(n)] # dp[city][remaining fuel]
        def routes(curr, fuel):
            if fuel < 0: return 0
            if dp[curr][fuel] is not None: return dp[curr][fuel]
            nums = 1 if curr == finish else 0
            for i in range(n):
                if i != curr and fuel >= abs(locations[i] - locations[curr]):
                    nums += routes(i, fuel - abs(locations[i] - locations[curr]))
            dp[curr][fuel] = nums
            return nums
        return routes(start, fuel) % (10**9+7)
s = Solution()
print(s.countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5))