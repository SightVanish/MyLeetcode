from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def convertIndex(label):
            label -= 1
            if (label // n) % 2 == 0: return n - 1 - label // n, label % n
            else: return n - 1 - label // n, n - 1 - label % n
        
        
