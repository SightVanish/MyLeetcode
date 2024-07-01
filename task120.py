from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

s = Solution()
print(s.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))