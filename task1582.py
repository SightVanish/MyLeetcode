"""
Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""
from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for i in mat:
            if sum(i) == 1:
                if sum([s[i.index(1)] for s in mat]) == 1: res += 1
        return res
