'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
board = \
[["5","",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# my way--straight forward

# check each row
for i in range(0, len(board)):
    n = []
    for j in range(0, len(board)):
        if board[i][j] != ".":
            if board[i][j] not in n:
                n += [board[i][j]]
            else:
                print("false")
# check each column           
for j in range(0, len(board)):
    n = []
    for i in range(0, len(board)):
        if board[i][j] != ".":
            if board[i][j] not in n:
                n += [board[i][j]]
            else:
                print("false")
# check each sub-box
for i in range(0,3):
    for j in range(0,3):
        a = []
        for m in range(0,3):
            for n in range(0,3):
                if board[i*3+m][j*3+n] != ".":
                    a += [board[i*3+m][j*3+n]]
        b = set(a)
        if len(a) != len(b):
            print("false")
print("true")


# pythonic solution -- simple & clear
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [[x for x in y if x != '.'] for y in board]
        col = [[x for x in y if x != '.'] for y in zip(*board)]
        pal = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != '.'] for i in (0, 3, 6) for j in (0, 3, 6)]
        return all(len(set(x)) == len(x) for x in (*row, *col, *pal))

# note: zip(*board) use * to extract board
# print(list(zip(*board)))
# it is a special trick to get the column of the list