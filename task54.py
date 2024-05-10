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


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1 # mark the four corners
        res = []
        while len(res) < len(matrix)*len(matrix[0]):
            # go right
            if up <= down and left <= right:
                for i in range(left, right+1): res.append(matrix[up][i])
                up += 1
            # go down
            if up <= down and left <= right:
                for i in range(up, down+1): res.append(matrix[i][right])
                right -= 1
            # go left
            if up <= down and left <= right:
                for i in range(right, left-1, -1): res.append(matrix[down][i])
                down -= 1
            # go up
            if up <= down and left <= right:
                for i in range(down, up-1, -1): res.append(matrix[i][left])
                left += 1
        return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()
print(s.spiralOrder(matrix))