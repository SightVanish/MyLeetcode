from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def expand(i, j):
            # expand from this node to find all adjacent points
            stack = [[i, j]]
            while stack:
                i, j = stack.pop()
                board[i][j] = 'V'
                if i > 0 and board[i - 1][j] == 'O': stack.append([i - 1, j])
                if i < m - 1 and board[i + 1][j] == 'O': stack.append([i + 1, j])
                if j > 0 and board[i][j - 1] == 'O': stack.append([i, j - 1])
                if j < n - 1 and board[i][j + 1] == 'O': stack.append([i, j + 1])
        for i in range(m):
            if board[i][0] == 'O': expand(i, 0)
            if board[i][n - 1] == 'O': expand(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O': expand(0, j)
            if board[m - 1][j] == 'O': expand(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'V': board[i][j] = 'O'
                

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()
print(s.solve(board))
