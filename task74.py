from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        while i <= j:
            mid = (i + j) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target: return True
            elif mid_value < target: i = mid + 1
            else: j = mid - 1
        return False
        
s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 2))
