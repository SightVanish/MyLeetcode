def printMatrix(matrix):
    for m in matrix:
        print(m)
    print('')

class Solution:
    def totalNQueens(self, n: int) -> int:
        output = [0]
        board = [[0 for _ in range(n)] for _ in range(n)]
        def updateBoard(x, y, board, disable, modified = []):
            if disable:
                modified = []
                for i in range(n):
                    for (dx, dy) in ((i, i), (i, -i), (-i, i), (-i, -i)):
                        if 0 <= x + dx < n and 0 <= y + dy < n: 
                            if board[x + dx][y + dy] == 0: modified.append((x + dx, y + dy))
                            board[x + dx][y + dy] = 1
                    if board[x][i] == 0: modified.append((x, i))
                    if board[i][y] == 0: modified.append((i, y))
                    board[x][i] = 1
                    board[i][y] = 1
                board[x][y] = 2
                return modified
            else:
                for x, y in modified: board[x][y] = 0

        def backtrack(board, i, j, queens):
            if queens == n: 
                output[0] += 1
            else:
                modified = updateBoard(i, j, board, True)
                for x in range(i + 1, n):
                    for y in range(n):
                        if board[x][y] == 0: backtrack(board, x, y, queens + 1)
                updateBoard(i, j, board, False, modified)
        for i in range(n):
            for j in range(n):
                backtrack(board, i, j, 1)
        return output[0]

s = Solution()
print(s.totalNQueens(4))
