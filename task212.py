from typing import List
from collections import deque
# my solution with bfs
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie for word
        wordList = {}
        for w in words:
            curr = wordList
            for l in w:
                if l not in curr: curr[l] = {}
                curr = curr[l]
            curr['end'] = {}
        res = []
        m, n, l = len(board), len(board[0]), max([len(i) for i in words])
        for i in range(m):
            for j in range(n):
                if board[i][j] not in wordList: continue
                queue = deque()
                visited = set()
                if board[i][j] in wordList: queue.append((board[i][j], i, j, wordList[board[i][j]], visited))
                while queue:
                    curr, x, y, currList, visited = queue.popleft()
                    visited.add((x, y))
                    if 'end' in currList: res.append(curr)
                    if len(curr) < l:
                        if x > 0 and board[x-1][y] in currList and (x-1, y) not in visited: queue.append((curr+board[x-1][y], x-1, y, currList[board[x-1][y]], visited.copy()))
                        if x < m-1 and board[x+1][y] in currList and (x+1, y) not in visited: queue.append((curr+board[x+1][y], x+1, y, currList[board[x+1][y]], visited.copy()))
                        if y > 0 and board[x][y-1] in currList and (x, y-1) not in visited: queue.append((curr+board[x][y-1], x, y-1, currList[board[x][y-1]], visited.copy()))
                        if y < n-1 and board[x][y+1] in currList and (x, y+1) not in visited: queue.append((curr+board[x][y+1], x, y+1, currList[board[x][y+1]], visited.copy()))
        return list(set(res))

# a better solution with dfs
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordList = {}
        res = []
        for w in words:
            curr = wordList
            for l in w:
                if l not in curr: curr[l] = {}
                curr = curr[l]
            curr['end'] = w

        def dfs(x, y, trie):
            curr = board[x][y]
            if curr not in trie: return
            trie = trie[curr]
            if 'end' in trie: res.append(trie.pop('end'))
            board[x][y] = '*' # mark this position as visited
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] in trie: dfs(new_x, new_y, trie)
            board[x][y] = curr # restore the position
       
        m, n, l = len(board), len(board[0]), max([len(i) for i in words])
        for i in range(m):
            for j in range(n):
                if board[i][j] in wordList: dfs(i, j, wordList)
        return res


s = Solution()
print(s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain","hklf", "hf"]))
