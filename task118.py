"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1]+res[i-1][j])
            res.append(tmp)

        return res




s = Solution()
print(s.generate(5))






