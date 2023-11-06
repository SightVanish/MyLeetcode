"""
Given an integer array arr of distinct integers and an integer k.
A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
Return the integer which will win the game.
It is guaranteed that there will be a winner of the game.
"""
from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        winner = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if winner > arr[i]: win += 1
            else:
                winner = arr[i]
                win = 1
            if win == k: return winner
        return winner # what is left must be the largest one


arr = [1,25,35,68,42,37]
k = 5
s = Solution()
print(s.getWinner(arr,k))