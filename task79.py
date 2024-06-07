from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def search(x, y, visited, s, index):
            if s == word: return True
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == word[index] and (x + dx, y + dy) not in visited:  
                    visited.add((x + dx, y + dy)) 
                    if search(x + dx, y + dy, visited, s + board[x + dx][y + dy], index + 1): return True
                    visited.remove((x + dx, y + dy))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(i, j, set([(i, j)]), board[i][j], 1): return True
        return False


s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))