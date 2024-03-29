"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = sum([mat[i][i] for i in range(len(mat))])
        res += sum([mat[i][-1-i] for i in range(len(mat))])
        if len(mat) % 2:
            res -= mat[len(mat)//2][len(mat)//2]
        return res
    