from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if '1' in [i for j in matrix for i in j]: res = 1
        else: return 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1': 
                    matrix[i][j] = 1 + min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1]))
                    res = max(res, matrix[i][j])
        return res * res

s = Solution()
print(s.maximalSquare([["0","1"],["1","0"]]))
