from typing import List
# with O(m+n) extra space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(len(matrix[0])): matrix[i][j] = 0
        for i in column:
            for j in range(len(matrix)): matrix[j][i] = 0
        
# with O(1) extra space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fillfirstrow, fillfirstcolumn = False, False
        # use the first element in row/column as indicator
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0: fillfirstrow = True
                    if j == 0: fillfirstcolumn = True
                    matrix[0][j], matrix[i][0] = 0, 0
        # fill the matrix except for the first row/column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0: matrix[i][j] = 0
        # fill the first row/column
        if fillfirstrow:
            for j in range(len(matrix[0])): matrix[0][j] = 0
        if fillfirstcolumn:
            for i in range(len(matrix)): matrix[i][0] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
print(s.setZeroes(matrix))