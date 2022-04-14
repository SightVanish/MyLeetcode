# SUDOKU solver
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''
import time
def isValidSudoku(board) -> bool:
    
    row = [[x for x in y if x != '.'] for y in board]
    col = [[x for x in y if x != '.'] for y in zip(*board)]
    pal = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != '.'] for i in (0, 3, 6) for j in (0, 3, 6)]
    return all(len(set(x)) == len(x) for x in (*row, *col, *pal))

data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
tmp = data
'''
# This solution is implemented with DFS, no purning
# available number
nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
# container for row, col and sub-box
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
sub = [[set() for _ in range(3)] for _ in range(3)]  # 3*3

blank = [] # record which box we need to fill

# deal with the given numbers
for i in range(9):
    for j in range(9):
        if board[i][j] != ".":
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            sub[i//3][j//3].add(board[i][j])
        else:
            blank.append((i,j)) # record location
# deep first search, n is the number of boxes we have filled
def dfs(n):
    if n == len(blank):
        return True
    (i,j) = blank[n] # the box we care now
    numb = nums - row[i] - col[j] - sub[i//3][j//3] # the numbers we can use
    if not numb: # if numb is empty, track back
        return False
    # go through all possible number
    for num in numb:
        board[i][j] = num

        row[i].add(board[i][j])
        col[j].add(board[i][j])
        sub[i//3][j//3].add(board[i][j])

        # go deep, only when all boxes are filled, dfs will return true
        if dfs(n+1): 
            return True

        # for the next row
        row[i].remove(num)
        col[j].remove(num)
        sub[i//3][j//3].remove(num)
# start with n = 0
dfs(0)
print(isValidSudoku(board))
# True
'''



def Sudoku(board:list()):
    def flip(i: int, j: int, digit: int):
        line[i] ^= (1 << digit)
        column[j] ^= (1 << digit)
        block[i // 3][j // 3] ^= (1 << digit)

    def dfs(pos: int):
        # nonlocal valid
        if pos == len(spaces):
            valid = True
            return
        
        i, j = spaces[pos]
        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
        while mask:
            digitMask = mask & (-mask)
            digit = bin(digitMask).count("0") - 1
            flip(i, j, digit)
            board[i][j] = str(digit + 1)
            dfs(pos + 1)
            flip(i, j, digit)
            mask &= (mask - 1)
            if valid:
                return
        
    line = [0] * 9
    column = [0] * 9
    block = [[0] * 3 for _ in range(3)]
    valid = False
    spaces = list()

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                digit = int(board[i][j]) - 1
                flip(i, j, digit)

    while True:
        modified = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                    if not (mask & (mask - 1)):
                        digit = bin(mask).count("0") - 1
                        flip(i, j, digit)
                        board[i][j] = str(digit + 1)
                        modified = True
        if not modified:
            break

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                spaces.append((i, j))

    dfs(0)
a = time.time()

# RUN 100000 times
for i in range(1000000):
    tmp = data
    # the method you us
    Sudoku(tmp)
b = time.time()
# print time consumption
print(b-a)
