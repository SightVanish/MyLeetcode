"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List
# iterate for rowIndex times
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         current, next = [1], []
#         for i in range(rowIndex):
#             for j in range(1, i+1):
#                 next.append(current[j-1]+current[j])
#             current = [1] + next + [1]
#             next = []
#         return current

# in rowIndexth row, each number can be presentes as C(n, k) (in combination presentation)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(res[-1] * (rowIndex-i) // (i+1)) # C(n, k) = C(n, k-1) * (n-k+1)/k
        return res
    

s = Solution()
print(s.getRow(4))
