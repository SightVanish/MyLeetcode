from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def convertIndex(label):
            label -= 1
            if (label // n) % 2 == 0: return n - 1 - label // n, label % n
            else: return n - 1 - label // n, n - 1 - label % n
        visited, queue = set(), [(1, 0)] # starting at 1 with 0 step
        # run a BFS to find the shallowest ending node
        while queue:
            curr, step = queue[0]
            queue = queue[1:]
            r, c = convertIndex(curr)
            if board[r][c] != -1: curr = board[r][c]
            if curr == n * n: return step
            for dice in range(1, 7):
                dest = curr + dice
                if dest <= n * n and dest not in visited:
                    visited.add(dest)
                    queue.append((dest, step + 1))
        return -1