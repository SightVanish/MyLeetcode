"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.
Return the maximum number of coins that you can have.
"""
# intuitive proof:
# first round: 1 2 3 4 5 6 7 8 9 -- cannot pick 9 anyway, so we can only pick from 1 to 8
#              whatever we pick, we cannot pick the max item left -> so to maximize output, we pick 8
#              we leave the smallest one for Bob (obviously, no other option can be better than this)
# second round: 2 3 4 5 6 7 -- same situation as the first round

from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[-2:len(piles)//3-1:-2])

piles = [9,8,7,6,5,1,2,3,4]
s = Solution()
print(s.maxCoins(piles))