"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
"""
from typing import List
import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                avg = [p for p in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)] if p[0]>=0 and p[1]>=0 and p[0]<m and p[1]<n]
                avg = [img[p[0]][p[1]] for p in avg]
                res[i][j] = math.floor(sum(avg) / len(avg))
        return res
    

s = Solution()
print(s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))