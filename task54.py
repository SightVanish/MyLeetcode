from typing import List

class Solution:
    def rotateMatrix(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            return []

        new_matrix = []
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][len(matrix[0]) - i - 1])
            new_matrix.append(tmp)
        return new_matrix

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while len(matrix) >= 1:
            ans += matrix.pop(0)
            matrix = self.rotateMatrix(matrix)
            # matrix = list(zip(*matrix))[::-1]
        return ans


def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end = ' ')
        print('')
    print('')

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()

printMatrix(matrix)
matrix = s.rotateMatrix(matrix)
printMatrix(matrix)