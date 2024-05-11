from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbours(i, j):
            neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            res = 0
            for dr, dc in neighbours:
                if -1 < i + dr < len(board) and -1 < j + dc < len(board[0]):
                    if board[i + dr][j + dc] == 1 or board[i + dr][j + dc] == 2:
                        res += 1
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = get_neighbours(i, j)
                if board[i][j] == 1 and (n == 2 or n == 3): board[i][j] = 2
                if board[i][j] == 0 and n == 3: board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2 or board[i][j] == 3: board[i][j] = 1
                else: board[i][j] = 0


s = Solution()
print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

                
        