from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # [row, col]
        res = [[0] * n for _ in range(n)]
        direct = 0 # index of direction 
        pos = [0, 0]
        for i in range(1, n * n + 1):

            # print(direction[direct])
            # print(res)

            res[pos[0]][pos[1]] = i
            new_pos = [pos[0] + direction[direct][0], pos[1] + direction[direct][1]]
            if new_pos[0] not in range(0, n) or new_pos[1] not in range(0, n) or res[new_pos[0]][new_pos[1]] != 0:
                # change direction
                direct = (direct + 1) % 4
            pos = [pos[0] + direction[direct][0], pos[1] + direction[direct][1]]
        return res
s = Solution()

print(s.generateMatrix(3))